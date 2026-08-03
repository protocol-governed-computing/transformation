# WF_P0_SEED_ADMISSIBILITY_V0

## Header (Mandatory)

- **Artifact Code:** WF_P0_SEED_ADMISSIBILITY_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Phase 0 of the change pipeline: decide whether an offered seed is admissible.

The workflow composes one reused governed call — judge a document — and carries the **rule set
itself** as declared node input. That is the point of this artifact. The rules deciding
admissibility are compiled, sealed, versioned and readable from the composition through ordinary
artifact inspection; they are not configuration, not code, and not editable outside a governed
change.

The mechanisms hold no policy. Reading the evaluator tells you how a check runs. Reading this
workflow tells you what is governed. Later phases reuse the same mechanisms and declare their own
rule sets here, in their own workflow.

---

## 2. Verdict, not exception

`INADMISSIBLE` is a normal outcome. A seed that fails the rule set has been correctly judged, not
incorrectly executed. `VIOLATION` is reserved for a rule naming a check kind the evaluator does not
implement — a defect in the rule set, not in the seed.

---

## Machine

```yaml
fqdn: transformation::WF_P0_SEED_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered seed is admissible
  actor_context: transformation::AC_SEED_AUTHOR_V0

  start_node: IN_SEED_SUBMITTED_V0

  nodes:
    IN_SEED_SUBMITTED_V0:
      type: IN
      code: IN_SEED_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_DOCUMENT_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_DOCUMENT_V0:
      type: CC
      code: CC_JUDGE_DOCUMENT_V0
      inputs:
        document_text: $.payload.seed_text
        # P0's input is human prose, not a phase document — there is no upstream register.
        prior_texts: {}
        rule_set:
        - id: REGISTER_EMPTY
          check: SECTION_HAS_TEXT
          register: subdomain_purpose
          params:
            detail: narrative register is empty — it states nothing
          intent: a narrative register carries the context nothing downstream can rederive
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
          intent: downstream phases read these columns by name
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
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: out_of_scope
          intent: an empty required register asserts nothing
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
            - EXTENDED
            - MODIFIED
            - DEPRECATED
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
        - id: BELIEF_CARRIES_CERTAINTY
          check: COLUMN_ABSENT
          register: system_beliefs
          params:
            column: Certainty
            detail: beliefs must not carry a Certainty column — that would make them facts
          intent: the truth/belief split is what P2 verification depends on
        - id: BELIEF_WITHOUT_VERIFICATION_GOAL
          check: CELL_NOT_EMPTY
          register: system_beliefs
          params:
            column: Verification Goal
            detail: every belief must state what P2 has to establish
          intent: an unverifiable belief silently becomes an assumption
        - id: BELIEF_STATED_AS_FACT
          check: CELL_NOT_PREFIXED
          register: system_beliefs
          params:
            column: Belief
            prefixes:
            - 'there is '
            - 'there are '
            - 'the system provides '
            - 'the system has '
            - 'it is confirmed '
            - 'confirmed: '
            detail: belief is asserted, not suspected ({prefix!r}) — state it as a belief or move it to Known
              Facts
          intent: P0 must not promote a System Belief to a Known Fact
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
