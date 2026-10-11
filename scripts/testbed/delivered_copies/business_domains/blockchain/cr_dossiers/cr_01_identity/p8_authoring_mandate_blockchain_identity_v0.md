# Stage 8 — Authoring Mandate: blockchain / identity

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_01_identity
  Status: DRAFT
  Feeds: Artifact Authoring
registers:
  build_order:
    columns:
    - Wave
    - Step
    - Code
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Depends On
    rows:
    - Wave: '1'
      Step: '1'
      Code: blockchain::AC_PARTICIPANT_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '1'
      Step: '2'
      Code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '1'
      Step: '3'
      Code: blockchain::EV_ACTOR_ACCEPTED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '1'
      Step: '4'
      Code: blockchain::EV_ACTOR_REJECTED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '2'
      Step: '5'
      Code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '3'
      Step: '6'
      Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '3'
      Step: '7'
      Code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    - Wave: '3'
      Step: '8'
      Code: blockchain::CC_REGISTER_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    - Wave: '3'
      Step: '9'
      Code: blockchain::CC_RESOLVE_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    - Wave: '3'
      Step: '10'
      Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    - Wave: '3'
      Step: '11'
      Code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    - Wave: '4'
      Step: '12'
      Code: blockchain::IN_ACTOR_REGISTERED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::CC_VALIDATE_REGISTRATION_V0
    - Wave: '4'
      Step: '13'
      Code: blockchain::IN_ACTOR_VERIFIED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::CC_RESOLVE_ACTOR_V0
    - Wave: '5'
      Step: '14'
      Code: blockchain::WF_REGISTER_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::IN_ACTOR_REGISTERED_V0
    - Wave: '5'
      Step: '15'
      Code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::IN_ACTOR_VERIFIED_V0
    - Wave: '6'
      Step: '16'
      Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::WF_REGISTER_ACTOR_V0
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    - Position: '2'
      Code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    - Position: '3'
      Code: blockchain::CC_REGISTER_ACTOR_V0
    - Position: '4'
      Code: blockchain::IN_ACTOR_REGISTERED_V0
    - Position: '5'
      Code: blockchain::WF_REGISTER_ACTOR_V0
    - Position: '6'
      Code: blockchain::RB_IDENTITY_BINDINGS_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '16'
      Description: 1 AC, 3 EV, 1 STRUCTURE, 6 CC, 2 IN, 2 WF, 1 RB — the whole of the identity subdomain, nothing extended because nothing of this domain exists
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: blockchain::AC_PARTICIPANT_V0
      Subdomain Field: identity
    - Code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Subdomain Field: identity
    - Code: blockchain::EV_ACTOR_ACCEPTED_V0
      Subdomain Field: identity
    - Code: blockchain::EV_ACTOR_REJECTED_V0
      Subdomain Field: identity
    - Code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Subdomain Field: identity
    - Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Subdomain Field: identity
    - Code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Subdomain Field: identity
    - Code: blockchain::CC_REGISTER_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::CC_RESOLVE_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Subdomain Field: identity
    - Code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Subdomain Field: identity
    - Code: blockchain::IN_ACTOR_REGISTERED_V0
      Subdomain Field: identity
    - Code: blockchain::IN_ACTOR_VERIFIED_V0
      Subdomain Field: identity
    - Code: blockchain::WF_REGISTER_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Subdomain Field: identity
    - Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Subdomain Field: identity
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Purpose: Confirm a registration carries a name and a contact address of the form asked for, so that only details the business cannot read are refused and judgement is left to the decision
      Inputs: actor_record:object, registration_schema:object
      Outputs: violations:array
    - Code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Purpose: Claim the contact address atomically so that two registrations of one person resolve to one actor rather than producing two
      Inputs: actor_record:object, address_path:string, address_type:string
      Outputs: result:string, address:string
    - Code: blockchain::CC_REGISTER_ACTOR_V0
      Purpose: Write the actor unverified once its address is claimed, so that a refused registration leaves nothing behind
      Inputs: actor_fields:object, contact_address:string
      Outputs: result_status:string
    - Code: blockchain::CC_RESOLVE_ACTOR_V0
      Purpose: Answer which actor a contact address denotes and report when none does, so a decision against an unregistered person is refused
      Inputs: contact_address:string
      Outputs: actor_record:object
    - Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Purpose: Refuse every declared refusal and move the actor to its decided state, so an actor is decided about once and never by itself
      Inputs: current_state:string, states_admitting_a_decision:array, decision:string, admitted_outcomes:array, verifying_authority:string, contact_address:string, decided_actor_fields:object
      Outputs: result_status:string
    - Code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Purpose: Read the time now and append one occurrence carrying it, so the business can afterwards show who registered, who decided, what was decided and when it happened
      Inputs: occurrence_fields:object, stream_id:string, contact_address:string
      Outputs: timestamp:string, sequence_number:integer
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: blockchain::IN_ACTOR_REGISTERED_V0
      Purpose: Admit a request from a person to be recorded as an actor of the system
      Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Inputs: actor_record:object, registration_schema:object
    - Code: blockchain::IN_ACTOR_VERIFIED_V0
      Purpose: Admit a request from an authority to record a decision against a registered actor
      Workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Inputs: contact_address:string, verifying_authority:string, decision:string, grounds:string
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Note: The occurrence carries occurred_at, read from capability_side_effects::CS_CLOCK_V0 at the moment the occurrence is recorded. No caller supplies it.
    - Code: blockchain::WF_REGISTER_ACTOR_V0
      Note: Reached in process. No transport ingress is scheduled, so the operation is not reachable over HTTP; a follow-on change request adds the boundary without altering this workflow.
    - Code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Note: Reached in process, on the same terms.
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
