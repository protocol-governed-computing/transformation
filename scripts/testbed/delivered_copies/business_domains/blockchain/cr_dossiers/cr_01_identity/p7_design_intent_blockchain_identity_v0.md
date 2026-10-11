# Stage 7 — Design Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p7
  domain: blockchain
  subdomain: identity
  cr: cr_01_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: The trail rests on the append-only capability
    business_fact: An occurrence that has happened cannot be un-happened
    resolution: ACTOR_OCCURRENCES is typed CS_APPENDONLY_JSONL_V0, which offers no update and no delete
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: An actor's state is held as a value
    business_fact: The refusal that an actor is decided about once needs the state at the moment of deciding
    resolution: ACTORS is typed CS_MUTABLE_JSON_V0 and read by blockchain::CC_RESOLVE_ACTOR_V0 before any decision is recorded
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: The contact address is the identifier
    business_fact: Two registrations carrying the same address are the same person
    resolution: CONTACT_ADDRESS_REGISTRY is typed CS_REGISTRY_V0 and keyed on the address as supplied; no identifier is generated
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: Acceptance and rejection are two occurrences
    business_fact: A rejected actor must never be readable as accepted
    resolution: blockchain::EV_ACTOR_ACCEPTED_V0 and blockchain::EV_ACTOR_REJECTED_V0 are separate artifacts; no artifact carries an outcome field
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: The time capability is a substrate gap
    business_fact: Every occurrence carries the time it actually happened, determined as it occurs
    resolution: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 reads capability_side_effects::CS_CLOCK_V0 before it assembles the record, so occurred_at is determined where the occurrence is recorded and no caller may assert it
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: The authority is recorded and never resolved
    business_fact: An authority is identified outside this function
    resolution: The decision carries verifying_authority as a value; no store holds authorities and no step resolves one
    source_finding: {phase: p4, register: design_decisions, row: 6}
  existing_inventory:
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: Appends a record to a named stream and reads the stream whole
    reason: Holds the occurrence trail; offers no update and no delete
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_APPENDONLY_JSONL_V0'}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REUSE
    summary: Keyed JSON state with read, write and select
    reason: Holds the actor record and its state
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    action: REUSE
    summary: Registers, resolves and reports a key
    reason: Claims the contact address and reports one already held
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    action: REUSE
    summary: Reads a record for required fields and their form
    reason: Reads a registration for absence and malformation
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    action: REUSE
    summary: Reads a value against a declared admitted set
    reason: Reads the decision outcome and the state a decision is admitted from
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0'}
  - fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    action: REUSE
    summary: Compares two supplied values
    reason: Compares the authority named against the actor decided about
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_COMPARE_EQUAL_V0'}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: Assembles a record from supplied fields
    reason: Assembles the actor record and each occurrence record
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  - fqdn: capability_side_effects::CS_CLOCK_V0
    action: REUSE
    summary: Answers the current instant
    reason: Determines the time an occurrence happened, which no transform can
    source_finding: {phase: p4, register: dependency_graph, key: the substrate capability supplying the current time}
  - fqdn: capability_transforms::CT_PURE_EXTRACT_V0
    action: REUSE
    summary: Extracts a named value from a supplied structure
    reason: Extracts the address and the decision fields
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_EXTRACT_V0'}
  new_artifacts:
  - capability: Declare the actors of this business
    family: AC
    code: blockchain::AC_PARTICIPANT_V0
    summary: The ordinary participant who registers themselves and is decided about
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: AC_PARTICIPANT_V0}
  - capability: Declare the stores identity owns
    family: STRUCTURE
    code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    summary: Declares the three stores identity owns and the paths they occupy
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: STRUCTURE_IDENTITY_STORAGE_V0}
  - capability: Bind identity's workflows to the stores they use
    family: RB
    code: blockchain::RB_IDENTITY_BINDINGS_V0
    summary: Binds identity's workflows to the side effects and storage they use
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: RB_IDENTITY_BINDINGS_V0}
  - capability: Recognise the moments an actor is registered, accepted and rejected
    family: EV
    code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    summary: The moment a person is admitted and trusted with nothing
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_ACTOR_REGISTERED_UNVERIFIED_V0}
  - capability: Recognise the moments an actor is registered, accepted and rejected
    family: EV
    code: blockchain::EV_ACTOR_ACCEPTED_V0
    summary: The moment an authority records a decision to trust an actor
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_ACTOR_ACCEPTED_V0}
  - capability: Recognise the moments an actor is registered, accepted and rejected
    family: EV
    code: blockchain::EV_ACTOR_REJECTED_V0
    summary: The moment an authority records a decision not to trust an actor
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_ACTOR_REJECTED_V0}
  - capability: Admit a request to register a person
    family: IN
    code: blockchain::IN_ACTOR_REGISTERED_V0
    summary: A request to admit a person as an actor
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_ACTOR_REGISTERED_V0}
  - capability: Admit a request to record a verification decision
    family: IN
    code: blockchain::IN_ACTOR_VERIFIED_V0
    summary: A request to record a decision, carrying the authority, the outcome and the grounds
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_ACTOR_VERIFIED_V0}
  - capability: Admit a person's registration and record them unverified
    family: WF
    code: blockchain::WF_REGISTER_ACTOR_V0
    summary: The governed sequence that admits a person as an unverified actor
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_REGISTER_ACTOR_V0}
  - capability: Record an authority's decision against a registered actor
    family: WF
    code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    summary: The governed sequence that records a decision against a registered actor
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_RECORD_VERIFICATION_DECISION_V0}
  - capability: Admit a person's registration and record them unverified
    family: CC
    code: blockchain::CC_VALIDATE_REGISTRATION_V0
    summary: Confirms a registration carries a name and an address of the form asked for
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_VALIDATE_REGISTRATION_V0}
  - capability: Admit a person's registration and record them unverified
    family: CC
    code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    summary: Claims a contact address so that two registrations of one person do not produce two actors
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CLAIM_CONTACT_ADDRESS_V0}
  - capability: Admit a person's registration and record them unverified
    family: CC
    code: blockchain::CC_REGISTER_ACTOR_V0
    summary: Writes the actor unverified after its address is claimed
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_REGISTER_ACTOR_V0}
  - capability: Record an authority's decision against a registered actor
    family: CC
    code: blockchain::CC_RESOLVE_ACTOR_V0
    summary: Answers which actor a contact address denotes, and reports when none does
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_RESOLVE_ACTOR_V0}
  - capability: Record an authority's decision against a registered actor
    family: CC
    code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    summary: Refuses every declared refusal and moves the actor to its decided state
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - capability: Record an acceptance and a rejection
    family: CC
    code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    summary: Appends one occurrence to the trail
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  rb_declarations:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REGISTER_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: An atomic claim on each contact address}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: 'A durable record of every person the business knows, carrying whether it has accepted them'}
  execution_topology:
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::IN_ACTOR_REGISTERED_V0
    node_type: IN
    routing:
      ACK: blockchain::CC_VALIDATE_REGISTRATION_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_ACTOR_REGISTERED_V0}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_VALIDATE_REGISTRATION_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_VALIDATE_REGISTRATION_V0}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_REGISTER_ACTOR_V0
      ALREADY_EXISTS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_CONTACT_ADDRESS_V0}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_REGISTER_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_REGISTER_ACTOR_V0}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: new_artifacts, key: WF_REGISTER_ACTOR_V0}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: EXIT_SUCCESS
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: new_artifacts, key: WF_REGISTER_ACTOR_V0}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: blockchain::IN_ACTOR_VERIFIED_V0
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_ACTOR_VERIFIED_V0}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: blockchain::CC_RESOLVE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RESOLVE_ACTOR_V0}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: new_artifacts, key: WF_RECORD_VERIFICATION_DECISION_V0}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: EXIT_SUCCESS
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: new_artifacts, key: WF_RECORD_VERIFICATION_DECISION_V0}
  cc_composition:
  - cc_code: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: '1'
    step_name: read_registration
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: '1'
    step_name: extract_address
    capability: capability_transforms::CT_PURE_EXTRACT_V0
    kind: CT
    operation: EXTRACT
    store: null
    consumes:
    - from
    - path
    - type
    produces:
    - result
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        from: from
        path: path
        type: type
      out:
        result: result
  - cc_code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: '2'
    step_name: claim_address
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: CONTACT_ADDRESS_REGISTRY
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
  - cc_code: blockchain::CC_REGISTER_ACTOR_V0
    step: '1'
    step_name: assemble_actor
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - fields
    produces:
    - record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: record
  - cc_code: blockchain::CC_REGISTER_ACTOR_V0
    step: '2'
    step_name: write_actor
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: ACTORS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V0
    step: '1'
    step_name: resolve_address
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: CONTACT_ADDRESS_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V0
    step: '2'
    step_name: read_actor
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: ACTORS
    consumes:
    - key
    produces:
    - value
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '1'
    step_name: read_state_admits_decision
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: is_member
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '2'
    step_name: read_outcome_admitted
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: is_member
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '3'
    step_name: refuse_self_verification
    capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    kind: CT
    operation: COMPARE_EQUAL
    store: null
    consumes:
    - left
    - right
    produces:
    - is_equal
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        left: left
        right: right
      out:
        is_equal: is_equal
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '4'
    step_name: assemble_decided_actor
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - fields
    produces:
    - record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: record
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '5'
    step_name: write_decided_actor
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: ACTORS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: '1'
    step_name: read_now
    capability: capability_side_effects::CS_CLOCK_V0
    kind: CS
    operation: NOW
    store: null
    consumes: null
    produces:
    - timestamp
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: '2'
    step_name: assemble_occurrence
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - fields
    produces:
    - record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: record
  - cc_code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: '3'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: ACTOR_OCCURRENCES
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - sequence_number
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  step_bindings:
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: read_registration
    direction: INPUT
    field: record
    bound_to: inputs.actor_record
    source_finding: {phase: p7, register: cc_composition, key: read_registration}
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: read_registration
    direction: INPUT
    field: schema
    bound_to: inputs.registration_schema
    source_finding: {phase: p7, register: cc_composition, key: read_registration}
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: read_registration
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: read_registration}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: extract_address
    direction: INPUT
    field: from
    bound_to: inputs.actor_record
    source_finding: {phase: p7, register: cc_composition, key: extract_address}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: extract_address
    direction: INPUT
    field: path
    bound_to: inputs.address_path
    source_finding: {phase: p7, register: cc_composition, key: extract_address}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: extract_address
    direction: INPUT
    field: type
    bound_to: inputs.address_type
    source_finding: {phase: p7, register: cc_composition, key: extract_address}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: extract_address
    direction: OUTPUT
    field: result
    bound_to: capability_result.result
    source_finding: {phase: p7, register: cc_composition, key: extract_address}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: key
    bound_to: results.extract_address.result
    source_finding: {phase: p7, register: cc_composition, key: claim_address}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
    source_finding: {phase: p7, register: cc_composition, key: claim_address}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: target_ref
    bound_to:
      literal: ACTORS
    source_finding: {phase: p7, register: cc_composition, key: claim_address}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
    source_finding: {phase: p7, register: cc_composition, key: claim_address}
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_address}
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: assemble_actor
    direction: INPUT
    field: fields
    bound_to: inputs.actor_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_actor}
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: assemble_actor
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_actor}
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: write_actor
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: write_actor}
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: write_actor
    direction: INPUT
    field: value
    bound_to: results.assemble_actor.record
    source_finding: {phase: p7, register: cc_composition, key: write_actor}
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: write_actor
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_actor}
  - owner: blockchain::CC_RESOLVE_ACTOR_V0
    step: resolve_address
    direction: INPUT
    field: key_or_address
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: resolve_address}
  - owner: blockchain::CC_RESOLVE_ACTOR_V0
    step: resolve_address
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
    source_finding: {phase: p7, register: cc_composition, key: resolve_address}
  - owner: blockchain::CC_RESOLVE_ACTOR_V0
    step: read_actor
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: read_actor}
  - owner: blockchain::CC_RESOLVE_ACTOR_V0
    step: read_actor
    direction: OUTPUT
    field: value
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: INPUT
    field: value
    bound_to: inputs.current_state
    source_finding: {phase: p7, register: cc_composition, key: read_state_admits_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: INPUT
    field: allowed_set
    bound_to: inputs.states_admitting_a_decision
    source_finding: {phase: p7, register: cc_composition, key: read_state_admits_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: read_state_admits_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: INPUT
    field: value
    bound_to: inputs.decision
    source_finding: {phase: p7, register: cc_composition, key: read_outcome_admitted}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: INPUT
    field: allowed_set
    bound_to: inputs.admitted_outcomes
    source_finding: {phase: p7, register: cc_composition, key: read_outcome_admitted}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: read_outcome_admitted}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_verification
    direction: INPUT
    field: left
    bound_to: inputs.verifying_authority
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_verification}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_verification
    direction: INPUT
    field: right
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_verification}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_verification
    direction: OUTPUT
    field: is_equal
    bound_to: capability_result.is_equal
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_verification}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: assemble_decided_actor
    direction: INPUT
    field: fields
    bound_to: inputs.decided_actor_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: assemble_decided_actor
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: write_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: INPUT
    field: value
    bound_to: results.assemble_decided_actor.record
    source_finding: {phase: p7, register: cc_composition, key: write_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_decided_actor}
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
    source_finding: {phase: p7, register: cc_composition, key: read_now}
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to:
      literal:
        occurrence: $.inputs.occurrence_fields.occurrence
        contact_address: $.inputs.contact_address
        verifying_authority: $.inputs.occurrence_fields.verifying_authority
        grounds: $.inputs.occurrence_fields.grounds
        occurred_at: $.results.read_now.timestamp
    source_finding: {phase: p7, register: cc_composition, key: assemble_occurrence}
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_occurrence}
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to: inputs.stream_id
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: actor_id
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: append_occurrence
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_REGISTRATION_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: registration_schema
    bound_to: payload.registration_schema
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_REGISTRATION_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_CONTACT_ADDRESS_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_path
    bound_to: payload.address_path
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_CONTACT_ADDRESS_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_type
    bound_to: payload.address_type
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_CONTACT_ADDRESS_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: actor_fields
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: CC_RESOLVE_ACTOR_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p7, register: execution_topology, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: states_admitting_a_decision
    bound_to: payload.states_admitting_a_decision
    source_finding: {phase: p7, register: execution_topology, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to: payload.decision
    source_finding: {phase: p7, register: execution_topology, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: admitted_outcomes
    bound_to: payload.admitted_outcomes
    source_finding: {phase: p7, register: execution_topology, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding: {phase: p7, register: execution_topology, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decided_actor_fields
    bound_to: payload.decided_actor_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_RECORD_VERIFICATION_DECISION_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  - owner: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_ACTOR_OCCURRENCE_V0}
  interface_fields:
  - artifact: blockchain::IN_ACTOR_REGISTERED_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: ''
    meaning: The details the person supplies about themselves
  - artifact: blockchain::IN_ACTOR_REGISTERED_V0
    direction: INPUT
    field: registration_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The schema the supplied details are read against for absence and form
  - artifact: blockchain::IN_ACTOR_VERIFIED_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The address naming the actor the decision is about
  - artifact: blockchain::IN_ACTOR_VERIFIED_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority making the decision, recorded and never resolved
  - artifact: blockchain::IN_ACTOR_VERIFIED_V0
    direction: INPUT
    field: decision
    type: string
    required: 'YES'
    default: ''
    meaning: The outcome, which must be one of the two admitted values
  - artifact: blockchain::IN_ACTOR_VERIFIED_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: The reason stated for the decision; required for a rejection
  - artifact: blockchain::AC_PARTICIPANT_V0
    direction: ATTRIBUTE
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The address identifying the participant
  - artifact: blockchain::AC_PARTICIPANT_V0
    direction: ATTRIBUTE
    field: name
    type: string
    required: 'YES'
    default: ''
    meaning: What the person is called, as they supplied it
  - artifact: blockchain::AC_PARTICIPANT_V0
    direction: ATTRIBUTE
    field: currency_preference
    type: string
    required: 'NO'
    default: BACHI
    meaning: The currency the person prefers to be quoted in
  - artifact: blockchain::AC_PARTICIPANT_V0
    direction: ATTRIBUTE
    field: language
    type: string
    required: 'NO'
    default: en
    meaning: The language the person prefers to be addressed in
  - artifact: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    direction: ATTRIBUTE
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor admitted
  - artifact: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    direction: ATTRIBUTE
    field: occurred_at
    type: string
    required: 'YES'
    default: ''
    meaning: The time the admission happened, determined at the moment it occurred
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: ATTRIBUTE
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor accepted
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: ATTRIBUTE
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority that accepted them
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: ATTRIBUTE
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: The reason stated, which an acceptance may omit
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: ATTRIBUTE
    field: occurred_at
    type: string
    required: 'YES'
    default: ''
    meaning: The time the acceptance happened, determined at the moment it occurred
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: ATTRIBUTE
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor rejected
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: ATTRIBUTE
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority that rejected them
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: ATTRIBUTE
    field: grounds
    type: string
    required: 'YES'
    default: ''
    meaning: The reason stated, which a rejection must carry
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: ATTRIBUTE
    field: occurred_at
    type: string
    required: 'YES'
    default: ''
    meaning: The time the rejection happened, determined at the moment it occurred
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: ''
    meaning: The details the person supplied, as the operation receives them
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: registration_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The schema the details are read against for absence and form
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: OUTPUT
    field: violations
    type: array
    required: 'YES'
    default: ''
    meaning: The fields the registration failed to supply readably
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: ''
    meaning: The registration carrying the address to claim
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_path
    type: string
    required: 'YES'
    default: ''
    meaning: Where in the registration the contact address is found
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_type
    type: string
    required: 'YES'
    default: ''
    meaning: The type the contact address must be
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: OUTPUT
    field: result
    type: string
    required: 'YES'
    default: ''
    meaning: The contact address as extracted from the registration
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: ''
    meaning: The store address the claim was registered at
  - artifact: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: actor_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The fields the actor record is assembled from
  - artifact: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The claimed address the actor is written under
  - artifact: blockchain::CC_REGISTER_ACTOR_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the actor was written
  - artifact: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The address naming the actor to resolve
  - artifact: blockchain::CC_RESOLVE_ACTOR_V0
    direction: OUTPUT
    field: value
    type: object
    required: 'YES'
    default: ''
    meaning: The actor and its current state, or absent when none is held
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    type: string
    required: 'YES'
    default: ''
    meaning: The actor's state as read before the decision
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: states_admitting_a_decision
    type: array
    required: 'YES'
    default: ''
    meaning: The states from which a decision may be made
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    type: string
    required: 'YES'
    default: ''
    meaning: The outcome the authority states
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: admitted_outcomes
    type: array
    required: 'YES'
    default: ''
    meaning: The two outcomes a decision may carry
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority making the decision, recorded and never resolved
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor decided about
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decided_actor_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The fields the decided actor record is assembled from
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the decision was recorded
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The fields the occurrence record is assembled from, including occurred_at
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    type: string
    required: 'YES'
    default: ''
    meaning: The trail the occurrence is appended to
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor the occurrence is recorded against
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The position the occurrence was written at, which the store assigns
  implementation_bindings: []
  vocabulary_extensions: []
  runtime_policies:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: 'A durable record of every person the business knows, carrying whether it has accepted them'}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: An atomic claim on each contact address}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: An unamendable trail of every occurrence recorded against an actor}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_CLOCK_V0
    key: precision
    value: seconds
    source_finding: {phase: p4, register: design_decisions, row: 5}
  artifact_properties:
  - artifact: blockchain::AC_PARTICIPANT_V0
    property: type
    value: ENDUSER
    source_finding: {phase: p5, register: provisional_codes, key: AC_PARTICIPANT_V0}
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    property: grounds_required
    value: 'YES'
    source_finding: {phase: p6, register: boundary_rules, key: ACCEPTANCE_AND_REJECTION_ARE_DISTINCT}
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    property: grounds_required
    value: 'NO'
    source_finding: {phase: p6, register: boundary_rules, key: ACCEPTANCE_AND_REJECTION_ARE_DISTINCT}
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    property: occurred_at_source
    value: capability_side_effects::CS_CLOCK_V0
    source_finding: {phase: p6, register: boundary_rules, key: NO_TIME_IS_INVENTED}
  structure_stores:
  - store_name: ACTORS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: blockchain/identity/actors.json
    used_by: blockchain::CC_REGISTER_ACTOR_V0
    source_finding: {phase: p6, register: storage_governance, key: 'A durable record of every person the business knows, carrying whether it has accepted them'}
  - store_name: CONTACT_ADDRESS_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: blockchain/identity/contact_address_registry.jsonl
    used_by: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    source_finding: {phase: p6, register: storage_governance, key: An atomic claim on each contact address}
  - store_name: ACTOR_OCCURRENCES
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: blockchain/identity/actor_occurrences.jsonl
    used_by: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    source_finding: {phase: p6, register: storage_governance, key: An unamendable trail of every occurrence recorded against an actor}
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: identity
    count: '16'
    artifacts: 1 AC, 1 STRUCTURE, 1 RB, 3 EV, 2 IN, 2 WF, 6 CC
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
