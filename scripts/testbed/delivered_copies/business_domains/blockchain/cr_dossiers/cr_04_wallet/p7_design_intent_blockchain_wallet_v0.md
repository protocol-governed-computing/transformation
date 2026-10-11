# Stage 7 — Design Intent: blockchain / wallet

## Machine

```yaml
document:
  phase: p7
  domain: blockchain
  subdomain: wallet
  cr: cr_04_wallet
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Wallet is a subdomain of its own
    business_fact: A wallet is a thing the business holds in its own right
    resolution: '`wallet` subdomain, owning three stores and writing no store identity owns'
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: Working out an address is pure computation
    business_fact: The same key material always yields the same address
    resolution: '`blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0`, a transform; the closed side-effect set is unchanged'
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: Key material is supplied, never generated
    business_fact: The same request must produce the same wallet
    resolution: The transform takes the material as a declared input and derives nothing at random
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: A wallet's identity is derived from its holder
    business_fact: One person holds one wallet
    resolution: '`CT_PURE_GENERATE_ID_V0` over the holder''s identity alone'
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: The declared moments are announced from where the operations record what they did
    business_fact: The moments already exist and are referred to by nothing
    resolution: '`emit:` on the terminal node of each identity workflow'
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: Wallet creation is refused for a person not held, not accepted, or already holding a wallet
    business_fact: The business stated each refusal
    resolution: Declared outcomes routing to a terminal node, never an unhandled path
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - decision: Acceptance stands on its own
    business_fact: A wallet that cannot be created does not un-accept the person
    resolution: Wallet creation is a separate workflow; identity's workflows terminate without it
    source_finding: {phase: p4, register: design_decisions, row: 7}
  - decision: The deciding workflow is split rather than amended
    business_fact: A rejection must state grounds, and each outcome must announce
    resolution: Two workflows replace one, each with its own admission and its own terminal node to announce from
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  existing_inventory:
  - fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    action: REPLACE
    summary: ''
    reason: Superseded by two workflows, one per outcome, each announcing its own moment and the rejection requiring grounds throughout.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: blockchain::IN_ACTOR_VERIFIED_V0
    action: REPLACE
    summary: ''
    reason: Superseded by an acceptance intent and a rejection intent. One intent dispatches one workflow, so a decision split in two leaves this one nothing to dispatch.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    action: EXTEND
    summary: Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the decision, admitted states and outcomes, and the acceptance occurrence label
    reason: Its handler routes to the workflow this change stands down, and must reach the acceptance path instead.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    action: EXTEND
    summary: Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the decision, admitted states and outcomes, and the rejection occurrence label
    reason: Its handler routes to the workflow this change stands down, and must reach the rejection path and supply the grounds it checks.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: blockchain::WF_REGISTER_ACTOR_V0
    action: EXTEND
    summary: The governed sequence that admits a person as an unverified actor, and announces that it did
    reason: Its terminal node announces nothing. Everything else about it is unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    action: EXTEND
    summary: Refuses every declared refusal and moves the actor to its decided state
    reason: Its self-verification step computed whether the decider is the subject and routed on whether the *transform ran*, so a person could decide about themselves. The step must refuse on what it found, not on the fact that it looked.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    action: REUSE
    summary: ''
    reason: Resolves a person and carries their state; wallet reads it and identity's workflows keep it.
    source_finding: {phase: p5, register: cross_subdomain_refs, row: 1}
  - fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    action: REUSE
    summary: ''
    reason: Records a moment on a person's trail, unchanged.
    source_finding: {phase: p3, register: dependency_discoveries, row: 8}
  - fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    action: REUSE
    summary: ''
    reason: Admits a registration, unchanged; the registration workflow is redeclared whole and runs it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    action: REUSE
    summary: ''
    reason: Validates a registration, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    action: REUSE
    summary: ''
    reason: Claims a contact address, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: blockchain::CC_REGISTER_ACTOR_V0
    action: REUSE
    summary: ''
    reason: Records the person, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: blockchain::EV_ACTOR_ACCEPTED_V0
    action: REUSE
    summary: ''
    reason: Declared already; this change refers to it for the first time.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    action: REUSE
    summary: ''
    reason: The same.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: blockchain::EV_ACTOR_REJECTED_V0
    action: REUSE
    summary: ''
    reason: The same.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: blockchain::AC_PARTICIPANT_V0
    action: REUSE
    summary: ''
    reason: The authority context both identity workflows already run under.
    source_finding: {phase: p6, register: ownership, row: 10}
  - fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
    action: EXTEND
    summary: The bindings identity's workflows resolve their capabilities and stores through
    reason: Two new workflows must bind through it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
    action: EXTEND
    summary: Declares what the blockchain domain compiles
    reason: It knows of one subdomain and must know of two.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REUSE
    summary: ''
    reason: Holds a wallet.
    source_finding: {phase: p6, register: ownership, row: 6}
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: ''
    reason: Holds a wallet's trail.
    source_finding: {phase: p6, register: ownership, row: 7}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    action: REUSE
    summary: ''
    reason: Claims a wallet's identity.
    source_finding: {phase: p6, register: ownership, row: 9}
  - fqdn: capability_side_effects::CS_CLOCK_V0
    action: REUSE
    summary: ''
    reason: Supplies the time a moment occurred.
    source_finding: {phase: p6, register: ownership, row: 11}
  - fqdn: capability_transforms::CT_PURE_GENERATE_ID_V0
    action: REUSE
    summary: ''
    reason: Derives a wallet's identity from its holder.
    source_finding: {phase: p6, register: ownership, row: 8}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    action: REUSE
    summary: ''
    reason: Refuses a value outside the set the business admits — the state a decision may be made from, and the outcomes it may carry.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: ''
    reason: Assembles a record from declared fields.
    source_finding: {phase: p7, register: cc_composition, row: 5}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    action: REUSE
    summary: ''
    reason: Judges a parameter against declared rules.
    source_finding: {phase: p7, register: cc_composition, row: 10}
  - fqdn: blockchain::IN_WALLET_CREATION_V0
    action: EXTEND
    summary: Admits a request naming the person a wallet is for, and refuses one that names nobody
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 1}
  - fqdn: blockchain::WF_CREATE_WALLET_V0
    action: EXTEND
    summary: The governed sequence that gives an accepted person a wallet and records that it did
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 2}
  - fqdn: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    action: EXTEND
    summary: Derives the wallet's identity from the person who holds it
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 3}
  - fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    action: EXTEND
    summary: Claims the identity, and refuses when the person already holds a wallet
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 4}
  - fqdn: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    action: EXTEND
    summary: Establishes the address from key material supplied with the request
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 5}
  - fqdn: blockchain::CC_CREATE_WALLET_RECORD_V0
    action: EXTEND
    summary: Records the wallet with a balance of zero, its denomination and its classification
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 6}
  - fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    action: EXTEND
    summary: Records the moment on the wallet's trail
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 7}
  - fqdn: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    action: EXTEND
    summary: Derives an address from supplied key material; the same material always yields the same address
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 8}
  - fqdn: blockchain::EV_WALLET_CREATED_V0
    action: EXTEND
    summary: Announces that a wallet was created, for whom, and when
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 9}
  - fqdn: blockchain::RB_WALLET_BINDINGS_V0
    action: EXTEND
    summary: Binds the wallet workflow to the capabilities and stores it uses
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 10}
  - fqdn: blockchain::STRUCTURE_WALLET_STORAGE_V0
    action: EXTEND
    summary: Declares the three stores wallet owns
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 11}
  - fqdn: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    action: EXTEND
    summary: The fixed set of wallet classifications, of which only the default is used
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 12}
  - fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    action: EXTEND
    summary: Admits a request to accept a person, and refuses one that names nobody
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 13}
  - fqdn: blockchain::IN_ACTOR_REJECTION_V0
    action: EXTEND
    summary: Admits a request to reject a person, and refuses one that states no grounds
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 14}
  - fqdn: blockchain::WF_ACCEPT_ACTOR_V0
    action: EXTEND
    summary: The governed sequence that records an acceptance and announces it
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 15}
  - fqdn: blockchain::WF_REJECT_ACTOR_V0
    action: EXTEND
    summary: The governed sequence that records a rejection, with grounds required, and announces it
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 16}
  - fqdn: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    action: EXTEND
    summary: Refuses a rejection stating no grounds, before anything is recorded
    reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
    source_finding: {phase: p5, register: provisional_codes, row: 17}
  new_artifacts:
  - capability: Refusing a wallet to a person the business has not accepted
    family: CC
    code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    summary: Refuses a wallet for a person the business has not accepted, before anything is claimed or recorded
    owner_subdomain: wallet
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, row: 3}
  rb_declarations:
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    binds_wf: blockchain::WF_CREATE_WALLET_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
    source_finding: {phase: p5, register: provisional_codes, row: 10}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_ACCEPT_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REJECT_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REGISTER_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  execution_topology:
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: blockchain::IN_WALLET_CREATION_V0
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p5, register: actions, row: 1}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: blockchain::CC_RESOLVE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p5, register: provisional_codes, row: 3}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p5, register: provisional_codes, row: 4}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CREATE_WALLET_RECORD_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p5, register: provisional_codes, row: 5}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: blockchain::CC_CREATE_WALLET_RECORD_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p5, register: provisional_codes, row: 6}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p5, register: provisional_codes, row: 7}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
    source_finding: {phase: p5, register: provisional_codes, row: 9}
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p5, register: invariants, row: 4}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: blockchain::IN_ACTOR_ACCEPTANCE_V0
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p5, register: provisional_codes, row: 13}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: blockchain::CC_RESOLVE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p3, register: dependency_discoveries, row: 8}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p5, register: invariants, row: 4}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::IN_ACTOR_REJECTION_V0
    node_type: IN
    routing:
      ACK: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p5, register: provisional_codes, row: 14}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RESOLVE_ACTOR_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p4, register: gap_register, key: GAP-5}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::CC_RESOLVE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p3, register: dependency_discoveries, row: 8}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p5, register: invariants, row: 4}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::IN_ACTOR_REGISTERED_V0
    node_type: IN
    routing:
      ACK: blockchain::CC_VALIDATE_REGISTRATION_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_VALIDATE_REGISTRATION_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_REGISTER_ACTOR_V0
      ALREADY_EXISTS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_REGISTER_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  cc_composition:
  - cc_code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    step: '1'
    step_name: require_holder_accepted
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
        value: holder_state
        allowed_set: states_admitting_a_wallet
      out:
        is_member: is_accepted
  - cc_code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    step: '1'
    step_name: derive_wallet_identity
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: GENERATE_ID
    store: null
    consumes:
    - data
    - prefix
    produces:
    - id
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        data: data
        prefix: prefix
      out:
        id: id
  - cc_code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    step: '1'
    step_name: claim_wallet_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: WALLET_IDENTITIES
    consumes:
    - key
    produces:
    - result_status
    routing:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        result_status: result_status
  - cc_code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    step: '1'
    step_name: derive_wallet_address
    capability: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    kind: CT
    operation: DERIVE_WALLET_ADDRESS
    store: null
    consumes:
    - key_material
    produces:
    - address
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_material: key_material
      out:
        address: address
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: '1'
    step_name: read_created_at
    capability: capability_side_effects::CS_CLOCK_V0
    kind: CS
    operation: NOW
    store: null
    consumes: []
    produces:
    - timestamp
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: {}
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: '2'
    step_name: assemble_wallet
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
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: '3'
    step_name: write_wallet
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: WALLETS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: '1'
    step_name: read_occurred_at
    capability: capability_side_effects::CS_CLOCK_V0
    kind: CS
    operation: NOW
    store: null
    consumes: []
    produces:
    - timestamp
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: {}
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
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
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: '3'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: WALLET_OCCURRENCES
    consumes:
    - stream_id
    - record
    produces:
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        stream_id: stream_id
        record: record
      out:
        result_status: result_status
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
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
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
    interface: {}
  - cc_code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: '1'
    step_name: require_grounds_stated
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  step_bindings:
  - owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    step: derive_wallet_identity
    direction: INPUT
    field: data
    bound_to: inputs.holder
    source_finding: {phase: p7, register: cc_composition, key: derive_wallet_identity}
  - owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    step: derive_wallet_identity
    direction: INPUT
    field: prefix
    bound_to: inputs.wallet_id_prefix
    source_finding: {phase: p7, register: cc_composition, key: derive_wallet_identity}
  - owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    step: derive_wallet_identity
    direction: OUTPUT
    field: id
    bound_to: capability_result.id
    source_finding: {phase: p7, register: cc_composition, key: derive_wallet_identity}
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    step: claim_wallet_identity
    direction: INPUT
    field: key
    bound_to: inputs.wallet_id
    source_finding: {phase: p7, register: cc_composition, key: claim_wallet_identity}
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    step: claim_wallet_identity
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_wallet_identity}
  - owner: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    step: derive_wallet_address
    direction: INPUT
    field: key_material
    bound_to: inputs.key_material
    source_finding: {phase: p7, register: cc_composition, key: derive_wallet_address}
  - owner: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    step: derive_wallet_address
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
    source_finding: {phase: p7, register: cc_composition, key: derive_wallet_address}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: read_created_at
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
    source_finding: {phase: p7, register: cc_composition, key: read_created_at}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: assemble_wallet
    direction: INPUT
    field: fields
    bound_to: inputs.wallet_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_wallet}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: assemble_wallet
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_wallet}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: write_wallet
    direction: INPUT
    field: key
    bound_to: inputs.wallet_id
    source_finding: {phase: p7, register: cc_composition, key: write_wallet}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: write_wallet
    direction: INPUT
    field: value
    bound_to: results.assemble_wallet.record
    source_finding: {phase: p7, register: cc_composition, key: write_wallet}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: write_wallet
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_wallet}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: read_occurred_at
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
    source_finding: {phase: p7, register: cc_composition, key: read_occurred_at}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to: inputs.occurrence_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_occurrence}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_occurrence}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to: inputs.stream_id
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: append_occurrence
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
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
    field: parameters
    bound_to: inputs.self_check_parameters
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_verification}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_verification
    direction: INPUT
    field: rules
    bound_to: inputs.self_check_rules
    source_finding: {phase: p7, register: cc_composition, key: refuse_self_verification}
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_verification
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
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
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: self_check_parameters
    bound_to: payload.self_check_parameters
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: self_check_rules
    bound_to: payload.self_check_rules
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: self_check_parameters
    bound_to: payload.self_check_parameters
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: self_check_rules
    bound_to: payload.self_check_rules
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: require_grounds_stated
    direction: INPUT
    field: parameters
    bound_to: inputs.grounds_parameters
    source_finding: {phase: p7, register: cc_composition, key: require_grounds_stated}
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: require_grounds_stated
    direction: INPUT
    field: rules
    bound_to: inputs.grounds_rules
    source_finding: {phase: p7, register: cc_composition, key: require_grounds_stated}
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: require_grounds_stated
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_grounds_stated}
  - owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    step: require_holder_accepted
    direction: INPUT
    field: value
    bound_to: inputs.holder_state
    source_finding: {phase: p7, register: cc_composition, key: require_holder_accepted}
  - owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    step: require_holder_accepted
    direction: INPUT
    field: allowed_set
    bound_to: inputs.states_admitting_a_wallet
    source_finding: {phase: p7, register: cc_composition, key: require_holder_accepted}
  - owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    step: require_holder_accepted
    direction: OUTPUT
    field: is_accepted
    bound_to: capability_result.is_member
    source_finding: {phase: p7, register: cc_composition, key: require_holder_accepted}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: holder_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: states_admitting_a_wallet
    bound_to:
      literal:
      - ACCEPTED
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: holder
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_DETERMINE_WALLET_IDENTITY_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id_prefix
    bound_to: payload.wallet_id_prefix
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_DETERMINE_WALLET_IDENTITY_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CLAIM_WALLET_IDENTITY_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    bound_to: payload.key_material
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CREATE_WALLET_RECORD_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_fields
    bound_to: payload.wallet_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CREATE_WALLET_RECORD_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_WALLET_OCCURRENCE_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_WALLET_OCCURRENCE_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds_parameters
    bound_to: payload.grounds_parameters
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds_rules
    bound_to: payload.grounds_rules
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p3, register: dependency_discoveries, row: 8}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: states_admitting_a_decision
    bound_to: payload.states_admitting_a_decision
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to: payload.decision
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: admitted_outcomes
    bound_to: payload.admitted_outcomes
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decided_actor_fields
    bound_to: payload.decided_actor_fields
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: states_admitting_a_decision
    bound_to: payload.states_admitting_a_decision
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to: payload.decision
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: admitted_outcomes
    bound_to: payload.admitted_outcomes
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decided_actor_fields
    bound_to: payload.decided_actor_fields
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: registration_schema
    bound_to: payload.registration_schema
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_path
    bound_to: payload.address_path
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_type
    bound_to: payload.address_type
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: actor_fields
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ACTOR_V0}
  interface_fields:
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    type: string
    required: 'YES'
    default: ''
    meaning: The state the actor is in when the decision is made.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: states_admitting_a_decision
    type: array
    required: 'YES'
    default: ''
    meaning: The states from which a decision may be made.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    type: string
    required: 'YES'
    default: ''
    meaning: The outcome being recorded.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: admitted_outcomes
    type: array
    required: 'YES'
    default: ''
    meaning: The outcomes the business admits.
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
    field: decided_actor_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The actor record as it will stand once decided.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: self_check_parameters
    type: object
    required: 'YES'
    default: ''
    meaning: The decider and the subject, as the parameter map the rule evaluator reads.
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: self_check_rules
    type: array
    required: 'YES'
    default: ''
    meaning: 'The rule the decider must satisfy: not the person being decided about.'
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the decision was recorded.
  - artifact: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    type: string
    required: 'YES'
    default: ''
    meaning: The public key material supplied with the request. Never generated here.
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
  - artifact: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: ''
    meaning: The address others may pay to. The same material always yields the same address.
  - artifact: blockchain::IN_WALLET_CREATION_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The person the wallet is for.
  - artifact: blockchain::IN_WALLET_CREATION_V0
    direction: INPUT
    field: key_material
    type: string
    required: 'YES'
    default: ''
    meaning: The key material the address is worked out from.
  - artifact: blockchain::IN_WALLET_CREATION_V0
    direction: INPUT
    field: wallet_id_prefix
    type: string
    required: 'YES'
    default: ''
    meaning: The prefix a wallet identity carries, so the identity is recognisable as a wallet.
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
  - artifact: blockchain::IN_ACTOR_REJECTION_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The person being rejected.
  - artifact: blockchain::IN_ACTOR_REJECTION_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority recording the rejection.
  - artifact: blockchain::IN_ACTOR_REJECTION_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'YES'
    default: ''
    meaning: Why the person is refused. A rejection stating none is refused.
  - artifact: blockchain::EV_WALLET_CREATED_V0
    direction: ATTRIBUTE
    field: wallet_id
    type: string
    required: 'YES'
    default: ''
    meaning: The wallet created.
  - artifact: blockchain::EV_WALLET_CREATED_V0
    direction: ATTRIBUTE
    field: holder
    type: string
    required: 'YES'
    default: ''
    meaning: The person it belongs to.
  - artifact: blockchain::EV_WALLET_CREATED_V0
    direction: ATTRIBUTE
    field: occurred_at
    type: string
    required: 'YES'
    default: ''
    meaning: When it was created.
  - artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: holder
    type: string
    required: 'YES'
    default: ''
    meaning: The person the wallet belongs to.
  - artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id_prefix
    type: string
    required: 'YES'
    default: ''
    meaning: The prefix a wallet identity carries.
  - artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: OUTPUT
    field: id
    type: string
    required: 'YES'
    default: ''
    meaning: The identity derived for the wallet.
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: ''
    meaning: The identity being claimed.
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the claim succeeded, or the identity was already held.
  - artifact: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    type: string
    required: 'YES'
    default: ''
    meaning: The key material supplied with the request.
  - artifact: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: ''
    meaning: The address others may pay to.
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: ''
    meaning: The wallet being recorded.
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_fields
    type: object
    required: 'YES'
    default: ''
    meaning: What the business holds about the wallet.
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the wallet was recorded.
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    type: string
    required: 'YES'
    default: ''
    meaning: The trail the moment is added to.
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    type: object
    required: 'YES'
    default: ''
    meaning: What the moment records.
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the moment was recorded.
  - artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: holder_state
    type: string
    required: 'YES'
    default: ''
    meaning: The state the person is in, read from the record identity holds.
  - artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: states_admitting_a_wallet
    type: array
    required: 'YES'
    default: ''
    meaning: The states a wallet may be created from. Acceptance, and nothing else — fixed by the design, never taken from the caller, because a rule the caller supplies is a rule the caller can widen.
  - artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: OUTPUT
    field: is_accepted
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the person is one the business has accepted.
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds_parameters
    type: object
    required: 'YES'
    default: ''
    meaning: The grounds, as the parameter map the rule evaluator reads.
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds_rules
    type: array
    required: 'YES'
    default: ''
    meaning: 'The rules the grounds must satisfy: stated at all, and not empty.'
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether grounds were stated.
  implementation_bindings:
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    callable: execute
    operation: DERIVE_WALLET_ADDRESS
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding: {phase: p4, register: design_decisions, row: 3}
  vocabulary_extensions:
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    value: DEFAULT
    meaning: The only classification this change creates.
    source_finding: {phase: p5, register: known_facts, row: 15}
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    value: PRIVATE
    meaning: Named and unused until a business need arises.
    source_finding: {phase: p5, register: known_facts, row: 15}
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    value: BUSINESS
    meaning: Named and unused.
    source_finding: {phase: p5, register: known_facts, row: 15}
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    value: SAVINGS
    meaning: Named and unused.
    source_finding: {phase: p5, register: known_facts, row: 15}
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    value: INVESTMENT
    meaning: Named and unused.
    source_finding: {phase: p5, register: known_facts, row: 15}
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    value: MINT
    meaning: Named and unused.
    source_finding: {phase: p5, register: known_facts, row: 15}
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    value: BURN
    meaning: Named and unused.
    source_finding: {phase: p5, register: known_facts, row: 15}
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    value: POOL
    meaning: Named and unused.
    source_finding: {phase: p5, register: known_facts, row: 15}
  runtime_policies:
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: store
    value: WALLETS
    source_finding: {phase: p7, register: structure_stores, row: 1}
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: store
    value: WALLET_OCCURRENCES
    source_finding: {phase: p7, register: structure_stores, row: 2}
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: store
    value: WALLET_IDENTITIES
    source_finding: {phase: p7, register: structure_stores, row: 3}
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    capability: capability_side_effects::CS_CLOCK_V0
    key: policy
    value: utc
    source_finding: {phase: p7, register: rb_declarations, row: 1}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p7, register: existing_inventory, key: RB_IDENTITY_BINDINGS_V0}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p7, register: existing_inventory, key: RB_IDENTITY_BINDINGS_V0}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p7, register: existing_inventory, key: RB_IDENTITY_BINDINGS_V0}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_CLOCK_V0
    key: precision
    value: seconds
    source_finding: {phase: p7, register: existing_inventory, key: RB_IDENTITY_BINDINGS_V0}
  artifact_properties:
  - artifact: blockchain::WF_CREATE_WALLET_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_WALLET_CREATED_V0
    source_finding: {phase: p7, register: execution_topology, row: 8}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_ACCEPTED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REJECTED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    property: supersedes
    value:
    - blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    property: supersedes
    value:
    - blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    property: supersedes
    value:
    - blockchain::IN_ACTOR_VERIFIED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::IN_ACTOR_REJECTION_V0
    property: supersedes
    value:
    - blockchain::IN_ACTOR_VERIFIED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  transport_bindings:
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: decision
    bound_to:
      literal: ACCEPTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: states_admitting_a_decision
    bound_to:
      literal:
      - UNVERIFIED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: admitted_outcomes
    bound_to:
      literal:
      - ACCEPTED
      - REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: decided_actor_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: decided_actor_fields.state
    bound_to:
      literal: ACCEPTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: decided_actor_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: decided_actor_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: self_check_parameters.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: self_check_parameters.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: self_check_rules
    bound_to:
      literal:
      - field: verifying_authority
        op: neq
        value: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: occurrence_fields.occurrence
    bound_to:
      literal: ACTOR_ACCEPTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: occurrence_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: occurrence_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: occurrence_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: decision
    bound_to:
      literal: REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: states_admitting_a_decision
    bound_to:
      literal:
      - UNVERIFIED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: admitted_outcomes
    bound_to:
      literal:
      - ACCEPTED
      - REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: decided_actor_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: decided_actor_fields.state
    bound_to:
      literal: REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: decided_actor_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: decided_actor_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: self_check_parameters.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: self_check_parameters.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: self_check_rules
    bound_to:
      literal:
      - field: verifying_authority
        op: neq
        value: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: occurrence_fields.occurrence
    bound_to:
      literal: ACTOR_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: occurrence_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: occurrence_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: occurrence_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: grounds_parameters.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: grounds_rules
    bound_to:
      literal:
      - field: grounds
        op: not_null
      - field: grounds
        op: neq
        value: ''
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  structure_stores:
  - store_name: WALLETS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: blockchain/wallet/wallets.json
    used_by: blockchain::CC_CREATE_WALLET_RECORD_V0
    source_finding: {phase: p5, register: business_objects, row: 1}
  - store_name: WALLET_OCCURRENCES
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: blockchain/wallet/wallet_occurrences.jsonl
    used_by: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    source_finding: {phase: p5, register: business_objects, row: 2}
  - store_name: WALLET_IDENTITIES
    storage_type: CS_REGISTRY_V0
    proposed_path: blockchain/wallet/wallet_identity_registry.jsonl
    used_by: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    source_finding: {phase: p5, register: business_objects, row: 3}
  artifact_summary:
  - action: NEW
    subdomain: wallet
    count: '1'
    artifacts: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
  - action: EXTEND
    subdomain: wallet
    count: '13'
    artifacts: blockchain::IN_WALLET_CREATION_V0, blockchain::WF_CREATE_WALLET_V0, blockchain::CC_DETERMINE_WALLET_IDENTITY_V0, blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0, blockchain::CC_CREATE_WALLET_RECORD_V0, blockchain::CC_APPEND_WALLET_OCCURRENCE_V0, blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0, blockchain::EV_WALLET_CREATED_V0, blockchain::RB_WALLET_BINDINGS_V0, blockchain::STRUCTURE_WALLET_STORAGE_V0, blockchain::VOCAB_WALLET_CLASSIFICATION_V0, blockchain::AC_PARTICIPANT_V0
  - action: EXTEND
    subdomain: identity
    count: '9'
    artifacts: blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0, blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0, blockchain::WF_REGISTER_ACTOR_V0, blockchain::RB_IDENTITY_BINDINGS_V0, blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0, blockchain::TI_ACCEPT_ACTOR_V0
  generation_provenance:
  - artifact: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
    generator: transformation.build.render:build_manifest
    generator_sources:
    - S8 build_order
    - S8 field_declarations
    - transformation/design/families.py
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  declared_reach:
  - act: blockchain::WF_CREATE_WALLET_V0
    consults:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-9}
```

HOW it is realised. Binding identities are assigned here.

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

## 14. Transport Bindings

## 13. STRUCTURE Stores

---

## 15. Artifact Summary

---

## 16. Generation Provenance

*One artifact this design amends is derived rather than designed. The build manifest states which
layers the compiler searches, how the namespace is matched and where projections are written —
every field of it computed from the domain, its subdomains and its families, none of it decided
here. It is reached by invoking the generator that already derives it, so this design states the
path to it and not its contents. Everything else is authored and is its own source of truth.*

---

## 17. Declared Reach
