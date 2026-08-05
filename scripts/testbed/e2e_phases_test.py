"""End-to-end phase check — every phase through the real runtime.

The differential (`differential.py`) drives the capability transforms directly. It proves the rule
sets and the check logic, and it proves nothing about IN/WF/CC wiring, node input bindings, or
routing — because it never boots a snapshot or dispatches a workflow.

That gap is not theoretical. A workflow that bound `$.capability_result.header` across nodes passed
the differential and failed the moment it ran through `protocol_runtime`: workflow nodes read the
intent payload, not a previous node's result. Only executing the compiled workflow catches that
class of defect.

So this script executes each phase the way the runbook used to, one case per line, and asserts the
expected verdict and finding count. Adding a phase is an entry in `CASES` — the runbook stays one
line however many phases exist.

Run:  python scripts/testbed/e2e_phases.py [snapshot_root]
Exit: 0 if every case matched, 1 otherwise.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent

# Domain CT/CS implementations are imported by declared module path at execution. Their roots are
# env-provisioned — the runtime never manipulates sys.path — so a suite that drives the runtime has
# to provision them the way `run.sh` does. P2 is the first phase to need this: it binds a capability
# whose host lives in the governance surface.
for _root in (WORKSPACE / "software_governance", WORKSPACE / "conformance_workloads",
              WORKSPACE / "business_domains", REPO):
    if str(_root) not in sys.path:
        sys.path.insert(0, str(_root))

from runtime import api
from transformation.design.merit import Merit, load_policy, rate
PAYLOADS = REPO / "testbed" / "phases" / "test_payloads"

# phase, workflow, payload file, expected verdict, expected rule ids, expected rules evaluated,
# expected figure of merit.
#
# The rating is asserted, not just printed. A figure of merit nobody checks drifts into decoration:
# it would keep reporting a number while the thing it measures changed underneath it. Note that the
# two axes move independently — every admissible CR-1 document rates 4/5 because it carries a
# declared open question, which is a governed hole rather than a defect.
#
# The expectation names the rules that must fire, not how many. A finding *count* is a weak
# assertion: seven entirely different rules firing satisfies "7 findings", and the suite reports OK
# over the wrong behaviour. Naming them catches a rule that stops working even when another starts
# firing in its place.
#
# Both an admissible and an inadmissible case per phase: a suite that only runs the passing case
# proves transport, not governance.
CASES = [
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "01_admissible_seed.json", "ADMISSIBLE", [], 80, 4),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "02_admissible_reference.json", "ADMISSIBLE", [], 80, 4),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "03_inadmissible_seven_violations.json", "INADMISSIBLE", [
         "BELIEF_STATED_AS_FACT",
         "BELIEF_WITHOUT_VERIFICATION_GOAL",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "LIFECYCLE_STATE_NOT_IN_VOCABULARY",
     ], 80, 3),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "04_inadmissible_structural.json", "INADMISSIBLE", ["REGISTER_MISSING"] * 5, 80, 3),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "05_inadmissible_truncated.json", "INADMISSIBLE", ["REGISTER_MISSING"] * 12, 80, 4),
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "06_p1_admissible_register.json", "ADMISSIBLE", [], 167, 4),
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "07_p1_inadmissible_register.json", "INADMISSIBLE", [
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "ROW_WITHOUT_SOURCE_FINDING",
         # The leak and the loss are one edit seen from two sides: naming a transform inside a
         # business invariant also stops the row restating the invariant the seed declared. The
         # fixture was cut for the first defect years before the second rule existed.
         "SEED_ROW_NOT_CARRIED",
         # The second is the assumption this fixture inherits from the change request it was cut
         # from, reworded there from "register structure" to "section structure".
         "SEED_ROW_NOT_CARRIED",
         # Both mutations are additions as well as losses: a reworded row states something the seed
         # does not, which is the half of the contract confinement governs.
         "ROW_NOT_IN_SEED",
         "ROW_NOT_IN_SEED",
         "SOURCE_FINDING_UNRESOLVED",
     ], 167, 3),
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "08_p2_admissible_register.json", "ADMISSIBLE", [], 64, 4),
    # Grounding: a misspelled identity and a right-code/wrong-namespace one are defects; an
    # identity simply absent from the baseline is proposed-new and correctly goes unflagged.
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "09_p2_inadmissible_register.json", "INADMISSIBLE", [
         "BASELINE_IDENTITY_UNRESOLVED",
         "BASELINE_IDENTITY_UNRESOLVED",
     ], 64, 2),
    # CR-1 — the same three phases over a business subject. CR-0 is the pipeline authoring its own
    # domain, so it grounds every claim against artifacts this repo also wrote; the catalog CR
    # grounds against a composition it contributed nothing to, which is the harder case.
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "10_p0_admissible_catalog_seed.json", "ADMISSIBLE", [], 80, 4),
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "11_p1_admissible_catalog_register.json", "ADMISSIBLE", [], 167, 4),
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "12_p2_admissible_catalog_register.json", "ADMISSIBLE", [], 64, 4),
    # The rules must bite on business content, not only on documents about the pipeline. A
    # misspelled identity and a right-code/wrong-namespace one are defects; design leaking into a
    # business-language cell is a third. An identity merely absent from the baseline stays
    # unflagged — that is proposed-new, which is what a CR is for.
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "13_p2_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "BASELINE_IDENTITY_UNRESOLVED",
         "BASELINE_IDENTITY_UNRESOLVED",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
     ], 64, 1),
    # P3 decides, so it observes twice: the artifact list resolves identities, the composition
    # summary carries what each domain declares about being reused. The inadmissible case offers a
    # business CR a pipeline capability and a conformance workload — a confusion that is invisible
    # in the document and only a declaration can settle.
    ("P3", "transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0",
     "14_p3_admissible_catalog_register.json", "ADMISSIBLE", [], 48, 4),
    ("P3", "transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0",
     "15_p3_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "REUSE_CANDIDATE_NOT_ELIGIBLE",
         "REUSE_CANDIDATE_NOT_ELIGIBLE",
     ], 48, 3),
    # P4 consolidates: its defects live between registers, where every register is individually
    # well formed and the document as a whole asserts something untrue. The admissible case is the
    # corpus's only 5/5 — a consolidation carries no open questions of its own, because P3
    # resolved them.
    ("P4", "transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0",
     "16_p4_admissible_catalog_register.json", "ADMISSIBLE", [], 68, 5),
    ("P4", "transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0",
     "17_p4_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "DEPENDENCY_IDENTITY_UNRESOLVED",
         "GAP_ENTRY_UNDECLARED",
         "GAP_WITHOUT_OWNER",
         "SCOPE_GAP_UNDECLARED",
     ], 68, 2),
    # P5 is the first rung up the purity ladder, and its two rules pull opposite ways: a
    # provisional code must NOT be namespaced, while a borrowed capability MUST be — one names
    # what this change creates, the other what it leans on.
    ("P5", "transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0",
     "18_p5_admissible_catalog_register.json", "ADMISSIBLE", [], 53, 4),
    ("P5", "transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0",
     "19_p5_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "BINDING_LEAKED_INTO_INTENT",
         "CROSS_SUBDOMAIN_REF_UNRESOLVED",
         "PROVISIONAL_CODE_ALREADY_BOUND",
         "PROVISIONAL_CODE_MALFORMED",
         "PROVISIONAL_FAMILY_MISMATCH",
         "PROVISIONAL_FAMILY_MISMATCH",
     ], 53, 3),
    # P6 draws lines, and the ladder does not simply accumulate: P5 requires provisional codes,
    # P6 forbids them. Each rung admits its own vocabulary rather than everything below it.
    ("P6", "transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0",
     "20_p6_admissible_catalog_register.json", "ADMISSIBLE", [], 45, 5),
    ("P6", "transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0",
     "21_p6_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "DEPENDENCY_DIRECTION_MALFORMED",
         # Writing a provisional code where a capability belongs also stops P5's in-scope
         # capability being placed under the name P5 gave it — one edit, two rules, and the
         # fixture was cut for the first long before the second existed.
         "IN_SCOPE_CAPABILITY_UNPLACED",
         "OUTCOME_CAPABILITY_UNPLACED",
         "OUTCOME_CAPABILITY_UNPLACED",
         "PROVISIONAL_CODE_IN_PLACEMENT",
         "SATISFIED_WITHOUT_EXISTING_ARTIFACT",
     ], 45, 4),
    # P7 assigns binding identity, and one of its rules runs backwards: every other grounded phase
    # is wrong when a citation fails to resolve, this one is wrong when a NEW code *does*. A
    # collision is not a new artifact but a silent redefinition of an old one.
    # Judged against the design-time baseline — the composition CR-1 was designed against, not the
    # one containing its own output. Getting this wrong makes every assigned identity collide.
    ("P7", "transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0",
     "22_p7_admissible_catalog_register.json", "ADMISSIBLE", [], 93, 5, "design"),
    ("P7", "transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0",
     "23_p7_inadmissible_catalog_register.json", "INADMISSIBLE", [
         # Two, not three: the third was the search step's `filter` input binding, removed from the
         # dossier when `LIST` was corrected to `SELECT` — `LIST` accepted no input to bind.
         "BINDING_STEP_OWNER_UNDECLARED",
         "BINDING_STEP_OWNER_UNDECLARED",
         "COMPOSITION_CC_UNDECLARED",
         "CONTRACT_WITHOUT_COMPOSITION",
         "INTERFACE_ARTIFACT_UNDECLARED",
         "INTERFACE_ARTIFACT_UNDECLARED",
         "INTERFACE_ARTIFACT_UNDECLARED",
         "NEW_CODE_MALFORMED",
         "PROVISIONAL_CODE_NEVER_BOUND",
         "STORE_WITHOUT_PROPOSED_PATH",
         "TOPOLOGY_NODE_UNDECLARED",
         "TOPOLOGY_NODE_UNDECLARED",
     ], 93, 4, "design"),
    # P8 is the only phase judged on row *order*. Every rule before it decides a row on its own; a
    # mandate can be made entirely of well-formed rows and still be unexecutable, because a dropped
    # step and a prerequisite scheduled too late exist between rows rather than in any one of them.
    # CR-1's authored mandate, judged against its own design. It does not reconcile: one artifact
    # P7 declared is scheduled nowhere, which every other P8 rule passes because the step sequence
    # stays contiguous over a hole that was never a step. Kept as authored — the finding is the
    # evidence, and rewriting the dossier to make the suite green would delete it.
    ("P8", "transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0",
     "24_p8_admissible_catalog_mandate.json", "ADMISSIBLE", [], 33, 5, "design"),
    ("P8", "transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0",
     "25_p8_inadmissible_catalog_mandate.json", "INADMISSIBLE", [
         "BUILD_STEPS_NOT_CONTIGUOUS",
         "DEPENDENCY_SCHEDULED_LATER",
         "DESIGNED_ARTIFACT_NOT_SCHEDULED",
     ], 33, 4, "design"),
    # The first two cases whose defect is in neither document. Each register is correct read alone
    # — the P2 resolves every belief it lists, the P3 re-verifies every item it names — and the
    # pipeline is wrong anyway, because a commitment was lost between them. Nothing in the suite
    # before these could fail for a reason that lives in a handoff.
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "26_p2_inadmissible_dropped_belief.json", "INADMISSIBLE", [
         "BELIEF_NOT_CARRIED_FROM_P1",
     ], 64, 3),
    ("P3", "transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0",
     "27_p3_inadmissible_restated_result.json", "INADMISSIBLE", [
         "BELIEF_RESULT_RESTATED_FROM_P2",
     ], 48, 3),
    # Reconciliation, both directions. A mandate scheduling everything the design declared is the
    # corpus's only fully reconciled one; the second schedules an identity no phase ever designed,
    # which reads as an ordinary well-formed row.
    ("P8", "transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0",
     "29_p8_inadmissible_undesigned_artifact.json", "INADMISSIBLE", [
         "SCHEDULED_ARTIFACT_NOT_DESIGNED",
     ], 33, 4, "design"),
    # The two edges at the ends of the pipeline. Neither defect is visible in the document that
    # carries it: a change request missing an acceptance criterion is a well-formed change request,
    # and a design that never binds a provisional code is a complete design.
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "30_p1_inadmissible_dropped_criterion.json", "INADMISSIBLE", [
         "SEED_ROW_NOT_CARRIED",
     ], 167, 3),
    ("P7", "transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0",
     "31_p7_inadmissible_unbound_code.json", "INADMISSIBLE", [
         "INTERFACE_ARTIFACT_UNDECLARED",
         "INTERFACE_ARTIFACT_UNDECLARED",
         "PROVISIONAL_CODE_NEVER_BOUND",
     ], 93, 4, "design"),
    # The last two handoffs. P4's consolidation loses a decision P3 committed to; P7 drops a reused
    # artifact P6 declared a dependency satisfied by. The second fires two rules on one edit — an
    # artifact that is inventoried is also composed, so removing it is visible from both directions.
    # Only the cross-phase rule would fire for a dependency satisfied by an artifact the design
    # never referenced at all.
    ("P4", "transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0",
     "32_p4_inadmissible_dropped_decision.json", "INADMISSIBLE", [
         "AUTHORING_DECISION_NOT_CONSOLIDATED",
     ], 68, 4),
    ("P7", "transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0",
     "33_p7_inadmissible_dropped_reuse.json", "INADMISSIBLE", [
         "COMPOSITION_STEP_UNDECLARED",
         "SATISFIED_DEPENDENCY_NOT_INVENTORIED",
     ], 93, 4, "design"),
    # The other face of reconciliation: an artifact the design declared that the mandate schedules
    # nowhere. CR-1's own mandate carried this defect until the dossier was completed, so the
    # corpus has to carry it now — it is the one the P7↔P8 rule was built for.
    ("P8", "transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0",
     "35_p8_inadmissible_dropped_artifact.json", "INADMISSIBLE", [
         "DESIGNED_ARTIFACT_NOT_SCHEDULED",
     ], 33, 4, "design"),
    ("P6", "transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0",
     "34_p6_inadmissible_unplaced_scope.json", "INADMISSIBLE", [
         "IN_SCOPE_CAPABILITY_UNPLACED",
     ], 45, 4),
]


PHASE_TEMPLATE = {"P0": "p0", "P1": "p1", "P2": "p2", "P3": "p3", "P4": "p4", "P5": "p5", "P6": "p6", "P7": "p7", "P8": "p8"}


def merit_of(surface: dict, payload: dict, phase: str, policy: dict) -> Merit:
    """The figure of merit for a judged document.

    Derived here rather than returned by the workflow: admissibility is what the composition
    decides, and quality is a read over the result. A runtime that scored its own output would be
    asserting an opinion the snapshot never declared.
    """
    from transformation.design.oracle import Verdict, Finding
    from transformation.design.read import parse_text

    verdict = Verdict(
        verdict=surface.get("verdict"),
        seed="",
        rules_evaluated=surface.get("rules_evaluated") or 0,
        findings=[
            Finding(rule=f["rule"], where=f.get("where", ""), detail=f.get("detail", ""),
                    intent=f.get("intent", ""))
            for f in (surface.get("findings") or [])
        ],
    )
    text = payload.get("register_text") or payload.get("seed_text") or ""
    from transformation.design.evaluate import ParsedDocument
    header, sections, registers = parse_text(text)
    doc = ParsedDocument(header=header, sections=sections, registers=registers, raw=text, path="")
    return rate(verdict, doc, policy)


# A CR's dossier is judged against the composition it was DESIGNED against, never against one that
# already contains its own output. CR-1's design assigns 23 identities; once those are built, every
# one of them collides — correctly, and fatally for any attempt to re-validate the design.
#
# The baseline does not need archiving. Snapshots are dispensable and reassembled at will, so the
# design-time composition is *reproduced* on demand from the same compiled domains minus the one
# the CR authored — cheaper than storing it, and it cannot go stale *provided the reproduction is
# actually re-run*. Caching it under /tmp keyed on nothing is what makes it go stale: a P8 rule was
# added and compiled, and three cases were judged against a baseline still carrying the previous
# sealed rule set, reporting "30 rules evaluated" against 32 declared. Reproduction is now
# conditional on the sources being no newer than the cache.
DESIGN_BASELINE = Path("/tmp/pgc_cr01_design_baseline")

DESIGN_BASELINE_ROOTS = [
    WORKSPACE / "software_governance",
    WORKSPACE / "conformance_workloads" / "workloads" / "collatz",
    WORKSPACE / "business_domains" / "ai_governance",
    WORKSPACE / "snapshot_inspector",
    REPO,
]


def _baseline_is_stale() -> bool:
    """Whether any source domain has been recompiled since the baseline was reproduced.

    A cached snapshot is only a reproduction while its inputs have not moved. Checking `is_file()`
    alone answers "was this ever built", which is a different question and the one that let a stale
    composition judge a freshly compiled rule set.
    """
    manifest = DESIGN_BASELINE / "manifest.json"
    if not manifest.is_file():
        return True
    built_at = manifest.stat().st_mtime
    for root in DESIGN_BASELINE_ROOTS:
        compiled = root / "snapshot" / "compiled"
        if any(f.stat().st_mtime > built_at for f in compiled.rglob("*.json")):
            return True
    return False


def design_baseline() -> str:
    """The composition CR-1 was designed against, reproduced whenever its sources have moved."""
    if _baseline_is_stale():
        import os
        import shutil
        import subprocess

        # Reassembling over a populated directory would leave the previous reproduction's artifacts
        # behind, which is the same staleness one level down.
        shutil.rmtree(DESIGN_BASELINE, ignore_errors=True)
        roots = ":".join(str(r / "snapshot" / "compiled") for r in DESIGN_BASELINE_ROOTS)
        env = {**os.environ,
               "PGC_SOURCE_ROOTS": roots,
               "PGC_SNAPSHOT_OUT": str(DESIGN_BASELINE)}
        subprocess.run([str(WORKSPACE / "snapshot_assembler" / "assemble.sh")],
                       env=env, capture_output=True, check=True)
    return str(DESIGN_BASELINE)


def main() -> int:
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else str(REPO.parent / "snapshot")
    data_root = str(REPO.parent / "data" / "transformation")
    # The deduction weights are governance, read from the composition like the rule sets.
    policy = load_policy(snapshot_root)

    phases = sorted({c[0] for c in CASES})
    print(f"e2e phases — {len(CASES)} case(s) across {len(phases)}: {', '.join(phases)}")
    print(f"  snapshot {snapshot_root}\n")

    failures = 0
    for case in CASES:
        phase, wf, payload_file, want_verdict, want_rule_ids, want_rules, want_rating = case[:7]
        # A case may name the composition it is judged against; most use the live snapshot.
        case_snapshot = design_baseline() if len(case) > 7 and case[7] == "design" else snapshot_root
        path = PAYLOADS / payload_file
        if not path.is_file():
            print(f"  MISSING  {phase}  {payload_file} — run scripts/testbed/build_payloads.py")
            failures += 1
            continue

        payload = json.loads(path.read_text(encoding="utf-8"))
        result = api.run_workflow(
            wf_fqdn=wf, payload=payload, snapshot_root=case_snapshot, data_root=data_root
        )

        verdict = result.surface.get("verdict")
        fired = sorted(f["rule"] for f in (result.surface.get("findings") or []))
        expected = sorted(want_rule_ids)
        rules = result.surface.get("rules_evaluated")

        # A workflow that judges a document correctly still completes successfully: an inadmissible
        # verdict is a governed outcome, not an execution failure. Status VIOLATION would mean the
        # phase itself is broken.
        problems = []
        if result.status != "SUCCESS":
            problems.append(f"status {result.status}")
        if verdict != want_verdict:
            problems.append(f"verdict {verdict} != {want_verdict}")
        if fired != expected:
            # Compared as multisets, not as sets. Membership tests alone report nothing when a rule
            # fires twice against one expected occurrence — the lists differ, `missing` and
            # `unexpected` both come back empty, and the case prints OK over a real change in what
            # the phase found. That is how a second SEED_ROW_NOT_CARRIED went unreported here.
            fired_counts, expected_counts = Counter(fired), Counter(expected)
            missing = sorted((expected_counts - fired_counts).elements())
            unexpected = sorted((fired_counts - expected_counts).elements())
            if missing:
                problems.append(f"rules that did not fire: {missing}")
            if unexpected:
                problems.append(f"rules that fired unexpectedly: {unexpected}")
        if rules != want_rules:
            problems.append(f"rules evaluated {rules} != {want_rules}")

        # The runtime returns the verdict, not the rating: the figure of merit is a read over the
        # judged document, and re-deriving it here keeps the runtime free of a quality opinion.
        merit = merit_of(result.surface, payload, phase, policy)
        if merit.rating != want_rating:
            problems.append(f"figure of merit {merit.rating}/5 != {want_rating}/5")

        # PASS/FAIL, not the verdict. ADMISSIBLE and INADMISSIBLE are both correct outcomes — half
        # these cases exist to be refused — so printing the verdict in the result column invited
        # reading a governed refusal as a broken test. What this line reports is whether the case
        # matched what it declared, and the verdict appears below only when it did not.
        print(
            f"  {'PASS' if not problems else 'FAIL'}  {phase}  {payload_file:<40} "
            f"{len(fired):>2} finding(s)  {rules} rules  "
            f"{merit.stars} {merit.rating}/{merit.maximum}"
        )
        if problems:
            failures += 1
            print(f"          verdict {verdict}; {'; '.join(problems)}")

    print()
    if failures:
        print(f"E2E FAILED — {failures} of {len(CASES)} case(s) did not match")
        return 1
    print(f"E2E PASSED — {len(CASES)} case(s), every phase executed through the runtime")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
