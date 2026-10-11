# Stage 8 — Authoring Mandate: blockchain / wallet

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_04_wallet
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
    rows:
    - Wave: '1'
      Step: '1'
      Code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: wallet
      Depends On: —
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '1'
      Description: The step that refuses a wallet to a person the business has not accepted.
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '22'
      Description: The wallet function and the identity acts it depends on, redeclared whole so that the design and the artifacts agree — carrying the reach the act declares and the refusal it was always meant to make.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: blockchain::IN_WALLET_CREATION_V0
      Subdomain Field: wallet
    - Code: blockchain::WF_CREATE_WALLET_V0
      Subdomain Field: wallet
    - Code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Subdomain Field: wallet
    - Code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Subdomain Field: wallet
    - Code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Subdomain Field: wallet
    - Code: blockchain::CC_CREATE_WALLET_RECORD_V0
      Subdomain Field: wallet
    - Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Subdomain Field: wallet
    - Code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
      Subdomain Field: wallet
    - Code: blockchain::EV_WALLET_CREATED_V0
      Subdomain Field: wallet
    - Code: blockchain::RB_WALLET_BINDINGS_V0
      Subdomain Field: wallet
    - Code: blockchain::STRUCTURE_WALLET_STORAGE_V0
      Subdomain Field: wallet
    - Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Subdomain Field: wallet
    - Code: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Subdomain Field: identity
    - Code: blockchain::IN_ACTOR_REJECTION_V0
      Subdomain Field: identity
    - Code: blockchain::WF_ACCEPT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::WF_REJECT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Subdomain Field: identity
    - Code: blockchain::WF_REGISTER_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Subdomain Field: identity
    - Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Subdomain Field: identity
    - Code: blockchain::TI_ACCEPT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TI_REJECT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Subdomain Field: identity
    - Code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Subdomain Field: wallet
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Purpose: Derives the wallet's identity from the person who holds it
      Inputs: holder, wallet_id_prefix
      Outputs: wallet_id
    - Code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Purpose: Claims the identity, refusing when the person already holds a wallet
      Inputs: wallet_id
      Outputs: result_status
    - Code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Purpose: Establishes the address others may pay to, from supplied key material
      Inputs: key_material
      Outputs: address
    - Code: blockchain::CC_CREATE_WALLET_RECORD_V0
      Purpose: Records the wallet with a balance of zero, its denomination and its classification
      Inputs: wallet_id, wallet_fields
      Outputs: result_status
    - Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Purpose: Records that the wallet was created, for whom, and when
      Inputs: stream_id, occurrence_fields
      Outputs: result_status
    - Code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Purpose: Refuses a rejection that states no grounds, before anything is recorded
      Inputs: grounds, grounds_rules
      Outputs: valid
    - Code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
      Purpose: Works out an address from supplied key material; the same material always yields the same address
      Inputs: key_material
      Outputs: address
    - Code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Purpose: Refuses a wallet for a person the business has not accepted, before anything is claimed or recorded.
      Inputs: holder_state:string, states_admitting_a_wallet:array
      Outputs: is_accepted:boolean
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: blockchain::IN_WALLET_CREATION_V0
      Purpose: Admits a request to give an accepted person a wallet
      Workflow: blockchain::WF_CREATE_WALLET_V0
      Inputs: contact_address, key_material, wallet_id_prefix
    - Code: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Purpose: Admits a request to accept a person
      Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Inputs: contact_address, verifying_authority
    - Code: blockchain::IN_ACTOR_REJECTION_V0
      Purpose: Admits a request to reject a person, refusing one that states no grounds
      Workflow: blockchain::WF_REJECT_ACTOR_V0
      Inputs: contact_address, verifying_authority, grounds
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: blockchain::CC_RESOLVE_ACTOR_V0
      Note: Owned by identity, read by wallet's workflow. Wallet reads a person and never writes one.
    - Code: blockchain::EV_ACTOR_ACCEPTED_V0
      Note: Declared and announced by identity. Wallet consumes the moment and declares none of the three.
    - Code: blockchain::WF_REGISTER_ACTOR_V0
      Note: Extended by this change although wallet does not use it, because the three declared moments are announced together or the gap simply moves.
    - Code: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
      Note: 'Built last: it declares the second subdomain, and declaring a subdomain whose artifacts do not yet exist would compile to nothing.'
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
