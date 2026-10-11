"""Compare the rebuild with the oracle, document by document (REBUILD_DESIGN.md §8.2).

1. The oracle lists the corpus: each judged document, its phase and its priors.
2. The oracle converts every document and prior into the Machine-block form, in a mirror tree.
3. The oracle judges each original; the rebuild judges each conversion. Both use the working
   tree's declared rules and the frozen composition.
4. For each document: the verdict must be identical, and so must every finding's code, location
   and detail. `CODE_MAP` is where a declared divergence would translate a retired code; it is empty
   until a milestone declares one in the charter.

    python scripts/rebuild/compare.py [--keep DIR]

Exit 0 when every document agrees, 1 otherwise.
"""
from __future__ import annotations

import json
import os
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


def findings(result: dict) -> Counter:
    return Counter((CODE_MAP.get(f["rule"], f["rule"]), f["where"], f["detail"])
                   for f in result.get("findings", []))


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
            if a.get("rules_evaluated") != b.get("rules_evaluated"):
                problems.append(f"rules evaluated {a.get('rules_evaluated')} → {b.get('rules_evaluated')}")
            fa, fb = findings(a), findings(b)
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
