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
from transformation.phases.merit import Merit, load_policy, rate
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
     "01_admissible_seed.json", "ADMISSIBLE", [], 68, 4),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "02_admissible_reference.json", "ADMISSIBLE", [], 68, 4),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "03_inadmissible_seven_violations.json", "INADMISSIBLE", [
         "BELIEF_STATED_AS_FACT",
         "BELIEF_WITHOUT_VERIFICATION_GOAL",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "LIFECYCLE_STATE_NOT_IN_VOCABULARY",
     ], 68, 3),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "04_inadmissible_structural.json", "INADMISSIBLE", ["REGISTER_MISSING"], 68, 3),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "05_inadmissible_truncated.json", "INADMISSIBLE", ["REGISTER_MISSING"] * 8, 68, 4),
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "06_p1_admissible_register.json", "ADMISSIBLE", [], 94, 4),
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "07_p1_inadmissible_register.json", "INADMISSIBLE", [
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "ROW_WITHOUT_SOURCE_FINDING",
         "SOURCE_FINDING_UNRESOLVED",
     ], 94, 3),
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "08_p2_admissible_register.json", "ADMISSIBLE", [], 62, 4),
    # Grounding: a misspelled identity and a right-code/wrong-namespace one are defects; an
    # identity simply absent from the baseline is proposed-new and correctly goes unflagged.
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "09_p2_inadmissible_register.json", "INADMISSIBLE", [
         "BASELINE_IDENTITY_UNRESOLVED",
         "BASELINE_IDENTITY_UNRESOLVED",
     ], 62, 2),
    # CR-1 — the same three phases over a business subject. CR-0 is the pipeline authoring its own
    # domain, so it grounds every claim against artifacts this repo also wrote; the catalog CR
    # grounds against a composition it contributed nothing to, which is the harder case.
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "10_p0_admissible_catalog_seed.json", "ADMISSIBLE", [], 68, 4),
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "11_p1_admissible_catalog_register.json", "ADMISSIBLE", [], 94, 4),
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "12_p2_admissible_catalog_register.json", "ADMISSIBLE", [], 62, 4),
    # The rules must bite on business content, not only on documents about the pipeline. A
    # misspelled identity and a right-code/wrong-namespace one are defects; design leaking into a
    # business-language cell is a third. An identity merely absent from the baseline stays
    # unflagged — that is proposed-new, which is what a CR is for.
    ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
     "13_p2_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "BASELINE_IDENTITY_UNRESOLVED",
         "BASELINE_IDENTITY_UNRESOLVED",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
     ], 62, 1),
    # P3 decides, so it observes twice: the artifact list resolves identities, the composition
    # summary carries what each domain declares about being reused. The inadmissible case offers a
    # business CR a pipeline capability and a conformance workload — a confusion that is invisible
    # in the document and only a declaration can settle.
    ("P3", "transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0",
     "14_p3_admissible_catalog_register.json", "ADMISSIBLE", [], 46, 4),
    ("P3", "transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0",
     "15_p3_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "REUSE_CANDIDATE_NOT_ELIGIBLE",
         "REUSE_CANDIDATE_NOT_ELIGIBLE",
     ], 46, 3),
    # P4 consolidates: its defects live between registers, where every register is individually
    # well formed and the document as a whole asserts something untrue. The admissible case is the
    # corpus's only 5/5 — a consolidation carries no open questions of its own, because P3
    # resolved them.
    ("P4", "transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0",
     "16_p4_admissible_catalog_register.json", "ADMISSIBLE", [], 67, 5),
    ("P4", "transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0",
     "17_p4_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "DEPENDENCY_IDENTITY_UNRESOLVED",
         "GAP_ENTRY_UNDECLARED",
         "GAP_WITHOUT_OWNER",
         "SCOPE_GAP_UNDECLARED",
     ], 67, 2),
]


PHASE_TEMPLATE = {"P0": "p0", "P1": "p1", "P2": "p2", "P3": "p3", "P4": "p4"}


def merit_of(surface: dict, payload: dict, phase: str, policy: dict) -> Merit:
    """The figure of merit for a judged document.

    Derived here rather than returned by the workflow: admissibility is what the composition
    decides, and quality is a read over the result. A runtime that scored its own output would be
    asserting an opinion the snapshot never declared.
    """
    from transformation.phases.oracle import Verdict, Finding
    from transformation.phases.read import parse_text

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
    from transformation.phases.evaluate import ParsedDocument
    header, sections, registers = parse_text(text)
    doc = ParsedDocument(header=header, sections=sections, registers=registers, raw=text, path="")
    return rate(verdict, doc, policy)


def main() -> int:
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else str(REPO.parent / "snapshot")
    data_root = str(REPO.parent / "data" / "transformation")
    # The deduction weights are governance, read from the composition like the rule sets.
    policy = load_policy(snapshot_root)

    phases = sorted({c[0] for c in CASES})
    print(f"e2e phases — {len(CASES)} case(s) across {len(phases)}: {', '.join(phases)}")
    print(f"  snapshot {snapshot_root}\n")

    failures = 0
    for phase, wf, payload_file, want_verdict, want_rule_ids, want_rules, want_rating in CASES:
        path = PAYLOADS / payload_file
        if not path.is_file():
            print(f"  MISSING  {phase}  {payload_file} — run scripts/testbed/build_payloads.py")
            failures += 1
            continue

        payload = json.loads(path.read_text(encoding="utf-8"))
        result = api.run_workflow(
            wf_fqdn=wf, payload=payload, snapshot_root=snapshot_root, data_root=data_root
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
            missing = [r for r in expected if r not in fired]
            unexpected = [r for r in fired if r not in expected]
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

        mark = "OK   " if not problems else "FAIL "
        print(
            f"  {mark}  {phase}  {payload_file:<40} "
            f"{str(verdict):<13} {len(fired):>2} finding(s)  {rules} rules  "
            f"{merit.stars} {merit.rating}/{merit.maximum}"
        )
        if problems:
            failures += 1
            print(f"          {'; '.join(problems)}")

    print()
    if failures:
        print(f"E2E FAILED — {failures} of {len(CASES)} case(s) did not match")
        return 1
    print(f"E2E PASSED — {len(CASES)} case(s), every phase executed through the runtime")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
