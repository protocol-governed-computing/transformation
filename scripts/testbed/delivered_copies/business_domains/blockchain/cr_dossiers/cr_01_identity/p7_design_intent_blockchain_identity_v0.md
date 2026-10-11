# Stage 7 — Design Intent: blockchain / identity

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_01_identity
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
    - Decision: The trail rests on the append-only capability
      Business Fact: An occurrence that has happened cannot be un-happened
      Resolution: ACTOR_OCCURRENCES is typed CS_APPENDONLY_JSONL_V0, which offers no update and no delete
      Source Finding: 'S4 design_decisions #1'
    - Decision: An actor's state is held as a value
      Business Fact: The refusal that an actor is decided about once needs the state at the moment of deciding
      Resolution: ACTORS is typed CS_MUTABLE_JSON_V0 and read by blockchain::CC_RESOLVE_ACTOR_V0 before any decision is recorded
      Source Finding: 'S4 design_decisions #2'
    - Decision: The contact address is the identifier
      Business Fact: Two registrations carrying the same address are the same person
      Resolution: CONTACT_ADDRESS_REGISTRY is typed CS_REGISTRY_V0 and keyed on the address as supplied; no identifier is generated
      Source Finding: 'S4 design_decisions #3'
    - Decision: Acceptance and rejection are two occurrences
      Business Fact: A rejected actor must never be readable as accepted
      Resolution: blockchain::EV_ACTOR_ACCEPTED_V0 and blockchain::EV_ACTOR_REJECTED_V0 are separate artifacts; no artifact carries an outcome field
      Source Finding: 'S4 design_decisions #4'
    - Decision: The time capability is a substrate gap
      Business Fact: Every occurrence carries the time it actually happened, determined as it occurs
      Resolution: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 reads capability_side_effects::CS_CLOCK_V0 before it assembles the record, so occurred_at is determined where the occurrence is recorded and no caller may assert it
      Source Finding: 'S4 design_decisions #5'
    - Decision: The authority is recorded and never resolved
      Business Fact: An authority is identified outside this function
      Resolution: The decision carries verifying_authority as a value; no store holds authorities and no step resolves one
      Source Finding: 'S4 design_decisions #6'
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
      Summary: Appends a record to a named stream and reads the stream whole
      Reason: Holds the occurrence trail; offers no update and no delete
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_APPENDONLY_JSONL_V0
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Keyed JSON state with read, write and select
      Reason: Holds the actor record and its state
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_MUTABLE_JSON_V0
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Registers, resolves and reports a key
      Reason: Claims the contact address and reports one already held
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_REGISTRY_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Reads a record for required fields and their form
      Reason: Reads a registration for absence and malformation
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Reads a value against a declared admitted set
      Reason: Reads the decision outcome and the state a decision is admitted from
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    - FQDN: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Compares two supplied values
      Reason: Compares the authority named against the actor decided about
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Assembles a record from supplied fields
      Reason: Assembles the actor record and each occurrence record
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - FQDN: capability_side_effects::CS_CLOCK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Answers the current instant
      Reason: Determines the time an occurrence happened, which no transform can
      Source Finding: S4 dependency_graph the substrate capability supplying the current time
    - FQDN: capability_transforms::CT_PURE_EXTRACT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Extracts a named value from a supplied structure
      Reason: Extracts the address and the decision fields
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_EXTRACT_V0
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: Declare the actors of this business
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): AC
      Code: blockchain::AC_PARTICIPANT_V0
      Summary: The ordinary participant who registers themselves and is decided about
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes AC_PARTICIPANT_V0
    - Capability: Declare the stores identity owns
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): STRUCTURE
      Code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Summary: Declares the three stores identity owns and the paths they occupy
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes STRUCTURE_IDENTITY_STORAGE_V0
    - Capability: Bind identity's workflows to the stores they use
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): RB
      Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Summary: Binds identity's workflows to the side effects and storage they use
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes RB_IDENTITY_BINDINGS_V0
    - Capability: Recognise the moments an actor is registered, accepted and rejected
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Summary: The moment a person is admitted and trusted with nothing
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes EV_ACTOR_REGISTERED_UNVERIFIED_V0
    - Capability: Recognise the moments an actor is registered, accepted and rejected
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: blockchain::EV_ACTOR_ACCEPTED_V0
      Summary: The moment an authority records a decision to trust an actor
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes EV_ACTOR_ACCEPTED_V0
    - Capability: Recognise the moments an actor is registered, accepted and rejected
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: blockchain::EV_ACTOR_REJECTED_V0
      Summary: The moment an authority records a decision not to trust an actor
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes EV_ACTOR_REJECTED_V0
    - Capability: Admit a request to register a person
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: blockchain::IN_ACTOR_REGISTERED_V0
      Summary: A request to admit a person as an actor
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes IN_ACTOR_REGISTERED_V0
    - Capability: Admit a request to record a verification decision
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: blockchain::IN_ACTOR_VERIFIED_V0
      Summary: A request to record a decision, carrying the authority, the outcome and the grounds
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes IN_ACTOR_VERIFIED_V0
    - Capability: Admit a person's registration and record them unverified
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: blockchain::WF_REGISTER_ACTOR_V0
      Summary: The governed sequence that admits a person as an unverified actor
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes WF_REGISTER_ACTOR_V0
    - Capability: Record an authority's decision against a registered actor
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Summary: The governed sequence that records a decision against a registered actor
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes WF_RECORD_VERIFICATION_DECISION_V0
    - Capability: Admit a person's registration and record them unverified
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Summary: Confirms a registration carries a name and an address of the form asked for
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes CC_VALIDATE_REGISTRATION_V0
    - Capability: Admit a person's registration and record them unverified
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Summary: Claims a contact address so that two registrations of one person do not produce two actors
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes CC_CLAIM_CONTACT_ADDRESS_V0
    - Capability: Admit a person's registration and record them unverified
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: blockchain::CC_REGISTER_ACTOR_V0
      Summary: Writes the actor unverified after its address is claimed
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes CC_REGISTER_ACTOR_V0
    - Capability: Record an authority's decision against a registered actor
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: blockchain::CC_RESOLVE_ACTOR_V0
      Summary: Answers which actor a contact address denotes, and reports when none does
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes CC_RESOLVE_ACTOR_V0
    - Capability: Record an authority's decision against a registered actor
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Summary: Refuses every declared refusal and moves the actor to its decided state
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes CC_RECORD_VERIFICATION_DECISION_V0
    - Capability: Record an acceptance and a rejection
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Summary: Appends one occurrence to the trail
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes CC_APPEND_ACTOR_OCCURRENCE_V0
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_REGISTER_ACTOR_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: S6 storage_governance An atomic claim on each contact address
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every person the business knows, carrying whether it has accepted them
  execution_topology:
    columns:
    - Workflow
    - Node
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::IN_ACTOR_REGISTERED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_VALIDATE_REGISTRATION_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_ACTOR_REGISTERED_V0
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_VALIDATE_REGISTRATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_CLAIM_CONTACT_ADDRESS_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_VALIDATE_REGISTRATION_V0
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_REGISTER_ACTOR_V0; ALREADY_EXISTS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_CONTACT_ADDRESS_V0
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_REGISTER_ACTOR_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_REGISTER_ACTOR_V0
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_ACTOR_OCCURRENCE_V0
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 new_artifacts WF_REGISTER_ACTOR_V0
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: EXIT_SUCCESS
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 new_artifacts WF_REGISTER_ACTOR_V0
    - Workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Node: blockchain::IN_ACTOR_VERIFIED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_ACTOR_VERIFIED_V0
    - Workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RESOLVE_ACTOR_V0
    - Workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RECORD_VERIFICATION_DECISION_V0
    - Workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_ACTOR_OCCURRENCE_V0
    - Workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 new_artifacts WF_RECORD_VERIFICATION_DECISION_V0
    - Workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Node: EXIT_SUCCESS
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 new_artifacts WF_RECORD_VERIFICATION_DECISION_V0
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
    - CC Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: '1'
      Step Name: read_registration
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: record, schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=record, schema=schema; out: violations=violations'
    - CC Code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: '1'
      Step Name: extract_address
      Capability: capability_transforms::CT_PURE_EXTRACT_V0
      Kind (CT, CS): CT
      Operation: EXTRACT
      Store: —
      Consumes: from, path, type
      Produces: result
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: from=from, path=path, type=type; out: result=result'
    - CC Code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: '2'
      Step Name: claim_address
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: CONTACT_ADDRESS_REGISTRY
      Consumes: key, target_cs, target_ref
      Produces: address
      Routing: SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: ALREADY_EXISTS
      Interface: —
    - CC Code: blockchain::CC_REGISTER_ACTOR_V0
      Step: '1'
      Step Name: assemble_actor
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: fields
      Produces: record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=fields; out: record=record'
    - CC Code: blockchain::CC_REGISTER_ACTOR_V0
      Step: '2'
      Step Name: write_actor
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: ACTORS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: blockchain::CC_RESOLVE_ACTOR_V0
      Step: '1'
      Step Name: resolve_address
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: RESOLVE
      Store: CONTACT_ADDRESS_REGISTRY
      Consumes: key_or_address
      Produces: target_ref
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: blockchain::CC_RESOLVE_ACTOR_V0
      Step: '2'
      Step Name: read_actor
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: ACTORS
      Consumes: key
      Produces: value
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '1'
      Step Name: read_state_admits_decision
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: value, allowed_set
      Produces: is_member
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=value, allowed_set=allowed_set; out: is_member=is_member'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '2'
      Step Name: read_outcome_admitted
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: value, allowed_set
      Produces: is_member
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=value, allowed_set=allowed_set; out: is_member=is_member'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '3'
      Step Name: refuse_self_verification
      Capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
      Kind (CT, CS): CT
      Operation: COMPARE_EQUAL
      Store: —
      Consumes: left, right
      Produces: is_equal
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: left=left, right=right; out: is_equal=is_equal'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '4'
      Step Name: assemble_decided_actor
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: fields
      Produces: record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=fields; out: record=record'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '5'
      Step Name: write_decided_actor
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: ACTORS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: '1'
      Step Name: read_now
      Capability: capability_side_effects::CS_CLOCK_V0
      Kind (CT, CS): CS
      Operation: NOW
      Store: —
      Consumes: —
      Produces: timestamp
      Routing: SUCCESS -> continue; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: '2'
      Step Name: assemble_occurrence
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: fields
      Produces: record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=fields; out: record=record'
    - CC Code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: '3'
      Step Name: append_occurrence
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Kind (CT, CS): CS
      Operation: APPEND
      Store: ACTOR_OCCURRENCES
      Consumes: record, stream_id, actor_id
      Produces: sequence_number
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
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
    - Owner: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: read_registration
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.actor_record
      Source Finding: S7 cc_composition read_registration
    - Owner: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: read_registration
      Direction (INPUT, OUTPUT): INPUT
      Field: schema
      Bound To: inputs.registration_schema
      Source Finding: S7 cc_composition read_registration
    - Owner: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: read_registration
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition read_registration
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: extract_address
      Direction (INPUT, OUTPUT): INPUT
      Field: from
      Bound To: inputs.actor_record
      Source Finding: S7 cc_composition extract_address
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: extract_address
      Direction (INPUT, OUTPUT): INPUT
      Field: path
      Bound To: inputs.address_path
      Source Finding: S7 cc_composition extract_address
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: extract_address
      Direction (INPUT, OUTPUT): INPUT
      Field: type
      Bound To: inputs.address_type
      Source Finding: S7 cc_composition extract_address
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: extract_address
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result
      Bound To: capability_result.result
      Source Finding: S7 cc_composition extract_address
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: claim_address
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: results.extract_address.result
      Source Finding: S7 cc_composition claim_address
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: claim_address
      Direction (INPUT, OUTPUT): INPUT
      Field: target_cs
      Bound To: CS_MUTABLE_JSON_V0
      Source Finding: S7 cc_composition claim_address
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: claim_address
      Direction (INPUT, OUTPUT): INPUT
      Field: target_ref
      Bound To: ACTORS
      Source Finding: S7 cc_composition claim_address
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: claim_address
      Direction (INPUT, OUTPUT): OUTPUT
      Field: address
      Bound To: capability_result.address
      Source Finding: S7 cc_composition claim_address
    - Owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Step: claim_address
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition claim_address
    - Owner: blockchain::CC_REGISTER_ACTOR_V0
      Step: assemble_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: inputs.actor_fields
      Source Finding: S7 cc_composition assemble_actor
    - Owner: blockchain::CC_REGISTER_ACTOR_V0
      Step: assemble_actor
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_actor
    - Owner: blockchain::CC_REGISTER_ACTOR_V0
      Step: write_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition write_actor
    - Owner: blockchain::CC_REGISTER_ACTOR_V0
      Step: write_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_actor.record
      Source Finding: S7 cc_composition write_actor
    - Owner: blockchain::CC_REGISTER_ACTOR_V0
      Step: write_actor
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_actor
    - Owner: blockchain::CC_RESOLVE_ACTOR_V0
      Step: resolve_address
      Direction (INPUT, OUTPUT): INPUT
      Field: key_or_address
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition resolve_address
    - Owner: blockchain::CC_RESOLVE_ACTOR_V0
      Step: resolve_address
      Direction (INPUT, OUTPUT): OUTPUT
      Field: target_ref
      Bound To: capability_result.target_ref
      Source Finding: S7 cc_composition resolve_address
    - Owner: blockchain::CC_RESOLVE_ACTOR_V0
      Step: read_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition read_actor
    - Owner: blockchain::CC_RESOLVE_ACTOR_V0
      Step: read_actor
      Direction (INPUT, OUTPUT): OUTPUT
      Field: value
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_actor
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: read_state_admits_decision
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: inputs.current_state
      Source Finding: S7 cc_composition read_state_admits_decision
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: read_state_admits_decision
      Direction (INPUT, OUTPUT): INPUT
      Field: allowed_set
      Bound To: inputs.states_admitting_a_decision
      Source Finding: S7 cc_composition read_state_admits_decision
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: read_state_admits_decision
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_member
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition read_state_admits_decision
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: read_outcome_admitted
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: inputs.decision
      Source Finding: S7 cc_composition read_outcome_admitted
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: read_outcome_admitted
      Direction (INPUT, OUTPUT): INPUT
      Field: allowed_set
      Bound To: inputs.admitted_outcomes
      Source Finding: S7 cc_composition read_outcome_admitted
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: read_outcome_admitted
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_member
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition read_outcome_admitted
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: refuse_self_verification
      Direction (INPUT, OUTPUT): INPUT
      Field: left
      Bound To: inputs.verifying_authority
      Source Finding: S7 cc_composition refuse_self_verification
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: refuse_self_verification
      Direction (INPUT, OUTPUT): INPUT
      Field: right
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition refuse_self_verification
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: refuse_self_verification
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_equal
      Bound To: capability_result.is_equal
      Source Finding: S7 cc_composition refuse_self_verification
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: assemble_decided_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: inputs.decided_actor_fields
      Source Finding: S7 cc_composition assemble_decided_actor
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: assemble_decided_actor
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_decided_actor
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: write_decided_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition write_decided_actor
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: write_decided_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_decided_actor.record
      Source Finding: S7 cc_composition write_decided_actor
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: write_decided_actor
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_decided_actor
    - Owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: read_now
      Direction (INPUT, OUTPUT): OUTPUT
      Field: timestamp
      Bound To: capability_result.timestamp
      Source Finding: S7 cc_composition read_now
    - Owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: assemble_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''occurrence'': ''$.inputs.occurrence_fields.occurrence'', ''contact_address'': ''$.inputs.contact_address'', ''verifying_authority'': ''$.inputs.occurrence_fields.verifying_authority'', ''grounds'': ''$.inputs.occurrence_fields.grounds'', ''occurred_at'': ''$.results.read_now.timestamp''}'
      Source Finding: S7 cc_composition assemble_occurrence
    - Owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: assemble_occurrence
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_occurrence
    - Owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: append_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: results.assemble_occurrence.record
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: append_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: inputs.stream_id
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: append_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_id
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Step: append_occurrence
      Direction (INPUT, OUTPUT): OUTPUT
      Field: sequence_number
      Bound To: capability_result.sequence_number
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_record
      Bound To: payload.actor_record
      Source Finding: S7 execution_topology CC_VALIDATE_REGISTRATION_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: registration_schema
      Bound To: payload.registration_schema
      Source Finding: S7 execution_topology CC_VALIDATE_REGISTRATION_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_record
      Bound To: payload.actor_record
      Source Finding: S7 execution_topology CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: address_path
      Bound To: payload.address_path
      Source Finding: S7 execution_topology CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: address_type
      Bound To: payload.address_type
      Source Finding: S7 execution_topology CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_fields
      Bound To: payload.actor_record
      Source Finding: S7 execution_topology CC_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      Source Finding: S7 execution_topology CC_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      Source Finding: S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology CC_RESOLVE_ACTOR_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: current_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: states_admitting_a_decision
      Bound To: payload.states_admitting_a_decision
      Source Finding: S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decision
      Bound To: payload.decision
      Source Finding: S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: admitted_outcomes
      Bound To: payload.admitted_outcomes
      Source Finding: S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: verifying_authority
      Bound To: payload.verifying_authority
      Source Finding: S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decided_actor_fields
      Bound To: payload.decided_actor_fields
      Source Finding: S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0
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
    - Artifact: blockchain::IN_ACTOR_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: actor_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The details the person supplies about themselves
    - Artifact: blockchain::IN_ACTOR_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: registration_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The schema the supplied details are read against for absence and form
    - Artifact: blockchain::IN_ACTOR_VERIFIED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The address naming the actor the decision is about
    - Artifact: blockchain::IN_ACTOR_VERIFIED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The authority making the decision, recorded and never resolved
    - Artifact: blockchain::IN_ACTOR_VERIFIED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: decision
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The outcome, which must be one of the two admitted values
    - Artifact: blockchain::IN_ACTOR_VERIFIED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The reason stated for the decision; required for a rejection
    - Artifact: blockchain::AC_PARTICIPANT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The address identifying the participant
    - Artifact: blockchain::AC_PARTICIPANT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: name
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the person is called, as they supplied it
    - Artifact: blockchain::AC_PARTICIPANT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: currency_preference
      Type: string
      Required (YES, NO): 'NO'
      Default: BACHI
      Meaning: The currency the person prefers to be quoted in
    - Artifact: blockchain::AC_PARTICIPANT_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: language
      Type: string
      Required (YES, NO): 'NO'
      Default: en
      Meaning: The language the person prefers to be addressed in
    - Artifact: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor admitted
    - Artifact: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: occurred_at
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time the admission happened, determined at the moment it occurred
    - Artifact: blockchain::EV_ACTOR_ACCEPTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor accepted
    - Artifact: blockchain::EV_ACTOR_ACCEPTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The authority that accepted them
    - Artifact: blockchain::EV_ACTOR_ACCEPTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: grounds
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The reason stated, which an acceptance may omit
    - Artifact: blockchain::EV_ACTOR_ACCEPTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: occurred_at
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time the acceptance happened, determined at the moment it occurred
    - Artifact: blockchain::EV_ACTOR_REJECTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor rejected
    - Artifact: blockchain::EV_ACTOR_REJECTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The authority that rejected them
    - Artifact: blockchain::EV_ACTOR_REJECTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: grounds
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The reason stated, which a rejection must carry
    - Artifact: blockchain::EV_ACTOR_REJECTED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: occurred_at
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The time the rejection happened, determined at the moment it occurred
    - Artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: actor_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The details the person supplied, as the operation receives them
    - Artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: registration_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The schema the details are read against for absence and form
    - Artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: violations
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields the registration failed to supply readably
    - Artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: actor_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The registration carrying the address to claim
    - Artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: address_path
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Where in the registration the contact address is found
    - Artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: address_type
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The type the contact address must be
    - Artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The contact address as extracted from the registration
    - Artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The store address the claim was registered at
    - Artifact: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: actor_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields the actor record is assembled from
    - Artifact: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The claimed address the actor is written under
    - Artifact: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the actor was written
    - Artifact: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The address naming the actor to resolve
    - Artifact: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: value
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor and its current state, or absent when none is held
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: current_state
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor's state as read before the decision
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: states_admitting_a_decision
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The states from which a decision may be made
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: decision
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The outcome the authority states
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: admitted_outcomes
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The two outcomes a decision may carry
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The authority making the decision, recorded and never resolved
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor decided about
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: decided_actor_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields the decided actor record is assembled from
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the decision was recorded
    - Artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: occurrence_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields the occurrence record is assembled from, including occurred_at
    - Artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: stream_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The trail the occurrence is appended to
    - Artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor the occurrence is recorded against
    - Artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: sequence_number
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The position the occurrence was written at, which the store assigns
  implementation_bindings:
    columns:
    - CT Code
    - Module
    - Callable
    - Operation
    - Kind (atom, molecule)
    - Purity (ct_pure, ct_impure)
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Module: ''
      Callable: ''
      Operation: ''
      Kind (atom, molecule): ''
      Purity (ct_pure, ct_impure): ''
      Source Finding: ''
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: NONE IDENTIFIED
      Extends: ''
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
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Key: structure
      Value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every person the business knows, carrying whether it has accepted them
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Capability: capability_side_effects::CS_REGISTRY_V0
      Key: structure
      Value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: S6 storage_governance An atomic claim on each contact address
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Key: structure
      Value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: S6 storage_governance An unamendable trail of every occurrence recorded against an actor
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Capability: capability_side_effects::CS_CLOCK_V0
      Key: precision
      Value: seconds
      Source Finding: 'S4 design_decisions #5'
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: blockchain::AC_PARTICIPANT_V0
      Property: type
      Value: ENDUSER
      Source Finding: S5 provisional_codes AC_PARTICIPANT_V0
    - Artifact: blockchain::EV_ACTOR_REJECTED_V0
      Property: grounds_required
      Value: 'YES'
      Source Finding: S6 boundary_rules ACCEPTANCE_AND_REJECTION_ARE_DISTINCT
    - Artifact: blockchain::EV_ACTOR_ACCEPTED_V0
      Property: grounds_required
      Value: 'NO'
      Source Finding: S6 boundary_rules ACCEPTANCE_AND_REJECTION_ARE_DISTINCT
    - Artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Property: occurred_at_source
      Value: capability_side_effects::CS_CLOCK_V0
      Source Finding: S6 boundary_rules NO_TIME_IS_INVENTED
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: ACTORS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_MUTABLE_JSON_V0
      Proposed Path: blockchain/identity/actors.json
      Used By: blockchain::CC_REGISTER_ACTOR_V0
      Source Finding: S6 storage_governance A durable record of every person the business knows, carrying whether it has accepted them
    - Store Name: CONTACT_ADDRESS_REGISTRY
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: blockchain/identity/contact_address_registry.jsonl
      Used By: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Source Finding: S6 storage_governance An atomic claim on each contact address
    - Store Name: ACTOR_OCCURRENCES
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_APPENDONLY_JSONL_V0
      Proposed Path: blockchain/identity/actor_occurrences.jsonl
      Used By: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Source Finding: S6 storage_governance An unamendable trail of every occurrence recorded against an actor
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
      Subdomain: identity
      Count: '16'
      Artifacts: 1 AC, 1 STRUCTURE, 1 RB, 3 EV, 2 IN, 2 WF, 6 CC
```

The first phase that names artifacts. Every code the business intent proposed is bound to an
identity in the blockchain namespace, every store is given a type and a path, and every capability
contract is composed step by step. One step cannot be composed: the substrate offers no capability
that determines a time, and the design declares the field rather than inventing a value for it.

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

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Implementation Bindings

---

## 10. Vocabulary Extensions

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

## Gate 1 — Design Approval

The dossier is reviewed as a body. One thing is known and unresolved: no capability in the
composition determines a time, so `occurred_at` is declared on every occurrence and supplied by no
step of this design. Construction will report it undetermined, which is the correct outcome —
the design states what must be true and refuses to invent the value that would make it appear true.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | p5_business_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 6 — Governance Intent | p6_governance_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 7 — Design Intent | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | provisional_codes · business_objects · identity_semantics · invariants · actions |
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary |
