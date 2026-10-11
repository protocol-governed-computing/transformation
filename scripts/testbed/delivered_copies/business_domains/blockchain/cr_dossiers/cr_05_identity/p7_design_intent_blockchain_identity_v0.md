# Stage 7 — Design Intent: blockchain / identity

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_05_identity
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
    - Decision: Each rule is held by the step that applies it
      Business Fact: A rule the caller supplies is a rule the caller can widen
      Resolution: The registration schema, the states admitting a decision, the admitted outcomes and the grounds rules are literal inputs of the step that applies each; the contracts no longer declare them as inputs
      Source Finding: 'S4 design_decisions #1'
    - Decision: The registration check is followed by a rule refusing when it found anything
      Business Fact: An incomplete registration is refused
      Resolution: '`CC_VALIDATE_REGISTRATION_V0` gains `refuse_incomplete_registration`, a rule step over the check''s violations requiring none'
      Source Finding: 'S4 design_decisions #2'
    - Decision: The self-decision rule is a comparison followed by a fixed rule
      Business Fact: No authority decides about themselves
      Resolution: '`compare_authority_to_person` compares the authority with the person; `refuse_self_decision` requires the comparison to be false'
      Source Finding: 'S4 design_decisions #3'
    - Decision: The decided record is built from the decision the step checked
      Business Fact: The state recorded is the decision admitted
      Resolution: The decided record is assembled inside the contract from the checked decision, the authority and the grounds; no request hands it a record
      Source Finding: 'S4 design_decisions #4'
    - Decision: Each act fixes its decision
      Business Fact: An acceptance act accepts and a rejection act rejects
      Resolution: The acceptance act hands the contract ACCEPTED and the rejection act REJECTED, as literals
      Source Finding: 'S4 design_decisions #4'
    - Decision: Registration writes the state unverified as its own
      Business Fact: The lifecycle has one way in
      Resolution: The registration act builds the record it registers with the state UNVERIFIED as a literal
      Source Finding: 'S4 design_decisions #5'
    - Decision: The entrances stop supplying what identity holds
      Business Fact: Nothing a caller sends or is told changes
      Resolution: The three entrances drop the schema, the sets, the rules, the decision and the decided record from their payloads; their input contracts are unchanged, and the registration gate stops requiring the schema they no longer send
      Source Finding: 'S4 design_decisions #6'
    - Decision: Records made before this change are left as they are
      Business Fact: The record is added to and never rewritten
      Resolution: No migration, backfill or repair step is designed
      Source Finding: 'S4 design_decisions #7'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: blockchain::CC_VALIDATE_REGISTRATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Refuses a registration lacking the person's name or their address
      Reason: It takes its schema from the request and refuses nothing it finds.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Refuses a decision about a person not unverified, a decision other than an acceptance or a rejection, or an authority deciding about themselves, and records the decision it checked
      Reason: It takes its sets and its self-decision rule from the request, and records a state the request supplies.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Refuses a rejection stating no grounds, before anything is recorded
      Reason: It takes its rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: blockchain::WF_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that admits a person as an unverified actor, and announces that it did
      Reason: It binds the schema from the request and writes the state it is handed.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: blockchain::WF_ACCEPT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that records an acceptance and announces it
      Reason: It binds the rules and the decision from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: blockchain::WF_REJECT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that records a rejection, with grounds required, and announces it
      Reason: It binds the rules and the decision from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: blockchain::TI_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request to register an actor, declaring the name and contact address a caller sends and holding the address path, stream, preferences and occurrence label the act requires
      Reason: It supplies the schema and the state identity now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: blockchain::TI_ACCEPT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the stream and the acceptance occurrence label
      Reason: It supplies the rules and the decided record identity now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - FQDN: blockchain::TI_REJECT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the stream and the rejection occurrence label
      Reason: It supplies the rules and the decided record identity now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - FQDN: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request to accept a person, with the grounds the authority chooses to state, and refuses one that names nobody
      Reason: It does not declare the grounds an acceptance may carry.
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - FQDN: blockchain::CC_RESOLVE_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Resolves a person and carries their state, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - FQDN: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Claims a contact address, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - FQDN: blockchain::CC_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Records the person it is handed, unchanged; the act now hands it the state.
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - FQDN: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Records a moment on a person's trail, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - FQDN: blockchain::IN_ACTOR_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to admit a person as an actor
      Reason: It requires the schema identity now holds and the entrance no longer supplies.
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - FQDN: blockchain::IN_ACTOR_REJECTION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Admits a rejection and its grounds, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by the registration act, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: blockchain::EV_ACTOR_ACCEPTED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by the acceptance act, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: blockchain::EV_ACTOR_REJECTED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by the rejection act, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: blockchain::AC_PARTICIPANT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The authority context the three acts run under, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: blockchain::RB_IDENTITY_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The bindings the three acts resolve their capabilities and stores through, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Reports what a registration lacks.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Refuses on a fixed list of rules.
      Source Finding: 'S6 cross_subdomain_deps #2'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Refuses a value outside a fixed set.
      Source Finding: 'S6 cross_subdomain_deps #3'
    - FQDN: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Compares the authority with the person decided about.
      Source Finding: 'S6 cross_subdomain_deps #4'
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Assembles the decided record from the checked decision.
      Source Finding: 'S6 cross_subdomain_deps #5'
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Holds the actor record the decision updates.
      Source Finding: 'S6 storage_governance #1'
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows: []
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
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_ACCEPT_ACTOR_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_REJECT_ACTOR_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
  execution_topology:
    columns:
    - Workflow
    - Node
    - Runs
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::IN_ACTOR_REGISTERED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_VALIDATE_REGISTRATION_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_VALIDATE_REGISTRATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_CLAIM_CONTACT_ADDRESS_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_REGISTER_ACTOR_V0; ALREADY_EXISTS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_REGISTER_ACTOR_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: EXIT_SUCCESS
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S5 invariants #7'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: EXIT_SUCCESS
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit blockchain::EV_ACTOR_ACCEPTED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S5 invariants #7'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::IN_ACTOR_REJECTION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RESOLVE_ACTOR_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: EXIT_SUCCESS
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit blockchain::EV_ACTOR_REJECTED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S5 invariants #7'
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
      Consumes: actor_record
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=actor_record, schema=registration_schema; out: violations=violations'
    - CC Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: '2'
      Step Name: refuse_incomplete_registration
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: violations
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=registration_findings, rules=completeness_rules; out: valid=valid'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '1'
      Step Name: read_state_admits_decision
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: current_state
      Produces: is_member
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=current_state, allowed_set=states_admitting_a_decision; out: is_member=is_member'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '2'
      Step Name: read_outcome_admitted
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: decision
      Produces: is_member
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=decision, allowed_set=admitted_outcomes; out: is_member=is_member'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '3'
      Step Name: compare_authority_to_person
      Capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
      Kind (CT, CS): CT
      Operation: COMPARE_EQUAL
      Store: —
      Consumes: verifying_authority, contact_address
      Produces: is_self
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: left=verifying_authority, right=contact_address; out: is_equal=is_self'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '4'
      Step Name: refuse_self_decision
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: is_self
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=self_findings, rules=self_rules; out: valid=valid'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '5'
      Step Name: assemble_decided_actor
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: contact_address, decision, verifying_authority, grounds
      Produces: record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=decided_fields; out: record=record'
    - CC Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: '6'
      Step Name: write_decided_actor
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: UPDATE
      Store: ACTORS
      Consumes: key, updates
      Produces: result_status
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=contact_address, updates=record; out: result_status=result_status'
    - CC Code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Step: '1'
      Step Name: require_grounds_stated
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: grounds
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=grounds_findings, rules=grounds_rules; out: valid=valid'
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
      Bound To: '{''name'': {''type'': ''string'', ''required'': True}, ''contact_address'': {''type'': ''string'', ''required'': True}}'
      Source Finding: S7 cc_composition read_registration
    - Owner: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: read_registration
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition read_registration
    - Owner: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: refuse_incomplete_registration
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''violations'': ''$.results.read_registration.violations''}'
      Source Finding: S7 cc_composition refuse_incomplete_registration
    - Owner: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: refuse_incomplete_registration
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''violations'', ''op'': ''eq'', ''value'': []}]'
      Source Finding: S7 cc_composition refuse_incomplete_registration
    - Owner: blockchain::CC_VALIDATE_REGISTRATION_V0
      Step: refuse_incomplete_registration
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition refuse_incomplete_registration
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
      Bound To: '[''UNVERIFIED'']'
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
      Bound To: '[''ACCEPTED'', ''REJECTED'']'
      Source Finding: S7 cc_composition read_outcome_admitted
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: read_outcome_admitted
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_member
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition read_outcome_admitted
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: compare_authority_to_person
      Direction (INPUT, OUTPUT): INPUT
      Field: left
      Bound To: inputs.verifying_authority
      Source Finding: S7 cc_composition compare_authority_to_person
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: compare_authority_to_person
      Direction (INPUT, OUTPUT): INPUT
      Field: right
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition compare_authority_to_person
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: compare_authority_to_person
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_self
      Bound To: capability_result.is_equal
      Source Finding: S7 cc_composition compare_authority_to_person
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: refuse_self_decision
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''is_self'': ''$.results.compare_authority_to_person.is_self''}'
      Source Finding: S7 cc_composition refuse_self_decision
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: refuse_self_decision
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''is_self'', ''op'': ''eq'', ''value'': False}]'
      Source Finding: S7 cc_composition refuse_self_decision
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: refuse_self_decision
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition refuse_self_decision
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: assemble_decided_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''contact_address'': ''$.inputs.contact_address'', ''state'': ''$.inputs.decision'', ''verifying_authority'': ''$.inputs.verifying_authority'', ''grounds'': ''$.inputs.grounds''}'
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
      Field: updates
      Bound To: results.assemble_decided_actor.record
      Source Finding: S7 cc_composition write_decided_actor
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: write_decided_actor
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_decided_actor
    - Owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Step: require_grounds_stated
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''grounds'': ''$.inputs.grounds''}'
      Source Finding: S7 cc_composition require_grounds_stated
    - Owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Step: require_grounds_stated
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''grounds'', ''op'': ''not_null''}, {''field'': ''grounds'', ''op'': ''neq'', ''value'': ''''}]'
      Source Finding: S7 cc_composition require_grounds_stated
    - Owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Step: require_grounds_stated
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_grounds_stated
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_record
      Bound To: payload.actor_record
      Source Finding: S7 execution_topology blockchain::CC_VALIDATE_REGISTRATION_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_record
      Bound To: payload.actor_record
      Source Finding: S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: address_path
      Bound To: payload.address_path
      Source Finding: S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: address_type
      Bound To: payload.address_type
      Source Finding: S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_fields
      Bound To: '{''name'': ''$.payload.actor_record.name'', ''contact_address'': ''$.payload.actor_record.contact_address'', ''state'': ''UNVERIFIED'', ''currency_preference'': ''$.payload.actor_record.currency_preference'', ''language'': ''$.payload.actor_record.language''}'
      Source Finding: S7 execution_topology blockchain::CC_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      Source Finding: S7 execution_topology blockchain::CC_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_RESOLVE_ACTOR_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: current_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decision
      Bound To: ACCEPTED
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: verifying_authority
      Bound To: payload.verifying_authority
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: grounds
      Bound To: payload.grounds
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: grounds
      Bound To: payload.grounds
      Source Finding: S7 execution_topology blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_RESOLVE_ACTOR_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: current_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decision
      Bound To: REJECTED
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: verifying_authority
      Bound To: payload.verifying_authority
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: grounds
      Bound To: payload.grounds
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
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
    - Artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: actor_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The registration as the person supplied it.
    - Artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: violations
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the registration lacks; a registration lacking anything is refused.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: current_state
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The state the person is in when the decision is made.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: decision
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The decision the act records.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is making the decision.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person the decision is about.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Why, where the authority states it.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the decision was recorded.
    - Artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Why the person is refused. A rejection stating none is refused by the rule, not by admission.
    - Artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: valid
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether grounds were stated.
    - Artifact: blockchain::IN_ACTOR_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: actor_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The registration as the person supplied it.
    - Artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person being accepted.
    - Artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The authority recording the acceptance.
    - Artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Why, where the authority chooses to say.
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: name
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person's name.
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The address the person is reached at.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person the decision is about.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is making the decision.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: Why, where the decider chooses to say.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person the decision is about.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is making the decision.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Why the person is refused. A rejection stating none is refused.
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
    rows: []
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Group
    - Casing
    - Value
    - Meaning
    - Source Finding
    rows: []
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows: []
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: blockchain::WF_REGISTER_ACTOR_V0
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_ACCEPTED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_REJECTED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Property: supersedes
      Value: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Property: supersedes
      Value: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Property: supersedes
      Value: blockchain::IN_ACTOR_VERIFIED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows: []
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
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.name
      Bound To: ${input.name}
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.currency_preference
      Bound To: BACHI
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.language
      Bound To: en
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: address_path
      Bound To: contact_address
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: address_type
      Bound To: string
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: stream_id
      Bound To: ACTOR_OCCURRENCES
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: occurrence_fields.occurrence
      Bound To: ACTOR_REGISTERED_UNVERIFIED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.register_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: occurrence_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: stream_id
      Bound To: ACTOR_OCCURRENCES
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: occurrence_fields.occurrence
      Bound To: ACTOR_ACCEPTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: occurrence_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: occurrence_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: occurrence_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: stream_id
      Bound To: ACTOR_OCCURRENCES
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: occurrence_fields.occurrence
      Bound To: ACTOR_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: occurrence_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: occurrence_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: occurrence_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: identity
      Count: '11'
      Artifacts: blockchain::CC_VALIDATE_REGISTRATION_V0, blockchain::CC_RECORD_VERIFICATION_DECISION_V0, blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0, blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0, blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REJECT_ACTOR_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REGISTERED_V0
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows: []
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows: []
  refusal_discharge:
    columns:
    - Operation
    - Refused When
    - Act
    - Step
    - Outcome
    - Source Finding
    rows:
    - Operation: Registering a person
      Refused When: The registration lacks the person's name or their address
      Act: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_VALIDATE_REGISTRATION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Recording a decision
      Refused When: The person is not unverified
      Act: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Recording a decision
      Refused When: The person is not unverified
      Act: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Recording a decision
      Refused When: The decision is neither an acceptance nor a rejection
      Act: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #3'
    - Operation: Recording a decision
      Refused When: The decision is neither an acceptance nor a rejection
      Act: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #3'
    - Operation: Recording a rejection
      Refused When: No grounds are stated
      Act: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #4'
    - Operation: Recording a decision
      Refused When: The authority is the person decided about
      Act: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #5'
    - Operation: Recording a decision
      Refused When: The authority is the person decided about
      Act: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #5'
  refusal_deferrals:
    columns:
    - Operation
    - Refused When
    - Deferred To
    - Until
    - Source Finding
    rows: []
  refusal_governance_discharge:
    columns:
    - Operation
    - Refused When
    - Phase
    - Governing Rule
    - Source Finding
    rows: []
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
    rows: []
  molecule_step_bindings:
    columns:
    - CT Code
    - Step
    - Role (INPUT, CARRY, UPDATE)
    - Field
    - Bound To
    - Source Finding
    rows: []
  test_cases:
    columns:
    - CT Code
    - Case
    - Expected Outcome (SUCCESS, VIOLATION)
    - Source Finding
    rows: []
  test_case_values:
    columns:
    - CT Code
    - Case
    - Role (INPUT, EXPECTED, ASSERT, RECORDED)
    - Field
    - Value
    - Source Finding
    rows: []
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows:
    - Artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
      Fact: .core.inputs.registration_schema
      Reason: The contract holds what a registration must contain.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Fact: .core.inputs.states_admitting_a_decision
      Reason: The contract holds the states a decision may be made from.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Fact: .core.inputs.admitted_outcomes
      Reason: The contract holds the decisions it admits.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Fact: .core.inputs.self_check_parameters
      Reason: The self-decision rule compares the authority with the person itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Fact: .core.inputs.self_check_rules
      Reason: The contract holds the self-decision rule.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Fact: .core.inputs.decided_actor_fields
      Reason: The decided record is built from the decision the contract checked.
      Source Finding: 'S6 boundary_rules #3'
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Fact: .core.pipeline[refuse_self_verification]
      Reason: Replaced by a comparison and a fixed rule on its result.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Fact: .core.inputs.grounds_parameters
      Reason: The contract reads the grounds directly.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Fact: .core.inputs.grounds_rules
      Reason: The contract holds the grounds rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::IN_ACTOR_REGISTERED_V0
      Fact: .core.inputs.registration_schema
      Reason: The gate no longer requires what identity holds and the entrance no longer supplies.
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - Artifact: blockchain::WF_REGISTER_ACTOR_V0
      Fact: .core.nodes.CC_VALIDATE_REGISTRATION_V0.inputs.registration_schema
      Reason: The contract no longer takes a schema.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.states_admitting_a_decision
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.admitted_outcomes
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.self_check_parameters
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.self_check_rules
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.decided_actor_fields
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.states_admitting_a_decision
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.admitted_outcomes
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.self_check_parameters
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.self_check_rules
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.decided_actor_fields
      Reason: The contract no longer takes this; it holds the rule or builds the record itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Fact: .core.nodes.CC_REQUIRE_REJECTION_GROUNDS_V0.inputs.grounds_parameters
      Reason: The contract no longer takes this; it holds its rules and reads the grounds.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Fact: .core.nodes.CC_REQUIRE_REJECTION_GROUNDS_V0.inputs.grounds_rules
      Reason: The contract no longer takes this; it holds its rules and reads the grounds.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Fact: .handler.payload_template.registration_schema
      Reason: Identity holds what a registration must contain.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Fact: .handler.payload_template.actor_record.state
      Reason: Registration writes the state unverified itself.
      Source Finding: 'S6 boundary_rules #4'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Fact: .handler.payload_template.decision
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Fact: .handler.payload_template.states_admitting_a_decision
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Fact: .handler.payload_template.admitted_outcomes
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Fact: .handler.payload_template.decided_actor_fields
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Fact: .handler.payload_template.self_check_parameters
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Fact: .handler.payload_template.self_check_rules
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Fact: .handler.payload_template.decision
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Fact: .handler.payload_template.states_admitting_a_decision
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Fact: .handler.payload_template.admitted_outcomes
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Fact: .handler.payload_template.decided_actor_fields
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Fact: .handler.payload_template.self_check_parameters
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Fact: .handler.payload_template.self_check_rules
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Fact: .handler.payload_template.grounds_parameters
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Fact: .handler.payload_template.grounds_rules
      Reason: Identity holds this; the entrance stops supplying it.
      Source Finding: 'S6 boundary_rules #5'
```

Every binding names a field the capability declares, read from the pinned baseline
`4d366ccab335cfbd9f94d49ec80b2c43cdcb5a0dd417e56e1895b076fbc10e02`.

Nothing new is authored. Eleven artifacts identity already holds are redeclared whole: three contracts
take their rules as fixed values, three acts stop passing rules along and fix what they write, three
entrances stop supplying what identity now holds, the registration gate stops requiring the schema,
and the acceptance gate declares the grounds an acceptance may carry.

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

The routing of the three acts is unchanged. What changes is what each node is handed, in §7.

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

---

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

---

## 18. Refusal Discharge

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
