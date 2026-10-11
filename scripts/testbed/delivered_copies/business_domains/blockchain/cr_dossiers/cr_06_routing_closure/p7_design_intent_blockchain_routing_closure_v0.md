# Stage 7 — Design Intent: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p7
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Each step whose store can fail ends its contract on a failed record
    business_fact: No act carries on past a record it could not read or write
    resolution: The lookup and the read in blockchain::CC_RESOLVE_ACTOR_V1, the claim in blockchain::CC_CLAIM_WALLET_IDENTITY_V1, the write in blockchain::CC_CREATE_WALLET_RECORD_V1 and the append in blockchain::CC_APPEND_WALLET_OCCURRENCE_V1 each route BACKEND_ERROR to exit
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: Each act routes a failed record to its rejected ending
    business_fact: Every act ends as succeeded or rejected
    resolution: Every node of blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1, blockchain::WF_REJECT_ACTOR_V1 and blockchain::WF_CREATE_WALLET_V1 whose contract can end with BACKEND_ERROR routes it to EXIT_REJECTED
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: A contract that can now end with a failed record says so
    business_fact: A contract states every outcome it can end with
    resolution: The exit routes added above extend what blockchain::CC_RESOLVE_ACTOR_V1 and blockchain::CC_CLAIM_WALLET_IDENTITY_V1 can end with; the other two already end with it through their clock step
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: Records made before a failure are left as they are
    business_fact: The record is added to and never rewritten
    resolution: No compensation, repair or backfill step is designed
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: Each of the eight acts is stated under a next version
    business_fact: A change of meaning is a new identity, and identity is fixed at publication
    resolution: blockchain::CC_RESOLVE_ACTOR_V1, blockchain::CC_CLAIM_WALLET_IDENTITY_V1, blockchain::CC_CREATE_WALLET_RECORD_V1, blockchain::CC_APPEND_WALLET_OCCURRENCE_V1, blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1, blockchain::WF_REJECT_ACTOR_V1 and blockchain::WF_CREATE_WALLET_V1 each supersede their published version
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: The entrances and intents are re-pointed
    business_fact: Every caller starts the same act as today
    resolution: blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REJECT_ACTOR_V0, blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0 and blockchain::IN_WALLET_CREATION_V0 name the next version of the act they start, and nothing else in them changes
    source_finding: {phase: p4, register: design_decisions, row: 6}
  existing_inventory:
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    action: REPLACE
    summary: Answers which actor a contact address denotes, and reports when none does
    reason: A step carries on past a failed record its store declares. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    action: REPLACE
    summary: Claims the identity, and refuses when the person already holds a wallet
    reason: A step carries on past a failed record its store declares. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: blockchain::CC_CREATE_WALLET_RECORD_V0
    action: REPLACE
    summary: Records the wallet with a balance of zero, its denomination and its classification
    reason: A step carries on past a failed record its store declares. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    action: REPLACE
    summary: Records the moment on the wallet's trail
    reason: A step carries on past a failed record its store declares. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: blockchain::WF_REGISTER_ACTOR_V0
    action: REPLACE
    summary: The governed sequence that admits a person as an unverified actor, and announces that it did
    reason: It leaves a failed record unanswered. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: blockchain::WF_ACCEPT_ACTOR_V0
    action: REPLACE
    summary: The governed sequence that records an acceptance and announces it
    reason: It leaves a failed record unanswered. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: blockchain::WF_REJECT_ACTOR_V0
    action: REPLACE
    summary: The governed sequence that records a rejection, with grounds required, and announces it
    reason: It leaves a failed record unanswered. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: blockchain::WF_CREATE_WALLET_V0
    action: REPLACE
    summary: The governed sequence that gives an accepted person a wallet and records that it did
    reason: It leaves a failed record unanswered. Stood down by its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: capability_side_effects::CS_CLOCK_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - fqdn: blockchain::CC_REGISTER_ACTOR_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - fqdn: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::RB_WALLET_BINDINGS_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::STRUCTURE_WALLET_STORAGE_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    action: REPOINT
    summary: ''
    reason: Starts an act being replaced; re-pointed to its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  - fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    action: REPOINT
    summary: ''
    reason: Starts an act being replaced; re-pointed to its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 17}
  - fqdn: blockchain::EV_ACTOR_ACCEPTED_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::IN_ACTOR_REJECTION_V0
    action: REPOINT
    summary: ''
    reason: Starts an act being replaced; re-pointed to its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 18}
  - fqdn: blockchain::EV_ACTOR_REJECTED_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::IN_WALLET_CREATION_V0
    action: REPOINT
    summary: ''
    reason: Starts an act being replaced; re-pointed to its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 19}
  - fqdn: blockchain::EV_WALLET_CREATED_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    action: REUSE
    summary: ''
    reason: Named by a replaced artifact's next version, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: blockchain::AC_PARTICIPANT_V0
    action: REUSE
    summary: ''
    reason: The authority context the four acts run under, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: blockchain::TI_REGISTER_ACTOR_V0
    action: REPOINT
    summary: ''
    reason: Starts an act being replaced; re-pointed to its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    action: REPOINT
    summary: ''
    reason: Starts an act being replaced; re-pointed to its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    action: REPOINT
    summary: ''
    reason: Starts an act being replaced; re-pointed to its next version.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  new_artifacts:
  - capability: Look a person up
    family: CC
    code: blockchain::CC_RESOLVE_ACTOR_V1
    summary: Answers which actor a contact address denotes, and reports when none does
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 1}
  - capability: Claim a wallet's identity
    family: CC
    code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    summary: Claims the identity, and refuses when the person already holds a wallet
    owner_subdomain: wallet
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 2}
  - capability: Record a wallet
    family: CC
    code: blockchain::CC_CREATE_WALLET_RECORD_V1
    summary: Records the wallet with a balance of zero, its denomination and its classification
    owner_subdomain: wallet
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 2}
  - capability: Record a moment on a wallet's trail
    family: CC
    code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    summary: Records the moment on the wallet's trail
    owner_subdomain: wallet
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 2}
  - capability: Register a person
    family: WF
    code: blockchain::WF_REGISTER_ACTOR_V1
    summary: The governed sequence that admits a person as an unverified actor, and announces that it did
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 3}
  - capability: Accept a person
    family: WF
    code: blockchain::WF_ACCEPT_ACTOR_V1
    summary: The governed sequence that records an acceptance and announces it
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 3}
  - capability: Reject a person
    family: WF
    code: blockchain::WF_REJECT_ACTOR_V1
    summary: The governed sequence that records a rejection, with grounds required, and announces it
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 3}
  - capability: Create a wallet
    family: WF
    code: blockchain::WF_CREATE_WALLET_V1
    summary: The governed sequence that gives an accepted person a wallet and records that it did
    owner_subdomain: wallet
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 3}
  rb_declarations:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REGISTER_ACTOR_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_ACCEPT_ACTOR_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REJECT_ACTOR_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    binds_wf: blockchain::WF_CREATE_WALLET_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  execution_topology:
  - workflow: blockchain::WF_REGISTER_ACTOR_V1
    node: blockchain::IN_ACTOR_REGISTERED_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_VALIDATE_REGISTRATION_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - workflow: blockchain::WF_REGISTER_ACTOR_V1
    node: blockchain::CC_VALIDATE_REGISTRATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - workflow: blockchain::WF_REGISTER_ACTOR_V1
    node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_REGISTER_ACTOR_V0
      ALREADY_EXISTS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - workflow: blockchain::WF_REGISTER_ACTOR_V1
    node: blockchain::CC_REGISTER_ACTOR_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - workflow: blockchain::WF_REGISTER_ACTOR_V1
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - workflow: blockchain::WF_REGISTER_ACTOR_V1
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - workflow: blockchain::WF_REGISTER_ACTOR_V1
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: blockchain::IN_ACTOR_ACCEPTANCE_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: blockchain::CC_RESOLVE_ACTOR_V0
    runs: blockchain::CC_RESOLVE_ACTOR_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: blockchain::IN_ACTOR_REJECTION_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RESOLVE_ACTOR_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: blockchain::CC_RESOLVE_ACTOR_V0
    runs: blockchain::CC_RESOLVE_ACTOR_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: blockchain::IN_WALLET_CREATION_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: blockchain::CC_RESOLVE_ACTOR_V0
    runs: blockchain::CC_RESOLVE_ACTOR_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    runs: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CREATE_WALLET_RECORD_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: blockchain::CC_CREATE_WALLET_RECORD_V0
    runs: blockchain::CC_CREATE_WALLET_RECORD_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    runs: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  cc_composition:
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V1
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
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V1
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
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
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
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        result_status: result_status
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V1
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
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V1
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
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V1
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
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
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
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
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
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
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
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        stream_id: stream_id
        record: record
      out:
        result_status: result_status
  step_bindings:
  - owner: blockchain::CC_RESOLVE_ACTOR_V1
    step: resolve_address
    direction: INPUT
    field: key_or_address
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: resolve_address}
  - owner: blockchain::CC_RESOLVE_ACTOR_V1
    step: resolve_address
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
    source_finding: {phase: p7, register: cc_composition, key: resolve_address}
  - owner: blockchain::CC_RESOLVE_ACTOR_V1
    step: read_actor
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
    source_finding: {phase: p7, register: cc_composition, key: read_actor}
  - owner: blockchain::CC_RESOLVE_ACTOR_V1
    step: read_actor
    direction: OUTPUT
    field: value
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_actor}
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: claim_wallet_identity
    direction: INPUT
    field: key
    bound_to: inputs.wallet_id
    source_finding: {phase: p7, register: cc_composition, key: claim_wallet_identity}
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: claim_wallet_identity
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_wallet_identity}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V1
    step: read_created_at
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
    source_finding: {phase: p7, register: cc_composition, key: read_created_at}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V1
    step: assemble_wallet
    direction: INPUT
    field: fields
    bound_to: inputs.wallet_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_wallet}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V1
    step: assemble_wallet
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_wallet}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V1
    step: write_wallet
    direction: INPUT
    field: key
    bound_to: inputs.wallet_id
    source_finding: {phase: p7, register: cc_composition, key: write_wallet}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V1
    step: write_wallet
    direction: INPUT
    field: value
    bound_to: results.assemble_wallet.record
    source_finding: {phase: p7, register: cc_composition, key: write_wallet}
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V1
    step: write_wallet
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_wallet}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    step: read_occurred_at
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
    source_finding: {phase: p7, register: cc_composition, key: read_occurred_at}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to: inputs.occurrence_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_occurrence}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_occurrence}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to: inputs.stream_id
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    step: append_occurrence
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
    source_finding: {phase: p7, register: cc_composition, key: append_occurrence}
  - owner: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_VALIDATE_REGISTRATION_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_path
    bound_to: payload.address_path
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_type
    bound_to: payload.address_type
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V1
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
  - owner: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REGISTER_ACTOR_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: ACCEPTED
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: REJECTED
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: payload.stream_id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: holder_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: states_admitting_a_wallet
    bound_to:
      literal:
      - ACCEPTED
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: holder
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.contact_address
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_DETERMINE_WALLET_IDENTITY_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id_prefix
    bound_to: payload.wallet_id_prefix
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_DETERMINE_WALLET_IDENTITY_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CLAIM_WALLET_IDENTITY_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    bound_to: payload.key_material
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CREATE_WALLET_RECORD_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_fields
    bound_to: payload.wallet_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_CREATE_WALLET_RECORD_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_WALLET_OCCURRENCE_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to: payload.occurrence_fields
    source_finding: {phase: p7, register: execution_topology, key: 'blockchain::CC_APPEND_WALLET_OCCURRENCE_V0'}
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  interface_fields:
  - artifact: blockchain::CC_RESOLVE_ACTOR_V1
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The address naming the actor to resolve
  - artifact: blockchain::CC_RESOLVE_ACTOR_V1
    direction: OUTPUT
    field: value
    type: object
    required: 'YES'
    default: ''
    meaning: The actor and its current state, or absent when none is held
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    direction: INPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: ''
    meaning: The identity being claimed.
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the claim succeeded, or the identity was already held.
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V1
    direction: INPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: ''
    meaning: The wallet being recorded.
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V1
    direction: INPUT
    field: wallet_fields
    type: object
    required: 'YES'
    default: ''
    meaning: What the business holds about the wallet.
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V1
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the wallet was recorded.
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    direction: INPUT
    field: stream_id
    type: string
    required: 'YES'
    default: ''
    meaning: The trail the moment is added to.
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    direction: INPUT
    field: occurrence_fields
    type: object
    required: 'YES'
    default: ''
    meaning: What the moment records.
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: ''
    meaning: Whether the moment was recorded.
  artifact_properties:
  - artifact: blockchain::WF_REGISTER_ACTOR_V1
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V1
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_ACCEPTED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - artifact: blockchain::WF_ACCEPT_ACTOR_V1
    property: supersedes
    value:
    - blockchain::WF_ACCEPT_ACTOR_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - artifact: blockchain::WF_REJECT_ACTOR_V1
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REJECTED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::WF_REJECT_ACTOR_V1
    property: supersedes
    value:
    - blockchain::WF_REJECT_ACTOR_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: blockchain::WF_CREATE_WALLET_V1
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_WALLET_CREATED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: blockchain::WF_REGISTER_ACTOR_V1
    property: supersedes
    value:
    - blockchain::WF_REGISTER_ACTOR_V0
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - artifact: blockchain::WF_CREATE_WALLET_V1
    property: supersedes
    value:
    - blockchain::WF_CREATE_WALLET_V0
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - artifact: blockchain::CC_RESOLVE_ACTOR_V1
    property: supersedes
    value:
    - blockchain::CC_RESOLVE_ACTOR_V0
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    property: supersedes
    value:
    - blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V1
    property: supersedes
    value:
    - blockchain::CC_CREATE_WALLET_RECORD_V0
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    property: supersedes
    value:
    - blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    source_finding: {phase: p4, register: design_decisions, row: 5}
  structure_stores:
  - store_name: WALLET_IDENTITIES
    storage_type: CS_REGISTRY_V0
    proposed_path: blockchain/wallet/wallet_identity_registry.jsonl
    used_by: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - store_name: WALLETS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: blockchain/wallet/wallets.json
    used_by: blockchain::CC_CREATE_WALLET_RECORD_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - store_name: WALLET_OCCURRENCES
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: blockchain/wallet/wallet_occurrences.jsonl
    used_by: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  artifact_summary:
  - action: NEW
    subdomain: identity
    count: '4'
    artifacts: blockchain::CC_RESOLVE_ACTOR_V1, blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1, blockchain::WF_REJECT_ACTOR_V1
  - action: NEW
    subdomain: wallet
    count: '4'
    artifacts: blockchain::CC_CLAIM_WALLET_IDENTITY_V1, blockchain::CC_CREATE_WALLET_RECORD_V1, blockchain::CC_APPEND_WALLET_OCCURRENCE_V1, blockchain::WF_CREATE_WALLET_V1
  - action: REPLACE
    subdomain: identity
    count: '4'
    artifacts: blockchain::CC_RESOLVE_ACTOR_V0, blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0
  - action: REPLACE
    subdomain: wallet
    count: '4'
    artifacts: blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_CREATE_WALLET_RECORD_V0, blockchain::CC_APPEND_WALLET_OCCURRENCE_V0, blockchain::WF_CREATE_WALLET_V0
  declared_reach:
  - act: blockchain::WF_CREATE_WALLET_V1
    consults:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  implementation_bindings: null
  vocabulary_extensions: null
  runtime_policies: null
  transport_bindings: null
  generation_provenance: null
  refusal_discharge:
  - operation: Registering a person
    refused_when: A record the registration needs fails
    act: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Registering a person
    refused_when: A record the registration needs fails
    act: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_REGISTER_ACTOR_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Registering a person
    refused_when: A record the registration needs fails
    act: blockchain::WF_REGISTER_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Accepting a person
    refused_when: A record the acceptance needs fails
    act: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_RESOLVE_ACTOR_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Accepting a person
    refused_when: A record the acceptance needs fails
    act: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Accepting a person
    refused_when: A record the acceptance needs fails
    act: blockchain::WF_ACCEPT_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Rejecting a person
    refused_when: A record the rejection needs fails
    act: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_RESOLVE_ACTOR_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Rejecting a person
    refused_when: A record the rejection needs fails
    act: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Rejecting a person
    refused_when: A record the rejection needs fails
    act: blockchain::WF_REJECT_ACTOR_V1
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Creating a wallet
    refused_when: A record the wallet needs fails
    act: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_RESOLVE_ACTOR_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Creating a wallet
    refused_when: A record the wallet needs fails
    act: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Creating a wallet
    refused_when: A record the wallet needs fails
    act: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_CREATE_WALLET_RECORD_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Creating a wallet
    refused_when: A record the wallet needs fails
    act: blockchain::WF_CREATE_WALLET_V1
    step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    outcome: BACKEND_ERROR
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  refusal_deferrals: null
  refusal_governance_discharge: null
  molecule_steps: null
  molecule_step_bindings: null
  test_cases: null
  test_case_values: null
  withdrawn_facts: null
```

Every binding names a field the capability declares, read from the pinned baseline
`f8356d9c8938aea16ab7850d7bda964d8d16c42c64e5db9056d5fe58040ec1d0`.

Eight acts identity and wallet published in v5 are replaced by their next versions, and the published
versions are stood down unchanged. The next versions of four contracts answer a failed record at the
five steps whose stores declare one. The next versions of four acts route a failed record to the
rejected ending they already have, at thirteen nodes, and keep every place label; a place whose
contract is replaced runs its next version. The three entrances and four intents that start an act
are re-pointed to its next version. Every other step, route, binding and field is restated exactly as
it stands.

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

## 9. Artifact Properties

---

## 10. Structure Stores

---

## 11. Artifact Summary

---

## 12. Declared Reach

---

## 13. Unchanged Registers

No transform, vocabulary, policy, entrance or generator is touched.

---

## 14. Refusal Discharge

Each refusal the business named is discharged where a failed record reaches the rejected ending.

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn: every next version keeps every fact its published version has and gains one answer.
