"""Construction acceptance — render CR-1's artifacts from its dossier and compare with what was built.

CR-1's twenty-five artifacts were hand-authored, compiled, and validated 9/9 against acceptance
criteria the business declared before any design existed. That makes them the acceptance corpus for
the Construction lifecycle, and it makes this comparison the only test that matters: **a design at
100% Construction Completeness should determine them.**

Every difference is one of exactly two things, and the difference itself says which:

    a generator bug          the design states the fact and the renderer got it wrong
    a design insufficiency   the design does not state the fact at all

The second is the more valuable finding. Construction Completeness measures whether the facts the
probe *knows to ask about* are determined; this measures whether the artifact can actually be
rebuilt, which is the question the probe's fact list can only approximate.

Comparison is semantic and scoped to the Machine block. An artifact's prose is human narrative that
no register determines, and comparing text would report a hundred differences about paragraphs
nobody claims are generated.

Run:  python scripts/testbed/construction_acceptance.py [dossier] [registry]
Exit: 0 when every artifact matches, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from transformation.build.render import render_all, bare
from transformation.design.read import read_seed

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
DOSSIER = WORKSPACE / "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog"
REGISTRY = WORKSPACE / "business_domains/book_library_mgmt/registry"

MACHINE = re.compile(r"```yaml\n(.*?)\n```", re.S)


def registers(path: Path) -> dict[str, list[dict]]:
    doc = read_seed(path)
    out: dict[str, list[dict]] = {}
    for entry in doc.registers:
        block = doc.register(entry["id"])
        if block and block.table:
            out[entry["id"]] = block.table.rows
    return out


def built(registry: Path) -> dict[str, dict]:
    out = {}
    for path in sorted(registry.rglob("*.md")):
        found = MACHINE.search(path.read_text(encoding="utf-8"))
        if not found:
            continue
        machine = yaml.safe_load(found.group(1))
        if isinstance(machine, dict) and "fqdn" in machine:
            out[bare(machine["fqdn"])] = machine
    return out


# Keys that are documentation even inside the Machine block. Two tests decide membership, and both
# are empirical rather than aesthetic:
#
#   nothing consumes it   `isolation`, `resolution`, `storage_roots` and `extensions` appear in no
#                         compiler, assembler or runtime read path. `isolation.rules` restates in
#                         prose what `entity_stores` already says structurally.
#   it varies by author   the built corpus carries a field `description` on some fields and not
#                         others; a governed fact is present or absent by rule.
#
# A key that something reads is governed however prose-like it looks — `parameters` on a runtime
# binding is a list of names an assertion checks, so it stays in.
DOCUMENTATION = {"description", "isolation", "resolution", "storage_roots", "extensions"}


def diff(expected, actual, path: str = "") -> list[str]:
    """Every leaf where two Machine blocks disagree, addressed by dotted path."""
    if isinstance(expected, dict) and isinstance(actual, dict):
        out = []
        for key in sorted(set(expected) | set(actual)):
            if key in DOCUMENTATION:
                continue
            here = f"{path}.{key}" if path else key
            if key not in actual:
                out.append(f"{here}: not rendered")
            elif key not in expected:
                out.append(f"{here}: rendered but not built")
            else:
                out += diff(expected[key], actual[key], here)
        return out
    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            return [f"{path}: {len(actual)} rendered, {len(expected)} built"]
        out = []
        for i, (e, a) in enumerate(zip(expected, actual)):
            out += diff(e, a, f"{path}[{i}]")
        return out
    if expected != actual:
        return [f"{path}: rendered {actual!r}, built {expected!r}"]
    return []


def main() -> int:
    dossier = Path(sys.argv[1]) if len(sys.argv) > 1 else DOSSIER
    registry = Path(sys.argv[2]) if len(sys.argv) > 2 else REGISTRY

    p7 = registers(next(dossier.glob("p7_*.md")))
    p8 = registers(next(dossier.glob("p8_*.md")))
    rendered = {bare(a["machine"]["fqdn"]): a for a in render_all(p7, p8)}
    reference = built(registry)

    print(f"construction acceptance — {len(rendered)} rendered against {len(reference)} built\n")

    failures, total_diffs = 0, 0
    for code in sorted(reference):
        if code not in rendered:
            print(f"  MISS  {code:<44} rendered nothing")
            failures += 1
            continue
        differences = diff(reference[code], rendered[code]["machine"])
        total_diffs += len(differences)
        if not differences:
            print(f"  OK    {code}")
            continue
        failures += 1
        print(f"  DIFF  {code:<44} {len(differences)} field(s)")
        for line in differences[:6]:
            print(f"          {line}")
        if len(differences) > 6:
            print(f"          … {len(differences) - 6} more")

    extra = sorted(set(rendered) - set(reference))
    for code in extra:
        print(f"  EXTRA {code:<44} rendered, never built")
        failures += 1

    print(f"\n  {len(reference) - failures}/{len(reference)} artifacts reproduced"
          f"   ({total_diffs} field difference(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
