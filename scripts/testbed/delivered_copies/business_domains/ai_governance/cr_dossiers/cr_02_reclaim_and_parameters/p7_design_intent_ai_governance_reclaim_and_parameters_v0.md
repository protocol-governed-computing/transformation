# Stage 7 — Design Intent: ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p7
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: The removal step ends the contract on a refused removal
    business_fact: No reclaim carries on past a removal the registry refused
    resolution: The deregister_license step of ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1 routes VIOLATION to exit
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: A refused removal ends as still active
    business_fact: A license the registry did not release stays with the employee
    resolution: ai_governance::WF_AUTO_RECLAIM_V0 already routes the contract's VIOLATION to EXIT_ACTIVE; it is re-pointed and not restated
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: The check reports what it receives
    business_fact: A check reports only what it receives
    resolution: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 maps `validation_result` from the check's `valid`, a boolean
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: Next versions
    business_fact: A change of meaning is a new identity, and identity is fixed at publication
    resolution: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1 supersedes ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0, and ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 supersedes ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: The acts run the next versions
    business_fact: Each decides exactly as today
    resolution: 'ai_governance::WF_AUTO_RECLAIM_V0 and ai_governance::WF_GOVERN_AGENT_ACTION_V0 are re-pointed: the place that runs each contract runs its next version; its label and routes are unchanged'
    source_finding: {phase: p4, register: design_decisions, row: 5}
  existing_inventory:
  - fqdn: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    action: REPLACE
    summary: ''
    reason: Its removal step carries on past a refusal its registry declares. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    action: REUSE
    summary: ''
    reason: Named by the reclaim's next version, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: ai_governance::WF_AUTO_RECLAIM_V0
    action: REPOINT
    summary: ''
    reason: Runs the reclaim being replaced; re-pointed to its next version. It already routes the refusal to still active.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    action: REPLACE
    summary: ''
    reason: Reports a result it never receives. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    action: REPOINT
    summary: ''
    reason: Runs the parameter check being replaced; re-pointed to its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    action: REUSE
    summary: ''
    reason: Checks the parameters against the rules, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: capability_transforms::CT_PURE_LOOKUP_V0
    action: REUSE
    summary: ''
    reason: Looks up the tool's rules, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    action: REUSE
    summary: ''
    reason: Named by the reclaim's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: ai_governance::RB_LICENSE_BINDINGS_V0
    action: REUSE
    summary: ''
    reason: Binds the license registry, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    action: REUSE
    summary: ''
    reason: Places the license registry, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  new_artifacts:
  - capability: End a reclaim the registry refuses
    family: CC
    code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    summary: Reclaim license from inactive user
    owner_subdomain: ai_licensing
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 1}
  - capability: Check an action's parameters
    family: CC
    code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    summary: Enforce declared parameter constraints for an authorized tool
    owner_subdomain: agent_governance
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 2}
  rb_declarations: []
  execution_topology: []
  cc_composition:
  - cc_code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: '1'
    step_name: evaluate_inactivity
    capability: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    kind: CT
    operation: EVALUATE_INACTIVITY
    store: null
    consumes:
    - last_active_date
    - evaluation_date
    - threshold_days
    produces:
    - is_inactive
    - days_inactive
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        last_active_date: last_active_date
        evaluation_date: evaluation_date
        threshold_days: threshold_days
      out:
        is_inactive: is_inactive
        days_inactive: days_inactive
  - cc_code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: '2'
    step_name: deregister_license
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: DEREGISTER
    store: LICENSE_REGISTRY
    consumes:
    - key_or_address
    produces:
    - result_status
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      BACKEND_ERROR: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_or_address: employee_id
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    step: '1'
    step_name: lookup_parameter_rules
    capability: capability_transforms::CT_PURE_LOOKUP_V0
    kind: CT
    operation: LOOKUP
    store: null
    consumes:
    - key
    - map
    produces:
    - result
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: tool_name
        map: rules declared per tool
      out:
        result: rules
  - cc_code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    step: '2'
    step_name: validate_parameters
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: validation_result
  step_bindings:
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: evaluate_inactivity
    direction: INPUT
    field: last_active_date
    bound_to: inputs.last_active_date
    source_finding: {phase: p7, register: cc_composition, key: evaluate_inactivity}
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: evaluate_inactivity
    direction: INPUT
    field: evaluation_date
    bound_to: inputs.evaluation_date
    source_finding: {phase: p7, register: cc_composition, key: evaluate_inactivity}
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: evaluate_inactivity
    direction: INPUT
    field: threshold_days
    bound_to: inputs.threshold_days
    source_finding: {phase: p7, register: cc_composition, key: evaluate_inactivity}
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: evaluate_inactivity
    direction: OUTPUT
    field: is_inactive
    bound_to: capability_result.is_inactive
    source_finding: {phase: p7, register: cc_composition, key: evaluate_inactivity}
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: evaluate_inactivity
    direction: OUTPUT
    field: days_inactive
    bound_to: capability_result.days_inactive
    source_finding: {phase: p7, register: cc_composition, key: evaluate_inactivity}
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: deregister_license
    direction: INPUT
    field: key_or_address
    bound_to: inputs.employee_id
    source_finding: {phase: p7, register: cc_composition, key: deregister_license}
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    step: deregister_license
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: deregister_license}
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    step: lookup_parameter_rules
    direction: INPUT
    field: key
    bound_to: inputs.tool_name
    source_finding: {phase: p7, register: cc_composition, key: lookup_parameter_rules}
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    step: lookup_parameter_rules
    direction: INPUT
    field: map
    bound_to:
      literal:
        READ_RECORD:
        - field: record_type
          op: in
          allowed:
          - license_pool
          - user_profile
        - field: id
          op: not_null
        PROVISION_STANDARD_LICENSE:
        - field: tier
          op: eq
          value: standard
        - field: quantity
          op: lte
          value: 100
        PROVISION_PREMIUM_LICENSE:
        - field: tier
          op: eq
          value: premium
        - field: quantity
          op: lte
          value: 50
    source_finding: {phase: p7, register: cc_composition, key: lookup_parameter_rules}
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    step: lookup_parameter_rules
    direction: OUTPUT
    field: rules
    bound_to: capability_result.result
    source_finding: {phase: p7, register: cc_composition, key: lookup_parameter_rules}
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    step: validate_parameters
    direction: INPUT
    field: parameters
    bound_to: inputs.parameters
    source_finding: {phase: p7, register: cc_composition, key: validate_parameters}
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    step: validate_parameters
    direction: INPUT
    field: rules
    bound_to: results.lookup_parameter_rules.rules
    source_finding: {phase: p7, register: cc_composition, key: validate_parameters}
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    step: validate_parameters
    direction: OUTPUT
    field: validation_result
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: validate_parameters}
  interface_fields:
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    direction: INPUT
    field: license_id
    type: string
    required: 'YES'
    default: ''
    meaning: License to evaluate
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: ''
    meaning: Employee holding the license
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    direction: INPUT
    field: last_active_date
    type: string
    format: date-time
    required: 'YES'
    default: ''
    meaning: Last usage date
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    direction: INPUT
    field: evaluation_date
    type: string
    format: date-time
    required: 'YES'
    default: ''
    meaning: The date the reclaim is evaluated as of
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    direction: INPUT
    field: threshold_days
    type: integer
    required: 'YES'
    default: 30
    meaning: Inactivity threshold in days
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    direction: OUTPUT
    field: result_status
    type: string
    required: 'NO'
    default: ''
    meaning: Operation result
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    direction: OUTPUT
    field: is_inactive
    type: boolean
    required: 'NO'
    default: ''
    meaning: Whether the user is inactive
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    direction: OUTPUT
    field: days_inactive
    type: integer
    required: 'NO'
    default: ''
    meaning: Number of days inactive
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: ''
    meaning: Tool the agent proposes to use
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    direction: INPUT
    field: parameters
    type: object
    required: 'YES'
    default: ''
    meaning: Parameters of the proposed action
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    direction: OUTPUT
    field: rules
    type: array
    required: 'NO'
    default: ''
    meaning: The rules declared for the tool
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    direction: OUTPUT
    field: validation_result
    type: boolean
    required: 'NO'
    default: ''
    meaning: Whether every declared rule passed
  artifact_properties:
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    property: description
    value: Evaluates inactivity and reclaims license if threshold exceeded
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    property: supersedes
    value:
    - ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    property: supersedes
    value:
    - ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    property: description
    value: Evaluates declarative parameter constraints — policy in governance, evaluation in generic CT
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  structure_stores: null
  artifact_summary:
  - action: NEW
    subdomain: ai_licensing
    count: '1'
    artifacts: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
  - action: NEW
    subdomain: agent_governance
    count: '1'
    artifacts: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
  - action: REPLACE
    subdomain: ai_licensing
    count: '1'
    artifacts: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
  - action: REPLACE
    subdomain: agent_governance
    count: '1'
    artifacts: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
  declared_reach: null
  implementation_bindings: null
  vocabulary_extensions: null
  runtime_policies: null
  transport_bindings: null
  generation_provenance: null
  refusal_discharge: null
  refusal_deferrals:
  - operation: Reclaiming a license
    refused_when: The registry refuses to remove the assignment
    deferred_to: 'ai_governance::WF_AUTO_RECLAIM_V0, re-pointed and not restated: its place ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0, which runs the next version, routes VIOLATION to EXIT_ACTIVE'
    until: The act is next restated
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  refusal_governance_discharge: null
  molecule_steps: null
  molecule_step_bindings: null
  test_cases: null
  test_case_values: null
  withdrawn_facts: null
```

Read against the pinned baseline
`6f931dffd412e3c91cdee4a8c65ba55f269507541436a25faa24a09e716553b9`.

Two contracts v5 published are replaced by their next versions, and the published versions are stood
down unchanged. The reclaim's next version answers a refused removal at its removal step and ends the
contract with it; every other step, binding and field is restated as it stands. The parameter check's
next version reports what it receives: whether every declared rule passed. The reclaim act and the
governed action are re-pointed to run the next versions, and nothing else about either changes.

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

No transform, vocabulary, policy, entrance or generator is touched. The reclaim act and the governed action are re-pointed, not restated.

---

## 14. Refusal Discharge

The refusal the business named is carried by the reclaim act, which this change re-points and does not
restate: it already routes the contract's VIOLATION to EXIT_ACTIVE. The act states admission rules and
a renamed node that no register carries, so it cannot be restated here, and the deferral names it.

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn: each next version keeps every fact its published version has, and gains one answer or reports what it receives.
