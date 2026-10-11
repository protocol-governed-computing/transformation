# Stage 8 — Authoring Mandate: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p8
  domain: causal_language_model
  subdomain: model_response
  cr: cr_01_model_response
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '2'
    code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '3'
    code: causal_language_model::AC_MODEL_STAFF_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '4'
    code: causal_language_model::AC_REQUESTER_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '5'
    code: causal_language_model::EV_MODEL_REGISTERED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '6'
    code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '7'
    code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '8'
    code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '9'
    code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '10'
    code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '11'
    code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '12'
    code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '13'
    code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '14'
    code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '15'
    code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '16'
    code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
  - wave: '1'
    step: '17'
    code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
  - wave: '1'
    step: '18'
    code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
  - wave: '1'
    step: '19'
    code: causal_language_model::IN_REGISTER_MODEL_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '20'
    code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '21'
    code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '22'
    code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '23'
    code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '2'
    step: '24'
    code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    - causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
  - wave: '2'
    step: '25'
    code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_side_effects::CS_REGISTRY_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - wave: '2'
    step: '26'
    code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    - capability_side_effects::CS_REGISTRY_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - wave: '2'
    step: '27'
    code: causal_language_model::CC_REGISTER_MODEL_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - wave: '2'
    step: '28'
    code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
  - wave: '2'
    step: '29'
    code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
  - wave: '2'
    step: '30'
    code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
  - wave: '2'
    step: '31'
    code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    - causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
  - wave: '2'
    step: '32'
    code: causal_language_model::CC_CONFIRM_READING_FITS_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
  - wave: '2'
    step: '33'
    code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - wave: '2'
    step: '34'
    code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - capability_transforms::CT_PURE_FILTER_RECORDS_V0
  - wave: '2'
    step: '35'
    code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - wave: '3'
    step: '36'
    code: causal_language_model::CT_WRITE_RESPONSE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_WRITE_NEXT_WORD_V0
  - wave: '3'
    step: '37'
    code: causal_language_model::WF_REGISTER_MODEL_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::IN_REGISTER_MODEL_V0
    - causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    - causal_language_model::CC_REGISTER_MODEL_V0
    - causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    - causal_language_model::EV_MODEL_REGISTERED_V0
  - wave: '3'
    step: '38'
    code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    - causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    - causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    - causal_language_model::EV_MODEL_SERVICE_STARTED_V0
  - wave: '3'
    step: '39'
    code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    - causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    - causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    - causal_language_model::EV_MODEL_SERVICE_ENDED_V0
  - wave: '3'
    step: '40'
    code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    - causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    - causal_language_model::CC_APPEND_MODEL_OPERATION_V0
  - wave: '4'
    step: '41'
    code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    - causal_language_model::CT_WRITE_RESPONSE_V0
  - wave: '5'
    step: '42'
    code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    - causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - causal_language_model::CC_ADMIT_USER_PROMPT_V0
    - causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    - causal_language_model::CC_CONFIRM_READING_FITS_V0
    - causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    - causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    - causal_language_model::CC_RECORD_USER_PROMPT_V0
    - causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
  - wave: '6'
    step: '43'
    code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::WF_REGISTER_MODEL_V0
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    - causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    - causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    - causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
  critical_path:
  - position: '1'
    code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
  - position: '2'
    code: causal_language_model::CT_WRITE_NEXT_WORD_V0
  - position: '3'
    code: causal_language_model::CT_WRITE_RESPONSE_V0
  - position: '4'
    code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
  - position: '5'
    code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
  - position: '6'
    code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
  mandate_artifact_summary:
  - action: NEW
    count: '43'
    description: 2 AC, 5 IN, 5 WF, 15 CC, 8 CT, 5 EV, 1 VOCAB, 1 RB, 1 STRUCTURE — every identity Stage 7 assigned
  field_declarations:
  - code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    subdomain_field: model_response
  - code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    subdomain_field: model_response
  - code: causal_language_model::AC_MODEL_STAFF_V0
    subdomain_field: model_response
  - code: causal_language_model::AC_REQUESTER_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_MODEL_REGISTERED_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_REGISTER_MODEL_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_REGISTER_MODEL_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_READING_FITS_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_WRITE_RESPONSE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_REGISTER_MODEL_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    subdomain_field: model_response
  - code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    subdomain_field: model_response
  new_capabilities:
  - code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    purpose: Form the single key claimed for a model from its description and fingerprint
    inputs: description:object, fingerprint:string
    outputs: identity_key:string
  - code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    purpose: Decide whether a kind of information is no more sensitive than a ceiling
    inputs: kind:string, ceiling:string, kinds:array
    outputs: within_ceiling:boolean
  - code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    purpose: Assemble exactly what the model reads and decide whether it fits
    inputs: system_prompt:string, question:string, supporting_material:string, reading_capacity:integer
    outputs: reading:object, reading_length:integer
  - code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    purpose: Form the response rules in force for one user prompt
    inputs: response_rules:object, account_numbers:array, seed:integer
    outputs: rules_in_force:object, positions:array
  - code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    purpose: The model's offer of its next words
    inputs: reading:object, text:string, finished:boolean, stopped_by:string
    outputs: candidates:array
  - code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    purpose: Stop forbidden words and choose one permitted word
    inputs: candidates:array, rules_in_force:object, position:integer, text:string, finished:boolean, stopped_by:string, stopped:array
    outputs: text:string, finished:boolean, stopped_by:string, stopped:array
  - code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    purpose: 'One pass of writing: the model''s offer, then the rules'' choice'
    inputs: reading:object, rules_in_force:object, position:integer, text:string, finished:boolean, stopped_by:string, stopped:array
    outputs: result:object
  - code: causal_language_model::CT_WRITE_RESPONSE_V0
    purpose: Write a response one pass per word, up to the longest response
    inputs: reading:object, rules_in_force:object, positions:array
    outputs: result:object
  new_intents:
  - code: causal_language_model::IN_REGISTER_MODEL_V0
    purpose: A request to register a model with its description and fingerprint
    workflow: causal_language_model::WF_REGISTER_MODEL_V0
    inputs: staff_credentials:object, staff_id:string, description:object, fingerprint:string
  - code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    purpose: A request to place a registered model in service with its ceiling, system prompt and response rules
    workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    inputs: staff_credentials:object, staff_id:string, identity_key:string, time_in_service_id:string, ceiling:string, system_prompt:string, response_rules:object
  - code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    purpose: A request to withdraw a model from service
    workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    inputs: staff_credentials:object, staff_id:string, identity_key:string
  - code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    purpose: A user prompt submitted on behalf of a customer
    workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    inputs: user_prompt_id:string, requester_id:string, permitted_customers:array, customer_id:string, account_numbers:array, identity_key:string, kind:string, question:string, supporting_material:string, seed:integer
  - code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    purpose: A request to retrieve the record of a user prompt
    workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    inputs: staff_credentials:object, staff_id:string, user_prompt_id:string
  cross_subdomain_notes:
  - code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    note: Checks the staff member's asserted credentials against rules this design fixes, and grants nothing. Who is model staff is decided by the business's existing arrangements, which assert it through the ingress.
  - code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    note: Checks the customer against the requester's permitted customers as the business's existing arrangements assert them, and grants nothing.
```

The 43 artifacts Stage 7 designed, scheduled in dependency order. Nothing is added here and
nothing is dropped: the mandate orders the build, it does not decide it. Every artifact the design
reuses already exists in the composition and is named only as a dependency.

---

## 1. Build Dependency Order

Each artifact sits in the earliest wave its authored dependencies allow. Wave 1 holds everything that
depends only on the platform: the store declaration, the vocabulary, the actors, the business moments,
the six atoms, the entry points and the three contracts built from reused transforms alone. Wave 2 adds
the pass molecule and the contracts that address a store or a new atom. Wave 3 adds the response
molecule and the four staff workflows. The writing contract waits on the response molecule, the
submission workflow on the writing contract, and the runtime binding, which binds every workflow,
comes last.

---

## 2. Critical Path

The longest chain runs from the model's offer through both writing molecules, the writing contract
and the submission workflow to the runtime binding. No user prompt can be answered until it is
complete.

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
| Stage 7 — Design Intent | p7_design_intent_clm_model_response_v0.md | GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring | per build_order | PENDING |
