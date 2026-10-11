# Stage 7 — Design Intent: causal_language_model / model_response

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_02_hosted_model
  Status: DRAFT
  Feeds: Stage 8 — Authoring Mandate
registers:
  design_resolution:
    columns:
    - Decision
    - Business Fact
    - Resolution
    - Source Finding
    rows:
    - Decision: One act per step, driven by the host
      Business Fact: The host proposes; the business chooses
      Resolution: 'Three workflows: begin, offer, release. The host calls them; nothing in them calls the host'
      Source Finding: 'S4 design_decisions #1'
    - Decision: Admission is the test model's
      Business Fact: A hosted request is admitted under the same conditions
      Resolution: The begin act runs the four admission contracts and the reading check of the test model's way, unchanged and in the same order
      Source Finding: 'S4 design_decisions #2'
    - Decision: The reported size is checked with each offer
      Business Fact: The host counts what the model reads once it has it
      Resolution: The offer act compares the size the host reports with the capacity recorded at admission before anything is chosen, and records the report with the step
      Source Finding: 'S4 design_decisions #3'
    - Decision: The trail is the state
      Business Fact: One truth for a hosted request; an abandoned one stays visible
      Resolution: The opening entry holds what the model reads, the rules in force, the limits and the admitted fingerprint; each offer reads the trail and reduces it to the response as built; the existing record closes it
      Source Finding: 'S4 design_decisions #4'
    - Decision: Tokens are joined as they are
      Business Fact: A pattern split across tokens is not written
      Resolution: A new choice transform applies the test model's stopping and choosing to the text as built, with the permitted length
      Source Finding: 'S4 design_decisions #5'
    - Decision: The permitted length is the smaller limit
      Business Fact: The registered maximum and the rules' longest response both bind
      Resolution: The opening entry keeps both; the reduced state carries the smaller, and a token chosen at it that does not end the response refuses the request as unfinished
      Source Finding: 'S4 design_decisions #6'
    - Decision: The fingerprint is compared at every step
      Business Fact: An offer for another model is refused; the host is not authenticated
      Resolution: The offer act confirms the offered fingerprint is the admitted model's before choosing
      Source Finding: 'S4 design_decisions #7'
    - Decision: Release closes the record with the business's text
      Business Fact: The host never supplies what is released
      Resolution: The release act reads the trail, confirms the response complete, and records it with the text the trail holds
      Source Finding: 'S4 design_decisions #8'
    - Decision: Grounding is a rule of the time in service
      Business Fact: A time in service may require every number to be one the model read
      Resolution: The opening entry carries the stored rules' grounding beside the rules in force; the choice stops a number no number in the reading begins, or ends one that is not in it
      Source Finding: 'S4 design_decisions #9'
    - Decision: A number's beginning is judged, and its lookalikes
      Business Fact: A pattern judged only when complete lets its beginning through
      Resolution: The choice judges the compatibility form of the text, and stops the first digit of a forbidden number the model read unless it could still be a permitted one
      Source Finding: 'S4 design_decisions #10'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Appends every entry of a hosted request's trail and reads the trail back.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Assembles the opening and step entries of a hosted request's trail.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_RECORD_USER_PROMPT_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Confirms the reported reading size against the capacity.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Confirms an offer names the admitted model's fingerprint.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - FQDN: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reused unchanged by the hosted acts.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - FQDN: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reused unchanged by the hosted acts.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - FQDN: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reused unchanged by the hosted acts.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_ADMIT_USER_PROMPT_V0
    - FQDN: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reused unchanged by the hosted acts.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    - FQDN: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reused unchanged by the hosted acts.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_READING_FITS_V0
    - FQDN: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reused unchanged by the hosted acts.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    - FQDN: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reused unchanged by the hosted acts.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CC_RECORD_USER_PROMPT_V0
    - FQDN: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Forms the rules in force when a hosted request's record opens.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    - FQDN: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Binds the hosted acts to the subdomain's stores, as it binds the test model's.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - FQDN: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Declares the user prompt records the trail is kept in.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    - FQDN: causal_language_model::AC_REQUESTER_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The requester a hosted request is begun for.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::AC_REQUESTER_V0
    - FQDN: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced when a hosted response is released.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    - FQDN: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced when a hosted request is refused.
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::EV_USER_PROMPT_REFUSED_V0
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: The host of a model in service, which proposes and holds no authority
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): AC
      Code: causal_language_model::AC_MODEL_HOST_V0
      Summary: The host of a model in service, which proposes and holds no authority
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes AC_MODEL_HOST_V0
    - Capability: A request to a hosted model on behalf of a customer
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): IN
      Code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Summary: A request to a hosted model on behalf of a customer
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes IN_BEGIN_HOSTED_RESPONSE_V0
    - Capability: The candidates a hosted model could write next, naming its fingerprint
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): IN
      Code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Summary: The candidates a hosted model could write next, naming its fingerprint and the size of what it reads
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes IN_OFFER_NEXT_TOKENS_V0
    - Capability: A request to release a completed hosted response
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): IN
      Code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
      Summary: A request to release a completed hosted response
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes IN_RELEASE_HOSTED_RESPONSE_V0
    - Capability: Admitting a hosted request and opening its record, or refusing it
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Summary: Admitting a hosted request and opening its record, or refusing it
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes WF_BEGIN_HOSTED_RESPONSE_V0
    - Capability: Choosing a permitted token from an offer and recording the step, or refusing the request
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Summary: Choosing a permitted token from an offer and recording the step, or refusing the request
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes WF_OFFER_NEXT_TOKENS_V0
    - Capability: Releasing a completed hosted response from the record
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Summary: Releasing a completed hosted response from the record
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes WF_RELEASE_HOSTED_RESPONSE_V0
    - Capability: Refuse an offer whose reported reading size exceeds the model's capacity
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Summary: Refuse an offer whose reported reading size exceeds the model's capacity
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_CONFIRM_HOSTED_READING_FITS_V0
    - Capability: Form the rules in force and open the record of a hosted request
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Summary: Form the rules in force and open the record of a hosted request
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_OPEN_HOSTED_RECORD_V0
    - Capability: Read a hosted request's trail and reduce it to the response as built
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_READ_HOSTED_STATE_V0
      Summary: Read a hosted request's trail and reduce it to the response as built
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_READ_HOSTED_STATE_V0
    - Capability: Refuse an offer naming another model's fingerprint
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Summary: Refuse an offer naming another model's fingerprint
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_CONFIRM_OFFER_FOR_MODEL_V0
    - Capability: Choose a permitted token from an offer under the rules in force
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Summary: Choose a permitted token from an offer under the rules in force
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_CHOOSE_PERMITTED_TOKEN_V0
    - Capability: Record an offer and the choice made from it in the request's trail
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Summary: Record an offer and the choice made from it in the request's trail
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_RECORD_HOSTED_STEP_V0
    - Capability: Reduce a hosted request's trail to its state
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Summary: Reduces a hosted request's trail to the response as built, its position, whether it is complete, and its permitted length
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_READ_HOSTED_STATE_V0
    - Capability: Stop forbidden tokens and choose a permitted one
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Summary: Stops forbidden tokens among those offered and chooses one permitted token, joined as it is, within the permitted length
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Binds WF: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Binds WF: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Binds WF: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S6 pps_artifacts_requiring_action causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
  execution_topology:
    columns:
    - Workflow
    - Node
    - Runs
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_BEGIN_HOSTED_RESPONSE_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_ADMIT_USER_PROMPT_V0; VIOLATION -> RECORD_REFUSED_NOT_PERMITTED
      Source Finding: S7 new_artifacts CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0; NOT_FOUND -> RECORD_REFUSED_NOT_REGISTERED; VIOLATION -> RECORD_REFUSED_NOT_IN_SERVICE; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_ADMIT_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CONFIRM_READING_FITS_V0; NOT_FOUND -> RECORD_REFUSED_NOT_IN_SERVICE; VIOLATION -> RECORD_REFUSED_ABOVE_CEILING; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_WITHIN_CEILING_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_OPEN_HOSTED_RECORD_V0; VIOLATION -> RECORD_REFUSED_TOO_LONG_TO_READ
      Source Finding: S7 new_artifacts CC_CONFIRM_READING_FITS_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_WRITING; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_OPEN_HOSTED_RECORD_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: RECORD_REFUSED_NOT_PERMITTED
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: RECORD_REFUSED_NOT_REGISTERED
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: RECORD_REFUSED_NOT_IN_SERVICE
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: RECORD_REFUSED_ABOVE_CEILING
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: RECORD_REFUSED_TOO_LONG_TO_READ
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: EXIT_WRITING
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_BEGIN_HOSTED_RESPONSE_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: EXIT_REFUSED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_BEGIN_HOSTED_RESPONSE_V0
    - Workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_BEGIN_HOSTED_RESPONSE_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> causal_language_model::CC_READ_HOSTED_STATE_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_OFFER_NEXT_TOKENS_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: causal_language_model::CC_READ_HOSTED_STATE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_READ_HOSTED_STATE_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0; VIOLATION -> RECORD_REFUSED_OTHER_MODEL
      Source Finding: S7 new_artifacts CC_CONFIRM_OFFER_FOR_MODEL_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0; VIOLATION -> RECORD_REFUSED_TOO_LONG_TO_READ
      Source Finding: S7 new_artifacts CC_CONFIRM_HOSTED_READING_FITS_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> CONFIRM_NO_RULE_STOPPED; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CHOOSE_PERMITTED_TOKEN_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: CONFIRM_NO_RULE_STOPPED
      Runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> CONFIRM_WITHIN_LENGTH; VIOLATION -> RECORD_STOPPED_STEP
      Source Finding: S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: CONFIRM_WITHIN_LENGTH
      Runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> RECORD_STEP; VIOLATION -> RECORD_UNFINISHED_STEP
      Source Finding: S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: RECORD_STEP
      Runs: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_CHOSEN; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_HOSTED_STEP_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: RECORD_STOPPED_STEP
      Runs: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> RECORD_REFUSED_BY_RULE; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_HOSTED_STEP_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: RECORD_UNFINISHED_STEP
      Runs: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> RECORD_REFUSED_UNFINISHED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_HOSTED_STEP_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: RECORD_REFUSED_OTHER_MODEL
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: RECORD_REFUSED_TOO_LONG_TO_READ
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: RECORD_REFUSED_BY_RULE
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: RECORD_REFUSED_UNFINISHED
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: EXIT_CHOSEN
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_OFFER_NEXT_TOKENS_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: EXIT_REFUSED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_OFFER_NEXT_TOKENS_V0
    - Workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_OFFER_NEXT_TOKENS_V0
    - Workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Node: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> causal_language_model::CC_READ_HOSTED_STATE_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_RELEASE_HOSTED_RESPONSE_V0
    - Workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Node: causal_language_model::CC_READ_HOSTED_STATE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> CONFIRM_FINISHED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_READ_HOSTED_STATE_V0
    - Workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Node: CONFIRM_FINISHED
      Runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> RECORD_RESPONDED; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0
    - Workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Node: RECORD_RESPONDED
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_RESPONDED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Node: EXIT_RESPONDED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_RELEASE_HOSTED_RESPONSE_V0
    - Workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_RELEASE_HOSTED_RESPONSE_V0
  cc_composition:
    columns:
    - CC Code
    - Step
    - Step Name
    - Capability
    - Kind (CT, CS)
    - Operation
    - Store
    - Consumes
    - Produces
    - Routing
    - Interpreted By
    - Semantic Status
    - Interface
    rows:
    - CC Code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Step: '1'
      Step Name: confirm_reported_reading_fits
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: reported_reading_size, reading_capacity
      Produces: reading_fits
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=reported_reading_size, rules=reading_capacity; out: valid=reading_fits'
    - CC Code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: '1'
      Step Name: form_rules_in_force
      Capability: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Kind (CT, CS): CT
      Operation: FORM_RESPONSE_RULES
      Store: —
      Consumes: response_rules, account_numbers, seed
      Produces: rules_in_force, positions
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: response_rules=response_rules, account_numbers=account_numbers, seed=seed; out: rules_in_force=rules_in_force, positions=positions'
    - CC Code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: '2'
      Step Name: assemble_opening_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: user_prompt_id, requester_id, customer_id, identity_key, kind, question, supporting_material, time_in_service_id, reading, fingerprint, reading_capacity, maximum_response_length, response_rules
      Produces: opening_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=opening_fields; out: record=opening_record'
    - CC Code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: '3'
      Step Name: append_opening_record
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Kind (CT, CS): CS
      Operation: APPEND
      Store: USER_PROMPT_RECORDS
      Consumes: record, stream_id, actor_id
      Produces: record_id, sequence_number
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: causal_language_model::CC_READ_HOSTED_STATE_V0
      Step: '1'
      Step Name: read_trail
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Kind (CT, CS): CS
      Operation: GET_ALL
      Store: USER_PROMPT_RECORDS
      Consumes: stream_id
      Produces: entries
      Routing: SUCCESS -> continue; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: causal_language_model::CC_READ_HOSTED_STATE_V0
      Step: '2'
      Step Name: reduce_trail
      Capability: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Kind (CT, CS): CT
      Operation: READ_HOSTED_STATE
      Store: —
      Consumes: entries
      Produces: state
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: entries=entries; out: state=state'
    - CC Code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Step: '1'
      Step Name: confirm_same_model
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: offered_fingerprint, admitted_fingerprint
      Produces: offer_for_model
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=offered_fingerprint, allowed_set=admitted_fingerprint; out: is_member=offer_for_model'
    - CC Code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Step: '1'
      Step Name: choose_token
      Capability: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Kind (CT, CS): CT
      Operation: CHOOSE_PERMITTED_TOKEN
      Store: —
      Consumes: state, candidates
      Produces: step, text, finished, stopped_by, within_length
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: state=state, candidates=candidates; out: step=step, text=text, finished=finished, stopped_by=stopped_by, within_length=within_length'
    - CC Code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: '1'
      Step Name: assemble_step_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: user_prompt_id, host_id, fingerprint, reported_reading_size, step
      Produces: step_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=step_fields; out: record=step_record'
    - CC Code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: '2'
      Step Name: append_step_record
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Kind (CT, CS): CS
      Operation: APPEND
      Store: USER_PROMPT_RECORDS
      Consumes: record, stream_id, actor_id
      Produces: record_id, sequence_number
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Step: confirm_reported_reading_fits
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''reported_reading_size'': ''$.inputs.reported_reading_size''}'
      Source Finding: S7 cc_composition confirm_reported_reading_fits
    - Owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Step: confirm_reported_reading_fits
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''reported_reading_size'', ''op'': ''lte'', ''value'': ''$.inputs.reading_capacity''}]'
      Source Finding: S7 cc_composition confirm_reported_reading_fits
    - Owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Step: confirm_reported_reading_fits
      Direction (INPUT, OUTPUT): OUTPUT
      Field: reading_fits
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition confirm_reported_reading_fits
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): INPUT
      Field: response_rules
      Bound To: inputs.response_rules
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): INPUT
      Field: account_numbers
      Bound To: inputs.account_numbers
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): INPUT
      Field: seed
      Bound To: inputs.seed
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): OUTPUT
      Field: rules_in_force
      Bound To: capability_result.rules_in_force
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): OUTPUT
      Field: positions
      Bound To: capability_result.positions
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: assemble_opening_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''user_prompt_id'': ''$.inputs.user_prompt_id'', ''requester_id'': ''$.inputs.requester_id'', ''customer_id'': ''$.inputs.customer_id'', ''identity_key'': ''$.inputs.identity_key'', ''kind'': ''$.inputs.kind'', ''question'': ''$.inputs.question'', ''supporting_material'': ''$.inputs.supporting_material'', ''time_in_service_id'': ''$.inputs.time_in_service_id'', ''reading'': ''$.inputs.reading'', ''fingerprint'': ''$.inputs.fingerprint'', ''reading_capacity'': ''$.inputs.reading_capacity'', ''maximum_response_length'': ''$.inputs.maximum_response_length'', ''rules_in_force'': ''$.results.form_rules_in_force.rules_in_force'', ''ground_numbers'': ''$.inputs.response_rules.ground_numbers'', ''longest_response'': ''$.inputs.response_rules.longest_response'', ''outcome'': ''WRITING''}'
      Source Finding: S7 cc_composition assemble_opening_record
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: assemble_opening_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: opening_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_opening_record
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: append_opening_record
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: results.assemble_opening_record.opening_record
      Source Finding: S7 cc_composition append_opening_record
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: append_opening_record
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: inputs.user_prompt_id
      Source Finding: S7 cc_composition append_opening_record
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: append_opening_record
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_id
      Bound To: inputs.requester_id
      Source Finding: S7 cc_composition append_opening_record
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: append_opening_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record_id
      Bound To: capability_result.record_id
      Source Finding: S7 cc_composition append_opening_record
    - Owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Step: append_opening_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: sequence_number
      Bound To: capability_result.sequence_number
      Source Finding: S7 cc_composition append_opening_record
    - Owner: causal_language_model::CC_READ_HOSTED_STATE_V0
      Step: read_trail
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: inputs.user_prompt_id
      Source Finding: S7 cc_composition read_trail
    - Owner: causal_language_model::CC_READ_HOSTED_STATE_V0
      Step: read_trail
      Direction (INPUT, OUTPUT): OUTPUT
      Field: entries
      Bound To: capability_result.entries
      Source Finding: S7 cc_composition read_trail
    - Owner: causal_language_model::CC_READ_HOSTED_STATE_V0
      Step: read_trail
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_trail
    - Owner: causal_language_model::CC_READ_HOSTED_STATE_V0
      Step: reduce_trail
      Direction (INPUT, OUTPUT): INPUT
      Field: entries
      Bound To: results.read_trail.entries
      Source Finding: S7 cc_composition reduce_trail
    - Owner: causal_language_model::CC_READ_HOSTED_STATE_V0
      Step: reduce_trail
      Direction (INPUT, OUTPUT): OUTPUT
      Field: state
      Bound To: capability_result.state
      Source Finding: S7 cc_composition reduce_trail
    - Owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Step: confirm_same_model
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: inputs.offered_fingerprint
      Source Finding: S7 cc_composition confirm_same_model
    - Owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Step: confirm_same_model
      Direction (INPUT, OUTPUT): INPUT
      Field: allowed_set
      Bound To: '[''$.inputs.admitted_fingerprint'']'
      Source Finding: S7 cc_composition confirm_same_model
    - Owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Step: confirm_same_model
      Direction (INPUT, OUTPUT): OUTPUT
      Field: offer_for_model
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition confirm_same_model
    - Owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Step: choose_token
      Direction (INPUT, OUTPUT): INPUT
      Field: state
      Bound To: inputs.state
      Source Finding: S7 cc_composition choose_token
    - Owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Step: choose_token
      Direction (INPUT, OUTPUT): INPUT
      Field: candidates
      Bound To: inputs.candidates
      Source Finding: S7 cc_composition choose_token
    - Owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Step: choose_token
      Direction (INPUT, OUTPUT): OUTPUT
      Field: step
      Bound To: capability_result.step
      Source Finding: S7 cc_composition choose_token
    - Owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Step: choose_token
      Direction (INPUT, OUTPUT): OUTPUT
      Field: text
      Bound To: capability_result.text
      Source Finding: S7 cc_composition choose_token
    - Owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Step: choose_token
      Direction (INPUT, OUTPUT): OUTPUT
      Field: finished
      Bound To: capability_result.finished
      Source Finding: S7 cc_composition choose_token
    - Owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Step: choose_token
      Direction (INPUT, OUTPUT): OUTPUT
      Field: stopped_by
      Bound To: capability_result.stopped_by
      Source Finding: S7 cc_composition choose_token
    - Owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Step: choose_token
      Direction (INPUT, OUTPUT): OUTPUT
      Field: within_length
      Bound To: capability_result.within_length
      Source Finding: S7 cc_composition choose_token
    - Owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: assemble_step_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''user_prompt_id'': ''$.inputs.user_prompt_id'', ''outcome'': ''STEP'', ''host_id'': ''$.inputs.host_id'', ''fingerprint'': ''$.inputs.fingerprint'', ''reported_reading_size'': ''$.inputs.reported_reading_size'', ''position'': ''$.inputs.step.position'', ''candidates'': ''$.inputs.step.candidates'', ''chosen'': ''$.inputs.step.chosen'', ''stopped'': ''$.inputs.step.stopped'', ''stopped_by'': ''$.inputs.step.stopped_by'', ''finished'': ''$.inputs.step.finished'', ''within_length'': ''$.inputs.step.within_length''}'
      Source Finding: S7 cc_composition assemble_step_record
    - Owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: assemble_step_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: step_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_step_record
    - Owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: append_step_record
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: results.assemble_step_record.step_record
      Source Finding: S7 cc_composition append_step_record
    - Owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: append_step_record
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: inputs.user_prompt_id
      Source Finding: S7 cc_composition append_step_record
    - Owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: append_step_record
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_id
      Bound To: inputs.host_id
      Source Finding: S7 cc_composition append_step_record
    - Owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: append_step_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record_id
      Bound To: capability_result.record_id
      Source Finding: S7 cc_composition append_step_record
    - Owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Step: append_step_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: sequence_number
      Bound To: capability_result.sequence_number
      Source Finding: S7 cc_composition append_step_record
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: permitted_customers
      Bound To: payload.permitted_customers
      Source Finding: S7 execution_topology CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_ADMIT_USER_PROMPT_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology CC_CONFIRM_WITHIN_CEILING_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology CC_CONFIRM_WITHIN_CEILING_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: system_prompt
      Bound To: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt
      Source Finding: S7 execution_topology CC_CONFIRM_READING_FITS_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology CC_CONFIRM_READING_FITS_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology CC_CONFIRM_READING_FITS_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: reading_capacity
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
      Source Finding: S7 execution_topology CC_CONFIRM_READING_FITS_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: account_numbers
      Bound To: payload.account_numbers
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: seed
      Bound To: payload.seed
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_CONFIRM_READING_FITS_V0.reading
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: response_rules
      Bound To: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: fingerprint
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.fingerprint
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: reading_capacity
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: maximum_response_length
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.maximum_response_length
      Source Finding: S7 execution_topology CC_OPEN_HOSTED_RECORD_V0
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: requester_not_permitted_for_customer
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: model_not_registered
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: model_not_in_service
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: kind_above_sensitivity_ceiling
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: reading_longer_than_model_can_read
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: causal_language_model::CC_READ_HOSTED_STATE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology CC_READ_HOSTED_STATE_V0
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: offered_fingerprint
      Bound To: payload.fingerprint
      Source Finding: S7 execution_topology CC_CONFIRM_OFFER_FOR_MODEL_V0
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: admitted_fingerprint
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.fingerprint
      Source Finding: S7 execution_topology CC_CONFIRM_OFFER_FOR_MODEL_V0
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: reported_reading_size
      Bound To: payload.reported_reading_size
      Source Finding: S7 execution_topology CC_CONFIRM_HOSTED_READING_FITS_V0
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: reading_capacity
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.reading_capacity
      Source Finding: S7 execution_topology CC_CONFIRM_HOSTED_READING_FITS_V0
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: state
      Bound To: results.CC_READ_HOSTED_STATE_V0.state
      Source Finding: S7 execution_topology CC_CHOOSE_PERMITTED_TOKEN_V0
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: candidates
      Bound To: payload.candidates
      Source Finding: S7 execution_topology CC_CHOOSE_PERMITTED_TOKEN_V0
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: CONFIRM_NO_RULE_STOPPED
      Direction (INPUT, OUTPUT): INPUT
      Field: release_facts
      Bound To: '{''stopped_by'': ''$.results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by''}'
      Source Finding: S7 execution_topology CONFIRM_NO_RULE_STOPPED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: CONFIRM_NO_RULE_STOPPED
      Direction (INPUT, OUTPUT): INPUT
      Field: release_rules
      Bound To: '[{''field'': ''stopped_by'', ''op'': ''eq'', ''value'': ''none''}]'
      Source Finding: S7 execution_topology CONFIRM_NO_RULE_STOPPED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: CONFIRM_WITHIN_LENGTH
      Direction (INPUT, OUTPUT): INPUT
      Field: release_facts
      Bound To: '{''within_length'': ''$.results.CC_CHOOSE_PERMITTED_TOKEN_V0.within_length''}'
      Source Finding: S7 execution_topology CONFIRM_WITHIN_LENGTH
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: CONFIRM_WITHIN_LENGTH
      Direction (INPUT, OUTPUT): INPUT
      Field: release_rules
      Bound To: '[{''field'': ''within_length'', ''op'': ''eq'', ''value'': True}]'
      Source Finding: S7 execution_topology CONFIRM_WITHIN_LENGTH
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: host_id
      Bound To: payload.host_id
      Source Finding: S7 execution_topology RECORD_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: fingerprint
      Bound To: payload.fingerprint
      Source Finding: S7 execution_topology RECORD_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: reported_reading_size
      Bound To: payload.reported_reading_size
      Source Finding: S7 execution_topology RECORD_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: step
      Bound To: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
      Source Finding: S7 execution_topology RECORD_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STOPPED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_STOPPED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STOPPED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: host_id
      Bound To: payload.host_id
      Source Finding: S7 execution_topology RECORD_STOPPED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STOPPED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: fingerprint
      Bound To: payload.fingerprint
      Source Finding: S7 execution_topology RECORD_STOPPED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STOPPED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: reported_reading_size
      Bound To: payload.reported_reading_size
      Source Finding: S7 execution_topology RECORD_STOPPED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_STOPPED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: step
      Bound To: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
      Source Finding: S7 execution_topology RECORD_STOPPED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_UNFINISHED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_UNFINISHED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_UNFINISHED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: host_id
      Bound To: payload.host_id
      Source Finding: S7 execution_topology RECORD_UNFINISHED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_UNFINISHED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: fingerprint
      Bound To: payload.fingerprint
      Source Finding: S7 execution_topology RECORD_UNFINISHED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_UNFINISHED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: reported_reading_size
      Bound To: payload.reported_reading_size
      Source Finding: S7 execution_topology RECORD_UNFINISHED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_UNFINISHED_STEP
      Direction (INPUT, OUTPUT): INPUT
      Field: step
      Bound To: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
      Source Finding: S7 execution_topology RECORD_UNFINISHED_STEP
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.question
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: offer_for_another_model
      Source Finding: S7 execution_topology RECORD_REFUSED_OTHER_MODEL
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.question
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: reading_longer_than_model_can_read
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.question
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.question
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: longest_response_reached
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: causal_language_model::CC_READ_HOSTED_STATE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology CC_READ_HOSTED_STATE_V0
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: CONFIRM_FINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: release_facts
      Bound To: '{''finished'': ''$.results.CC_READ_HOSTED_STATE_V0.state.finished''}'
      Source Finding: S7 execution_topology CONFIRM_FINISHED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: CONFIRM_FINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: release_rules
      Bound To: '[{''field'': ''finished'', ''op'': ''eq'', ''value'': True}]'
      Source Finding: S7 execution_topology CONFIRM_FINISHED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.question
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: RESPONDED
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: response
      Bound To: results.CC_READ_HOSTED_STATE_V0.state.text
      Source Finding: S7 execution_topology RECORD_RESPONDED
  interface_fields:
    columns:
    - Artifact
    - Direction (INPUT, OUTPUT, ATTRIBUTE)
    - Field
    - Type
    - Required (YES, NO)
    - Default
    - Meaning
    rows:
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The request's identity, named by the requester and claimed once
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: requester_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The requester who submits the request
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: permitted_customers
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customers the requester may act for, as the business's existing arrangements state
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: customer_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer the request is for
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: account_numbers
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer's own account numbers, from the business's existing records
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key of the hosted model the request is for
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: kind
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most sensitive kind of information the question and its material contain
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: question
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the requester asks on the customer's behalf
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: supporting_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Material carried with the question for the model to read
    - Artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: seed
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The seed each adventurous choice is drawn from
    - Artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The request's identity, named by the requester and claimed once
    - Artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: host_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The host offering, as it names itself; recorded, not authenticated
    - Artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fingerprint of the model the offer is claimed to come from
    - Artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reported_reading_size
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many tokens the host reports the model reads for this request
    - Artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: candidates
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The tokens the model could write next, each with its likelihood
    - Artifact: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The request's identity, named by the requester and claimed once
    - Artifact: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: host_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The host offering, as it names itself; recorded, not authenticated
    - Artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reported_reading_size
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many tokens the host reports the model reads for this request
    - Artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading_capacity
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many tokens the model can read in one request
    - Artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: reading_fits
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the reported size is within the capacity
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The request's identity, named by the requester and claimed once
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: requester_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The requester who submits the request
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: customer_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer the request is for
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key of the hosted model the request is for
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: kind
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most sensitive kind of information the question and its material contain
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: question
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the requester asks on the customer's behalf
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: supporting_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Material carried with the question for the model to read
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: time_in_service_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The model's open time in service
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Exactly what the model reads
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: response_rules
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time in service's forbidden words and patterns, account-number shape, freedom and longest response
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: account_numbers
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer's own account numbers, from the business's existing records
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: seed
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The seed each adventurous choice is drawn from
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fingerprint of the model the offer is claimed to come from
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading_capacity
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many tokens the model can read in one request
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: maximum_response_length
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most tokens a response of the model may have
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: rules_in_force
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response rules in force for this request, with its seed
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: positions
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: One position per token up to the rules' longest response
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: opening_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The opening entry of the request's trail, with what the model reads
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: record_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The identity of the opening entry
    - Artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: sequence_number
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The opening entry's position in the user prompt records
    - Artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The request's identity, named by the requester and claimed once
    - Artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: entries
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The request's trail as recorded
    - Artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: state
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The hosted request's response as built, its position, whether it is complete, and its permitted length
    - Artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: offered_fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fingerprint an offer names
    - Artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: admitted_fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fingerprint of the model the request was admitted for
    - Artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: offer_for_model
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the offer names the admitted model's fingerprint
    - Artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: state
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The hosted request's response as built, its position, whether it is complete, and its permitted length
    - Artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: candidates
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The tokens the model could write next, each with its likelihood
    - Artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: step
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: One offer and the choice made from it
    - Artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: text
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response with the chosen token
    - Artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: finished
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the chosen token ends the response
    - Artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: stopped_by
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rule that left no permitted token, or none
    - Artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: within_length
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the response is still within its permitted length
    - Artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The request's identity, named by the requester and claimed once
    - Artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: host_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The host offering, as it names itself; recorded, not authenticated
    - Artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fingerprint of the model the offer is claimed to come from
    - Artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reported_reading_size
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many tokens the host reports the model reads for this request
    - Artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: step
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: One offer and the choice made from it
    - Artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: step_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The step entry appended to the request's trail
    - Artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: record_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The identity of the step entry
    - Artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: sequence_number
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The step entry's position in the user prompt records
    - Artifact: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: entries
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The request's trail as recorded
    - Artifact: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: state
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The hosted request's response as built, its position, whether it is complete, and its permitted length
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: state
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The hosted request's response as built, its position, whether it is complete, and its permitted length
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: candidates
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The tokens the model could write next, each with its likelihood
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: step
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: One offer and the choice made from it
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: text
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response with the chosen token
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: finished
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the chosen token ends the response
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: stopped_by
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rule that left no permitted token, or none
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: within_length
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the response is still within its permitted length
    - Artifact: causal_language_model::AC_MODEL_HOST_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: host_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The host's name for itself; recorded against every offer, not authenticated
  implementation_bindings:
    columns:
    - CT Code
    - Module
    - Callable
    - Operation
    - Kind (atom, molecule)
    - Purity (ct_pure, ct_impure)
    - Refusal (raises, returns, never)
    - Source Finding
    rows:
    - CT Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_read_hosted_state_v0
      Callable: execute
      Operation: READ_HOSTED_STATE
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: S7 new_artifacts CT_PURE_READ_HOSTED_STATE_V0
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_choose_permitted_token_v0
      Callable: execute
      Operation: CHOOSE_PERMITTED_TOKEN
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: S7 new_artifacts CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Group
    - Casing
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: NONE IDENTIFIED
      Extends: ''
      Group: ''
      Casing: ''
      Value: ''
      Meaning: ''
      Source Finding: ''
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows:
    - RB Code: NONE IDENTIFIED
      Capability: ''
      Key: ''
      Value: ''
      Source Finding: ''
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: causal_language_model::AC_MODEL_HOST_V0
      Property: type
      Value: ENDUSER
      Source Finding: S5 provisional_codes AC_MODEL_HOST_V0
    - Artifact: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
      Property: emit.EXIT_REFUSED
      Value: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Source Finding: 'S1 business_events #2'
    - Artifact: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Property: emit.EXIT_REFUSED
      Value: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Source Finding: 'S1 business_events #2'
    - Artifact: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Property: emit.EXIT_RESPONDED
      Value: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Source Finding: 'S1 business_events #1'
    - Artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Property: moment
      Value: refusal
      Source Finding: 'S1 business_events #2'
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: NONE IDENTIFIED
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): ''
      Proposed Path: ''
      Used By: ''
      Source Finding: ''
  transport_bindings:
    columns:
    - Artifact
    - Direction (INGRESS, EGRESS)
    - Operation
    - Handler Kind (WF_INVOCATION, SNAPSHOT_READ)
    - Handler Target
    - Field
    - Bound To
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Direction (INGRESS, EGRESS): ''
      Operation: ''
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): ''
      Handler Target: ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: model_response
      Count: '15'
      Artifacts: 1 AC, 3 IN, 3 WF, 6 CC, 2 CT
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Generator: ''
      Generator Sources: ''
      Source Finding: ''
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: NONE IDENTIFIED
      Consults: ''
      Source Finding: ''
  refusal_discharge:
    columns:
    - Operation
    - Refused When
    - Act
    - Step
    - Outcome
    - Source Finding
    rows:
    - Operation: Offer candidates
      Refused When: The reported reading size exceeds the model's reading capacity.
      Act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Offer candidates
      Refused When: The offer names a fingerprint other than the model's the request was admitted for.
      Act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_OTHER_MODEL
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Offer candidates
      Refused When: The request is not being written.
      Act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: causal_language_model::CC_READ_HOSTED_STATE_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #3'
    - Operation: Offer candidates
      Refused When: Every candidate is forbidden.
      Act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_BY_RULE
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #4'
    - Operation: Offer candidates
      Refused When: The response reaches its permitted length before it is complete.
      Act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
      Step: RECORD_REFUSED_UNFINISHED
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #5'
    - Operation: Release a response
      Refused When: The response is not complete.
      Act: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
      Step: CONFIRM_FINISHED
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #6'
  refusal_deferrals:
    columns:
    - Operation
    - Refused When
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Deferred To: ''
      Until: ''
      Source Finding: ''
  refusal_governance_discharge:
    columns:
    - Operation
    - Refused When
    - Phase
    - Governing Rule
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Phase: ''
      Governing Rule: ''
      Source Finding: ''
  molecule_steps:
    columns:
    - CT Code
    - Step
    - Kind (atom, molecule, loop)
    - Target
    - Over
    - Iterator
    - Emits
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Step: ''
      Kind (atom, molecule, loop): ''
      Target: ''
      Over: ''
      Iterator: ''
      Emits: ''
      Source Finding: ''
  molecule_step_bindings:
    columns:
    - CT Code
    - Step
    - Role (INPUT, CARRY, UPDATE)
    - Field
    - Bound To
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Step: ''
      Role (INPUT, CARRY, UPDATE): ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  test_cases:
    columns:
    - CT Code
    - Case
    - Expected Outcome (SUCCESS, VIOLATION)
    - Source Finding
    rows:
    - CT Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Case: reduces_the_trail_to_the_response_as_built
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Case: refuses_a_request_never_admitted
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Case: refuses_a_closed_request
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: stops_an_account_number_split_across_tokens
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: writes_the_customers_own_account_across_tokens
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: names_the_rule_when_no_permitted_token_remains
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: passes_the_permitted_length_unfinished
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: finishes_on_the_end_of_the_response
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: judges_a_lookalike_digit_as_the_digit
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: does_not_begin_a_forbidden_number_the_model_read
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: begins_a_number_the_model_read_that_is_permitted
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_writes_a_number_it_read
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_does_not_change_a_value_it_read
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: ungrounded_writes_a_number_it_did_not_read
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: refuses_an_offer_for_a_complete_response
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
  test_case_values:
    columns:
    - CT Code
    - Case
    - Role (INPUT, EXPECTED, ASSERT, RECORDED)
    - Field
    - Value
    - Source Finding
    rows:
    - CT Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Case: reduces_the_trail_to_the_response_as_built
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: entries
      Value: '[{sequence_number: 1, record: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}}, {sequence_number: 2, record: {outcome: STEP, chosen: ''Your''}}, {sequence_number: 3, record: {outcome: STEP, chosen: '' balance''}}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Case: reduces_the_trail_to_the_response_as_built
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Your balance'', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Case: refuses_a_request_never_admitted
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: entries
      Value: '[{sequence_number: 1, record: {outcome: REFUSED, reason: model_not_registered}}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
      Case: refuses_a_closed_request
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: entries
      Value: '[{sequence_number: 1, record: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}}, {sequence_number: 2, record: {outcome: RESPONDED}}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: stops_an_account_number_split_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 1, text: ''Account 8765'', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: stops_an_account_number_split_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: ''4321'', likelihood: 0.7}, {token: '' is'', likelihood: 0.2}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: stops_an_account_number_split_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Account 8765 is
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: stops_an_account_number_split_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: stops_an_account_number_split_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: stops_an_account_number_split_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: stops_an_account_number_split_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 2, candidates: [{token: ''4321'', likelihood: 0.7}, {token: '' is'', likelihood: 0.2}], chosen: '' is'', stopped: [{token: ''4321'', rule: another_customers_account_number}], stopped_by: none, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: writes_the_customers_own_account_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 1, text: ''Account 1234'', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: writes_the_customers_own_account_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: ''5678'', likelihood: 0.8}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: writes_the_customers_own_account_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Account 12345678
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: writes_the_customers_own_account_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: writes_the_customers_own_account_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 2, candidates: [{token: ''5678'', likelihood: 0.8}], chosen: ''5678'', stopped: [], stopped_by: none, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: writes_the_customers_own_account_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: writes_the_customers_own_account_across_tokens
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: names_the_rule_when_no_permitted_token_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 0, text: '''', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: names_the_rule_when_no_permitted_token_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: ''87654321'', likelihood: 0.9}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: names_the_rule_when_no_permitted_token_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: '""'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: names_the_rule_when_no_permitted_token_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: another_customers_account_number
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: names_the_rule_when_no_permitted_token_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: names_the_rule_when_no_permitted_token_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 1, candidates: [{token: ''87654321'', likelihood: 0.9}], chosen: null, stopped: [{token: ''87654321'', rule: another_customers_account_number}], stopped_by: another_customers_account_number, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: names_the_rule_when_no_permitted_token_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: passes_the_permitted_length_unfinished
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 3, text: ''Your balance is'', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: passes_the_permitted_length_unfinished
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: '' today'', likelihood: 0.9}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: passes_the_permitted_length_unfinished
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Your balance is today
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: passes_the_permitted_length_unfinished
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: passes_the_permitted_length_unfinished
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: passes_the_permitted_length_unfinished
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 4, candidates: [{token: '' today'', likelihood: 0.9}], chosen: '' today'', stopped: [], stopped_by: none, finished: false, within_length: false}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: passes_the_permitted_length_unfinished
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Your balance'', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: <end>, likelihood: 0.9}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Your balance
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 3, candidates: [{token: <end>, likelihood: 0.9}], chosen: <end>, stopped: [], stopped_by: none, finished: true, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: judges_a_lookalike_digit_as_the_digit
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Spouse account 8765432'', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: judges_a_lookalike_digit_as_the_digit
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: ''₁'', likelihood: 0.8}, {token: ''.'', likelihood: 0.1}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: judges_a_lookalike_digit_as_the_digit
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Spouse account 8765432.
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: judges_a_lookalike_digit_as_the_digit
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: judges_a_lookalike_digit_as_the_digit
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 3, candidates: [{token: "\u2081", likelihood: 0.8}, {token: ., likelihood: 0.1}], chosen: ., stopped: [{token: "\u2081", rule: another_customers_account_number}], stopped_by: none, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: judges_a_lookalike_digit_as_the_digit
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: judges_a_lookalike_digit_as_the_digit
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: does_not_begin_a_forbidden_number_the_model_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Spouse account '', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: does_not_begin_a_forbidden_number_the_model_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: ''8'', likelihood: 0.8}, {token: withheld, likelihood: 0.1}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: does_not_begin_a_forbidden_number_the_model_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Spouse account withheld
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: does_not_begin_a_forbidden_number_the_model_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: does_not_begin_a_forbidden_number_the_model_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 3, candidates: [{token: ''8'', likelihood: 0.8}, {token: withheld, likelihood: 0.1}], chosen: withheld, stopped: [{token: ''8'', rule: another_customers_account_number}], stopped_by: none, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: does_not_begin_a_forbidden_number_the_model_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: does_not_begin_a_forbidden_number_the_model_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: begins_a_number_the_model_read_that_is_permitted
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Balance '', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: begins_a_number_the_model_read_that_is_permitted
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: ''4'', likelihood: 0.8}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: begins_a_number_the_model_read_that_is_permitted
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Balance 4
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: begins_a_number_the_model_read_that_is_permitted
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: begins_a_number_the_model_read_that_is_permitted
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 3, candidates: [{token: ''4'', likelihood: 0.8}], chosen: ''4'', stopped: [], stopped_by: none, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: begins_a_number_the_model_read_that_is_permitted
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: begins_a_number_the_model_read_that_is_permitted
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_writes_a_number_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: true, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Balance 4'', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_writes_a_number_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: ''9'', likelihood: 0.8}, {token: ''0'', likelihood: 0.1}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_writes_a_number_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Balance 40
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_writes_a_number_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_writes_a_number_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 3, candidates: [{token: ''9'', likelihood: 0.8}, {token: ''0'', likelihood: 0.1}], chosen: ''0'', stopped: [{token: ''9'', rule: numbers_from_the_reading}], stopped_by: none, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_writes_a_number_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_writes_a_number_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_does_not_change_a_value_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: true, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Balance 4'', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_does_not_change_a_value_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: '' dollars'', likelihood: 0.8}, {token: <end>, likelihood: 0.1}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_does_not_change_a_value_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Balance 4
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_does_not_change_a_value_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: numbers_from_the_reading
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_does_not_change_a_value_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 3, candidates: [{token: '' dollars'', likelihood: 0.8}, {token: <end>, likelihood: 0.1}], chosen: null, stopped: [{token: '' dollars'', rule: numbers_from_the_reading}, {token: <end>, rule: numbers_from_the_reading}], stopped_by: numbers_from_the_reading, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_does_not_change_a_value_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: grounded_does_not_change_a_value_it_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: ungrounded_writes_a_number_it_did_not_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Balance '', finished: false, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: ungrounded_writes_a_number_it_did_not_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: ''9'', likelihood: 0.8}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: ungrounded_writes_a_number_it_did_not_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Balance 9
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: ungrounded_writes_a_number_it_did_not_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: ungrounded_writes_a_number_it_did_not_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: step
      Value: '{position: 3, candidates: [{token: ''9'', likelihood: 0.8}], chosen: ''9'', stopped: [], stopped_by: none, finished: false, within_length: true}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: ungrounded_writes_a_number_it_did_not_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: ungrounded_writes_a_number_it_did_not_read
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_length
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: refuses_an_offer_for_a_complete_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: state
      Value: '{opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: ''Answer only from the supporting material.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40. Spouse account 87654321.''}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: ''Your balance'', finished: true, limit: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
      Case: refuses_an_offer_for_a_complete_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{token: '' more'', likelihood: 0.9}]'
      Source Finding: human decision
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Fact: ''
      Reason: ''
      Source Finding: ''
```

Every binding names a field the capability declares, read from the pinned baseline
`b8dd7145232e48f29575a00a5f056ba68930e1a34a7cf8aae5e3e6b23a02f1ef`.

The hosted way is three acts beside the test model's, which is not touched. The host drives them: it
begins a request on the requester's behalf, offers the model's candidates one step at a time, and asks
for release. The business chooses, records and releases. A hosted request's record trail is its state:
an opening entry at admission, a step entry per offer, and a closing entry on release or refusal.

---

## 1. Design Decisions Resolution

---

## 2. Artifact Inventory — Existing Artifacts

---

## 3. Artifact Family Mapping — New Artifacts

---

## 4. Runtime Binding (RB) Declarations

---

## 5. Execution Topology

Every refusal is recorded before the act ends: the existing recording contract runs at one place per
refusal, each handed its outcome and reason. In the offer act, a step the rules or the length stopped
is recorded first, so the trail keeps the offer that ended the request; the step recording contract
runs at three places for that. The releasability contract runs at two places in the offer act and one
in the release act, each with its own condition.

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Implementation Bindings

The state is read from the trail and nowhere else: the opening entry, then the steps in the order they
were appended. A trail with no opening entry, or with a closing one, is refused. The chosen tokens are
joined as they are into the response so far; the end marker `<end>` ends it.

The choice stops a candidate when a forbidden rule's pattern matches the response so far joined to the
candidate, at a match that reaches into the candidate, unless the matched characters with spaces and
dashes removed are among the rule's exceptions. Text is judged in its compatibility form, so a
lookalike digit is the digit it looks like. A number is judged on its digits, spaces, commas, dots and
dashes between them being separators. A number the model read is not begun unless it could be a
permitted one: a candidate is stopped when it writes digits that begin a number a rule forbids in what
the model read, and begin no other number the model read. Where the opening sets grounding, a number
may not be begun unless a number the model read begins with its digits, nor ended unless it is one, and
a candidate that would do either is stopped by `numbers_from_the_reading`. It chooses among the
permitted candidates, most likely first and ties in offered order: of the first freedom-plus-one, the
one at position (seed plus the token's position) modulo their count. A response may have at most its
permitted length in tokens, the end marker not counted; a token that would take it past that leaves it
outside its length. An offer for a complete response is refused.

---

## 10. Vocabulary Extensions

---

## 11. Runtime Policies

---

## 12. Artifact Properties

---

## 13. STRUCTURE Stores

The trail is kept in the user prompt records the subdomain already declares; no store is added.

---

## 14. Transport Bindings

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

Every act reads only what model_response owns.

---

## 18. Refusal Discharge

A refusal that closes the request is discharged at the place that records it, whose success ends the
act at `EXIT_REFUSED`. An offer for a request not being written, and a release of an incomplete
response, change nothing and end at `EXIT_REJECTED`.

---

## 19. Refusal Deferrals

---

## 20. Refusal — Governance-Surface Discharge

---

## 21. Molecule Steps

---

## 22. Molecule Step Bindings

---

## 23. Test Cases

---

## 24. Test Case Values

---

## 25. Withdrawn Facts

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
