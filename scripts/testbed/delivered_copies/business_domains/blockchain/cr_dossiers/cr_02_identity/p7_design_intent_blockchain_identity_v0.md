# Stage 7 — Design Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p7
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: The decision act is offered as two named acts, one for acceptance and one for rejection.
    business_fact: The business holds a rejection to be its own occurrence, distinct in kind from an acceptance, and refuses to record one decision distinguished by a field.
    resolution: Each act records a fixed occurrence — accepted or rejected — and a boundary declaration substitutes whole values and passes constants; it derives nothing. One act carrying the decision as a field would require the occurrence to be computed from it, which no declaration can do. Two acts each hold a constant, and the split follows what the business already records.
    source_finding: {phase: p5, register: provisional_codes, key: 'blockchain::TI_ACCEPT_ACTOR_V0'}
  - decision: A workflow input may be the caller's own data or a constant, never a derivation of the caller's data.
    business_fact: The business asks that a caller send only their own details, and that what judges them is held by the business.
    resolution: The deciding act takes an occurrence name derived from the decision. Nothing in the act computes it, so whoever assembles the payload does — a person, silently, when the caller was inside the business. Reached from outside there is no such person. Where the derived value has one possible value per act it is held as a constant here; where it does not, the derivation belongs inside the act, which is the change GAP-11 records.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  - decision: The two preferences are not offered to a caller and are recorded at their declared defaults.
    business_fact: The business records a preferred currency and a preferred language for every actor, each having a default, so that nothing downstream must decide what an absent preference means.
    resolution: The boundary applies no default — an optional field a caller omits is omitted from what the act receives, and the act supplies nothing in its place. Rather than admit an actor carrying no preference, the declarations hold both defaults as constants. A caller states no preference because the page does not ask; every actor still carries an answer.
    source_finding: {phase: p1, register: known_facts, row: 28}
  - decision: Grounds are optional on an acceptance and required on a rejection.
    business_fact: The business requires grounds for a rejection, where they are the substance of the decision, and permits their omission on an acceptance, where the decision is the statement.
    resolution: 'Each act declares its own requirement, which is possible only because they are two declarations. Verified against the pinned snapshot: an acceptance carrying no grounds is admitted and records grounds as absent rather than failing.'
    source_finding: {phase: p1, register: known_facts, row: 19}
  - decision: What a caller sends is named in the business's own terms, not the prior implementation's.
    business_fact: The business names an actor by their name and their contact address, and a decision by its authority and its grounds.
    resolution: 'The pages are lifted from the prior implementation and their fields are replaced: what it called a first name, a last name and an email registration is one name and one contact address; what it called a verifier and notes is the verifying authority and the grounds. The form and the way it gathers what is typed survive; none of its names does.'
    source_finding: {phase: p4, register: design_decisions, row: 7}
  existing_inventory:
  - fqdn: blockchain::WF_REGISTER_ACTOR_V0
    action: REUSE
    summary: The governed sequence that admits a person as an unverified actor.
    reason: Reached unchanged by a new boundary declaration. Nothing about the act is amended, and it is impacted by nothing in the composition.
    source_finding: {phase: p6, register: ownership, key: Admit a person's registration}
  - fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    action: REUSE
    summary: The governed sequence that records an authority's decision against a registered actor.
    reason: Reached unchanged by two new boundary declarations, one for each outcome the business records.
    source_finding: {phase: p6, register: ownership, key: Record an authority's decision}
  - fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    action: REVIEW
    summary: Confirms a registration carries a name and an address of the form asked for.
    reason: Untouched, but the declaration it validates against is now supplied by a sealed boundary artifact rather than by whoever calls. Same contract, different provenance for its input.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::CC_VALIDATE_REGISTRATION_V0'}
  - fqdn: blockchain::AC_PARTICIPANT_V0
    action: REUSE
    summary: Declares the kind of party that performs identity's acts.
    reason: Reused unchanged. A caller from outside is not established to be this or any actor.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'blockchain::AC_PARTICIPANT_V0'}
  - fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
    action: REUSE
    summary: Binds identity's workflows to the stores they use.
    reason: Reused unchanged; the acts reached bind exactly as they did.
    source_finding: {phase: p6, register: ownership, key: Admit a person's registration}
  - fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    action: REUSE
    summary: The request that starts the act of admitting a person.
    reason: Reached unchanged; what a caller sends becomes this act's payload.
    source_finding: {phase: p6, register: ownership, key: Admit a person's registration}
  - fqdn: blockchain::IN_ACTOR_VERIFIED_V0
    action: REUSE
    summary: The request that starts the act of recording a decision.
    reason: Reached unchanged by both decision declarations.
    source_finding: {phase: p6, register: ownership, key: Record an authority's decision}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    action: REUSE
    summary: Reads a supplied record for fields the declaration requires and for the form they must take.
    reason: Reused unchanged, reached through the act. Impacted by 31 artifacts.
    source_finding: {phase: p6, register: cross_subdomain_deps, key: Reading a record for absence and for form}
  - fqdn: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    action: REUSE
    summary: Governs the kind that admits a request from outside.
    reason: Governs the three new ingress declarations; not amended.
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The governed kind that admits a request from outside}
  - fqdn: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
    action: REUSE
    summary: Governs the kind that states what a caller is told, over a closed set of answer kinds.
    reason: Governs the three new egress declarations; not amended, and its closed set is not extended.
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The governed kind that states what a caller is told}
  - fqdn: workload::TI_COLLATZ_COMPUTE_V0
    action: REUSE
    summary: The worked precedent for a public name, a declared caller input and a template holding what a caller does not send.
    reason: Read, not changed.
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The worked precedent for naming an act and holding what a caller does not send}
  - fqdn: workload::TE_COLLATZ_COMPUTE_V0
    action: REUSE
    summary: The worked precedent for classifying an ending and exposing evidence by reference.
    reason: Read, not changed.
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The worked precedent for classifying an ending and exposing evidence by reference}
  new_artifacts:
  - capability: Offer registering an actor to a caller outside the business
    family: TI
    code: blockchain::TI_REGISTER_ACTOR_V0
    summary: Admits a request to register an actor, declaring the name and contact address a caller sends and holding the schema, address path, stream, preferences and occurrence label the act requires.
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: 'blockchain::TI_REGISTER_ACTOR_V0'}
  - capability: Tell a caller how their registration ended
    family: TE
    code: blockchain::TE_REGISTER_ACTOR_V0
    summary: Classifies the endings of registering an actor and projects the contact address, the occurrence, its time and its position.
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: 'blockchain::TE_REGISTER_ACTOR_V0'}
  - capability: Offer recording a verification decision to a caller outside the business
    family: TI
    code: blockchain::TI_ACCEPT_ACTOR_V0
    summary: Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the decision, admitted states and outcomes, and the acceptance occurrence label.
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: 'blockchain::TI_ACCEPT_ACTOR_V0'}
  - capability: Tell a caller how their decision ended
    family: TE
    code: blockchain::TE_ACCEPT_ACTOR_V0
    summary: Classifies the endings of accepting an actor, including the actor that does not exist, and projects what was recorded.
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: 'blockchain::TE_ACCEPT_ACTOR_V0'}
  - capability: Offer recording a verification decision to a caller outside the business
    family: TI
    code: blockchain::TI_REJECT_ACTOR_V0
    summary: Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the decision, admitted states and outcomes, and the rejection occurrence label.
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: 'blockchain::TI_REJECT_ACTOR_V0'}
  - capability: Tell a caller how their decision ended
    family: TE
    code: blockchain::TE_REJECT_ACTOR_V0
    summary: Classifies the endings of rejecting an actor, including the actor that does not exist, and projects what was recorded.
    owner_subdomain: identity
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: 'blockchain::TE_REJECT_ACTOR_V0'}
  rb_declarations:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REGISTER_ACTOR_V0
    cs_bindings:
    - Unchanged by this change
    storage_structure: Unchanged by this change
    source_finding: {phase: p6, register: ownership, key: Admit a person's registration}
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    cs_bindings:
    - Unchanged by this change
    storage_structure: Unchanged by this change
    source_finding: {phase: p6, register: ownership, key: Record an authority's decision}
  execution_topology:
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: blockchain::IN_ACTOR_REGISTERED_V0
    node_type: IN
    routing: Unchanged by this change; what a caller sends becomes this act's payload and the act routes as it already does
    source_finding: {phase: p6, register: ownership, key: Admit a person's registration}
  - workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    node: blockchain::IN_ACTOR_VERIFIED_V0
    node_type: IN
    routing: Unchanged by this change; both decision declarations reach this same entry, differing only in what they hold
    source_finding: {phase: p6, register: ownership, key: Record an authority's decision}
  cc_composition: null
  step_bindings: null
  interface_fields:
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INPUT
    field: name
    type: string
    required: 'YES'
    default: ''
    meaning: What the person is called, supplied by them.
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The address the person registers with, which is what identifies them as an actor.
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: OUTPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The address the actor was admitted under.
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: OUTPUT
    field: occurrence
    type: string
    required: 'YES'
    default: ''
    meaning: Which moment was recorded.
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: OUTPUT
    field: occurred_at
    type: string
    required: 'YES'
    default: ''
    meaning: The time the occurrence happened, determined as it occurred.
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The position at which the occurrence was written to the trail.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor being accepted.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority recording the acceptance. Recorded as named and never resolved.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: The reason stated. Optional on an acceptance, where the decision is itself the statement.
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: OUTPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor the decision was recorded against.
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: OUTPUT
    field: occurrence
    type: string
    required: 'YES'
    default: ''
    meaning: Which moment was recorded.
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: OUTPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority the record names.
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: OUTPUT
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: The grounds recorded, absent when none were stated.
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: OUTPUT
    field: occurred_at
    type: string
    required: 'YES'
    default: ''
    meaning: The time the decision was recorded.
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The position at which the occurrence was written to the trail.
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor being rejected.
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority recording the rejection. Recorded as named and never resolved.
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'YES'
    default: ''
    meaning: The reason stated. Required on a rejection, where the grounds are the substance of the decision.
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: OUTPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The actor the decision was recorded against.
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: OUTPUT
    field: occurrence
    type: string
    required: 'YES'
    default: ''
    meaning: Which moment was recorded.
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: OUTPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: The authority the record names.
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: OUTPUT
    field: grounds
    type: string
    required: 'YES'
    default: ''
    meaning: The grounds stated for the rejection.
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: OUTPUT
    field: occurred_at
    type: string
    required: 'YES'
    default: ''
    meaning: The time the decision was recorded.
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The position at which the occurrence was written to the trail.
  implementation_bindings: null
  vocabulary_extensions: null
  runtime_policies: null
  artifact_properties:
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    property: governed_by
    value: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The governed kind that admits a request from outside}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    property: governed_by
    value: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The governed kind that admits a request from outside}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    property: governed_by
    value: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The governed kind that admits a request from outside}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    property: context_requirements
    value: none — the boundary requires no context of a caller, and this change establishes nothing about who they are
    source_finding: {phase: p6, register: ownership, key: 'Establishing who a caller is, and what they are allowed to do'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    property: context_requirements
    value: none — the boundary requires no context of a caller, and this change establishes nothing about who they are
    source_finding: {phase: p6, register: ownership, key: 'Establishing who a caller is, and what they are allowed to do'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    property: context_requirements
    value: none — the boundary requires no context of a caller, and this change establishes nothing about who they are
    source_finding: {phase: p6, register: ownership, key: 'Establishing who a caller is, and what they are allowed to do'}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: governed_by
    value: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The governed kind that states what a caller is told}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: governed_by
    value: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The governed kind that states what a caller is told}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: governed_by
    value: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
    source_finding: {phase: p6, register: cross_subdomain_deps, key: The governed kind that states what a caller is told}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: result_class.SUCCESS
    value: SUCCESS
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: result_class.VIOLATION
    value: VIOLATION
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: result_class.NOT_FOUND
    value: NOT_FOUND
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: result_class.SUCCESS
    value: SUCCESS
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: result_class.VIOLATION
    value: VIOLATION
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: result_class.NOT_FOUND
    value: NOT_FOUND
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: result_class.SUCCESS
    value: SUCCESS
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: result_class.VIOLATION
    value: VIOLATION
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: result_class.NOT_FOUND
    value: NOT_FOUND
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: default_result_class
    value: EXECUTION_FAILURE
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: default_result_class
    value: EXECUTION_FAILURE
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: default_result_class
    value: EXECUTION_FAILURE
    source_finding: {phase: p6, register: boundary_rules, key: THE_ANSWER_KINDS_ARE_NOT_OURS}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: evidence_policy
    value: reference_only
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: evidence_policy
    value: reference_only
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: evidence_policy
    value: reference_only
    source_finding: {phase: p4, register: design_decisions, row: 6}
  structure_stores: null
  transport_bindings:
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.name
    bound_to: ${input.name}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REGISTER_ACTOR_V0 name'}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REGISTER_ACTOR_V0 contact_address'}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.state
    bound_to:
      literal: UNVERIFIED
    source_finding: {phase: p7, register: design_resolution, key: The two preferences are not offered to a caller and are recorded at their declared defaults.}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.currency_preference
    bound_to:
      literal: BACHI
    source_finding: {phase: p7, register: design_resolution, key: The two preferences are not offered to a caller and are recorded at their declared defaults.}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.language
    bound_to:
      literal: en
    source_finding: {phase: p7, register: design_resolution, key: The two preferences are not offered to a caller and are recorded at their declared defaults.}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: registration_schema.name.required
    bound_to:
      literal: true
    source_finding: {phase: p6, register: boundary_rules, key: ONE_TEST_STATED_TWICE}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: registration_schema.name.type
    bound_to:
      literal: string
    source_finding: {phase: p6, register: boundary_rules, key: ONE_TEST_STATED_TWICE}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: registration_schema.contact_address.required
    bound_to:
      literal: true
    source_finding: {phase: p6, register: boundary_rules, key: ONE_TEST_STATED_TWICE}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: registration_schema.contact_address.type
    bound_to:
      literal: string
    source_finding: {phase: p6, register: boundary_rules, key: ONE_TEST_STATED_TWICE}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: address_path
    bound_to:
      literal: contact_address
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: address_type
    bound_to:
      literal: string
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: occurrence_fields.occurrence
    bound_to:
      literal: ACTOR_REGISTERED_UNVERIFIED
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: occurrence_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REGISTER_ACTOR_V0 contact_address'}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: EGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: contact_address
    bound_to: surface.contact_address
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REGISTER_ACTOR_V0 contact_address'}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: EGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: occurrence
    bound_to: surface.record.occurrence
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REGISTER_ACTOR_V0 occurrence'}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: EGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: occurred_at
    bound_to: surface.record.occurred_at
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REGISTER_ACTOR_V0 occurred_at'}
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: EGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: sequence_number
    bound_to: surface.sequence_number
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REGISTER_ACTOR_V0 sequence_number'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 contact_address'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decision
    bound_to:
      literal: ACCEPTED
    source_finding: {phase: p7, register: design_resolution, key: 'The decision act is offered as two named acts, one for acceptance and one for rejection.'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 grounds'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: states_admitting_a_decision
    bound_to:
      literal:
      - UNVERIFIED
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: admitted_outcomes
    bound_to:
      literal:
      - ACCEPTED
      - REJECTED
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decided_actor_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 contact_address'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decided_actor_fields.state
    bound_to:
      literal: ACCEPTED
    source_finding: {phase: p7, register: design_resolution, key: 'The decision act is offered as two named acts, one for acceptance and one for rejection.'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decided_actor_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decided_actor_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 grounds'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence_fields.occurrence
    bound_to:
      literal: ACTOR_ACCEPTED
    source_finding: {phase: p7, register: design_resolution, key: 'The decision act is offered as two named acts, one for acceptance and one for rejection.'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 contact_address'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority'}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_ACCEPT_ACTOR_V0 grounds'}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: contact_address
    bound_to: surface.contact_address
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_ACCEPT_ACTOR_V0 contact_address'}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence
    bound_to: surface.record.occurrence
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_ACCEPT_ACTOR_V0 occurrence'}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: verifying_authority
    bound_to: surface.record.verifying_authority
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_ACCEPT_ACTOR_V0 verifying_authority'}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: grounds
    bound_to: surface.record.grounds
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_ACCEPT_ACTOR_V0 grounds'}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurred_at
    bound_to: surface.record.occurred_at
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_ACCEPT_ACTOR_V0 occurred_at'}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: sequence_number
    bound_to: surface.sequence_number
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_ACCEPT_ACTOR_V0 sequence_number'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 contact_address'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 verifying_authority'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decision
    bound_to:
      literal: REJECTED
    source_finding: {phase: p7, register: design_resolution, key: 'The decision act is offered as two named acts, one for acceptance and one for rejection.'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 grounds'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: states_admitting_a_decision
    bound_to:
      literal:
      - UNVERIFIED
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: admitted_outcomes
    bound_to:
      literal:
      - ACCEPTED
      - REJECTED
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decided_actor_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 contact_address'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decided_actor_fields.state
    bound_to:
      literal: REJECTED
    source_finding: {phase: p7, register: design_resolution, key: 'The decision act is offered as two named acts, one for acceptance and one for rejection.'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decided_actor_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 verifying_authority'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: decided_actor_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 grounds'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding: {phase: p6, register: boundary_rules, key: THE_CALLER_SENDS_ONLY_THEIR_OWN}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence_fields.occurrence
    bound_to:
      literal: ACTOR_REJECTED
    source_finding: {phase: p7, register: design_resolution, key: 'The decision act is offered as two named acts, one for acceptance and one for rejection.'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence_fields.contact_address
    bound_to: ${input.contact_address}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 contact_address'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence_fields.verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 verifying_authority'}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence_fields.grounds
    bound_to: ${input.grounds}
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TI_REJECT_ACTOR_V0 grounds'}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: contact_address
    bound_to: surface.contact_address
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REJECT_ACTOR_V0 contact_address'}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurrence
    bound_to: surface.record.occurrence
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REJECT_ACTOR_V0 occurrence'}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: verifying_authority
    bound_to: surface.record.verifying_authority
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REJECT_ACTOR_V0 verifying_authority'}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: grounds
    bound_to: surface.record.grounds
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REJECT_ACTOR_V0 grounds'}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: occurred_at
    bound_to: surface.record.occurred_at
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REJECT_ACTOR_V0 occurred_at'}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    field: sequence_number
    bound_to: surface.sequence_number
    source_finding: {phase: p7, register: interface_fields, key: 'blockchain::TE_REJECT_ACTOR_V0 sequence_number'}
  artifact_summary:
  - action: NEW
    subdomain: identity
    count: '6'
    artifacts: 3 TI, 3 TE
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
