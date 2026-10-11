# Stage 8 — Authoring Mandate: blockchain / wallet

## Machine

```yaml
document:
  phase: p8
  domain: blockchain
  subdomain: wallet
  cr: cr_04_wallet
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  critical_path:
  - position: '1'
    code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
  mandate_artifact_summary:
  - action: NEW
    count: '1'
    description: The step that refuses a wallet to a person the business has not accepted.
  - action: EXTEND
    count: '22'
    description: The wallet function and the identity acts it depends on, redeclared whole so that the design and the artifacts agree — carrying the reach the act declares and the refusal it was always meant to make.
  field_declarations:
  - code: blockchain::IN_WALLET_CREATION_V0
    subdomain_field: wallet
  - code: blockchain::WF_CREATE_WALLET_V0
    subdomain_field: wallet
  - code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    subdomain_field: wallet
  - code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    subdomain_field: wallet
  - code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::CC_CREATE_WALLET_RECORD_V0
    subdomain_field: wallet
  - code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    subdomain_field: wallet
  - code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::EV_WALLET_CREATED_V0
    subdomain_field: wallet
  - code: blockchain::RB_WALLET_BINDINGS_V0
    subdomain_field: wallet
  - code: blockchain::STRUCTURE_WALLET_STORAGE_V0
    subdomain_field: wallet
  - code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    subdomain_field: wallet
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REJECTION_V0
    subdomain_field: identity
  - code: blockchain::WF_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::WF_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    subdomain_field: identity
  - code: blockchain::WF_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    subdomain_field: identity
  - code: blockchain::RB_IDENTITY_BINDINGS_V0
    subdomain_field: identity
  - code: blockchain::TI_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    subdomain_field: identity
  - code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    subdomain_field: wallet
  new_capabilities:
  - code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    purpose: Derives the wallet's identity from the person who holds it
    inputs: holder, wallet_id_prefix
    outputs: wallet_id
  - code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    purpose: Claims the identity, refusing when the person already holds a wallet
    inputs: wallet_id
    outputs: result_status
  - code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    purpose: Establishes the address others may pay to, from supplied key material
    inputs: key_material
    outputs: address
  - code: blockchain::CC_CREATE_WALLET_RECORD_V0
    purpose: Records the wallet with a balance of zero, its denomination and its classification
    inputs: wallet_id, wallet_fields
    outputs: result_status
  - code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    purpose: Records that the wallet was created, for whom, and when
    inputs: stream_id, occurrence_fields
    outputs: result_status
  - code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    purpose: Refuses a rejection that states no grounds, before anything is recorded
    inputs: grounds, grounds_rules
    outputs: valid
  - code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    purpose: Works out an address from supplied key material; the same material always yields the same address
    inputs: key_material
    outputs: address
  - code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    purpose: Refuses a wallet for a person the business has not accepted, before anything is claimed or recorded.
    inputs: holder_state:string, states_admitting_a_wallet:array
    outputs: is_accepted:boolean
  new_intents:
  - code: blockchain::IN_WALLET_CREATION_V0
    purpose: Admits a request to give an accepted person a wallet
    workflow: blockchain::WF_CREATE_WALLET_V0
    inputs: contact_address, key_material, wallet_id_prefix
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    purpose: Admits a request to accept a person
    workflow: blockchain::WF_ACCEPT_ACTOR_V0
    inputs: contact_address, verifying_authority
  - code: blockchain::IN_ACTOR_REJECTION_V0
    purpose: Admits a request to reject a person, refusing one that states no grounds
    workflow: blockchain::WF_REJECT_ACTOR_V0
    inputs: contact_address, verifying_authority, grounds
  cross_subdomain_notes:
  - code: blockchain::CC_RESOLVE_ACTOR_V0
    note: Owned by identity, read by wallet's workflow. Wallet reads a person and never writes one.
  - code: blockchain::EV_ACTOR_ACCEPTED_V0
    note: Declared and announced by identity. Wallet consumes the moment and declares none of the three.
  - code: blockchain::WF_REGISTER_ACTOR_V0
    note: Extended by this change although wallet does not use it, because the three declared moments are announced together or the gap simply moves.
  - code: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
    note: 'Built last: it declares the second subdomain, and declaring a subdomain whose artifacts do not yet exist would compile to nothing.'
```

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing.

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
