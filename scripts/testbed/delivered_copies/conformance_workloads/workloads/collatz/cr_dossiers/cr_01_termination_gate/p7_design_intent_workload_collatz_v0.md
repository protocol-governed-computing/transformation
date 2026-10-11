# Stage 7 — Design Intent: workload / collatz

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_01_termination_gate
  Status: DRAFT
  Feeds: Stage 8 — Authoring Mandate
registers:
  design_resolution:
    columns:
    - Decision
    - Business Fact
    - Resolution
    - Source Finding
    rows:
    - Decision: A capability decides
      Business Fact: A decision is made by a capability
      Resolution: workload::CC_VERIFY_TERMINATION_V1 runs workload::CT_PURE_TERMINATION_CHECK_V0 unchanged in check_termination, then capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 in require_every_sequence_terminated, with value all_terminate and allowed_set holding only true; the second refuses when a sequence did not end at 1
      Source Finding: 'S4 design_decisions #1'
    - Decision: The gate routes on its steps
      Business Fact: Routing is a lookup
      Resolution: Each step routes SUCCESS to continue and VIOLATION to exit, and workload::CC_VERIFY_TERMINATION_V1 declares no evaluation block; its inputs and allowed outcomes are those of workload::CC_VERIFY_TERMINATION_V0, and it adds the output conjecture_holds, because every step declares what it reports
      Source Finding: 'S4 design_decisions #2'
    - Decision: The workflow runs the new gate
      Business Fact: It decides as today
      Resolution: 'workload::WF_COLLATZ_CONJECTURE_V0 is re-pointed: the place labelled CC_VERIFY_TERMINATION_V0 runs workload::CC_VERIFY_TERMINATION_V1; its label, routes and the store''s bindings to it are unchanged'
      Source Finding: 'S4 design_decisions #3'
    - Decision: A new version
      Business Fact: A change of meaning is a new identity
      Resolution: workload::CC_VERIFY_TERMINATION_V1 supersedes workload::CC_VERIFY_TERMINATION_V0
      Source Finding: 'S4 design_decisions #4'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: workload::CC_VERIFY_TERMINATION_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: ''
      Reason: Routes to a condition nothing runs. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: workload::WF_COLLATZ_CONJECTURE_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Runs the gate being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: workload::CT_PURE_TERMINATION_CHECK_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Reports whether every sequence ended at 1, and which did not, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Refuses a value not in a declared set, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: workload::CC_STORE_RESULTS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Records the sequences and the check's findings, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: Gate the conjecture
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: workload::CC_VERIFY_TERMINATION_V1
      Summary: Verify all Collatz sequences terminate at 1
      Owner Subdomain: collatz
      Status: NEW
      Source Finding: 'S6 governance_outcome #1'
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: NONE IDENTIFIED
      Binds WF: ''
      CS Bindings: ''
      Storage Structure: ''
      Source Finding: ''
  execution_topology:
    columns:
    - Workflow
    - Node
    - Runs
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: NONE IDENTIFIED
      Node: ''
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): ''
      Routing: ''
      Source Finding: ''
  cc_composition:
    columns:
    - CC Code
    - Step
    - Step Name
    - Capability
    - Kind (CT, CS)
    - Operation
    - Store
    - Consumes
    - Produces
    - Routing
    - Interpreted By
    - Semantic Status
    - Interface
    rows:
    - CC Code: workload::CC_VERIFY_TERMINATION_V1
      Step: '1'
      Step Name: check_termination
      Capability: workload::CT_PURE_TERMINATION_CHECK_V0
      Kind (CT, CS): CT
      Operation: PURE_TERMINATION_CHECK
      Store: —
      Consumes: sequences
      Produces: all_terminate, non_terminating
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: sequences=sequences; out: all_terminate=all_terminate, non_terminating=non_terminating'
    - CC Code: workload::CC_VERIFY_TERMINATION_V1
      Step: '2'
      Step Name: require_every_sequence_terminated
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: all_terminate
      Produces: conjecture_holds
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=all_terminate, allowed_set=true only; out: is_member=conjecture_holds'
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: workload::CC_VERIFY_TERMINATION_V1
      Step: check_termination
      Direction (INPUT, OUTPUT): INPUT
      Field: sequences
      Bound To: inputs.sequences
      Source Finding: S7 cc_composition check_termination
    - Owner: workload::CC_VERIFY_TERMINATION_V1
      Step: check_termination
      Direction (INPUT, OUTPUT): OUTPUT
      Field: all_terminate
      Bound To: capability_result.all_terminate
      Source Finding: S7 cc_composition check_termination
    - Owner: workload::CC_VERIFY_TERMINATION_V1
      Step: check_termination
      Direction (INPUT, OUTPUT): OUTPUT
      Field: non_terminating
      Bound To: capability_result.non_terminating
      Source Finding: S7 cc_composition check_termination
    - Owner: workload::CC_VERIFY_TERMINATION_V1
      Step: require_every_sequence_terminated
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.check_termination.all_terminate
      Source Finding: S7 cc_composition require_every_sequence_terminated
    - Owner: workload::CC_VERIFY_TERMINATION_V1
      Step: require_every_sequence_terminated
      Direction (INPUT, OUTPUT): INPUT
      Field: allowed_set
      Bound To: '[True]'
      Source Finding: S7 cc_composition require_every_sequence_terminated
    - Owner: workload::CC_VERIFY_TERMINATION_V1
      Step: require_every_sequence_terminated
      Direction (INPUT, OUTPUT): OUTPUT
      Field: conjecture_holds
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition require_every_sequence_terminated
  interface_fields:
    columns:
    - Artifact
    - Direction (INPUT, OUTPUT, ATTRIBUTE)
    - Field
    - Type
    - Required (YES, NO)
    - Default
    - Meaning
    rows:
    - Artifact: workload::CC_VERIFY_TERMINATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: sequences
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The sequences computed for a run
    - Artifact: workload::CC_VERIFY_TERMINATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: all_terminate
      Type: boolean
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Whether every sequence ends at 1
    - Artifact: workload::CC_VERIFY_TERMINATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: non_terminating
      Type: array
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The numbers whose sequences did not end at 1
    - Artifact: workload::CC_VERIFY_TERMINATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: conjecture_holds
      Type: boolean
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: True when every sequence ended at 1; the gate refuses otherwise
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: workload::CC_VERIFY_TERMINATION_V1
      Property: supersedes
      Value: workload::CC_VERIFY_TERMINATION_V0
      Source Finding: 'S4 design_decisions #4'
    - Artifact: workload::CC_VERIFY_TERMINATION_V1
      Property: description
      Value: Protocol gate for Collatz Conjecture — SUCCESS means conjecture holds for this input set
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows: []
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: collatz
      Count: '1'
      Artifacts: workload::CC_VERIFY_TERMINATION_V1
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Subdomain: collatz
      Count: '1'
      Artifacts: workload::CC_VERIFY_TERMINATION_V0
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows: []
  implementation_bindings:
    columns:
    - CT Code
    - Module
    - Callable
    - Operation
    - Kind (atom, molecule)
    - Purity (ct_pure, ct_impure)
    - Refusal (raises, returns, never)
    - Source Finding
    rows: []
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Group
    - Casing
    - Value
    - Meaning
    - Source Finding
    rows: []
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows: []
  transport_bindings:
    columns:
    - Artifact
    - Direction (INGRESS, EGRESS)
    - Operation
    - Handler Kind (WF_INVOCATION, SNAPSHOT_READ)
    - Handler Target
    - Field
    - Bound To
    - Source Finding
    rows: []
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows: []
  refusal_discharge:
    columns:
    - Operation
    - Refused When
    - Act
    - Step
    - Outcome
    - Source Finding
    rows: []
  refusal_deferrals:
    columns:
    - Operation
    - Refused When
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Operation: Gating the conjecture
      Refused When: A sequence does not end at 1
      Deferred To: workload::CC_VERIFY_TERMINATION_V1, step require_every_sequence_terminated, which ends the gate VIOLATION; the workflow routes it to EXIT_CONJECTURE_VIOLATED
      Until: Armed by this change
      Source Finding: 'S0 operation_refusals #1'
  refusal_governance_discharge:
    columns:
    - Operation
    - Refused When
    - Phase
    - Governing Rule
    - Source Finding
    rows: []
  molecule_steps:
    columns:
    - CT Code
    - Step
    - Kind (atom, molecule, loop)
    - Target
    - Over
    - Iterator
    - Emits
    - Source Finding
    rows: []
  molecule_step_bindings:
    columns:
    - CT Code
    - Step
    - Role (INPUT, CARRY, UPDATE)
    - Field
    - Bound To
    - Source Finding
    rows: []
  test_cases:
    columns:
    - CT Code
    - Case
    - Expected Outcome (SUCCESS, VIOLATION)
    - Source Finding
    rows: []
  test_case_values:
    columns:
    - CT Code
    - Case
    - Role (INPUT, EXPECTED, ASSERT, RECORDED)
    - Field
    - Value
    - Source Finding
    rows: []
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows: []
```

Read against the pinned baseline
`d42ef69df1b0b2f03d40c896076bb718ef333f383e58a1a29d54e68b229f921e`.

The termination gate is replaced by a version that decides: after the unchanged termination check
reports, the platform's set-membership check refuses unless every sequence ended at 1. Both steps
route on their own outcomes, and the gate declares no condition. The workflow is re-pointed to run
the new gate, and nothing else about it changes.

---

## 1. Design Decisions Resolution

---

## 2. Artifact Inventory — Existing Artifacts

---

## 3. Artifact Family Mapping — New Artifacts

---

## 4. Runtime Binding (RB) Declarations

---

## 5. Execution Topology

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Artifact Properties

---

## 10. Structure Stores

---

## 11. Artifact Summary

---

## 12. Declared Reach

---

## 13. Unchanged Registers

No transform, vocabulary, policy, entrance or generator is touched. The workflow is re-pointed, not restated.

---

## 14. Refusal Discharge

The business declared one refusal. It is made in the new gate, which the workflow runs at a place
this design re-points and does not restate, so it is deferred to that step rather than discharged at
a place of the design's own topology.

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn. The workload declares no test data.
