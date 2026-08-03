# WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0

## Header (Mandatory)

- **Artifact Code:** WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Phase 1 of the change pipeline: decide whether an offered Change Request register is admissible.

This workflow **authors no new mechanism**. It composes the same governed call P0 uses — judge a
document against a declared rule set — and differs only in the rule set it carries. That is the
generalization the pipeline was designed for: phases share mechanisms and differ in declared data.

---

## 2. What P1 adds over P0

P0 governs a seed, where business content enters. P1 governs the register that restates it, so P1
can check something P0 cannot: **traceability**. Every row must cite the seed finding it came from,
in a parseable form. An uncited row is content the phase invented, which is precisely what P1 must
not do.

The rule set below is **derived from the vendored template**
(`templates/p1_change_request_template_v0.md`), which declares the fifteen registers, their columns,
their inline controlled vocabularies, which may be empty, and which hold business language. Only the
document header — which belongs to no register — is declared by hand.

Traceability follows from the template too: every register carrying a `Source Finding` column gets a
`ROW_WITHOUT_SOURCE_FINDING` and a `SOURCE_FINDING_MALFORMED` rule, so a register added later is
traced automatically rather than left as a hole where invention is silently permitted.

---

## Machine

```yaml
fqdn: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: phases
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Change Request register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_CHANGE_REQUEST_SUBMITTED_V0

  nodes:
    IN_CHANGE_REQUEST_SUBMITTED_V0:
      type: IN
      code: IN_CHANGE_REQUEST_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_DOCUMENT_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_DOCUMENT_V0:
      type: CC
      code: CC_JUDGE_DOCUMENT_V0
      inputs:
        document_text: $.payload.register_text
        prior_texts: $.payload.prior_texts
        rule_set:
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: cr_type
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: cr_type
          params:
            columns:
            - Classification
            - Rationale
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: cr_type
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: cr_type
          params:
            column: Classification
            vocabulary:
            - NEW_SUBDOMAIN
            - EXTEND_SUBDOMAIN
            - MODIFY
            - DEPRECATE
          intent: Classification is a controlled vocabulary declared by the template
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: cr_type
          params:
            columns:
            - Classification
            - Rationale
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: cr_type
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: cr_type
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
            - identity_semantics
            - impact_analysis
            - implementation_bindings
            - interface_fields
            - invariants
            - known_facts
            - lifecycle_states
            - mandate_artifact_summary
            - new_artifacts
            - new_capabilities
            - new_intents
            - open_questions
            - out_of_scope
            - ownership
            - placement_decision
            - pps_artifacts_requiring_action
            - pps_baseline_fqdns
            - process_steps
            - provisional_codes
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
          register: business_vocabulary
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: business_vocabulary
          params:
            columns:
            - Term
            - Definition
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: business_vocabulary
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: business_vocabulary
          params:
            columns:
            - Term
            - Definition
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: business_vocabulary
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: business_vocabulary
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
          register: requested_outcomes
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: requested_outcomes
          params:
            columns:
            - Outcome
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: requested_outcomes
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: requested_outcomes
          params:
            columns:
            - Outcome
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: requested_outcomes
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: requested_outcomes
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
          register: known_facts
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: known_facts
          params:
            columns:
            - Fact
            - Certainty
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: known_facts
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: known_facts
          params:
            column: Certainty
            vocabulary:
            - HIGH
            - MEDIUM
            - LOW
          intent: Certainty is a controlled vocabulary declared by the template
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: known_facts
          params:
            columns:
            - Fact
            - Certainty
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: known_facts
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: known_facts
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
          register: system_beliefs
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: system_beliefs
          params:
            columns:
            - Belief
            - Why It Matters
            - Verification Goal
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: system_beliefs
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: system_beliefs
          params:
            columns:
            - Belief
            - Why It Matters
            - Verification Goal
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: system_beliefs
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: system_beliefs
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
          register: assumptions
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: assumptions
          params:
            columns:
            - Assumption
            - Basis
            - Source Finding
          intent: downstream phases read these columns by name
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: assumptions
          params:
            columns:
            - Assumption
            - Basis
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: assumptions
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: assumptions
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
          register: constraints
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: constraints
          params:
            columns:
            - Constraint
            - Source
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: constraints
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: constraints
          params:
            columns:
            - Constraint
            - Source
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: constraints
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: constraints
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
          register: business_invariants
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: business_invariants
          params:
            columns:
            - Invariant
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: business_invariants
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: business_invariants
          params:
            columns:
            - Invariant
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: business_invariants
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: business_invariants
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
          register: lifecycle_states
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: lifecycle_states
          params:
            columns:
            - Object
            - State
            - Meaning
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: lifecycle_states
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: lifecycle_states
          params:
            columns:
            - Object
            - State
            - Meaning
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: lifecycle_states
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: lifecycle_states
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
          register: business_events
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: business_events
          params:
            columns:
            - Event
            - When It Occurs
            - Significance
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: business_events
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: business_events
          params:
            columns:
            - Event
            - When It Occurs
            - Significance
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: business_events
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: business_events
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
          register: authority_boundaries
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: authority_boundaries
          params:
            columns:
            - Business Object
            - Authoritative Owner
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: authority_boundaries
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: authority_boundaries
          params:
            columns:
            - Business Object
            - Authoritative Owner
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: authority_boundaries
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: authority_boundaries
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
          register: out_of_scope
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: out_of_scope
          params:
            columns:
            - Item
            - Reason
            - Source Finding
          intent: downstream phases read these columns by name
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: out_of_scope
          params:
            columns:
            - Item
            - Reason
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: out_of_scope
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: out_of_scope
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
          register: governance_scope
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: governance_scope
          params:
            columns:
            - Scope Item
            - Relationship
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: governance_scope
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: governance_scope
          params:
            column: Relationship
            vocabulary:
            - CREATED
            - ADJACENT
          intent: Relationship is a controlled vocabulary declared by the template
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: governance_scope
          params:
            columns:
            - Scope Item
            - Relationship
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: governance_scope
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: governance_scope
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
          register: clarification_requests
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: clarification_requests
          params:
            columns:
            - Question
            - Why Needed
            - Blocking
            - Owner
            - Source Finding
          intent: downstream phases read these columns by name
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: clarification_requests
          params:
            column: Blocking
            vocabulary:
            - 'YES'
            - 'NO'
          intent: Blocking is a controlled vocabulary declared by the template
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: clarification_requests
          params:
            column: Owner
            vocabulary:
            - HUMAN
            - SNAPSHOT
            - GOVERNANCE
          intent: Owner is a controlled vocabulary declared by the template
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: clarification_requests
          params:
            columns:
            - Question
            - Why Needed
            - Blocking
            - Owner
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: clarification_requests
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: clarification_requests
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
          register: acceptance_criteria
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: acceptance_criteria
          params:
            columns:
            - Criterion
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: acceptance_criteria
          intent: an empty required register asserts nothing
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: acceptance_criteria
          params:
            columns:
            - Criterion
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: acceptance_criteria
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: acceptance_criteria
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: SEED_ROW_NOT_CARRIED
          check: PRIOR_ROWS_PRESENT_BY_KEY
          register: system_beliefs
          params:
            prior_phase: p0
            prior_register: system_beliefs
            prior_key_column: Belief
            key_column: Belief
          intent: P0 reorganizes and P1 restates; neither may drop what the business said
        - id: SEED_ROW_NOT_CARRIED
          check: PRIOR_ROWS_PRESENT_BY_KEY
          register: requested_outcomes
          params:
            prior_phase: p0
            prior_register: requested_outcomes
            prior_key_column: Outcome
            key_column: Outcome
          intent: P0 reorganizes and P1 restates; neither may drop what the business said
        - id: SEED_ROW_NOT_CARRIED
          check: PRIOR_ROWS_PRESENT_BY_KEY
          register: business_invariants
          params:
            prior_phase: p0
            prior_register: business_invariants
            prior_key_column: Invariant
            key_column: Invariant
          intent: P0 reorganizes and P1 restates; neither may drop what the business said
        - id: SEED_ROW_NOT_CARRIED
          check: PRIOR_ROWS_PRESENT_BY_KEY
          register: acceptance_criteria
          params:
            prior_phase: p0
            prior_register: acceptance_criteria
            prior_key_column: Criterion
            key_column: Criterion
          intent: P0 reorganizes and P1 restates; neither may drop what the business said
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

    EXIT_JUDGED:
      type: EXIT
      status: SUCCESS

    EXIT_REJECTED:
      type: EXIT
      status: VIOLATION
```
