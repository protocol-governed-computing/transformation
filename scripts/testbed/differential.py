"""Differential conformance — the genesis oracle against each compiled phase.

The rehost claim is that authoring P0 as governed artifacts preserved its behaviour. That is only
evidence if both paths are actually exercised over the same seeds and compared:

    genesis oracle    rules from transformation.design.p0_change_seed.rules  (Python declaration)
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
    ct_pure_parse_prior_phases_v0,
    ct_pure_parse_registers_v0,
)
from transformation.design.oracle import evaluate
from transformation.design.read import read_seed
from transformation.design.p0_change_seed.rules import rule_set as p0_rule_set
from transformation.design.p1_change_request.rules import rule_set as p1_rule_set
from transformation.design.p2_domain_model.rules import rule_set as p2_rule_set
from transformation.design.p3_analysis_loop.rules import rule_set as p3_rule_set
from transformation.design.p4_business_model.rules import rule_set as p4_rule_set
from transformation.design.p5_business_intent.rules import rule_set as p5_rule_set
from transformation.design.p6_governance_intent.rules import rule_set as p6_rule_set
from transformation.design.p7_design_intent.rules import rule_set as p7_rule_set
from transformation.design.p8_authoring_mandate.rules import rule_set as p8_rule_set

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent

# A business CR's dossier lives with the domain it changes, not with the pipeline that judges it.
CR_01 = WORKSPACE / "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog"

# A CR's dossier grounds against the composition it was designed against; judged against the live
# one, the P7/P8 documents report collisions with their own output — true, and uninformative about
# the two paths. Reproduced through `e2e_phases_test.design_baseline()` rather than checked for
# existence: a cached baseline whose sources have since been recompiled is stale, and a stale
# baseline seals a rule set the declaration has already moved past.
from e2e_phases_test import design_baseline

# Each phase: its workflow, its declared rule set, and the corpus it judges. A phase added here
# without a corpus would report "identical rule sets" and prove nothing about behaviour, so the
# corpus is part of the declaration rather than discovered.
PHASES = {
    "P0": {
        "wf": "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
        "rules": p0_rule_set,
        "corpus": [
            REPO / "cr_dossiers/cr_00_new_subdomain/p0_seed_transformation_phases_v0.md",
            CR_01 / "p0_seed_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus").glob("*.md")),
        ],
    },
    "P1": {
        "wf": "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
        "rules": p1_rule_set,
        "priors": True,
        "corpus": [
            REPO / "cr_dossiers/cr_00_new_subdomain/p1_change_request_transformation_phases_v0.md",
            CR_01 / "p1_change_request_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p1").glob("*.md")),
        ],
    },
    "P2": {
        "wf": "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
        "rules": p2_rule_set,
        # P2 grounds claims against the composition, so the differential must supply the same
        # observation the compiled workflow gathers. Comparing two ungrounded runs would agree
        # perfectly while exercising none of the grounding.
        "observes": {"si.artifact.list": "artifacts"},
        # Cross-phase rules read an upstream document, and which one is a property of the
        # document being judged, not of the phase — see PRIORS_BY_DOCUMENT.
        "priors": True,
        "corpus": [
            REPO / "cr_dossiers/cr_00_new_subdomain/p2_domain_model_transformation_phases_v0.md",
            CR_01 / "p2_domain_model_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p2").glob("*.md")),
        ],
    },
    "P3": {
        "wf": "transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0",
        "rules": p3_rule_set,
        # Two observations, answering different questions: does this identity exist, and may this
        # domain be drawn on at all. A differential that supplied only the first would agree with
        # itself perfectly while leaving the reuse ruling unexercised.
        "observes": {"si.artifact.list": "artifacts", "si.snapshot.summary": "reuse_visibility"},
        "priors": True,
        "corpus": [
            CR_01 / "p3_analysis_loop_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p3").glob("*.md")),
        ],
    },
    "P4": {
        "wf": "transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0",
        "rules": p4_rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "priors": True,
        "corpus": [
            CR_01 / "p4_business_model_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p4").glob("*.md")),
        ],
    },
    "P5": {
        "wf": "transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0",
        "rules": p5_rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "corpus": [
            CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p5").glob("*.md")),
        ],
    },
    "P6": {
        "wf": "transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0",
        "rules": p6_rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "priors": True,
        "corpus": [
            CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p6").glob("*.md")),
        ],
    },
    "P7": {
        "wf": "transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0",
        "rules": p7_rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "priors": True,
        "corpus": [
            CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p7").glob("*.md")),
        ],
    },
    "P8": {
        "wf": "transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0",
        "rules": p8_rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "priors": True,
        "corpus": [
            CR_01 / "p8_authoring_mandate_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p8").glob("*.md")),
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


def observation(operations: dict | None, snapshot_root: str) -> dict:
    """The facts a grounding phase's workflow gathers, keyed by the operation that produced them.

    `operations` maps operation → the key its result carries rows under, because a phase may ground
    against more than one surface and they do not answer in the same shape.
    """
    gathered = {}
    for operation, result_key in (operations or {}).items():
        status, result = api.query(operation, {}, snapshot_root)
        if status != "SUCCESS":
            raise RuntimeError(f"{operation} failed against {snapshot_root}: {status}")
        gathered[operation] = result.get(result_key, result)
    return gathered


# Which upstream document each judged document was handed. Keyed per document, not per phase: the
# P2 corpus holds pages from two different change requests, and judging CR-0's domain model against
# CR-1's change request reports eight confident findings about a handoff that never happened. Both
# paths agreed on every one of them, which is how a differential passes while proving nothing.
#
# So a phase that declares cross-phase rules must declare a prior for every document it judges. An
# unmapped document is a hard failure rather than an unchecked handoff — the corpus is discovered by
# glob, and a fixture dropped in without one would quietly stop exercising the rule.
CR_00 = REPO / "cr_dossiers/cr_00_new_subdomain"

PRIORS_BY_DOCUMENT = {
    "p2_domain_model_transformation_phases_v0.md": {
        "p1": CR_00 / "p1_change_request_transformation_phases_v0.md"},
    "inadmissible_p2_register.md": {
        "p1": CR_00 / "p1_change_request_transformation_phases_v0.md"},
    "p2_domain_model_book_library_mgmt_catalog_v0.md": {
        "p1": CR_01 / "p1_change_request_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p2_catalog_register.md": {
        "p1": CR_01 / "p1_change_request_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p2_dropped_belief.md": {
        "p1": CR_01 / "p1_change_request_book_library_mgmt_catalog_v0.md"},
    "p3_analysis_loop_book_library_mgmt_catalog_v0.md": {
        "p2": CR_01 / "p2_domain_model_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p3_ineligible_reuse.md": {
        "p2": CR_01 / "p2_domain_model_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p3_restated_result.md": {
        "p2": CR_01 / "p2_domain_model_book_library_mgmt_catalog_v0.md"},
    "p8_authoring_mandate_book_library_mgmt_catalog_v0.md": {
        "p7": CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p8_broken_order.md": {
        "p7": CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md"},
    "admissible_p8_reconciled_mandate.md": {
        "p7": CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p8_undesigned_artifact.md": {"p7": CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p8_dropped_artifact.md": {"p7": CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md"},
    "p1_change_request_transformation_phases_v0.md": {
        "p0": CR_00 / "p0_seed_transformation_phases_v0.md"},
    "inadmissible_p1_register.md": {
        "p0": CR_00 / "p0_seed_transformation_phases_v0.md"},
    "p1_change_request_book_library_mgmt_catalog_v0.md": {
        "p0": CR_01 / "p0_seed_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p1_dropped_criterion.md": {
        "p0": CR_01 / "p0_seed_book_library_mgmt_catalog_v0.md"},
    "p7_design_intent_book_library_mgmt_catalog_v0.md": {"p5": CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md", "p6": CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p7_collision.md": {"p5": CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md", "p6": CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p7_unbound_code.md": {"p5": CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md", "p6": CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p7_dropped_reuse.md": {"p5": CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md", "p6": CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p7_unrooted_source.md": {"p5": CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md", "p6": CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md"},
    "p6_governance_intent_book_library_mgmt_catalog_v0.md": {"p5": CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p6_unplaced.md": {"p5": CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p6_unplaced_scope.md": {"p5": CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md"},
    "p4_business_model_book_library_mgmt_catalog_v0.md": {"p3": CR_01 / "p3_analysis_loop_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p4_broken_consolidation.md": {"p3": CR_01 / "p3_analysis_loop_book_library_mgmt_catalog_v0.md"},
    "inadmissible_p4_dropped_decision.md": {"p3": CR_01 / "p3_analysis_loop_book_library_mgmt_catalog_v0.md"},
}


def prior_texts(doc_path: Path, reads_priors: bool) -> dict:
    """The upstream documents this document is judged against, as text a workflow is handed."""
    if not reads_priors:
        return {}
    declared = PRIORS_BY_DOCUMENT.get(doc_path.name)
    if declared is None:
        raise SystemExit(
            f"{doc_path.name} is judged by a phase with cross-phase rules and declares no prior; "
            f"add it to PRIORS_BY_DOCUMENT"
        )
    return {
        phase_id: path.read_text(encoding="utf-8")
        for phase_id, path in declared.items()
    }


def compiled_verdict(
    seed_text: str,
    rules: list[dict],
    observed: dict | None = None,
    priors: dict | None = None,
) -> tuple[str, list[tuple[str, str]]]:
    """Drive the compiled phase's atoms exactly as the workflow composes them."""
    parsed = ct_pure_parse_registers_v0.execute({"document_text": seed_text})
    parsed_priors = ct_pure_parse_prior_phases_v0.execute({"prior_texts": priors or {}})
    result = ct_pure_evaluate_rules_v0.execute(
        {
            "header": parsed["header"],
            "sections": parsed["sections"],
            "registers": parsed["registers"],
            "document_text": seed_text,
            "rule_set": rules,
            "observed": observed or {},
            "priors": parsed_priors["priors"],
        }
    )
    findings = [(f["rule"], f["where"]) for f in result["findings"]]
    return result["verdict"], findings


def genesis_verdict(
    doc_path: Path,
    rules,
    observed: dict | None = None,
    priors: dict | None = None,
) -> tuple[str, list[tuple[str, str]]]:
    doc = read_seed(doc_path)
    doc.observed = observed or {}
    # The genesis path parses its priors with the same reader the transform uses, so a divergence
    # is a difference in rule evaluation rather than in how the two paths read a document.
    doc.priors = ct_pure_parse_prior_phases_v0.execute({"prior_texts": priors or {}})["priors"]
    verdict = evaluate(doc, rules)
    return verdict.verdict, [(f.rule, f.where) for f in verdict.findings]


def main() -> int:
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else str(REPO.parent / "snapshot")
    failures = 0
    total = 0

    for phase, spec in PHASES.items():
        # P7 and P8 judge assigned identities against a baseline; the rest are baseline-agnostic.
        root = design_baseline() if phase in ("P7", "P8") else snapshot_root
        sealed = sealed_rule_set(spec["wf"], root)
        declared = spec["rules"]()

        print(f"{phase}  rule sets   sealed={len(sealed)}  declared={len(declared)}")
        if [r["id"] for r in sealed] != [r.id for r in declared]:
            print("  DIVERGENT: the sealed rule set is not the declared one")
            failures += 1
            continue
        print("  identical")

        observed = observation(spec.get("observes"), root)
        reads_priors = bool(spec.get("priors"))
        corpus = [p for p in spec["corpus"] if p.is_file()]
        if not corpus:
            print(f"  NO DOCUMENTS — a differential over an empty corpus is not evidence")
            failures += 1
            continue

        for doc_path in corpus:
            total += 1
            text = doc_path.read_text(encoding="utf-8")
            priors = prior_texts(doc_path, reads_priors)
            g_verdict, g_findings = genesis_verdict(doc_path, declared, observed, priors)
            c_verdict, c_findings = compiled_verdict(text, sealed, observed, priors)
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
