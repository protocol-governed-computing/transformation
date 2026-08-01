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

from runtime import api

REPO = Path(__file__).resolve().parents[2]
PAYLOADS = REPO / "testbed" / "phases" / "test_payloads"

# phase, workflow, payload file, expected verdict, expected rule ids, expected rules evaluated.
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
     "01_admissible_seed.json", "ADMISSIBLE", [], 75),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "02_admissible_reference.json", "ADMISSIBLE", [], 75),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "03_inadmissible_seven_violations.json", "INADMISSIBLE", [
         "BELIEF_STATED_AS_FACT",
         "BELIEF_WITHOUT_VERIFICATION_GOAL",
         "CERTAINTY_NOT_IN_VOCABULARY",
         "CR_TYPE_NOT_DECLARED",
         "DESIGN_LEAKED_INTO_SEED",
         "HEADER_FIELD_MISSING",
         "SCOPE_RELATIONSHIP_NOT_IN_VOCABULARY",
     ], 75),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "04_inadmissible_structural.json", "INADMISSIBLE", [
         "SECTION_MISNUMBERED",
         "SECTION_OUT_OF_ORDER",
     ], 75),
    ("P0", "transformation::WF_P0_SEED_ADMISSIBILITY_V0",
     "05_inadmissible_truncated.json", "INADMISSIBLE", [
         "SECTION_MISSING", "SECTION_MISSING", "SECTION_MISSING",
         "SECTION_MISSING", "SECTION_MISSING", "SECTION_MISSING",
     ], 75),
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "06_p1_admissible_register.json", "ADMISSIBLE", [], 94),
    ("P1", "transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0",
     "07_p1_inadmissible_register.json", "INADMISSIBLE", [
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "ROW_WITHOUT_SOURCE_FINDING",
         "SOURCE_FINDING_UNRESOLVED",
     ], 94),
]


def main() -> int:
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else str(REPO.parent / "snapshot")
    data_root = str(REPO.parent / "data" / "transformation")

    phases = sorted({c[0] for c in CASES})
    print(f"e2e phases — {len(CASES)} case(s) across {len(phases)}: {', '.join(phases)}")
    print(f"  snapshot {snapshot_root}\n")

    failures = 0
    for phase, wf, payload_file, want_verdict, want_rule_ids, want_rules in CASES:
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

        mark = "OK   " if not problems else "FAIL "
        print(
            f"  {mark}  {phase}  {payload_file:<38} "
            f"{str(verdict):<13} {len(fired):>2} finding(s)  {rules} rules"
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
