# Stage 7 — Design Intent: blockchain / wallet

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_04_wallet
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
    - Decision: Wallet is a subdomain of its own
      Business Fact: A wallet is a thing the business holds in its own right
      Resolution: '`wallet` subdomain, owning three stores and writing no store identity owns'
      Source Finding: 'S4 design_decisions #1'
    - Decision: Working out an address is pure computation
      Business Fact: The same key material always yields the same address
      Resolution: '`blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0`, a transform; the closed side-effect set is unchanged'
      Source Finding: 'S4 design_decisions #2'
    - Decision: Key material is supplied, never generated
      Business Fact: The same request must produce the same wallet
      Resolution: The transform takes the material as a declared input and derives nothing at random
      Source Finding: 'S4 design_decisions #3'
    - Decision: A wallet's identity is derived from its holder
      Business Fact: One person holds one wallet
      Resolution: '`CT_PURE_GENERATE_ID_V0` over the holder''s identity alone'
      Source Finding: 'S4 design_decisions #4'
    - Decision: The declared moments are announced from where the operations record what they did
      Business Fact: The moments already exist and are referred to by nothing
      Resolution: '`emit:` on the terminal node of each identity workflow'
      Source Finding: 'S4 design_decisions #5'
    - Decision: Wallet creation is refused for a person not held, not accepted, or already holding a wallet
      Business Fact: The business stated each refusal
      Resolution: Declared outcomes routing to a terminal node, never an unhandled path
      Source Finding: 'S4 design_decisions #6'
    - Decision: Acceptance stands on its own
      Business Fact: A wallet that cannot be created does not un-accept the person
      Resolution: Wallet creation is a separate workflow; identity's workflows terminate without it
      Source Finding: 'S4 design_decisions #7'
    - Decision: The deciding workflow is split rather than amended
      Business Fact: A rejection must state grounds, and each outcome must announce
      Resolution: Two workflows replace one, each with its own admission and its own terminal node to announce from
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REPLACE
      Summary: ''
      Reason: Superseded by two workflows, one per outcome, each announcing its own moment and the rejection requiring grounds throughout.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: blockchain::IN_ACTOR_VERIFIED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REPLACE
      Summary: ''
      Reason: Superseded by an acceptance intent and a rejection intent. One intent dispatches one workflow, so a decision split in two leaves this one nothing to dispatch.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: blockchain::TI_ACCEPT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the decision, admitted states and outcomes, and the acceptance occurrence label
      Reason: Its handler routes to the workflow this change stands down, and must reach the acceptance path instead.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: blockchain::TI_REJECT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the decision, admitted states and outcomes, and the rejection occurrence label
      Reason: Its handler routes to the workflow this change stands down, and must reach the rejection path and supply the grounds it checks.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: blockchain::WF_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that admits a person as an unverified actor, and announces that it did
      Reason: Its terminal node announces nothing. Everything else about it is unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Refuses every declared refusal and moves the actor to its decided state
      Reason: Its self-verification step computed whether the decider is the subject and routed on whether the *transform ran*, so a person could decide about themselves. The step must refuse on what it found, not on the fact that it looked.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: blockchain::CC_RESOLVE_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Resolves a person and carries their state; wallet reads it and identity's workflows keep it.
      Source Finding: 'S5 cross_subdomain_refs #1'
    - FQDN: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Records a moment on a person's trail, unchanged.
      Source Finding: 'S3 dependency_discoveries #8'
    - FQDN: blockchain::IN_ACTOR_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Admits a registration, unchanged; the registration workflow is redeclared whole and runs it.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: blockchain::CC_VALIDATE_REGISTRATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Validates a registration, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Claims a contact address, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: blockchain::CC_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Records the person, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: blockchain::EV_ACTOR_ACCEPTED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Declared already; this change refers to it for the first time.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The same.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: blockchain::EV_ACTOR_REJECTED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The same.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: blockchain::AC_PARTICIPANT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The authority context both identity workflows already run under.
      Source Finding: 'S6 ownership #10'
    - FQDN: blockchain::RB_IDENTITY_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The bindings identity's workflows resolve their capabilities and stores through
      Reason: Two new workflows must bind through it.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Declares what the blockchain domain compiles
      Reason: It knows of one subdomain and must know of two.
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Holds a wallet.
      Source Finding: 'S6 ownership #6'
    - FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Holds a wallet's trail.
      Source Finding: 'S6 ownership #7'
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Claims a wallet's identity.
      Source Finding: 'S6 ownership #9'
    - FQDN: capability_side_effects::CS_CLOCK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Supplies the time a moment occurred.
      Source Finding: 'S6 ownership #11'
    - FQDN: capability_transforms::CT_PURE_GENERATE_ID_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Derives a wallet's identity from its holder.
      Source Finding: 'S6 ownership #8'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Refuses a value outside the set the business admits — the state a decision may be made from, and the outcomes it may carry.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Assembles a record from declared fields.
      Source Finding: 'S7 cc_composition #5'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Judges a parameter against declared rules.
      Source Finding: 'S7 cc_composition #10'
    - FQDN: blockchain::IN_WALLET_CREATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request naming the person a wallet is for, and refuses one that names nobody
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #1'
    - FQDN: blockchain::WF_CREATE_WALLET_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that gives an accepted person a wallet and records that it did
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #2'
    - FQDN: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Derives the wallet's identity from the person who holds it
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #3'
    - FQDN: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Claims the identity, and refuses when the person already holds a wallet
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #4'
    - FQDN: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Establishes the address from key material supplied with the request
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #5'
    - FQDN: blockchain::CC_CREATE_WALLET_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Records the wallet with a balance of zero, its denomination and its classification
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #6'
    - FQDN: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Records the moment on the wallet's trail
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #7'
    - FQDN: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Derives an address from supplied key material; the same material always yields the same address
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #8'
    - FQDN: blockchain::EV_WALLET_CREATED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Announces that a wallet was created, for whom, and when
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #9'
    - FQDN: blockchain::RB_WALLET_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Binds the wallet workflow to the capabilities and stores it uses
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #10'
    - FQDN: blockchain::STRUCTURE_WALLET_STORAGE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Declares the three stores wallet owns
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #11'
    - FQDN: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The fixed set of wallet classifications, of which only the default is used
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #12'
    - FQDN: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request to accept a person, and refuses one that names nobody
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #13'
    - FQDN: blockchain::IN_ACTOR_REJECTION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Admits a request to reject a person, and refuses one that states no grounds
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #14'
    - FQDN: blockchain::WF_ACCEPT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that records an acceptance and announces it
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #15'
    - FQDN: blockchain::WF_REJECT_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that records a rejection, with grounds required, and announces it
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #16'
    - FQDN: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Refuses a rejection stating no grounds, before anything is recorded
      Reason: Authored by an earlier pass of this change and already in the business's hands; redeclared whole so the design and the artifact agree.
      Source Finding: 'S5 provisional_codes #17'
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
    - Capability: Refusing a wallet to a person the business has not accepted
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): CC
      Code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Summary: Refuses a wallet for a person the business has not accepted, before anything is claimed or recorded
      Owner Subdomain: wallet
      Status: NEW
      Source Finding: 'S5 provisional_codes #3'
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: blockchain::RB_WALLET_BINDINGS_V0
      Binds WF: blockchain::WF_CREATE_WALLET_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
      Source Finding: 'S5 provisional_codes #10'
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_ACCEPT_ACTOR_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_REJECT_ACTOR_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_REGISTER_ACTOR_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0
      Storage Structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
  execution_topology:
    columns:
    - Workflow
    - Node
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: blockchain::IN_WALLET_CREATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S5 actions #1'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 cross_subdomain_deps #1'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_DETERMINE_WALLET_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S1 operation_refusals #2'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_CLAIM_WALLET_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S5 provisional_codes #3'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S5 provisional_codes #4'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_CREATE_WALLET_RECORD_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S5 provisional_codes #5'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: blockchain::CC_CREATE_WALLET_RECORD_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_WALLET_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S5 provisional_codes #6'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S5 provisional_codes #7'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: EXIT_SUCCESS
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: emit blockchain::EV_WALLET_CREATED_V0
      Source Finding: 'S5 provisional_codes #9'
    - Workflow: blockchain::WF_CREATE_WALLET_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S5 invariants #4'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S5 provisional_codes #13'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S3 dependency_discoveries #8'
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: EXIT_SUCCESS
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: emit blockchain::EV_ACTOR_ACCEPTED_V0
      Source Finding: S4 gap_register GAP-4
    - Workflow: blockchain::WF_ACCEPT_ACTOR_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S5 invariants #4'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::IN_ACTOR_REJECTION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S5 provisional_codes #14'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RESOLVE_ACTOR_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S4 gap_register GAP-5
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::CC_RESOLVE_ACTOR_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S3 dependency_discoveries #8'
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: EXIT_SUCCESS
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: emit blockchain::EV_ACTOR_REJECTED_V0
      Source Finding: S4 gap_register GAP-4
    - Workflow: blockchain::WF_REJECT_ACTOR_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S5 invariants #4'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::IN_ACTOR_REGISTERED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> blockchain::CC_VALIDATE_REGISTRATION_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_VALIDATE_REGISTRATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_CLAIM_CONTACT_ADDRESS_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_REGISTER_ACTOR_V0; ALREADY_EXISTS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_REGISTER_ACTOR_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: EXIT_SUCCESS
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: emit blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Source Finding: S4 gap_register GAP-4
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
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
    - CC Code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Step: '1'
      Step Name: require_holder_accepted
      Capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_SET_MEMBERSHIP
      Store: —
      Consumes: value, allowed_set
      Produces: is_member
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: value=holder_state, allowed_set=states_admitting_a_wallet; out: is_member=is_accepted'
    - CC Code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Step: '1'
      Step Name: derive_wallet_identity
      Capability: capability_transforms::CT_PURE_GENERATE_ID_V0
      Kind (CT, CS): CT
      Operation: GENERATE_ID
      Store: —
      Consumes: data, prefix
      Produces: id
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: data=data, prefix=prefix; out: id=id'
    - CC Code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Step: '1'
      Step Name: claim_wallet_identity
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: WALLET_IDENTITIES
      Consumes: key
      Produces: result_status
      Routing: SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=key; out: result_status=result_status'
    - CC Code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Step: '1'
      Step Name: derive_wallet_address
      Capability: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
      Kind (CT, CS): CT
      Operation: DERIVE_WALLET_ADDRESS
      Store: —
      Consumes: key_material
      Produces: address
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key_material=key_material; out: address=address'
    - CC Code: blockchain::CC_CREATE_WALLET_RECORD_V0
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
    - CC Code: blockchain::CC_CREATE_WALLET_RECORD_V0
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
    - CC Code: blockchain::CC_CREATE_WALLET_RECORD_V0
      Step: '3'
      Step Name: write_wallet
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: WALLETS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=key, value=value; out: result_status=result_status'
    - CC Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
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
    - CC Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
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
    - CC Code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Step: '3'
      Step Name: append_occurrence
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Kind (CT, CS): CS
      Operation: APPEND
      Store: WALLET_OCCURRENCES
      Consumes: stream_id, record
      Produces: result_status
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: stream_id=stream_id, record=record; out: result_status=result_status'
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
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=valid'
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
      Operation: UPDATE
      Store: ACTORS
      Consumes: key, updates
      Produces: result_status
      Routing: SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: ''
    - CC Code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Step: '1'
      Step Name: require_grounds_stated
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=valid'
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Step: derive_wallet_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: data
      Bound To: inputs.holder
      Source Finding: S7 cc_composition derive_wallet_identity
    - Owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Step: derive_wallet_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: prefix
      Bound To: inputs.wallet_id_prefix
      Source Finding: S7 cc_composition derive_wallet_identity
    - Owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Step: derive_wallet_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: id
      Bound To: capability_result.id
      Source Finding: S7 cc_composition derive_wallet_identity
    - Owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Step: claim_wallet_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.wallet_id
      Source Finding: S7 cc_composition claim_wallet_identity
    - Owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Step: claim_wallet_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: capability_result.result_status
      Source Finding: S7 cc_composition claim_wallet_identity
    - Owner: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Step: derive_wallet_address
      Direction (INPUT, OUTPUT): INPUT
      Field: key_material
      Bound To: inputs.key_material
      Source Finding: S7 cc_composition derive_wallet_address
    - Owner: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Step: derive_wallet_address
      Direction (INPUT, OUTPUT): OUTPUT
      Field: address
      Bound To: capability_result.address
      Source Finding: S7 cc_composition derive_wallet_address
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V0
      Step: read_created_at
      Direction (INPUT, OUTPUT): OUTPUT
      Field: timestamp
      Bound To: capability_result.timestamp
      Source Finding: S7 cc_composition read_created_at
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V0
      Step: assemble_wallet
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: inputs.wallet_fields
      Source Finding: S7 cc_composition assemble_wallet
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V0
      Step: assemble_wallet
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_wallet
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V0
      Step: write_wallet
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.wallet_id
      Source Finding: S7 cc_composition write_wallet
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V0
      Step: write_wallet
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_wallet.record
      Source Finding: S7 cc_composition write_wallet
    - Owner: blockchain::CC_CREATE_WALLET_RECORD_V0
      Step: write_wallet
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: capability_result.result_status
      Source Finding: S7 cc_composition write_wallet
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Step: read_occurred_at
      Direction (INPUT, OUTPUT): OUTPUT
      Field: timestamp
      Bound To: capability_result.timestamp
      Source Finding: S7 cc_composition read_occurred_at
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Step: assemble_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: inputs.occurrence_fields
      Source Finding: S7 cc_composition assemble_occurrence
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Step: assemble_occurrence
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_occurrence
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Step: append_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: inputs.stream_id
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Step: append_occurrence
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: results.assemble_occurrence.record
      Source Finding: S7 cc_composition append_occurrence
    - Owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Step: append_occurrence
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: capability_result.result_status
      Source Finding: S7 cc_composition append_occurrence
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
      Field: parameters
      Bound To: inputs.self_check_parameters
      Source Finding: S7 cc_composition refuse_self_verification
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: refuse_self_verification
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: inputs.self_check_rules
      Source Finding: S7 cc_composition refuse_self_verification
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: refuse_self_verification
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
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
      Field: updates
      Bound To: results.assemble_decided_actor.record
      Source Finding: S7 cc_composition write_decided_actor
    - Owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Step: write_decided_actor
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_decided_actor
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: self_check_parameters
      Bound To: payload.self_check_parameters
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: self_check_rules
      Bound To: payload.self_check_rules
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: self_check_parameters
      Bound To: payload.self_check_parameters
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: self_check_rules
      Bound To: payload.self_check_rules
      Source Finding: S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - Owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Step: require_grounds_stated
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: inputs.grounds_parameters
      Source Finding: S7 cc_composition require_grounds_stated
    - Owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Step: require_grounds_stated
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: inputs.grounds_rules
      Source Finding: S7 cc_composition require_grounds_stated
    - Owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Step: require_grounds_stated
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_grounds_stated
    - Owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Step: require_holder_accepted
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: inputs.holder_state
      Source Finding: S7 cc_composition require_holder_accepted
    - Owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Step: require_holder_accepted
      Direction (INPUT, OUTPUT): INPUT
      Field: allowed_set
      Bound To: inputs.states_admitting_a_wallet
      Source Finding: S7 cc_composition require_holder_accepted
    - Owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Step: require_holder_accepted
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_accepted
      Bound To: capability_result.is_member
      Source Finding: S7 cc_composition require_holder_accepted
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: holder_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: S7 execution_topology blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: states_admitting_a_wallet
      Bound To: '[''ACCEPTED'']'
      Source Finding: S7 execution_topology blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: holder
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.contact_address
      Source Finding: S7 execution_topology blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: wallet_id_prefix
      Bound To: payload.wallet_id_prefix
      Source Finding: S7 execution_topology blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: wallet_id
      Bound To: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
      Source Finding: S7 execution_topology blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: key_material
      Bound To: payload.key_material
      Source Finding: S7 execution_topology blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_CREATE_WALLET_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: wallet_id
      Bound To: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
      Source Finding: S7 execution_topology blockchain::CC_CREATE_WALLET_RECORD_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_CREATE_WALLET_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: wallet_fields
      Bound To: payload.wallet_fields
      Source Finding: S7 execution_topology blockchain::CC_CREATE_WALLET_RECORD_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
      Source Finding: S7 execution_topology blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 execution_topology blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: grounds_parameters
      Bound To: payload.grounds_parameters
      Source Finding: S7 execution_topology blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: grounds_rules
      Bound To: payload.grounds_rules
      Source Finding: S7 execution_topology blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    - Owner: blockchain::WF_CREATE_WALLET_V0
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: 'S3 dependency_discoveries #8'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: current_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: states_admitting_a_decision
      Bound To: payload.states_admitting_a_decision
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decision
      Bound To: payload.decision
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: admitted_outcomes
      Bound To: payload.admitted_outcomes
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: verifying_authority
      Bound To: payload.verifying_authority
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decided_actor_fields
      Bound To: payload.decided_actor_fields
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_ACCEPT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RESOLVE_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: current_state
      Bound To: results.CC_RESOLVE_ACTOR_V0.value.state
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: states_admitting_a_decision
      Bound To: payload.states_admitting_a_decision
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decision
      Bound To: payload.decision
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: admitted_outcomes
      Bound To: payload.admitted_outcomes
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: verifying_authority
      Bound To: payload.verifying_authority
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: decided_actor_fields
      Bound To: payload.decided_actor_fields
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REJECT_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: payload.contact_address
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_record
      Bound To: payload.actor_record
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_VALIDATE_REGISTRATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: registration_schema
      Bound To: payload.registration_schema
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_record
      Bound To: payload.actor_record
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: address_path
      Bound To: payload.address_path
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: address_type
      Bound To: payload.address_type
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_fields
      Bound To: payload.actor_record
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_REGISTER_ACTOR_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: occurrence_fields
      Bound To: payload.occurrence_fields
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: payload.stream_id
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
    - Owner: blockchain::WF_REGISTER_ACTOR_V0
      Step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: contact_address
      Bound To: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      Source Finding: S7 existing_inventory WF_REGISTER_ACTOR_V0
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
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: current_state
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The state the actor is in when the decision is made.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: states_admitting_a_decision
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The states from which a decision may be made.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: decision
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The outcome being recorded.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: admitted_outcomes
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The outcomes the business admits.
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
      Field: decided_actor_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The actor record as it will stand once decided.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: self_check_parameters
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The decider and the subject, as the parameter map the rule evaluator reads.
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: self_check_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: 'The rule the decider must satisfy: not the person being decided about.'
    - Artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the decision was recorded.
    - Artifact: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: key_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The public key material supplied with the request. Never generated here.
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
    - Artifact: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The address others may pay to. The same material always yields the same address.
    - Artifact: blockchain::IN_WALLET_CREATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person the wallet is for.
    - Artifact: blockchain::IN_WALLET_CREATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: key_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key material the address is worked out from.
    - Artifact: blockchain::IN_WALLET_CREATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: wallet_id_prefix
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The prefix a wallet identity carries, so the identity is recognisable as a wallet.
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
    - Artifact: blockchain::IN_ACTOR_REJECTION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: contact_address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person being rejected.
    - Artifact: blockchain::IN_ACTOR_REJECTION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: verifying_authority
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The authority recording the rejection.
    - Artifact: blockchain::IN_ACTOR_REJECTION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Why the person is refused. A rejection stating none is refused.
    - Artifact: blockchain::EV_WALLET_CREATED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: wallet_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The wallet created.
    - Artifact: blockchain::EV_WALLET_CREATED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: holder
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person it belongs to.
    - Artifact: blockchain::EV_WALLET_CREATED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: occurred_at
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: When it was created.
    - Artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: holder
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The person the wallet belongs to.
    - Artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: wallet_id_prefix
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The prefix a wallet identity carries.
    - Artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The identity derived for the wallet.
    - Artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: wallet_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The identity being claimed.
    - Artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the claim succeeded, or the identity was already held.
    - Artifact: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: key_material
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key material supplied with the request.
    - Artifact: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The address others may pay to.
    - Artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: wallet_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The wallet being recorded.
    - Artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: wallet_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the business holds about the wallet.
    - Artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the wallet was recorded.
    - Artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: stream_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The trail the moment is added to.
    - Artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: occurrence_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What the moment records.
    - Artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: result_status
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the moment was recorded.
    - Artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: holder_state
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The state the person is in, read from the record identity holds.
    - Artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: states_admitting_a_wallet
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The states a wallet may be created from. Acceptance, and nothing else — fixed by the design, never taken from the caller, because a rule the caller supplies is a rule the caller can widen.
    - Artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: is_accepted
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the person is one the business has accepted.
    - Artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds_parameters
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The grounds, as the parameter map the rule evaluator reads.
    - Artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: grounds_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: 'The rules the grounds must satisfy: stated at all, and not empty.'
    - Artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: valid
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether grounds were stated.
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
    - CT Code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
      Module: blockchain.implementation.capability_transforms.atoms.ct_pure_derive_wallet_address_v0
      Callable: execute
      Operation: DERIVE_WALLET_ADDRESS
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): never
      Source Finding: 'S4 design_decisions #3'
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Extends: NONE
      Value: DEFAULT
      Meaning: The only classification this change creates.
      Source Finding: 'S5 known_facts #15'
    - Vocabulary Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Extends: NONE
      Value: PRIVATE
      Meaning: Named and unused until a business need arises.
      Source Finding: 'S5 known_facts #15'
    - Vocabulary Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Extends: NONE
      Value: BUSINESS
      Meaning: Named and unused.
      Source Finding: 'S5 known_facts #15'
    - Vocabulary Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Extends: NONE
      Value: SAVINGS
      Meaning: Named and unused.
      Source Finding: 'S5 known_facts #15'
    - Vocabulary Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Extends: NONE
      Value: INVESTMENT
      Meaning: Named and unused.
      Source Finding: 'S5 known_facts #15'
    - Vocabulary Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Extends: NONE
      Value: MINT
      Meaning: Named and unused.
      Source Finding: 'S5 known_facts #15'
    - Vocabulary Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Extends: NONE
      Value: BURN
      Meaning: Named and unused.
      Source Finding: 'S5 known_facts #15'
    - Vocabulary Code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
      Extends: NONE
      Value: POOL
      Meaning: Named and unused.
      Source Finding: 'S5 known_facts #15'
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows:
    - RB Code: blockchain::RB_WALLET_BINDINGS_V0
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Key: store
      Value: WALLETS
      Source Finding: 'S7 structure_stores #1'
    - RB Code: blockchain::RB_WALLET_BINDINGS_V0
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Key: store
      Value: WALLET_OCCURRENCES
      Source Finding: 'S7 structure_stores #2'
    - RB Code: blockchain::RB_WALLET_BINDINGS_V0
      Capability: capability_side_effects::CS_REGISTRY_V0
      Key: store
      Value: WALLET_IDENTITIES
      Source Finding: 'S7 structure_stores #3'
    - RB Code: blockchain::RB_WALLET_BINDINGS_V0
      Capability: capability_side_effects::CS_CLOCK_V0
      Key: policy
      Value: utc
      Source Finding: 'S7 rb_declarations #1'
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Key: structure
      Value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: S7 existing_inventory RB_IDENTITY_BINDINGS_V0
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Capability: capability_side_effects::CS_REGISTRY_V0
      Key: structure
      Value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: S7 existing_inventory RB_IDENTITY_BINDINGS_V0
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Key: structure
      Value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
      Source Finding: S7 existing_inventory RB_IDENTITY_BINDINGS_V0
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Capability: capability_side_effects::CS_CLOCK_V0
      Key: precision
      Value: seconds
      Source Finding: S7 existing_inventory RB_IDENTITY_BINDINGS_V0
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: blockchain::WF_CREATE_WALLET_V0
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_WALLET_CREATED_V0
      Source Finding: 'S7 execution_topology #8'
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_ACCEPTED_V0
      Source Finding: S4 gap_register GAP-4
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_REJECTED_V0
      Source Finding: S4 gap_register GAP-4
    - Artifact: blockchain::WF_REGISTER_ACTOR_V0
      Property: emit.EXIT_SUCCESS
      Value: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
      Source Finding: S4 gap_register GAP-4
    - Artifact: blockchain::WF_ACCEPT_ACTOR_V0
      Property: supersedes
      Value: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::WF_REJECT_ACTOR_V0
      Property: supersedes
      Value: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
      Property: supersedes
      Value: blockchain::IN_ACTOR_VERIFIED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::IN_ACTOR_REJECTION_V0
      Property: supersedes
      Value: blockchain::IN_ACTOR_VERIFIED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
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
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: decision
      Bound To: ACCEPTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: states_admitting_a_decision
      Bound To: '[UNVERIFIED]'
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: admitted_outcomes
      Bound To: '[ACCEPTED, REJECTED]'
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: decided_actor_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: decided_actor_fields.state
      Bound To: ACCEPTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: decided_actor_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: decided_actor_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: self_check_parameters.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: self_check_parameters.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: self_check_rules
      Bound To: '[{field: verifying_authority, op: neq, value: ''${input.contact_address}''}]'
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: stream_id
      Bound To: ACTOR_OCCURRENCES
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: occurrence_fields.occurrence
      Bound To: ACTOR_ACCEPTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: occurrence_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: occurrence_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.accept_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_ACCEPT_ACTOR_V0
      Field: occurrence_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: decision
      Bound To: REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: states_admitting_a_decision
      Bound To: '[UNVERIFIED]'
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: admitted_outcomes
      Bound To: '[ACCEPTED, REJECTED]'
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: decided_actor_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: decided_actor_fields.state
      Bound To: REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: decided_actor_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: decided_actor_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: self_check_parameters.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: self_check_parameters.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: self_check_rules
      Bound To: '[{field: verifying_authority, op: neq, value: ''${input.contact_address}''}]'
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: stream_id
      Bound To: ACTOR_OCCURRENCES
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: occurrence_fields.occurrence
      Bound To: ACTOR_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: occurrence_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: occurrence_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: occurrence_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: grounds_parameters.grounds
      Bound To: ${input.grounds}
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction (INGRESS, EGRESS): INGRESS
      Operation: blockchain.reject_actor
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): WF_INVOCATION
      Handler Target: blockchain::WF_REJECT_ACTOR_V0
      Field: grounds_rules
      Bound To: '[{field: grounds, op: not_null}, {field: grounds, op: neq, value: ''''}]'
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: WALLETS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_MUTABLE_JSON_V0
      Proposed Path: blockchain/wallet/wallets.json
      Used By: blockchain::CC_CREATE_WALLET_RECORD_V0
      Source Finding: 'S5 business_objects #1'
    - Store Name: WALLET_OCCURRENCES
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_APPENDONLY_JSONL_V0
      Proposed Path: blockchain/wallet/wallet_occurrences.jsonl
      Used By: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      Source Finding: 'S5 business_objects #2'
    - Store Name: WALLET_IDENTITIES
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: blockchain/wallet/wallet_identity_registry.jsonl
      Used By: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      Source Finding: 'S5 business_objects #3'
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: wallet
      Count: '1'
      Artifacts: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: wallet
      Count: '13'
      Artifacts: blockchain::IN_WALLET_CREATION_V0, blockchain::WF_CREATE_WALLET_V0, blockchain::CC_DETERMINE_WALLET_IDENTITY_V0, blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0, blockchain::CC_CREATE_WALLET_RECORD_V0, blockchain::CC_APPEND_WALLET_OCCURRENCE_V0, blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0, blockchain::EV_WALLET_CREATED_V0, blockchain::RB_WALLET_BINDINGS_V0, blockchain::STRUCTURE_WALLET_STORAGE_V0, blockchain::VOCAB_WALLET_CLASSIFICATION_V0, blockchain::AC_PARTICIPANT_V0
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: identity
      Count: '9'
      Artifacts: blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0, blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0, blockchain::WF_REGISTER_ACTOR_V0, blockchain::RB_IDENTITY_BINDINGS_V0, blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0, blockchain::TI_ACCEPT_ACTOR_V0
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
      Generator: transformation.build.render:build_manifest
      Generator Sources: S8 build_order, S8 field_declarations, transformation/design/families.py
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: blockchain::WF_CREATE_WALLET_V0
      Consults: blockchain::RB_IDENTITY_BINDINGS_V0
      Source Finding: S4 gap_register GAP-9
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
