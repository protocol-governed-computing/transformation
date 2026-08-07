# WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0

## Header (Mandatory)

- **Artifact Code:** WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Phase 7 of the change pipeline: decide whether an offered Design Intent register is admissible.

P7 answers HOW, and it is where identity becomes binding. Stage 5 assigned provisional codes and
Stage 6 placed capabilities in subdomains; this phase turns those into domain-qualified FQDNs that
later phases, the compiler and the runtime all use verbatim. **Gate 1 closes here** — the dossier is
reviewed as a body before any mandate may be drafted.

---

## 2. The one rule that runs backwards

Every earlier phase cites artifacts that exist, and is wrong when a citation fails to resolve. This
phase assigns identities that *will* exist, and is wrong when one **does**. A code colliding with
something already in the composition is not a new artifact — it is a silent redefinition of an old
one, and nothing downstream would notice.

So this workflow grounds for the opposite reason every other grounded phase does: not to confirm a
citation, but to refuse a name already taken. A collision check that could not see the composition
would admit every colliding name, so an unobserved composition is itself the finding.

## 3. Immutability discipline

A binding FQDN is assigned once and reused as the exact same string everywhere. A spelling variant
of the same concept does not read as a synonym; it creates a second, permanently misnamed artifact.
Every code referenced in the topology, in a runtime binding, or in a composition must therefore be
declared — as new here, or as an existing artifact carried over. A reference to neither is a name
nobody owns.

---

## Machine

```yaml
fqdn: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Design Intent register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_DESIGN_INTENT_SUBMITTED_V0

  nodes:
    IN_DESIGN_INTENT_SUBMITTED_V0:
      type: IN
      code: IN_DESIGN_INTENT_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_AGAINST_SNAPSHOT_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_AGAINST_SNAPSHOT_V0:
      type: CC
      code: CC_JUDGE_AGAINST_SNAPSHOT_V0
      inputs:
        document_text: $.payload.register_text
        prior_texts: $.payload.prior_texts
        rule_set:
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: design_resolution
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: design_resolution
          params:
            columns:
            - Decision
            - Business Fact
            - Resolution
            - Source Finding
          intent: downstream phases read these columns by name
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: design_resolution
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: design_resolution
          params:
            column: Source Finding
            known_registers: &id001
            - acceptance_criteria
            - actions
            - actors
            - analysis_findings
            - architectural_observations
            - artifact_properties
            - artifact_summary
            - assumptions
            - authoring_decisions
            - authoring_scope
            - authority_boundaries
            - authority_deferrals
            - belief_verification
            - bm_entities
            - boundary_rules
            - build_order
            - business_events
            - business_invariants
            - business_objects
            - business_processes
            - business_vocabulary
            - capability_graph
            - cc_composition
            - clarification_requests
            - constraint_register
            - constraints
            - cr_type
            - critical_path
            - cross_subdomain_deps
            - cross_subdomain_notes
            - cross_subdomain_refs
            - dependency_discoveries
            - dependency_graph
            - design_decisions
            - design_resolution
            - discovery_concerns
            - entities
            - entity_attributes
            - events
            - execution_topology
            - existing_inventory
            - field_declarations
            - gap_register
            - gaps
            - governance_outcome
            - governance_scope
            - identity_and_sameness
            - identity_semantics
            - impact_analysis
            - implementation_bindings
            - interface_fields
            - invariants
            - known_facts
            - lifecycle_states
            - lifecycle_transitions
            - mandate_artifact_summary
            - new_artifacts
            - new_capabilities
            - new_intents
            - open_questions
            - operation_refusals
            - out_of_scope
            - ownership
            - placement_decision
            - pps_artifacts_requiring_action
            - pps_baseline_fqdns
            - process_steps
            - provisional_codes
            - purpose_provenance
            - rb_declarations
            - relationships
            - requested_outcomes
            - resources
            - runtime_policies
            - saturation
            - scope_boundary
            - step_bindings
            - storage_governance
            - structure_stores
            - subdomain_purpose
            - system_beliefs
            - verification_results
            - vocabulary_extensions
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: existing_inventory
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: existing_inventory
          params:
            columns:
            - FQDN
            - Action
            - Summary
            - Reason
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: existing_inventory
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: existing_inventory
          params:
            column: Action
            vocabulary:
            - REPLACE
            - REUSE
            - EXTEND
            - REVIEW
          intent: Action is a controlled vocabulary declared by the template
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: existing_inventory
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: existing_inventory
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: new_artifacts
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: new_artifacts
          params:
            columns:
            - Capability
            - Family
            - Code
            - Summary
            - Owner Subdomain
            - Status
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: new_artifacts
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: new_artifacts
          params:
            column: Family
            vocabulary:
            - AC
            - IN
            - WF
            - RB
            - CC
            - CT
            - EV
            - VOCAB
            - STRUCTURE
          intent: Family is a controlled vocabulary declared by the template
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: new_artifacts
          params:
            columns:
            - capability
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: new_artifacts
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: new_artifacts
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: rb_declarations
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: rb_declarations
          params:
            columns:
            - RB Code
            - Binds WF
            - CS Bindings
            - Storage Structure
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: rb_declarations
          intent: an empty required register asserts nothing
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: rb_declarations
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: rb_declarations
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: execution_topology
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: execution_topology
          params:
            columns:
            - Workflow
            - Node
            - Node Type
            - Routing
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: execution_topology
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: execution_topology
          params:
            column: Node Type
            vocabulary:
            - IN
            - CC
            - EXIT
            - EXIT_SUCCESS
          intent: Node Type is a controlled vocabulary declared by the template
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: execution_topology
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: execution_topology
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: cc_composition
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: cc_composition
          params:
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
          intent: downstream phases read these columns by name
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: cc_composition
          params:
            column: Kind
            vocabulary:
            - CT
            - CS
          intent: Kind is a controlled vocabulary declared by the template
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: step_bindings
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: step_bindings
          params:
            columns:
            - Owner
            - Step
            - Direction
            - Field
            - Bound To
            - Source Finding
          intent: downstream phases read these columns by name
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: step_bindings
          params:
            column: Direction
            vocabulary:
            - INPUT
            - OUTPUT
          intent: Direction is a controlled vocabulary declared by the template
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: step_bindings
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: step_bindings
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: interface_fields
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: interface_fields
          params:
            columns:
            - Artifact
            - Direction
            - Field
            - Type
            - Required
            - Default
            - Meaning
          intent: downstream phases read these columns by name
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: interface_fields
          params:
            column: Direction
            vocabulary:
            - INPUT
            - OUTPUT
            - ATTRIBUTE
          intent: Direction is a controlled vocabulary declared by the template
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: interface_fields
          params:
            column: Required
            vocabulary:
            - 'YES'
            - 'NO'
          intent: Required is a controlled vocabulary declared by the template
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: implementation_bindings
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: implementation_bindings
          params:
            columns:
            - CT Code
            - Module
            - Callable
            - Operation
            - Kind (atom, molecule)
            - Purity (ct_pure, ct_impure)
            - Source Finding
          intent: downstream phases read these columns by name
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: implementation_bindings
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: implementation_bindings
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: vocabulary_extensions
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: vocabulary_extensions
          params:
            columns:
            - Vocabulary Code
            - Extends
            - Value
            - Meaning
            - Source Finding
          intent: downstream phases read these columns by name
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: vocabulary_extensions
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: vocabulary_extensions
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: runtime_policies
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: runtime_policies
          params:
            columns:
            - RB Code
            - Capability
            - Key
            - Value
            - Source Finding
          intent: downstream phases read these columns by name
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: runtime_policies
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: runtime_policies
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: artifact_properties
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: artifact_properties
          params:
            columns:
            - Artifact
            - Property
            - Value
            - Source Finding
          intent: downstream phases read these columns by name
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: artifact_properties
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: artifact_properties
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: structure_stores
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: structure_stores
          params:
            columns:
            - Store Name
            - Storage Type
            - Proposed Path
            - Used By
            - Source Finding
          intent: downstream phases read these columns by name
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: structure_stores
          params:
            column: Storage Type
            vocabulary:
            - CS_APPENDONLY_JSONL_V0
            - CS_MUTABLE_JSON_V0
            - CS_REGISTRY_V0
          intent: Storage Type is a controlled vocabulary declared by the template
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: structure_stores
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: structure_stores
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: artifact_summary
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: artifact_summary
          params:
            columns:
            - Action
            - Subdomain
            - Count
            - Artifacts
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: artifact_summary
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: artifact_summary
          params:
            column: Action
            vocabulary:
            - REPLACE
            - EXTEND
            - NEW
          intent: Action is a controlled vocabulary declared by the template
        - id: NEW_CODE_ALREADY_EXISTS
          check: CITED_ARTIFACTS_ABSENT
          register: new_artifacts
          params:
            column: Code
            pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
            observation: si.artifact.list
          intent: an identity assigned as new must not already name something else
        - id: NEW_CODE_MALFORMED
          check: CELL_MATCHES
          register: new_artifacts
          params:
            column: Code
            pattern: ^[a-z][a-z0-9_.]*::(?:WF|IN|RB|CC|CT|CS|EV|AC|VOCAB|STRUCTURE)_[A-Z0-9_]+_V\d+$
            detail: binding code {value!r} must be domain::FAMILY_NAME_V<n>
          intent: a binding identity is domain-qualified, family-prefixed and versioned
        - id: EXISTING_INVENTORY_UNRESOLVED
          check: CITED_ARTIFACTS_RESOLVE
          register: existing_inventory
          params:
            column: FQDN
            pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
            observation: si.artifact.list
          intent: an artifact carried over from the composition must really be in it
        - id: TOPOLOGY_WORKFLOW_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: execution_topology
          params:
            column: Workflow
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
          intent: a workflow in the topology is one this design declared or carried over
        - id: TOPOLOGY_NODE_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: execution_topology
          params:
            column: Node
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
            exempt_prefixes:
            - EXIT
            detail: a binding identity is immutable, so a spelling variant is a second artifact rather than a
              synonym
          intent: every node in the topology is an identity this design actually assigned
        - id: RB_BINDS_UNDECLARED_WORKFLOW
          check: CELL_RESOLVES_IN_REGISTER
          register: rb_declarations
          params:
            column: Binds WF
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
          intent: a runtime binding binds a workflow that exists in this design
        - id: RB_CODE_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: rb_declarations
          params:
            column: RB Code
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
          intent: a runtime binding is itself a declared artifact, never implicit
        - id: COMPOSITION_CC_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: cc_composition
          params:
            column: CC Code
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
          intent: a composition belongs to a capability contract this design declared
        - id: COMPOSITION_STEP_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: cc_composition
          params:
            column: Capability
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
          intent: a step invokes a capability that is declared new or carried over, never invented inline
        - id: OBSERVATION_WITHOUT_INTERPRETATION
          check: CELL_NOT_EMPTY
          register: cc_composition
          params:
            column: Interpreted By
            only_when_column: Kind
            only_when_value: CS
            detail: a step that reads external state names no interpreting transform — a raw observation cannot
              drive business routing, because the status it carries says the store answered, not what it found
          intent: every read of external state declares how its output becomes a decision
        - id: OBSERVATION_WITHOUT_SEMANTIC_STATUS
          check: CELL_NOT_EMPTY
          register: cc_composition
          params:
            column: Semantic Status
            only_when_column: Kind
            only_when_value: CS
            detail: a step that reads external state names no semantic status — the workflow branch it feeds has
              nothing declared to route on
          intent: an interpretation names the outcome it yields, closing the route
        - id: INTERPRETATION_TRANSFORM_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: cc_composition
          params:
            column: Interpreted By
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
            detail: an interpreting transform is an artifact like any other, declared or carried over
          intent: the transform that turns an observation into a decision is itself governed
        - id: STORE_WITHOUT_PROPOSED_PATH
          check: CELL_NOT_EMPTY
          register: structure_stores
          params:
            column: Proposed Path
            detail: store declares no proposed path — a store nobody can locate is not designed
          intent: a declared store says where it will live
        - id: SATISFIED_DEPENDENCY_NOT_INVENTORIED
          check: PRIOR_IDENTITIES_COVERED
          register: existing_inventory
          params:
            prior_phase: p6
            prior_register: cross_subdomain_deps
            prior_column: Existing Artifact
            column: FQDN
            require: prior_in_here
          intent: a dependency declared satisfied by an existing artifact must be inventoried as reuse
        - id: PROVISIONAL_CODE_NEVER_BOUND
          check: PRIOR_IDENTITIES_COVERED
          register: new_artifacts
          params:
            prior_phase: p5
            prior_register: provisional_codes
            prior_column: Provisional Code
            column: Code
            require: prior_in_here
            match_on: bare_code
            union:
            - register: existing_inventory
              column: FQDN
              only_when_column: Action
              only_when_value: EXTEND
          intent: a capability the business asked for and the design never bound is declined, not deferred
        - id: AUTHORED_ARTIFACT_WITHOUT_INTENT
          check: PRIOR_IDENTITIES_COVERED
          register: new_artifacts
          params:
            prior_phase: p5
            prior_register: provisional_codes
            prior_column: Provisional Code
            column: Code
            require: here_in_prior
            match_on: bare_code
          intent: an artifact the design authors is one the business asked for, never one it invented
        - id: WORKFLOW_WITHOUT_TOPOLOGY
          check: REGISTER_COVERS_REGISTER
          register: execution_topology
          params:
            source_register: new_artifacts
            source_column: Code
            column: Workflow
            only_when_column: Family
            only_when_value: WF
          intent: a workflow with no declared graph is a workflow construction would have to invent
        - id: WORKFLOW_WITHOUT_RUNTIME_BINDING
          check: REGISTER_COVERS_REGISTER
          register: rb_declarations
          params:
            source_register: new_artifacts
            source_column: Code
            column: Binds WF
            only_when_column: Family
            only_when_value: WF
          intent: a workflow with no runtime binding cannot resolve the capabilities it composes
        - id: CONTRACT_WITHOUT_COMPOSITION
          check: REGISTER_COVERS_REGISTER
          register: cc_composition
          params:
            source_register: new_artifacts
            source_column: Code
            column: CC Code
            only_when_column: Family
            only_when_value: CC
          intent: a capability contract with no declared pipeline specifies nothing to build
        - id: TRANSFORM_WITHOUT_IMPLEMENTATION
          check: REGISTER_COVERS_REGISTER
          register: implementation_bindings
          params:
            source_register: new_artifacts
            source_column: Code
            column: CT Code
            only_when_column: Family
            only_when_value: CT
          intent: a transform is the one family that points outside the composition; the path is designed, not
            discovered
        - id: VOCABULARY_WITHOUT_VALUES
          check: REGISTER_COVERS_REGISTER
          register: vocabulary_extensions
          params:
            source_register: new_artifacts
            source_column: Code
            column: Vocabulary Code
            only_when_column: Family
            only_when_value: VOCAB
          intent: a vocabulary that declares no value admits nothing
        - id: BINDING_STEP_OWNER_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: step_bindings
          params:
            column: Owner
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
          intent: a binding belongs to a workflow or contract this design declared
        - id: INTERFACE_ARTIFACT_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: interface_fields
          params:
            column: Artifact
            target_registers:
            - new_artifacts
            - existing_inventory
            target_column: Code
            target_columns:
            - Code
            - FQDN
          intent: a field belongs to an artifact this design declared
        - id: BINDING_READS_UNPUBLISHED_FIELD
          check: BINDING_SOURCE_PUBLISHED
          register: step_bindings
          params:
            step_register: cc_composition
            observation: si.capability.surface
          intent: a binding reads a field the operation yields, never one it was hoped would exist
        - id: STEP_CONSUMES_UNDECLARED_INPUT
          check: STEP_CONSUMES_PUBLISHED
          register: cc_composition
          params:
            observation: si.capability.surface
          intent: a step hands an operation fields it accepts, never ones it was hoped would exist
        - id: IMPLEMENTATION_WITHOUT_MODULE
          check: CELL_NOT_EMPTY
          register: implementation_bindings
          params:
            column: Module
            detail: transform names no module — an implementation nobody can locate is not designed
          intent: a declared implementation says where it lives
        - id: BINDING_WITHOUT_SOURCE
          check: CELL_NOT_EMPTY
          register: step_bindings
          params:
            column: Bound To
            detail: field is bound to nothing — construction would have to choose a source
          intent: every declared input names where its value comes from
        - id: STORE_PATH_FORMAT_MISMATCH
          check: STORE_PATH_MATCHES_STORAGE
          register: structure_stores
          params:
            storage_column: Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
            path_column: Proposed Path
            formats:
              CS_MUTABLE_JSON_V0: .json
              CS_REGISTRY_V0: .jsonl
              CS_APPENDONLY_JSONL_V0: .jsonl
          intent: a store is named for the format its capability actually writes
        - id: BINDING_SOURCE_UNROOTED
          check: BINDING_SOURCE_ROOTED
          register: step_bindings
          params:
            roots:
            - payload
            - inputs
            - results
            - capability_result
            - result_status
            value_roots:
            - result_status
          intent: a source that names a place is rooted in one execution scope actually offers
        - id: NODE_INPUT_UNBOUND
          check: NODE_INPUT_BOUND
          register: step_bindings
          params:
            topology_register: execution_topology
            fields_register: interface_fields
          intent: a workflow hands a contract everything that contract says it requires
        - id: BINDING_SOURCE_UNREACHABLE
          check: BINDING_SOURCE_REACHABLE
          register: step_bindings
          params:
            topology_register: execution_topology
            pattern: results\.([A-Za-z][A-Za-z0-9_.:]*?)\.
          intent: a source that names another node must name one this workflow reaches
        - id: REGISTER_CELL_UNRESOLVED
          check: UNRESOLVED_MARKER_ABSENT
          params:
            exempt: []
            detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask it
              as a clarification, do not hedge it in a register'
          intent: an unanswered question left in a register reads as decided to every later phase
        - id: HEADER_FIELD_MISSING
          check: HEADER_FIELD_PRESENT
          params:
            fields:
            - Stage
            - CR
            - Status
            - Feeds
          intent: a dossier document states its phase, its CR, its lifecycle state, and what it feeds
        - id: LIFECYCLE_STATE_NOT_IN_VOCABULARY
          check: HEADER_FIELD_MATCHES
          params:
            fields:
            - Status
            pattern: ^(DRAFT|CONSTRUCTION_COMPLETE|ADMITTED_UNVALIDATED|EXECUTION_VALIDATED|PROMOTED)\b
          intent: the lifecycle axis is a controlled vocabulary, not free text
      next:
        SUCCESS: EXIT_JUDGED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED

    EXIT_JUDGED:
      type: EXIT
      outcome: SUCCESS

    EXIT_REJECTED:
      type: EXIT
      outcome: VIOLATION
```
