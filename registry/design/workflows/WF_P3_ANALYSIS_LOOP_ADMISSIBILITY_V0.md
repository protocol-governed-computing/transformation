# WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0

## Header (Mandatory)

- **Artifact Code:** WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Phase 3 of the change pipeline: decide whether an offered Analysis Loop register is admissible.

P3 is the first phase that **decides**. P0 reorganizes, P1 classifies, P2 discovers; P3 resolves
the extend-vs-new question P2 deferred and commits every capability to REUSE, EXTEND or
AUTHOR_NEW.

---

## 2. Why this workflow observes twice

P2 asks whether a cited identity exists, and the artifact list answers it. A phase that decides
asks a further question — may this artifact be offered to this change request at all — and that is
a property of the domain that owns it, declared by that domain.

So this workflow composes `CC_JUDGE_AGAINST_COMPOSITION_V0`: the artifact list resolves identities,
the composition summary carries each domain's declared reuse visibility, and the two answer
different questions. A domain declaring no visibility is a hard failure, not a permissive default —
absence would otherwise mean "search everything", which is the inference the declaration exists to
prevent.

**The declaration bounds the search space; it never makes the decision.** Which artifacts are
reused, extended or newly authored stays with the author, per artifact, against evidence.

---

## 3. Why it also reads P2

P3's verification pass exists to re-ground every prior result against the composition rather than
inherit it. Whether it actually covered them is not a property of this register: a pass over two of
P2's three belief results reads as complete, and the third was inherited silently.

So this workflow takes `prior_texts` and is judged against P2 as well as against the composition. A
result nobody re-verified is a finding, and so is one re-verified under a claim P2 never made — the
citation would otherwise lend a substitution provenance it does not have.

---

## Machine

```yaml
fqdn: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Analysis Loop register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_ANALYSIS_LOOP_SUBMITTED_V0

  nodes:
    IN_ANALYSIS_LOOP_SUBMITTED_V0:
      type: IN
      code: IN_ANALYSIS_LOOP_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_AGAINST_COMPOSITION_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_AGAINST_COMPOSITION_V0:
      type: CC
      code: CC_JUDGE_AGAINST_COMPOSITION_V0
      inputs:
        document_text: $.payload.register_text
        prior_texts: $.payload.prior_texts
        rule_set:
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: analysis_findings
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: analysis_findings
          params:
            columns:
            - Question Id
            - Finding
            - Impact
            - Evidence Status
            - Confidence
            - Resolution Status
            - Evidence
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: analysis_findings
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: analysis_findings
          params:
            column: Evidence Status
            vocabulary:
            - OBSERVED
            - INFERRED
            - OPEN
          intent: Evidence Status is a controlled vocabulary declared by the template
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: analysis_findings
          params:
            column: Confidence
            vocabulary:
            - HIGH
            - MEDIUM
            - LOW
          intent: Confidence is a controlled vocabulary declared by the template
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: analysis_findings
          params:
            column: Resolution Status
            vocabulary:
            - CLOSED
            - OPEN
          intent: Resolution Status is a controlled vocabulary declared by the template
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: verification_results
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: verification_results
          params:
            columns:
            - Item
            - Origin
            - Result
            - Evidence
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: verification_results
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: verification_results
          params:
            column: Result
            vocabulary:
            - CONFIRMED
            - OVERTURNED
          intent: Result is a controlled vocabulary declared by the template
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: dependency_discoveries
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: dependency_discoveries
          params:
            columns:
            - Dependency
            - Type
            - Disposition
            - Evidence
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: dependency_discoveries
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: dependency_discoveries
          params:
            column: Disposition
            vocabulary:
            - EXISTING
            - REUSE
            - AUTHOR_NEW
            - INVESTIGATE
          intent: Disposition is a controlled vocabulary declared by the template
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: impact_analysis
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: impact_analysis
          params:
            columns:
            - Artifact
            - Impact Scope
            - Consumer Count
            - Evidence
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: impact_analysis
          intent: an empty required register asserts nothing
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: authoring_decisions
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: authoring_decisions
          params:
            columns:
            - Capability
            - Decision
            - Rationale
            - Alternatives Checked
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: authoring_decisions
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: authoring_decisions
          params:
            column: Decision
            vocabulary:
            - REUSE
            - EXTEND
            - AUTHOR_NEW
          intent: Decision is a controlled vocabulary declared by the template
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: authoring_decisions
          params:
            columns:
            - capability
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: authoring_decisions
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: authoring_decisions
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
            - transport_bindings
            - verification_results
            - vocabulary_extensions
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: CITATION_ORDINAL_UNRESOLVED
          check: CITED_ORDINAL_RESOLVES
          register: authoring_decisions
          params:
            column: Source Finding
          intent: an ordinal past the end of a register cites a finding that is not there
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: placement_decision
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: placement_decision
          params:
            columns:
            - Decision
            - Subdomain
            - Rationale
            - Source Finding
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: placement_decision
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: placement_decision
          params:
            column: Decision
            vocabulary:
            - NEW_SUBDOMAIN
            - EXTEND
          intent: Decision is a controlled vocabulary declared by the template
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: placement_decision
          params:
            columns:
            - subdomain
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: ROW_WITHOUT_SOURCE_FINDING
          check: CELL_NOT_EMPTY
          register: placement_decision
          params:
            column: Source Finding
            detail: row cites no earlier finding — a phase restates its input, it does not add to it
          intent: an uncited row has no provenance in the dossier
        - id: SOURCE_FINDING_UNRESOLVED
          check: SOURCE_FINDING_RESOLVES
          register: placement_decision
          params:
            column: Source Finding
            known_registers: *id001
            literal_sources:
            - CR seed
            - human decision
            - projection
            - S1 seed
          intent: a citation must name something this phase can actually cite
        - id: CITATION_ORDINAL_UNRESOLVED
          check: CITED_ORDINAL_RESOLVES
          register: placement_decision
          params:
            column: Source Finding
          intent: an ordinal past the end of a register cites a finding that is not there
        - id: REGISTER_MISSING
          check: TABLE_PRESENT
          register: saturation
          intent: a declared register must be present and readable as rows
        - id: REGISTER_COLUMN_MISSING
          check: TABLE_HAS_COLUMNS
          register: saturation
          params:
            columns:
            - Criterion
            - Status
            - Evidence
          intent: downstream phases read these columns by name
        - id: REGISTER_EMPTY
          check: TABLE_HAS_ROWS
          register: saturation
          intent: an empty required register asserts nothing
        - id: CELL_NOT_IN_VOCABULARY
          check: CELL_IN_VOCABULARY
          register: saturation
          params:
            column: Status
            vocabulary:
            - SATISFIED
            - NOT_SATISFIED
          intent: Status is a controlled vocabulary declared by the template
        - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
          check: CELL_TOKEN_ABSENT
          register: saturation
          params:
            columns:
            - criterion
            pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
            detail: '{token!r} appears in business-language column {column!r} — this register states business
              meaning, not design'
          intent: business registers name no compiled artifact
        - id: REUSE_CANDIDATE_NOT_ELIGIBLE
          check: REUSE_CANDIDATE_ELIGIBLE
          register: authoring_decisions
          params:
            column: Alternatives Checked
            pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
            observation: si.snapshot.summary
            artifact_observation: si.artifact.list
            eligible:
            - substrate
            - business
          intent: a change request may only be offered candidates from a domain that permits reuse
        - id: DECISION_WITHOUT_ALTERNATIVES
          check: CELL_NOT_EMPTY
          register: authoring_decisions
          params:
            column: Alternatives Checked
            detail: decision records no alternatives examined — 'I searched and found nothing' is credible only
              with the search shown
          intent: a committed decision shows the search that produced it
        - id: DECISION_WITHOUT_RATIONALE
          check: CELL_NOT_EMPTY
          register: authoring_decisions
          params:
            column: Rationale
            detail: decision states no rationale — a classification without a reason is an assertion
          intent: every decision traces to a grounded reason
        - id: CITED_ALTERNATIVE_UNRESOLVED
          check: CITED_ARTIFACTS_RESOLVE
          register: authoring_decisions
          params:
            column: Alternatives Checked
            pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
            observation: si.artifact.list
          intent: an alternative examined must be one that really exists
        - id: IMPACT_WITHOUT_EVIDENCE
          check: CELL_NOT_EMPTY
          register: impact_analysis
          params:
            column: Evidence
            detail: impact row carries no evidence — consumer counts are observed, never estimated
          intent: impact is mechanically captured, never summarised from memory
        - id: VERIFICATION_WITHOUT_EVIDENCE
          check: CELL_NOT_EMPTY
          register: verification_results
          params:
            column: Evidence
            detail: verification records no evidence — grounding is not inherited, so a re-check that cites nothing
              did not happen
          intent: an overturned answer is marked with what overturned it, never erased
        - id: SATURATION_CRITERIA_INCOMPLETE
          check: TABLE_HAS_ROWS
          register: saturation
          params:
            minimum: 5
          intent: analysis is saturated only against every declared criterion; a claim resting on fewer is the
            gap the criteria exist to close
        - id: SATURATION_CLAIMED_WITHOUT_EVIDENCE
          check: CELL_NOT_EMPTY
          register: saturation
          params:
            column: Evidence
            detail: criterion is asserted satisfied with nothing to show for it
          intent: saturation is demonstrated, not declared
        - id: BELIEF_RESULT_NOT_REVERIFIED
          check: PRIOR_ROWS_CITED
          register: verification_results
          params:
            prior_phase: p2
            prior_register: belief_verification
            prior_key_column: Belief
            citation_column: Origin
          intent: a result nobody re-verified was inherited, and grounding is not inherited
        - id: BELIEF_RESULT_RESTATED_FROM_P2
          check: PRIOR_ROW_MATCHES_CITED
          register: verification_results
          params:
            prior_phase: p2
            prior_register: belief_verification
            prior_key_column: Belief
            key_column: Item
            citation_column: Origin
          intent: a re-verification must address the result it cites, not a substitute for it
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
