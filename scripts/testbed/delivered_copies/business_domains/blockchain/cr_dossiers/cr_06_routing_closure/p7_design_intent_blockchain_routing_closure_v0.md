# Stage 7 — Design Intent: blockchain / identity and wallet

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_06_routing_closure
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
    - Decision: Each step whose store can fail ends its contract on a failed record
      Business Fact: No act carries on past a record it could not read or write
      Resolution: The lookup and the read in blockchain::CC_RESOLVE_ACTOR_V1, the claim in blockchain::CC_CLAIM_WALLET_IDENTITY_V1, the write in blockchain::CC_CREATE_WALLET_RECORD_V1 and the append in blockchain::CC_APPEND_WALLET_OCCURRENCE_V1 each route BACKEND_ERROR to exit
      Source Finding: 'S4 design_decisions #1'
    - Decision: Each act routes a failed record to its rejected ending
      Business Fact: Every act ends as succeeded or rejected
      Resolution: Every node of blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1, blockchain::WF_REJECT_ACTOR_V1 and blockchain::WF_CREATE_WALLET_V1 whose contract can end with BACKEND_ERROR routes it to EXIT_REJECTED
      Source Finding: 'S4 design_decisions #2'
    - Decision: A contract that can now end with a failed record says so
      Business Fact: A contract states every outcome it can end with
      Resolution: The exit routes added above extend what blockchain::CC_RESOLVE_ACTOR_V1 and blockchain::CC_CLAIM_WALLET_IDENTITY_V1 can end with; the other two already end with it through their clock step
      Source Finding: 'S4 design_decisions #3'
    - Decision: Records made before a failure are left as they are
      Business Fact: The record is added to and never rewritten
      Resolution: No compensation, repair or backfill step is designed
      Source Finding: 'S4 design_decisions #4'
    - Decision: Each of the eight acts is stated under a next version
      Business Fact: A change of meaning is a new identity, and identity is fixed at publication
      Resolution: blockchain::CC_RESOLVE_ACTOR_V1, blockchain::CC_CLAIM_WALLET_IDENTITY_V1, blockchain::CC_CREATE_WALLET_RECORD_V1, blockchain::CC_APPEND_WALLET_OCCURRENCE_V1, blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1, blockchain::WF_REJECT_ACTOR_V1 and blockchain::WF_CREATE_WALLET_V1 each supersede their published version
      Source Finding: 'S4 design_decisions #5'
    - Decision: The entrances and intents are re-pointed
      Business Fact: Every caller starts the same act as today
      Resolution: blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REJECT_ACTOR_V0, blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0 and blockchain::IN_WALLET_CREATION_V0 name the next version of the act they start, and nothing else in them changes
      Source Finding: 'S4 design_decisions #6'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: blockchain::CC_RESOLVE_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: Answers which actor a contact address denotes, and reports when none does
      Reason: A step carries on past a failed record its store declares. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: Claims the identity, and refuses when the person already holds a wallet
      Reason: A step carries on past a failed record its store declares. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: blockchain::CC_CREATE_WALLET_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: Records the wallet with a balance of zero, its denomination and its classification
      Reason: A step carries on past a failed record its store declares. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: Records the moment on the wallet's trail
      Reason: A step carries on past a failed record its store declares. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: blockchain::WF_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: The governed sequence that admits a person as an unverified actor, and announces that it did
      Reason: It leaves a failed record unanswered. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: blockchain::WF_ACCEPT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: The governed sequence that records an acceptance and announces it
      Reason: It leaves a failed record unanswered. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: blockchain::WF_REJECT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: The governed sequence that records a rejection, with grounds required, and announces it
      Reason: It leaves a failed record unanswered. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: blockchain::WF_CREATE_WALLET_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: The governed sequence that gives an accepted person a wallet and records that it did
      Reason: It leaves a failed record unanswered. Stood down by its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: capability_side_effects::CS_CLOCK_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::CC_VALIDATE_REGISTRATION_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - FQDN: blockchain::CC_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - FQDN: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - FQDN: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - FQDN: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::RB_IDENTITY_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::RB_WALLET_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::STRUCTURE_WALLET_STORAGE_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::IN_ACTOR_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Starts an act being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
    - FQDN: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Starts an act being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #17'
    - FQDN: blockchain::EV_ACTOR_ACCEPTED_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::IN_ACTOR_REJECTION_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Starts an act being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #18'
    - FQDN: blockchain::EV_ACTOR_REJECTED_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::IN_WALLET_CREATION_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Starts an act being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #19'
    - FQDN: blockchain::EV_WALLET_CREATED_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Named by a replaced artifact's next version, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: blockchain::AC_PARTICIPANT_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: The authority context the four acts run under, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: blockchain::TI_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Starts an act being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - FQDN: blockchain::TI_ACCEPT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Starts an act being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - FQDN: blockchain::TI_REJECT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: ''
      Reason: Starts an act being replaced; re-pointed to its next version.
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
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
    - Capability: Look a person up
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: blockchain::CC_RESOLVE_ACTOR_V1
      Summary: Answers which actor a contact address denotes, and reports when none does
      Owner Subdomain: identity
      Status: NEW
      Source Finding: 'S6 governance_outcome #1'
    - Capability: Claim a wallet's identity
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Summary: Claims the identity, and refuses when the person already holds a wallet
      Owner Subdomain: wallet
      Status: NEW
      Source Finding: 'S6 governance_outcome #2'
    - Capability: Record a wallet
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: blockchain::CC_CREATE_WALLET_RECORD_V1
      Summary: Records the wallet with a balance of zero, its denomination and its classification
      Owner Subdomain: wallet
      Status: NEW
      Source Finding: 'S6 governance_outcome #2'
    - Capability: Record a moment on a wallet's trail
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Summary: Records the moment on the wallet's trail
      Owner Subdomain: wallet
      Status: NEW
      Source Finding: 'S6 governance_outcome #2'
    - Capability: Register a person
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: blockchain::WF_REGISTER_ACTOR_V1
      Summary: The governed sequence that admits a person as an unverified actor, and announces that it did
      Owner Subdomain: identity
      Status: NEW
      Source Finding: 'S6 governance_outcome #3'
    - Capability: Accept a person
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: blockchain::WF_ACCEPT_ACTOR_V1
      Summary: The governed sequence that records an acceptance and announces it
      Owner Subdomain: identity
      Status: NEW
      Source Finding: 'S6 governance_outcome #3'
    - Capability: Reject a person
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: blockchain::WF_REJECT_ACTOR_V1
      Summary: The governed sequence that records a rejection, with grounds required, and announces it
      Owner Subdomain: identity
      Status: NEW
      Source Finding: 'S6 governance_outcome #3'
    - Capability: Create a wallet
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: blockchain::WF_CREATE_WALLET_V1
      Summary: The governed sequence that gives an accepted person a wallet and records that it did
      Owner Subdomain: wallet
      Status: NEW
      Source Finding: 'S6 governance_outcome #3'
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_REGISTER_ACTOR_V1
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_ACCEPT_ACTOR_V1
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_REJECT_ACTOR_V1
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - RB Code: blockchain::RB_WALLET_BINDINGS_V0
      Binds WF: blockchain::WF_CREATE_WALLET_V1
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
  execution_topology:
    columns:
    - Workflow
    - Node
    - Runs
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: blockchain::WF_REGISTER_ACTOR_V1
      Node: blockchain::IN_ACTOR_REGISTERED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_VALIDATE_REGISTRATION_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V1
      Node: blockchain::CC_VALIDATE_REGISTRATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_CLAIM_CONTACT_ADDRESS_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V1
      Node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_REGISTER_ACTOR_V0; ALREADY_EXISTS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V1
      Node: blockchain::CC_REGISTER_ACTOR_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V1
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V1
      Node: EXIT_SUCCESS
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V1
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V1
      Node: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V1
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Runs: blockchain::CC_RESOLVE_ACTOR_V1
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V1
      Node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V1
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V1
      Node: EXIT_SUCCESS
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit blockchain::EV_ACTOR_ACCEPTED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V1
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Workflow: blockchain::WF_REJECT_ACTOR_V1
      Node: blockchain::IN_ACTOR_REJECTION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: blockchain::WF_REJECT_ACTOR_V1
      Node: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RESOLVE_ACTOR_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: blockchain::WF_REJECT_ACTOR_V1
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Runs: blockchain::CC_RESOLVE_ACTOR_V1
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: blockchain::WF_REJECT_ACTOR_V1
      Node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: blockchain::WF_REJECT_ACTOR_V1
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: blockchain::WF_REJECT_ACTOR_V1
      Node: EXIT_SUCCESS
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit blockchain::EV_ACTOR_REJECTED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: blockchain::WF_REJECT_ACTOR_V1
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: blockchain::IN_WALLET_CREATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Runs: blockchain::CC_RESOLVE_ACTOR_V1
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_DETERMINE_WALLET_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_CLAIM_WALLET_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Runs: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_CREATE_WALLET_RECORD_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: blockchain::CC_CREATE_WALLET_RECORD_V0
      Runs: blockchain::CC_CREATE_WALLET_RECORD_V1
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_WALLET_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Runs: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: EXIT_SUCCESS
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit blockchain::EV_WALLET_CREATED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: blockchain::WF_CREATE_WALLET_V1
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
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
    - CC Code: blockchain::CC_RESOLVE_ACTOR_V1
      Step: '1'
      Step Name: resolve_address
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: RESOLVE
      Store: CONTACT_ADDRESS_REGISTRY
      Consumes: key_or_address
      Produces: target_ref
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: blockchain::CC_RESOLVE_ACTOR_V1
      Step: '2'
      Step Name: read_actor
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: ACTORS
      Consumes: key
      Produces: value
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Step: '1'
      Step Name: claim_wallet_identity
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: WALLET_IDENTITIES
      Consumes: key
      Produces: result_status
      Routing: SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=key; out: result_status=result_status'
    - CC Code: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: '1'
      Step Name: read_created_at
      Capability: capability_side_effects::CS_CLOCK_V0
      Kind (CT, CS): CS
      Operation: NOW
      Store: —
      Consumes: ''
      Produces: timestamp
      Routing: SUCCESS -> continue; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: ''
    - CC Code: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: '2'
      Step Name: assemble_wallet
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
    - CC Code: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: '3'
      Step Name: write_wallet
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: WALLETS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=key, value=value; out: result_status=result_status'
    - CC Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Step: '1'
      Step Name: read_occurred_at
      Capability: capability_side_effects::CS_CLOCK_V0
      Kind (CT, CS): CS
      Operation: NOW
      Store: —
      Consumes: ''
      Produces: timestamp
      Routing: SUCCESS -> continue; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: ''
    - CC Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
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
    - CC Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Step: '3'
      Step Name: append_occurrence
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Kind (CT, CS): CS
      Operation: APPEND
      Store: WALLET_OCCURRENCES
      Consumes: stream_id, record
      Produces: result_status
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: stream_id=stream_id, record=record; out: result_status=result_status'
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: blockchain::CC_RESOLVE_ACTOR_V1
      Step: resolve_address
      Direction (INPUT, OUTPUT): INPUT
      Field: key_or_address
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition resolve_address
    - Owner: blockchain::CC_RESOLVE_ACTOR_V1
      Step: resolve_address
      Direction (INPUT, OUTPUT): OUTPUT
      Field: target_ref
      Bound To: capability_result.target_ref
      Source Finding: S7 cc_composition resolve_address
    - Owner: blockchain::CC_RESOLVE_ACTOR_V1
      Step: read_actor
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.contact_address
      Source Finding: S7 cc_composition read_actor
    - Owner: blockchain::CC_RESOLVE_ACTOR_V1
      Step: read_actor
      Direction (INPUT, OUTPUT): OUTPUT
      Field: value
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_actor
    - Owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Step: claim_wallet_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.wallet_id
      Source Finding: S7 cc_composition claim_wallet_identity
    - Owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Step: claim_wallet_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: capability_result.result_status
      Source Finding: S7 cc_composition claim_wallet_identity
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: read_created_at
      Direction (INPUT, OUTPUT): OUTPUT
      Field: timestamp
      Bound To: capability_result.timestamp
      Source Finding: S7 cc_composition read_created_at
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: assemble_wallet
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: inputs.wallet_fields
      Source Finding: S7 cc_composition assemble_wallet
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: assemble_wallet
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_wallet
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: write_wallet
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.wallet_id
      Source Finding: S7 cc_composition write_wallet
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: write_wallet
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_wallet.record
      Source Finding: S7 cc_composition write_wallet
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V1
      Step: write_wallet
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: capability_result.result_status
      Source Finding: S7 cc_composition write_wallet
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Step: read_occurred_at
      Direction (INPUT, OUTPUT): OUTPUT
      Field: timestamp
      Bound To: capability_result.timestamp
      Source Finding: S7 cc_composition read_occurred_at
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Step: assemble_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: inputs.occurrence_fields
      Source Finding: S7 cc_composition assemble_occurrence
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Step: assemble_occurrence
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_occurrence
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Step: append_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: inputs.stream_id
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Step: append_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: results.assemble_occurrence.record
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Step: append_occurrence
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: capability_result.result_status
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_record
      Bound To: payload.actor_record
      Source Finding: S7 execution_topology blockchain::CC_VALIDATE_REGISTRATION_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_record
      Bound To: payload.actor_record
      Source Finding: S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: address_path
      Bound To: payload.address_path
      Source Finding: S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: address_type
      Bound To: payload.address_type
      Source Finding: S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_fields
      Bound To: '{''name'': ''$.payload.actor_record.name'', ''contact_address'': ''$.payload.actor_record.contact_address'', ''state'': ''UNVERIFIED'', ''currency_preference'': ''$.payload.actor_record.currency_preference'', ''language'': ''$.payload.actor_record.language''}'
      Source Finding: S7 execution_topology blockchain::CC_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      Source Finding: S7 execution_topology blockchain::CC_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_RESOLVE_ACTOR_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: current_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decision
      Bound To: ACCEPTED
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: verifying_authority
      Bound To: payload.verifying_authority
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: grounds
      Bound To: payload.grounds
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: grounds
      Bound To: payload.grounds
      Source Finding: S7 execution_topology blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_RESOLVE_ACTOR_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: current_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decision
      Bound To: REJECTED
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: verifying_authority
      Bound To: payload.verifying_authority
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: grounds
      Bound To: payload.grounds
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: holder_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: S7 execution_topology blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: states_admitting_a_wallet
      Bound To: '[''ACCEPTED'']'
      Source Finding: S7 execution_topology blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: holder
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.contact_address
      Source Finding: S7 execution_topology blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: wallet_id_prefix
      Bound To: payload.wallet_id_prefix
      Source Finding: S7 execution_topology blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: wallet_id
      Bound To: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
      Source Finding: S7 execution_topology blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: key_material
      Bound To: payload.key_material
      Source Finding: S7 execution_topology blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_CREATE_WALLET_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: wallet_id
      Bound To: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
      Source Finding: S7 execution_topology blockchain::CC_CREATE_WALLET_RECORD_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_CREATE_WALLET_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: wallet_fields
      Bound To: payload.wallet_fields
      Source Finding: S7 execution_topology blockchain::CC_CREATE_WALLET_RECORD_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
      Source Finding: S7 execution_topology blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    - Owner: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
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
    - Artifact: blockchain::CC_RESOLVE_ACTOR_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The address naming the actor to resolve
    - Artifact: blockchain::CC_RESOLVE_ACTOR_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: value
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor and its current state, or absent when none is held
    - Artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: wallet_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The identity being claimed.
    - Artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the claim succeeded, or the identity was already held.
    - Artifact: blockchain::CC_CREATE_WALLET_RECORD_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: wallet_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The wallet being recorded.
    - Artifact: blockchain::CC_CREATE_WALLET_RECORD_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: wallet_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the business holds about the wallet.
    - Artifact: blockchain::CC_CREATE_WALLET_RECORD_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the wallet was recorded.
    - Artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: stream_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The trail the moment is added to.
    - Artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: occurrence_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the moment records.
    - Artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the moment was recorded.
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: blockchain::WF_REGISTER_ACTOR_V1
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V1
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_ACCEPTED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V1
      Property: supersedes
      Value: blockchain::WF_ACCEPT_ACTOR_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - Artifact: blockchain::WF_REJECT_ACTOR_V1
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_REJECTED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::WF_REJECT_ACTOR_V1
      Property: supersedes
      Value: blockchain::WF_REJECT_ACTOR_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: blockchain::WF_CREATE_WALLET_V1
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_WALLET_CREATED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: blockchain::WF_REGISTER_ACTOR_V1
      Property: supersedes
      Value: blockchain::WF_REGISTER_ACTOR_V0
      Source Finding: 'S4 design_decisions #5'
    - Artifact: blockchain::WF_CREATE_WALLET_V1
      Property: supersedes
      Value: blockchain::WF_CREATE_WALLET_V0
      Source Finding: 'S4 design_decisions #5'
    - Artifact: blockchain::CC_RESOLVE_ACTOR_V1
      Property: supersedes
      Value: blockchain::CC_RESOLVE_ACTOR_V0
      Source Finding: 'S4 design_decisions #5'
    - Artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
      Property: supersedes
      Value: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Source Finding: 'S4 design_decisions #5'
    - Artifact: blockchain::CC_CREATE_WALLET_RECORD_V1
      Property: supersedes
      Value: blockchain::CC_CREATE_WALLET_RECORD_V0
      Source Finding: 'S4 design_decisions #5'
    - Artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
      Property: supersedes
      Value: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Source Finding: 'S4 design_decisions #5'
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: WALLET_IDENTITIES
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: blockchain/wallet/wallet_identity_registry.jsonl
      Used By: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Store Name: WALLETS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_MUTABLE_JSON_V0
      Proposed Path: blockchain/wallet/wallets.json
      Used By: blockchain::CC_CREATE_WALLET_RECORD_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - Store Name: WALLET_OCCURRENCES
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_APPENDONLY_JSONL_V0
      Proposed Path: blockchain/wallet/wallet_occurrences.jsonl
      Used By: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Count: '4'
      Artifacts: blockchain::CC_RESOLVE_ACTOR_V1, blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1, blockchain::WF_REJECT_ACTOR_V1
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: wallet
      Count: '4'
      Artifacts: blockchain::CC_CLAIM_WALLET_IDENTITY_V1, blockchain::CC_CREATE_WALLET_RECORD_V1, blockchain::CC_APPEND_WALLET_OCCURRENCE_V1, blockchain::WF_CREATE_WALLET_V1
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Subdomain: identity
      Count: '4'
      Artifacts: blockchain::CC_RESOLVE_ACTOR_V0, blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Subdomain: wallet
      Count: '4'
      Artifacts: blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_CREATE_WALLET_RECORD_V0, blockchain::CC_APPEND_WALLET_OCCURRENCE_V0, blockchain::WF_CREATE_WALLET_V0
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: blockchain::WF_CREATE_WALLET_V1
      Consults: blockchain::RB_IDENTITY_BINDINGS_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
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
    rows: []
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
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
      Refused When: A record the registration needs fails
      Act: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Registering a person
      Refused When: A record the registration needs fails
      Act: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Registering a person
      Refused When: A record the registration needs fails
      Act: blockchain::WF_REGISTER_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Accepting a person
      Refused When: A record the acceptance needs fails
      Act: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Accepting a person
      Refused When: A record the acceptance needs fails
      Act: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Accepting a person
      Refused When: A record the acceptance needs fails
      Act: blockchain::WF_ACCEPT_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Rejecting a person
      Refused When: A record the rejection needs fails
      Act: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #3'
    - Operation: Rejecting a person
      Refused When: A record the rejection needs fails
      Act: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #3'
    - Operation: Rejecting a person
      Refused When: A record the rejection needs fails
      Act: blockchain::WF_REJECT_ACTOR_V1
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #3'
    - Operation: Creating a wallet
      Refused When: A record the wallet needs fails
      Act: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #4'
    - Operation: Creating a wallet
      Refused When: A record the wallet needs fails
      Act: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #4'
    - Operation: Creating a wallet
      Refused When: A record the wallet needs fails
      Act: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_CREATE_WALLET_RECORD_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #4'
    - Operation: Creating a wallet
      Refused When: A record the wallet needs fails
      Act: blockchain::WF_CREATE_WALLET_V1
      Step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Outcome: BACKEND_ERROR
      Source Finding: 'S0 operation_refusals #4'
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
    rows: []
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
