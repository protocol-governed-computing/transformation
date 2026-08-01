"""Differential conformance — the genesis oracle against each compiled phase.

The rehost claim is that authoring P0 as governed artifacts preserved its behaviour. That is only
evidence if both paths are actually exercised over the same seeds and compared:

    genesis oracle    rules from transformation.phases.p0.rules  (Python declaration)
    compiled phase    rules from the sealed snapshot        (si.artifact.show)

The rule sets must be identical and the verdicts must agree, seed by seed and finding by finding.
Divergence is a defect in one of them, and this script says which seeds expose it.

Run:  python scripts/testbed/differential.py [snapshot_root]
"""

from __future__ import annotations

import sys
from pathlib import Path

from inspector import api

from transformation.implementation.capability_transforms.atoms import (
    ct_pure_evaluate_rules_v0,
    ct_pure_parse_registers_v0,
)
from transformation.phases.oracle import judge_path
from transformation.phases.p0.rules import rule_set as p0_rule_set
from transformation.phases.p1.rules import rule_set as p1_rule_set

REPO = Path(__file__).resolve().parents[2]

# Each phase: its workflow, its declared rule set, and the corpus it judges. A phase added here
# without a corpus would report "identical rule sets" and prove nothing about behaviour, so the
# corpus is part of the declaration rather than discovered.
PHASES = {
    "P0": {
        "wf": "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
        "rules": p0_rule_set,
        "corpus": [
            REPO / "examples/transformation/phases/cr_00_new_subdomain/p0_seed_transformation_phases_v0.md",
            *sorted((REPO / "scripts/testbed/corpus").glob("*.md")),
        ],
    },
    "P1": {
        "wf": "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
        "rules": p1_rule_set,
        "corpus": [
            REPO / "examples/transformation/phases/cr_00_new_subdomain/p1_change_request_transformation_phases_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p1").glob("*.md")),
        ],
    },
}


def _find_rule_set(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "rule_set":
                return value
            found = _find_rule_set(value)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = _find_rule_set(value)
            if found is not None:
                return found
    return None


def sealed_rule_set(wf: str, snapshot_root: str) -> list[dict]:
    """The rule set as it exists in the composition — no Python declaration consulted."""
    status, artifact = api.query("si.artifact.show", {"artifact": wf}, snapshot_root)
    if status != "SUCCESS":
        raise RuntimeError(f"{wf} not readable from {snapshot_root}: {status}")
    rules = _find_rule_set(artifact)
    if rules is None:
        raise RuntimeError(f"{wf} carries no rule_set — the governance did not survive compilation")
    return rules


def compiled_verdict(seed_text: str, rules: list[dict]) -> tuple[str, list[tuple[str, str]]]:
    """Drive the compiled phase's atoms exactly as the workflow composes them."""
    parsed = ct_pure_parse_registers_v0.execute({"document_text": seed_text})
    result = ct_pure_evaluate_rules_v0.execute(
        {
            "header": parsed["header"],
            "sections": parsed["sections"],
            "document_text": seed_text,
            "rule_set": rules,
        }
    )
    findings = [(f["rule"], f["where"]) for f in result["findings"]]
    return result["verdict"], findings


def genesis_verdict(doc_path: Path, rules) -> tuple[str, list[tuple[str, str]]]:
    verdict = judge_path(doc_path, rules)
    return verdict.verdict, [(f.rule, f.where) for f in verdict.findings]


def main() -> int:
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else str(REPO.parent / "snapshot")
    failures = 0
    total = 0

    for phase, spec in PHASES.items():
        sealed = sealed_rule_set(spec["wf"], snapshot_root)
        declared = spec["rules"]()

        print(f"{phase}  rule sets   sealed={len(sealed)}  declared={len(declared)}")
        if [r["id"] for r in sealed] != [r.id for r in declared]:
            print("  DIVERGENT: the sealed rule set is not the declared one")
            failures += 1
            continue
        print("  identical")

        corpus = [p for p in spec["corpus"] if p.is_file()]
        if not corpus:
            print(f"  NO DOCUMENTS — a differential over an empty corpus is not evidence")
            failures += 1
            continue

        for doc_path in corpus:
            total += 1
            text = doc_path.read_text(encoding="utf-8")
            g_verdict, g_findings = genesis_verdict(doc_path, declared)
            c_verdict, c_findings = compiled_verdict(text, sealed)
            agree = g_verdict == c_verdict and sorted(g_findings) == sorted(c_findings)
            print(f"  {'AGREE ' if agree else 'DIVERGE'}  {g_verdict:<12} {len(g_findings):>2} finding(s)  {doc_path.name}")
            if not agree:
                failures += 1
                print(f"           genesis : {g_verdict} {sorted(g_findings)}")
                print(f"           compiled: {c_verdict} {sorted(c_findings)}")
        print()

    if failures:
        print(f"DIFFERENTIAL FAILED — {failures} divergence(s) over {total} document(s)")
        return 1
    print(f"DIFFERENTIAL PASSED — {total} document(s) across {len(PHASES)} phase(s), both paths agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
