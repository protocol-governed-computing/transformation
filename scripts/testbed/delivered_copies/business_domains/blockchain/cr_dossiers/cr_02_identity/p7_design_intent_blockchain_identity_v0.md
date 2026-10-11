# Stage 7 — Design Intent: blockchain / identity

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_02_identity
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
    - Decision: The decision act is offered as two named acts, one for acceptance and one for rejection.
      Business Fact: The business holds a rejection to be its own occurrence, distinct in kind from an acceptance, and refuses to record one decision distinguished by a field.
      Resolution: Each act records a fixed occurrence — accepted or rejected — and a boundary declaration substitutes whole values and passes constants; it derives nothing. One act carrying the decision as a field would require the occurrence to be computed from it, which no declaration can do. Two acts each hold a constant, and the split follows what the business already records.
      Source Finding: S5 provisional_codes blockchain::TI_ACCEPT_ACTOR_V0
    - Decision: A workflow input may be the caller's own data or a constant, never a derivation of the caller's data.
      Business Fact: The business asks that a caller send only their own details, and that what judges them is held by the business.
      Resolution: The deciding act takes an occurrence name derived from the decision. Nothing in the act computes it, so whoever assembles the payload does — a person, silently, when the caller was inside the business. Reached from outside there is no such person. Where the derived value has one possible value per act it is held as a constant here; where it does not, the derivation belongs inside the act, which is the change GAP-11 records.
      Source Finding: S3 analysis_findings Q3
    - Decision: The two preferences are not offered to a caller and are recorded at their declared defaults.
      Business Fact: The business records a preferred currency and a preferred language for every actor, each having a default, so that nothing downstream must decide what an absent preference means.
      Resolution: The boundary applies no default — an optional field a caller omits is omitted from what the act receives, and the act supplies nothing in its place. Rather than admit an actor carrying no preference, the declarations hold both defaults as constants. A caller states no preference because the page does not ask; every actor still carries an answer.
      Source Finding: 'S1 known_facts #28'
    - Decision: Grounds are optional on an acceptance and required on a rejection.
      Business Fact: The business requires grounds for a rejection, where they are the substance of the decision, and permits their omission on an acceptance, where the decision is the statement.
      Resolution: 'Each act declares its own requirement, which is possible only because they are two declarations. Verified against the pinned snapshot: an acceptance carrying no grounds is admitted and records grounds as absent rather than failing.'
      Source Finding: 'S1 known_facts #19'
    - Decision: What a caller sends is named in the business's own terms, not the prior implementation's.
      Business Fact: The business names an actor by their name and their contact address, and a decision by its authority and its grounds.
      Resolution: 'The pages are lifted from the prior implementation and their fields are replaced: what it called a first name, a last name and an email registration is one name and one contact address; what it called a verifier and notes is the verifying authority and the grounds. The form and the way it gathers what is typed survive; none of its names does.'
      Source Finding: 'S4 design_decisions #7'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: blockchain::WF_REGISTER_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The governed sequence that admits a person as an unverified actor.
      Reason: Reached unchanged by a new boundary declaration. Nothing about the act is amended, and it is impacted by nothing in the composition.
      Source Finding: S6 ownership Admit a person's registration
    - FQDN: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The governed sequence that records an authority's decision against a registered actor.
      Reason: Reached unchanged by two new boundary declarations, one for each outcome the business records.
      Source Finding: S6 ownership Record an authority's decision
    - FQDN: blockchain::CC_VALIDATE_REGISTRATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Confirms a registration carries a name and an address of the form asked for.
      Reason: Untouched, but the declaration it validates against is now supplied by a sealed boundary artifact rather than by whoever calls. Same contract, different provenance for its input.
      Source Finding: S6 pps_artifacts_requiring_action blockchain::CC_VALIDATE_REGISTRATION_V0
    - FQDN: blockchain::AC_PARTICIPANT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Declares the kind of party that performs identity's acts.
      Reason: Reused unchanged. A caller from outside is not established to be this or any actor.
      Source Finding: S6 pps_artifacts_requiring_action blockchain::AC_PARTICIPANT_V0
    - FQDN: blockchain::RB_IDENTITY_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Binds identity's workflows to the stores they use.
      Reason: Reused unchanged; the acts reached bind exactly as they did.
      Source Finding: S6 ownership Admit a person's registration
    - FQDN: blockchain::IN_ACTOR_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The request that starts the act of admitting a person.
      Reason: Reached unchanged; what a caller sends becomes this act's payload.
      Source Finding: S6 ownership Admit a person's registration
    - FQDN: blockchain::IN_ACTOR_VERIFIED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The request that starts the act of recording a decision.
      Reason: Reached unchanged by both decision declarations.
      Source Finding: S6 ownership Record an authority's decision
    - FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Reads a supplied record for fields the declaration requires and for the form they must take.
      Reason: Reused unchanged, reached through the act. Impacted by 31 artifacts.
      Source Finding: S6 cross_subdomain_deps Reading a record for absence and for form
    - FQDN: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Governs the kind that admits a request from outside.
      Reason: Governs the three new ingress declarations; not amended.
      Source Finding: S6 cross_subdomain_deps The governed kind that admits a request from outside
    - FQDN: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Governs the kind that states what a caller is told, over a closed set of answer kinds.
      Reason: Governs the three new egress declarations; not amended, and its closed set is not extended.
      Source Finding: S6 cross_subdomain_deps The governed kind that states what a caller is told
    - FQDN: workload::TI_COLLATZ_COMPUTE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The worked precedent for a public name, a declared caller input and a template holding what a caller does not send.
      Reason: Read, not changed.
      Source Finding: S6 cross_subdomain_deps The worked precedent for naming an act and holding what a caller does not send
    - FQDN: workload::TE_COLLATZ_COMPUTE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The worked precedent for classifying an ending and exposing evidence by reference.
      Reason: Read, not changed.
      Source Finding: S6 cross_subdomain_deps The worked precedent for classifying an ending and exposing evidence by reference
  new_artifacts:
    columns:
    - Capability
    - Family
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: Offer registering an actor to a caller outside the business
      Family: TI
      Code: blockchain::TI_REGISTER_ACTOR_V0
      Summary: Admits a request to register an actor, declaring the name and contact address a caller sends and holding the schema, address path, stream, preferences and occurrence label the act requires.
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes blockchain::TI_REGISTER_ACTOR_V0
    - Capability: Tell a caller how their registration ended
      Family: TE
      Code: blockchain::TE_REGISTER_ACTOR_V0
      Summary: Classifies the endings of registering an actor and projects the contact address, the occurrence, its time and its position.
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes blockchain::TE_REGISTER_ACTOR_V0
    - Capability: Offer recording a verification decision to a caller outside the business
      Family: TI
      Code: blockchain::TI_ACCEPT_ACTOR_V0
      Summary: Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the decision, admitted states and outcomes, and the acceptance occurrence label.
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes blockchain::TI_ACCEPT_ACTOR_V0
    - Capability: Tell a caller how their decision ended
      Family: TE
      Code: blockchain::TE_ACCEPT_ACTOR_V0
      Summary: Classifies the endings of accepting an actor, including the actor that does not exist, and projects what was recorded.
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes blockchain::TE_ACCEPT_ACTOR_V0
    - Capability: Offer recording a verification decision to a caller outside the business
      Family: TI
      Code: blockchain::TI_REJECT_ACTOR_V0
      Summary: Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the decision, admitted states and outcomes, and the rejection occurrence label.
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes blockchain::TI_REJECT_ACTOR_V0
    - Capability: Tell a caller how their decision ended
      Family: TE
      Code: blockchain::TE_REJECT_ACTOR_V0
      Summary: Classifies the endings of rejecting an actor, including the actor that does not exist, and projects what was recorded.
      Owner Subdomain: identity
      Status: NEW
      Source Finding: S5 provisional_codes blockchain::TE_REJECT_ACTOR_V0
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
      CS Bindings: Unchanged by this change
      Storage Structure: Unchanged by this change
      Source Finding: S6 ownership Admit a person's registration
    - RB Code: blockchain::RB_IDENTITY_BINDINGS_V0
      Binds WF: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      CS Bindings: Unchanged by this change
      Storage Structure: Unchanged by this change
      Source Finding: S6 ownership Record an authority's decision
  execution_topology:
    columns:
    - Workflow
    - Node
    - Node Type
    - Routing
    - Source Finding
    rows:
    - Workflow: blockchain::WF_REGISTER_ACTOR_V0
      Node: blockchain::IN_ACTOR_REGISTERED_V0
      Node Type: IN
      Routing: Unchanged by this change; what a caller sends becomes this act's payload and the act routes as it already does
      Source Finding: S6 ownership Admit a person's registration
    - Workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Node: blockchain::IN_ACTOR_VERIFIED_V0
      Node Type: IN
      Routing: Unchanged by this change; both decision declarations reach this same entry, differing only in what they hold
      Source Finding: S6 ownership Record an authority's decision
  cc_composition:
    columns:
    - CC Code
    - Step
    - Step Name
    - Capability
    - Kind
    - Operation
    - Store
    - Consumes
    - Produces
    - Routing
    - Interpreted By
    - Semantic Status
    - Interface
    rows: []
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction
    - Field
    - Bound To
    - Source Finding
    rows: []
  interface_fields:
    columns:
    - Artifact
    - Direction
    - Field
    - Type
    - Required
    - Default
    - Meaning
    rows:
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INPUT
      Field: name
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: What the person is called, supplied by them.
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INPUT
      Field: contact_address
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The address the person registers with, which is what identifies them as an actor.
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Direction: OUTPUT
      Field: contact_address
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The address the actor was admitted under.
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Direction: OUTPUT
      Field: occurrence
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: Which moment was recorded.
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Direction: OUTPUT
      Field: occurred_at
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The time the occurrence happened, determined as it occurred.
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Direction: OUTPUT
      Field: sequence_number
      Type: integer
      Required: 'YES'
      Default: ''
      Meaning: The position at which the occurrence was written to the trail.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INPUT
      Field: contact_address
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The actor being accepted.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INPUT
      Field: verifying_authority
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The authority recording the acceptance. Recorded as named and never resolved.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INPUT
      Field: grounds
      Type: string
      Required: 'NO'
      Default: ''
      Meaning: The reason stated. Optional on an acceptance, where the decision is itself the statement.
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: OUTPUT
      Field: contact_address
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The actor the decision was recorded against.
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: OUTPUT
      Field: occurrence
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: Which moment was recorded.
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: OUTPUT
      Field: verifying_authority
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The authority the record names.
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: OUTPUT
      Field: grounds
      Type: string
      Required: 'NO'
      Default: ''
      Meaning: The grounds recorded, absent when none were stated.
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: OUTPUT
      Field: occurred_at
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The time the decision was recorded.
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: OUTPUT
      Field: sequence_number
      Type: integer
      Required: 'YES'
      Default: ''
      Meaning: The position at which the occurrence was written to the trail.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INPUT
      Field: contact_address
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The actor being rejected.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INPUT
      Field: verifying_authority
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The authority recording the rejection. Recorded as named and never resolved.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INPUT
      Field: grounds
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The reason stated. Required on a rejection, where the grounds are the substance of the decision.
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: OUTPUT
      Field: contact_address
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The actor the decision was recorded against.
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: OUTPUT
      Field: occurrence
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: Which moment was recorded.
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: OUTPUT
      Field: verifying_authority
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The authority the record names.
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: OUTPUT
      Field: grounds
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The grounds stated for the rejection.
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: OUTPUT
      Field: occurred_at
      Type: string
      Required: 'YES'
      Default: ''
      Meaning: The time the decision was recorded.
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: OUTPUT
      Field: sequence_number
      Type: integer
      Required: 'YES'
      Default: ''
      Meaning: The position at which the occurrence was written to the trail.
  implementation_bindings:
    columns:
    - CT Code
    - Module
    - Callable
    - Operation
    - Kind (atom, molecule)
    - Purity (ct_pure, ct_impure)
    - Source Finding
    rows: []
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
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
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Property: governed_by
      Value: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
      Source Finding: S6 cross_subdomain_deps The governed kind that admits a request from outside
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Property: governed_by
      Value: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
      Source Finding: S6 cross_subdomain_deps The governed kind that admits a request from outside
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Property: governed_by
      Value: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
      Source Finding: S6 cross_subdomain_deps The governed kind that admits a request from outside
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Property: context_requirements
      Value: none — the boundary requires no context of a caller, and this change establishes nothing about who they are
      Source Finding: S6 ownership Establishing who a caller is, and what they are allowed to do
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Property: context_requirements
      Value: none — the boundary requires no context of a caller, and this change establishes nothing about who they are
      Source Finding: S6 ownership Establishing who a caller is, and what they are allowed to do
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Property: context_requirements
      Value: none — the boundary requires no context of a caller, and this change establishes nothing about who they are
      Source Finding: S6 ownership Establishing who a caller is, and what they are allowed to do
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Property: governed_by
      Value: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
      Source Finding: S6 cross_subdomain_deps The governed kind that states what a caller is told
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Property: governed_by
      Value: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
      Source Finding: S6 cross_subdomain_deps The governed kind that states what a caller is told
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Property: governed_by
      Value: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
      Source Finding: S6 cross_subdomain_deps The governed kind that states what a caller is told
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Property: result_class.SUCCESS
      Value: SUCCESS
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Property: result_class.VIOLATION
      Value: VIOLATION
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Property: result_class.NOT_FOUND
      Value: NOT_FOUND
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Property: result_class.SUCCESS
      Value: SUCCESS
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Property: result_class.VIOLATION
      Value: VIOLATION
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Property: result_class.NOT_FOUND
      Value: NOT_FOUND
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Property: result_class.SUCCESS
      Value: SUCCESS
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Property: result_class.VIOLATION
      Value: VIOLATION
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Property: result_class.NOT_FOUND
      Value: NOT_FOUND
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Property: default_result_class
      Value: EXECUTION_FAILURE
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Property: default_result_class
      Value: EXECUTION_FAILURE
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Property: default_result_class
      Value: EXECUTION_FAILURE
      Source Finding: S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Property: evidence_policy
      Value: reference_only
      Source Finding: 'S4 design_decisions #6'
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Property: evidence_policy
      Value: reference_only
      Source Finding: 'S4 design_decisions #6'
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Property: evidence_policy
      Value: reference_only
      Source Finding: 'S4 design_decisions #6'
  structure_stores:
    columns:
    - Store Name
    - Storage Type
    - Proposed Path
    - Used By
    - Source Finding
    rows: []
  transport_bindings:
    columns:
    - Artifact
    - Direction
    - Operation
    - Handler Kind
    - Handler Target
    - Field
    - Bound To
    - Source Finding
    rows:
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.name
      Bound To: ${input.name}
      Source Finding: S7 interface_fields blockchain::TI_REGISTER_ACTOR_V0 name
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.contact_address
      Bound To: ${input.contact_address}
      Source Finding: S7 interface_fields blockchain::TI_REGISTER_ACTOR_V0 contact_address
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.state
      Bound To: UNVERIFIED
      Source Finding: S7 design_resolution The two preferences are not offered to a caller and are recorded at their declared defaults.
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.currency_preference
      Bound To: BACHI
      Source Finding: S7 design_resolution The two preferences are not offered to a caller and are recorded at their declared defaults.
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: actor_record.language
      Bound To: en
      Source Finding: S7 design_resolution The two preferences are not offered to a caller and are recorded at their declared defaults.
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: registration_schema.name.required
      Bound To: 'true'
      Source Finding: S6 boundary_rules ONE_TEST_STATED_TWICE
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: registration_schema.name.type
      Bound To: string
      Source Finding: S6 boundary_rules ONE_TEST_STATED_TWICE
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: registration_schema.contact_address.required
      Bound To: 'true'
      Source Finding: S6 boundary_rules ONE_TEST_STATED_TWICE
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: registration_schema.contact_address.type
      Bound To: string
      Source Finding: S6 boundary_rules ONE_TEST_STATED_TWICE
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: address_path
      Bound To: contact_address
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: address_type
      Bound To: string
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: stream_id
      Bound To: ACTOR_OCCURRENCES
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: occurrence_fields.occurrence
      Bound To: ACTOR_REGISTERED_UNVERIFIED
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_REGISTER_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: occurrence_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: S7 interface_fields blockchain::TI_REGISTER_ACTOR_V0 contact_address
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: contact_address
      Bound To: surface.contact_address
      Source Finding: S7 interface_fields blockchain::TE_REGISTER_ACTOR_V0 contact_address
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: occurrence
      Bound To: surface.record.occurrence
      Source Finding: S7 interface_fields blockchain::TE_REGISTER_ACTOR_V0 occurrence
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: occurred_at
      Bound To: surface.record.occurred_at
      Source Finding: S7 interface_fields blockchain::TE_REGISTER_ACTOR_V0 occurred_at
    - Artifact: blockchain::TE_REGISTER_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.register_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_REGISTER_ACTOR_V0
      Field: sequence_number
      Bound To: surface.sequence_number
      Source Finding: S7 interface_fields blockchain::TE_REGISTER_ACTOR_V0 sequence_number
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: contact_address
      Bound To: ${input.contact_address}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 contact_address
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decision
      Bound To: ACCEPTED
      Source Finding: S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: grounds
      Bound To: ${input.grounds}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 grounds
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: states_admitting_a_decision
      Bound To: '[UNVERIFIED]'
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: admitted_outcomes
      Bound To: '[ACCEPTED, REJECTED]'
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decided_actor_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 contact_address
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decided_actor_fields.state
      Bound To: ACCEPTED
      Source Finding: S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decided_actor_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decided_actor_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 grounds
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: stream_id
      Bound To: ACTOR_OCCURRENCES
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence_fields.occurrence
      Bound To: ACTOR_ACCEPTED
      Source Finding: S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection.
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 contact_address
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority
    - Artifact: blockchain::TI_ACCEPT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 grounds
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: contact_address
      Bound To: surface.contact_address
      Source Finding: S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 contact_address
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence
      Bound To: surface.record.occurrence
      Source Finding: S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 occurrence
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: verifying_authority
      Bound To: surface.record.verifying_authority
      Source Finding: S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 verifying_authority
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: grounds
      Bound To: surface.record.grounds
      Source Finding: S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 grounds
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurred_at
      Bound To: surface.record.occurred_at
      Source Finding: S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 occurred_at
    - Artifact: blockchain::TE_ACCEPT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.accept_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: sequence_number
      Bound To: surface.sequence_number
      Source Finding: S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 sequence_number
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: contact_address
      Bound To: ${input.contact_address}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 contact_address
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 verifying_authority
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decision
      Bound To: REJECTED
      Source Finding: S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: grounds
      Bound To: ${input.grounds}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 grounds
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: states_admitting_a_decision
      Bound To: '[UNVERIFIED]'
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: admitted_outcomes
      Bound To: '[ACCEPTED, REJECTED]'
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decided_actor_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 contact_address
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decided_actor_fields.state
      Bound To: REJECTED
      Source Finding: S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decided_actor_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 verifying_authority
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: decided_actor_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 grounds
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: stream_id
      Bound To: ACTOR_OCCURRENCES
      Source Finding: S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence_fields.occurrence
      Bound To: ACTOR_REJECTED
      Source Finding: S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection.
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence_fields.contact_address
      Bound To: ${input.contact_address}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 contact_address
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence_fields.verifying_authority
      Bound To: ${input.verifying_authority}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 verifying_authority
    - Artifact: blockchain::TI_REJECT_ACTOR_V0
      Direction: INGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence_fields.grounds
      Bound To: ${input.grounds}
      Source Finding: S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 grounds
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: contact_address
      Bound To: surface.contact_address
      Source Finding: S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 contact_address
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurrence
      Bound To: surface.record.occurrence
      Source Finding: S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 occurrence
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: verifying_authority
      Bound To: surface.record.verifying_authority
      Source Finding: S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 verifying_authority
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: grounds
      Bound To: surface.record.grounds
      Source Finding: S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 grounds
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: occurred_at
      Bound To: surface.record.occurred_at
      Source Finding: S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 occurred_at
    - Artifact: blockchain::TE_REJECT_ACTOR_V0
      Direction: EGRESS
      Operation: blockchain.reject_actor
      Handler Kind: WF_INVOCATION
      Handler Target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Field: sequence_number
      Bound To: surface.sequence_number
      Source Finding: S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 sequence_number
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Count: '6'
      Artifacts: 3 TI, 3 TE
```

Six artifacts, all of them boundary declarations. No workflow, contract, transform, event, actor or
store is authored: the acts being offered already exist and are reached unchanged. What is designed
here is what a caller may name, what they may send, what is held for them, and what they are told.

---

## 1. Design Resolution

---

## 2. Existing Inventory

---

## 3. New Artifacts

---

## 4. Runtime Binding Declarations

---

## 5. Execution Topology

---

## 6. Capability Contract Composition

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

## 13. Structure Stores

---

## 14. Transport Bindings

---

## 15. Artifact Summary

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions, provisional codes | COMPLETE |
| Stage 6 — Governance Intent | Ownership, dependencies, boundary rules | COMPLETE |
| Stage 7 — Design Intent | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · interface_fields · artifact_properties · transport_bindings · artifact_summary |
