# Domain Model — transformation / design, build

## Machine

```yaml
document:
  phase: p2
  domain: transformation
  subdomain:
  - design
  - build
  cr: genesis
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Phase Document
    description: The document one phase judges, written by its author of record.
    store_model: Not held by the pipeline. The person driving the change supplies its whole text with each request, so a verdict is reproducible from what was judged.
    evidence_status: INFERRED
    source_finding:
    - {phase: p1, register: business_vocabulary, key: Phase}
    - {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Rule
    description: A declared condition a document must meet, with the reason it exists.
    store_model: Declared once, versioned, and carried with the phase it governs, so it can be read from the composition.
    evidence_status: INFERRED
    source_finding:
    - {phase: p1, register: business_vocabulary, key: Rule}
    - {phase: p1, register: identity_and_sameness, row: 2}
  - entity: Verdict
    description: The result of judging one document, with every finding.
    store_model: Returned to the person who asked; not held by the pipeline.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Verdict}
  - entity: Finding
    description: One failed rule, placed in the document, with the reason the rule exists.
    store_model: Part of its verdict.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Finding}
  - entity: Mandate
    description: The approved schedule of the artifacts to build.
    store_model: A phase document; supplied as text with the request to build it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Mandate}
  entity_attributes:
  - entity: Phase Document
    attribute: Phase
    meaning: Which phase's rules judge it; part of what identifies it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Phase Document
    attribute: Domain and Subdomain
    meaning: What the change is to; part of what identifies it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Phase Document
    attribute: Change
    meaning: The change it belongs to; part of what identifies it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Phase Document
    attribute: State
    meaning: Drafted, admissible, inadmissible or approved.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_states, key: Phase Document}
  - entity: Rule
    attribute: Reason
    meaning: Why the rule exists, reported with every finding against it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - entity: Verdict
    attribute: Outcome
    meaning: Admissible or inadmissible; there is no partial pass.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - entity: Finding
    attribute: Place
    meaning: Where in the document the rule failed.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 5}
  - entity: Mandate
    attribute: Determination
    meaning: How much of each built artifact the design stated.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 13}
  business_processes:
  - process: Judge a phase document
    initiator: The document's author
    outcome: A verdict naming every rule the document failed, where, and why the rule exists.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Document Judged}
  - process: Approve a document at its gate
    initiator: The reviewer
    outcome: The admissible document is approved and the pipeline continues past the gate.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Document Approved}
  - process: Build an approved mandate
    initiator: The person driving the change
    outcome: The artifacts the mandate schedules, with how much of each the design determined.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Mandate Built}
  process_steps:
  - process: Judge a phase document
    step: '1'
    action: Read the document into its registers, adding and deciding nothing
    record_produced: The document's registers
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 2}
  - process: Judge a phase document
    step: '2'
    action: Read the earlier phase documents whose commitments this one must preserve
    record_produced: The earlier documents' registers
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 8}
  - process: Judge a phase document
    step: '3'
    action: Observe the composition the change is designed against, through the inspection capability
    record_produced: The facts the rules ground against
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 20}
  - process: Judge a phase document
    step: '4'
    action: Apply every rule declared for the phase, never stopping at the first failure
    record_produced: The verdict and its findings
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 4}
  - process: Approve a document at its gate
    step: '1'
    action: Confirm the document is admissible
    record_produced: An admissibility decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Approve a document at its gate
    step: '2'
    action: Record the reviewer's approval on the document
    record_produced: The approval
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 5}
  - process: Build an approved mandate
    step: '1'
    action: Confirm the mandate is approved
    record_produced: An approval decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - process: Build an approved mandate
    step: '2'
    action: Read the design and the mandate into their registers
    record_produced: The design's and mandate's registers
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 12}
  - process: Build an approved mandate
    step: '3'
    action: Render each scheduled artifact from what the design states
    record_produced: The rendered artifacts
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 12}
  - process: Build an approved mandate
    step: '4'
    action: Measure how much of each artifact the design determined, and say where each value came from
    record_produced: The determination and its provenance
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 13}
  - process: Build an approved mandate
    step: '5'
    action: Write the artifacts where the composition is authored
    record_produced: The built artifacts
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Mandate Built}
  belief_verification:
  - belief: The composition the change is designed against holds no part of the transformation domain.
    result: NOT_FOUND
    evidence: The pinned composition declares seven domains — ai_governance, blockchain, book_library_mgmt, causal_language_model, inspection, platform, workload — and its artifact index carries no identity in the transformation namespace.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The platform offers an inspection capability that answers questions about a composition.
    result: VERIFIED
    evidence: 'capability_side_effects::CS_SNAPSHOT_QUERY_V0 observes an assembled composition read-only through the inspection surface, and the composition publishes nineteen inspection operations, among them si.artifact.show, si.artifact.list, si.artifact.refs, si.rule_set.list, si.vocab.resolve and si.capability.surface.'
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: The platform governs how a capability, a workflow, a binding and a structure are declared.
    result: VERIFIED
    evidence: 'The composition holds a constitution for each kind the pipeline declares: actor::CONSTITUTION_ACTOR_IDENTITY_V0, capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0, capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0, intent::CONSTITUTION_INTENT_V0, runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0, structure::CONSTITUTION_STRUCTURE_V0, vocabulary::CONSTITUTION_VOCABULARY_V0 and workflow::CONSTITUTION_WORKFLOW_V0.'
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  pps_baseline_fqdns:
  - capability: Composition observation
    fqdn: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    what_it_does: Observes an assembled composition read-only, through the inspection surface.
    fit: EXACT
    cannot_do: It answers questions; it decides nothing about a change.
  - capability: Text artifact persistence
    fqdn: capability_side_effects::CS_TEXT_ARTIFACT_V0
    what_it_does: Writes rendered artifacts as text documents beneath a declared root.
    fit: EXACT
    cannot_do: It writes what it is handed; it decides nothing about what to build.
  - capability: Runtime execution configuration
    fqdn: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    what_it_does: Configures how a workflow is executed by the runtime.
    fit: EXACT
    cannot_do: It carries no pipeline semantics.
  - capability: Governance of the change pipeline
    fqdn: lifecycle::CONSTITUTION_CHANGE_MGMT_V1
    what_it_does: States the pipeline as phases and names the invariants the design compiler enforces.
    fit: EXACT
    cannot_do: It declares what must hold; it judges no document.
  - capability: Governance of construction
    fqdn: lifecycle::CONSTITUTION_CONSTRUCTION_V1
    what_it_does: States the invariants construction enforces.
    fit: EXACT
    cannot_do: It declares what must hold; it builds nothing.
  gaps:
  - gap: Nothing in the composition judges a phase document.
    severity: CRITICAL
    impact: Every requested outcome depends on phases that judge by declared rules; none exists.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: No rule set for any phase is declared in the composition.
    severity: CRITICAL
    impact: Rules readable from the composition is the outcome this change exists for.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: Nothing in the composition builds an approved mandate or measures its determination.
    severity: CRITICAL
    impact: Construction has no counterpart in the composition.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: No actor exists for an author of record or a reviewer.
    severity: CRITICAL
    impact: Accountability at each gate has nothing to bind to.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, row: 7}
  architectural_observations:
  - observation: Reading a composition through the inspection surface is already a declared side effect, so the pipeline need not reach into compiled output.
    evidence: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - observation: Writing rendered artifacts as text is already a declared side effect.
    evidence: capability_side_effects::CS_TEXT_ARTIFACT_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_events, key: Mandate Built}
  - observation: The invariants the pipeline must enforce are already declared by the platform, in two lifecycle constitutions.
    evidence: lifecycle::CONSTITUTION_CHANGE_MGMT_V1 · lifecycle::CONSTITUTION_CONSTRUCTION_V1
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  discovery_concerns:
  - concern: The pipeline judges its own founding change, so the composition this change is designed against cannot hold the pipeline's own rules; its documents are judged by the rules the change itself declares.
    evidence: lifecycle::CONSTITUTION_CHANGE_MGMT_V1
    severity: MAJOR
    evidence_status: INFERRED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  open_questions: null
```

Every claim about what exists is grounded in the pinned baseline
`01fd3cfe7adf131601084130c4d866f3e673bdf2d93a6fb664986a30f4f1f6ee` — 505 artifacts across
ai_governance, blockchain, book_library_mgmt, causal_language_model, inspection, platform and
workload — read through the inspection interface. The semantic model is inherited from Stage 1 and
confirmed here, never re-derived.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions
