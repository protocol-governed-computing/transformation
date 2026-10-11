# Stage 8 — Authoring Mandate: causal_language_model / model_response

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_02_hosted_model
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
      Code: causal_language_model::AC_MODEL_HOST_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '2'
      Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '3'
      Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '4'
      Code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - Wave: '1'
      Step: '5'
      Code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0, capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - Wave: '1'
      Step: '6'
      Code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    - Wave: '1'
      Step: '7'
      Code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - Wave: '1'
      Step: '8'
      Code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '9'
      Code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '10'
      Code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '2'
      Step: '11'
      Code: causal_language_model::CC_READ_HOSTED_STATE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    - Wave: '2'
      Step: '12'
      Code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    - Wave: '2'
      Step: '13'
      Code: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0, causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0, causal_language_model::CC_CONFIRM_READING_FITS_V0, causal_language_model::CC_OPEN_HOSTED_RECORD_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::EV_USER_PROMPT_REFUSED_V0
    - Wave: '3'
      Step: '14'
      Code: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::IN_OFFER_NEXT_TOKENS_V0, causal_language_model::CC_READ_HOSTED_STATE_V0, causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0, causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0, causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0, causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_HOSTED_STEP_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::EV_USER_PROMPT_REFUSED_V0
    - Wave: '3'
      Step: '15'
      Code: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0, causal_language_model::CC_READ_HOSTED_STATE_V0, causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::EV_USER_PROMPT_RESPONDED_V0
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    - Position: '2'
      Code: causal_language_model::CC_READ_HOSTED_STATE_V0
    - Position: '3'
      Code: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '15'
      Description: 1 AC, 3 IN, 3 WF, 6 CC, 2 CT — every identity Stage 7 assigned
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: causal_language_model::AC_MODEL_HOST_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Subdomain Field: model_response
    - Code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Subdomain Field: model_response
    - Code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_READ_HOSTED_STATE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Subdomain Field: model_response
    - Code: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Subdomain Field: model_response
    - Code: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Subdomain Field: model_response
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Purpose: Reduce a hosted request's trail to its state
      Inputs: entries:array
      Outputs: state:object
    - Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Purpose: Stop forbidden tokens and choose a permitted one
      Inputs: state:object, candidates:array
      Outputs: step:object, text:string, finished:boolean, stopped_by:string, within_length:boolean
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Purpose: A request to a hosted model on behalf of a customer
      Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Inputs: user_prompt_id:string, requester_id:string, permitted_customers:array, customer_id:string, account_numbers:array, identity_key:string, kind:string, question:string, supporting_material:string, seed:integer
    - Code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Purpose: The candidates a hosted model could write next, naming its fingerprint
      Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Inputs: user_prompt_id:string, host_id:string, fingerprint:string, reported_reading_size:integer, candidates:array
    - Code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
      Purpose: A request to release a completed hosted response
      Workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Inputs: user_prompt_id:string, host_id:string
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: causal_language_model::AC_MODEL_HOST_V0
      Note: Names a host as it names itself. The host holds no authority and is not authenticated; each offer is checked against the admitted request, and a false one refuses the request.
```

The 15 artifacts Stage 7 designed, scheduled in dependency order. Nothing is added here and
nothing is dropped: the mandate orders the build, it does not decide it. Every artifact the design
reuses already exists in the composition and is named only as a dependency.

---

## 1. Build Dependency Order

Each artifact sits in the earliest wave its authored dependencies allow. Wave 1 holds the host, the
three entry points, the two atoms and the three contracts built from reused transforms alone. Wave 2
adds the contracts built on the new atoms. The three workflows come last, each waiting on the contracts
it runs.

---

## 2. Critical Path

The longest chain runs from the atom that reads the trail, through the contract that reads it, to the
offer act. No hosted response can be written until it is complete.

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

No model_response artifact writes into a store another subdomain owns.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | p7_design_intent_clm_hosted_model_v0.md | GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring | per build_order | PENDING |
