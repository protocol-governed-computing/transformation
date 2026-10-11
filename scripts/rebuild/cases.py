"""The comparison corpus, as the oracle sees it: every judged document, its phase and its priors.

Runs against the oracle (`PYTHONPATH=~/pgc-oracle/transformation`), from the oracle's root, and
prints JSON. A document's phase comes from where it sits; its priors are the phases its rule module
declares, taken from the dossier its `CR:` header names, exactly as the testbed derives them.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from transformation.design.meta import RULE_MODULES

ROOT = Path.cwd()
CR = re.compile(r"^\*\*CR:\*\*\s*(?P<cr>.+?)\s*$", re.M)
DOSSIER_ROOTS = (ROOT / "scripts/testbed/fixture_dossiers", ROOT / "dossiers")


def cr_of(path: Path) -> str | None:
    match = CR.search(path.read_text(encoding="utf-8"))
    return match.group("cr") if match else None


def dossiers() -> dict[str, Path]:
    out: dict[str, Path] = {}
    for root in DOSSIER_ROOTS:
        for seed in sorted(root.glob("*/p0_seed_*.md")):
            cr = cr_of(seed)
            if cr and cr not in out:
                out[cr] = seed.parent
    return out


def phase_of(path: Path) -> str | None:
    parent = path.parent.name
    if parent == "corpus":
        return "p0"
    match = re.fullmatch(r"corpus_(p\d)", parent)
    if match:
        return match.group(1)
    if path.name.startswith("p0_business_problem_statement"):
        return None
    match = re.match(r"(p\d)_", path.name)
    return match.group(1) if match else None


def main() -> int:
    by_cr = dossiers()
    docs = sorted(p for p in (ROOT / "scripts/testbed").rglob("*.md")
                  if "register:" in p.read_text(encoding="utf-8"))
    for dossier in sorted((ROOT / "dossiers").iterdir()):
        docs += sorted(p for p in dossier.glob("p*.md") if "register:" in p.read_text(encoding="utf-8"))
    cases = []
    for doc in docs:
        phase = phase_of(doc)
        if phase is None:
            continue
        priors: dict[str, str] = {}
        declared = getattr(RULE_MODULES[phase], "PRIORS", ())
        dossier = by_cr.get(cr_of(doc) or "")
        for prior in declared:
            if dossier is None:
                break
            pattern = "p0_seed_*.md" if prior == "p0" else f"{prior}_*.md"
            found = sorted(dossier.glob(pattern))
            if found:
                priors[prior] = str(found[0].relative_to(ROOT))
        cases.append({"doc": str(doc.relative_to(ROOT)), "phase": phase, "priors": priors})
    json.dump(cases, sys.stdout, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
