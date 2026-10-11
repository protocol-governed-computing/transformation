# Stage 8 — Authoring Mandate: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p8
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: blockchain::CC_RESOLVE_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '2'
    code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '3'
    code: blockchain::CC_CREATE_WALLET_RECORD_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '4'
    code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '5'
    code: blockchain::WF_REGISTER_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '2'
    step: '6'
    code: blockchain::WF_ACCEPT_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::CC_RESOLVE_ACTOR_V1
  - wave: '2'
    step: '7'
    code: blockchain::WF_REJECT_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::CC_RESOLVE_ACTOR_V1
  - wave: '2'
    step: '8'
    code: blockchain::WF_CREATE_WALLET_V1
    action: NEW
    subdomain: wallet
    depends_on:
    - blockchain::CC_RESOLVE_ACTOR_V1
    - blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    - blockchain::CC_CREATE_WALLET_RECORD_V1
    - blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
  critical_path:
  - position: '1'
    code: blockchain::CC_RESOLVE_ACTOR_V1
  - position: '2'
    code: blockchain::WF_CREATE_WALLET_V1
  mandate_artifact_summary:
  - action: NEW
    count: '8'
    description: The next versions of four contracts that end on a failed record, and of four acts that route a failed record to their rejected ending.
  - action: REPLACE
    count: '8'
    description: The published versions they stand in for, stood down unchanged.
  field_declarations:
  - code: blockchain::CC_RESOLVE_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::WF_REGISTER_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::WF_ACCEPT_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::WF_REJECT_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    subdomain_field: wallet
  - code: blockchain::CC_CREATE_WALLET_RECORD_V1
    subdomain_field: wallet
  - code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    subdomain_field: wallet
  - code: blockchain::WF_CREATE_WALLET_V1
    subdomain_field: wallet
  new_capabilities:
  - code: blockchain::CC_RESOLVE_ACTOR_V1
    purpose: Answers which actor a contact address denotes, and reports when none does
    inputs: contact_address
    outputs: value
  - code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    purpose: Claims the identity, and refuses when the person already holds a wallet
    inputs: wallet_id
    outputs: result_status
  - code: blockchain::CC_CREATE_WALLET_RECORD_V1
    purpose: Records the wallet with a balance of zero, its denomination and its classification
    inputs: wallet_id, wallet_fields
    outputs: result_status
  - code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    purpose: Records the moment on the wallet's trail
    inputs: stream_id, occurrence_fields
    outputs: result_status
  new_intents: null
  cross_subdomain_notes:
  - code: blockchain::CC_RESOLVE_ACTOR_V1
    note: Identity's lookup, whose next version wallet runs too; both acts gain the same answer for a failed record.
```

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. The four contracts come first; three acts run the next version of a replaced contract and
wait for it. The published versions are stood down as their next versions are built, and the
entrances and intents are re-pointed with them.

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
