"""Regenerate the committed P0 test payloads from their source documents.

A payload embeds a whole seed document as `seed_text`, so a hand-edited payload silently drifts
from the seed it was copied from. Generating them keeps one source of truth: edit the seed or the
corpus entry, run this, commit the result.

Run:  python scripts/testbed/build_payloads.py
"""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
OUT = REPO / "testbed" / "phases" / "test_payloads"

AUTHOR = "bachipeachy"

# A source is resolved against the repo unless it names a workspace root. CR-0 is this repo's own
# change request and its dossier lives here; a business CR's dossier lives with the domain it
# changes, which is a sibling repo. Both are payload sources, so the map carries the root.
ROOTS = {"business_domains": WORKSPACE}

CATALOG_P1 = (
    "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
    "p1_change_request_book_library_mgmt_catalog_v0.md"
)
CATALOG_P0 = (
    "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
    "p0_seed_book_library_mgmt_catalog_v0.md"
)
CATALOG_P3 = (
    "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
    "p3_analysis_loop_book_library_mgmt_catalog_v0.md"
)
CATALOG_P6 = (
    "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
    "p6_governance_intent_book_library_mgmt_catalog_v0.md"
)
CATALOG_P5 = (
    "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
    "p5_business_intent_book_library_mgmt_catalog_v0.md"
)
CATALOG_P7 = (
    "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
    "p7_design_intent_book_library_mgmt_catalog_v0.md"
)
CATALOG_P2 = (
    "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
    "p2_domain_model_book_library_mgmt_catalog_v0.md"
)

PAYLOADS = {
    "01_admissible_seed.json": (
        "dossiers/new_subdomain/p0_seed_transformation_phases_v0.md"
    ),
    "02_admissible_reference.json": "scripts/testbed/corpus/admissible_blockchain_reference.md",
    "03_inadmissible_seven_violations.json": (
        "scripts/testbed/corpus/inadmissible_seven_violations.md"
    ),
    "04_inadmissible_structural.json": "scripts/testbed/corpus/inadmissible_structural.md",
    "05_inadmissible_truncated.json": "scripts/testbed/corpus/inadmissible_truncated.md",
    "06_p1_admissible_register.json": (
        "dossiers/new_subdomain/"
        "p1_change_request_transformation_phases_v0.md"
    ),
    "07_p1_inadmissible_register.json": "scripts/testbed/corpus_p1/inadmissible_p1_register.md",
    "08_p2_admissible_register.json": (
        "dossiers/new_subdomain/"
        "p2_domain_model_transformation_phases_v0.md"
    ),
    "09_p2_inadmissible_register.json": "scripts/testbed/corpus_p2/inadmissible_p2_register.md",
    # CR-1 — the first business subject. CR-0 is the pipeline authoring its own domain, so it
    # cannot exercise a phase against business content; these three carry the same phases over a
    # library catalog instead.
    "10_p0_admissible_catalog_seed.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p0_seed_book_library_mgmt_catalog_v0.md"
    ),
    "11_p1_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p1_change_request_book_library_mgmt_catalog_v0.md"
    ),
    "12_p2_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p2_domain_model_book_library_mgmt_catalog_v0.md"
    ),
    # The catalog register with three defects introduced. Without it the evidence that the rules
    # bite comes only from documents about the pipeline itself — a phase could pass every business
    # document by doing nothing and the suite would still be green.
    "13_p2_inadmissible_catalog_register.json": (
        "scripts/testbed/corpus_p2/inadmissible_p2_catalog_register.md"
    ),
    # P3 — the first phase that decides. The inadmissible case offers a business change request a
    # pipeline capability and a conformance workload: the exact confusion the reuse ruling exists
    # to prevent, and one no amount of reading the document could catch.
    "14_p3_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p3_analysis_loop_book_library_mgmt_catalog_v0.md"
    ),
    "15_p3_inadmissible_catalog_register.json": (
        "scripts/testbed/corpus_p3/inadmissible_p3_ineligible_reuse.md"
    ),
    # P4 consolidates, so its defects are between registers rather than inside one. The
    # inadmissible case points a capability and a scope entry at gaps nobody declared, leaves a
    # gap unowned, and depends on an artifact in the wrong namespace.
    "16_p4_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p4_business_model_book_library_mgmt_catalog_v0.md"
    ),
    "17_p4_inadmissible_catalog_register.json": (
        "scripts/testbed/corpus_p4/inadmissible_p4_broken_consolidation.md"
    ),
    # P5 is the first step up the purity ladder. The inadmissible case places a provisional code,
    # files a code under the wrong family, borrows a capability that is not there, and leaks a
    # binding expression into intent.
    "18_p5_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p5_business_intent_book_library_mgmt_catalog_v0.md"
    ),
    "19_p5_inadmissible_catalog_register.json": (
        "scripts/testbed/corpus_p5/inadmissible_p5_binding_leak.md"
    ),
    # P6 draws lines. The inadmissible case names an artifact where a subdomain belongs, claims a
    # capability satisfied with nothing to show, gives a boundary one side, and reaches an outcome
    # for a capability nobody placed.
    "20_p6_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p6_governance_intent_book_library_mgmt_catalog_v0.md"
    ),
    "21_p6_inadmissible_catalog_register.json": (
        "scripts/testbed/corpus_p6/inadmissible_p6_unplaced.md"
    ),
    # P7 assigns binding identity. The inadmissible case collides with an artifact that already
    # exists, omits a namespace, references a spelling variant nobody declared, and leaves a store
    # with nowhere to live.
    "22_p7_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p7_design_intent_book_library_mgmt_catalog_v0.md"
    ),
    "23_p7_inadmissible_catalog_register.json": (
        "scripts/testbed/corpus_p7/inadmissible_p7_collision.md"
    ),
    # P8 is judged on row order. The inadmissible case drops a step, schedules a prerequisite after
    # the thing that needs it, and routes the critical path through a step nobody scheduled — three
    # defects that exist between rows rather than in any one of them.
    "24_p8_admissible_catalog_mandate.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p8_authoring_mandate_book_library_mgmt_catalog_v0.md"
    ),
    "25_p8_inadmissible_catalog_mandate.json": (
        "scripts/testbed/corpus_p8/inadmissible_p8_broken_order.md"
    ),
    # The first two cases whose defect exists in neither document. Each is a correct dossier page
    # by itself: the P2 register resolves every belief it lists, the P3 register re-verifies every
    # item it names. Only the handoff is wrong.
    "26_p2_inadmissible_dropped_belief.json": (
        "scripts/testbed/corpus_p2/inadmissible_p2_dropped_belief.md"
    ),
    # P8 reconciles against P7 as sets of identities. CR-1's own mandate does not reconcile — it
    # drops one designed artifact — so the corpus carries a corrected mandate as the admissible
    # case, and the authored one stays as authored.
    "29_p8_inadmissible_undesigned_artifact.json": (
        "scripts/testbed/corpus_p8/inadmissible_p8_undesigned_artifact.md"
    ),
    "35_p8_inadmissible_dropped_artifact.json": (
        "scripts/testbed/corpus_p8/inadmissible_p8_dropped_artifact.md"
    ),
    # P0→P1 is matched on the claim, not a citation — the seed's section titles are free-form. The
    # dropped criterion is the one execution validation later runs the composition against.
    "30_p1_inadmissible_dropped_criterion.json": (
        "scripts/testbed/corpus_p1/inadmissible_p1_dropped_criterion.md"
    ),
    # P5→P7 closes the purity ladder: a provisional code that never acquires a binding identity is
    # a capability the business asked for and the design declined.
    "31_p7_inadmissible_unbound_code.json": (
        "scripts/testbed/corpus_p7/inadmissible_p7_unbound_code.md"
    ),
    # P3→P4 is the consolidation edge: P4's key rule is "consolidation, not re-litigation", and a
    # decision that never reaches the capability graph has been neither.
    "32_p4_inadmissible_dropped_decision.json": (
        "scripts/testbed/corpus_p4/inadmissible_p4_dropped_decision.md"
    ),
    # P6→P7: a dependency P6 declared satisfied by an existing artifact, never inventoried as reuse.
    "33_p7_inadmissible_dropped_reuse.json": (
        "scripts/testbed/corpus_p7/inadmissible_p7_dropped_reuse.md"
    ),
    # A binding source that names a place execution does not offer, read as a literal by everything
    # beneath it.
    "36_p7_inadmissible_unrooted_source.json": (
        "scripts/testbed/corpus_p7/inadmissible_p7_unrooted_source.md"
    ),
    # A store named for a format its storage capability does not write.
    "37_p7_inadmissible_store_path.json": (
        "scripts/testbed/corpus_p7/inadmissible_p7_store_path.md"
    ),
    # A seed that asks a blocking question and hands it on unanswered. Every other rule passes:
    # the row is well-formed and in vocabulary, and says in the author's own words that the next
    # phase cannot proceed without the answer.
    "38_p0_inadmissible_blocking_clarification.json": (
        "scripts/testbed/corpus/inadmissible_p0_blocking_clarification.md"
    ),
    # P5→P6: a capability declared in scope that the placement phase never mentions. A row missing
    # from `ownership` alone is what OUTCOME_CAPABILITY_UNPLACED already catches; this is the case
    # no single document can see.
    "34_p6_inadmissible_unplaced_scope.json": (
        "scripts/testbed/corpus_p6/inadmissible_p6_unplaced_scope.md"
    ),
    "27_p3_inadmissible_restated_result.json": (
        "scripts/testbed/corpus_p3/inadmissible_p3_restated_result.md"
    ),
}

# payload → phase id → the upstream document that phase is judged against.
#
# The prior travels in the payload rather than being looked up: a workflow reads what it is handed,
# and a testbed that resolved a prior by filename convention would prove the convention, not the
# rule. Every P2 and P3 case carries one, including the admissible ones — a cross-phase rule that
# only ever ran on a doctored document would never be shown to pass.
PRIOR_SOURCES = {
    "08_p2_admissible_register.json": {
        "p1": "dossiers/new_subdomain/p1_change_request_transformation_phases_v0.md"},
    "09_p2_inadmissible_register.json": {
        "p1": "dossiers/new_subdomain/p1_change_request_transformation_phases_v0.md"},
    "12_p2_admissible_catalog_register.json": {"p1": CATALOG_P1},
    "13_p2_inadmissible_catalog_register.json": {"p1": CATALOG_P1},
    "26_p2_inadmissible_dropped_belief.json": {"p1": CATALOG_P1},
    # P5 carries the subdomain purpose forward from the seed, so the seed travels with it.
    "18_p5_admissible_catalog_register.json": {"p0": CATALOG_P0},
    "19_p5_inadmissible_catalog_register.json": {"p0": CATALOG_P0},
    "14_p3_admissible_catalog_register.json": {"p2": CATALOG_P2},
    "15_p3_inadmissible_catalog_register.json": {"p2": CATALOG_P2},
    "27_p3_inadmissible_restated_result.json": {"p2": CATALOG_P2},
    "24_p8_admissible_catalog_mandate.json": {"p7": CATALOG_P7},
    "25_p8_inadmissible_catalog_mandate.json": {"p7": CATALOG_P7},
    "29_p8_inadmissible_undesigned_artifact.json": {"p7": CATALOG_P7},
    "35_p8_inadmissible_dropped_artifact.json": {"p7": CATALOG_P7},
    "06_p1_admissible_register.json": {
        "p0": "dossiers/new_subdomain/p0_seed_transformation_phases_v0.md"},
    "07_p1_inadmissible_register.json": {
        "p0": "dossiers/new_subdomain/p0_seed_transformation_phases_v0.md"},
    "11_p1_admissible_catalog_register.json": {"p0": CATALOG_P0},
    "30_p1_inadmissible_dropped_criterion.json": {"p0": CATALOG_P0},
    "22_p7_admissible_catalog_register.json": {"p5": CATALOG_P5, "p6": CATALOG_P6},
    "23_p7_inadmissible_catalog_register.json": {"p5": CATALOG_P5, "p6": CATALOG_P6},
    "31_p7_inadmissible_unbound_code.json": {"p5": CATALOG_P5, "p6": CATALOG_P6},
    "16_p4_admissible_catalog_register.json": {"p3": CATALOG_P3},
    "17_p4_inadmissible_catalog_register.json": {"p3": CATALOG_P3},
    "32_p4_inadmissible_dropped_decision.json": {"p3": CATALOG_P3},
    "33_p7_inadmissible_dropped_reuse.json": {"p5": CATALOG_P5, "p6": CATALOG_P6},
    "36_p7_inadmissible_unrooted_source.json": {"p5": CATALOG_P5, "p6": CATALOG_P6},
    "37_p7_inadmissible_store_path.json": {"p5": CATALOG_P5, "p6": CATALOG_P6},
    "20_p6_admissible_catalog_register.json": {"p5": CATALOG_P5},
    "21_p6_inadmissible_catalog_register.json": {"p5": CATALOG_P5},
    "34_p6_inadmissible_unplaced_scope.json": {"p5": CATALOG_P5},
}

# P0 offers a seed, P1 offers a register — the intent field differs, so the payload key does too.
PAYLOAD_KEY = {
    "06_p1_admissible_register.json": "register_text",
    "07_p1_inadmissible_register.json": "register_text",
    "08_p2_admissible_register.json": "register_text",
    "09_p2_inadmissible_register.json": "register_text",
    "11_p1_admissible_catalog_register.json": "register_text",
    "12_p2_admissible_catalog_register.json": "register_text",
    "13_p2_inadmissible_catalog_register.json": "register_text",
    "14_p3_admissible_catalog_register.json": "register_text",
    "15_p3_inadmissible_catalog_register.json": "register_text",
    "16_p4_admissible_catalog_register.json": "register_text",
    "17_p4_inadmissible_catalog_register.json": "register_text",
    "18_p5_admissible_catalog_register.json": "register_text",
    "19_p5_inadmissible_catalog_register.json": "register_text",
    "20_p6_admissible_catalog_register.json": "register_text",
    "21_p6_inadmissible_catalog_register.json": "register_text",
    "22_p7_admissible_catalog_register.json": "register_text",
    "23_p7_inadmissible_catalog_register.json": "register_text",
    "24_p8_admissible_catalog_mandate.json": "register_text",
    "25_p8_inadmissible_catalog_mandate.json": "register_text",
    "26_p2_inadmissible_dropped_belief.json": "register_text",
    "27_p3_inadmissible_restated_result.json": "register_text",
    "29_p8_inadmissible_undesigned_artifact.json": "register_text",
    "35_p8_inadmissible_dropped_artifact.json": "register_text",
    "30_p1_inadmissible_dropped_criterion.json": "register_text",
    "31_p7_inadmissible_unbound_code.json": "register_text",
    "32_p4_inadmissible_dropped_decision.json": "register_text",
    "33_p7_inadmissible_dropped_reuse.json": "register_text",
    "36_p7_inadmissible_unrooted_source.json": "register_text",
    "37_p7_inadmissible_store_path.json": "register_text",
    "34_p6_inadmissible_unplaced_scope.json": "register_text",
}


def root_for(source: str) -> Path:
    return ROOTS.get(source.split("/", 1)[0], REPO)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, source in PAYLOADS.items():
        src = root_for(source) / source
        if not src.is_file():
            raise FileNotFoundError(f"payload source missing: {src}")
        key = PAYLOAD_KEY.get(name, "seed_text")
        payload = {key: src.read_text(encoding="utf-8"), "author_of_record": AUTHOR}
        # A phase that reads no upstream document still declares that it read none. Omitting the
        # field would make "this handoff is ungoverned" indistinguishable from "the driver forgot".
        payload["prior_texts"] = {
            phase_id: (root_for(source) / source).read_text(encoding="utf-8")
            for phase_id, source in PRIOR_SOURCES.get(name, {}).items()
        }
        (OUT / name).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"  {name:<40} <- {source}")
    print(f"\n{len(PAYLOADS)} payload(s) written to {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
