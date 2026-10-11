# Stage 7 — Design Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p7
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Each rule is held by the step that applies it
    business_fact: A rule the caller supplies is a rule the caller can widen
    resolution: The registration schema, the states admitting a decision, the admitted outcomes and the grounds rules are literal inputs of the step that applies each; the contracts no longer declare them as inputs
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: The registration check is followed by a rule refusing when it found anything
    business_fact: An incomplete registration is refused
    resolution: '`CC_VALIDATE_REGISTRATION_V0` gains `refuse_incomplete_registration`, a rule step over the check''s violations requiring none'
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: The self-decision rule is a comparison followed by a fixed rule
    business_fact: No authority decides about themselves
    resolution: '`compare_authority_to_person` compares the authority with the person; `refuse_self_decision` requires the comparison to be false'
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: The decided record is built from the decision the step checked
    business_fact: The state recorded is the decision admitted
    resolution: The decided record is assembled inside the contract from the checked decision, the authority and the grounds; no request hands it a record
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: Each act fixes its decision
    business_fact: An acceptance act accepts and a rejection act rejects
    resolution: The acceptance act hands the contract ACCEPTED and the rejection act REJECTED, as literals
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: Registration writes the state unverified as its own
    business_fact: The lifecycle has one way in
    resolution: The registration act builds the record it registers with the state UNVERIFIED as a literal
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: The entrances stop supplying what identity holds
    business_fact: Nothing a caller sends or is told changes
    resolution: The three entrances drop the schema, the sets, the rules, the decision and the decided record from their payloads; their input contracts are unchanged, and the registration gate stops requiring the schema they no longer send
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - decision: Records made before this change are left as they are
    business_fact: The record is added to and never rewritten
    resolution: No migration, backfill or repair step is designed
    source_finding: {phase: p4, register: design_decisions, row: 7}
  existing_inventory:
  - fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    action: EXTEND
    summary: Refuses a registration lacking the person's name or their address
    reason: It takes its schema from the request and refuses nothing it finds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    action: EXTEND
    summary: Refuses a decision about a person not unverified, a decision other than an acceptance or a rejection, or an authority deciding about themselves, and records the decision it checked
    reason: It takes its sets and its self-decision rule from the request, and records a state the request supplies.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    action: EXTEND
    summary: Refuses a rejection stating no grounds, before anything is recorded
    reason: It takes its rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: blockchain::WF_REGISTER_ACTOR_V0
    action: EXTEND
    summary: The governed sequence that admits a person as an unverified actor, and announces that it did
    reason: It binds the schema from the request and writes the state it is handed.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: blockchain::WF_ACCEPT_ACTOR_V0
    action: EXTEND
    summary: The governed sequence that records an acceptance and announces it
    reason: It binds the rules and the decision from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: blockchain::WF_REJECT_ACTOR_V0
    action: EXTEND
    summary: The governed sequence that records a rejection, with grounds required, and announces it
    reason: It binds the rules and the decision from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: blockchain::TI_REGISTER_ACTOR_V0
    action: EXTEND
    summary: Admits a request to register an actor, declaring the name and contact address a caller sends and holding the address path, stream, preferences and occurrence label the act requires
    reason: It supplies the schema and the state identity now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    action: EXTEND
    summary: Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the stream and the acceptance occurrence label
    reason: It supplies the rules and the decided record identity now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    action: EXTEND
    summary: Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the stream and the rejection occurrence label
    reason: It supplies the rules and the decided record identity now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    action: EXTEND
    summary: Admits a request to accept a person, with the grounds the authority chooses to state, and refuses one that names nobody
    reason: It does not declare the grounds an acceptance may carry.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    action: REUSE
    summary: ''
    reason: Resolves a person and carries their state, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    action: REUSE
    summary: ''
    reason: Claims a contact address, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - fqdn: blockchain::CC_REGISTER_ACTOR_V0
    action: REUSE
    summary: ''
    reason: Records the person it is handed, unchanged; the act now hands it the state.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    action: REUSE
    summary: ''
    reason: Records a moment on a person's trail, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    action: EXTEND
    summary: A request to admit a person as an actor
    reason: It requires the schema identity now holds and the entrance no longer supplies.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - fqdn: blockchain::IN_ACTOR_REJECTION_V0
    action: REUSE
    summary: ''
    reason: Admits a rejection and its grounds, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    action: REUSE
    summary: ''
    reason: Announced by the registration act, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: blockchain::EV_ACTOR_ACCEPTED_V0
    action: REUSE
    summary: ''
    reason: Announced by the acceptance act, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: blockchain::EV_ACTOR_REJECTED_V0
    action: REUSE
    summary: ''
    reason: Announced by the rejection act, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: blockchain::AC_PARTICIPANT_V0
    action: REUSE
    summary: ''
    reason: The authority context the three acts run under, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
    action: REUSE
    summary: ''
    reason: The bindings the three acts resolve their capabilities and stores through, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    action: REUSE
    summary: ''
    reason: Reports what a registration lacks.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    action: REUSE
    summary: ''
    reason: Refuses on a fixed list of rules.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 2}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    action: REUSE
    summary: ''
    reason: Refuses a value outside a fixed set.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 3}
  - fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    action: REUSE
    summary: ''
    reason: Compares the authority with the person decided about.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 4}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: ''
    reason: Assembles the decided record from the checked decision.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 5}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REUSE
    summary: ''
    reason: Holds the actor record the decision updates.
    source_finding: {phase: p6, register: storage_governance, row: 1}
  new_artifacts: null
  rb_declarations:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REGISTER_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_ACCEPT_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REJECT_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  execution_topology:
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::IN_ACTOR_REGISTERED_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_VALIDATE_REGISTRATION_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_VALIDATE_REGISTRATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_REGISTER_ACTOR_V0
      ALREADY_EXISTS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_REGISTER_ACTOR_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p5, register: invariants, row: 7}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: blockchain::IN_ACTOR_ACCEPTANCE_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: blockchain::CC_RESOLVE_ACTOR_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p5, register: invariants, row: 7}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::IN_ACTOR_REJECTION_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RESOLVE_ACTOR_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::CC_RESOLVE_ACTOR_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p5, register: invariants, row: 7}
  cc_composition:
  - cc_code: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: '1'
    step_name: read_registration
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - actor_record
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: actor_record
        schema: registration_schema
      out:
        violations: violations
  - cc_code: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: '2'
    step_name: refuse_incomplete_registration
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
        parameters: registration_findings
        rules: completeness_rules
      out:
        valid: valid
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '1'
    step_name: read_state_admits_decision
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: VALIDATE_SET_MEMBERSHIP
    store: null
    consumes:
    - current_state
    produces:
    - is_member
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: current_state
        allowed_set: states_admitting_a_decision
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
    - decision
    produces:
    - is_member
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: decision
        allowed_set: admitted_outcomes
      out:
        is_member: is_member
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '3'
    step_name: compare_authority_to_person
    capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    kind: CT
    operation: COMPARE_EQUAL
    store: null
    consumes:
    - verifying_authority
    - contact_address
    produces:
    - is_self
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        left: verifying_authority
        right: contact_address
      out:
        is_equal: is_self
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '4'
    step_name: refuse_self_decision
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - is_self
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: self_findings
        rules: self_rules
      out:
        valid: valid
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '5'
    step_name: assemble_decided_actor
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - contact_address
    - decision
    - verifying_authority
    - grounds
    produces:
    - record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: decided_fields
      out:
        record: record
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '6'
    step_name: write_decided_actor
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE
    store: ACTORS
    consumes:
    - key
    - updates
    produces:
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: contact_address
        updates: record
      out:
        result_status: result_status
  - cc_code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: '1'
    step_name: require_grounds_stated
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - grounds
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: grounds_findings
        rules: grounds_rules
      out:
        valid: valid
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
    bound_to:
      literal:
        name:
          type: string
          required: true
        contact_address:
          type: string
          required: true
    source_finding: {phase: p7, register: cc_composition, key: read_registration}
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: read_registration
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: read_registration}
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: refuse_incomplete_registration
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.read_registration.violations
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_registration}
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: refuse_incomplete_registration
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_registration}
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: refuse_incomplete_registration
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_registration}
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
    bound_to:
      literal:
      - UNVERIFIED
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
    bound_to:
      literal:
      - ACCEPTED
      - REJECTED
    source_finding: {phase: p7, register: cc_composition, key: read_outcome_admitted}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: read_outcome_admitted}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: compare_authority_to_person
    direction: INPUT
    field: left
    bound_to: inputs.verifying_authority
    source_finding: {phase: p7, register: cc_composition, key: compare_authority_to_person}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: compare_authority_to_person
    direction: INPUT
    field: right
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: compare_authority_to_person}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: compare_authority_to_person
    direction: OUTPUT
    field: is_self
    bound_to: capability_result.is_equal
    source_finding: {phase: p7, register: cc_composition, key: compare_authority_to_person}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_decision
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        is_self: $.results.compare_authority_to_person.is_self
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_decision
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: is_self
        op: eq
        value: false
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_decision
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_decision}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: assemble_decided_actor
    direction: INPUT
    field: fields
    bound_to:
      literal:
        contact_address: $.inputs.contact_address
        state: $.inputs.decision
        verifying_authority: $.inputs.verifying_authority
        grounds: $.inputs.grounds
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
    field: updates
    bound_to: results.assemble_decided_actor.record
    source_finding: {phase: p7, register: cc_composition, key: write_decided_actor}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_decided_actor}
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: require_grounds_stated
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        grounds: $.inputs.grounds
    source_finding: {phase: p7, register: cc_composition, key: require_grounds_stated}
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: require_grounds_stated
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: grounds
        op: not_null
      - field: grounds
        op: neq
        value: ''
    source_finding: {phase: p7, register: cc_composition, key: require_grounds_stated}
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: require_grounds_stated
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_grounds_stated}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_VALIDATE_REGISTRATION_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_path
    bound_to: payload.address_path
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_type
    bound_to: payload.address_type
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: actor_fields
    bound_to:
      literal:
        name: $.payload.actor_record.name
        contact_address: $.payload.actor_record.contact_address
        state: UNVERIFIED
        currency_preference: $.payload.actor_record.currency_preference
        language: $.payload.actor_record.language
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REGISTER_ACTOR_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REGISTER_ACTOR_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: ACCEPTED
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: REJECTED
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  interface_fields:
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: ''
    meaning: The registration as the person supplied it.
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: OUTPUT
    field: violations
    type: array
    required: 'YES'
    default: ''
    meaning: What the registration lacks; a registration lacking anything is refused.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    type: string
    required: 'YES'
    default: ''
    meaning: The state the person is in when the decision is made.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    type: string
    required: 'YES'
    default: ''
    meaning: The decision the act records.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: Who is making the decision.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The person the decision is about.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: Why, where the authority states it.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the decision was recorded.
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: Why the person is refused. A rejection stating none is refused by the rule, not by admission.
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether grounds were stated.
  - artifact: blockchain::IN_ACTOR_REGISTERED_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: ''
    meaning: The registration as the person supplied it.
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The person being accepted.
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority recording the acceptance.
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: Why, where the authority chooses to say.
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INPUT
    field: name
    type: string
    required: 'YES'
    default: ''
    meaning: The person's name.
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The address the person is reached at.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The person the decision is about.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: Who is making the decision.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: Why, where the decider chooses to say.
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The person the decision is about.
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: Who is making the decision.
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'YES'
    default: ''
    meaning: Why the person is refused. A rejection stating none is refused.
  implementation_bindings: null
  vocabulary_extensions: null
  runtime_policies: null
  artifact_properties:
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_ACCEPTED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REJECTED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    property: supersedes
    value:
    - blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    property: supersedes
    value:
    - blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    property: supersedes
    value:
    - blockchain::IN_ACTOR_VERIFIED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  structure_stores: null
  transport_bindings:
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.name
    bound_to: ${input.name}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.currency_preference
    bound_to:
      literal: BACHI
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.language
    bound_to:
      literal: en
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: address_path
    bound_to:
      literal: contact_address
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: address_type
    bound_to:
      literal: string
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: occurrence_fields.occurrence
    bound_to:
      literal: ACTOR_REGISTERED_UNVERIFIED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: occurrence_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: occurrence_fields.occurrence
    bound_to:
      literal: ACTOR_ACCEPTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: occurrence_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: occurrence_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: occurrence_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: occurrence_fields.occurrence
    bound_to:
      literal: ACTOR_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: occurrence_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: occurrence_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: occurrence_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  artifact_summary:
  - action: EXTEND
    subdomain: identity
    count: '11'
    artifacts: blockchain::CC_VALIDATE_REGISTRATION_V0, blockchain::CC_RECORD_VERIFICATION_DECISION_V0, blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0, blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0, blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REJECT_ACTOR_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REGISTERED_V0
  generation_provenance: null
  declared_reach: null
  refusal_discharge:
  - operation: Registering a person
    refused_when: The registration lacks the person's name or their address
    act: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_VALIDATE_REGISTRATION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Recording a decision
    refused_when: The person is not unverified
    act: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Recording a decision
    refused_when: The person is not unverified
    act: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Recording a decision
    refused_when: The decision is neither an acceptance nor a rejection
    act: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Recording a decision
    refused_when: The decision is neither an acceptance nor a rejection
    act: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Recording a rejection
    refused_when: No grounds are stated
    act: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Recording a decision
    refused_when: The authority is the person decided about
    act: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: Recording a decision
    refused_when: The authority is the person decided about
    act: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  refusal_deferrals: null
  refusal_governance_discharge: null
  molecule_steps: null
  molecule_step_bindings: null
  test_cases: null
  test_case_values: null
  withdrawn_facts:
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    fact: .core.inputs.registration_schema
    reason: The contract holds what a registration must contain.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    fact: .core.inputs.states_admitting_a_decision
    reason: The contract holds the states a decision may be made from.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    fact: .core.inputs.admitted_outcomes
    reason: The contract holds the decisions it admits.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    fact: .core.inputs.self_check_parameters
    reason: The self-decision rule compares the authority with the person itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    fact: .core.inputs.self_check_rules
    reason: The contract holds the self-decision rule.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    fact: .core.inputs.decided_actor_fields
    reason: The decided record is built from the decision the contract checked.
    source_finding: {phase: p6, register: boundary_rules, row: 3}
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    fact: .core.pipeline[refuse_self_verification]
    reason: Replaced by a comparison and a fixed rule on its result.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    fact: .core.inputs.grounds_parameters
    reason: The contract reads the grounds directly.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    fact: .core.inputs.grounds_rules
    reason: The contract holds the grounds rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::IN_ACTOR_REGISTERED_V0
    fact: .core.inputs.registration_schema
    reason: The gate no longer requires what identity holds and the entrance no longer supplies.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    fact: .core.nodes.CC_VALIDATE_REGISTRATION_V0.inputs.registration_schema
    reason: The contract no longer takes a schema.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.states_admitting_a_decision
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.admitted_outcomes
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.self_check_parameters
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.self_check_rules
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.decided_actor_fields
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.states_admitting_a_decision
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.admitted_outcomes
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.self_check_parameters
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.self_check_rules
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    fact: .core.nodes.CC_RECORD_VERIFICATION_DECISION_V0.inputs.decided_actor_fields
    reason: The contract no longer takes this; it holds the rule or builds the record itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    fact: .core.nodes.CC_REQUIRE_REJECTION_GROUNDS_V0.inputs.grounds_parameters
    reason: The contract no longer takes this; it holds its rules and reads the grounds.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    fact: .core.nodes.CC_REQUIRE_REJECTION_GROUNDS_V0.inputs.grounds_rules
    reason: The contract no longer takes this; it holds its rules and reads the grounds.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    fact: .handler.payload_template.registration_schema
    reason: Identity holds what a registration must contain.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    fact: .handler.payload_template.actor_record.state
    reason: Registration writes the state unverified itself.
    source_finding: {phase: p6, register: boundary_rules, row: 4}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    fact: .handler.payload_template.decision
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    fact: .handler.payload_template.states_admitting_a_decision
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    fact: .handler.payload_template.admitted_outcomes
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    fact: .handler.payload_template.decided_actor_fields
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    fact: .handler.payload_template.self_check_parameters
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    fact: .handler.payload_template.self_check_rules
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    fact: .handler.payload_template.decision
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    fact: .handler.payload_template.states_admitting_a_decision
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    fact: .handler.payload_template.admitted_outcomes
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    fact: .handler.payload_template.decided_actor_fields
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    fact: .handler.payload_template.self_check_parameters
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    fact: .handler.payload_template.self_check_rules
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    fact: .handler.payload_template.grounds_parameters
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    fact: .handler.payload_template.grounds_rules
    reason: Identity holds this; the entrance stops supplying it.
    source_finding: {phase: p6, register: boundary_rules, row: 5}
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
