"""Differential conformance — the genesis oracle against the compiled P0 phase.

The rehost claim is that authoring P0 as governed artifacts preserved its behaviour. That is only
evidence if both paths are actually exercised over the same seeds and compared:

    genesis oracle    rules from transformation.seed.rules  (Python declaration)
    compiled phase    rules from the sealed snapshot        (si.artifact.show)

The rule sets must be identical and the verdicts must agree, seed by seed and finding by finding.
Divergence is a defect in one of them, and this script says which seeds expose it.

Run:  python scripts/testbed/differential_p0.py [snapshot_root]
"""

from __future__ import annotations

import sys
from pathlib import Path

from inspector import api

from transformation.implementation.capability_transforms.atoms import (
    ct_pure_evaluate_rules_v0,
    ct_pure_parse_registers_v0,
)
from transformation.seed.oracle import judge_path
from transformation.seed.rules import rule_set

WF = "transformation::WF_P0_SEED_ADMISSIBILITY_V0"
REPO = Path(__file__).resolve().parents[2]


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


def sealed_rule_set(snapshot_root: str) -> list[dict]:
    """The rule set as it exists in the composition — no Python declaration consulted."""
    status, artifact = api.query("si.artifact.show", {"artifact": WF}, snapshot_root)
    if status != "SUCCESS":
        raise RuntimeError(f"{WF} not readable from {snapshot_root}: {status}")
    rules = _find_rule_set(artifact)
    if rules is None:
        raise RuntimeError(f"{WF} carries no rule_set — the governance did not survive compilation")
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


def genesis_verdict(seed_path: Path) -> tuple[str, list[tuple[str, str]]]:
    verdict = judge_path(seed_path)
    return verdict.verdict, [(f.rule, f.where) for f in verdict.findings]


def main() -> int:
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else str(REPO.parent / "snapshot")

    sealed = sealed_rule_set(snapshot_root)
    declared = rule_set()

    print(f"rule sets   sealed={len(sealed)}  declared={len(declared)}")
    sealed_ids = [r["id"] for r in sealed]
    declared_ids = [r.id for r in declared]
    if sealed_ids != declared_ids:
        print("  DIVERGENT: the sealed rule set is not the declared one")
        only_sealed = set(sealed_ids) - set(declared_ids)
        only_declared = set(declared_ids) - set(sealed_ids)
        if only_sealed:
            print(f"    only sealed:   {sorted(only_sealed)}")
        if only_declared:
            print(f"    only declared: {sorted(only_declared)}")
        return 1
    print("  identical\n")

    corpus = sorted(
        (REPO / "examples").rglob("*seed*.md")
    ) + sorted((REPO / "scripts" / "testbed" / "corpus").glob("*.md"))

    if not corpus:
        print("NO SEEDS — a differential over an empty corpus is not evidence")
        return 1

    failures = 0
    for seed_path in corpus:
        seed_text = seed_path.read_text(encoding="utf-8")
        g_verdict, g_findings = genesis_verdict(seed_path)
        c_verdict, c_findings = compiled_verdict(seed_text, sealed)

        agree = g_verdict == c_verdict and sorted(g_findings) == sorted(c_findings)
        mark = "AGREE " if agree else "DIVERGE"
        print(f"{mark}  {g_verdict:<12} {len(g_findings):>2} finding(s)  {seed_path.name}")

        if not agree:
            failures += 1
            print(f"         genesis : {g_verdict} {sorted(g_findings)}")
            print(f"         compiled: {c_verdict} {sorted(c_findings)}")

    print()
    if failures:
        print(f"DIFFERENTIAL FAILED — {failures} of {len(corpus)} seed(s) diverged")
        return 1
    print(f"DIFFERENTIAL PASSED — {len(corpus)} seed(s), both paths agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
