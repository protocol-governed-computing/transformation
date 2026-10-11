# Stage 8 — Authoring Mandate: blockchain / identity

## Machine

```yaml
document:
  phase: p8
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order: null
  critical_path: null
  mandate_artifact_summary:
  - action: EXTEND
    count: '11'
    description: Identity's three contracts, three acts, three entrances and two admission gates, redeclared whole so that identity holds every rule it applies and no request supplies one.
  field_declarations:
  - code: blockchain::CC_VALIDATE_REGISTRATION_V0
    subdomain_field: identity
  - code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    subdomain_field: identity
  - code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    subdomain_field: identity
  - code: blockchain::WF_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::WF_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::WF_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    subdomain_field: identity
  new_capabilities:
  - code: blockchain::CC_VALIDATE_REGISTRATION_V0
    purpose: Refuses a registration lacking the person's name or their address
    inputs: actor_record
    outputs: violations
  - code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    purpose: Refuses a decision about a person not unverified, a decision other than an acceptance or a rejection, or an authority deciding about themselves, and records the decision it checked
    inputs: current_state, decision, verifying_authority, contact_address, grounds
    outputs: result_status
  - code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    purpose: Refuses a rejection stating no grounds, before anything is recorded
    inputs: grounds
    outputs: valid
  new_intents:
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    purpose: Admits a request to accept a person, with the grounds the authority chooses to state
    workflow: blockchain::WF_ACCEPT_ACTOR_V0
    inputs: contact_address, verifying_authority, grounds
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    purpose: A request to admit a person as an actor
    workflow: blockchain::WF_REGISTER_ACTOR_V0
    inputs: actor_record
  cross_subdomain_notes:
  - code: blockchain::CC_RESOLVE_ACTOR_V0
    note: Reused unchanged; wallet reads the same resolution, and nothing it reads changes.
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
