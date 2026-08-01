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

The rule set below carries that: a `ROW_WITHOUT_SOURCE_FINDING` and a `SOURCE_FINDING_MALFORMED`
rule for every table register, derived from the template so a register added later is traced
automatically rather than left as a hole where invention is silently permitted.

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
        rule_set:
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
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: CR Type
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: CR Type
          params:
            columns:
            - Classification
            - Rationale
            - Source Finding
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: CR Type
          intent: an empty required register asserts nothing
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
            - Source Finding
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
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Requested Outcomes
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Requested Outcomes
          params:
            columns:
            - Outcome
            - Source Finding
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Requested Outcomes
          intent: an empty required register asserts nothing
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
            - Fact
            - Certainty
            - Source Finding
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
            - Belief
            - Why It Matters
            - Verification Goal
            - Source Finding
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
            - Source Finding
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
            - Source Finding
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
            - Invariant
            - Source Finding
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
            - Source Finding
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
            - Source Finding
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
            - Source Finding
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
            - Source Finding
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
            - Source Finding
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
        - id: TABLE_MISSING
          check: TABLE_PRESENT
          register: Acceptance Criteria
          intent: a register must be readable as rows, not prose
        - id: TABLE_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: Acceptance Criteria
          params:
            columns:
            - Criterion
            - Source Finding
          intent: downstream phases read these columns by name
        - id: TABLE_EMPTY
          check: TABLE_HAS_ROWS
          register: Acceptance Criteria
          intent: an empty required register asserts nothing
        - id: SECTION_OUT_OF_ORDER
          check: SECTIONS_ASCENDING
          intent: section order is part of the template contract
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: CR Type
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: CR Type
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Business Vocabulary
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Business Vocabulary
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Requested Outcomes
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Requested Outcomes
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Known Facts
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Known Facts
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Existing-System Beliefs
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Existing-System Beliefs
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Assumptions
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Assumptions
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Constraints
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Constraints
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Business Invariants
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Business Invariants
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Lifecycle States
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Lifecycle States
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Business Events
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Business Events
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Authority Boundaries
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Authority Boundaries
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Out of Scope
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Out of Scope
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Governance Scope
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Governance Scope
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: Acceptance Criteria
          params:
            column: Source Finding
            detail: row cites no seed finding — P1 restates the seed, it does not add to it
          intent: an uncited row is content the phase invented
        - id: SOURCE_FINDING_MALFORMED
          check: CELL_MATCHES
          register: Acceptance Criteria
          params:
            column: Source Finding
            pattern: ^(CR seed §\d+|CR seed Subdomain Purpose|human decision)
            detail: '{value!r} does not name a seed register — cite ''CR seed §N …'', ''CR seed Subdomain Purpose'',
              or ''human decision'''
          intent: an unparseable citation is not traceability
        - id: HEADER_FIELD_MISSING
          check: HEADER_FIELD_PRESENT
          params:
            fields:
            - Domain
            - Primary subdomain
            - Secondary subdomain
            - CR version
          intent: the register must say which domain and subdomain it changes
        - id: HEADER_MALFORMED
          check: HEADER_FIELD_MATCHES
          params:
            fields:
            - Domain
            - Primary subdomain
            pattern: ^[a-z][a-z0-9_]*
          intent: domain and subdomain are identifiers, not prose
        - id: CLASSIFICATION_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: CR Type
          params:
            column: Classification
            vocabulary:
            - NEW_SUBDOMAIN
            - EXTEND_SUBDOMAIN
            - MODIFY
            - DEPRECATE
          intent: the classification is the decision P1 exists to record
        - id: CLASSIFICATION_WITHOUT_RATIONALE
          check: CELL_NOT_EMPTY
          register: CR Type
          params:
            column: Rationale
            detail: a classification with no rationale cannot be reviewed at the gate
          intent: the decision must be reviewable, not merely recorded
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
          intent: P2 consumes these goals directly; an empty one is an unverifiable belief
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
        - id: DESIGN_LEAKED_INTO_REGISTER
          check: TOKEN_ABSENT
          params:
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} is a compiled artifact identifier — design is assigned at P6b'
          intent: P1 classifies business content; it assigns no design
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
