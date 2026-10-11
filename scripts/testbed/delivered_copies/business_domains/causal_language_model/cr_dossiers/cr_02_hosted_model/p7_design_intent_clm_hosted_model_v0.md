# Stage 7 — Design Intent: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p7
  domain: causal_language_model
  subdomain: model_response
  cr: cr_02_hosted_model
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: One act per step, driven by the host
    business_fact: The host proposes; the business chooses
    resolution: 'Three workflows: begin, offer, release. The host calls them; nothing in them calls the host'
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: Admission is the test model's
    business_fact: A hosted request is admitted under the same conditions
    resolution: The begin act runs the four admission contracts and the reading check of the test model's way, unchanged and in the same order
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: The reported size is checked with each offer
    business_fact: The host counts what the model reads once it has it
    resolution: The offer act compares the size the host reports with the capacity recorded at admission before anything is chosen, and records the report with the step
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: The trail is the state
    business_fact: One truth for a hosted request; an abandoned one stays visible
    resolution: The opening entry holds what the model reads, the rules in force, the limits and the admitted fingerprint; each offer reads the trail and reduces it to the response as built; the existing record closes it
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: Tokens are joined as they are
    business_fact: A pattern split across tokens is not written
    resolution: A new choice transform applies the test model's stopping and choosing to the text as built, with the permitted length
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: The permitted length is the smaller limit
    business_fact: The registered maximum and the rules' longest response both bind
    resolution: The opening entry keeps both; the reduced state carries the smaller, and a token chosen at it that does not end the response refuses the request as unfinished
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - decision: The fingerprint is compared at every step
    business_fact: An offer for another model is refused; the host is not authenticated
    resolution: The offer act confirms the offered fingerprint is the admitted model's before choosing
    source_finding: {phase: p4, register: design_decisions, row: 7}
  - decision: Release closes the record with the business's text
    business_fact: The host never supplies what is released
    resolution: The release act reads the trail, confirms the response complete, and records it with the text the trail holds
    source_finding: {phase: p4, register: design_decisions, row: 8}
  - decision: Grounding is a rule of the time in service
    business_fact: A time in service may require every number to be one the model read
    resolution: The opening entry carries the stored rules' grounding beside the rules in force; the choice stops a number no number in the reading begins, or ends one that is not in it
    source_finding: {phase: p4, register: design_decisions, row: 9}
  - decision: A number's beginning is judged, and its lookalikes
    business_fact: A pattern judged only when complete lets its beginning through
    resolution: The choice judges the compatibility form of the text, and stops the first digit of a forbidden number the model read unless it could still be a permitted one
    source_finding: {phase: p4, register: design_decisions, row: 10}
  existing_inventory:
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: ''
    reason: Appends every entry of a hosted request's trail and reads the trail back.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0'}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: ''
    reason: Assembles the opening and step entries of a hosted request's trail.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_RECORD_USER_PROMPT_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    action: REUSE
    summary: ''
    reason: Confirms the reported reading size against the capacity.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    action: REUSE
    summary: ''
    reason: Confirms an offer names the admitted model's fingerprint.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0'}
  - fqdn: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Reused unchanged by the hosted acts.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0'}
  - fqdn: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    action: REUSE
    summary: ''
    reason: Reused unchanged by the hosted acts.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0'}
  - fqdn: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    action: REUSE
    summary: ''
    reason: Reused unchanged by the hosted acts.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_ADMIT_USER_PROMPT_V0'}
  - fqdn: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    action: REUSE
    summary: ''
    reason: Reused unchanged by the hosted acts.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0'}
  - fqdn: causal_language_model::CC_CONFIRM_READING_FITS_V0
    action: REUSE
    summary: ''
    reason: Reused unchanged by the hosted acts.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_CONFIRM_READING_FITS_V0'}
  - fqdn: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    action: REUSE
    summary: ''
    reason: Reused unchanged by the hosted acts.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0'}
  - fqdn: causal_language_model::CC_RECORD_USER_PROMPT_V0
    action: REUSE
    summary: ''
    reason: Reused unchanged by the hosted acts.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CC_RECORD_USER_PROMPT_V0'}
  - fqdn: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    action: REUSE
    summary: ''
    reason: Forms the rules in force when a hosted request's record opens.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0'}
  - fqdn: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    action: REUSE
    summary: ''
    reason: Binds the hosted acts to the subdomain's stores, as it binds the test model's.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0'}
  - fqdn: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    action: REUSE
    summary: ''
    reason: Declares the user prompt records the trail is kept in.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0'}
  - fqdn: causal_language_model::AC_REQUESTER_V0
    action: REUSE
    summary: ''
    reason: The requester a hosted request is begun for.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::AC_REQUESTER_V0'}
  - fqdn: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    action: REUSE
    summary: ''
    reason: Announced when a hosted response is released.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::EV_USER_PROMPT_RESPONDED_V0'}
  - fqdn: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    action: REUSE
    summary: ''
    reason: Announced when a hosted request is refused.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::EV_USER_PROMPT_REFUSED_V0'}
  new_artifacts:
  - capability: The host of a model in service, which proposes and holds no authority
    family: AC
    code: causal_language_model::AC_MODEL_HOST_V0
    summary: The host of a model in service, which proposes and holds no authority
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: AC_MODEL_HOST_V0}
  - capability: A request to a hosted model on behalf of a customer
    family: IN
    code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    summary: A request to a hosted model on behalf of a customer
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_BEGIN_HOSTED_RESPONSE_V0}
  - capability: The candidates a hosted model could write next, naming its fingerprint
    family: IN
    code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    summary: The candidates a hosted model could write next, naming its fingerprint and the size of what it reads
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_OFFER_NEXT_TOKENS_V0}
  - capability: A request to release a completed hosted response
    family: IN
    code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    summary: A request to release a completed hosted response
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_RELEASE_HOSTED_RESPONSE_V0}
  - capability: Admitting a hosted request and opening its record, or refusing it
    family: WF
    code: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    summary: Admitting a hosted request and opening its record, or refusing it
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_BEGIN_HOSTED_RESPONSE_V0}
  - capability: Choosing a permitted token from an offer and recording the step, or refusing the request
    family: WF
    code: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    summary: Choosing a permitted token from an offer and recording the step, or refusing the request
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_OFFER_NEXT_TOKENS_V0}
  - capability: Releasing a completed hosted response from the record
    family: WF
    code: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    summary: Releasing a completed hosted response from the record
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_RELEASE_HOSTED_RESPONSE_V0}
  - capability: Refuse an offer whose reported reading size exceeds the model's capacity
    family: CC
    code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    summary: Refuse an offer whose reported reading size exceeds the model's capacity
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CONFIRM_HOSTED_READING_FITS_V0}
  - capability: Form the rules in force and open the record of a hosted request
    family: CC
    code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    summary: Form the rules in force and open the record of a hosted request
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_OPEN_HOSTED_RECORD_V0}
  - capability: Read a hosted request's trail and reduce it to the response as built
    family: CC
    code: causal_language_model::CC_READ_HOSTED_STATE_V0
    summary: Read a hosted request's trail and reduce it to the response as built
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_READ_HOSTED_STATE_V0}
  - capability: Refuse an offer naming another model's fingerprint
    family: CC
    code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    summary: Refuse an offer naming another model's fingerprint
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CONFIRM_OFFER_FOR_MODEL_V0}
  - capability: Choose a permitted token from an offer under the rules in force
    family: CC
    code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    summary: Choose a permitted token from an offer under the rules in force
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CHOOSE_PERMITTED_TOKEN_V0}
  - capability: Record an offer and the choice made from it in the request's trail
    family: CC
    code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    summary: Record an offer and the choice made from it in the request's trail
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_RECORD_HOSTED_STEP_V0}
  - capability: Reduce a hosted request's trail to its state
    family: CT
    code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    summary: Reduces a hosted request's trail to the response as built, its position, whether it is complete, and its permitted length
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_READ_HOSTED_STATE_V0}
  - capability: Stop forbidden tokens and choose a permitted one
    family: CT
    code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    summary: Stops forbidden tokens among those offered and chooses one permitted token, joined as it is, within the permitted length
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_CHOOSE_PERMITTED_TOKEN_V0}
  rb_declarations:
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0'}
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0'}
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0'}
  execution_topology:
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    runs: ''
    node_type: IN
    routing:
      ACK: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_BEGIN_HOSTED_RESPONSE_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_USER_PROMPT_IDENTITY_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      VIOLATION: RECORD_REFUSED_NOT_PERMITTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      NOT_FOUND: RECORD_REFUSED_NOT_REGISTERED
      VIOLATION: RECORD_REFUSED_NOT_IN_SERVICE
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_ADMIT_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CONFIRM_READING_FITS_V0
      NOT_FOUND: RECORD_REFUSED_NOT_IN_SERVICE
      VIOLATION: RECORD_REFUSED_ABOVE_CEILING
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_WITHIN_CEILING_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: causal_language_model::CC_CONFIRM_READING_FITS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
      VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_READING_FITS_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_WRITING
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_OPEN_HOSTED_RECORD_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_NOT_PERMITTED
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_NOT_REGISTERED
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_NOT_IN_SERVICE
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_ABOVE_CEILING
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_TOO_LONG_TO_READ
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: EXIT_WRITING
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_BEGIN_HOSTED_RESPONSE_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: EXIT_REFUSED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_BEGIN_HOSTED_RESPONSE_V0}
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_BEGIN_HOSTED_RESPONSE_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    runs: ''
    node_type: IN
    routing:
      ACK: causal_language_model::CC_READ_HOSTED_STATE_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_OFFER_NEXT_TOKENS_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: causal_language_model::CC_READ_HOSTED_STATE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_READ_HOSTED_STATE_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
      VIOLATION: RECORD_REFUSED_OTHER_MODEL
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_OFFER_FOR_MODEL_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
      VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_HOSTED_READING_FITS_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: CONFIRM_NO_RULE_STOPPED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CHOOSE_PERMITTED_TOKEN_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: CONFIRM_NO_RULE_STOPPED
    runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    node_type: CC
    routing:
      SUCCESS: CONFIRM_WITHIN_LENGTH
      VIOLATION: RECORD_STOPPED_STEP
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_RESPONSE_RELEASABLE_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: CONFIRM_WITHIN_LENGTH
    runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_STEP
      VIOLATION: RECORD_UNFINISHED_STEP
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_RESPONSE_RELEASABLE_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_STEP
    runs: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_CHOSEN
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_HOSTED_STEP_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_STOPPED_STEP
    runs: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_REFUSED_BY_RULE
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_HOSTED_STEP_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_UNFINISHED_STEP
    runs: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_REFUSED_UNFINISHED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_HOSTED_STEP_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_REFUSED_OTHER_MODEL
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_REFUSED_TOO_LONG_TO_READ
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_REFUSED_BY_RULE
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_REFUSED_UNFINISHED
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: EXIT_CHOSEN
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_OFFER_NEXT_TOKENS_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: EXIT_REFUSED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_OFFER_NEXT_TOKENS_V0}
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_OFFER_NEXT_TOKENS_V0}
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    runs: ''
    node_type: IN
    routing:
      ACK: causal_language_model::CC_READ_HOSTED_STATE_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_RELEASE_HOSTED_RESPONSE_V0}
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: causal_language_model::CC_READ_HOSTED_STATE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: CONFIRM_FINISHED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_READ_HOSTED_STATE_V0}
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: CONFIRM_FINISHED
    runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_RESPONDED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_RESPONSE_RELEASABLE_V0}
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: RECORD_RESPONDED
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_RESPONDED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: EXIT_RESPONDED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RELEASE_HOSTED_RESPONSE_V0}
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RELEASE_HOSTED_RESPONSE_V0}
  cc_composition:
  - cc_code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    step: '1'
    step_name: confirm_reported_reading_fits
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - reported_reading_size
    - reading_capacity
    produces:
    - reading_fits
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: reported_reading_size
        rules: reading_capacity
      out:
        valid: reading_fits
  - cc_code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: '1'
    step_name: form_rules_in_force
    capability: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    kind: CT
    operation: FORM_RESPONSE_RULES
    store: null
    consumes:
    - response_rules
    - account_numbers
    - seed
    produces:
    - rules_in_force
    - positions
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        response_rules: response_rules
        account_numbers: account_numbers
        seed: seed
      out:
        rules_in_force: rules_in_force
        positions: positions
  - cc_code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: '2'
    step_name: assemble_opening_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - user_prompt_id
    - requester_id
    - customer_id
    - identity_key
    - kind
    - question
    - supporting_material
    - time_in_service_id
    - reading
    - fingerprint
    - reading_capacity
    - maximum_response_length
    - response_rules
    produces:
    - opening_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: opening_fields
      out:
        record: opening_record
  - cc_code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: '3'
    step_name: append_opening_record
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: USER_PROMPT_RECORDS
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - record_id
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: '1'
    step_name: read_trail
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: GET_ALL
    store: USER_PROMPT_RECORDS
    consumes:
    - stream_id
    produces:
    - entries
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: '2'
    step_name: reduce_trail
    capability: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    kind: CT
    operation: READ_HOSTED_STATE
    store: null
    consumes:
    - entries
    produces:
    - state
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        entries: entries
      out:
        state: state
  - cc_code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    step: '1'
    step_name: confirm_same_model
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - offered_fingerprint
    - admitted_fingerprint
    produces:
    - offer_for_model
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: offered_fingerprint
        allowed_set: admitted_fingerprint
      out:
        is_member: offer_for_model
  - cc_code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: '1'
    step_name: choose_token
    capability: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    kind: CT
    operation: CHOOSE_PERMITTED_TOKEN
    store: null
    consumes:
    - state
    - candidates
    produces:
    - step
    - text
    - finished
    - stopped_by
    - within_length
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        state: state
        candidates: candidates
      out:
        step: step
        text: text
        finished: finished
        stopped_by: stopped_by
        within_length: within_length
  - cc_code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: '1'
    step_name: assemble_step_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - user_prompt_id
    - host_id
    - fingerprint
    - reported_reading_size
    - step
    produces:
    - step_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: step_fields
      out:
        record: step_record
  - cc_code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: '2'
    step_name: append_step_record
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: USER_PROMPT_RECORDS
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - record_id
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  step_bindings:
  - owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    step: confirm_reported_reading_fits
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        reported_reading_size: $.inputs.reported_reading_size
    source_finding: {phase: p7, register: cc_composition, key: confirm_reported_reading_fits}
  - owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    step: confirm_reported_reading_fits
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: reported_reading_size
        op: lte
        value: $.inputs.reading_capacity
    source_finding: {phase: p7, register: cc_composition, key: confirm_reported_reading_fits}
  - owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    step: confirm_reported_reading_fits
    direction: OUTPUT
    field: reading_fits
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: confirm_reported_reading_fits}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: INPUT
    field: response_rules
    bound_to: inputs.response_rules
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: INPUT
    field: account_numbers
    bound_to: inputs.account_numbers
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: INPUT
    field: seed
    bound_to: inputs.seed
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: OUTPUT
    field: rules_in_force
    bound_to: capability_result.rules_in_force
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: OUTPUT
    field: positions
    bound_to: capability_result.positions
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: assemble_opening_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        user_prompt_id: $.inputs.user_prompt_id
        requester_id: $.inputs.requester_id
        customer_id: $.inputs.customer_id
        identity_key: $.inputs.identity_key
        kind: $.inputs.kind
        question: $.inputs.question
        supporting_material: $.inputs.supporting_material
        time_in_service_id: $.inputs.time_in_service_id
        reading: $.inputs.reading
        fingerprint: $.inputs.fingerprint
        reading_capacity: $.inputs.reading_capacity
        maximum_response_length: $.inputs.maximum_response_length
        rules_in_force: $.results.form_rules_in_force.rules_in_force
        ground_numbers: $.inputs.response_rules.ground_numbers
        longest_response: $.inputs.response_rules.longest_response
        outcome: WRITING
    source_finding: {phase: p7, register: cc_composition, key: assemble_opening_record}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: assemble_opening_record
    direction: OUTPUT
    field: opening_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_opening_record}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: INPUT
    field: record
    bound_to: results.assemble_opening_record.opening_record
    source_finding: {phase: p7, register: cc_composition, key: append_opening_record}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
    source_finding: {phase: p7, register: cc_composition, key: append_opening_record}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: INPUT
    field: actor_id
    bound_to: inputs.requester_id
    source_finding: {phase: p7, register: cc_composition, key: append_opening_record}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
    source_finding: {phase: p7, register: cc_composition, key: append_opening_record}
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
    source_finding: {phase: p7, register: cc_composition, key: append_opening_record}
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: read_trail
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
    source_finding: {phase: p7, register: cc_composition, key: read_trail}
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: read_trail
    direction: OUTPUT
    field: entries
    bound_to: capability_result.entries
    source_finding: {phase: p7, register: cc_composition, key: read_trail}
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: read_trail
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_trail}
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: reduce_trail
    direction: INPUT
    field: entries
    bound_to: results.read_trail.entries
    source_finding: {phase: p7, register: cc_composition, key: reduce_trail}
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: reduce_trail
    direction: OUTPUT
    field: state
    bound_to: capability_result.state
    source_finding: {phase: p7, register: cc_composition, key: reduce_trail}
  - owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    step: confirm_same_model
    direction: INPUT
    field: value
    bound_to: inputs.offered_fingerprint
    source_finding: {phase: p7, register: cc_composition, key: confirm_same_model}
  - owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    step: confirm_same_model
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - $.inputs.admitted_fingerprint
    source_finding: {phase: p7, register: cc_composition, key: confirm_same_model}
  - owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    step: confirm_same_model
    direction: OUTPUT
    field: offer_for_model
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: confirm_same_model}
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: INPUT
    field: state
    bound_to: inputs.state
    source_finding: {phase: p7, register: cc_composition, key: choose_token}
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: INPUT
    field: candidates
    bound_to: inputs.candidates
    source_finding: {phase: p7, register: cc_composition, key: choose_token}
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: step
    bound_to: capability_result.step
    source_finding: {phase: p7, register: cc_composition, key: choose_token}
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: text
    bound_to: capability_result.text
    source_finding: {phase: p7, register: cc_composition, key: choose_token}
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: finished
    bound_to: capability_result.finished
    source_finding: {phase: p7, register: cc_composition, key: choose_token}
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: stopped_by
    bound_to: capability_result.stopped_by
    source_finding: {phase: p7, register: cc_composition, key: choose_token}
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: within_length
    bound_to: capability_result.within_length
    source_finding: {phase: p7, register: cc_composition, key: choose_token}
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: assemble_step_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        user_prompt_id: $.inputs.user_prompt_id
        outcome: STEP
        host_id: $.inputs.host_id
        fingerprint: $.inputs.fingerprint
        reported_reading_size: $.inputs.reported_reading_size
        position: $.inputs.step.position
        candidates: $.inputs.step.candidates
        chosen: $.inputs.step.chosen
        stopped: $.inputs.step.stopped
        stopped_by: $.inputs.step.stopped_by
        finished: $.inputs.step.finished
        within_length: $.inputs.step.within_length
    source_finding: {phase: p7, register: cc_composition, key: assemble_step_record}
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: assemble_step_record
    direction: OUTPUT
    field: step_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_step_record}
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: INPUT
    field: record
    bound_to: results.assemble_step_record.step_record
    source_finding: {phase: p7, register: cc_composition, key: append_step_record}
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
    source_finding: {phase: p7, register: cc_composition, key: append_step_record}
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: INPUT
    field: actor_id
    bound_to: inputs.host_id
    source_finding: {phase: p7, register: cc_composition, key: append_step_record}
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
    source_finding: {phase: p7, register: cc_composition, key: append_step_record}
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
    source_finding: {phase: p7, register: cc_composition, key: append_step_record}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_USER_PROMPT_IDENTITY_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: permitted_customers
    bound_to: payload.permitted_customers
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_ADMIT_USER_PROMPT_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_WITHIN_CEILING_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_WITHIN_CEILING_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: system_prompt
    bound_to: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_READING_FITS_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_READING_FITS_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_READING_FITS_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_READING_FITS_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: account_numbers
    bound_to: payload.account_numbers
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: seed
    bound_to: payload.seed
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: response_rules
    bound_to: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: fingerprint
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.fingerprint
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: reading_capacity
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: maximum_response_length
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.maximum_response_length
    source_finding: {phase: p7, register: execution_topology, key: CC_OPEN_HOSTED_RECORD_V0}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: reason
    bound_to:
      literal: requester_not_permitted_for_customer
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: reason
    bound_to:
      literal: model_not_registered
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: reason
    bound_to:
      literal: model_not_in_service
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: reason
    bound_to:
      literal: kind_above_sensitivity_ceiling
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: reason
    bound_to:
      literal: reading_longer_than_model_can_read
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: causal_language_model::CC_READ_HOSTED_STATE_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: CC_READ_HOSTED_STATE_V0}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: INPUT
    field: offered_fingerprint
    bound_to: payload.fingerprint
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_OFFER_FOR_MODEL_V0}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: INPUT
    field: admitted_fingerprint
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.fingerprint
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_OFFER_FOR_MODEL_V0}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: INPUT
    field: reported_reading_size
    bound_to: payload.reported_reading_size
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_HOSTED_READING_FITS_V0}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading_capacity
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_HOSTED_READING_FITS_V0}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: state
    bound_to: results.CC_READ_HOSTED_STATE_V0.state
    source_finding: {phase: p7, register: execution_topology, key: CC_CHOOSE_PERMITTED_TOKEN_V0}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: candidates
    bound_to: payload.candidates
    source_finding: {phase: p7, register: execution_topology, key: CC_CHOOSE_PERMITTED_TOKEN_V0}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CONFIRM_NO_RULE_STOPPED
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        stopped_by: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_NO_RULE_STOPPED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CONFIRM_NO_RULE_STOPPED
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: stopped_by
        op: eq
        value: none
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_NO_RULE_STOPPED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CONFIRM_WITHIN_LENGTH
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        within_length: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.within_length
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_WITHIN_LENGTH}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CONFIRM_WITHIN_LENGTH
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: within_length
        op: eq
        value: true
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_WITHIN_LENGTH}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: reported_reading_size
    bound_to: payload.reported_reading_size
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: step
    bound_to: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STOPPED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STOPPED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STOPPED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: reported_reading_size
    bound_to: payload.reported_reading_size
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STOPPED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: step
    bound_to: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
    source_finding: {phase: p7, register: execution_topology, key: RECORD_STOPPED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_UNFINISHED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_UNFINISHED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
    source_finding: {phase: p7, register: execution_topology, key: RECORD_UNFINISHED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: reported_reading_size
    bound_to: payload.reported_reading_size
    source_finding: {phase: p7, register: execution_topology, key: RECORD_UNFINISHED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: step
    bound_to: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
    source_finding: {phase: p7, register: execution_topology, key: RECORD_UNFINISHED_STEP}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: reason
    bound_to:
      literal: offer_for_another_model
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_OTHER_MODEL}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: reason
    bound_to:
      literal: reading_longer_than_model_can_read
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: reason
    bound_to: results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: reason
    bound_to:
      literal: longest_response_reached
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: causal_language_model::CC_READ_HOSTED_STATE_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: CC_READ_HOSTED_STATE_V0}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: CONFIRM_FINISHED
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        finished: $.results.CC_READ_HOSTED_STATE_V0.state.finished
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_FINISHED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: CONFIRM_FINISHED
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: finished
        op: eq
        value: true
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_FINISHED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: outcome
    bound_to:
      literal: RESPONDED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: response
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.text
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  interface_fields:
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The request's identity, named by the requester and claimed once
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: requester_id
    type: string
    required: 'YES'
    default: ''
    meaning: The requester who submits the request
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: permitted_customers
    type: array
    required: 'YES'
    default: ''
    meaning: The customers the requester may act for, as the business's existing arrangements state
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: ''
    meaning: The customer the request is for
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: ''
    meaning: The customer's own account numbers, from the business's existing records
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key of the hosted model the request is for
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: ''
    meaning: The most sensitive kind of information the question and its material contain
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: ''
    meaning: What the requester asks on the customer's behalf
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: ''
    meaning: Material carried with the question for the model to read
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: ''
    meaning: The seed each adventurous choice is drawn from
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The request's identity, named by the requester and claimed once
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: ''
    meaning: The host offering, as it names itself; recorded, not authenticated
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The fingerprint of the model the offer is claimed to come from
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: reported_reading_size
    type: integer
    required: 'YES'
    default: ''
    meaning: How many tokens the host reports the model reads for this request
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: candidates
    type: array
    required: 'YES'
    default: ''
    meaning: The tokens the model could write next, each with its likelihood
  - artifact: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The request's identity, named by the requester and claimed once
  - artifact: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: ''
    meaning: The host offering, as it names itself; recorded, not authenticated
  - artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: INPUT
    field: reported_reading_size
    type: integer
    required: 'YES'
    default: ''
    meaning: How many tokens the host reports the model reads for this request
  - artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    type: integer
    required: 'YES'
    default: ''
    meaning: How many tokens the model can read in one request
  - artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: OUTPUT
    field: reading_fits
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the reported size is within the capacity
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The request's identity, named by the requester and claimed once
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: requester_id
    type: string
    required: 'YES'
    default: ''
    meaning: The requester who submits the request
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: ''
    meaning: The customer the request is for
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key of the hosted model the request is for
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: ''
    meaning: The most sensitive kind of information the question and its material contain
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: ''
    meaning: What the requester asks on the customer's behalf
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: ''
    meaning: Material carried with the question for the model to read
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: ''
    meaning: The model's open time in service
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: ''
    meaning: Exactly what the model reads
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: ''
    meaning: The time in service's forbidden words and patterns, account-number shape, freedom and longest response
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: ''
    meaning: The customer's own account numbers, from the business's existing records
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: ''
    meaning: The seed each adventurous choice is drawn from
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The fingerprint of the model the offer is claimed to come from
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: reading_capacity
    type: integer
    required: 'YES'
    default: ''
    meaning: How many tokens the model can read in one request
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: maximum_response_length
    type: integer
    required: 'YES'
    default: ''
    meaning: The most tokens a response of the model may have
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: ''
    meaning: The response rules in force for this request, with its seed
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: positions
    type: array
    required: 'YES'
    default: ''
    meaning: One position per token up to the rules' longest response
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: opening_record
    type: object
    required: 'YES'
    default: ''
    meaning: The opening entry of the request's trail, with what the model reads
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: ''
    meaning: The identity of the opening entry
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The opening entry's position in the user prompt records
  - artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The request's identity, named by the requester and claimed once
  - artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
    direction: OUTPUT
    field: entries
    type: array
    required: 'YES'
    default: ''
    meaning: The request's trail as recorded
  - artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
    direction: OUTPUT
    field: state
    type: object
    required: 'YES'
    default: ''
    meaning: The hosted request's response as built, its position, whether it is complete, and its permitted length
  - artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: INPUT
    field: offered_fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The fingerprint an offer names
  - artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: INPUT
    field: admitted_fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The fingerprint of the model the request was admitted for
  - artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: OUTPUT
    field: offer_for_model
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the offer names the admitted model's fingerprint
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: state
    type: object
    required: 'YES'
    default: ''
    meaning: The hosted request's response as built, its position, whether it is complete, and its permitted length
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: candidates
    type: array
    required: 'YES'
    default: ''
    meaning: The tokens the model could write next, each with its likelihood
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: step
    type: object
    required: 'YES'
    default: ''
    meaning: One offer and the choice made from it
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: text
    type: string
    required: 'YES'
    default: ''
    meaning: The response with the chosen token
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: finished
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the chosen token ends the response
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: ''
    meaning: The rule that left no permitted token, or none
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: within_length
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the response is still within its permitted length
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The request's identity, named by the requester and claimed once
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: ''
    meaning: The host offering, as it names itself; recorded, not authenticated
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The fingerprint of the model the offer is claimed to come from
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: reported_reading_size
    type: integer
    required: 'YES'
    default: ''
    meaning: How many tokens the host reports the model reads for this request
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: step
    type: object
    required: 'YES'
    default: ''
    meaning: One offer and the choice made from it
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: OUTPUT
    field: step_record
    type: object
    required: 'YES'
    default: ''
    meaning: The step entry appended to the request's trail
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: ''
    meaning: The identity of the step entry
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The step entry's position in the user prompt records
  - artifact: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    direction: INPUT
    field: entries
    type: array
    required: 'YES'
    default: ''
    meaning: The request's trail as recorded
  - artifact: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    direction: OUTPUT
    field: state
    type: object
    required: 'YES'
    default: ''
    meaning: The hosted request's response as built, its position, whether it is complete, and its permitted length
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: state
    type: object
    required: 'YES'
    default: ''
    meaning: The hosted request's response as built, its position, whether it is complete, and its permitted length
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: candidates
    type: array
    required: 'YES'
    default: ''
    meaning: The tokens the model could write next, each with its likelihood
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: step
    type: object
    required: 'YES'
    default: ''
    meaning: One offer and the choice made from it
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: text
    type: string
    required: 'YES'
    default: ''
    meaning: The response with the chosen token
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: finished
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the chosen token ends the response
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: ''
    meaning: The rule that left no permitted token, or none
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: within_length
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the response is still within its permitted length
  - artifact: causal_language_model::AC_MODEL_HOST_V0
    direction: ATTRIBUTE
    field: host_id
    type: string
    required: 'YES'
    default: ''
    meaning: The host's name for itself; recorded against every offer, not authenticated
  implementation_bindings:
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    callable: execute
    operation: READ_HOSTED_STATE
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_READ_HOSTED_STATE_V0}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    callable: execute
    operation: CHOOSE_PERMITTED_TOKEN
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_CHOOSE_PERMITTED_TOKEN_V0}
  vocabulary_extensions: []
  runtime_policies: []
  artifact_properties:
  - artifact: causal_language_model::AC_MODEL_HOST_V0
    property: type
    value: ENDUSER
    source_finding: {phase: p5, register: provisional_codes, key: AC_MODEL_HOST_V0}
  - artifact: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    property: emit.EXIT_REFUSED
    value:
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
    source_finding: {phase: p1, register: business_events, row: 2}
  - artifact: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    property: emit.EXIT_REFUSED
    value:
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
    source_finding: {phase: p1, register: business_events, row: 2}
  - artifact: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    property: emit.EXIT_RESPONDED
    value:
    - causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    source_finding: {phase: p1, register: business_events, row: 1}
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    property: moment
    value: refusal
    source_finding: {phase: p1, register: business_events, row: 2}
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: model_response
    count: '15'
    artifacts: 1 AC, 3 IN, 3 WF, 6 CC, 2 CT
  generation_provenance: []
  declared_reach: []
  refusal_discharge:
  - operation: Offer candidates
    refused_when: The reported reading size exceeds the model's reading capacity.
    act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Offer candidates
    refused_when: The offer names a fingerprint other than the model's the request was admitted for.
    act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Offer candidates
    refused_when: The request is not being written.
    act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: causal_language_model::CC_READ_HOSTED_STATE_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Offer candidates
    refused_when: Every candidate is forbidden.
    act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Offer candidates
    refused_when: The response reaches its permitted length before it is complete.
    act: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: Release a response
    refused_when: The response is not complete.
    act: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: CONFIRM_FINISHED
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  refusal_deferrals: []
  refusal_governance_discharge: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: reduces_the_trail_to_the_response_as_built
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: refuses_a_request_never_admitted
    expected_outcome: VIOLATION
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: refuses_a_closed_request
    expected_outcome: VIOLATION
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: refuses_an_offer_for_a_complete_response
    expected_outcome: VIOLATION
    source_finding: {source: human}
  test_case_values:
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: reduces_the_trail_to_the_response_as_built
    role: INPUT
    field: entries
    value:
    - sequence_number: 1
      record:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
    - sequence_number: 2
      record:
        outcome: STEP
        chosen: Your
    - sequence_number: 3
      record:
        outcome: STEP
        chosen: ' balance'
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: reduces_the_trail_to_the_response_as_built
    role: EXPECTED
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Your balance
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: refuses_a_request_never_admitted
    role: INPUT
    field: entries
    value:
    - sequence_number: 1
      record:
        outcome: REFUSED
        reason: model_not_registered
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: refuses_a_closed_request
    role: INPUT
    field: entries
    value:
    - sequence_number: 1
      record:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
    - sequence_number: 2
      record:
        outcome: RESPONDED
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 1
      text: Account 8765
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: INPUT
    field: candidates
    value:
    - token: '4321'
      likelihood: 0.7
    - token: ' is'
      likelihood: 0.2
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: text
    value: Account 8765 is
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: step
    value:
      position: 2
      candidates:
      - token: '4321'
        likelihood: 0.7
      - token: ' is'
        likelihood: 0.2
      chosen: ' is'
      stopped:
      - token: '4321'
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 1
      text: Account 1234
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: INPUT
    field: candidates
    value:
    - token: '5678'
      likelihood: 0.8
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: text
    value: Account 12345678
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: step
    value:
      position: 2
      candidates:
      - token: '5678'
        likelihood: 0.8
      chosen: '5678'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 0
      text: ''
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: INPUT
    field: candidates
    value:
    - token: '87654321'
      likelihood: 0.9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: text
    value: ''
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: stopped_by
    value: another_customers_account_number
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: step
    value:
      position: 1
      candidates:
      - token: '87654321'
        likelihood: 0.9
      chosen: null
      stopped:
      - token: '87654321'
        rule: another_customers_account_number
      stopped_by: another_customers_account_number
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 3
      text: Your balance is
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: INPUT
    field: candidates
    value:
    - token: ' today'
      likelihood: 0.9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: text
    value: Your balance is today
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: within_length
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: step
    value:
      position: 4
      candidates:
      - token: ' today'
        likelihood: 0.9
      chosen: ' today'
      stopped: []
      stopped_by: none
      finished: false
      within_length: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Your balance
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: candidates
    value:
    - token: <end>
      likelihood: 0.9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: text
    value: Your balance
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: finished
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: <end>
        likelihood: 0.9
      chosen: <end>
      stopped: []
      stopped_by: none
      finished: true
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Spouse account 8765432
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: INPUT
    field: candidates
    value:
    - token: ₁
      likelihood: 0.8
    - token: .
      likelihood: 0.1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: text
    value: Spouse account 8765432.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: ₁
        likelihood: 0.8
      - token: .
        likelihood: 0.1
      chosen: .
      stopped:
      - token: ₁
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Spouse account '
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: INPUT
    field: candidates
    value:
    - token: '8'
      likelihood: 0.8
    - token: withheld
      likelihood: 0.1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: text
    value: Spouse account withheld
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: '8'
        likelihood: 0.8
      - token: withheld
        likelihood: 0.1
      chosen: withheld
      stopped:
      - token: '8'
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Balance '
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: INPUT
    field: candidates
    value:
    - token: '4'
      likelihood: 0.8
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: text
    value: Balance 4
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: '4'
        likelihood: 0.8
      chosen: '4'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: true
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Balance 4
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: INPUT
    field: candidates
    value:
    - token: '9'
      likelihood: 0.8
    - token: '0'
      likelihood: 0.1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: text
    value: Balance 40
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: '9'
        likelihood: 0.8
      - token: '0'
        likelihood: 0.1
      chosen: '0'
      stopped:
      - token: '9'
        rule: numbers_from_the_reading
      stopped_by: none
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: true
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Balance 4
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: INPUT
    field: candidates
    value:
    - token: ' dollars'
      likelihood: 0.8
    - token: <end>
      likelihood: 0.1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: text
    value: Balance 4
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: stopped_by
    value: numbers_from_the_reading
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: ' dollars'
        likelihood: 0.8
      - token: <end>
        likelihood: 0.1
      chosen: null
      stopped:
      - token: ' dollars'
        rule: numbers_from_the_reading
      - token: <end>
        rule: numbers_from_the_reading
      stopped_by: numbers_from_the_reading
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Balance '
      finished: false
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: INPUT
    field: candidates
    value:
    - token: '9'
      likelihood: 0.8
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: text
    value: Balance 9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: '9'
        likelihood: 0.8
      chosen: '9'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: within_length
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: refuses_an_offer_for_a_complete_response
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Your balance
      finished: true
      limit: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: refuses_an_offer_for_a_complete_response
    role: INPUT
    field: candidates
    value:
    - token: ' more'
      likelihood: 0.9
    source_finding: {source: human}
  withdrawn_facts: []
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
