# Stage 7 — Design Intent: causal_language_model / model_response

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_01_model_response
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
    - Decision: model_response is a new subdomain
      Business Fact: Nothing in the composition registers a model or governs how one writes
      Resolution: A new subdomain of the causal_language_model namespace with its own two actors, five stores, one binding and five operations
      Source Finding: 'S4 design_decisions #1'
    - Decision: Writing is a molecule of two declared steps per pass
      Business Fact: The rules must act while the model writes, visibly to governance
      Resolution: One pass is a molecule of the model's offer and the rules' choice; the response is a molecule whose loop runs one pass per position up to the longest response
      Source Finding: 'S4 design_decisions #2'
    - Decision: Determinism ends at the model's step
      Business Fact: A reader must see exactly where determinism ends
      Resolution: Only the offer is declared ct_impure; the choice emits each pass's result, so nothing is decided on the model's offer
      Source Finding: 'S4 design_decisions #3'
    - Decision: A trace is reproduced from its record
      Business Fact: A user prompt's trace must be reproducible from what was recorded
      Resolution: The platform records each offer where it is produced; the writing molecule's vectors state recorded offers and are proven by substituting them
      Source Finding: 'S4 design_decisions #4'
    - Decision: The seed is a recorded input
      Business Fact: Anyone reading the record can re-derive each chosen word
      Resolution: The user prompt states a seed; it enters the rules in force, which the user prompt record keeps whole
      Source Finding: 'S4 design_decisions #5'
    - Decision: The test model is a realization of the model's step
      Business Fact: The rules must be shown to hold against a model that tries to break them
      Resolution: The offer's implementation is the test model, which offers another customer's account number first
      Source Finding: 'S4 design_decisions #6'
    - Decision: The customer's account numbers travel with the user prompt
      Business Fact: The rule against another customer's account number is formed per user prompt
      Resolution: The rules in force add one forbidden pattern, the account-number shape, excepting the customer's own numbers; every rule is read against the response so far joined to the candidate, so a number written across several words is stopped at the word that completes it
      Source Finding: 'S4 design_decisions #7'
    - Decision: Uniqueness by a formed key
      Business Fact: Two registrations with the same description and fingerprint are the same model
      Resolution: A pure transform forms one key from the description and fingerprint; the registry claims it atomically, and ALREADY_EXISTS is the duplicate refusal
      Source Finding: 'S4 design_decisions #8'
    - Decision: State is data on the record
      Business Fact: A model moves into and out of service repeatedly
      Resolution: The model record carries its state and its open time in service. Placement and withdrawal change the model's state only from the state they expect, in one conditional update, and refuse when it matched nothing; the time in service record is written after, so a failure between the two leaves a model no user prompt can reach rather than one answering under no rules
      Source Finding: 'S4 design_decisions #9'
    - Decision: Membership before order
      Business Fact: Membership is mechanism; the comparison is this subdomain's rule
      Resolution: The stated kind is confirmed a declared kind, then compared with the ceiling by the declared order
      Source Finding: 'S4 design_decisions #10'
    - Decision: Retrieval raises no event
      Business Fact: Nothing reacts to a read
      Resolution: Retrieval appends to the operation trail and declares no business moment
      Source Finding: 'S4 design_decisions #11'
    - Decision: Authorization is read, never granted
      Business Fact: Which staff are model staff and who may act for which customer is decided elsewhere
      Resolution: The business's existing arrangements are the trusted source of who is model staff and whom a requester may act for; they assert both through the ingress, as the staff member's credentials and the requester's permitted customers, and model_response trusts that assertion and authenticates neither. The rules the credentials are checked against, and the schema a description is checked against, are fixed by this design and never supplied by the caller
      Source Finding: 'S4 design_decisions #12'
    - Decision: Every refusal is recorded with its reason
      Business Fact: Every user prompt is recorded, whether responded to or refused
      Resolution: 'Each refusal routes to its own place in the submission, where the recording contract runs with that refusal''s reason; a failure to write the response, or a store failing before the model reads, is recorded as FAILED with the stage. Not recorded: a payload the intent refuses, a second submission under a claimed identity, and a failure of the user prompt records themselves, which ends the act rejected and reports no record. A submission is traced by its user prompt record, which names the requester'
      Source Finding: 'S4 constraint_register #9'
    - Decision: One identity, one record
      Business Fact: Each model the business holds has exactly one record
      Resolution: A time in service and a user prompt are each claimed in their own register before anything is written under them; a duplicate is refused rather than overwriting or appending a second record
      Source Finding: 'S4 design_decisions #8'
    - Decision: The governed unit is a word
      Business Fact: A language model writes a response one word at a time
      Resolution: 'Choosing, stopping and reading capacity are counted in words, which is exact for the test model and a simulation for a real one: a real model''s tokens join this design only through a realization that offers whole words. A rule governs what its pattern can express and nothing else; the business does not claim a response is true'
      Source Finding: 'S4 design_decisions #6'
    - Decision: How the seed draws an adventurous word
      Business Fact: Anyone reading the record can re-derive each chosen word
      Resolution: The permitted candidates, most likely first and ties in offered order, are narrowed to the first freedom-plus-one; the word at position (seed plus the word's position) modulo that count is chosen. Freedom zero always chooses the most likely permitted word
      Source Finding: 'S4 design_decisions #5'
    - Decision: A finished response invokes no model
      Business Fact: An unfinished response is not a response
      Resolution: The loop runs one pass per position to the longest response, as molecules run; once the response has finished or a rule has stopped it, the offer is handed that fact and returns no words without consulting the model, and the choice changes nothing
      Source Finding: 'S4 design_decisions #2'
    - Decision: The kinds of information are copied into three bindings
      Business Fact: The kinds are declared once, in order, least sensitive first
      Resolution: A binding cannot read a vocabulary, so the ordered kinds are written as a literal where membership and order are checked, each copy identical to the vocabulary's entries in the same order
      Source Finding: 'S4 design_decisions #10'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Holds the model record and the time in service record, read and updated in place.
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_MUTABLE_JSON_V0
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Register-if-absent gives the atomic claim duplicate prevention needs, on a key the subdomain forms.
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_REGISTRY_V0
    - FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Appends the user prompt record and the operation trail, neither of which can be amended.
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_APPENDONLY_JSONL_V0
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Assembles the model, time in service and user prompt records from supplied values.
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reports what a model description lacks of the fields registration requires; a following rule refuses it when anything is reported.
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Confirms model staff credentials, a model's state and a response's release conditions against declared rules, and interprets each into a decision.
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Confirms a stated kind of information is a declared kind, and that a requester may act for the customer.
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    - FQDN: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Selects the one user prompt record retrieved, and interprets a record not found into a refusal.
      Source Finding: S6 ownership Append an entry to a trail that cannot be amended
    - FQDN: capability_transforms::CONSTITUTION_MOLECULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Governs the two writing molecules and runs the loop's body once per pass.
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CONSTITUTION_MOLECULES_V0
    - FQDN: capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: 'Governs the model''s offer: recorded when produced, replayed from the record, offered to a deterministic step.'
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0
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
    - Capability: The authorized model staff member who registers, places, withdraws and retrieves
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): AC
      Code: causal_language_model::AC_MODEL_STAFF_V0
      Summary: The actor whose authorization every model staff operation binds
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes AC_MODEL_STAFF_V0
    - Capability: The authorized requester who submits a user prompt on behalf of a customer
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): AC
      Code: causal_language_model::AC_REQUESTER_V0
      Summary: The actor who submits a user prompt for one customer
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes AC_REQUESTER_V0
    - Capability: A request to register a model with its description and fingerprint
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): IN
      Code: causal_language_model::IN_REGISTER_MODEL_V0
      Summary: A request to register a model with its description and fingerprint
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes IN_REGISTER_MODEL_V0
    - Capability: A request to place a registered model in service with its ceiling, system prompt and response rules
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): IN
      Code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Summary: A request to place a registered model in service with its ceiling, system prompt and response rules
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes IN_PLACE_MODEL_IN_SERVICE_V0
    - Capability: A request to withdraw a model from service
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): IN
      Code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
      Summary: A request to withdraw a model from service
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    - Capability: A user prompt submitted on behalf of a customer
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): IN
      Code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Summary: A user prompt submitted on behalf of a customer
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes IN_SUBMIT_USER_PROMPT_V0
    - Capability: A request to retrieve the record of a user prompt
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): IN
      Code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
      Summary: A request to retrieve the record of a user prompt
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes IN_RETRIEVE_USER_PROMPT_RECORD_V0
    - Capability: Registering a model, refusing a second registration of the same model
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: causal_language_model::WF_REGISTER_MODEL_V0
      Summary: Registering a model, refusing a second registration of the same model
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes WF_REGISTER_MODEL_V0
    - Capability: Opening a time in service for a registered model not already in service
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Summary: Opening a time in service for a registered model not already in service
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes WF_PLACE_MODEL_IN_SERVICE_V0
    - Capability: Closing a model's time in service
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Summary: Closing a model's time in service
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    - Capability: Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Summary: Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes WF_SUBMIT_USER_PROMPT_V0
    - Capability: Reading a user prompt record and recording that it was read
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Summary: Reading a user prompt record and recording that it was read
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes WF_RETRIEVE_USER_PROMPT_RECORD_V0
    - Capability: Confirm the staff member is model staff
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Summary: Confirm the staff member is model staff
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Capability: Claim a user prompt's identity so a second submission under it is refused
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Summary: Claim a user prompt's identity so a second submission under it is refused
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - Capability: Confirm the requester may act for the customer the user prompt is for
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Summary: Confirm the requester may act for the customer the user prompt is for
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - Capability: Claim a model's identity so a second registration of the same model is refused
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Summary: Claim a model's identity so a second registration of the same model is refused
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_CLAIM_MODEL_IDENTITY_V0
    - Capability: Record a model's description and fingerprint as its record, registered
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_REGISTER_MODEL_V0
      Summary: Record a model's description and fingerprint as its record, registered
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_REGISTER_MODEL_V0
    - Capability: Open a time in service with its ceiling, system prompt and response rules, and mark the model in service
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Summary: Open a time in service with its ceiling, system prompt and response rules, and mark the model in service
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_PLACE_MODEL_IN_SERVICE_V0
    - Capability: Close the time in service and mark the model registered
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Summary: Close the time in service and mark the model registered
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    - Capability: Refuse a user prompt whose model is not registered or not in service
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Summary: Refuse a user prompt before the model sees it when its model is not registered or not in service
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_ADMIT_USER_PROMPT_V0
    - Capability: Refuse a user prompt whose kind of information is above the model's ceiling
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Summary: Refuse a user prompt before the model sees it when it states a kind more sensitive than the ceiling
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_ADMIT_USER_PROMPT_V0
    - Capability: Refuse a user prompt longer than the model can read at once
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Summary: Assemble exactly what the model reads and refuse it before the model sees it when it is too long
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_ADMIT_USER_PROMPT_V0
    - Capability: Write the response word by word under the rules in force
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Summary: Form the rules in force and write the response word by word under them
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_WRITE_MODEL_RESPONSE_V0
    - Capability: Release a written response only when it finished and no rule stopped it
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Summary: Confirm one release condition of a written response, refusing it otherwise
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_WRITE_MODEL_RESPONSE_V0
    - Capability: Append the user prompt record with what the model read, the rules in force and the outcome
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Summary: Append the user prompt record with what the model read, the rules in force and the outcome
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_RECORD_USER_PROMPT_V0
    - Capability: Read the record of a user prompt
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Summary: Read the record of a user prompt
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_RETRIEVE_USER_PROMPT_RECORD_V0
    - Capability: Append a durable account of a performed operation to the subdomain's own trail
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Summary: Append a durable account of a performed operation to the subdomain's own trail
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CC_APPEND_MODEL_OPERATION_V0
    - Capability: Form the single key claimed for a model from its description and fingerprint
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Summary: Forms the single key claimed for a model from its description and fingerprint
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    - Capability: Decide whether a kind of information is no more sensitive than a ceiling
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Summary: Decides whether a kind of information is no more sensitive than a ceiling, by the declared order
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_COMPARE_SENSITIVITY_V0
    - Capability: Assemble exactly what the model reads and decide whether it fits
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Summary: Assembles exactly what the model reads and decides whether it fits what the model can read at once
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_ASSEMBLE_MODEL_READING_V0
    - Capability: Form the response rules in force for one user prompt
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Summary: Forms the response rules in force for one user prompt from the time in service and the customer's account numbers
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_FORM_RESPONSE_RULES_V0
    - Capability: The model's offer of its next words
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Summary: 'The model''s step: offers its next words given the response so far; the one step whose result is not determined by its inputs'
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_IMPURE_OFFER_NEXT_WORDS_V0
    - Capability: Stop forbidden words and choose one permitted word
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Summary: Stops forbidden words among those offered and chooses one permitted word under the freedom of word choice and a stated seed
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_CHOOSE_PERMITTED_WORD_V0
    - Capability: 'One pass of writing: the model''s offer, then the rules'' choice'
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Summary: One pass of writing, composed of the model's offer and the rules' choice
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_WRITE_NEXT_WORD_V0
    - Capability: Write a response one pass per word, up to the longest response
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CT
      Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Summary: Writes a response by repeating one pass per word, up to the longest response, carrying the response so far and the words stopped
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes CT_WRITE_RESPONSE_V0
    - Capability: The moment the business records a model
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): EV
      Code: causal_language_model::EV_MODEL_REGISTERED_V0
      Summary: The moment the business records a model
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes EV_MODEL_REGISTERED_V0
    - Capability: The moment a model is placed in service and a time in service begins
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): EV
      Code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
      Summary: The moment a model is placed in service and a time in service begins
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes EV_MODEL_SERVICE_STARTED_V0
    - Capability: The moment a model is withdrawn from service and its time in service ends
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): EV
      Code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
      Summary: The moment a model is withdrawn from service and its time in service ends
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes EV_MODEL_SERVICE_ENDED_V0
    - Capability: The moment a model response is released
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): EV
      Code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Summary: The moment a model response is released
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes EV_USER_PROMPT_RESPONDED_V0
    - Capability: The moment a user prompt yields no response
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): EV
      Code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Summary: The moment a user prompt yields no response
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes EV_USER_PROMPT_REFUSED_V0
    - Capability: The kinds of information, least sensitive first
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): VOCAB
      Code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
      Summary: 'The kinds of information, least sensitive first: public, internal, confidential, restricted'
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0
    - Capability: Bind the subdomain's operations to the stores and mechanisms they use
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): RB
      Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Summary: Binds every model response workflow to the mechanisms and stores it uses
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes RB_MODEL_RESPONSE_BINDINGS_V0
    - Capability: Declare the stores the subdomain owns
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): STRUCTURE
      Code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Summary: Declares the seven stores the subdomain owns and the paths they occupy
      Owner Subdomain: model_response
      Status: NEW
      Source Finding: S5 provisional_codes STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Binds WF: causal_language_model::WF_REGISTER_MODEL_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every model the business holds
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Binds WF: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every model the business holds
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Binds WF: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every model the business holds
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Binds WF: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every model the business holds
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Binds WF: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every model the business holds
  execution_topology:
    columns:
    - Workflow
    - Node
    - Runs
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: causal_language_model::WF_REGISTER_MODEL_V0
      Node: causal_language_model::IN_REGISTER_MODEL_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_REGISTER_MODEL_V0
    - Workflow: causal_language_model::WF_REGISTER_MODEL_V0
      Node: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Workflow: causal_language_model::WF_REGISTER_MODEL_V0
      Node: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_REGISTER_MODEL_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_MODEL_IDENTITY_V0
    - Workflow: causal_language_model::WF_REGISTER_MODEL_V0
      Node: causal_language_model::CC_REGISTER_MODEL_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_APPEND_MODEL_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_REGISTER_MODEL_V0
    - Workflow: causal_language_model::WF_REGISTER_MODEL_V0
      Node: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REGISTERED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_MODEL_OPERATION_V0
    - Workflow: causal_language_model::WF_REGISTER_MODEL_V0
      Node: EXIT_REGISTERED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_REGISTER_MODEL_V0
    - Workflow: causal_language_model::WF_REGISTER_MODEL_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_REGISTER_MODEL_V0
    - Workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Node: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_PLACE_MODEL_IN_SERVICE_V0
    - Workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Node: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Node: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_APPEND_MODEL_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_PLACE_MODEL_IN_SERVICE_V0
    - Workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Node: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_PLACED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_MODEL_OPERATION_V0
    - Workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Node: EXIT_PLACED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_PLACE_MODEL_IN_SERVICE_V0
    - Workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_PLACE_MODEL_IN_SERVICE_V0
    - Workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Node: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    - Workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Node: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Node: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_APPEND_MODEL_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    - Workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Node: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_WITHDRAWN; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_MODEL_OPERATION_V0
    - Workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Node: EXIT_WITHDRAWN
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    - Workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_SUBMIT_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_ADMIT_USER_PROMPT_V0; VIOLATION -> RECORD_REFUSED_NOT_PERMITTED
      Source Finding: S7 new_artifacts CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0; NOT_FOUND -> RECORD_REFUSED_NOT_REGISTERED; VIOLATION -> RECORD_REFUSED_NOT_IN_SERVICE; BACKEND_ERROR -> RECORD_FAILED_BEFORE_READING
      Source Finding: S7 new_artifacts CC_ADMIT_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_CONFIRM_READING_FITS_V0; NOT_FOUND -> RECORD_REFUSED_NOT_IN_SERVICE; VIOLATION -> RECORD_REFUSED_ABOVE_CEILING; BACKEND_ERROR -> RECORD_FAILED_BEFORE_READING
      Source Finding: S7 new_artifacts CC_CONFIRM_WITHIN_CEILING_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_WRITE_MODEL_RESPONSE_V0; VIOLATION -> RECORD_REFUSED_TOO_LONG_TO_READ
      Source Finding: S7 new_artifacts CC_CONFIRM_READING_FITS_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> CONFIRM_NO_RULE_STOPPED; VIOLATION -> RECORD_FAILED_WHILE_WRITING
      Source Finding: S7 new_artifacts CC_WRITE_MODEL_RESPONSE_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: CONFIRM_NO_RULE_STOPPED
      Runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> CONFIRM_FINISHED; VIOLATION -> RECORD_REFUSED_BY_RULE
      Source Finding: S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: CONFIRM_FINISHED
      Runs: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> RECORD_RESPONDED; VIOLATION -> RECORD_REFUSED_UNFINISHED
      Source Finding: S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_RESPONDED
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_RESPONDED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_REFUSED_NOT_PERMITTED
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_REFUSED_NOT_REGISTERED
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_REFUSED_NOT_IN_SERVICE
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_REFUSED_ABOVE_CEILING
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_REFUSED_TOO_LONG_TO_READ
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_REFUSED_BY_RULE
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_REFUSED_UNFINISHED
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_FAILED_BEFORE_READING
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: RECORD_FAILED_WHILE_WRITING
      Runs: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: EXIT_RESPONDED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_SUBMIT_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: EXIT_REFUSED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_SUBMIT_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_SUBMIT_USER_PROMPT_V0
    - Workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Node: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_RETRIEVE_USER_PROMPT_RECORD_V0
    - Workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Node: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_APPEND_MODEL_OPERATION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Node: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_MODEL_OPERATION_V0
    - Workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Node: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_RETRIEVED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RETRIEVE_USER_PROMPT_RECORD_V0
    - Workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Node: EXIT_RETRIEVED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_RETRIEVE_USER_PROMPT_RECORD_V0
    - Workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_RETRIEVE_USER_PROMPT_RECORD_V0
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
    - CC Code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Step: '1'
      Step Name: confirm_authorization
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: staff_credentials, authorization_rules
      Produces: is_authorized
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=staff_credentials, rules=authorization_rules; out: valid=is_authorized'
    - CC Code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Step: '1'
      Step Name: confirm_acts_for_customer
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: customer_id, permitted_customers
      Produces: acts_for_customer
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=customer_id, allowed_set=permitted_customers; out: is_member=acts_for_customer'
    - CC Code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: '1'
      Step Name: validate_description
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: description, description_schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=description, schema=description_schema; out: violations=violations'
    - CC Code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: '2'
      Step Name: require_description_complete
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: violations
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=description_findings, rules=completeness_rules; out: valid=valid'
    - CC Code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: '3'
      Step Name: form_identity_key
      Capability: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Kind (CT, CS): CT
      Operation: FORM_MODEL_IDENTITY_KEY
      Store: —
      Consumes: description, fingerprint
      Produces: identity_key
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: description=description, fingerprint=fingerprint; out: identity_key=identity_key'
    - CC Code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: '4'
      Step Name: claim_identity
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: MODEL_IDENTITY_REGISTRY
      Consumes: key, target_cs, target_ref
      Produces: address
      Routing: SUCCESS -> exit; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: ALREADY_EXISTS
      Interface: —
    - CC Code: causal_language_model::CC_REGISTER_MODEL_V0
      Step: '1'
      Step Name: assemble_model_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: identity_key, description, fingerprint
      Produces: model_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=model_fields; out: record=model_record'
    - CC Code: causal_language_model::CC_REGISTER_MODEL_V0
      Step: '2'
      Step Name: write_model_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: MODELS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: '1'
      Step Name: read_model_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: MODELS
      Consumes: key
      Produces: model_record
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: '2'
      Step Name: require_registered
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: model_record
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=model_state, rules=state_rules; out: valid=valid'
    - CC Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: '3'
      Step Name: confirm_ceiling_declared
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: ceiling
      Produces: ceiling_declared
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=ceiling, allowed_set=kinds; out: is_member=ceiling_declared'
    - CC Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: '4'
      Step Name: claim_time_in_service
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: TIME_IN_SERVICE_REGISTRY
      Consumes: key, target_cs, target_ref
      Produces: address
      Routing: SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: ALREADY_EXISTS
      Interface: —
    - CC Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: '5'
      Step Name: mark_in_service
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: UPDATE_WHERE
      Store: MODELS
      Consumes: filter, updates
      Produces: matched_keys, updated_count
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: '6'
      Step Name: require_transition
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: updated_count
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=transition, rules=transition_rules; out: valid=valid'
    - CC Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: '7'
      Step Name: assemble_time_in_service
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: time_in_service_id, identity_key, ceiling, system_prompt, response_rules
      Produces: time_in_service
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=time_in_service_fields; out: record=time_in_service'
    - CC Code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: '8'
      Step Name: write_time_in_service
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: TIMES_IN_SERVICE
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: '1'
      Step Name: read_model_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: MODELS
      Consumes: key
      Produces: model_record
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: '2'
      Step Name: require_in_service
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: model_record
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=model_state, rules=state_rules; out: valid=valid'
    - CC Code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: '3'
      Step Name: mark_registered
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: UPDATE_WHERE
      Store: MODELS
      Consumes: filter, updates
      Produces: matched_keys, updated_count
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: '4'
      Step Name: require_transition
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: updated_count
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=transition, rules=transition_rules; out: valid=valid'
    - CC Code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: '5'
      Step Name: close_time_in_service
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: UPDATE
      Store: TIMES_IN_SERVICE
      Consumes: key, updates
      Produces: result_status
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Step: '1'
      Step Name: claim_user_prompt
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: USER_PROMPT_REGISTRY
      Consumes: key, target_cs, target_ref
      Produces: address
      Routing: SUCCESS -> exit; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: ALREADY_EXISTS
      Interface: —
    - CC Code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Step: '1'
      Step Name: read_model_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: MODELS
      Consumes: key
      Produces: model_record
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Step: '2'
      Step Name: require_in_service
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: model_record
      Produces: valid
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=model_state, rules=state_rules; out: valid=valid'
    - CC Code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: '1'
      Step Name: read_time_in_service
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: TIMES_IN_SERVICE
      Consumes: key
      Produces: time_in_service
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: '2'
      Step Name: confirm_kind_declared
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: kind
      Produces: kind_declared
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=kind, allowed_set=kinds; out: is_member=kind_declared'
    - CC Code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: '3'
      Step Name: compare_sensitivity
      Capability: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Kind (CT, CS): CT
      Operation: COMPARE_SENSITIVITY
      Store: —
      Consumes: kind, time_in_service
      Produces: within_ceiling
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: kind=kind, ceiling=ceiling, kinds=kinds; out: within_ceiling=within_ceiling'
    - CC Code: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Step: '1'
      Step Name: assemble_reading
      Capability: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_MODEL_READING
      Store: —
      Consumes: system_prompt, question, supporting_material, reading_capacity
      Produces: reading, reading_length
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: system_prompt=system_prompt, question=question, supporting_material=supporting_material, reading_capacity=reading_capacity; out: reading=reading, reading_length=reading_length'
    - CC Code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
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
    - CC Code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: '2'
      Step Name: write_response
      Capability: causal_language_model::CT_WRITE_RESPONSE_V0
      Kind (CT, CS): CT
      Operation: WRITE_RESPONSE
      Store: —
      Consumes: reading, rules_in_force, positions
      Produces: written_response
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: reading=reading, rules_in_force=rules_in_force, positions=positions; out: result=written_response'
    - CC Code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Step: '1'
      Step Name: confirm_releasable
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: release_facts, release_rules
      Produces: releasable
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=release_facts, rules=release_rules; out: valid=releasable'
    - CC Code: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: '1'
      Step Name: assemble_user_prompt_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: user_prompt_id, requester_id, customer_id, identity_key, kind, question, supporting_material, outcome, time_in_service_id, reading, rules_in_force, response, reason
      Produces: user_prompt_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=user_prompt_fields; out: record=user_prompt_record'
    - CC Code: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: '2'
      Step Name: append_user_prompt_record
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
    - CC Code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: '1'
      Step Name: read_user_prompt_entries
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
    - CC Code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: '2'
      Step Name: select_user_prompt_record
      Capability: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Kind (CT, CS): CT
      Operation: FILTER_RECORDS
      Store: —
      Consumes: entries, record_criteria
      Produces: user_prompt_record
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: source=entries, filter=record_criteria; out: extracted=user_prompt_record'
    - CC Code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Step: '1'
      Step Name: append_operation
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Kind (CT, CS): CS
      Operation: APPEND
      Store: MODEL_OPERATIONS
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
    - Owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Step: confirm_authorization
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: inputs.staff_credentials
      Source Finding: S7 cc_composition confirm_authorization
    - Owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Step: confirm_authorization
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: inputs.authorization_rules
      Source Finding: S7 cc_composition confirm_authorization
    - Owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Step: confirm_authorization
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_authorized
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition confirm_authorization
    - Owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Step: confirm_acts_for_customer
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: inputs.customer_id
      Source Finding: S7 cc_composition confirm_acts_for_customer
    - Owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Step: confirm_acts_for_customer
      Direction (INPUT, OUTPUT): INPUT
      Field: allowed_set
      Bound To: inputs.permitted_customers
      Source Finding: S7 cc_composition confirm_acts_for_customer
    - Owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Step: confirm_acts_for_customer
      Direction (INPUT, OUTPUT): OUTPUT
      Field: acts_for_customer
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition confirm_acts_for_customer
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: validate_description
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.description
      Source Finding: S7 cc_composition validate_description
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: validate_description
      Direction (INPUT, OUTPUT): INPUT
      Field: schema
      Bound To: inputs.description_schema
      Source Finding: S7 cc_composition validate_description
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: validate_description
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_description
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: require_description_complete
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''violations'': ''$.results.validate_description.violations''}'
      Source Finding: S7 cc_composition require_description_complete
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: require_description_complete
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''violations'', ''op'': ''eq'', ''value'': []}]'
      Source Finding: S7 cc_composition require_description_complete
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: require_description_complete
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_description_complete
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: form_identity_key
      Direction (INPUT, OUTPUT): INPUT
      Field: description
      Bound To: inputs.description
      Source Finding: S7 cc_composition form_identity_key
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: form_identity_key
      Direction (INPUT, OUTPUT): INPUT
      Field: fingerprint
      Bound To: inputs.fingerprint
      Source Finding: S7 cc_composition form_identity_key
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: form_identity_key
      Direction (INPUT, OUTPUT): OUTPUT
      Field: identity_key
      Bound To: capability_result.identity_key
      Source Finding: S7 cc_composition form_identity_key
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: results.form_identity_key.identity_key
      Source Finding: S7 cc_composition claim_identity
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: target_cs
      Bound To: CS_MUTABLE_JSON_V0
      Source Finding: S7 cc_composition claim_identity
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: target_ref
      Bound To: MODELS
      Source Finding: S7 cc_composition claim_identity
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: address
      Bound To: capability_result.address
      Source Finding: S7 cc_composition claim_identity
    - Owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition claim_identity
    - Owner: causal_language_model::CC_REGISTER_MODEL_V0
      Step: assemble_model_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''description'': ''$.inputs.description'', ''fingerprint'': ''$.inputs.fingerprint'', ''state'': ''REGISTERED'', ''time_in_service_id'': ''''}'
      Source Finding: S7 cc_composition assemble_model_record
    - Owner: causal_language_model::CC_REGISTER_MODEL_V0
      Step: assemble_model_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: model_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_model_record
    - Owner: causal_language_model::CC_REGISTER_MODEL_V0
      Step: write_model_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition write_model_record
    - Owner: causal_language_model::CC_REGISTER_MODEL_V0
      Step: write_model_record
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_model_record.model_record
      Source Finding: S7 cc_composition write_model_record
    - Owner: causal_language_model::CC_REGISTER_MODEL_V0
      Step: write_model_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_model_record
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: model_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: require_registered
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''state'': ''$.results.read_model_record.model_record.state''}'
      Source Finding: S7 cc_composition require_registered
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: require_registered
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''state'', ''op'': ''eq'', ''value'': ''REGISTERED''}]'
      Source Finding: S7 cc_composition require_registered
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: require_registered
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_registered
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: confirm_ceiling_declared
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: inputs.ceiling
      Source Finding: S7 cc_composition confirm_ceiling_declared
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: confirm_ceiling_declared
      Direction (INPUT, OUTPUT): INPUT
      Field: allowed_set
      Bound To: '[''public'', ''internal'', ''confidential'', ''restricted'']'
      Source Finding: S7 cc_composition confirm_ceiling_declared
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: confirm_ceiling_declared
      Direction (INPUT, OUTPUT): OUTPUT
      Field: ceiling_declared
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition confirm_ceiling_declared
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: claim_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.time_in_service_id
      Source Finding: S7 cc_composition claim_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: claim_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: target_cs
      Bound To: CS_MUTABLE_JSON_V0
      Source Finding: S7 cc_composition claim_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: claim_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: target_ref
      Bound To: TIMES_IN_SERVICE
      Source Finding: S7 cc_composition claim_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: claim_time_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: address
      Bound To: capability_result.address
      Source Finding: S7 cc_composition claim_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: claim_time_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition claim_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: mark_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''state'': ''REGISTERED''}'
      Source Finding: S7 cc_composition mark_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: mark_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: updates
      Bound To: '{''state'': ''IN_SERVICE'', ''time_in_service_id'': ''$.inputs.time_in_service_id''}'
      Source Finding: S7 cc_composition mark_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: mark_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: matched_keys
      Bound To: capability_result.matched_keys
      Source Finding: S7 cc_composition mark_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: mark_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_count
      Bound To: capability_result.updated_count
      Source Finding: S7 cc_composition mark_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: mark_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition mark_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: require_transition
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''updated_count'': ''$.results.mark_in_service.updated_count''}'
      Source Finding: S7 cc_composition require_transition
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: require_transition
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''updated_count'', ''op'': ''eq'', ''value'': 1}]'
      Source Finding: S7 cc_composition require_transition
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: require_transition
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_transition
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: assemble_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''time_in_service_id'': ''$.inputs.time_in_service_id'', ''identity_key'': ''$.inputs.identity_key'', ''ceiling'': ''$.inputs.ceiling'', ''system_prompt'': ''$.inputs.system_prompt'', ''response_rules'': ''$.inputs.response_rules'', ''state'': ''OPEN''}'
      Source Finding: S7 cc_composition assemble_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: assemble_time_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: time_in_service
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: write_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.time_in_service_id
      Source Finding: S7 cc_composition write_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: write_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_time_in_service.time_in_service
      Source Finding: S7 cc_composition write_time_in_service
    - Owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Step: write_time_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_time_in_service
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: model_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: require_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''state'': ''$.results.read_model_record.model_record.state''}'
      Source Finding: S7 cc_composition require_in_service
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: require_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''state'', ''op'': ''eq'', ''value'': ''IN_SERVICE''}]'
      Source Finding: S7 cc_composition require_in_service
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: require_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_in_service
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: mark_registered
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''state'': ''IN_SERVICE''}'
      Source Finding: S7 cc_composition mark_registered
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: mark_registered
      Direction (INPUT, OUTPUT): INPUT
      Field: updates
      Bound To: '{''state'': ''REGISTERED'', ''time_in_service_id'': ''''}'
      Source Finding: S7 cc_composition mark_registered
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: mark_registered
      Direction (INPUT, OUTPUT): OUTPUT
      Field: matched_keys
      Bound To: capability_result.matched_keys
      Source Finding: S7 cc_composition mark_registered
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: mark_registered
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_count
      Bound To: capability_result.updated_count
      Source Finding: S7 cc_composition mark_registered
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: mark_registered
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition mark_registered
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: require_transition
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''updated_count'': ''$.results.mark_registered.updated_count''}'
      Source Finding: S7 cc_composition require_transition
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: require_transition
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''updated_count'', ''op'': ''eq'', ''value'': 1}]'
      Source Finding: S7 cc_composition require_transition
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: require_transition
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_transition
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: close_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: results.read_model_record.model_record.time_in_service_id
      Source Finding: S7 cc_composition close_time_in_service
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: close_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: updates
      Bound To: '{''state'': ''CLOSED''}'
      Source Finding: S7 cc_composition close_time_in_service
    - Owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: close_time_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition close_time_in_service
    - Owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Step: claim_user_prompt
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.user_prompt_id
      Source Finding: S7 cc_composition claim_user_prompt
    - Owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Step: claim_user_prompt
      Direction (INPUT, OUTPUT): INPUT
      Field: target_cs
      Bound To: CS_APPENDONLY_JSONL_V0
      Source Finding: S7 cc_composition claim_user_prompt
    - Owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Step: claim_user_prompt
      Direction (INPUT, OUTPUT): INPUT
      Field: target_ref
      Bound To: USER_PROMPT_RECORDS
      Source Finding: S7 cc_composition claim_user_prompt
    - Owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Step: claim_user_prompt
      Direction (INPUT, OUTPUT): OUTPUT
      Field: address
      Bound To: capability_result.address
      Source Finding: S7 cc_composition claim_user_prompt
    - Owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Step: claim_user_prompt
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition claim_user_prompt
    - Owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: model_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Step: read_model_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_model_record
    - Owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Step: require_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''state'': ''$.results.read_model_record.model_record.state''}'
      Source Finding: S7 cc_composition require_in_service
    - Owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Step: require_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''state'', ''op'': ''eq'', ''value'': ''IN_SERVICE''}]'
      Source Finding: S7 cc_composition require_in_service
    - Owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Step: require_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_in_service
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: read_time_in_service
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.time_in_service_id
      Source Finding: S7 cc_composition read_time_in_service
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: read_time_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: time_in_service
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_time_in_service
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: read_time_in_service
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_time_in_service
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: confirm_kind_declared
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: inputs.kind
      Source Finding: S7 cc_composition confirm_kind_declared
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: confirm_kind_declared
      Direction (INPUT, OUTPUT): INPUT
      Field: allowed_set
      Bound To: '[''public'', ''internal'', ''confidential'', ''restricted'']'
      Source Finding: S7 cc_composition confirm_kind_declared
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: confirm_kind_declared
      Direction (INPUT, OUTPUT): OUTPUT
      Field: kind_declared
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition confirm_kind_declared
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: compare_sensitivity
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: inputs.kind
      Source Finding: S7 cc_composition compare_sensitivity
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: compare_sensitivity
      Direction (INPUT, OUTPUT): INPUT
      Field: ceiling
      Bound To: results.read_time_in_service.time_in_service.ceiling
      Source Finding: S7 cc_composition compare_sensitivity
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: compare_sensitivity
      Direction (INPUT, OUTPUT): INPUT
      Field: kinds
      Bound To: '[''public'', ''internal'', ''confidential'', ''restricted'']'
      Source Finding: S7 cc_composition compare_sensitivity
    - Owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Step: compare_sensitivity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: within_ceiling
      Bound To: capability_result.within_ceiling
      Source Finding: S7 cc_composition compare_sensitivity
    - Owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Step: assemble_reading
      Direction (INPUT, OUTPUT): INPUT
      Field: system_prompt
      Bound To: inputs.system_prompt
      Source Finding: S7 cc_composition assemble_reading
    - Owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Step: assemble_reading
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: inputs.question
      Source Finding: S7 cc_composition assemble_reading
    - Owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Step: assemble_reading
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: inputs.supporting_material
      Source Finding: S7 cc_composition assemble_reading
    - Owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Step: assemble_reading
      Direction (INPUT, OUTPUT): INPUT
      Field: reading_capacity
      Bound To: inputs.reading_capacity
      Source Finding: S7 cc_composition assemble_reading
    - Owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Step: assemble_reading
      Direction (INPUT, OUTPUT): OUTPUT
      Field: reading
      Bound To: capability_result.reading
      Source Finding: S7 cc_composition assemble_reading
    - Owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Step: assemble_reading
      Direction (INPUT, OUTPUT): OUTPUT
      Field: reading_length
      Bound To: capability_result.reading_length
      Source Finding: S7 cc_composition assemble_reading
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): INPUT
      Field: response_rules
      Bound To: inputs.response_rules
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): INPUT
      Field: account_numbers
      Bound To: inputs.account_numbers
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): INPUT
      Field: seed
      Bound To: inputs.seed
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): OUTPUT
      Field: rules_in_force
      Bound To: capability_result.rules_in_force
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: form_rules_in_force
      Direction (INPUT, OUTPUT): OUTPUT
      Field: positions
      Bound To: capability_result.positions
      Source Finding: S7 cc_composition form_rules_in_force
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: write_response
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: inputs.reading
      Source Finding: S7 cc_composition write_response
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: write_response
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.form_rules_in_force.rules_in_force
      Source Finding: S7 cc_composition write_response
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: write_response
      Direction (INPUT, OUTPUT): INPUT
      Field: positions
      Bound To: results.form_rules_in_force.positions
      Source Finding: S7 cc_composition write_response
    - Owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Step: write_response
      Direction (INPUT, OUTPUT): OUTPUT
      Field: written_response
      Bound To: capability_result.result
      Source Finding: S7 cc_composition write_response
    - Owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Step: confirm_releasable
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: inputs.release_facts
      Source Finding: S7 cc_composition confirm_releasable
    - Owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Step: confirm_releasable
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: inputs.release_rules
      Source Finding: S7 cc_composition confirm_releasable
    - Owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Step: confirm_releasable
      Direction (INPUT, OUTPUT): OUTPUT
      Field: releasable
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition confirm_releasable
    - Owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: assemble_user_prompt_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''user_prompt_id'': ''$.inputs.user_prompt_id'', ''requester_id'': ''$.inputs.requester_id'', ''customer_id'': ''$.inputs.customer_id'', ''identity_key'': ''$.inputs.identity_key'', ''kind'': ''$.inputs.kind'', ''question'': ''$.inputs.question'', ''supporting_material'': ''$.inputs.supporting_material'', ''outcome'': ''$.inputs.outcome'', ''time_in_service_id'': ''$.inputs.time_in_service_id'', ''reading'': ''$.inputs.reading'', ''rules_in_force'': ''$.inputs.rules_in_force'', ''response'': ''$.inputs.response'', ''reason'': ''$.inputs.reason''}'
      Source Finding: S7 cc_composition assemble_user_prompt_record
    - Owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: assemble_user_prompt_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: user_prompt_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_user_prompt_record
    - Owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: append_user_prompt_record
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: results.assemble_user_prompt_record.user_prompt_record
      Source Finding: S7 cc_composition append_user_prompt_record
    - Owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: append_user_prompt_record
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: inputs.user_prompt_id
      Source Finding: S7 cc_composition append_user_prompt_record
    - Owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: append_user_prompt_record
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_id
      Bound To: inputs.requester_id
      Source Finding: S7 cc_composition append_user_prompt_record
    - Owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: append_user_prompt_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record_id
      Bound To: capability_result.record_id
      Source Finding: S7 cc_composition append_user_prompt_record
    - Owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Step: append_user_prompt_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: sequence_number
      Bound To: capability_result.sequence_number
      Source Finding: S7 cc_composition append_user_prompt_record
    - Owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: read_user_prompt_entries
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: inputs.user_prompt_id
      Source Finding: S7 cc_composition read_user_prompt_entries
    - Owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: read_user_prompt_entries
      Direction (INPUT, OUTPUT): OUTPUT
      Field: entries
      Bound To: capability_result.entries
      Source Finding: S7 cc_composition read_user_prompt_entries
    - Owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: read_user_prompt_entries
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_user_prompt_entries
    - Owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: select_user_prompt_record
      Direction (INPUT, OUTPUT): INPUT
      Field: source
      Bound To: results.read_user_prompt_entries.entries
      Source Finding: S7 cc_composition select_user_prompt_record
    - Owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: select_user_prompt_record
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: '{''stream_id'': ''$.inputs.user_prompt_id''}'
      Source Finding: S7 cc_composition select_user_prompt_record
    - Owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: select_user_prompt_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: user_prompt_record
      Bound To: capability_result.extracted
      Source Finding: S7 cc_composition select_user_prompt_record
    - Owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.record
      Source Finding: S7 cc_composition append_operation
    - Owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: MODEL_OPERATIONS
      Source Finding: S7 cc_composition append_operation
    - Owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_id
      Bound To: inputs.staff_id
      Source Finding: S7 cc_composition append_operation
    - Owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record_id
      Bound To: capability_result.record_id
      Source Finding: S7 cc_composition append_operation
    - Owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): OUTPUT
      Field: sequence_number
      Bound To: capability_result.sequence_number
      Source Finding: S7 cc_composition append_operation
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: '[{''field'': ''role'', ''op'': ''eq'', ''value'': ''model_staff''}]'
      Source Finding: S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REGISTER_MODEL
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REGISTER_MODEL'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key''}'
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: description
      Bound To: payload.description
      Source Finding: S7 execution_topology CC_CLAIM_MODEL_IDENTITY_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: fingerprint
      Bound To: payload.fingerprint
      Source Finding: S7 execution_topology CC_CLAIM_MODEL_IDENTITY_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: description_schema
      Bound To: '{''reading_capacity'': {''type'': ''integer'', ''required'': True}}'
      Source Finding: S7 execution_topology CC_CLAIM_MODEL_IDENTITY_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key
      Source Finding: S7 execution_topology CC_REGISTER_MODEL_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: description
      Bound To: payload.description
      Source Finding: S7 execution_topology CC_REGISTER_MODEL_V0
    - Owner: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: fingerprint
      Bound To: payload.fingerprint
      Source Finding: S7 execution_topology CC_REGISTER_MODEL_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: '[{''field'': ''role'', ''op'': ''eq'', ''value'': ''model_staff''}]'
      Source Finding: S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: PLACE_MODEL_IN_SERVICE
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''PLACE_MODEL_IN_SERVICE'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: payload.time_in_service_id
      Source Finding: S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: ceiling
      Bound To: payload.ceiling
      Source Finding: S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: system_prompt
      Bound To: payload.system_prompt
      Source Finding: S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0
    - Owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: response_rules
      Bound To: payload.response_rules
      Source Finding: S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0
    - Owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: '[{''field'': ''role'', ''op'': ''eq'', ''value'': ''model_staff''}]'
      Source Finding: S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: WITHDRAW_MODEL_FROM_SERVICE
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''WITHDRAW_MODEL_FROM_SERVICE'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    - Owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: '[{''field'': ''role'', ''op'': ''eq'', ''value'': ''model_staff''}]'
      Source Finding: S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - Owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: RETRIEVE_USER_PROMPT_RECORD
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''RETRIEVE_USER_PROMPT_RECORD'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.user_prompt_id''}'
      Source Finding: S7 execution_topology CC_APPEND_MODEL_OPERATION_V0
    - Owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology CC_RETRIEVE_USER_PROMPT_RECORD_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: permitted_customers
      Bound To: payload.permitted_customers
      Source Finding: S7 execution_topology CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_ADMIT_USER_PROMPT_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology CC_CONFIRM_WITHIN_CEILING_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology CC_CONFIRM_WITHIN_CEILING_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: system_prompt
      Bound To: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt
      Source Finding: S7 execution_topology CC_CONFIRM_READING_FITS_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology CC_CONFIRM_READING_FITS_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology CC_CONFIRM_READING_FITS_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: reading_capacity
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
      Source Finding: S7 execution_topology CC_CONFIRM_READING_FITS_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: response_rules
      Bound To: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules
      Source Finding: S7 execution_topology CC_WRITE_MODEL_RESPONSE_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: account_numbers
      Bound To: payload.account_numbers
      Source Finding: S7 execution_topology CC_WRITE_MODEL_RESPONSE_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: seed
      Bound To: payload.seed
      Source Finding: S7 execution_topology CC_WRITE_MODEL_RESPONSE_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_CONFIRM_READING_FITS_V0.reading
      Source Finding: S7 execution_topology CC_WRITE_MODEL_RESPONSE_V0
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: CONFIRM_NO_RULE_STOPPED
      Direction (INPUT, OUTPUT): INPUT
      Field: release_facts
      Bound To: '{''stopped_by'': ''$.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by''}'
      Source Finding: S7 execution_topology CONFIRM_NO_RULE_STOPPED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: CONFIRM_NO_RULE_STOPPED
      Direction (INPUT, OUTPUT): INPUT
      Field: release_rules
      Bound To: '[{''field'': ''stopped_by'', ''op'': ''eq'', ''value'': ''none''}]'
      Source Finding: S7 execution_topology CONFIRM_NO_RULE_STOPPED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: CONFIRM_FINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: release_facts
      Bound To: '{''finished'': ''$.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.finished''}'
      Source Finding: S7 execution_topology CONFIRM_FINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: CONFIRM_FINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: release_rules
      Bound To: '[{''field'': ''finished'', ''op'': ''eq'', ''value'': True}]'
      Source Finding: S7 execution_topology CONFIRM_FINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_CONFIRM_READING_FITS_V0.reading
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: response
      Bound To: results.CC_WRITE_MODEL_RESPONSE_V0.written_response.text
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_RESPONDED
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: RESPONDED
      Source Finding: S7 execution_topology RECORD_RESPONDED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: requester_not_permitted_for_customer
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_PERMITTED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: model_not_registered
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_REGISTERED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: model_not_in_service
      Source Finding: S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: kind_above_sensitivity_ceiling
      Source Finding: S7 execution_topology RECORD_REFUSED_ABOVE_CEILING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: reading_longer_than_model_can_read
      Source Finding: S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_CONFIRM_READING_FITS_V0.reading
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by
      Source Finding: S7 execution_topology RECORD_REFUSED_BY_RULE
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_CONFIRM_READING_FITS_V0.reading
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: rules_in_force
      Bound To: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: REFUSED
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: longest_response_reached
      Source Finding: S7 execution_topology RECORD_REFUSED_UNFINISHED
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: FAILED
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_BEFORE_READING
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: store_failed_before_the_model_read
      Source Finding: S7 execution_topology RECORD_FAILED_BEFORE_READING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: user_prompt_id
      Bound To: payload.user_prompt_id
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: requester_id
      Bound To: payload.requester_id
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: customer_id
      Bound To: payload.customer_id
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: kind
      Bound To: payload.kind
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: question
      Bound To: payload.question
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: supporting_material
      Bound To: payload.supporting_material
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: time_in_service_id
      Bound To: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: reading
      Bound To: results.CC_CONFIRM_READING_FITS_V0.reading
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: outcome
      Bound To: FAILED
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
    - Owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_FAILED_WHILE_WRITING
      Direction (INPUT, OUTPUT): INPUT
      Field: reason
      Bound To: writing_failed
      Source Finding: S7 execution_topology RECORD_FAILED_WHILE_WRITING
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
    - Artifact: causal_language_model::IN_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
    - Artifact: causal_language_model::IN_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the operation trail
    - Artifact: causal_language_model::IN_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: description
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How the model is built, including the amount of text it can read at once
    - Artifact: causal_language_model::IN_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The training fingerprint, the provider's claim
    - Artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
    - Artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the operation trail
    - Artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: time_in_service_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time in service's identity, claimed once at placement
    - Artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: ceiling
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most sensitive kind of information the model may read
    - Artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: system_prompt
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The business's standing instructions to the model for its time in service
    - Artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: response_rules
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response
    - Artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
    - Artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the operation trail
    - Artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The user prompt's identity, named by the requester and claimed once
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: requester_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The requester who submits the user prompt
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: permitted_customers
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customers the requester may act for, as the business's existing arrangements state
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: customer_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer the user prompt is for
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: account_numbers
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer's own account numbers, from the business's existing records
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: kind
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most sensitive kind of information the question and its material contain
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: question
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the requester asks on the customer's behalf
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: supporting_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Material carried with the question for the model to read
    - Artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: seed
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The seed each adventurous word choice is drawn from
    - Artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
    - Artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the operation trail
    - Artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The user prompt's identity, named by the requester and claimed once
    - Artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation and their role, as the business's existing arrangements assert it
    - Artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against, fixed by this design
    - Artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: is_authorized
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the staff member is model staff
    - Artifact: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The user prompt's identity, named by the requester and claimed once
    - Artifact: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Where the claimed identity resolves to
    - Artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: customer_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer the user prompt is for
    - Artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: permitted_customers
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customers the requester may act for, as the business's existing arrangements state
    - Artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: acts_for_customer
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the requester may act for the customer
    - Artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: description
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How the model is built, including the amount of text it can read at once
    - Artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: description_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields a model description must carry, fixed by this design
    - Artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The training fingerprint, the provider's claim
    - Artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Where the claimed key resolves to
    - Artifact: causal_language_model::CC_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::CC_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: description
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How the model is built, including the amount of text it can read at once
    - Artifact: causal_language_model::CC_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The training fingerprint, the provider's claim
    - Artifact: causal_language_model::CC_REGISTER_MODEL_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: model_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The model's record, registered
    - Artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: time_in_service_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time in service's identity, claimed once at placement
    - Artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: ceiling
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most sensitive kind of information the model may read
    - Artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: system_prompt
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The business's standing instructions to the model for its time in service
    - Artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: response_rules
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response
    - Artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: time_in_service
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time in service opened
    - Artifact: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: model_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The model's record as it stood before withdrawal
    - Artifact: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::CC_ADMIT_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: model_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The record of the model the user prompt names, in service
    - Artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: time_in_service_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time in service's identity, claimed once at placement
    - Artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: kind
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most sensitive kind of information the question and its material contain
    - Artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: time_in_service
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The model's open time in service, with its ceiling, system prompt and response rules
    - Artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: system_prompt
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The business's standing instructions to the model for its time in service
    - Artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: question
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the requester asks on the customer's behalf
    - Artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: supporting_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Material carried with the question for the model to read
    - Artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading_capacity
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many words the model can read at once; words, not a real model's tokens
    - Artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: reading
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Exactly what the model reads
    - Artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: reading_length
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How long what the model reads is, in words
    - Artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: response_rules
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response
    - Artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: account_numbers
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer's own account numbers, from the business's existing records
    - Artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: seed
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The seed each adventurous word choice is drawn from
    - Artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Exactly what the model read, when it read anything
    - Artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: rules_in_force
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response rules in force for this user prompt, with its seed
    - Artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: written_response
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response as written, whether it finished, the rule that stopped it and the words stopped
    - Artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: release_facts
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The facts of the written response one release condition reads
    - Artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: release_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The release condition, as a rule over those facts
    - Artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: releasable
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the condition for release holds
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The user prompt's identity, named by the requester and claimed once
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: requester_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The requester who submits the user prompt
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: customer_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer the user prompt is for
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: kind
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most sensitive kind of information the question and its material contain
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: question
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the requester asks on the customer's behalf
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: supporting_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Material carried with the question for the model to read
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: outcome
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: RESPONDED, REFUSED or FAILED
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: time_in_service_id
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The time in service's identity, claimed once at placement
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading
      Type: object
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Exactly what the model read, when it read anything
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: rules_in_force
      Type: object
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The response rules in force, when the model wrote
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: response
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The model response released
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reason
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Why the user prompt was refused, or where it failed
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: record_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The identity of the appended user prompt record
    - Artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: sequence_number
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The record's position in the user prompt records
    - Artifact: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The user prompt's identity, named by the requester and claimed once
    - Artifact: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: user_prompt_record
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The record of the user prompt
    - Artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The account of the performed operation
    - Artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the operation trail
    - Artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: operation
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The operation performed
    - Artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: record_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The identity of the appended trail entry
    - Artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: sequence_number
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The entry's position in the trail
    - Artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: description
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How the model is built, including the amount of text it can read at once
    - Artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: fingerprint
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The training fingerprint, the provider's claim
    - Artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: kind
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The kind of information stated
    - Artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: ceiling
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The most sensitive kind of information the model may read
    - Artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: kinds
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The declared kinds, least sensitive first
    - Artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: within_ceiling
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the kind is no more sensitive than the ceiling
    - Artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: system_prompt
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The business's standing instructions to the model for its time in service
    - Artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: question
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the requester asks on the customer's behalf
    - Artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: supporting_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Material carried with the question for the model to read
    - Artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading_capacity
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many words the model can read at once; words, not a real model's tokens
    - Artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: reading
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Exactly what the model reads
    - Artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: reading_length
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How long it is, in words
    - Artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: response_rules
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response
    - Artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: account_numbers
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The customer's own account numbers, from the business's existing records
    - Artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: seed
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The seed each adventurous word choice is drawn from
    - Artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: rules_in_force
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The forbidden rules, the freedom of word choice and the seed in force
    - Artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: positions
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: One position per word up to the longest response
    - Artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Exactly what the model reads
    - Artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: text
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response so far
    - Artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: finished
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the response has finished, in which case no word is offered
    - Artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: stopped_by
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rule that stopped the response, in which case no word is offered
    - Artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: candidates
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The words the model offers next, each with its likelihood
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: candidates
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The words offered, each with its likelihood
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: rules_in_force
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response rules in force
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: position
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Which word this is
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: text
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response so far
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: finished
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the response has finished
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: stopped_by
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rule that left no permitted word, or none
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: stopped
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The words stopped so far, each with its position and rule
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: text
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response so far, with the chosen word
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: finished
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the chosen word ends the response
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: stopped_by
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rule that left no permitted word, or none
    - Artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: stopped
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The words stopped so far, with those stopped this pass
    - Artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Exactly what the model reads
    - Artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: rules_in_force
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response rules in force
    - Artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: position
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Which word this is
    - Artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: text
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response so far
    - Artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: finished
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the response has finished
    - Artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: stopped_by
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rule that left no permitted word, or none
    - Artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: stopped
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The words stopped so far
    - Artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response so far, whether it finished, the rule that stopped it and the words stopped
    - Artifact: causal_language_model::CT_WRITE_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: reading
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Exactly what the model reads
    - Artifact: causal_language_model::CT_WRITE_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: rules_in_force
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response rules in force
    - Artifact: causal_language_model::CT_WRITE_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: positions
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: One position per word up to the longest response
    - Artifact: causal_language_model::CT_WRITE_RESPONSE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The response as written, whether it finished, the rule that stopped it and the words stopped
    - Artifact: causal_language_model::EV_MODEL_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::EV_MODEL_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the operation trail
    - Artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: time_in_service_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time in service's identity, claimed once at placement
    - Artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the operation trail
    - Artifact: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the operation trail
    - Artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The user prompt's identity, named by the requester and claimed once
    - Artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: requester_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The requester who submits the user prompt
    - Artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: user_prompt_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The user prompt's identity, named by the requester and claimed once
    - Artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a model's description and fingerprint
    - Artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: requester_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The requester who submits the user prompt
    - Artifact: causal_language_model::AC_MODEL_STAFF_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member's identity as the business knows it
    - Artifact: causal_language_model::AC_MODEL_STAFF_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: authorized
      Type: boolean
      Required (YES, NO): 'NO'
      Default: 'false'
      Meaning: Whether the staff member is model staff; decided by the business's existing arrangements, read here
    - Artifact: causal_language_model::AC_REQUESTER_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: requester_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The requester's identity as the business knows it
    - Artifact: causal_language_model::AC_REQUESTER_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: permitted_customers
      Type: array
      Required (YES, NO): 'NO'
      Default: '[]'
      Meaning: The customers the requester may act for; decided by the business's existing arrangements, read here
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
    - CT Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_form_model_identity_key_v0
      Callable: execute
      Operation: FORM_MODEL_IDENTITY_KEY
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): never
      Source Finding: S7 new_artifacts CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_compare_sensitivity_v0
      Callable: execute
      Operation: COMPARE_SENSITIVITY
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: S7 new_artifacts CT_PURE_COMPARE_SENSITIVITY_V0
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_assemble_model_reading_v0
      Callable: execute
      Operation: ASSEMBLE_MODEL_READING
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: S7 new_artifacts CT_PURE_ASSEMBLE_MODEL_READING_V0
    - CT Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_form_response_rules_v0
      Callable: execute
      Operation: FORM_RESPONSE_RULES
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): never
      Source Finding: S7 new_artifacts CT_PURE_FORM_RESPONSE_RULES_V0
    - CT Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Module: causal_language_model.implementation.capability_transforms.atoms.ct_impure_offer_next_words_v0
      Callable: execute
      Operation: OFFER_NEXT_WORDS
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_impure
      Refusal (raises, returns, never): never
      Source Finding: S7 new_artifacts CT_IMPURE_OFFER_NEXT_WORDS_V0
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_choose_permitted_word_v0
      Callable: execute
      Operation: CHOOSE_PERMITTED_WORD
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): returns
      Source Finding: S7 new_artifacts CT_PURE_CHOOSE_PERMITTED_WORD_V0
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Module: ''
      Callable: ''
      Operation: WRITE_NEXT_WORD
      Kind (atom, molecule): molecule
      Purity (ct_pure, ct_impure): ct_impure
      Refusal (raises, returns, never): returns
      Source Finding: S7 new_artifacts CT_WRITE_NEXT_WORD_V0
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Module: ''
      Callable: ''
      Operation: WRITE_RESPONSE
      Kind (atom, molecule): molecule
      Purity (ct_pure, ct_impure): ct_impure
      Refusal (raises, returns, never): returns
      Source Finding: S7 new_artifacts CT_WRITE_RESPONSE_V0
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
    - Vocabulary Code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
      Extends: NONE
      Group: kind_of_information
      Casing: lower_snake
      Value: public
      Meaning: The least sensitive kind
      Source Finding: S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0
    - Vocabulary Code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
      Extends: NONE
      Group: kind_of_information
      Casing: lower_snake
      Value: internal
      Meaning: More sensitive than public
      Source Finding: S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0
    - Vocabulary Code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
      Extends: NONE
      Group: kind_of_information
      Casing: lower_snake
      Value: confidential
      Meaning: More sensitive than internal
      Source Finding: S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0
    - Vocabulary Code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
      Extends: NONE
      Group: kind_of_information
      Casing: lower_snake
      Value: restricted
      Meaning: The most sensitive kind
      Source Finding: S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows:
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Key: structure
      Value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S7 rb_declarations RB_MODEL_RESPONSE_BINDINGS_V0
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Capability: capability_side_effects::CS_REGISTRY_V0
      Key: structure
      Value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S7 rb_declarations RB_MODEL_RESPONSE_BINDINGS_V0
    - RB Code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Key: structure
      Value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Source Finding: S7 rb_declarations RB_MODEL_RESPONSE_BINDINGS_V0
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: causal_language_model::AC_MODEL_STAFF_V0
      Property: type
      Value: ENDUSER
      Source Finding: S5 provisional_codes AC_MODEL_STAFF_V0
    - Artifact: causal_language_model::AC_REQUESTER_V0
      Property: type
      Value: ENDUSER
      Source Finding: S5 provisional_codes AC_REQUESTER_V0
    - Artifact: causal_language_model::WF_REGISTER_MODEL_V0
      Property: emit.EXIT_REGISTERED
      Value: causal_language_model::EV_MODEL_REGISTERED_V0
      Source Finding: S4 gap_register GAP-20
    - Artifact: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Property: emit.EXIT_PLACED
      Value: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
      Source Finding: S4 gap_register GAP-20
    - Artifact: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Property: emit.EXIT_WITHDRAWN
      Value: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
      Source Finding: S4 gap_register GAP-20
    - Artifact: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Property: emit.EXIT_RESPONDED
      Value: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
      Source Finding: S4 gap_register GAP-20
    - Artifact: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Property: emit.EXIT_REFUSED
      Value: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Source Finding: S4 gap_register GAP-20
    - Artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
      Property: moment
      Value: refusal
      Source Finding: S0 business_events User Prompt Refused
    - Artifact: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
      Property: layer
      Value: DOMAINS
      Source Finding: S5 provisional_codes STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: MODELS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_MUTABLE_JSON_V0
      Proposed Path: causal_language_model/model_response/models.json
      Used By: causal_language_model::CC_REGISTER_MODEL_V0
      Source Finding: S6 storage_governance A durable record of every model the business holds
    - Store Name: MODEL_IDENTITY_REGISTRY
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: causal_language_model/model_response/model_identity_registry.jsonl
      Used By: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Source Finding: S6 storage_governance A claim on each model's identity, held once
    - Store Name: TIME_IN_SERVICE_REGISTRY
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: causal_language_model/model_response/time_in_service_registry.jsonl
      Used By: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Source Finding: S6 storage_governance A claim on each time in service's identity, held once
    - Store Name: USER_PROMPT_REGISTRY
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: causal_language_model/model_response/user_prompt_registry.jsonl
      Used By: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
      Source Finding: S6 storage_governance A claim on each user prompt's identity, held once
    - Store Name: TIMES_IN_SERVICE
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_MUTABLE_JSON_V0
      Proposed Path: causal_language_model/model_response/times_in_service.json
      Used By: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Source Finding: S6 storage_governance A durable record of every time in service
    - Store Name: USER_PROMPT_RECORDS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_APPENDONLY_JSONL_V0
      Proposed Path: causal_language_model/model_response/user_prompt_records.jsonl
      Used By: causal_language_model::CC_RECORD_USER_PROMPT_V0
      Source Finding: S6 storage_governance A record of every user prompt that cannot be amended
    - Store Name: MODEL_OPERATIONS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_APPENDONLY_JSONL_V0
      Proposed Path: causal_language_model/model_response/model_operations.jsonl
      Used By: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
      Source Finding: S6 storage_governance A trail of performed operations that cannot be amended
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
      Count: '43'
      Artifacts: 2 AC, 5 IN, 5 WF, 15 CC, 8 CT, 5 EV, 1 VOCAB, 1 RB, 1 STRUCTURE
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
    - Operation: Register a model
      Refused When: Its description and fingerprint match a registered model.
      Act: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
      Outcome: ALREADY_EXISTS
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Place a model in service
      Refused When: The model is not registered.
      Act: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Outcome: NOT_FOUND
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Place a model in service
      Refused When: The model is already in service.
      Act: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #3'
    - Operation: Withdraw a model from service
      Refused When: The model is not in service.
      Act: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #4'
    - Operation: Withdraw a model from service
      Refused When: The model is not in service.
      Act: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      Outcome: NOT_FOUND
      Source Finding: 'S0 operation_refusals #4'
    - Operation: Submit a user prompt
      Refused When: The model is not registered.
      Act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_REGISTERED
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #5'
    - Operation: Submit a user prompt
      Refused When: The model is not in service.
      Act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_IN_SERVICE
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #6'
    - Operation: Submit a user prompt
      Refused When: The user prompt contains a more sensitive kind of information than the model may read.
      Act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_ABOVE_CEILING
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Submit a user prompt
      Refused When: What the model would read is longer than the model can read at once.
      Act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_TOO_LONG_TO_READ
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #8'
    - Operation: Submit a user prompt
      Refused When: The requester is not permitted to act for the customer.
      Act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_NOT_PERMITTED
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #9'
    - Operation: Submit a user prompt
      Refused When: The model cannot finish a response without breaking a response rule.
      Act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_BY_RULE
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #10'
    - Operation: Submit a user prompt
      Refused When: The response reaches the longest response before it is finished.
      Act: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
      Step: RECORD_REFUSED_UNFINISHED
      Outcome: SUCCESS
      Source Finding: 'S0 operation_refusals #11'
    - Operation: Register a model, place in service, withdraw, retrieve a record
      Refused When: The staff member is not authorized model staff.
      Act: causal_language_model::WF_REGISTER_MODEL_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #12'
    - Operation: Register a model, place in service, withdraw, retrieve a record
      Refused When: The staff member is not authorized model staff.
      Act: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #12'
    - Operation: Register a model, place in service, withdraw, retrieve a record
      Refused When: The staff member is not authorized model staff.
      Act: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #12'
    - Operation: Register a model, place in service, withdraw, retrieve a record
      Refused When: The staff member is not authorized model staff.
      Act: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
      Step: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #12'
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
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: offered
      Kind (atom, molecule, loop): atom
      Target: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Over: —
      Iterator: —
      Emits: —
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: chosen
      Kind (atom, molecule, loop): atom
      Target: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Over: —
      Iterator: —
      Emits: result
      Source Finding: 'S4 design_decisions #3'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Kind (atom, molecule, loop): loop
      Target: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Over: inputs.positions
      Iterator: position
      Emits: result
      Source Finding: 'S4 design_decisions #2'
  molecule_step_bindings:
    columns:
    - CT Code
    - Step
    - Role (INPUT, CARRY, UPDATE)
    - Field
    - Bound To
    - Source Finding
    rows:
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: offered
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: reading
      Bound To: inputs.reading
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: offered
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: text
      Bound To: inputs.text
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: offered
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: finished
      Bound To: inputs.finished
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: offered
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: stopped_by
      Bound To: inputs.stopped_by
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: chosen
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: candidates
      Bound To: results.offered.candidates
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: chosen
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: rules_in_force
      Bound To: inputs.rules_in_force
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: chosen
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: position
      Bound To: inputs.position
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: chosen
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: text
      Bound To: inputs.text
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: chosen
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: finished
      Bound To: inputs.finished
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: chosen
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: stopped_by
      Bound To: inputs.stopped_by
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Step: chosen
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: stopped
      Bound To: inputs.stopped
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): CARRY
      Field: text
      Bound To: '""'
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): CARRY
      Field: finished
      Bound To: 'false'
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): CARRY
      Field: stopped_by
      Bound To: none
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): CARRY
      Field: stopped
      Bound To: '[]'
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: position
      Bound To: iterator
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: reading
      Bound To: inputs.reading
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: rules_in_force
      Bound To: inputs.rules_in_force
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: text
      Bound To: accumulator.text
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: finished
      Bound To: accumulator.finished
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: stopped_by
      Bound To: accumulator.stopped_by
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): INPUT
      Field: stopped
      Bound To: accumulator.stopped
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): UPDATE
      Field: text
      Bound To: results.text
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): UPDATE
      Field: finished
      Bound To: results.finished
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): UPDATE
      Field: stopped_by
      Bound To: results.stopped_by
      Source Finding: 'S4 design_decisions #2'
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Step: written
      Role (INPUT, CARRY, UPDATE): UPDATE
      Field: stopped
      Bound To: results.stopped
      Source Finding: 'S4 design_decisions #2'
  test_cases:
    columns:
    - CT Code
    - Case
    - Expected Outcome (SUCCESS, VIOLATION)
    - Source Finding
    rows:
    - CT Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Case: forms_key_from_description_and_fingerprint
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Case: refuses_blank_fingerprint
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: admits_kind_within_ceiling
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: refuses_kind_above_ceiling
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: assembles_what_fits
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: refuses_reading_too_long
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Case: adds_the_account_rule_and_positions
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Case: offers_candidates
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: stops_unfinished_at_the_longest_response
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
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
    - CT Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Case: forms_key_from_description_and_fingerprint
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: description
      Value: '{reading_capacity: 64, layers: 2}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Case: forms_key_from_description_and_fingerprint
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: fingerprint
      Value: sha256:ab12
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Case: forms_key_from_description_and_fingerprint
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: identity_key
      Value: '''{"layers":2,"reading_capacity":64}|sha256:ab12'''
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Case: refuses_blank_fingerprint
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: description
      Value: '{reading_capacity: 64, layers: 2}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
      Case: refuses_blank_fingerprint
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: fingerprint
      Value: '" "'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: admits_kind_within_ceiling
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: kind
      Value: internal
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: admits_kind_within_ceiling
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: ceiling
      Value: confidential
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: admits_kind_within_ceiling
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: kinds
      Value: '[public, internal, confidential, restricted]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: admits_kind_within_ceiling
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: within_ceiling
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: refuses_kind_above_ceiling
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: kind
      Value: restricted
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: refuses_kind_above_ceiling
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: ceiling
      Value: internal
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
      Case: refuses_kind_above_ceiling
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: kinds
      Value: '[public, internal, confidential, restricted]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: assembles_what_fits
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: system_prompt
      Value: Answer briefly.
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: assembles_what_fits
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: question
      Value: What is my balance?
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: assembles_what_fits
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: supporting_material
      Value: Account 12345678 balance 40.
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: assembles_what_fits
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: reading_capacity
      Value: '20'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: assembles_what_fits
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: reading
      Value: '{system_prompt: ''Answer briefly.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40.''}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: assembles_what_fits
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: reading_length
      Value: '10'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: refuses_reading_too_long
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: system_prompt
      Value: Answer briefly.
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: refuses_reading_too_long
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: question
      Value: What is my balance?
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: refuses_reading_too_long
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: supporting_material
      Value: Account 12345678 balance 40.
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
      Case: refuses_reading_too_long
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: reading_capacity
      Value: '5'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Case: adds_the_account_rule_and_positions
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: response_rules
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}], account_number_pattern: ''[0-9](?:[ -]?[0-9]){7}'', freedom: 0, longest_response: 3}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Case: adds_the_account_rule_and_positions
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: account_numbers
      Value: '[''12345678'']'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Case: adds_the_account_rule_and_positions
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: seed
      Value: '7'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Case: adds_the_account_rule_and_positions
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
      Case: adds_the_account_rule_and_positions
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: positions
      Value: '[1, 2, 3]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Case: offers_candidates
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: reading
      Value: '{system_prompt: ''Answer briefly.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40.''}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Case: offers_candidates
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: text
      Value: '""'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Case: offers_candidates
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Case: offers_candidates
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
      Case: offers_candidates
      Role (INPUT, EXPECTED, ASSERT, RECORDED): ASSERT
      Field: candidates
      Value: '{mode: property, type: non_zero}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{word: ''87654321'', likelihood: 0.6}, {word: Your, likelihood: 0.3}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: position
      Value: '1'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: text
      Value: '""'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Your
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_another_customers_account_and_continues
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped
      Value: '[{position: 1, word: ''87654321'', rule: another_customers_account_number}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{word: ''4321'', likelihood: 0.7}, {word: is, likelihood: 0.2}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: position
      Value: '3'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: text
      Value: Account 8765
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Account 8765 is
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: stops_an_account_number_written_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped
      Value: '[{position: 3, word: ''4321'', rule: another_customers_account_number}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{word: ''5678'', likelihood: 0.8}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: position
      Value: '3'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: text
      Value: Account 1234
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Account 1234 5678
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: writes_the_customers_own_account_across_two_words
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{word: ''87654321'', likelihood: 0.9}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: position
      Value: '1'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: text
      Value: '""'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: '""'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: another_customers_account_number
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: names_the_rule_when_no_permitted_word_remains
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped
      Value: '[{position: 1, word: ''87654321'', rule: another_customers_account_number}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{word: balance, likelihood: 0.6}, {word: savings, likelihood: 0.3}, {word: loan, likelihood: 0.1}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 1, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: position
      Value: '2'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: text
      Value: Your
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Your savings
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: draws_an_adventurous_word_from_the_seed
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: candidates
      Value: '[{word: <end>, likelihood: 0.9}]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: position
      Value: '3'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: text
      Value: Your balance
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: text
      Value: Your balance
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: finished
      Value: 'true'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
      Case: finishes_on_the_end_of_the_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: reading
      Value: '{system_prompt: ''Answer briefly.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40.''}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: position
      Value: '1'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: text
      Value: '""'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: finished
      Value: 'false'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped_by
      Value: none
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: stopped
      Value: '[]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): RECORDED
      Field: offered
      Value: '{candidates: [{word: ''87654321'', likelihood: 0.6}, {word: Your, likelihood: 0.3}]}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_NEXT_WORD_V0
      Case: writes_one_permitted_word_from_a_recorded_offer
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: result
      Value: '{text: Your, finished: false, stopped_by: none, stopped: [{position: 1, word: ''87654321'', rule: another_customers_account_number}]}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: reading
      Value: '{system_prompt: ''Answer briefly.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40.''}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: positions
      Value: '[1, 2, 3, 4]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Role (INPUT, EXPECTED, ASSERT, RECORDED): RECORDED
      Field: written[0]/offered
      Value: '{candidates: [{word: ''87654321'', likelihood: 0.6}, {word: Your, likelihood: 0.3}]}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Role (INPUT, EXPECTED, ASSERT, RECORDED): RECORDED
      Field: written[1]/offered
      Value: '{candidates: [{word: balance, likelihood: 0.9}]}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Role (INPUT, EXPECTED, ASSERT, RECORDED): RECORDED
      Field: written[2]/offered
      Value: '{candidates: [{word: <end>, likelihood: 0.9}]}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Role (INPUT, EXPECTED, ASSERT, RECORDED): RECORDED
      Field: written[3]/offered
      Value: '{candidates: []}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: writes_a_finished_response_and_offers_nothing_after
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: result
      Value: '{text: Your balance, finished: true, stopped_by: none, stopped: [{position: 1, word: ''87654321'', rule: another_customers_account_number}]}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: stops_unfinished_at_the_longest_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: reading
      Value: '{system_prompt: ''Answer briefly.'', question: ''What is my balance?'', supporting_material: ''Account 12345678 balance 40.''}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: stops_unfinished_at_the_longest_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: rules_in_force
      Value: '{forbidden: [{rule: no_guarantees, pattern: ''\bguaranteed\b''}, {rule: another_customers_account_number, pattern: ''[0-9](?:[ -]?[0-9]){7}'', except: [''12345678'']}], freedom: 0, seed: 7}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: stops_unfinished_at_the_longest_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: positions
      Value: '[1]'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: stops_unfinished_at_the_longest_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): RECORDED
      Field: written[0]/offered
      Value: '{candidates: [{word: Your, likelihood: 0.9}]}'
      Source Finding: human decision
    - CT Code: causal_language_model::CT_WRITE_RESPONSE_V0
      Case: stops_unfinished_at_the_longest_response
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: result
      Value: '{text: Your, finished: false, stopped_by: none, stopped: []}'
      Source Finding: human decision
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows: []
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
