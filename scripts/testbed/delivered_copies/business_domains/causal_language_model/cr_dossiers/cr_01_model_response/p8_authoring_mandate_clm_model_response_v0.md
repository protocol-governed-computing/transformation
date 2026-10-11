# Stage 8 — Authoring Mandate: causal_language_model / model_response

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_01_model_response
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
      Code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '2'
      Code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '3'
      Code: causal_language_model::AC_MODEL_STAFF_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '4'
      Code: causal_language_model::AC_REQUESTER_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '5'
      Code: causal_language_model::EV_MODEL_REGISTERED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '6'
      Code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '7'
      Code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '8'
      Code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '9'
      Code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '10'
      Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '11'
      Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '12'
      Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '13'
      Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '14'
      Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '15'
      Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '16'
      Code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - Wave: '1'
      Step: '17'
      Code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    - Wave: '1'
      Step: '18'
      Code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - Wave: '1'
      Step: '19'
      Code: causal_language_model::IN_REGISTER_MODEL_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '20'
      Code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '21'
      Code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '22'
      Code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '1'
      Step: '23'
      Code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: —
    - Wave: '2'
      Step: '24'
      Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0, causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    - Wave: '2'
      Step: '25'
      Code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_side_effects::CS_REGISTRY_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - Wave: '2'
      Step: '26'
      Code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0, capability_side_effects::CS_REGISTRY_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - Wave: '2'
      Step: '27'
      Code: causal_language_model::CC_REGISTER_MODEL_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - Wave: '2'
      Step: '28'
      Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0, capability_side_effects::CS_REGISTRY_V0, capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - Wave: '2'
      Step: '29'
      Code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - Wave: '2'
      Step: '30'
      Code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - Wave: '2'
      Step: '31'
      Code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0, causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    - Wave: '2'
      Step: '32'
      Code: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    - Wave: '2'
      Step: '33'
      Code: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - Wave: '2'
      Step: '34'
      Code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_FILTER_RECORDS_V0
    - Wave: '2'
      Step: '35'
      Code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - Wave: '3'
      Step: '36'
      Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::CT_WRITE_NEXT_WORD_V0
    - Wave: '3'
      Step: '37'
      Code: causal_language_model::WF_REGISTER_MODEL_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::IN_REGISTER_MODEL_V0, causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0, causal_language_model::CC_REGISTER_MODEL_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0, causal_language_model::EV_MODEL_REGISTERED_V0
    - Wave: '3'
      Step: '38'
      Code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0, causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0, causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    - Wave: '3'
      Step: '39'
      Code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0, causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0, causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    - Wave: '3'
      Step: '40'
      Code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0, causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    - Wave: '4'
      Step: '41'
      Code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0, causal_language_model::CT_WRITE_RESPONSE_V0
    - Wave: '5'
      Step: '42'
      Code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::IN_SUBMIT_USER_PROMPT_V0, causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0, causal_language_model::CC_CONFIRM_READING_FITS_V0, causal_language_model::CC_WRITE_MODEL_RESPONSE_V0, causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::EV_USER_PROMPT_RESPONDED_V0, causal_language_model::EV_USER_PROMPT_REFUSED_V0
    - Wave: '6'
      Step: '43'
      Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Depends On: causal_language_model::WF_REGISTER_MODEL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0, causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0, causal_language_model::WF_SUBMIT_USER_PROMPT_V0, causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    - Position: '2'
      Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    - Position: '3'
      Code: causal_language_model::CT_WRITE_RESPONSE_V0
    - Position: '4'
      Code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    - Position: '5'
      Code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    - Position: '6'
      Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '43'
      Description: 2 AC, 5 IN, 5 WF, 15 CC, 8 CT, 5 EV, 1 VOCAB, 1 RB, 1 STRUCTURE — every identity Stage 7 assigned
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
      Subdomain Field: model_response
    - Code: causal_language_model::AC_MODEL_STAFF_V0
      Subdomain Field: model_response
    - Code: causal_language_model::AC_REQUESTER_V0
      Subdomain Field: model_response
    - Code: causal_language_model::EV_MODEL_REGISTERED_V0
      Subdomain Field: model_response
    - Code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
      Subdomain Field: model_response
    - Code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
      Subdomain Field: model_response
    - Code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Subdomain Field: model_response
    - Code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::IN_REGISTER_MODEL_V0
      Subdomain Field: model_response
    - Code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Subdomain Field: model_response
    - Code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_REGISTER_MODEL_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::WF_REGISTER_MODEL_V0
      Subdomain Field: model_response
    - Code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Subdomain Field: model_response
    - Code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Subdomain Field: model_response
    - Code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Subdomain Field: model_response
    - Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Subdomain Field: model_response
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Purpose: Form the single key claimed for a model from its description and fingerprint
      Inputs: description:object, fingerprint:string
      Outputs: identity_key:string
    - Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Purpose: Decide whether a kind of information is no more sensitive than a ceiling
      Inputs: kind:string, ceiling:string, kinds:array
      Outputs: within_ceiling:boolean
    - Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Purpose: Assemble exactly what the model reads and decide whether it fits
      Inputs: system_prompt:string, question:string, supporting_material:string, reading_capacity:integer
      Outputs: reading:object, reading_length:integer
    - Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Purpose: Form the response rules in force for one user prompt
      Inputs: response_rules:object, account_numbers:array, seed:integer
      Outputs: rules_in_force:object, positions:array
    - Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Purpose: The model's offer of its next words
      Inputs: reading:object, text:string, finished:boolean, stopped_by:string
      Outputs: candidates:array
    - Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Purpose: Stop forbidden words and choose one permitted word
      Inputs: candidates:array, rules_in_force:object, position:integer, text:string, finished:boolean, stopped_by:string, stopped:array
      Outputs: text:string, finished:boolean, stopped_by:string, stopped:array
    - Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Purpose: 'One pass of writing: the model''s offer, then the rules'' choice'
      Inputs: reading:object, rules_in_force:object, position:integer, text:string, finished:boolean, stopped_by:string, stopped:array
      Outputs: result:object
    - Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Purpose: Write a response one pass per word, up to the longest response
      Inputs: reading:object, rules_in_force:object, positions:array
      Outputs: result:object
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: causal_language_model::IN_REGISTER_MODEL_V0
      Purpose: A request to register a model with its description and fingerprint
      Workflow: causal_language_model::WF_REGISTER_MODEL_V0
      Inputs: staff_credentials:object, staff_id:string, description:object, fingerprint:string
    - Code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Purpose: A request to place a registered model in service with its ceiling, system prompt and response rules
      Workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Inputs: staff_credentials:object, staff_id:string, identity_key:string, time_in_service_id:string, ceiling:string, system_prompt:string, response_rules:object
    - Code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
      Purpose: A request to withdraw a model from service
      Workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Inputs: staff_credentials:object, staff_id:string, identity_key:string
    - Code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Purpose: A user prompt submitted on behalf of a customer
      Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Inputs: user_prompt_id:string, requester_id:string, permitted_customers:array, customer_id:string, account_numbers:array, identity_key:string, kind:string, question:string, supporting_material:string, seed:integer
    - Code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
      Purpose: A request to retrieve the record of a user prompt
      Workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Inputs: staff_credentials:object, staff_id:string, user_prompt_id:string
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Note: Checks the staff member's asserted credentials against rules this design fixes, and grants nothing. Who is model staff is decided by the business's existing arrangements, which assert it through the ingress.
    - Code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Note: Checks the customer against the requester's permitted customers as the business's existing arrangements assert them, and grants nothing.
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
