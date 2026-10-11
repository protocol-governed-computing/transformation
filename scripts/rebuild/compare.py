"""Compare the rebuild with the oracle, document by document (REBUILD_DESIGN.md §8.2).

1. The oracle lists the corpus: each judged document, its phase and its priors.
2. The oracle converts every document and prior into the Machine-block form, in a mirror tree.
3. The oracle judges each original; the rebuild judges each conversion. Both use the working
   tree's declared rules and the frozen composition.
4. For each document: the verdict must be identical, and so must every finding's code, location
   and detail, read through the normalisations the charter's divergences declare. The number of
   rules evaluated is not compared: `declarations.py` owns the rule sets. `CODE_MAP` is where a declared divergence would translate a retired code; it is empty
   until a milestone declares one in the charter.

    python scripts/rebuild/compare.py [--keep DIR]

Exit 0 when every document agrees, 1 otherwise.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

REBUILD = Path(__file__).resolve().parents[2]
ORACLE = Path.home() / "pgc-oracle" / "transformation"
SNAPSHOT = Path.home() / "pgc-oracle" / "snapshot"
HERE = Path(__file__).resolve().parent

CODE_MAP: dict[str, str] = {}
# M3.4a-1: procedures restated as constraints. The general kind words the finding its own way, so
# these are compared by code and place.
RESTATED_AS_CONSTRAINTS = ("BELIEF_STATED_AS_FACT", "STORE_PATH_FORMAT_MISMATCH", "BINDING_SOURCE_UNROOTED",
                           "BINDING_SOURCE_MALFORMED")


def _where(finding: dict) -> str:
    """The oracle's place string. M3.4c: the rebuild places a finding by a structured locator — the
    register, the row's ordinal or key, the field. Read back, it is the register, then `row <n>` for
    an ordinal or the key itself. The field is not compared: the oracle never stated it."""
    if "locator" not in finding:
        return finding["where"]
    register, row = finding["locator"]["register"], finding["locator"]["row"]
    if row is None:
        return register
    return f"{register} row {row}" if isinstance(row, int) else f"{register} {row}"


def _normalised(finding: dict, side: str) -> tuple | None:
    """A finding as the comparison reads it, after the divergences the charter declares (§8).

    - M2-2: a missing column is reported per row, not per register. Both sides read as the register
      and the column, once.
    - M3.3-6: a governed hole names the column by its key, not its heading. Both read as the
      register and the row, with the detail's column dropped.
    - M3.4a-2: the two ordinal rules are one. The oracle's row rule reads as the ordinal rule, and
      an unresolved ordinal is compared once per row.
    - M3.4a-1: a procedure restated as a constraint words its finding as the general kind does.
      Compared by code and place.
    - M3.4c: the rebuild names a finding's kind `code` and places it by a locator. Both read as the
      oracle's `rule` and `where`.
    - M3.3b-1: a citation is a mapping, so an unresolved one is shown as the mapping. Both read as
      the register and the row. A citation that does not structure is refused by its type, which
      reads as the unresolved citation it was.
    """
    raw = finding.get("code", finding["rule"])
    code, where, detail = CODE_MAP.get(raw, raw), _where(finding), finding["detail"]
    if code == "CITATION_ROW_UNRESOLVED":
        code = "CITATION_ORDINAL_UNRESOLVED"
    if code == "CITATION_ORDINAL_UNRESOLVED":
        return (code, where, "")
    if code == "CELL_NOT_OF_TYPE" and detail.startswith(("'Source Finding'", "'Origin'")):
        code = "SOURCE_FINDING_UNRESOLVED"
    if code in ("SOURCE_FINDING_UNRESOLVED",) + RESTATED_AS_CONSTRAINTS:
        return (code, where, "")
    register = where.split(" row ")[0]
    if code == "REGISTER_COLUMN_MISSING":
        column = re.search(r"required column '([^']+)' absent", detail)
        return (code, register, column.group(1) if column else detail)
    if code == "REGISTER_CELL_UNRESOLVED":
        return (code, where, re.sub(r"^'[^']*' ", "", detail))
    return (code, where, detail)


def oracle(*args: str, stdin: str | None = None) -> str:
    env = dict(os.environ, PYTHONPATH=str(ORACLE))
    done = subprocess.run([sys.executable, *args], cwd=ORACLE, env=env, input=stdin,
                          capture_output=True, text=True)
    if done.returncode:
        raise SystemExit(f"oracle {args[0]} failed:\n{done.stderr[-3000:]}")
    return done.stdout


def rebuild(*args: str, stdin: str) -> str:
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    done = subprocess.run([sys.executable, *args], cwd=REBUILD, env=env, input=stdin,
                          capture_output=True, text=True)
    if done.returncode:
        raise SystemExit(f"rebuild {args[0]} failed:\n{done.stderr[-3000:]}")
    return done.stdout


def _empty_registers(path: Path) -> set[str]:
    """The registers a converted document carries with no rows: declared empty, or stating nothing."""
    from transformation.design.read import parse_text

    _, _, registers = parse_text(path.read_text(encoding="utf-8"))
    return {r["id"] for r in registers if r["value"] is None or r["value"] == []}


def findings(result: dict, side: str) -> Counter:
    listed = result.get("findings", [])
    seen = Counter(_normalised(f, side) for f in listed)
    # A per-row missing column collapses to one finding per register and column, and an unresolved
    # ordinal to one finding per row (M3.4a-2).
    return Counter({k: (1 if k[0] in ("REGISTER_COLUMN_MISSING", "CITATION_ORDINAL_UNRESOLVED") else v)
                    for k, v in seen.items()})


def main(argv: list[str]) -> int:
    keep = Path(argv[argv.index("--keep") + 1]) if "--keep" in argv else None
    mirror = keep or Path(tempfile.mkdtemp(prefix="pgc_mirror_"))
    cases = json.loads(oracle(str(HERE / "cases.py")))

    paths = sorted({c["doc"] for c in cases} | {p for c in cases for p in c["priors"].values()})
    pairs = [x for p in paths for x in (str(ORACLE / p), str(mirror / p))]
    oracle(str(HERE / "convert.py"), *pairs)

    payload = json.dumps(cases)
    was = json.loads(oracle(str(HERE / "judge.py"), str(SNAPSHOT), str(ORACLE), stdin=payload))
    now = json.loads(rebuild(str(HERE / "judge.py"), str(SNAPSHOT), str(mirror), stdin=payload))

    differ = 0
    for before, after in zip(was, now):
        a, b = before["result"], after["result"]
        problems = []
        if "error" in a or "error" in b:
            problems.append(f"error — oracle: {a.get('error', 'ok')[:300]} / rebuild: {b.get('error', 'ok')[:300]}")
        else:
            if a["verdict"] != b["verdict"]:
                problems.append(f"verdict {a['verdict']} → {b['verdict']}")
            fa, fb = findings(a, 'oracle'), findings(b, 'rebuild')
            # M2-2: a register with no rows has no column to miss.
            empty = _empty_registers(mirror / before["doc"])
            fa = Counter({k: v for k, v in fa.items()
                          if not (k[0] == "REGISTER_COLUMN_MISSING" and k[1] in empty)})
            for f in sorted((fa - fb).elements()):
                problems.append(f"only oracle:  {f[0]} @ {f[1]} — {f[2][:160]}")
            for f in sorted((fb - fa).elements()):
                problems.append(f"only rebuild: {f[0]} @ {f[1]} — {f[2][:160]}")
        if problems:
            differ += 1
            print(f"\n{before['doc']}")
            for p in problems:
                print(f"   {p}")

    total = len(cases)
    findings_total = sum(len(r["result"].get("findings", [])) for r in was)
    if differ:
        print(f"\nCOMPARISON FAILED — {differ} of {total} documents differ")
        return 1
    print(f"COMPARISON PASSED — {total} documents, {findings_total} oracle findings, "
          f"identical verdicts and findings")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
