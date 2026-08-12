# WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0

## Header (Mandatory)

- **Artifact Code:** WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## Generated Artifact

This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and
the copy is never corrected directly: where this artifact and its generator disagree, this
artifact is stale, and an edit here lasts until whoever next runs the emission.

- **Generator:** `transformation.design.emit:emit_rule_sets`
- **Generator sources** — one generator together, never separately:
  - `templates/p8_authoring_mandate_template_v0.md`
  - `transformation/design/p8_authoring_mandate/rules.py`

To change what this phase judges, amend a source and invoke the generator.
`tc phase emit --check` refuses a build in which the two disagree.

---

## 1. Intent

Phase 8 of the change pipeline: decide whether an offered Authoring Mandate is admissible.

P8 is the last dossier phase and the least creative one, deliberately. It adds nothing and drops
nothing — it orders what Stage 7 assigned into the sequence a builder can follow. "Mandate" is
exact: this is not one possible plan but the only ordering the dependency graph admits. **Gate 2
closes here**, freezing scope; after it a departure is a recorded deviation, never a silent change.

---

## 2. The only phase judged on row order

Every rule before this one judges rows independently: a register is a set of claims, each true or
false on its own. A mandate is not. It can consist entirely of well-formed rows and still be wrong.

- A **gap** in the step sequence is an artifact silently dropped between two steps that both look
  correct. Nothing reading one row at a time sees an absence.
- A dependency scheduled **after** the step that needs it makes the mandate unexecutable, and the
  defect exists in neither row alone — only in their relationship.

Those two properties are what separate a topological sort from a list, so they are what this phase
checks. It also grounds, for Stage 7's reason: an artifact mandated for authoring must not already
be in the composition.

---

## 3. "It adds nothing and drops nothing" is now checked

That sentence has stated P8's whole contract since the phase was built, and until now nothing
enforced it. Both halves fail silently in a mandate that passes every rule above:

- An artifact P7 declared and P8 never schedules is **not** deferred. Deferral is recorded; this is
  loss, and the step sequence stays contiguous over the hole because the artifact was never a step.
- An identity P8 schedules that P7 never assigned is a design decision taken by whoever typed the
  row, downstream of the gate that exists to approve design.

Neither is visible in either document. So this workflow takes `prior_texts` and reconciles the two
registers as sets of identities — which needs no citation idiom at all, because an identity is
exact.

---

## Machine

```yaml
fqdn: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Authoring Mandate is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_AUTHORING_MANDATE_SUBMITTED_V0

  nodes:
    IN_AUTHORING_MANDATE_SUBMITTED_V0:
      type: IN
      code: IN_AUTHORING_MANDATE_SUBMITTED_V0
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
          register: build_order
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: build_order
          params:
            columns:
            - Wave
            - Step
            - Code
            - Action
            - Subdomain
            - Depends On
          intent: downstream phases read these columns by name
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: build_order
          params:
            column: Action
            vocabulary:
            - REPLACE
            - EXTEND
            - NEW
          intent: Action is a controlled vocabulary declared by the template
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: critical_path
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: critical_path
          params:
            columns:
            - Position
            - Code
          intent: downstream phases read these columns by name
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: mandate_artifact_summary
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: mandate_artifact_summary
          params:
            columns:
            - Action
            - Count
            - Description
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: mandate_artifact_summary
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: mandate_artifact_summary
          params:
            column: Action
            vocabulary:
            - REPLACE
            - EXTEND
            - NEW
          intent: Action is a controlled vocabulary declared by the template
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: field_declarations
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: field_declarations
          params:
            columns:
            - Code
            - Subdomain Field
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: field_declarations
          intent: an empty required register asserts nothing
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: new_capabilities
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: new_capabilities
          params:
            columns:
            - Code
            - Purpose
            - Inputs
            - Outputs
          intent: downstream phases read these columns by name
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: new_intents
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: new_intents
          params:
            columns:
            - Code
            - Purpose
            - Workflow
            - Inputs
          intent: downstream phases read these columns by name
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: cross_subdomain_notes
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: cross_subdomain_notes
          params:
            columns:
            - Code
            - Note
          intent: downstream phases read these columns by name
        - id: BUILD_STEPS_NOT_CONTIGUOUS
          check: COLUMN_SEQUENCE_CONTIGUOUS
          register: build_order
          params:
            column: Step
            start: 1
          intent: the build sequence is total and gapless, because a gap is a dropped artifact
        - id: DEPENDENCY_SCHEDULED_LATER
          check: DEPENDENCY_PRECEDES
          register: build_order
          params:
            column: Code
            depends_column: Depends On
            order_column: Step
          intent: everything a step depends on is built before it — this is what makes it a sort
        - id: BUILD_CODE_MALFORMED
          check: CELL_MATCHES
          register: build_order
          params:
            column: Code
            pattern: ^[a-z][a-z0-9_.]*::(?:STRUCTURE|VOCAB|AC|IN|WF|CC|CT|CS|RB|EV|TI|TE)_[A-Z0-9_]+_V\d+$
            detail: build code {value!r} must be a binding FQDN copied verbatim from Stage 7
          intent: a mandate orders binding identities, never re-typed approximations
        - id: BUILD_CODE_ALREADY_EXISTS
          check: CITED_ARTIFACTS_ABSENT
          register: build_order
          params:
            column: Code
            pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
            observation: si.artifact.list
          intent: an artifact mandated for authoring must not already be in the composition
        - id: CRITICAL_PATH_NOT_IN_BUILD_ORDER
          check: CELL_RESOLVES_IN_REGISTER
          register: critical_path
          params:
            column: Code
            target_register: build_order
            target_column: Code
            detail: the critical path runs through steps the mandate schedules, not past them
          intent: the critical path is a path through this build order
        - id: CRITICAL_PATH_NOT_CONTIGUOUS
          check: COLUMN_SEQUENCE_CONTIGUOUS
          register: critical_path
          params:
            column: Position
            start: 1
          intent: a path is an ordered chain, not an unordered set of steps
        - id: CAPABILITY_WITHOUT_PURPOSE
          check: CELL_NOT_EMPTY
          register: new_capabilities
          params:
            column: Purpose
            detail: capability states no purpose — a builder needs to know what to build, not only its name
          intent: a mandated capability says what it is for
        - id: INTENT_WITHOUT_WORKFLOW
          check: CELL_NOT_EMPTY
          register: new_intents
          params:
            column: Workflow
            detail: intent names no workflow — an entry point that starts nothing cannot be authored
          intent: every mandated intent names the workflow it starts
        - id: DESIGNED_ARTIFACT_NOT_SCHEDULED
          check: PRIOR_IDENTITIES_COVERED
          register: build_order
          params:
            prior_phase: p7
            prior_register: new_artifacts
            prior_column: Code
            column: Code
            require: prior_in_here
          intent: an artifact the design declared and the mandate never schedules is not deferred, it is lost
        - id: SCHEDULED_ARTIFACT_NOT_DESIGNED
          check: PRIOR_IDENTITIES_COVERED
          register: build_order
          params:
            prior_phase: p7
            prior_register: new_artifacts
            prior_column: Code
            column: Code
            require: here_in_prior
          intent: a mandate orders the build; it does not get to add to it
        - id: SCHEDULED_ARTIFACT_UNPLACED
          check: REGISTER_COVERS_REGISTER
          register: field_declarations
          params:
            source_register: build_order
            source_column: Code
            column: Code
          intent: every artifact the mandate schedules declares the subdomain it is built into
        - id: AMENDED_ARTIFACT_UNPLACED
          check: PRIOR_IDENTITIES_COVERED
          register: field_declarations
          params:
            prior_phase: p7
            prior_register: existing_inventory
            prior_column: FQDN
            column: Code
            require: prior_in_here
            match_on: bare_code
            prior_only_when_column: Action
            prior_only_when_values:
            - EXTEND
            - REPLACE
            prior_only_when_prefixes:
            - WF_
            - CC_
            - EV_
            - RB_
          intent: an artifact this change amends declares the subdomain it is placed in, as a scheduled one does
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

    EXIT_REJECTED:
      type: EXIT
```
