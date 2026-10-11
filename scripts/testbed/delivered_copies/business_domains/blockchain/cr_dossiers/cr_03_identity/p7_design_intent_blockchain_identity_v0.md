# Stage 7 — Design Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p7
  domain: blockchain
  subdomain: identity
  cr: cr_03_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: The writing step calls a keyed update rather than a keyed write.
    business_fact: A decision may change only the person's state, the authority who decided and the grounds stated, and must leave everything else the business holds about them as it was.
    resolution: A whole-value write sets what is held at a key, so every field the caller did not supply ceases to be held. A keyed update sets the fields it is given and leaves the rest of the record alone. The step changes operation and nothing else about the contract changes.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - decision: What the update sets is the record the fourth step assembles.
    business_fact: The three things a decision is entitled to change, and the address that identifies whose record it is.
    resolution: 'The assembling step already produces exactly those fields and no others, so it becomes the update''s argument rather than a whole value to overwrite with. The set of fields it carries is where the business rule now lives: what is absent from it is what a decision cannot touch.'
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - decision: The assembling step keeps its consumer, and the gap that recorded its loss is closed.
    business_fact: Nothing in the business asked for a step whose output nothing reads.
    resolution: An earlier reading of this correction passed the decided fields straight to the update, which would have left the fourth step producing a record no step consumed. Taking the update's argument from that step instead keeps it in the pipeline, doing what it always did. The deferral recorded for it is withdrawn rather than carried.
    source_finding: {phase: p4, register: gap_register, key: GAP-03}
  - decision: A decision that names a person the store does not hold is refused rather than creating one.
    business_fact: A decision records a decision; it does not admit anyone.
    resolution: The keyed write would set a value at a key nothing held, inventing a person nobody registered. The keyed update reports a violation and changes nothing. The refusal is a property of the operation, and the contract already admits that status.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
  - decision: The step keeps the name it has.
    business_fact: Nothing in the business names a step.
    resolution: 'Renaming it would report thirteen facts lost where one changed: the completeness check compares a render against what is held and cannot tell a renamed step from a deleted one. Keeping the name leaves exactly one narrowing — the whole-value input replaced by the fields to set — which is the change itself and should be the only thing a reviewer sees.'
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - decision: The contract's inputs, refusals and result statuses are reproduced unchanged.
    business_fact: A caller sends what they send now and is told what they are told now.
    resolution: Its three validations, its assembling step, its declared inputs and its admitted result statuses are stated here exactly as the composition holds them. A correction that altered any of them would be observable above the contract, which the business asked it not to be.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  existing_inventory:
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    action: EXTEND
    summary: Refuses every declared refusal and moves the actor to its decided state
    reason: The one artifact this change touches. Its fifth step writes a whole record where it must change part of one.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REUSE
    summary: The keyed store, publishing a keyed write, a keyed update and a filtered update.
    reason: Reused unchanged. A different operation of the same capability is called, which is a choice the contract makes and not a change to the capability.
    source_finding: {phase: p6, register: cross_subdomain_deps, key: Changing part of a held record without replacing it}
  - fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
    action: REUSE
    summary: Binds identity's workflows to the side effects and storage they use.
    reason: Reused unchanged; it binds the capability, not the operation.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::RB_IDENTITY_BINDINGS_V0'}
  - fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    action: REUSE
    summary: Declares the stores identity owns, including the actor store.
    reason: Reused unchanged; the store, its path and its declaration are untouched.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::STRUCTURE_IDENTITY_STORAGE_V0'}
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    action: REVIEW
    summary: Resolves a contact address to an actor and reads the record whole.
    reason: Untouched, and the only reader of the store. What it reads will start carrying fields a decision had been stripping; it asserts nothing about the record's shape, so it is safe and still wants a look.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    action: REUSE
    summary: The governed sequence that records an authority's decision.
    reason: Composes the amended contract and routes on a result status this change preserves. Not itself amended.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::WF_RECORD_VERIFICATION_DECISION_V0'}
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    action: REUSE
    summary: Admits a request to accept a registered actor.
    reason: Names the workflow, not the contract. Unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::TI_ACCEPT_ACTOR_V0'}
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    action: REUSE
    summary: Admits a request to reject a registered actor.
    reason: The same.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::TI_REJECT_ACTOR_V0'}
  - fqdn: blockchain::IN_ACTOR_VERIFIED_V0
    action: REUSE
    summary: The request that starts the act of recording a decision.
    reason: Reached unchanged; named so the topology this change restates is complete rather than partial.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    action: REUSE
    summary: Appends one occurrence to the trail.
    reason: Reached unchanged; the trail is unchanged by constraint.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    action: REUSE
    summary: Reads a supplied value against a declared admitted set.
    reason: Reached unchanged by two of the contract's steps.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    action: REUSE
    summary: Compares two supplied values.
    reason: Reached unchanged by the contract's third step.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: Assembles a record from supplied fields.
    reason: Reached unchanged by the contract's fourth step, whose output now feeds the update.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  new_artifacts: null
  rb_declarations:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    cs_bindings:
    - Unchanged by this change; the capability the corrected step calls is already bound
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::RB_IDENTITY_BINDINGS_V0'}
  execution_topology:
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: blockchain::IN_ACTOR_VERIFIED_V0
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::WF_RECORD_VERIFICATION_DECISION_V0'}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: blockchain::CC_RESOLVE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::WF_RECORD_VERIFICATION_DECISION_V0'}
  cc_composition:
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '1'
    step_name: read_state_admits_decision
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: is_member
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '2'
    step_name: read_outcome_admitted
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: is_member
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '3'
    step_name: refuse_self_verification
    capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    kind: CT
    operation: COMPARE_EQUAL
    store: null
    consumes:
    - left
    - right
    produces:
    - is_equal
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        left: left
        right: right
      out:
        is_equal: is_equal
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '4'
    step_name: assemble_decided_actor
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - fields
    produces:
    - record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: record
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '5'
    step_name: write_decided_actor
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE
    store: ACTORS
    consumes:
    - key
    - updates
    produces:
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  step_bindings:
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: INPUT
    field: value
    bound_to: inputs.current_state
    source_finding: {phase: p7, register: cc_composition, key: read_state_admits_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: INPUT
    field: allowed_set
    bound_to: inputs.states_admitting_a_decision
    source_finding: {phase: p7, register: cc_composition, key: read_state_admits_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: read_state_admits_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: INPUT
    field: value
    bound_to: inputs.decision
    source_finding: {phase: p7, register: cc_composition, key: read_outcome_admitted}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: INPUT
    field: allowed_set
    bound_to: inputs.admitted_outcomes
    source_finding: {phase: p7, register: cc_composition, key: read_outcome_admitted}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: read_outcome_admitted}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_verification
    direction: INPUT
    field: left
    bound_to: inputs.verifying_authority
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_verification}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_verification
    direction: INPUT
    field: right
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_verification}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_verification
    direction: OUTPUT
    field: is_equal
    bound_to: capability_result.is_equal
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_verification}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: assemble_decided_actor
    direction: INPUT
    field: fields
    bound_to: inputs.decided_actor_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: assemble_decided_actor
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: write_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: INPUT
    field: updates
    bound_to: results.assemble_decided_actor.record
    source_finding: {phase: p7, register: cc_composition, key: write_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_decided_actor}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: states_admitting_a_decision
    bound_to: payload.states_admitting_a_decision
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to: payload.decision
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: admitted_outcomes
    bound_to: payload.admitted_outcomes
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decided_actor_fields
    bound_to: payload.decided_actor_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  interface_fields:
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    type: string
    required: 'YES'
    default: ''
    meaning: The state the person is in when the decision is recorded.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: states_admitting_a_decision
    type: array
    required: 'YES'
    default: ''
    meaning: The states from which a decision may be recorded.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    type: string
    required: 'YES'
    default: ''
    meaning: The outcome the authority states.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: admitted_outcomes
    type: array
    required: 'YES'
    default: ''
    meaning: The outcomes a decision may carry.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority recording the decision.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: Whose record the decision is recorded against, and the key that identifies it.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decided_actor_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The fields a decision sets. What is absent from it is what a decision may not change.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the decision was recorded, refused, or failed in the store.
  implementation_bindings: null
  vocabulary_extensions: null
  runtime_policies: null
  artifact_properties:
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    property: summary
    value: Refuses every declared refusal and moves the actor to its decided state — carried unchanged, because an amendment states what the artifact is and not what the change did to it
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    property: result_status_contract.allowed
    value: VIOLATION, SUCCESS, BACKEND_ERROR
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    property: result_status_contract.on_input_failure
    value: VIOLATION
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  structure_stores: null
  transport_bindings: null
  artifact_summary:
  - action: EXTEND
    subdomain: identity
    count: '1'
    artifacts: 1 CC
```

One artifact, amended. No artifact is authored: this change corrects a step of a contract the
composition already holds, and the contract is rendered whole under its own code. Four of its five
steps are reproduced exactly as they are; the fifth changes the operation it calls and where its
value comes from.

---

## 1. Design Resolution

---

## 2. Existing Inventory

---

## 3. New Artifacts

---

## 4. Runtime Binding Declarations

---

## 5. Execution Topology

---

## 6. Capability Contract Composition

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

## 13. Structure Stores

---

## 14. Transport Bindings

---

## 15. Artifact Summary

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | Ownership, dependencies, boundary rules | COMPLETE |
| Stage 7 — Design Intent | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · cc_composition · step_bindings · interface_fields · artifact_properties · artifact_summary |
