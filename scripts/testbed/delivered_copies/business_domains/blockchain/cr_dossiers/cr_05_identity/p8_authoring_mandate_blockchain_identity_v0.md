# Stage 8 — Authoring Mandate: blockchain / identity

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_05_identity
  Status: DRAFT
  Feeds: Construction
registers:
  build_order:
    columns:
    - Wave
    - Step
    - Code
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Depends On
    rows: []
  critical_path:
    columns:
    - Position
    - Code
    rows: []
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '11'
      Description: Identity's three contracts, three acts, three entrances and two admission gates, redeclared whole so that identity holds every rule it applies and no request supplies one.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Subdomain Field: identity
    - Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Subdomain Field: identity
    - Code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Subdomain Field: identity
    - Code: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Subdomain Field: identity
    - Code: blockchain::WF_REGISTER_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::WF_ACCEPT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::WF_REJECT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TI_REGISTER_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TI_ACCEPT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TI_REJECT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::IN_ACTOR_REGISTERED_V0
      Subdomain Field: identity
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Purpose: Refuses a registration lacking the person's name or their address
      Inputs: actor_record
      Outputs: violations
    - Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Purpose: Refuses a decision about a person not unverified, a decision other than an acceptance or a rejection, or an authority deciding about themselves, and records the decision it checked
      Inputs: current_state, decision, verifying_authority, contact_address, grounds
      Outputs: result_status
    - Code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Purpose: Refuses a rejection stating no grounds, before anything is recorded
      Inputs: grounds
      Outputs: valid
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Purpose: Admits a request to accept a person, with the grounds the authority chooses to state
      Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Inputs: contact_address, verifying_authority, grounds
    - Code: blockchain::IN_ACTOR_REGISTERED_V0
      Purpose: A request to admit a person as an actor
      Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Inputs: actor_record
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: blockchain::CC_RESOLVE_ACTOR_V0
      Note: Reused unchanged; wallet reads the same resolution, and nothing it reads changes.
```

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the eleven redeclared artifacts are authored
whole in their subdomain.

---

## 1. Build Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes
