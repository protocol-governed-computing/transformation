# Stage 7 — Design Intent: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p7
  domain: causal_language_model
  subdomain: model_response
  cr: cr_01_model_response
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: model_response is a new subdomain
    business_fact: Nothing in the composition registers a model or governs how one writes
    resolution: A new subdomain of the causal_language_model namespace with its own two actors, five stores, one binding and five operations
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: Writing is a molecule of two declared steps per pass
    business_fact: The rules must act while the model writes, visibly to governance
    resolution: One pass is a molecule of the model's offer and the rules' choice; the response is a molecule whose loop runs one pass per position up to the longest response
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: Determinism ends at the model's step
    business_fact: A reader must see exactly where determinism ends
    resolution: Only the offer is declared ct_impure; the choice emits each pass's result, so nothing is decided on the model's offer
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: A trace is reproduced from its record
    business_fact: A user prompt's trace must be reproducible from what was recorded
    resolution: The platform records each offer where it is produced; the writing molecule's vectors state recorded offers and are proven by substituting them
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: The seed is a recorded input
    business_fact: Anyone reading the record can re-derive each chosen word
    resolution: The user prompt states a seed; it enters the rules in force, which the user prompt record keeps whole
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: The test model is a realization of the model's step
    business_fact: The rules must be shown to hold against a model that tries to break them
    resolution: The offer's implementation is the test model, which offers another customer's account number first
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - decision: The customer's account numbers travel with the user prompt
    business_fact: The rule against another customer's account number is formed per user prompt
    resolution: The rules in force add one forbidden pattern, the account-number shape, excepting the customer's own numbers; every rule is read against the response so far joined to the candidate, so a number written across several words is stopped at the word that completes it
    source_finding: {phase: p4, register: design_decisions, row: 7}
  - decision: Uniqueness by a formed key
    business_fact: Two registrations with the same description and fingerprint are the same model
    resolution: A pure transform forms one key from the description and fingerprint; the registry claims it atomically, and ALREADY_EXISTS is the duplicate refusal
    source_finding: {phase: p4, register: design_decisions, row: 8}
  - decision: State is data on the record
    business_fact: A model moves into and out of service repeatedly
    resolution: The model record carries its state and its open time in service. Placement and withdrawal change the model's state only from the state they expect, in one conditional update, and refuse when it matched nothing; the time in service record is written after, so a failure between the two leaves a model no user prompt can reach rather than one answering under no rules
    source_finding: {phase: p4, register: design_decisions, row: 9}
  - decision: Membership before order
    business_fact: Membership is mechanism; the comparison is this subdomain's rule
    resolution: The stated kind is confirmed a declared kind, then compared with the ceiling by the declared order
    source_finding: {phase: p4, register: design_decisions, row: 10}
  - decision: Retrieval raises no event
    business_fact: Nothing reacts to a read
    resolution: Retrieval appends to the operation trail and declares no business moment
    source_finding: {phase: p4, register: design_decisions, row: 11}
  - decision: Authorization is read, never granted
    business_fact: Which staff are model staff and who may act for which customer is decided elsewhere
    resolution: The business's existing arrangements are the trusted source of who is model staff and whom a requester may act for; they assert both through the ingress, as the staff member's credentials and the requester's permitted customers, and model_response trusts that assertion and authenticates neither. The rules the credentials are checked against, and the schema a description is checked against, are fixed by this design and never supplied by the caller
    source_finding: {phase: p4, register: design_decisions, row: 12}
  - decision: Every refusal is recorded with its reason
    business_fact: Every user prompt is recorded, whether responded to or refused
    resolution: 'Each refusal routes to its own place in the submission, where the recording contract runs with that refusal''s reason; a failure to write the response, or a store failing before the model reads, is recorded as FAILED with the stage. Not recorded: a payload the intent refuses, a second submission under a claimed identity, and a failure of the user prompt records themselves, which ends the act rejected and reports no record. A submission is traced by its user prompt record, which names the requester'
    source_finding: {phase: p4, register: constraint_register, row: 9}
  - decision: One identity, one record
    business_fact: Each model the business holds has exactly one record
    resolution: A time in service and a user prompt are each claimed in their own register before anything is written under them; a duplicate is refused rather than overwriting or appending a second record
    source_finding: {phase: p4, register: design_decisions, row: 8}
  - decision: The governed unit is a word
    business_fact: A language model writes a response one word at a time
    resolution: 'Choosing, stopping and reading capacity are counted in words, which is exact for the test model and a simulation for a real one: a real model''s tokens join this design only through a realization that offers whole words. A rule governs what its pattern can express and nothing else; the business does not claim a response is true'
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - decision: How the seed draws an adventurous word
    business_fact: Anyone reading the record can re-derive each chosen word
    resolution: The permitted candidates, most likely first and ties in offered order, are narrowed to the first freedom-plus-one; the word at position (seed plus the word's position) modulo that count is chosen. Freedom zero always chooses the most likely permitted word
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: A finished response invokes no model
    business_fact: An unfinished response is not a response
    resolution: The loop runs one pass per position to the longest response, as molecules run; once the response has finished or a rule has stopped it, the offer is handed that fact and returns no words without consulting the model, and the choice changes nothing
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: The kinds of information are copied into three bindings
    business_fact: The kinds are declared once, in order, least sensitive first
    resolution: A binding cannot read a vocabulary, so the ordered kinds are written as a literal where membership and order are checked, each copy identical to the vocabulary's entries in the same order
    source_finding: {phase: p4, register: design_decisions, row: 10}
  existing_inventory:
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REUSE
    summary: ''
    reason: Holds the model record and the time in service record, read and updated in place.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    action: REUSE
    summary: ''
    reason: Register-if-absent gives the atomic claim duplicate prevention needs, on a key the subdomain forms.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: ''
    reason: Appends the user prompt record and the operation trail, neither of which can be amended.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_APPENDONLY_JSONL_V0'}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: ''
    reason: Assembles the model, time in service and user prompt records from supplied values.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    action: REUSE
    summary: ''
    reason: Reports what a model description lacks of the fields registration requires; a following rule refuses it when anything is reported.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    action: REUSE
    summary: ''
    reason: Confirms model staff credentials, a model's state and a response's release conditions against declared rules, and interprets each into a decision.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    action: REUSE
    summary: ''
    reason: Confirms a stated kind of information is a declared kind, and that a requester may act for the customer.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0'}
  - fqdn: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    action: REUSE
    summary: ''
    reason: Selects the one user prompt record retrieved, and interprets a record not found into a refusal.
    source_finding: {phase: p6, register: ownership, key: Append an entry to a trail that cannot be amended}
  - fqdn: capability_transforms::CONSTITUTION_MOLECULES_V0
    action: REUSE
    summary: ''
    reason: Governs the two writing molecules and runs the loop's body once per pass.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CONSTITUTION_MOLECULES_V0'}
  - fqdn: capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0
    action: REUSE
    summary: ''
    reason: 'Governs the model''s offer: recorded when produced, replayed from the record, offered to a deterministic step.'
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0'}
  new_artifacts:
  - capability: The authorized model staff member who registers, places, withdraws and retrieves
    family: AC
    code: causal_language_model::AC_MODEL_STAFF_V0
    summary: The actor whose authorization every model staff operation binds
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: AC_MODEL_STAFF_V0}
  - capability: The authorized requester who submits a user prompt on behalf of a customer
    family: AC
    code: causal_language_model::AC_REQUESTER_V0
    summary: The actor who submits a user prompt for one customer
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: AC_REQUESTER_V0}
  - capability: A request to register a model with its description and fingerprint
    family: IN
    code: causal_language_model::IN_REGISTER_MODEL_V0
    summary: A request to register a model with its description and fingerprint
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_REGISTER_MODEL_V0}
  - capability: A request to place a registered model in service with its ceiling, system prompt and response rules
    family: IN
    code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    summary: A request to place a registered model in service with its ceiling, system prompt and response rules
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_PLACE_MODEL_IN_SERVICE_V0}
  - capability: A request to withdraw a model from service
    family: IN
    code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    summary: A request to withdraw a model from service
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_WITHDRAW_MODEL_FROM_SERVICE_V0}
  - capability: A user prompt submitted on behalf of a customer
    family: IN
    code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    summary: A user prompt submitted on behalf of a customer
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_SUBMIT_USER_PROMPT_V0}
  - capability: A request to retrieve the record of a user prompt
    family: IN
    code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    summary: A request to retrieve the record of a user prompt
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_RETRIEVE_USER_PROMPT_RECORD_V0}
  - capability: Registering a model, refusing a second registration of the same model
    family: WF
    code: causal_language_model::WF_REGISTER_MODEL_V0
    summary: Registering a model, refusing a second registration of the same model
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_REGISTER_MODEL_V0}
  - capability: Opening a time in service for a registered model not already in service
    family: WF
    code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    summary: Opening a time in service for a registered model not already in service
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_PLACE_MODEL_IN_SERVICE_V0}
  - capability: Closing a model's time in service
    family: WF
    code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    summary: Closing a model's time in service
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_WITHDRAW_MODEL_FROM_SERVICE_V0}
  - capability: Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it
    family: WF
    code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    summary: Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_SUBMIT_USER_PROMPT_V0}
  - capability: Reading a user prompt record and recording that it was read
    family: WF
    code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    summary: Reading a user prompt record and recording that it was read
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_RETRIEVE_USER_PROMPT_RECORD_V0}
  - capability: Confirm the staff member is model staff
    family: CC
    code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    summary: Confirm the staff member is model staff
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - capability: Claim a user prompt's identity so a second submission under it is refused
    family: CC
    code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    summary: Claim a user prompt's identity so a second submission under it is refused
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CLAIM_USER_PROMPT_IDENTITY_V0}
  - capability: Confirm the requester may act for the customer the user prompt is for
    family: CC
    code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    summary: Confirm the requester may act for the customer the user prompt is for
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0}
  - capability: Claim a model's identity so a second registration of the same model is refused
    family: CC
    code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    summary: Claim a model's identity so a second registration of the same model is refused
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CLAIM_MODEL_IDENTITY_V0}
  - capability: Record a model's description and fingerprint as its record, registered
    family: CC
    code: causal_language_model::CC_REGISTER_MODEL_V0
    summary: Record a model's description and fingerprint as its record, registered
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_REGISTER_MODEL_V0}
  - capability: Open a time in service with its ceiling, system prompt and response rules, and mark the model in service
    family: CC
    code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    summary: Open a time in service with its ceiling, system prompt and response rules, and mark the model in service
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_PLACE_MODEL_IN_SERVICE_V0}
  - capability: Close the time in service and mark the model registered
    family: CC
    code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    summary: Close the time in service and mark the model registered
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_WITHDRAW_MODEL_FROM_SERVICE_V0}
  - capability: Refuse a user prompt whose model is not registered or not in service
    family: CC
    code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    summary: Refuse a user prompt before the model sees it when its model is not registered or not in service
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_ADMIT_USER_PROMPT_V0}
  - capability: Refuse a user prompt whose kind of information is above the model's ceiling
    family: CC
    code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    summary: Refuse a user prompt before the model sees it when it states a kind more sensitive than the ceiling
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_ADMIT_USER_PROMPT_V0}
  - capability: Refuse a user prompt longer than the model can read at once
    family: CC
    code: causal_language_model::CC_CONFIRM_READING_FITS_V0
    summary: Assemble exactly what the model reads and refuse it before the model sees it when it is too long
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_ADMIT_USER_PROMPT_V0}
  - capability: Write the response word by word under the rules in force
    family: CC
    code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    summary: Form the rules in force and write the response word by word under them
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_WRITE_MODEL_RESPONSE_V0}
  - capability: Release a written response only when it finished and no rule stopped it
    family: CC
    code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    summary: Confirm one release condition of a written response, refusing it otherwise
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_WRITE_MODEL_RESPONSE_V0}
  - capability: Append the user prompt record with what the model read, the rules in force and the outcome
    family: CC
    code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    summary: Append the user prompt record with what the model read, the rules in force and the outcome
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_RECORD_USER_PROMPT_V0}
  - capability: Read the record of a user prompt
    family: CC
    code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    summary: Read the record of a user prompt
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_RETRIEVE_USER_PROMPT_RECORD_V0}
  - capability: Append a durable account of a performed operation to the subdomain's own trail
    family: CC
    code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    summary: Append a durable account of a performed operation to the subdomain's own trail
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_APPEND_MODEL_OPERATION_V0}
  - capability: Form the single key claimed for a model from its description and fingerprint
    family: CT
    code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    summary: Forms the single key claimed for a model from its description and fingerprint
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_FORM_MODEL_IDENTITY_KEY_V0}
  - capability: Decide whether a kind of information is no more sensitive than a ceiling
    family: CT
    code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    summary: Decides whether a kind of information is no more sensitive than a ceiling, by the declared order
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_COMPARE_SENSITIVITY_V0}
  - capability: Assemble exactly what the model reads and decide whether it fits
    family: CT
    code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    summary: Assembles exactly what the model reads and decides whether it fits what the model can read at once
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_ASSEMBLE_MODEL_READING_V0}
  - capability: Form the response rules in force for one user prompt
    family: CT
    code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    summary: Forms the response rules in force for one user prompt from the time in service and the customer's account numbers
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_FORM_RESPONSE_RULES_V0}
  - capability: The model's offer of its next words
    family: CT
    code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    summary: 'The model''s step: offers its next words given the response so far; the one step whose result is not determined by its inputs'
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_IMPURE_OFFER_NEXT_WORDS_V0}
  - capability: Stop forbidden words and choose one permitted word
    family: CT
    code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    summary: Stops forbidden words among those offered and chooses one permitted word under the freedom of word choice and a stated seed
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_CHOOSE_PERMITTED_WORD_V0}
  - capability: 'One pass of writing: the model''s offer, then the rules'' choice'
    family: CT
    code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    summary: One pass of writing, composed of the model's offer and the rules' choice
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_WRITE_NEXT_WORD_V0}
  - capability: Write a response one pass per word, up to the longest response
    family: CT
    code: causal_language_model::CT_WRITE_RESPONSE_V0
    summary: Writes a response by repeating one pass per word, up to the longest response, carrying the response so far and the words stopped
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_WRITE_RESPONSE_V0}
  - capability: The moment the business records a model
    family: EV
    code: causal_language_model::EV_MODEL_REGISTERED_V0
    summary: The moment the business records a model
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_MODEL_REGISTERED_V0}
  - capability: The moment a model is placed in service and a time in service begins
    family: EV
    code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    summary: The moment a model is placed in service and a time in service begins
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_MODEL_SERVICE_STARTED_V0}
  - capability: The moment a model is withdrawn from service and its time in service ends
    family: EV
    code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    summary: The moment a model is withdrawn from service and its time in service ends
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_MODEL_SERVICE_ENDED_V0}
  - capability: The moment a model response is released
    family: EV
    code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    summary: The moment a model response is released
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_USER_PROMPT_RESPONDED_V0}
  - capability: The moment a user prompt yields no response
    family: EV
    code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    summary: The moment a user prompt yields no response
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_USER_PROMPT_REFUSED_V0}
  - capability: The kinds of information, least sensitive first
    family: VOCAB
    code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    summary: 'The kinds of information, least sensitive first: public, internal, confidential, restricted'
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: VOCAB_KIND_OF_INFORMATION_V0}
  - capability: Bind the subdomain's operations to the stores and mechanisms they use
    family: RB
    code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    summary: Binds every model response workflow to the mechanisms and stores it uses
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: RB_MODEL_RESPONSE_BINDINGS_V0}
  - capability: Declare the stores the subdomain owns
    family: STRUCTURE
    code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    summary: Declares the seven stores the subdomain owns and the paths they occupy
    owner_subdomain: model_response
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: STRUCTURE_MODEL_RESPONSE_STORAGE_V0}
  rb_declarations:
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_REGISTER_MODEL_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every model the business holds}
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every model the business holds}
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every model the business holds}
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every model the business holds}
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every model the business holds}
  execution_topology:
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: causal_language_model::IN_REGISTER_MODEL_V0
    runs: ''
    node_type: IN
    routing:
      ACK: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_REGISTER_MODEL_V0}
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_REGISTER_MODEL_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_MODEL_IDENTITY_V0}
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: causal_language_model::CC_REGISTER_MODEL_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_REGISTER_MODEL_V0}
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_REGISTERED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_MODEL_OPERATION_V0}
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: EXIT_REGISTERED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_MODEL_V0}
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_MODEL_V0}
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    runs: ''
    node_type: IN
    routing:
      ACK: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_PLACE_MODEL_IN_SERVICE_V0}
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_PLACE_MODEL_IN_SERVICE_V0}
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_PLACED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_MODEL_OPERATION_V0}
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: EXIT_PLACED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_PLACE_MODEL_IN_SERVICE_V0}
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_PLACE_MODEL_IN_SERVICE_V0}
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    runs: ''
    node_type: IN
    routing:
      ACK: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_WITHDRAW_MODEL_FROM_SERVICE_V0}
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_WITHDRAW_MODEL_FROM_SERVICE_V0}
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_WITHDRAWN
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_MODEL_OPERATION_V0}
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: EXIT_WITHDRAWN
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_WITHDRAW_MODEL_FROM_SERVICE_V0}
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_WITHDRAW_MODEL_FROM_SERVICE_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    runs: ''
    node_type: IN
    routing:
      ACK: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_SUBMIT_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_USER_PROMPT_IDENTITY_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      VIOLATION: RECORD_REFUSED_NOT_PERMITTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      NOT_FOUND: RECORD_REFUSED_NOT_REGISTERED
      VIOLATION: RECORD_REFUSED_NOT_IN_SERVICE
      BACKEND_ERROR: RECORD_FAILED_BEFORE_READING
    source_finding: {phase: p7, register: new_artifacts, key: CC_ADMIT_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_CONFIRM_READING_FITS_V0
      NOT_FOUND: RECORD_REFUSED_NOT_IN_SERVICE
      VIOLATION: RECORD_REFUSED_ABOVE_CEILING
      BACKEND_ERROR: RECORD_FAILED_BEFORE_READING
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_WITHIN_CEILING_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: causal_language_model::CC_CONFIRM_READING_FITS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_READING_FITS_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: CONFIRM_NO_RULE_STOPPED
      VIOLATION: RECORD_FAILED_WHILE_WRITING
    source_finding: {phase: p7, register: new_artifacts, key: CC_WRITE_MODEL_RESPONSE_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CONFIRM_NO_RULE_STOPPED
    runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    node_type: CC
    routing:
      SUCCESS: CONFIRM_FINISHED
      VIOLATION: RECORD_REFUSED_BY_RULE
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_RESPONSE_RELEASABLE_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CONFIRM_FINISHED
    runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_RESPONDED
      VIOLATION: RECORD_REFUSED_UNFINISHED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_RESPONSE_RELEASABLE_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_RESPONDED
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_RESPONDED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_NOT_PERMITTED
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_NOT_REGISTERED
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_NOT_IN_SERVICE
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_ABOVE_CEILING
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_TOO_LONG_TO_READ
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_BY_RULE
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_UNFINISHED
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_FAILED_BEFORE_READING
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_FAILED_WHILE_WRITING
    runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: EXIT_RESPONDED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_SUBMIT_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: EXIT_REFUSED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_SUBMIT_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_SUBMIT_USER_PROMPT_V0}
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    runs: ''
    node_type: IN
    routing:
      ACK: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_RETRIEVE_USER_PROMPT_RECORD_V0}
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_MODEL_OPERATION_V0}
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_RETRIEVED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RETRIEVE_USER_PROMPT_RECORD_V0}
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: EXIT_RETRIEVED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RETRIEVE_USER_PROMPT_RECORD_V0}
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RETRIEVE_USER_PROMPT_RECORD_V0}
  cc_composition:
  - cc_code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    step: '1'
    step_name: confirm_authorization
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - staff_credentials
    - authorization_rules
    produces:
    - is_authorized
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: staff_credentials
        rules: authorization_rules
      out:
        valid: is_authorized
  - cc_code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    step: '1'
    step_name: confirm_acts_for_customer
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - customer_id
    - permitted_customers
    produces:
    - acts_for_customer
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: customer_id
        allowed_set: permitted_customers
      out:
        is_member: acts_for_customer
  - cc_code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: '1'
    step_name: validate_description
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - description
    - description_schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: description
        schema: description_schema
      out:
        violations: violations
  - cc_code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: '2'
    step_name: require_description_complete
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - violations
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: description_findings
        rules: completeness_rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: '3'
    step_name: form_identity_key
    capability: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    kind: CT
    operation: FORM_MODEL_IDENTITY_KEY
    store: null
    consumes:
    - description
    - fingerprint
    produces:
    - identity_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        description: description
        fingerprint: fingerprint
      out:
        identity_key: identity_key
  - cc_code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: '4'
    step_name: claim_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: MODEL_IDENTITY_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: ALREADY_EXISTS
    interface: null
  - cc_code: causal_language_model::CC_REGISTER_MODEL_V0
    step: '1'
    step_name: assemble_model_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - identity_key
    - description
    - fingerprint
    produces:
    - model_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: model_fields
      out:
        record: model_record
  - cc_code: causal_language_model::CC_REGISTER_MODEL_V0
    step: '2'
    step_name: write_model_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: MODELS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '1'
    step_name: read_model_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: MODELS
    consumes:
    - key
    produces:
    - model_record
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '2'
    step_name: require_registered
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - model_record
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: model_state
        rules: state_rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '3'
    step_name: confirm_ceiling_declared
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - ceiling
    produces:
    - ceiling_declared
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: ceiling
        allowed_set: kinds
      out:
        is_member: ceiling_declared
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '4'
    step_name: claim_time_in_service
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: TIME_IN_SERVICE_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    routing:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: ALREADY_EXISTS
    interface: null
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '5'
    step_name: mark_in_service
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: MODELS
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '6'
    step_name: require_transition
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - updated_count
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: transition
        rules: transition_rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '7'
    step_name: assemble_time_in_service
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - time_in_service_id
    - identity_key
    - ceiling
    - system_prompt
    - response_rules
    produces:
    - time_in_service
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: time_in_service_fields
      out:
        record: time_in_service
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '8'
    step_name: write_time_in_service
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: TIMES_IN_SERVICE
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '1'
    step_name: read_model_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: MODELS
    consumes:
    - key
    produces:
    - model_record
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '2'
    step_name: require_in_service
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - model_record
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: model_state
        rules: state_rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '3'
    step_name: mark_registered
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: MODELS
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '4'
    step_name: require_transition
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - updated_count
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: transition
        rules: transition_rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '5'
    step_name: close_time_in_service
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE
    store: TIMES_IN_SERVICE
    consumes:
    - key
    - updates
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: '1'
    step_name: claim_user_prompt
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: USER_PROMPT_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: ALREADY_EXISTS
    interface: null
  - cc_code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: '1'
    step_name: read_model_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: MODELS
    consumes:
    - key
    produces:
    - model_record
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: '2'
    step_name: require_in_service
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - model_record
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: model_state
        rules: state_rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: '1'
    step_name: read_time_in_service
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: TIMES_IN_SERVICE
    consumes:
    - key
    produces:
    - time_in_service
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: '2'
    step_name: confirm_kind_declared
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - kind
    produces:
    - kind_declared
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: kind
        allowed_set: kinds
      out:
        is_member: kind_declared
  - cc_code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: '3'
    step_name: compare_sensitivity
    capability: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    kind: CT
    operation: COMPARE_SENSITIVITY
    store: null
    consumes:
    - kind
    - time_in_service
    produces:
    - within_ceiling
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        kind: kind
        ceiling: ceiling
        kinds: kinds
      out:
        within_ceiling: within_ceiling
  - cc_code: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: '1'
    step_name: assemble_reading
    capability: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    kind: CT
    operation: ASSEMBLE_MODEL_READING
    store: null
    consumes:
    - system_prompt
    - question
    - supporting_material
    - reading_capacity
    produces:
    - reading
    - reading_length
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        system_prompt: system_prompt
        question: question
        supporting_material: supporting_material
        reading_capacity: reading_capacity
      out:
        reading: reading
        reading_length: reading_length
  - cc_code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
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
  - cc_code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: '2'
    step_name: write_response
    capability: causal_language_model::CT_WRITE_RESPONSE_V0
    kind: CT
    operation: WRITE_RESPONSE
    store: null
    consumes:
    - reading
    - rules_in_force
    - positions
    produces:
    - written_response
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        reading: reading
        rules_in_force: rules_in_force
        positions: positions
      out:
        result: written_response
  - cc_code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    step: '1'
    step_name: confirm_releasable
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - release_facts
    - release_rules
    produces:
    - releasable
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: release_facts
        rules: release_rules
      out:
        valid: releasable
  - cc_code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: '1'
    step_name: assemble_user_prompt_record
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
    - outcome
    - time_in_service_id
    - reading
    - rules_in_force
    - response
    - reason
    produces:
    - user_prompt_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: user_prompt_fields
      out:
        record: user_prompt_record
  - cc_code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: '2'
    step_name: append_user_prompt_record
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
  - cc_code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: '1'
    step_name: read_user_prompt_entries
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
  - cc_code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: '2'
    step_name: select_user_prompt_record
    capability: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    kind: CT
    operation: FILTER_RECORDS
    store: null
    consumes:
    - entries
    - record_criteria
    produces:
    - user_prompt_record
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: entries
        filter: record_criteria
      out:
        extracted: user_prompt_record
  - cc_code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: '1'
    step_name: append_operation
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: MODEL_OPERATIONS
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
  - owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: INPUT
    field: parameters
    bound_to: inputs.staff_credentials
    source_finding: {phase: p7, register: cc_composition, key: confirm_authorization}
  - owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: INPUT
    field: rules
    bound_to: inputs.authorization_rules
    source_finding: {phase: p7, register: cc_composition, key: confirm_authorization}
  - owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: OUTPUT
    field: is_authorized
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: confirm_authorization}
  - owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    step: confirm_acts_for_customer
    direction: INPUT
    field: value
    bound_to: inputs.customer_id
    source_finding: {phase: p7, register: cc_composition, key: confirm_acts_for_customer}
  - owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    step: confirm_acts_for_customer
    direction: INPUT
    field: allowed_set
    bound_to: inputs.permitted_customers
    source_finding: {phase: p7, register: cc_composition, key: confirm_acts_for_customer}
  - owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    step: confirm_acts_for_customer
    direction: OUTPUT
    field: acts_for_customer
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: confirm_acts_for_customer}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: validate_description
    direction: INPUT
    field: record
    bound_to: inputs.description
    source_finding: {phase: p7, register: cc_composition, key: validate_description}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: validate_description
    direction: INPUT
    field: schema
    bound_to: inputs.description_schema
    source_finding: {phase: p7, register: cc_composition, key: validate_description}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: validate_description
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_description}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: require_description_complete
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.validate_description.violations
    source_finding: {phase: p7, register: cc_composition, key: require_description_complete}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: require_description_complete
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
    source_finding: {phase: p7, register: cc_composition, key: require_description_complete}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: require_description_complete
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_description_complete}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: description
    bound_to: inputs.description
    source_finding: {phase: p7, register: cc_composition, key: form_identity_key}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: fingerprint
    bound_to: inputs.fingerprint
    source_finding: {phase: p7, register: cc_composition, key: form_identity_key}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: form_identity_key
    direction: OUTPUT
    field: identity_key
    bound_to: capability_result.identity_key
    source_finding: {phase: p7, register: cc_composition, key: form_identity_key}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: key
    bound_to: results.form_identity_key.identity_key
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: target_ref
    bound_to:
      literal: MODELS
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: assemble_model_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        description: $.inputs.description
        fingerprint: $.inputs.fingerprint
        state: REGISTERED
        time_in_service_id: ''
    source_finding: {phase: p7, register: cc_composition, key: assemble_model_record}
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: assemble_model_record
    direction: OUTPUT
    field: model_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_model_record}
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: write_model_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: write_model_record}
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: write_model_record
    direction: INPUT
    field: value
    bound_to: results.assemble_model_record.model_record
    source_finding: {phase: p7, register: cc_composition, key: write_model_record}
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: write_model_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_model_record}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: read_model_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: read_model_record
    direction: OUTPUT
    field: model_record
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: read_model_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_registered
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        state: $.results.read_model_record.model_record.state
    source_finding: {phase: p7, register: cc_composition, key: require_registered}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_registered
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: state
        op: eq
        value: REGISTERED
    source_finding: {phase: p7, register: cc_composition, key: require_registered}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_registered
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_registered}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: confirm_ceiling_declared
    direction: INPUT
    field: value
    bound_to: inputs.ceiling
    source_finding: {phase: p7, register: cc_composition, key: confirm_ceiling_declared}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: confirm_ceiling_declared
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - public
      - internal
      - confidential
      - restricted
    source_finding: {phase: p7, register: cc_composition, key: confirm_ceiling_declared}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: confirm_ceiling_declared
    direction: OUTPUT
    field: ceiling_declared
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: confirm_ceiling_declared}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: INPUT
    field: key
    bound_to: inputs.time_in_service_id
    source_finding: {phase: p7, register: cc_composition, key: claim_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
    source_finding: {phase: p7, register: cc_composition, key: claim_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: INPUT
    field: target_ref
    bound_to:
      literal: TIMES_IN_SERVICE
    source_finding: {phase: p7, register: cc_composition, key: claim_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
    source_finding: {phase: p7, register: cc_composition, key: claim_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: INPUT
    field: filter
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        state: REGISTERED
    source_finding: {phase: p7, register: cc_composition, key: mark_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: IN_SERVICE
        time_in_service_id: $.inputs.time_in_service_id
    source_finding: {phase: p7, register: cc_composition, key: mark_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
    source_finding: {phase: p7, register: cc_composition, key: mark_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
    source_finding: {phase: p7, register: cc_composition, key: mark_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: mark_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_transition
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        updated_count: $.results.mark_in_service.updated_count
    source_finding: {phase: p7, register: cc_composition, key: require_transition}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_transition
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: updated_count
        op: eq
        value: 1
    source_finding: {phase: p7, register: cc_composition, key: require_transition}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_transition
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_transition}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: assemble_time_in_service
    direction: INPUT
    field: fields
    bound_to:
      literal:
        time_in_service_id: $.inputs.time_in_service_id
        identity_key: $.inputs.identity_key
        ceiling: $.inputs.ceiling
        system_prompt: $.inputs.system_prompt
        response_rules: $.inputs.response_rules
        state: OPEN
    source_finding: {phase: p7, register: cc_composition, key: assemble_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: assemble_time_in_service
    direction: OUTPUT
    field: time_in_service
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: write_time_in_service
    direction: INPUT
    field: key
    bound_to: inputs.time_in_service_id
    source_finding: {phase: p7, register: cc_composition, key: write_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: write_time_in_service
    direction: INPUT
    field: value
    bound_to: results.assemble_time_in_service.time_in_service
    source_finding: {phase: p7, register: cc_composition, key: write_time_in_service}
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: write_time_in_service
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_time_in_service}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: read_model_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: read_model_record
    direction: OUTPUT
    field: model_record
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: read_model_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_in_service
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        state: $.results.read_model_record.model_record.state
    source_finding: {phase: p7, register: cc_composition, key: require_in_service}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_in_service
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: state
        op: eq
        value: IN_SERVICE
    source_finding: {phase: p7, register: cc_composition, key: require_in_service}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_in_service
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_in_service}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: INPUT
    field: filter
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        state: IN_SERVICE
    source_finding: {phase: p7, register: cc_composition, key: mark_registered}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: REGISTERED
        time_in_service_id: ''
    source_finding: {phase: p7, register: cc_composition, key: mark_registered}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
    source_finding: {phase: p7, register: cc_composition, key: mark_registered}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
    source_finding: {phase: p7, register: cc_composition, key: mark_registered}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: mark_registered}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_transition
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        updated_count: $.results.mark_registered.updated_count
    source_finding: {phase: p7, register: cc_composition, key: require_transition}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_transition
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: updated_count
        op: eq
        value: 1
    source_finding: {phase: p7, register: cc_composition, key: require_transition}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_transition
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_transition}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: close_time_in_service
    direction: INPUT
    field: key
    bound_to: results.read_model_record.model_record.time_in_service_id
    source_finding: {phase: p7, register: cc_composition, key: close_time_in_service}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: close_time_in_service
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: CLOSED
    source_finding: {phase: p7, register: cc_composition, key: close_time_in_service}
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: close_time_in_service
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: close_time_in_service}
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: INPUT
    field: key
    bound_to: inputs.user_prompt_id
    source_finding: {phase: p7, register: cc_composition, key: claim_user_prompt}
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_APPENDONLY_JSONL_V0
    source_finding: {phase: p7, register: cc_composition, key: claim_user_prompt}
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: INPUT
    field: target_ref
    bound_to:
      literal: USER_PROMPT_RECORDS
    source_finding: {phase: p7, register: cc_composition, key: claim_user_prompt}
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
    source_finding: {phase: p7, register: cc_composition, key: claim_user_prompt}
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_user_prompt}
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: read_model_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: read_model_record
    direction: OUTPUT
    field: model_record
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: read_model_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_model_record}
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: require_in_service
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        state: $.results.read_model_record.model_record.state
    source_finding: {phase: p7, register: cc_composition, key: require_in_service}
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: require_in_service
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: state
        op: eq
        value: IN_SERVICE
    source_finding: {phase: p7, register: cc_composition, key: require_in_service}
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: require_in_service
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_in_service}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: read_time_in_service
    direction: INPUT
    field: key
    bound_to: inputs.time_in_service_id
    source_finding: {phase: p7, register: cc_composition, key: read_time_in_service}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: read_time_in_service
    direction: OUTPUT
    field: time_in_service
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_time_in_service}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: read_time_in_service
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_time_in_service}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: confirm_kind_declared
    direction: INPUT
    field: value
    bound_to: inputs.kind
    source_finding: {phase: p7, register: cc_composition, key: confirm_kind_declared}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: confirm_kind_declared
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - public
      - internal
      - confidential
      - restricted
    source_finding: {phase: p7, register: cc_composition, key: confirm_kind_declared}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: confirm_kind_declared
    direction: OUTPUT
    field: kind_declared
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: confirm_kind_declared}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: compare_sensitivity
    direction: INPUT
    field: kind
    bound_to: inputs.kind
    source_finding: {phase: p7, register: cc_composition, key: compare_sensitivity}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: compare_sensitivity
    direction: INPUT
    field: ceiling
    bound_to: results.read_time_in_service.time_in_service.ceiling
    source_finding: {phase: p7, register: cc_composition, key: compare_sensitivity}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: compare_sensitivity
    direction: INPUT
    field: kinds
    bound_to:
      literal:
      - public
      - internal
      - confidential
      - restricted
    source_finding: {phase: p7, register: cc_composition, key: compare_sensitivity}
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: compare_sensitivity
    direction: OUTPUT
    field: within_ceiling
    bound_to: capability_result.within_ceiling
    source_finding: {phase: p7, register: cc_composition, key: compare_sensitivity}
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: INPUT
    field: system_prompt
    bound_to: inputs.system_prompt
    source_finding: {phase: p7, register: cc_composition, key: assemble_reading}
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: INPUT
    field: question
    bound_to: inputs.question
    source_finding: {phase: p7, register: cc_composition, key: assemble_reading}
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: INPUT
    field: supporting_material
    bound_to: inputs.supporting_material
    source_finding: {phase: p7, register: cc_composition, key: assemble_reading}
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: INPUT
    field: reading_capacity
    bound_to: inputs.reading_capacity
    source_finding: {phase: p7, register: cc_composition, key: assemble_reading}
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: OUTPUT
    field: reading
    bound_to: capability_result.reading
    source_finding: {phase: p7, register: cc_composition, key: assemble_reading}
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: OUTPUT
    field: reading_length
    bound_to: capability_result.reading_length
    source_finding: {phase: p7, register: cc_composition, key: assemble_reading}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: INPUT
    field: response_rules
    bound_to: inputs.response_rules
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: INPUT
    field: account_numbers
    bound_to: inputs.account_numbers
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: INPUT
    field: seed
    bound_to: inputs.seed
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: OUTPUT
    field: rules_in_force
    bound_to: capability_result.rules_in_force
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: OUTPUT
    field: positions
    bound_to: capability_result.positions
    source_finding: {phase: p7, register: cc_composition, key: form_rules_in_force}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: write_response
    direction: INPUT
    field: reading
    bound_to: inputs.reading
    source_finding: {phase: p7, register: cc_composition, key: write_response}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: write_response
    direction: INPUT
    field: rules_in_force
    bound_to: results.form_rules_in_force.rules_in_force
    source_finding: {phase: p7, register: cc_composition, key: write_response}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: write_response
    direction: INPUT
    field: positions
    bound_to: results.form_rules_in_force.positions
    source_finding: {phase: p7, register: cc_composition, key: write_response}
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: write_response
    direction: OUTPUT
    field: written_response
    bound_to: capability_result.result
    source_finding: {phase: p7, register: cc_composition, key: write_response}
  - owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    step: confirm_releasable
    direction: INPUT
    field: parameters
    bound_to: inputs.release_facts
    source_finding: {phase: p7, register: cc_composition, key: confirm_releasable}
  - owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    step: confirm_releasable
    direction: INPUT
    field: rules
    bound_to: inputs.release_rules
    source_finding: {phase: p7, register: cc_composition, key: confirm_releasable}
  - owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    step: confirm_releasable
    direction: OUTPUT
    field: releasable
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: confirm_releasable}
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: assemble_user_prompt_record
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
        outcome: $.inputs.outcome
        time_in_service_id: $.inputs.time_in_service_id
        reading: $.inputs.reading
        rules_in_force: $.inputs.rules_in_force
        response: $.inputs.response
        reason: $.inputs.reason
    source_finding: {phase: p7, register: cc_composition, key: assemble_user_prompt_record}
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: assemble_user_prompt_record
    direction: OUTPUT
    field: user_prompt_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_user_prompt_record}
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: INPUT
    field: record
    bound_to: results.assemble_user_prompt_record.user_prompt_record
    source_finding: {phase: p7, register: cc_composition, key: append_user_prompt_record}
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
    source_finding: {phase: p7, register: cc_composition, key: append_user_prompt_record}
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: INPUT
    field: actor_id
    bound_to: inputs.requester_id
    source_finding: {phase: p7, register: cc_composition, key: append_user_prompt_record}
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
    source_finding: {phase: p7, register: cc_composition, key: append_user_prompt_record}
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
    source_finding: {phase: p7, register: cc_composition, key: append_user_prompt_record}
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: read_user_prompt_entries
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
    source_finding: {phase: p7, register: cc_composition, key: read_user_prompt_entries}
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: read_user_prompt_entries
    direction: OUTPUT
    field: entries
    bound_to: capability_result.entries
    source_finding: {phase: p7, register: cc_composition, key: read_user_prompt_entries}
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: read_user_prompt_entries
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_user_prompt_entries}
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: select_user_prompt_record
    direction: INPUT
    field: source
    bound_to: results.read_user_prompt_entries.entries
    source_finding: {phase: p7, register: cc_composition, key: select_user_prompt_record}
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: select_user_prompt_record
    direction: INPUT
    field: filter
    bound_to:
      literal:
        stream_id: $.inputs.user_prompt_id
    source_finding: {phase: p7, register: cc_composition, key: select_user_prompt_record}
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: select_user_prompt_record
    direction: OUTPUT
    field: user_prompt_record
    bound_to: capability_result.extracted
    source_finding: {phase: p7, register: cc_composition, key: select_user_prompt_record}
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: record
    bound_to: inputs.record
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: stream_id
    bound_to:
      literal: MODEL_OPERATIONS
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: actor_id
    bound_to: inputs.staff_id
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to:
      literal:
      - field: role
        op: eq
        value: model_staff
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_MODEL
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_MODEL
        staff_id: $.payload.staff_id
        subject: $.results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: description
    bound_to: payload.description
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_MODEL_IDENTITY_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_MODEL_IDENTITY_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: description_schema
    bound_to:
      literal:
        reading_capacity:
          type: integer
          required: true
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_MODEL_IDENTITY_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_MODEL_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: description
    bound_to: payload.description
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_MODEL_V0}
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_MODEL_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to:
      literal:
      - field: role
        op: eq
        value: model_staff
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: PLACE_MODEL_IN_SERVICE
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: PLACE_MODEL_IN_SERVICE
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_PLACE_MODEL_IN_SERVICE_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: time_in_service_id
    bound_to: payload.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: CC_PLACE_MODEL_IN_SERVICE_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: ceiling
    bound_to: payload.ceiling
    source_finding: {phase: p7, register: execution_topology, key: CC_PLACE_MODEL_IN_SERVICE_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: system_prompt
    bound_to: payload.system_prompt
    source_finding: {phase: p7, register: execution_topology, key: CC_PLACE_MODEL_IN_SERVICE_V0}
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: response_rules
    bound_to: payload.response_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_PLACE_MODEL_IN_SERVICE_V0}
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to:
      literal:
      - field: role
        op: eq
        value: model_staff
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: WITHDRAW_MODEL_FROM_SERVICE
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: WITHDRAW_MODEL_FROM_SERVICE
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_WITHDRAW_MODEL_FROM_SERVICE_V0}
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to:
      literal:
      - field: role
        op: eq
        value: model_staff
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0}
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETRIEVE_USER_PROMPT_RECORD
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETRIEVE_USER_PROMPT_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_MODEL_OPERATION_V0}
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: CC_RETRIEVE_USER_PROMPT_RECORD_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_USER_PROMPT_IDENTITY_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: permitted_customers
    bound_to: payload.permitted_customers
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_ADMIT_USER_PROMPT_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_WITHIN_CEILING_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_WITHIN_CEILING_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: system_prompt
    bound_to: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_READING_FITS_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_READING_FITS_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_READING_FITS_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_READING_FITS_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: response_rules
    bound_to: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_WRITE_MODEL_RESPONSE_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: account_numbers
    bound_to: payload.account_numbers
    source_finding: {phase: p7, register: execution_topology, key: CC_WRITE_MODEL_RESPONSE_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: seed
    bound_to: payload.seed
    source_finding: {phase: p7, register: execution_topology, key: CC_WRITE_MODEL_RESPONSE_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
    source_finding: {phase: p7, register: execution_topology, key: CC_WRITE_MODEL_RESPONSE_V0}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CONFIRM_NO_RULE_STOPPED
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        stopped_by: $.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_NO_RULE_STOPPED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CONFIRM_NO_RULE_STOPPED
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: stopped_by
        op: eq
        value: none
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_NO_RULE_STOPPED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CONFIRM_FINISHED
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        finished: $.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.finished
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_FINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CONFIRM_FINISHED
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: finished
        op: eq
        value: true
    source_finding: {phase: p7, register: execution_topology, key: CONFIRM_FINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: response
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.written_response.text
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: outcome
    bound_to:
      literal: RESPONDED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_RESPONDED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: reason
    bound_to:
      literal: requester_not_permitted_for_customer
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_PERMITTED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: reason
    bound_to:
      literal: model_not_registered
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_REGISTERED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: reason
    bound_to:
      literal: model_not_in_service
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_NOT_IN_SERVICE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: reason
    bound_to:
      literal: kind_above_sensitivity_ceiling
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_ABOVE_CEILING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: reason
    bound_to:
      literal: reading_longer_than_model_can_read
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_TOO_LONG_TO_READ}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: reason
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_BY_RULE}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: reason
    bound_to:
      literal: longest_response_reached
    source_finding: {phase: p7, register: execution_topology, key: RECORD_REFUSED_UNFINISHED}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: outcome
    bound_to:
      literal: FAILED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: reason
    bound_to:
      literal: store_failed_before_the_model_read
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_BEFORE_READING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: kind
    bound_to: payload.kind
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: question
    bound_to: payload.question
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: outcome
    bound_to:
      literal: FAILED
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: reason
    bound_to:
      literal: writing_failed
    source_finding: {phase: p7, register: execution_topology, key: RECORD_FAILED_WHILE_WRITING}
  interface_fields:
  - artifact: causal_language_model::IN_REGISTER_MODEL_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
  - artifact: causal_language_model::IN_REGISTER_MODEL_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the operation trail
  - artifact: causal_language_model::IN_REGISTER_MODEL_V0
    direction: INPUT
    field: description
    type: object
    required: 'YES'
    default: ''
    meaning: How the model is built, including the amount of text it can read at once
  - artifact: causal_language_model::IN_REGISTER_MODEL_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The training fingerprint, the provider's claim
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the operation trail
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: ''
    meaning: The time in service's identity, claimed once at placement
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: ceiling
    type: string
    required: 'YES'
    default: ''
    meaning: The most sensitive kind of information the model may read
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: system_prompt
    type: string
    required: 'YES'
    default: ''
    meaning: The business's standing instructions to the model for its time in service
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: ''
    meaning: The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response
  - artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
  - artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the operation trail
  - artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The user prompt's identity, named by the requester and claimed once
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: requester_id
    type: string
    required: 'YES'
    default: ''
    meaning: The requester who submits the user prompt
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: permitted_customers
    type: array
    required: 'YES'
    default: ''
    meaning: The customers the requester may act for, as the business's existing arrangements state
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: ''
    meaning: The customer the user prompt is for
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: ''
    meaning: The customer's own account numbers, from the business's existing records
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: ''
    meaning: The most sensitive kind of information the question and its material contain
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: ''
    meaning: What the requester asks on the customer's behalf
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: ''
    meaning: Material carried with the question for the model to read
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: ''
    meaning: The seed each adventurous word choice is drawn from
  - artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
  - artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the operation trail
  - artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The user prompt's identity, named by the requester and claimed once
  - artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
  - artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against, fixed by this design
  - artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: OUTPUT
    field: is_authorized
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the staff member is model staff
  - artifact: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The user prompt's identity, named by the requester and claimed once
  - artifact: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: ''
    meaning: Where the claimed identity resolves to
  - artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: ''
    meaning: The customer the user prompt is for
  - artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: permitted_customers
    type: array
    required: 'YES'
    default: ''
    meaning: The customers the requester may act for, as the business's existing arrangements state
  - artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: OUTPUT
    field: acts_for_customer
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the requester may act for the customer
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: description
    type: object
    required: 'YES'
    default: ''
    meaning: How the model is built, including the amount of text it can read at once
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: description_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields a model description must carry, fixed by this design
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The training fingerprint, the provider's claim
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: ''
    meaning: Where the claimed key resolves to
  - artifact: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: description
    type: object
    required: 'YES'
    default: ''
    meaning: How the model is built, including the amount of text it can read at once
  - artifact: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The training fingerprint, the provider's claim
  - artifact: causal_language_model::CC_REGISTER_MODEL_V0
    direction: OUTPUT
    field: model_record
    type: object
    required: 'YES'
    default: ''
    meaning: The model's record, registered
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: ''
    meaning: The time in service's identity, claimed once at placement
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: ceiling
    type: string
    required: 'YES'
    default: ''
    meaning: The most sensitive kind of information the model may read
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: system_prompt
    type: string
    required: 'YES'
    default: ''
    meaning: The business's standing instructions to the model for its time in service
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: ''
    meaning: The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: OUTPUT
    field: time_in_service
    type: object
    required: 'YES'
    default: ''
    meaning: The time in service opened
  - artifact: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: OUTPUT
    field: model_record
    type: object
    required: 'YES'
    default: ''
    meaning: The model's record as it stood before withdrawal
  - artifact: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    direction: OUTPUT
    field: model_record
    type: object
    required: 'YES'
    default: ''
    meaning: The record of the model the user prompt names, in service
  - artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: ''
    meaning: The time in service's identity, claimed once at placement
  - artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: ''
    meaning: The most sensitive kind of information the question and its material contain
  - artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: OUTPUT
    field: time_in_service
    type: object
    required: 'YES'
    default: ''
    meaning: The model's open time in service, with its ceiling, system prompt and response rules
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: system_prompt
    type: string
    required: 'YES'
    default: ''
    meaning: The business's standing instructions to the model for its time in service
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: ''
    meaning: What the requester asks on the customer's behalf
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: ''
    meaning: Material carried with the question for the model to read
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    type: integer
    required: 'YES'
    default: ''
    meaning: How many words the model can read at once; words, not a real model's tokens
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: OUTPUT
    field: reading
    type: object
    required: 'YES'
    default: ''
    meaning: Exactly what the model reads
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: OUTPUT
    field: reading_length
    type: integer
    required: 'YES'
    default: ''
    meaning: How long what the model reads is, in words
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: ''
    meaning: The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: ''
    meaning: The customer's own account numbers, from the business's existing records
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: ''
    meaning: The seed each adventurous word choice is drawn from
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: ''
    meaning: Exactly what the model read, when it read anything
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: OUTPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: ''
    meaning: The response rules in force for this user prompt, with its seed
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: OUTPUT
    field: written_response
    type: object
    required: 'YES'
    default: ''
    meaning: The response as written, whether it finished, the rule that stopped it and the words stopped
  - artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    direction: INPUT
    field: release_facts
    type: object
    required: 'YES'
    default: ''
    meaning: The facts of the written response one release condition reads
  - artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    direction: INPUT
    field: release_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The release condition, as a rule over those facts
  - artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    direction: OUTPUT
    field: releasable
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the condition for release holds
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The user prompt's identity, named by the requester and claimed once
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: requester_id
    type: string
    required: 'YES'
    default: ''
    meaning: The requester who submits the user prompt
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: ''
    meaning: The customer the user prompt is for
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: ''
    meaning: The most sensitive kind of information the question and its material contain
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: ''
    meaning: What the requester asks on the customer's behalf
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: ''
    meaning: Material carried with the question for the model to read
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: outcome
    type: string
    required: 'YES'
    default: ''
    meaning: RESPONDED, REFUSED or FAILED
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'NO'
    default: ''
    meaning: The time in service's identity, claimed once at placement
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: reading
    type: object
    required: 'NO'
    default: ''
    meaning: Exactly what the model read, when it read anything
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: rules_in_force
    type: object
    required: 'NO'
    default: ''
    meaning: The response rules in force, when the model wrote
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: response
    type: string
    required: 'NO'
    default: ''
    meaning: The model response released
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: reason
    type: string
    required: 'NO'
    default: ''
    meaning: Why the user prompt was refused, or where it failed
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: ''
    meaning: The identity of the appended user prompt record
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The record's position in the user prompt records
  - artifact: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The user prompt's identity, named by the requester and claimed once
  - artifact: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: OUTPUT
    field: user_prompt_record
    type: array
    required: 'YES'
    default: ''
    meaning: The record of the user prompt
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    type: object
    required: 'YES'
    default: ''
    meaning: The account of the performed operation
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the operation trail
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    type: string
    required: 'YES'
    default: ''
    meaning: The operation performed
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: ''
    meaning: The identity of the appended trail entry
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The entry's position in the trail
  - artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    direction: INPUT
    field: description
    type: object
    required: 'YES'
    default: ''
    meaning: How the model is built, including the amount of text it can read at once
  - artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: ''
    meaning: The training fingerprint, the provider's claim
  - artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: ''
    meaning: The kind of information stated
  - artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    direction: INPUT
    field: ceiling
    type: string
    required: 'YES'
    default: ''
    meaning: The most sensitive kind of information the model may read
  - artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    direction: INPUT
    field: kinds
    type: array
    required: 'YES'
    default: ''
    meaning: The declared kinds, least sensitive first
  - artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    direction: OUTPUT
    field: within_ceiling
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the kind is no more sensitive than the ceiling
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: INPUT
    field: system_prompt
    type: string
    required: 'YES'
    default: ''
    meaning: The business's standing instructions to the model for its time in service
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: ''
    meaning: What the requester asks on the customer's behalf
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: ''
    meaning: Material carried with the question for the model to read
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: INPUT
    field: reading_capacity
    type: integer
    required: 'YES'
    default: ''
    meaning: How many words the model can read at once; words, not a real model's tokens
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: OUTPUT
    field: reading
    type: object
    required: 'YES'
    default: ''
    meaning: Exactly what the model reads
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: OUTPUT
    field: reading_length
    type: integer
    required: 'YES'
    default: ''
    meaning: How long it is, in words
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: ''
    meaning: The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: ''
    meaning: The customer's own account numbers, from the business's existing records
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: ''
    meaning: The seed each adventurous word choice is drawn from
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: OUTPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: ''
    meaning: The forbidden rules, the freedom of word choice and the seed in force
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: OUTPUT
    field: positions
    type: array
    required: 'YES'
    default: ''
    meaning: One position per word up to the longest response
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: ''
    meaning: Exactly what the model reads
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: INPUT
    field: text
    type: string
    required: 'YES'
    default: ''
    meaning: The response so far
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: INPUT
    field: finished
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the response has finished, in which case no word is offered
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: INPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: ''
    meaning: The rule that stopped the response, in which case no word is offered
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: OUTPUT
    field: candidates
    type: array
    required: 'YES'
    default: ''
    meaning: The words the model offers next, each with its likelihood
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: candidates
    type: array
    required: 'YES'
    default: ''
    meaning: The words offered, each with its likelihood
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: ''
    meaning: The response rules in force
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: position
    type: integer
    required: 'YES'
    default: ''
    meaning: Which word this is
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: text
    type: string
    required: 'YES'
    default: ''
    meaning: The response so far
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: finished
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the response has finished
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: ''
    meaning: The rule that left no permitted word, or none
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: stopped
    type: array
    required: 'YES'
    default: ''
    meaning: The words stopped so far, each with its position and rule
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: OUTPUT
    field: text
    type: string
    required: 'YES'
    default: ''
    meaning: The response so far, with the chosen word
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: OUTPUT
    field: finished
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the chosen word ends the response
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: OUTPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: ''
    meaning: The rule that left no permitted word, or none
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: OUTPUT
    field: stopped
    type: array
    required: 'YES'
    default: ''
    meaning: The words stopped so far, with those stopped this pass
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: ''
    meaning: Exactly what the model reads
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: ''
    meaning: The response rules in force
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: position
    type: integer
    required: 'YES'
    default: ''
    meaning: Which word this is
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: text
    type: string
    required: 'YES'
    default: ''
    meaning: The response so far
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: finished
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the response has finished
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: ''
    meaning: The rule that left no permitted word, or none
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: stopped
    type: array
    required: 'YES'
    default: ''
    meaning: The words stopped so far
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: OUTPUT
    field: result
    type: object
    required: 'YES'
    default: ''
    meaning: The response so far, whether it finished, the rule that stopped it and the words stopped
  - artifact: causal_language_model::CT_WRITE_RESPONSE_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: ''
    meaning: Exactly what the model reads
  - artifact: causal_language_model::CT_WRITE_RESPONSE_V0
    direction: INPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: ''
    meaning: The response rules in force
  - artifact: causal_language_model::CT_WRITE_RESPONSE_V0
    direction: INPUT
    field: positions
    type: array
    required: 'YES'
    default: ''
    meaning: One position per word up to the longest response
  - artifact: causal_language_model::CT_WRITE_RESPONSE_V0
    direction: OUTPUT
    field: result
    type: object
    required: 'YES'
    default: ''
    meaning: The response as written, whether it finished, the rule that stopped it and the words stopped
  - artifact: causal_language_model::EV_MODEL_REGISTERED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::EV_MODEL_REGISTERED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the operation trail
  - artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    direction: OUTPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: ''
    meaning: The time in service's identity, claimed once at placement
  - artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the operation trail
  - artifact: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the operation trail
  - artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    direction: OUTPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The user prompt's identity, named by the requester and claimed once
  - artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    direction: OUTPUT
    field: requester_id
    type: string
    required: 'YES'
    default: ''
    meaning: The requester who submits the user prompt
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    direction: OUTPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: ''
    meaning: The user prompt's identity, named by the requester and claimed once
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a model's description and fingerprint
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    direction: OUTPUT
    field: requester_id
    type: string
    required: 'YES'
    default: ''
    meaning: The requester who submits the user prompt
  - artifact: causal_language_model::AC_MODEL_STAFF_V0
    direction: ATTRIBUTE
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member's identity as the business knows it
  - artifact: causal_language_model::AC_MODEL_STAFF_V0
    direction: ATTRIBUTE
    field: authorized
    type: boolean
    required: 'NO'
    default: false
    meaning: Whether the staff member is model staff; decided by the business's existing arrangements, read here
  - artifact: causal_language_model::AC_REQUESTER_V0
    direction: ATTRIBUTE
    field: requester_id
    type: string
    required: 'YES'
    default: ''
    meaning: The requester's identity as the business knows it
  - artifact: causal_language_model::AC_REQUESTER_V0
    direction: ATTRIBUTE
    field: permitted_customers
    type: array
    required: 'NO'
    default: '[]'
    meaning: The customers the requester may act for; decided by the business's existing arrangements, read here
  implementation_bindings:
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    callable: execute
    operation: FORM_MODEL_IDENTITY_KEY
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_FORM_MODEL_IDENTITY_KEY_V0}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    callable: execute
    operation: COMPARE_SENSITIVITY
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_COMPARE_SENSITIVITY_V0}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    callable: execute
    operation: ASSEMBLE_MODEL_READING
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_ASSEMBLE_MODEL_READING_V0}
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    callable: execute
    operation: FORM_RESPONSE_RULES
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_FORM_RESPONSE_RULES_V0}
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    callable: execute
    operation: OFFER_NEXT_WORDS
    kind: atom
    purity: ct_impure
    refusal: never
    source_finding: {phase: p7, register: new_artifacts, key: CT_IMPURE_OFFER_NEXT_WORDS_V0}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    callable: execute
    operation: CHOOSE_PERMITTED_WORD
    kind: atom
    purity: ct_pure
    refusal: returns
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_CHOOSE_PERMITTED_WORD_V0}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    callable: ''
    operation: WRITE_NEXT_WORD
    kind: molecule
    purity: ct_impure
    refusal: returns
    source_finding: {phase: p7, register: new_artifacts, key: CT_WRITE_NEXT_WORD_V0}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    callable: ''
    operation: WRITE_RESPONSE
    kind: molecule
    purity: ct_impure
    refusal: returns
    source_finding: {phase: p7, register: new_artifacts, key: CT_WRITE_RESPONSE_V0}
  vocabulary_extensions:
  - vocabulary_code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    extends: null
    group: kind_of_information
    casing: lower_snake
    value: public
    meaning: The least sensitive kind
    source_finding: {phase: p5, register: provisional_codes, key: VOCAB_KIND_OF_INFORMATION_V0}
  - vocabulary_code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    extends: null
    group: kind_of_information
    casing: lower_snake
    value: internal
    meaning: More sensitive than public
    source_finding: {phase: p5, register: provisional_codes, key: VOCAB_KIND_OF_INFORMATION_V0}
  - vocabulary_code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    extends: null
    group: kind_of_information
    casing: lower_snake
    value: confidential
    meaning: More sensitive than internal
    source_finding: {phase: p5, register: provisional_codes, key: VOCAB_KIND_OF_INFORMATION_V0}
  - vocabulary_code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    extends: null
    group: kind_of_information
    casing: lower_snake
    value: restricted
    meaning: The most sensitive kind
    source_finding: {phase: p5, register: provisional_codes, key: VOCAB_KIND_OF_INFORMATION_V0}
  runtime_policies:
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p7, register: rb_declarations, key: RB_MODEL_RESPONSE_BINDINGS_V0}
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p7, register: rb_declarations, key: RB_MODEL_RESPONSE_BINDINGS_V0}
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    source_finding: {phase: p7, register: rb_declarations, key: RB_MODEL_RESPONSE_BINDINGS_V0}
  artifact_properties:
  - artifact: causal_language_model::AC_MODEL_STAFF_V0
    property: type
    value: ENDUSER
    source_finding: {phase: p5, register: provisional_codes, key: AC_MODEL_STAFF_V0}
  - artifact: causal_language_model::AC_REQUESTER_V0
    property: type
    value: ENDUSER
    source_finding: {phase: p5, register: provisional_codes, key: AC_REQUESTER_V0}
  - artifact: causal_language_model::WF_REGISTER_MODEL_V0
    property: emit.EXIT_REGISTERED
    value:
    - causal_language_model::EV_MODEL_REGISTERED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - artifact: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    property: emit.EXIT_PLACED
    value:
    - causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - artifact: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    property: emit.EXIT_WITHDRAWN
    value:
    - causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - artifact: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    property: emit.EXIT_RESPONDED
    value:
    - causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - artifact: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    property: emit.EXIT_REFUSED
    value:
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    property: moment
    value: refusal
    source_finding: {phase: p0, register: business_events, key: User Prompt Refused}
  - artifact: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    property: layer
    value: DOMAINS
    source_finding: {phase: p5, register: provisional_codes, key: STRUCTURE_MODEL_RESPONSE_STORAGE_V0}
  structure_stores:
  - store_name: MODELS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: causal_language_model/model_response/models.json
    used_by: causal_language_model::CC_REGISTER_MODEL_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every model the business holds}
  - store_name: MODEL_IDENTITY_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: causal_language_model/model_response/model_identity_registry.jsonl
    used_by: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    source_finding: {phase: p6, register: storage_governance, key: 'A claim on each model''s identity, held once'}
  - store_name: TIME_IN_SERVICE_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: causal_language_model/model_response/time_in_service_registry.jsonl
    used_by: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    source_finding: {phase: p6, register: storage_governance, key: 'A claim on each time in service''s identity, held once'}
  - store_name: USER_PROMPT_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: causal_language_model/model_response/user_prompt_registry.jsonl
    used_by: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    source_finding: {phase: p6, register: storage_governance, key: 'A claim on each user prompt''s identity, held once'}
  - store_name: TIMES_IN_SERVICE
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: causal_language_model/model_response/times_in_service.json
    used_by: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every time in service}
  - store_name: USER_PROMPT_RECORDS
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: causal_language_model/model_response/user_prompt_records.jsonl
    used_by: causal_language_model::CC_RECORD_USER_PROMPT_V0
    source_finding: {phase: p6, register: storage_governance, key: A record of every user prompt that cannot be amended}
  - store_name: MODEL_OPERATIONS
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: causal_language_model/model_response/model_operations.jsonl
    used_by: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    source_finding: {phase: p6, register: storage_governance, key: A trail of performed operations that cannot be amended}
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: model_response
    count: '43'
    artifacts: 2 AC, 5 IN, 5 WF, 15 CC, 8 CT, 5 EV, 1 VOCAB, 1 RB, 1 STRUCTURE
  generation_provenance: []
  declared_reach: []
  refusal_discharge:
  - operation: Register a model
    refused_when: Its description and fingerprint match a registered model.
    act: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    outcome: ALREADY_EXISTS
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Place a model in service
    refused_when: The model is not registered.
    act: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    outcome: NOT_FOUND
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Place a model in service
    refused_when: The model is already in service.
    act: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Withdraw a model from service
    refused_when: The model is not in service.
    act: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Withdraw a model from service
    refused_when: The model is not in service.
    act: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    outcome: NOT_FOUND
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Submit a user prompt
    refused_when: The model is not registered.
    act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: Submit a user prompt
    refused_when: The model is not in service.
    act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  - operation: Submit a user prompt
    refused_when: The user prompt contains a more sensitive kind of information than the model may read.
    act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Submit a user prompt
    refused_when: What the model would read is longer than the model can read at once.
    act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 8}
  - operation: Submit a user prompt
    refused_when: The requester is not permitted to act for the customer.
    act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 9}
  - operation: Submit a user prompt
    refused_when: The model cannot finish a response without breaking a response rule.
    act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 10}
  - operation: Submit a user prompt
    refused_when: The response reaches the longest response before it is finished.
    act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    outcome: SUCCESS
    source_finding: {phase: p0, register: operation_refusals, row: 11}
  - operation: Register a model, place in service, withdraw, retrieve a record
    refused_when: The staff member is not authorized model staff.
    act: causal_language_model::WF_REGISTER_MODEL_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 12}
  - operation: Register a model, place in service, withdraw, retrieve a record
    refused_when: The staff member is not authorized model staff.
    act: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 12}
  - operation: Register a model, place in service, withdraw, retrieve a record
    refused_when: The staff member is not authorized model staff.
    act: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 12}
  - operation: Register a model, place in service, withdraw, retrieve a record
    refused_when: The staff member is not authorized model staff.
    act: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 12}
  refusal_deferrals: []
  refusal_governance_discharge: []
  molecule_steps:
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    kind: atom
    target: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    over: null
    iterator: null
    emits: null
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    kind: atom
    target: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    over: null
    iterator: null
    emits: result
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    kind: loop
    target: causal_language_model::CT_WRITE_NEXT_WORD_V0
    over: inputs.positions
    iterator: position
    emits: result
    source_finding: {phase: p4, register: design_decisions, row: 2}
  molecule_step_bindings:
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    role: INPUT
    field: reading
    bound_to: inputs.reading
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    role: INPUT
    field: text
    bound_to: inputs.text
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    role: INPUT
    field: finished
    bound_to: inputs.finished
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    role: INPUT
    field: stopped_by
    bound_to: inputs.stopped_by
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: candidates
    bound_to: results.offered.candidates
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: rules_in_force
    bound_to: inputs.rules_in_force
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: position
    bound_to: inputs.position
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: text
    bound_to: inputs.text
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: finished
    bound_to: inputs.finished
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: stopped_by
    bound_to: inputs.stopped_by
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: stopped
    bound_to: inputs.stopped
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: CARRY
    field: text
    bound_to:
      literal: ''
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: CARRY
    field: finished
    bound_to:
      literal: false
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: CARRY
    field: stopped_by
    bound_to:
      literal: none
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: CARRY
    field: stopped
    bound_to:
      literal: []
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: position
    bound_to: iterator
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: reading
    bound_to: inputs.reading
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: rules_in_force
    bound_to: inputs.rules_in_force
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: text
    bound_to: accumulator.text
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: finished
    bound_to: accumulator.finished
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: stopped_by
    bound_to: accumulator.stopped_by
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: stopped
    bound_to: accumulator.stopped
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: UPDATE
    field: text
    bound_to: results.text
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: UPDATE
    field: finished
    bound_to: results.finished
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: UPDATE
    field: stopped_by
    bound_to: results.stopped_by
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: UPDATE
    field: stopped
    bound_to: results.stopped
    source_finding: {phase: p4, register: design_decisions, row: 2}
  test_cases:
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: forms_key_from_description_and_fingerprint
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: refuses_blank_fingerprint
    expected_outcome: VIOLATION
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: refuses_kind_above_ceiling
    expected_outcome: VIOLATION
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    expected_outcome: VIOLATION
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    expected_outcome: SUCCESS
    source_finding: {source: human}
  test_case_values:
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: forms_key_from_description_and_fingerprint
    role: INPUT
    field: description
    value:
      reading_capacity: 64
      layers: 2
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: forms_key_from_description_and_fingerprint
    role: INPUT
    field: fingerprint
    value: sha256:ab12
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: forms_key_from_description_and_fingerprint
    role: EXPECTED
    field: identity_key
    value: '{"layers":2,"reading_capacity":64}|sha256:ab12'
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: refuses_blank_fingerprint
    role: INPUT
    field: description
    value:
      reading_capacity: 64
      layers: 2
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: refuses_blank_fingerprint
    role: INPUT
    field: fingerprint
    value: ' '
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    role: INPUT
    field: kind
    value: internal
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    role: INPUT
    field: ceiling
    value: confidential
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    role: INPUT
    field: kinds
    value:
    - public
    - internal
    - confidential
    - restricted
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    role: EXPECTED
    field: within_ceiling
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: refuses_kind_above_ceiling
    role: INPUT
    field: kind
    value: restricted
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: refuses_kind_above_ceiling
    role: INPUT
    field: ceiling
    value: internal
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: refuses_kind_above_ceiling
    role: INPUT
    field: kinds
    value:
    - public
    - internal
    - confidential
    - restricted
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: INPUT
    field: system_prompt
    value: Answer briefly.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: INPUT
    field: question
    value: What is my balance?
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: INPUT
    field: supporting_material
    value: Account 12345678 balance 40.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: INPUT
    field: reading_capacity
    value: 20
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: EXPECTED
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: EXPECTED
    field: reading_length
    value: 10
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    role: INPUT
    field: system_prompt
    value: Answer briefly.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    role: INPUT
    field: question
    value: What is my balance?
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    role: INPUT
    field: supporting_material
    value: Account 12345678 balance 40.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    role: INPUT
    field: reading_capacity
    value: 5
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: INPUT
    field: response_rules
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      account_number_pattern: '[0-9](?:[ -]?[0-9]){7}'
      freedom: 0
      longest_response: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: INPUT
    field: account_numbers
    value:
    - '12345678'
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: INPUT
    field: seed
    value: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: EXPECTED
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: EXPECTED
    field: positions
    value:
    - 1
    - 2
    - 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: INPUT
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: INPUT
    field: text
    value: ''
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: INPUT
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: INPUT
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: ASSERT
    field: candidates
    value:
      mode: property
      type: non_zero
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: candidates
    value:
    - word: '87654321'
      likelihood: 0.6
    - word: Your
      likelihood: 0.3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: position
    value: 1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: text
    value: ''
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: EXPECTED
    field: text
    value: Your
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: EXPECTED
    field: stopped
    value:
    - position: 1
      word: '87654321'
      rule: another_customers_account_number
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: candidates
    value:
    - word: '4321'
      likelihood: 0.7
    - word: is
      likelihood: 0.2
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: position
    value: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: text
    value: Account 8765
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: EXPECTED
    field: text
    value: Account 8765 is
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: EXPECTED
    field: stopped
    value:
    - position: 3
      word: '4321'
      rule: another_customers_account_number
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: candidates
    value:
    - word: '5678'
      likelihood: 0.8
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: position
    value: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: text
    value: Account 1234
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: EXPECTED
    field: text
    value: Account 1234 5678
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: EXPECTED
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: candidates
    value:
    - word: '87654321'
      likelihood: 0.9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: position
    value: 1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: text
    value: ''
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: EXPECTED
    field: text
    value: ''
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: EXPECTED
    field: stopped_by
    value: another_customers_account_number
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: EXPECTED
    field: stopped
    value:
    - position: 1
      word: '87654321'
      rule: another_customers_account_number
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: candidates
    value:
    - word: balance
      likelihood: 0.6
    - word: savings
      likelihood: 0.3
    - word: loan
      likelihood: 0.1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 1
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: position
    value: 2
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: text
    value: Your
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: EXPECTED
    field: text
    value: Your savings
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: EXPECTED
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: EXPECTED
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: candidates
    value:
    - word: <end>
      likelihood: 0.9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: position
    value: 3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: text
    value: Your balance
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: text
    value: Your balance
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: finished
    value: true
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: position
    value: 1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: text
    value: ''
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: finished
    value: false
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: stopped_by
    value: none
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: stopped
    value: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: RECORDED
    field: offered
    value:
      candidates:
      - word: '87654321'
        likelihood: 0.6
      - word: Your
        likelihood: 0.3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: EXPECTED
    field: result
    value:
      text: Your
      finished: false
      stopped_by: none
      stopped:
      - position: 1
        word: '87654321'
        rule: another_customers_account_number
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: INPUT
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: INPUT
    field: positions
    value:
    - 1
    - 2
    - 3
    - 4
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: RECORDED
    field: written[0]/offered
    value:
      candidates:
      - word: '87654321'
        likelihood: 0.6
      - word: Your
        likelihood: 0.3
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: RECORDED
    field: written[1]/offered
    value:
      candidates:
      - word: balance
        likelihood: 0.9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: RECORDED
    field: written[2]/offered
    value:
      candidates:
      - word: <end>
        likelihood: 0.9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: RECORDED
    field: written[3]/offered
    value:
      candidates: []
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: EXPECTED
    field: result
    value:
      text: Your balance
      finished: true
      stopped_by: none
      stopped:
      - position: 1
        word: '87654321'
        rule: another_customers_account_number
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: INPUT
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: INPUT
    field: positions
    value:
    - 1
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: RECORDED
    field: written[0]/offered
    value:
      candidates:
      - word: Your
        likelihood: 0.9
    source_finding: {source: human}
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: EXPECTED
    field: result
    value:
      text: Your
      finished: false
      stopped_by: none
      stopped: []
    source_finding: {source: human}
  withdrawn_facts: null
```

Every binding names a field the capability declares, read from the pinned baseline
`3918d97c73a7431ecc9ef512938b34afa9028cd6e382626398750dca12defb1f`.

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

Every refusal of a submission is recorded before the act ends. The recording contract runs at eight
places in the submission, one per outcome, each handed its own outcome and reason; `Runs` names the
contract and `Node` names the place. The two release conditions run one contract at two places the
same way.

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Implementation Bindings

The offer's implementation is the test model: it offers another customer's account number first, then
the words of the supporting material, then the end of the response, and nothing once the response has
finished or a rule has stopped it. A real model later joins it as a second realization of the same
declared step, offering whole words.

The choice stops a candidate when a forbidden rule's pattern matches the response so far joined to the
candidate by one space, at a match that reaches into the candidate, unless the matched characters with
spaces and dashes removed are among the rule's exceptions. It then chooses among the permitted
candidates, most likely first and ties in offered order: of the first freedom-plus-one, the one at
position (seed plus the word's position) modulo their count. The end marker `<end>` finishes the
response; any other word is appended after one space. When nothing is permitted, the rule that stopped
the most likely candidate is named and the response is left as it stood. `none` names no rule: the
response has not been stopped.

---

## 10. Vocabulary Extensions

Every status this design routes on — ACK, NACK, SUCCESS, NOT_FOUND, ALREADY_EXISTS, VIOLATION,
BACKEND_ERROR — is already admitted. The one vocabulary authored is the kinds of information, in their
declared order.

---

## 11. Runtime Policies

---

## 12. Artifact Properties

---

## 13. STRUCTURE Stores

---

## 14. Transport Bindings

## 15. Artifact Summary

---

## 16. Generation Provenance

*Every artifact this design schedules is authored: construction renders it from the registers
above and it is its own source of truth. Nothing here is reached by invoking a generator.*

---

## 17. Declared Reach

Every act reads only what model_response owns.

---

## 18. Refusal Discharge

A submission's refusal is discharged at the place that records it: that place's success ends the act
at `EXIT_REFUSED`, which refuses. The check that found the refusal routes there and nowhere else.

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
