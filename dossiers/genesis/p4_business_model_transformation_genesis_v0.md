# Business Model — transformation / design, build

## Machine

```yaml
document:
  phase: p4
  domain: transformation
  subdomain:
  - design
  - build
  cr: genesis
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Author of record
    role: Writes a phase document and is accountable for its content
    authority_class: Operator
    source_finding: {phase: p1, register: authority_boundaries, key: A document's content}
  - actor: Reviewer
    role: Approves an admissible document at its gate
    authority_class: Approver
    source_finding: {phase: p1, register: authority_boundaries, key: Approval at a gate}
  - actor: Problem statement author
    role: Writes the problem statement in their own words and confirms the seed says what they meant
    authority_class: Owner
    source_finding: {phase: p1, register: known_facts, row: 15}
  bm_entities:
  - entity: Phase Document
    description: The document one phase judges
    store_model: Not held by the pipeline; supplied whole as text with each request
    source_finding: {phase: p2, register: entities, key: Phase Document}
  - entity: Rule
    description: A declared condition a document must meet, with the reason it exists
    store_model: Declared once, versioned, carried with the phase it governs
    source_finding: {phase: p2, register: entities, key: Rule}
  - entity: Verdict
    description: The result of judging one document, with every finding
    store_model: Returned to the person who asked
    source_finding: {phase: p2, register: entities, key: Verdict}
  - entity: Finding
    description: One failed rule, placed in the document, with the reason the rule exists
    store_model: Part of its verdict
    source_finding: {phase: p2, register: entities, key: Finding}
  - entity: Mandate
    description: The approved schedule of the artifacts to build
    store_model: A phase document supplied as text with the request to build it
    source_finding: {phase: p2, register: entities, key: Mandate}
  resources:
  - resource: Rule sets
    description: The rules each phase applies, readable from the composition
    source_finding: {phase: p2, register: entities, key: Rule}
  - resource: Built artifacts
    description: The artifacts construction writes where the composition is authored
    source_finding: {phase: p2, register: business_processes, key: Build an approved mandate}
  events:
  - event: Document judged
    trigger: A phase judges a document against its rules
    lifecycle_meaning: The document receives its verdict and every finding
    source_finding: {phase: p1, register: business_events, key: Document Judged}
  - event: Document approved
    trigger: The reviewer approves an admissible document at its gate
    lifecycle_meaning: The pipeline may continue past the gate
    source_finding: {phase: p1, register: business_events, key: Document Approved}
  - event: Mandate built
    trigger: Construction builds an approved mandate
    lifecycle_meaning: The change's artifacts exist and their determination is reported
    source_finding: {phase: p1, register: business_events, key: Mandate Built}
  relationships:
  - subject: Phase document
    verb: is judged by
    object: The rules declared for its phase
    capability_need: Apply every rule of a phase and report each failure
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - subject: Verdict
    verb: names
    object: Every finding
    capability_need: Apply every rule of a phase and report each failure
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - subject: Phase document
    verb: preserves
    object: The commitments of the earlier documents
    capability_need: Read the earlier phase documents a phase must agree with
    source_finding: {phase: p2, register: process_steps, row: 2}
  - subject: Phase document
    verb: is grounded in
    object: The composition the change is designed against
    capability_need: Observe the composition a change is designed against
    source_finding: {phase: p1, register: known_facts, row: 8}
  - subject: Mandate
    verb: is built into
    object: The artifacts it schedules
    capability_need: Build an approved mandate
    source_finding: {phase: p1, register: known_facts, row: 12}
  capability_graph:
  - capability: Observe the composition a change is designed against
    source_finding: {phase: p3, register: authoring_decisions, key: Observe the composition a change is designed against}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Write built artifacts where the composition is authored
    source_finding: {phase: p3, register: authoring_decisions, key: Write built artifacts where the composition is authored}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Read a phase document into its registers
    source_finding: {phase: p3, register: authoring_decisions, key: Read a phase document into its registers}
    status: GAP
    gap_register_entry: GAP-01
    notes: Authored; shared by every phase and by construction.
  - capability: Read the earlier phase documents a phase must agree with
    source_finding: {phase: p3, register: authoring_decisions, key: Read the earlier phase documents a phase must agree with}
    status: GAP
    gap_register_entry: GAP-02
    notes: Authored.
  - capability: Apply every rule of a phase and report each failure
    source_finding: {phase: p3, register: authoring_decisions, key: Apply every rule of a phase and report each failure}
    status: GAP
    gap_register_entry: GAP-03
    notes: Authored; mechanism only, the rules are carried by each phase.
  - capability: Judge a phase document, with and without the composition and earlier documents
    source_finding: {phase: p3, register: authoring_decisions, key: 'Judge a phase document, with and without the composition and earlier documents'}
    status: GAP
    gap_register_entry: GAP-04
    notes: Authored.
  - capability: The nine phases, each with its rules and its entry point
    source_finding: {phase: p3, register: authoring_decisions, key: 'The nine phases, each with its rules and its entry point'}
    status: GAP
    gap_register_entry: GAP-05
    notes: Authored.
  - capability: Render, measure and attribute the artifacts a mandate schedules
    source_finding: {phase: p3, register: authoring_decisions, key: 'Render, measure and attribute the artifacts a mandate schedules'}
    status: GAP
    gap_register_entry: GAP-06
    notes: Authored.
  - capability: Build an approved mandate
    source_finding: {phase: p3, register: authoring_decisions, key: Build an approved mandate}
    status: GAP
    gap_register_entry: GAP-07
    notes: Authored.
  - capability: The author of record and the reviewer
    source_finding: {phase: p3, register: authoring_decisions, key: The author of record and the reviewer}
    status: GAP
    gap_register_entry: GAP-08
    notes: Authored.
  dependency_graph:
  - from: design
    to: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Composition observation}
  - from: build
    to: capability_side_effects::CS_TEXT_ARTIFACT_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Artifact persistence}
  - from: design
    to: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    dependency_type: configuration
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Execution configuration}
  - from: design
    to: lifecycle::CONSTITUTION_CHANGE_MGMT_V1
    dependency_type: governance
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 4}
  - from: build
    to: lifecycle::CONSTITUTION_CONSTRUCTION_V1
    dependency_type: governance
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 5}
  constraint_register:
  - number: '1'
    constraint: What is checked, and why it matters, must not live in code.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: constraint
  - number: '2'
    constraint: The first phase must not add business content, resolve an open question, assign design, or treat a belief as a fact.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: constraint
  - number: '3'
    constraint: Construction must not write a value the design did not determine.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: constraint
  - number: '4'
    constraint: The pipeline must read the composition only through the platform's inspection capability.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: constraint
  - number: '5'
    constraint: Workers that draft documents, reachability beyond a local command line, and a governed generation step must not be designed into this change.
    source_finding: {phase: p1, register: constraints, row: 5}
    source: constraint
  - number: '6'
    constraint: Every phase is judged only by rules declared for it.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '7'
    constraint: A verdict reports every failed rule.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '8'
    constraint: The same document and the same rules give the same verdict.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '9'
    constraint: Every rule states why it exists.
    source_finding: {phase: p1, register: business_invariants, row: 4}
    source: invariant
  - number: '10'
    constraint: Nothing is built that a person did not approve.
    source_finding: {phase: p1, register: business_invariants, row: 5}
    source: invariant
  - number: '11'
    constraint: A built artifact holds only what the design or a governing artifact determined.
    source_finding: {phase: p1, register: business_invariants, row: 6}
    source: invariant
  - number: '12'
    constraint: Every document has a person accountable for it.
    source_finding: {phase: p1, register: business_invariants, row: 7}
    source: invariant
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Read a phase document into its registers}
    capability: Read a phase document into its registers
    owner_subdomain: design
    resolution: NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Read the earlier phase documents a phase must agree with}
    capability: Read the earlier phase documents a phase must agree with
    owner_subdomain: design
    resolution: NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Apply every rule of a phase and report each failure}
    capability: Apply every rule of a phase and report each failure
    owner_subdomain: design
    resolution: NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: 'Judge a phase document, with and without the composition and earlier documents'}
    capability: Judge a phase document, with and without the composition and earlier documents
    owner_subdomain: design
    resolution: NEW
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: 'The nine phases, each with its rules and its entry point'}
    capability: The nine phases, each with its rules and its entry point
    owner_subdomain: design
    resolution: NEW
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: 'Render, measure and attribute the artifacts a mandate schedules'}
    capability: Render, measure and attribute the artifacts a mandate schedules
    owner_subdomain: build
    resolution: NEW
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: Build an approved mandate}
    capability: Build an approved mandate
    owner_subdomain: build
    resolution: NEW
  - gap_code: GAP-08
    source_finding: {phase: p3, register: authoring_decisions, key: The author of record and the reviewer}
    capability: The author of record and the reviewer
    owner_subdomain: design
    resolution: NEW
  design_decisions:
  - number: '1'
    decision: Design and build are two new subdomains of one new domain, transformation.
    source_finding: {phase: p3, register: placement_decision}
    rationale: The composition carries nothing of the pipeline, and the phases and construction fail differently and are fixed by different people.
    constraints_imposed: Each subdomain owns its own capabilities; construction reads the phases' reading capability and nothing else of the design subdomain.
  - number: '2'
    decision: One reading capability, one evaluating capability and one judging composition serve all nine phases; each phase carries its own rules.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
    rationale: The phases differ only by their rules, and rules are governance, not mechanism.
    constraints_imposed: No phase may carry a mechanism of its own; a new kind of check is a change to the evaluating capability.
  - number: '3'
    decision: The founding change is judged by the rules it declares, each naming the platform invariant it realises.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    rationale: The composition it is designed against holds none of the pipeline's rules.
    constraints_imposed: Every later change to the pipeline is judged by the rules sealed in its pinned composition.
  - number: '4'
    decision: Construction reuses the platform's text persistence and authors only the pure steps before it.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    rationale: Writing carries no pipeline meaning; rendering, measuring and attributing do.
    constraints_imposed: Construction writes only beneath a declared root.
  authoring_scope:
  - capability: Read a phase document into its registers
    gap_register_ref: GAP-01
  - capability: Read the earlier phase documents a phase must agree with
    gap_register_ref: GAP-02
  - capability: Apply every rule of a phase and report each failure
    gap_register_ref: GAP-03
  - capability: Judge a phase document, with and without the composition and earlier documents
    gap_register_ref: GAP-04
  - capability: The nine phases, each with its rules and its entry point
    gap_register_ref: GAP-05
  - capability: Render, measure and attribute the artifacts a mandate schedules
    gap_register_ref: GAP-06
  - capability: Build an approved mandate
    gap_register_ref: GAP-07
  - capability: The author of record and the reviewer
    gap_register_ref: GAP-08
```

The canonical consolidation every later phase projects from. Nothing here re-litigates Stage 3.

---

## 1. Actors

---

## 2. Business Entities

---

## 3. Resources

---

## 4. Events

---

## 5. Relationships

---

## 6. Capability Graph

---

## 7. Dependency Graph

---

## 8. Constraint Register

---

## 9. Gap Register

---

## 10. Design Decisions

---

## 11. Authoring Scope
