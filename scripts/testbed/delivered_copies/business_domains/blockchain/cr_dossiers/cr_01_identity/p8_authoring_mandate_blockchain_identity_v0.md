# Stage 8 — Authoring Mandate: blockchain / identity

## Machine

```yaml
document:
  phase: p8
  domain: blockchain
  subdomain: identity
  cr: cr_01_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: blockchain::AC_PARTICIPANT_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '2'
    code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '3'
    code: blockchain::EV_ACTOR_ACCEPTED_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '4'
    code: blockchain::EV_ACTOR_REJECTED_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '2'
    step: '5'
    code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '3'
    step: '6'
    code: blockchain::CC_VALIDATE_REGISTRATION_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '3'
    step: '7'
    code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - wave: '3'
    step: '8'
    code: blockchain::CC_REGISTER_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - wave: '3'
    step: '9'
    code: blockchain::CC_RESOLVE_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - wave: '3'
    step: '10'
    code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - wave: '3'
    step: '11'
    code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - wave: '4'
    step: '12'
    code: blockchain::IN_ACTOR_REGISTERED_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::CC_VALIDATE_REGISTRATION_V0
  - wave: '4'
    step: '13'
    code: blockchain::IN_ACTOR_VERIFIED_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::CC_RESOLVE_ACTOR_V0
  - wave: '5'
    step: '14'
    code: blockchain::WF_REGISTER_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::IN_ACTOR_REGISTERED_V0
  - wave: '5'
    step: '15'
    code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::IN_ACTOR_VERIFIED_V0
  - wave: '6'
    step: '16'
    code: blockchain::RB_IDENTITY_BINDINGS_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::WF_REGISTER_ACTOR_V0
  critical_path:
  - position: '1'
    code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - position: '2'
    code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
  - position: '3'
    code: blockchain::CC_REGISTER_ACTOR_V0
  - position: '4'
    code: blockchain::IN_ACTOR_REGISTERED_V0
  - position: '5'
    code: blockchain::WF_REGISTER_ACTOR_V0
  - position: '6'
    code: blockchain::RB_IDENTITY_BINDINGS_V0
  mandate_artifact_summary:
  - action: NEW
    count: '16'
    description: 1 AC, 3 EV, 1 STRUCTURE, 6 CC, 2 IN, 2 WF, 1 RB — the whole of the identity subdomain, nothing extended because nothing of this domain exists
  field_declarations:
  - code: blockchain::AC_PARTICIPANT_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_ACCEPTED_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_REJECTED_V0
    subdomain_field: identity
  - code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    subdomain_field: identity
  - code: blockchain::CC_VALIDATE_REGISTRATION_V0
    subdomain_field: identity
  - code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    subdomain_field: identity
  - code: blockchain::CC_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_RESOLVE_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    subdomain_field: identity
  - code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_VERIFIED_V0
    subdomain_field: identity
  - code: blockchain::WF_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    subdomain_field: identity
  - code: blockchain::RB_IDENTITY_BINDINGS_V0
    subdomain_field: identity
  new_capabilities:
  - code: blockchain::CC_VALIDATE_REGISTRATION_V0
    purpose: Confirm a registration carries a name and a contact address of the form asked for, so that only details the business cannot read are refused and judgement is left to the decision
    inputs: actor_record:object, registration_schema:object
    outputs: violations:array
  - code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    purpose: Claim the contact address atomically so that two registrations of one person resolve to one actor rather than producing two
    inputs: actor_record:object, address_path:string, address_type:string
    outputs: result:string, address:string
  - code: blockchain::CC_REGISTER_ACTOR_V0
    purpose: Write the actor unverified once its address is claimed, so that a refused registration leaves nothing behind
    inputs: actor_fields:object, contact_address:string
    outputs: result_status:string
  - code: blockchain::CC_RESOLVE_ACTOR_V0
    purpose: Answer which actor a contact address denotes and report when none does, so a decision against an unregistered person is refused
    inputs: contact_address:string
    outputs: actor_record:object
  - code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    purpose: Refuse every declared refusal and move the actor to its decided state, so an actor is decided about once and never by itself
    inputs: current_state:string, states_admitting_a_decision:array, decision:string, admitted_outcomes:array, verifying_authority:string, contact_address:string, decided_actor_fields:object
    outputs: result_status:string
  - code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    purpose: Read the time now and append one occurrence carrying it, so the business can afterwards show who registered, who decided, what was decided and when it happened
    inputs: occurrence_fields:object, stream_id:string, contact_address:string
    outputs: timestamp:string, sequence_number:integer
  new_intents:
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    purpose: Admit a request from a person to be recorded as an actor of the system
    workflow: blockchain::WF_REGISTER_ACTOR_V0
    inputs: actor_record:object, registration_schema:object
  - code: blockchain::IN_ACTOR_VERIFIED_V0
    purpose: Admit a request from an authority to record a decision against a registered actor
    workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    inputs: contact_address:string, verifying_authority:string, decision:string, grounds:string
  cross_subdomain_notes:
  - code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    note: The occurrence carries occurred_at, read from capability_side_effects::CS_CLOCK_V0 at the moment the occurrence is recorded. No caller supplies it.
  - code: blockchain::WF_REGISTER_ACTOR_V0
    note: Reached in process. No transport ingress is scheduled, so the operation is not reachable over HTTP; a follow-on change request adds the boundary without altering this workflow.
  - code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    note: Reached in process, on the same terms.
```

Mechanically derived from the design. Every artifact the design declares appears here exactly once,
scheduled after everything it depends on. Nothing is decided at this stage; the order is read off
the design's own dependencies.

---

## 1. Build Dependency Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Subdomain Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 6 — Governance Intent | p6_governance_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 7 — Design Intent | p7_design_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 8 — Authoring Mandate | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Artifact Authoring

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 7 | new_artifacts · existing_inventory · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · structure_stores · artifact_summary |
| **Emits** → Artifact Authoring | build_order · critical_path · mandate_artifact_summary · field_declarations · new_capabilities · new_intents · cross_subdomain_notes |
