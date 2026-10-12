# Business Intent — transformation / design, build

## Machine

```yaml
document:
  phase: p5
  domain: transformation
  subdomain:
  - design
  - build
  cr: genesis
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The transformation domain governs how a composition is allowed to change. Its design subdomain
    judges each document of a change, phase by phase, against rules declared for that phase and
    readable from the composition, and reports every rule a document fails, where, and why the rule
    exists. Its build subdomain builds an approved mandate into exactly the artifacts it schedules and
    reports how much of each the design determined. The domain owns the pipeline: what each phase
    consumes and produces, which rules decide admissibility, and who is accountable at each gate. It
    holds no records of its own: every document is supplied whole with the request that judges it.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: REFINED
    refinement: States that the domain holds no records of its own, which the domain model established — every document arrives whole with its request. The seed states what the domain is for; this addition does not contradict it.
  subdomain_purposes:
  - subdomain: design
    purpose: Judges each document of a change against the rules declared for its phase, and reports every failure, where, and why the rule exists.
    source_finding: {phase: p1, register: cr_type, row: 1}
  - subdomain: build
    purpose: Builds an approved mandate into exactly the artifacts it schedules, and reports how much of each the design determined.
    source_finding: {phase: p1, register: cr_type, row: 2}
  scope_boundary:
  - capability: Read a phase document into its registers
    status: IN_SCOPE
    notes: Adds and decides nothing
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Read the earlier phase documents a phase must agree with
    status: IN_SCOPE
    notes: All at once, since a composition has no iteration
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Apply every rule of a phase and report each failure
    status: IN_SCOPE
    notes: Never stops at the first failure
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Judge a phase document, with and without the composition and earlier documents
    status: IN_SCOPE
    notes: One composition per kind of grounding
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: The nine phases, each with its rules and its entry point
    status: IN_SCOPE
    notes: Each phase carries its own rules
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Render, measure and attribute the artifacts a mandate schedules
    status: IN_SCOPE
    notes: Pure
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Build an approved mandate
    status: IN_SCOPE
    notes: Writes only beneath a declared root
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: The author of record and the reviewer
    status: IN_SCOPE
    notes: Accountability at every gate
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Workers that draft documents
    status: DEFERRED
    notes: Excluded by the problem statement
    source_finding: {phase: p1, register: out_of_scope, row: 1}
  - capability: A governed step that generates documents
    status: DEFERRED
    notes: Excluded by the problem statement
    source_finding: {phase: p1, register: out_of_scope, row: 3}
  business_objects: []
  identity_semantics: []
  invariants:
  - invariant: Every phase is judged only by rules declared for it
    business_reason: Rules readable from the composition is the outcome the change exists for; a rule held anywhere else is one nobody can read
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: A verdict reports every failed rule
    business_reason: An author needs the whole finding set to revise once, and a rule that stops running cannot be trusted
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: The same document and the same rules give the same verdict
    business_reason: A verdict is evidence only if it can be reproduced from what was judged
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: Every rule states why it exists
    business_reason: A finding without its reason tells the author what failed but not what to preserve when fixing it
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - invariant: Nothing is built that a person did not approve
    business_reason: People are accountable at the gates, and construction is downstream of every gate
    source_finding: {phase: p1, register: business_invariants, row: 5}
  - invariant: A built artifact holds only what the design or a governing artifact determined
    business_reason: A value construction invented is design nobody approved
    source_finding: {phase: p1, register: business_invariants, row: 6}
  - invariant: Every document has a person accountable for it
    business_reason: A document nobody owns has nobody to revise it
    source_finding: {phase: p1, register: business_invariants, row: 7}
  actions:
  - action: Judge
    object: Phase document
    trigger: The document's author submits it to its phase
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: 'Judge a phase document, with and without the composition and earlier documents'}
  - action: Build
    object: Approved mandate
    trigger: The person driving the change requests construction
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Build an approved mandate}
  - action: Draft
    object: Phase document
    trigger: A worker drafts a document for its author
    status: DEFERRED
    source_finding: {phase: p1, register: out_of_scope, row: 1}
  provisional_codes:
  - subdomain: build
    provisional_code: CC_CONSTRUCT_ARTIFACTS_V0
    family: CC
    summary: Measure a design, refuse it if under-determined, and render the artifacts it schedules
    source_finding:
      phase: p4
      register: capability_graph
      key: Build an approved mandate
  - subdomain: build
    provisional_code: CC_PERSIST_ARTIFACTS_V0
    family: CC
    summary: Write a rendered construction beneath the root its runtime binding declares
    source_finding:
      phase: p4
      register: capability_graph
      key: Build an approved mandate
  - subdomain: build
    provisional_code: CT_PURE_ATTRIBUTE_PROVENANCE_V1
    family: CT
    summary: Report, for each leaf of a rendered artifact, whether the design stated it, a constitution
      governs it, or the renderer supplied it
    source_finding:
      phase: p4
      register: capability_graph
      key: Render, measure and attribute the artifacts a mandate schedules
  - subdomain: build
    provisional_code: CT_PURE_MEASURE_COMPLETENESS_V0
    family: CT
    summary: Measure Construction Completeness and refuse a design that does not determine its artifacts
    source_finding:
      phase: p4
      register: capability_graph
      key: Render, measure and attribute the artifacts a mandate schedules
  - subdomain: build
    provisional_code: CT_PURE_RENDER_ARTIFACTS_V0
    family: CT
    summary: Render every artifact a mandate schedules from the design that determines it
    source_finding:
      phase: p4
      register: capability_graph
      key: Render, measure and attribute the artifacts a mandate schedules
  - subdomain: build
    provisional_code: IN_CONSTRUCTION_REQUESTED_V0
    family: IN
    summary: Offer an approved design and mandate for construction
    source_finding:
      phase: p4
      register: capability_graph
      key: Build an approved mandate
  - subdomain: build
    provisional_code: RB_CONSTRUCTION_BINDINGS_V0
    family: RB
    summary: Runtime bindings for the construction lifecycle
    source_finding:
      phase: p4
      register: capability_graph
      key: Build an approved mandate
  - subdomain: build
    provisional_code: VOCAB_FACT_PROVENANCE_V0
    family: VOCAB
    summary: Where a value construction wrote came from
    source_finding:
      phase: p4
      register: capability_graph
      key: Build an approved mandate
  - subdomain: build
    provisional_code: WF_CONSTRUCT_ARTIFACTS_V0
    family: WF
    summary: Construct protocol artifacts from an approved design and mandate
    source_finding:
      phase: p4
      register: capability_graph
      key: Build an approved mandate
  - subdomain: design
    provisional_code: AC_GATE_REVIEWER_V0
    family: AC
    summary: Human reviewer at a pipeline gate
    source_finding:
      phase: p4
      register: actors
      key: Reviewer
  - subdomain: design
    provisional_code: AC_REGISTER_AUTHOR_V0
    family: AC
    summary: Author of record for a phase register
    source_finding:
      phase: p4
      register: actors
      key: Author of record
  - subdomain: design
    provisional_code: AC_SEED_AUTHOR_V0
    family: AC
    summary: Author of record for a seed
    source_finding:
      phase: p4
      register: actors
      key: Problem statement author
  - subdomain: design
    provisional_code: CC_JUDGE_AGAINST_COMPOSITION_V1
    family: CC
    summary: Parse a phase document and its priors, observe the composition and its declarations, and judge
      them together
    source_finding:
      phase: p4
      register: capability_graph
      key: Judge a phase document, with and without the composition and earlier documents
  - subdomain: design
    provisional_code: CC_JUDGE_AGAINST_SNAPSHOT_V1
    family: CC
    summary: Parse a phase document and its priors, observe the composition, and judge them together
    source_finding:
      phase: p4
      register: capability_graph
      key: Judge a phase document, with and without the composition and earlier documents
  - subdomain: design
    provisional_code: CC_JUDGE_DOCUMENT_V0
    family: CC
    summary: Parse a phase document and judge it against a declared rule set
    source_finding:
      phase: p4
      register: capability_graph
      key: Judge a phase document, with and without the composition and earlier documents
  - subdomain: design
    provisional_code: CT_PURE_EVALUATE_RULES_V1
    family: CT
    summary: Evaluate a declared rule set against parsed registers
    source_finding:
      phase: p4
      register: capability_graph
      key: Apply every rule of a phase and report each failure
  - subdomain: design
    provisional_code: CT_PURE_PARSE_PRIOR_PHASES_V1
    family: CT
    summary: Parse the upstream phase documents a phase is judged against
    source_finding:
      phase: p4
      register: capability_graph
      key: Read the earlier phase documents a phase must agree with
  - subdomain: design
    provisional_code: CT_PURE_PARSE_REGISTERS_V1
    family: CT
    summary: Parse phase document text into structured registers
    source_finding:
      phase: p4
      register: capability_graph
      key: Read a phase document into its registers
  - subdomain: design
    provisional_code: IN_ANALYSIS_LOOP_SUBMITTED_V0
    family: IN
    summary: Offer an Analysis Loop register for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: IN_AUTHORING_MANDATE_SUBMITTED_V0
    family: IN
    summary: Offer an Authoring Mandate for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: IN_BUSINESS_INTENT_SUBMITTED_V0
    family: IN
    summary: Offer a Business Intent register for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: IN_BUSINESS_MODEL_SUBMITTED_V0
    family: IN
    summary: Offer a Business Model register for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: IN_CHANGE_REQUEST_SUBMITTED_V0
    family: IN
    summary: Offer a Change Request register for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: IN_DESIGN_INTENT_SUBMITTED_V0
    family: IN
    summary: Offer a Design Intent register for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: IN_DOMAIN_MODEL_SUBMITTED_V0
    family: IN
    summary: Offer a Domain Model register for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: IN_GOVERNANCE_INTENT_SUBMITTED_V0
    family: IN
    summary: Offer a Governance Intent register for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: IN_SEED_SUBMITTED_V0
    family: IN
    summary: Offer a seed document for admissibility judgement
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: RB_TRANSFORMATION_BINDINGS_V0
    family: RB
    summary: Runtime bindings for the transformation phase pipeline
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: VOCAB_DESIGN_REGISTER_TERMS_V0
    family: VOCAB
    summary: The controlled terms the phase registers are written in
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P0_SEED_ADMISSIBILITY_V1
    family: WF
    summary: Decide whether an offered seed is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    family: WF
    summary: Decide whether an offered Change Request register is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    family: WF
    summary: Decide whether an offered Domain Model register is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    family: WF
    summary: Decide whether an offered Analysis Loop register is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    family: WF
    summary: Decide whether an offered Business Model register is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    family: WF
    summary: Decide whether an offered Business Intent register is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    family: WF
    summary: Decide whether an offered Governance Intent register is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    family: WF
    summary: Decide whether an offered Design Intent register is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    family: WF
    summary: Decide whether an offered Authoring Mandate is admissible
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V1
    family: STRUCTURE
    summary: Build-time STRUCTURE manifest (transformation pipeline domain scope)
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - subdomain: design
    provisional_code: STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    family: STRUCTURE
    summary: Deterministic figure of merit for a phase document — deduction-based, 0 to 5
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: STRUCTURE_PHASE_FINDINGS_V0
    family: STRUCTURE
    summary: 'The rules a phase document failed: each one''s code, identity, place, detail and intent'
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: STRUCTURE_PHASE_HEADER_V0
    family: STRUCTURE
    summary: 'A phase document''s header: its Machine block''s `document` mapping, as parsed'
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: STRUCTURE_PHASE_PRIORS_V0
    family: STRUCTURE
    summary: The upstream phase documents a phase is judged against, parsed, by phase id
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: STRUCTURE_PHASE_REGISTERS_V0
    family: STRUCTURE
    summary: A phase document's registers, by id, each with its value as written
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: STRUCTURE_PHASE_SECTIONS_V0
    family: STRUCTURE
    summary: A phase document's prose sections, in order, as parsed
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  - subdomain: design
    provisional_code: STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
    family: STRUCTURE
    summary: Which register schema, workflow and template each design phase dispatches to
    source_finding:
      phase: p4
      register: capability_graph
      key: The nine phases, each with its rules and its entry point
  cross_subdomain_refs: null
```

WHAT the change does — behaviour, objects, identity, invariants, actions — with provisional codes. The
provisional codes are the artifacts as they stand; they were listed from the registry by
`.github/process/notes/genesis-generators/p5_provisional_codes.py`.

---

## 0. Subdomain Purpose

### Purpose Provenance

### Subdomain Purposes

---

## 1. Scope Boundary

---

## 2. Business Objects

---

## 3. Identity Semantics

---

## 4. Invariants

---

## 5. Actions

---

## 6. Provisional Codes

---

## 7. Cross-Subdomain References
