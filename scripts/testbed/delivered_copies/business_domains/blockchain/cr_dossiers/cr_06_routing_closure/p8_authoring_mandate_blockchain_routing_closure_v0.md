# Stage 8 — Authoring Mandate: blockchain / identity and wallet

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_06_routing_closure
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
      Code: blockchain::CC_RESOLVE_ACTOR_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '1'
      Step: '2'
      Code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: wallet
      Depends On: —
    - Wave: '1'
      Step: '3'
      Code: blockchain::CC_CREATE_WALLET_RECORD_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: wallet
      Depends On: —
    - Wave: '1'
      Step: '4'
      Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: wallet
      Depends On: —
    - Wave: '1'
      Step: '5'
      Code: blockchain::WF_REGISTER_ACTOR_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '2'
      Step: '6'
      Code: blockchain::WF_ACCEPT_ACTOR_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::CC_RESOLVE_ACTOR_V1
    - Wave: '2'
      Step: '7'
      Code: blockchain::WF_REJECT_ACTOR_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::CC_RESOLVE_ACTOR_V1
    - Wave: '2'
      Step: '8'
      Code: blockchain::WF_CREATE_WALLET_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: wallet
      Depends On: blockchain::CC_RESOLVE_ACTOR_V1, blockchain::CC_CLAIM_WALLET_IDENTITY_V1, blockchain::CC_CREATE_WALLET_RECORD_V1, blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: blockchain::CC_RESOLVE_ACTOR_V1
    - Position: '2'
      Code: blockchain::WF_CREATE_WALLET_V1
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '8'
      Description: The next versions of four contracts that end on a failed record, and of four acts that route a failed record to their rejected ending.
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Count: '8'
      Description: The published versions they stand in for, stood down unchanged.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: blockchain::CC_RESOLVE_ACTOR_V1
      Subdomain Field: identity
    - Code: blockchain::WF_REGISTER_ACTOR_V1
      Subdomain Field: identity
    - Code: blockchain::WF_ACCEPT_ACTOR_V1
      Subdomain Field: identity
    - Code: blockchain::WF_REJECT_ACTOR_V1
      Subdomain Field: identity
    - Code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Subdomain Field: wallet
    - Code: blockchain::CC_CREATE_WALLET_RECORD_V1
      Subdomain Field: wallet
    - Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Subdomain Field: wallet
    - Code: blockchain::WF_CREATE_WALLET_V1
      Subdomain Field: wallet
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: blockchain::CC_RESOLVE_ACTOR_V1
      Purpose: Answers which actor a contact address denotes, and reports when none does
      Inputs: contact_address
      Outputs: value
    - Code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Purpose: Claims the identity, and refuses when the person already holds a wallet
      Inputs: wallet_id
      Outputs: result_status
    - Code: blockchain::CC_CREATE_WALLET_RECORD_V1
      Purpose: Records the wallet with a balance of zero, its denomination and its classification
      Inputs: wallet_id, wallet_fields
      Outputs: result_status
    - Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Purpose: Records the moment on the wallet's trail
      Inputs: stream_id, occurrence_fields
      Outputs: result_status
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows: []
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: blockchain::CC_RESOLVE_ACTOR_V1
      Note: Identity's lookup, whose next version wallet runs too; both acts gain the same answer for a failed record.
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
