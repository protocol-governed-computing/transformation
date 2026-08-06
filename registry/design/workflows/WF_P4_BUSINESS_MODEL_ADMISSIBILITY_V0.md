# WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0

## Header (Mandatory)

- **Artifact Code:** WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Phase 4 of the change pipeline: decide whether an offered Business Model register is admissible.

P4 **consolidates**. P2 discovered and P3 decided; P4 is the canonical artifact every later phase
projects from, and it introduces no new design. Its rule is consolidation, not re-litigation.

---

## 2. Why the defects here are between registers

Every earlier phase judges a register on its own terms, because discovery has nothing to be
consistent with yet. Consolidation is different: a capability graph pointing at a gap nobody
declared is broken in a way no single-register rule can see, because each register is individually
well formed while the document as a whole asserts something untrue.

So P4 is the first phase with cross-register rules — a CRITICAL capability must name a declared
gap, a gap must have an owner, and in-scope work must trace to a gap rather than to intent.

It grounds once, like P2: `dependency_graph` is the one register permitted to cite existing
artifacts by FQDN, so it is the one that must be checked against the composition.

---

## Machine

```yaml
fqdn: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Business Model register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_BUSINESS_MODEL_SUBMITTED_V0

  nodes:
    IN_BUSINESS_MODEL_SUBMITTED_V0:
      type: IN
      code: IN_BUSINESS_MODEL_SUBMITTED_V0
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
          register: actors
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: actors
          params:
            columns:
            - Actor
            - Role
            - Authority Class
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: actors
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: actors
          params:
            columns:
            - Actor
            - Role
            - Authority Class
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: actors
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: actors
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
          register: bm_entities
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: bm_entities
          params:
            columns:
            - Entity
            - Description
            - Store Model
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: bm_entities
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: bm_entities
          params:
            columns:
            - Entity
            - Description
            - Store Model
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: bm_entities
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: bm_entities
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
          register: resources
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: resources
          params:
            columns:
            - Resource
            - Description
            - Source Finding
          intent: downstream phases read these columns by name
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: resources
          params:
            columns:
            - Resource
            - Description
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: resources
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: resources
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
          register: events
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: events
          params:
            columns:
            - Event
            - Trigger
            - Lifecycle Meaning
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: events
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: events
          params:
            columns:
            - Event
            - Trigger
            - Lifecycle Meaning
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: events
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: events
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
          register: relationships
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: relationships
          params:
            columns:
            - Subject
            - Verb
            - Object
            - Capability Need
            - Source Finding
          intent: downstream phases read these columns by name
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: relationships
          params:
            columns:
            - Subject
            - Verb
            - Object
            - Capability Need
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: relationships
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: relationships
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
          register: capability_graph
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: capability_graph
          params:
            columns:
            - Capability
            - Source Finding
            - Status
            - Gap Register Entry
            - Notes
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: capability_graph
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: capability_graph
          params:
            columns:
            - Capability
            - Status
            - Gap Register Entry
            - Notes
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: capability_graph
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: capability_graph
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
          register: dependency_graph
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: dependency_graph
          params:
            columns:
            - From
            - To
            - Dependency Type
            - PPS Status
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: dependency_graph
          intent: an empty required register asserts nothing
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: dependency_graph
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: dependency_graph
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
          register: constraint_register
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: constraint_register
          params:
            columns:
            - '#'
            - Constraint
            - Source Finding
            - Source
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: constraint_register
          intent: an empty required register asserts nothing
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: constraint_register
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: constraint_register
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
          register: gap_register
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: gap_register
          params:
            columns:
            - Gap Code
            - Source Finding
            - Capability
            - Owner Subdomain
            - Resolution
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: gap_register
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: gap_register
          params:
            columns:
            - Gap Code
            - Capability
            - Owner Subdomain
            - Resolution
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: gap_register
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: gap_register
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
          register: design_decisions
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: design_decisions
          params:
            columns:
            - '#'
            - Decision
            - Source Finding
            - Rationale
            - Constraints Imposed
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: design_decisions
          intent: an empty required register asserts nothing
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: design_decisions
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: design_decisions
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
          register: authoring_scope
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: authoring_scope
          params:
            columns:
            - Capability
            - Gap Register Ref
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: authoring_scope
          intent: an empty required register asserts nothing
        - id: CRITICAL_WITHOUT_GAP_ENTRY
          check: CELL_NOT_EMPTY
          register: capability_graph
          params:
            column: Gap Register Entry
            only_when_column: Status
            only_when_value: CRITICAL
            detail: capability is CRITICAL but names no gap — work this change request must do has nowhere to
              be tracked
          intent: every capability that must be authored is a declared gap
        - id: GAP_ENTRY_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: capability_graph
          params:
            column: Gap Register Entry
            target_register: gap_register
            target_column: Gap Code
            only_when_column: Status
            only_when_value: CRITICAL
            detail: a consolidation may only point at what it consolidated
          intent: a capability points only at a gap the document itself declares
        - id: GAP_WITHOUT_OWNER
          check: CELL_NOT_EMPTY
          register: gap_register
          params:
            column: Owner Subdomain
            detail: gap names no owning subdomain — an unowned gap is nobody's work
          intent: every gap has a subdomain accountable for closing it
        - id: SCOPE_WITHOUT_GAP_REFERENCE
          check: CELL_NOT_EMPTY
          register: authoring_scope
          params:
            column: Gap Register Ref
            detail: in-scope capability references no gap — scope must trace to evidence
          intent: what this change request builds traces to a declared gap, not to intent
        - id: SCOPE_GAP_UNDECLARED
          check: CELL_RESOLVES_IN_REGISTER
          register: authoring_scope
          params:
            column: Gap Register Ref
            target_register: gap_register
            target_column: Gap Code
            detail: a consolidation may only point at what it consolidated
          intent: scope points only at a gap the document itself declares
        - id: DEPENDENCY_IDENTITY_UNRESOLVED
          check: CITED_ARTIFACTS_RESOLVE
          register: dependency_graph
          params:
            column: To
            pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
            observation: si.artifact.list
          intent: a dependency on an existing artifact must be one that really exists
        - id: DECISION_WITHOUT_RATIONALE
          check: CELL_NOT_EMPTY
          register: design_decisions
          params:
            column: Rationale
            detail: design decision states no rationale — a decision without a reason cannot be reviewed
          intent: a consolidated decision carries the reasoning that produced it
        - id: AUTHORING_DECISION_NOT_CONSOLIDATED
          check: PRIOR_ROWS_PRESENT_BY_KEY
          register: capability_graph
          params:
            prior_phase: p3
            prior_register: authoring_decisions
            prior_key_column: Capability
            key_column: Capability
          intent: a capability P3 decided and P4 never consolidated is dropped, not deferred
        - id: REGISTER_CELL_UNRESOLVED
          check: UNRESOLVED_MARKER_ABSENT
          params:
            exempt:
            - gap_register
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
