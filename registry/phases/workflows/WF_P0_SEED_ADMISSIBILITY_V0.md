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
subdomain: phases
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
        rule_set:
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Subdomain Purpose
          intent: every declared register must be present
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: CR Type
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: CR Type
          params:
            number: 1
          intent: registers are referenced by number downstream
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Business Vocabulary
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Business Vocabulary
          params:
            number: 2
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Business Vocabulary
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Business Vocabulary
          params:
            columns:
            - Term
            - Definition
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Business Vocabulary
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Requested Outcomes
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Requested Outcomes
          params:
            number: 3
          intent: registers are referenced by number downstream
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Known Facts
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Known Facts
          params:
            number: 4
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Known Facts
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Known Facts
          params:
            columns:
            - '#'
            - Fact
            - Certainty
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Known Facts
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Existing-System Beliefs
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Existing-System Beliefs
          params:
            number: 5
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Existing-System Beliefs
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Existing-System Beliefs
          params:
            columns:
            - '#'
            - Belief
            - Why it matters
            - Verification Goal
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Existing-System Beliefs
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Assumptions
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Assumptions
          params:
            number: 6
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Assumptions
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Assumptions
          params:
            columns:
            - Assumption
            - Basis
          intent: downstream phases read these columns by name
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Constraints
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Constraints
          params:
            number: 7
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Constraints
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Constraints
          params:
            columns:
            - Constraint
            - Source
          intent: downstream phases read these columns by name
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Business Invariants
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Business Invariants
          params:
            number: 8
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Business Invariants
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Business Invariants
          params:
            columns:
            - '#'
            - Invariant
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Business Invariants
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Lifecycle States
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Lifecycle States
          params:
            number: 9
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Lifecycle States
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Lifecycle States
          params:
            columns:
            - Object
            - State
            - Meaning
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Lifecycle States
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Business Events
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Business Events
          params:
            number: 10
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Business Events
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Business Events
          params:
            columns:
            - Event
            - When It Occurs
            - Significance
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Business Events
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Authority Boundaries
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Authority Boundaries
          params:
            number: 11
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Authority Boundaries
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Authority Boundaries
          params:
            columns:
            - Business Object
            - Authoritative Owner
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Authority Boundaries
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Out of Scope
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Out of Scope
          params:
            number: 12
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Out of Scope
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Out of Scope
          params:
            columns:
            - Item
            - Reason
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Out of Scope
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Governance Scope
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Governance Scope
          params:
            number: 13
          intent: registers are referenced by number downstream
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Governance Scope
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Governance Scope
          params:
            columns:
            - Scope Item
            - Relationship
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Governance Scope
          intent: an empty required register asserts nothing
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Clarification Requests
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Clarification Requests
          params:
            number: 14
          intent: registers are referenced by number downstream
        - id: SECTION_MISSING
          check: SECTION_PRESENT
          register: Acceptance Criteria
          intent: every declared register must be present
        - id: SECTION_MISNUMBERED
          check: SECTION_NUMBERED
          register: Acceptance Criteria
          params:
            number: 15
          intent: registers are referenced by number downstream
        - id: SECTION_OUT_OF_ORDER
          check: SECTIONS_ASCENDING
          intent: section order is part of the template contract
        - id: HEADER_FIELD_MISSING
          check: HEADER_FIELD_PRESENT
          params:
            fields:
            - Domain
            - Primary subdomain
            - Secondary subdomain
            - CR version
          intent: the seed must say which domain and subdomain it changes
        - id: HEADER_MALFORMED
          check: HEADER_FIELD_MATCHES
          params:
            fields:
            - Domain
            - Primary subdomain
            pattern: ^[a-z][a-z0-9_]*
          intent: domain and subdomain are identifiers, not prose
        - id: CR_TYPE_NOT_DECLARED
          check: SECTION_DECLARES_ONE_OF
          register: CR Type
          params:
            vocabulary:
            - NEW_SUBDOMAIN
            - EXTEND_SUBDOMAIN
            - MODIFY
            - DEPRECATE
          intent: exactly one CR type; the transformation is one kind of change or another
        - id: CERTAINTY_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: Known Facts
          params:
            column: Certainty
            vocabulary:
            - HIGH
            - MEDIUM
            - LOW
          intent: a business truth carries a rated certainty
        - id: FACT_EMPTY
          check: CELL_NOT_EMPTY
          register: Known Facts
          params:
            column: Fact
            detail: Fact is empty
          intent: a rated row with no claim is not a fact
        - id: BELIEF_CARRIES_CERTAINTY
          check: COLUMN_ABSENT
          register: Existing-System Beliefs
          params:
            column: Certainty
            detail: beliefs must not carry a Certainty column — that would make them facts
          intent: the truth/belief split is what P2 verification depends on
        - id: BELIEF_WITHOUT_VERIFICATION_GOAL
          check: CELL_NOT_EMPTY
          register: Existing-System Beliefs
          params:
            column: Verification Goal
            detail: every belief must state what P2 has to establish
          intent: an unverifiable belief silently becomes an assumption
        - id: BELIEF_WITHOUT_RATIONALE
          check: CELL_NOT_EMPTY
          register: Existing-System Beliefs
          params:
            column: Why it matters
            detail: every belief must scope why it matters to this CR
          intent: an unscoped belief cannot be closed
        - id: BELIEF_STATED_AS_FACT
          check: CELL_NOT_PREFIXED
          register: Existing-System Beliefs
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
        - id: SCOPE_RELATIONSHIP_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: Governance Scope
          params:
            column: Relationship
            vocabulary:
            - CREATED
            - EXTENDED
            - MODIFIED
            - DEPRECATED
            - ADJACENT
          intent: governance relationships are a controlled vocabulary
        - id: DESIGN_LEAKED_INTO_SEED
          check: TOKEN_ABSENT
          params:
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} is a compiled artifact identifier — P0 must not assign design'
          intent: P0 rewrites business prose; design is assigned at P6b
        - id: CLARIFICATIONS_UNSTATED
          check: SECTION_HAS_TEXT
          register: Clarification Requests
          params:
            detail: state the open questions or '(none)' — an empty section asserts nothing
          intent: silence is not the same as 'no open questions'
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
