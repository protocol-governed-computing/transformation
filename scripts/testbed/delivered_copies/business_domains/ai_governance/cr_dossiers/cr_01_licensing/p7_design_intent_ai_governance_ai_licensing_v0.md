# Stage 7 — Design Intent: ai_governance / ai_licensing

## Machine

```yaml
document:
  phase: p7
  domain: ai_governance
  subdomain: ai_licensing
  cr: cr_01_licensing
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Each check is stated whole, as it stands, with its cases
    business_fact: A case belongs to a transform the design names
    resolution: The three checks are redeclared with the inputs, outputs, implementation and refusal they already declare
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: A no case expects a refusal; a yes case keeps its answer
    business_fact: The checks refuse, as the business decided
    resolution: Each check has one SUCCESS case with its answer and one VIOLATION case
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: The earlier values stay, under this system's names, with one boundary case added
    business_fact: The author answered both
    resolution: The earlier values are kept; the inactivity check gains a license unused for exactly the threshold
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: The build configuration is reached through its generator
    business_fact: It is derived from the design
    resolution: The build manifest is named as generated, so the domain compiles the stated cases
    source_finding: {phase: p4, register: design_decisions, row: 4}
  existing_inventory:
  - fqdn: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    action: EXTEND
    summary: Evaluate whether license quota remains available under the declared cap
    reason: Stated whole with the cases that prove it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    action: EXTEND
    summary: Evaluate whether required training has been completed
    reason: Stated whole with the cases that prove it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    action: EXTEND
    summary: Evaluate license inactivity against a declared threshold
    reason: Stated whole with the cases that prove it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
    action: EXTEND
    summary: Declares what the ai_governance domain compiles
    reason: It does not compile stated cases and must.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    action: REUSE
    summary: ''
    reason: Runs the training and license checks for provisioning, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    action: REUSE
    summary: ''
    reason: Runs the inactivity check for reclamation, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  new_artifacts: null
  rb_declarations: []
  execution_topology: []
  cc_composition: null
  step_bindings: null
  interface_fields:
  - artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    direction: INPUT
    field: assigned_count
    type: integer
    required: 'YES'
    default: ''
    meaning: Number of licenses currently assigned
  - artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    direction: INPUT
    field: quota
    type: integer
    required: 'YES'
    default: ''
    meaning: Declared license cap
  - artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    direction: OUTPUT
    field: quota_available
    type: boolean
    required: 'YES'
    default: ''
    meaning: True when at least one license remains under the cap
  - artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    direction: OUTPUT
    field: remaining
    type: integer
    required: 'YES'
    default: ''
    meaning: Licenses remaining under the cap, floored at zero
  - artifact: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    direction: INPUT
    field: training_completed
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the employee has completed required AI-use training
  - artifact: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    direction: OUTPUT
    field: training_eligible
    type: boolean
    required: 'YES'
    default: ''
    meaning: True when training is complete and the employee clears this gate
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: INPUT
    field: last_active_date
    type: string
    required: 'YES'
    default: ''
    meaning: ISO-8601 date or date-time of last recorded license activity
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: INPUT
    field: evaluation_date
    type: string
    required: 'YES'
    default: ''
    meaning: ISO-8601 date or date-time the evaluation is made as of — declared, never a clock read
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: INPUT
    field: threshold_days
    type: integer
    required: 'YES'
    default: ''
    meaning: Inactivity threshold in days
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: OUTPUT
    field: is_inactive
    type: boolean
    required: 'YES'
    default: ''
    meaning: True when days_inactive meets or exceeds threshold_days
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: OUTPUT
    field: days_inactive
    type: integer
    required: 'YES'
    default: ''
    meaning: Whole days elapsed between last_active_date and evaluation_date
  implementation_bindings:
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    callable: execute
    operation: PURE_CHECK_QUOTA_AVAILABLE
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    callable: execute
    operation: PURE_CHECK_TRAINING_STATUS
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    callable: execute
    operation: PURE_EVALUATE_INACTIVITY
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  vocabulary_extensions: null
  runtime_policies: null
  artifact_properties: null
  structure_stores: null
  transport_bindings: null
  artifact_summary:
  - action: EXTEND
    subdomain: ai_licensing
    count: '4'
    artifacts: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0, ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0, ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0, ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
  generation_provenance:
  - artifact: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
    generator: transformation.build.render:build_manifest
    generator_sources:
    - S8 build_order
    - S8 field_declarations
    - transformation/design/families.py
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  declared_reach: null
  refusal_discharge: null
  refusal_deferrals: null
  refusal_governance_discharge: null
  molecule_steps: null
  molecule_step_bindings: null
  test_cases:
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: refuses_at_cap
    expected_outcome: VIOLATION
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: eligible_once_trained
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: refuses_untrained
    expected_outcome: VIOLATION
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: refuses_recently_used
    expected_outcome: VIOLATION
    source_finding: {source: human}
  test_case_values:
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    role: INPUT
    field: assigned_count
    value: 5
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    role: INPUT
    field: quota
    value: 10
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    role: EXPECTED
    field: quota_available
    value: true
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    role: EXPECTED
    field: remaining
    value: 5
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: refuses_at_cap
    role: INPUT
    field: assigned_count
    value: 10
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: refuses_at_cap
    role: INPUT
    field: quota
    value: 10
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: eligible_once_trained
    role: INPUT
    field: training_completed
    value: true
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: eligible_once_trained
    role: EXPECTED
    field: training_eligible
    value: true
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: refuses_untrained
    role: INPUT
    field: training_completed
    value: false
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: INPUT
    field: last_active_date
    value: '2024-01-01T00:00:00Z'
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: INPUT
    field: evaluation_date
    value: '2024-02-15T00:00:00Z'
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: INPUT
    field: threshold_days
    value: 30
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: EXPECTED
    field: is_inactive
    value: true
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: EXPECTED
    field: days_inactive
    value: 45
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: INPUT
    field: last_active_date
    value: '2024-01-16T00:00:00Z'
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: INPUT
    field: evaluation_date
    value: '2024-02-15T00:00:00Z'
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: INPUT
    field: threshold_days
    value: 30
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: EXPECTED
    field: is_inactive
    value: true
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: EXPECTED
    field: days_inactive
    value: 30
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: refuses_recently_used
    role: INPUT
    field: last_active_date
    value: '2024-02-10T00:00:00Z'
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: refuses_recently_used
    role: INPUT
    field: evaluation_date
    value: '2024-02-15T00:00:00Z'
    source_finding: {source: human}
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: refuses_recently_used
    role: INPUT
    field: threshold_days
    value: 30
    source_finding: {source: human}
  withdrawn_facts: null
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
