# Stage 7 — Design Intent: ai_governance / ai_licensing

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_01_licensing
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
    - Decision: Each check is stated whole, as it stands, with its cases
      Business Fact: A case belongs to a transform the design names
      Resolution: The three checks are redeclared with the inputs, outputs, implementation and refusal they already declare
      Source Finding: 'S4 design_decisions #1'
    - Decision: A no case expects a refusal; a yes case keeps its answer
      Business Fact: The checks refuse, as the business decided
      Resolution: Each check has one SUCCESS case with its answer and one VIOLATION case
      Source Finding: 'S4 design_decisions #2'
    - Decision: The earlier values stay, under this system's names, with one boundary case added
      Business Fact: The author answered both
      Resolution: The earlier values are kept; the inactivity check gains a license unused for exactly the threshold
      Source Finding: 'S4 design_decisions #3'
    - Decision: The build configuration is reached through its generator
      Business Fact: It is derived from the design
      Resolution: The build manifest is named as generated, so the domain compiles the stated cases
      Source Finding: 'S4 design_decisions #4'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Evaluate whether license quota remains available under the declared cap
      Reason: Stated whole with the cases that prove it.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Evaluate whether required training has been completed
      Reason: Stated whole with the cases that prove it.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Evaluate license inactivity against a declared threshold
      Reason: Stated whole with the cases that prove it.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Declares what the ai_governance domain compiles
      Reason: It does not compile stated cases and must.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Runs the training and license checks for provisioning, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Runs the inactivity check for reclamation, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows: []
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
    rows: []
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows: []
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
    - Artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: assigned_count
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Number of licenses currently assigned
    - Artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: quota
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Declared license cap
    - Artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: quota_available
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: True when at least one license remains under the cap
    - Artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: remaining
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Licenses remaining under the cap, floored at zero
    - Artifact: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: training_completed
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the employee has completed required AI-use training
    - Artifact: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: training_eligible
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: True when training is complete and the employee clears this gate
    - Artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: last_active_date
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: ISO-8601 date or date-time of last recorded license activity
    - Artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: evaluation_date
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: ISO-8601 date or date-time the evaluation is made as of — declared, never a clock read
    - Artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: threshold_days
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Inactivity threshold in days
    - Artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: is_inactive
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: True when days_inactive meets or exceeds threshold_days
    - Artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: days_inactive
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whole days elapsed between last_active_date and evaluation_date
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
    rows:
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Module: ai_governance.implementation.capability_transforms.atoms.ct_pure_check_quota_available_v0
      Callable: execute
      Operation: PURE_CHECK_QUOTA_AVAILABLE
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - CT Code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Module: ai_governance.implementation.capability_transforms.atoms.ct_pure_check_training_status_v0
      Callable: execute
      Operation: PURE_CHECK_TRAINING_STATUS
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Module: ai_governance.implementation.capability_transforms.atoms.ct_pure_evaluate_inactivity_v0
      Callable: execute
      Operation: PURE_EVALUATE_INACTIVITY
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
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
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows: []
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
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
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: ai_licensing
      Count: '4'
      Artifacts: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0, ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0, ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0, ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
      Generator: transformation.build.render:build_manifest
      Generator Sources: S8 build_order, S8 field_declarations, transformation/design/families.py
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
  declared_reach:
    columns:
    - Act
    - Consults
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
    rows: []
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
    rows:
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Case: available_under_cap
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Case: refuses_at_cap
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Case: eligible_once_trained
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Case: refuses_untrained
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_past_threshold
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_at_threshold
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: refuses_recently_used
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
  test_case_values:
    columns:
    - CT Code
    - Case
    - Role (INPUT, EXPECTED, ASSERT, RECORDED)
    - Field
    - Value
    - Source Finding
    rows:
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Case: available_under_cap
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: assigned_count
      Value: '5'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Case: available_under_cap
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: quota
      Value: '10'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Case: available_under_cap
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: quota_available
      Value: 'true'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Case: available_under_cap
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: remaining
      Value: '5'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Case: refuses_at_cap
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: assigned_count
      Value: '10'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Case: refuses_at_cap
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: quota
      Value: '10'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Case: eligible_once_trained
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: training_completed
      Value: 'true'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Case: eligible_once_trained
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: training_eligible
      Value: 'true'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Case: refuses_untrained
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: training_completed
      Value: 'false'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_past_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: last_active_date
      Value: '"2024-01-01T00:00:00Z"'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_past_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: evaluation_date
      Value: '"2024-02-15T00:00:00Z"'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_past_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: threshold_days
      Value: '30'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_past_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: is_inactive
      Value: 'true'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_past_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: days_inactive
      Value: '45'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_at_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: last_active_date
      Value: '"2024-01-16T00:00:00Z"'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_at_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: evaluation_date
      Value: '"2024-02-15T00:00:00Z"'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_at_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: threshold_days
      Value: '30'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_at_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: is_inactive
      Value: 'true'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: inactive_at_threshold
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: days_inactive
      Value: '30'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: refuses_recently_used
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: last_active_date
      Value: '"2024-02-10T00:00:00Z"'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: refuses_recently_used
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: evaluation_date
      Value: '"2024-02-15T00:00:00Z"'
      Source Finding: human decision
    - CT Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Case: refuses_recently_used
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: threshold_days
      Value: '30'
      Source Finding: human decision
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows: []
```

Every binding names a field the capability declares, read from the pinned baseline
`25009fed290d52c7b699f7fdd85f653c594306b48568bd9d351d8e63a79ca843`.

Nothing new is authored. The three checks are redeclared whole, each with the cases that prove it;
the domain's build manifest is regenerated so that the domain compiles those cases. What each check
decides, and every act that uses them, is unchanged.

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

## 9. Implementation Bindings

---

## 10. Vocabulary Extensions

---

## 11. Runtime Policies

---

## 12. Artifact Properties

---

## 13. STRUCTURE Stores

---

## 14. Transport Bindings

---

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

---

## 18. Refusal Discharge

---

## 19. Refusal Deferrals

---

## 20. Refusal — Governance-Surface Discharge

---

## 21. Molecule Steps

---

## 22. Molecule Step Bindings

---

## 23. Test Cases

---

## 24. Test Case Values

---

## 25. Withdrawn Facts

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
