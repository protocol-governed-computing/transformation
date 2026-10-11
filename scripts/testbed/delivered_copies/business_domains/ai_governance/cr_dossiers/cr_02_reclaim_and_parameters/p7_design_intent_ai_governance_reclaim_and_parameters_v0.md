# Stage 7 — Design Intent: ai_governance / reclaim and parameter result

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_02_reclaim_and_parameters
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
    - Decision: The removal step ends the contract on a refused removal
      Business Fact: No reclaim carries on past a removal the registry refused
      Resolution: The deregister_license step of ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1 routes VIOLATION to exit
      Source Finding: 'S4 design_decisions #1'
    - Decision: A refused removal ends as still active
      Business Fact: A license the registry did not release stays with the employee
      Resolution: ai_governance::WF_AUTO_RECLAIM_V0 already routes the contract's VIOLATION to EXIT_ACTIVE; it is re-pointed and not restated
      Source Finding: 'S4 design_decisions #2'
    - Decision: The check reports what it receives
      Business Fact: A check reports only what it receives
      Resolution: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 maps `validation_result` from the check's `valid`, a boolean
      Source Finding: 'S4 design_decisions #3'
    - Decision: Next versions
      Business Fact: A change of meaning is a new identity, and identity is fixed at publication
      Resolution: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1 supersedes ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0, and ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 supersedes ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
      Source Finding: 'S4 design_decisions #4'
    - Decision: The acts run the next versions
      Business Fact: Each decides exactly as today
      Resolution: 'ai_governance::WF_AUTO_RECLAIM_V0 and ai_governance::WF_GOVERN_AGENT_ACTION_V0 are re-pointed: the place that runs each contract runs its next version; its label and routes are unchanged'
      Source Finding: 'S4 design_decisions #5'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: ''
      Reason: Its removal step carries on past a refusal its registry declares. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by the reclaim's next version, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: ai_governance::WF_AUTO_RECLAIM_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Runs the reclaim being replaced; re-pointed to its next version. It already routes the refusal to still active.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: ''
      Reason: Reports a result it never receives. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: ai_governance::WF_GOVERN_AGENT_ACTION_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Runs the parameter check being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Checks the parameters against the rules, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: capability_transforms::CT_PURE_LOOKUP_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Looks up the tool's rules, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by the reclaim's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: ai_governance::RB_LICENSE_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Binds the license registry, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Places the license registry, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
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
    - Capability: End a reclaim the registry refuses
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Summary: Reclaim license from inactive user
      Owner Subdomain: ai_licensing
      Status: NEW
      Source Finding: 'S6 governance_outcome #1'
    - Capability: Check an action's parameters
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Summary: Enforce declared parameter constraints for an authorized tool
      Owner Subdomain: agent_governance
      Status: NEW
      Source Finding: 'S6 governance_outcome #2'
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
    - CC Code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: '1'
      Step Name: evaluate_inactivity
      Capability: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Kind (CT, CS): CT
      Operation: EVALUATE_INACTIVITY
      Store: —
      Consumes: last_active_date, evaluation_date, threshold_days
      Produces: is_inactive, days_inactive
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: last_active_date=last_active_date, evaluation_date=evaluation_date, threshold_days=threshold_days; out: is_inactive=is_inactive, days_inactive=days_inactive'
    - CC Code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: '2'
      Step Name: deregister_license
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: DEREGISTER
      Store: LICENSE_REGISTRY
      Consumes: key_or_address
      Produces: result_status
      Routing: SUCCESS -> exit; NOT_FOUND -> exit; BACKEND_ERROR -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key_or_address=employee_id; out: result_status=result_status'
    - CC Code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Step: '1'
      Step Name: lookup_parameter_rules
      Capability: capability_transforms::CT_PURE_LOOKUP_V0
      Kind (CT, CS): CT
      Operation: LOOKUP
      Store: —
      Consumes: key, map
      Produces: result
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=tool_name, map=rules declared per tool; out: result=rules'
    - CC Code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Step: '2'
      Step Name: validate_parameters
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=validation_result'
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: evaluate_inactivity
      Direction (INPUT, OUTPUT): INPUT
      Field: last_active_date
      Bound To: inputs.last_active_date
      Source Finding: S7 cc_composition evaluate_inactivity
    - Owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: evaluate_inactivity
      Direction (INPUT, OUTPUT): INPUT
      Field: evaluation_date
      Bound To: inputs.evaluation_date
      Source Finding: S7 cc_composition evaluate_inactivity
    - Owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: evaluate_inactivity
      Direction (INPUT, OUTPUT): INPUT
      Field: threshold_days
      Bound To: inputs.threshold_days
      Source Finding: S7 cc_composition evaluate_inactivity
    - Owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: evaluate_inactivity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_inactive
      Bound To: capability_result.is_inactive
      Source Finding: S7 cc_composition evaluate_inactivity
    - Owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: evaluate_inactivity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: days_inactive
      Bound To: capability_result.days_inactive
      Source Finding: S7 cc_composition evaluate_inactivity
    - Owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: deregister_license
      Direction (INPUT, OUTPUT): INPUT
      Field: key_or_address
      Bound To: inputs.employee_id
      Source Finding: S7 cc_composition deregister_license
    - Owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Step: deregister_license
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition deregister_license
    - Owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Step: lookup_parameter_rules
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.tool_name
      Source Finding: S7 cc_composition lookup_parameter_rules
    - Owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Step: lookup_parameter_rules
      Direction (INPUT, OUTPUT): INPUT
      Field: map
      Bound To: '{"READ_RECORD": [{"field": "record_type", "op": "in", "allowed": ["license_pool", "user_profile"]}, {"field": "id", "op": "not_null"}], "PROVISION_STANDARD_LICENSE": [{"field": "tier", "op": "eq", "value": "standard"}, {"field": "quantity", "op": "lte", "value": 100}], "PROVISION_PREMIUM_LICENSE": [{"field": "tier", "op": "eq", "value": "premium"}, {"field": "quantity", "op": "lte", "value": 50}]}'
      Source Finding: S7 cc_composition lookup_parameter_rules
    - Owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Step: lookup_parameter_rules
      Direction (INPUT, OUTPUT): OUTPUT
      Field: rules
      Bound To: capability_result.result
      Source Finding: S7 cc_composition lookup_parameter_rules
    - Owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Step: validate_parameters
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: inputs.parameters
      Source Finding: S7 cc_composition validate_parameters
    - Owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Step: validate_parameters
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: results.lookup_parameter_rules.rules
      Source Finding: S7 cc_composition validate_parameters
    - Owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Step: validate_parameters
      Direction (INPUT, OUTPUT): OUTPUT
      Field: validation_result
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition validate_parameters
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
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: license_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: License to evaluate
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: employee_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Employee holding the license
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: last_active_date
      Type: string (date-time)
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Last usage date
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: evaluation_date
      Type: string (date-time)
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The date the reclaim is evaluated as of
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: threshold_days
      Type: integer
      Required (YES, NO): 'YES'
      Default: '30'
      Meaning: Inactivity threshold in days
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Operation result
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: is_inactive
      Type: boolean
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Whether the user is inactive
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: days_inactive
      Type: integer
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Number of days inactive
    - Artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: tool_name
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Tool the agent proposes to use
    - Artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: parameters
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Parameters of the proposed action
    - Artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: rules
      Type: array
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The rules declared for the tool
    - Artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: validation_result
      Type: boolean
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Whether every declared rule passed
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Property: description
      Value: Evaluates inactivity and reclaims license if threshold exceeded
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Property: supersedes
      Value: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
      Source Finding: 'S4 design_decisions #4'
    - Artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Property: supersedes
      Value: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
      Source Finding: 'S4 design_decisions #4'
    - Artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Property: description
      Value: Evaluates declarative parameter constraints — policy in governance, evaluation in generic CT
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
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
      Subdomain: ai_licensing
      Count: '1'
      Artifacts: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: agent_governance
      Count: '1'
      Artifacts: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Subdomain: ai_licensing
      Count: '1'
      Artifacts: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Subdomain: agent_governance
      Count: '1'
      Artifacts: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
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
    - Operation: Reclaiming a license
      Refused When: The registry refuses to remove the assignment
      Deferred To: 'ai_governance::WF_AUTO_RECLAIM_V0, re-pointed and not restated: its place ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0, which runs the next version, routes VIOLATION to EXIT_ACTIVE'
      Until: The act is next restated
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
