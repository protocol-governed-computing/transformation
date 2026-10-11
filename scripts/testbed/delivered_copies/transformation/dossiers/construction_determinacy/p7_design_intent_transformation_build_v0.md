# Stage 7 — Design Intent: transformation / build

## Machine

```yaml
document:
  phase: p7
  domain: transformation
  subdomain: build
  cr: construction_determinacy
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Where provenance is determined
    business_fact: Only the renderer knows where a value came from, because it is the thing that put it there.
    resolution: 'A transform reports, for each leaf of each rendered artifact, one of three origins: the design stated it, a constitution governs it, or the renderer supplied it.'
    source_finding: {phase: p6, register: boundary_rules, key: PROVENANCE_IS_THE_TEST}
  - decision: What the origins are, and which admit a design
    business_fact: A fact a constitution fixes may be supplied; a fact nobody governs and nobody states may not.
    resolution: 'A vocabulary carries the three origins and states which admit a design as complete: stated by the design, and governed elsewhere. Supplied by the renderer does not.'
    source_finding: {phase: p6, register: boundary_rules, key: A_FACT_HAS_A_STATED_ORIGIN}
  - decision: What the measure tests
    business_fact: Testing presence cannot distinguish a value the design supplied from one the renderer did.
    resolution: The measure keeps walking the renderer's output leaf by leaf, and marks a leaf determined when its reported origin is one the vocabulary admits, rather than when it is non-empty.
    source_finding: {phase: p6, register: boundary_rules, key: THE_POPULATION_STAYS_DERIVED}
  - decision: What happens to the three defaults
    business_fact: A design that omits a default measures complete, which is what the two literals did.
    resolution: Each default reports its origin as supplied by the renderer, so a design omitting one reads short. The fallback still produces a working artifact; it no longer produces a complete measurement.
    source_finding: {phase: p6, register: boundary_rules, key: A_DEFAULT_IS_AN_INVENTION}
  - decision: What happens to the event's moment field
    business_fact: The event constitution fixes it, and a design restating what a constitution settles would state it twice.
    resolution: It reports its origin as governed elsewhere, naming the constitution that fixes it. The ground moves from prose beside code into a value the measure reads.
    source_finding: {phase: p6, register: boundary_rules, key: A_FACT_HAS_A_STATED_ORIGIN}
  - decision: What happens to the two vocabulary literals
    business_fact: No register carries a vocabulary's group name or spelling rule.
    resolution: They report as supplied by the renderer, so every design scheduling a vocabulary reads short until the design subdomain adds the columns. The register is named for its owner; it is not amended here.
    source_finding: {phase: p6, register: boundary_rules, key: A_REGISTER_IS_EXTENDED_BY_ITS_OWNER}
  - decision: What happens to the build manifest
    business_fact: Every field of it is compiler configuration and no business fact determines any of them.
    resolution: Construction stops writing it. Nothing replaces it in this change, and a domain the compiler cannot yet discover is a named deferral rather than a silent gap.
    source_finding: {phase: p6, register: boundary_rules, key: NOTHING_OUTSIDE_THE_MANDATE}
  existing_inventory:
  - fqdn: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    action: EXTEND
    summary: Render every artifact a mandate schedules from the design that determines it
    reason: Gains the reporting of an origin per leaf. Every family it renders is answerable for each value it writes.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    action: EXTEND
    summary: Measure Construction Completeness and refuse a design that does not determine its artifacts
    reason: 'Its population is unchanged and its test changes: a leaf is determined when its reported origin admits a design, not when it is non-empty.'
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: transformation::CC_PERSIST_ARTIFACTS_V0
    action: REVIEW
    summary: Write a rendered construction beneath the root its runtime binding declares
    reason: 'Its declaration is already correct: one step, writing the documents it is handed. The founding of a build manifest happens above it, in what decides which documents to hand it, so what this change removes is not stated in this artifact.'
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    action: REVIEW
    summary: Construct protocol artifacts from an approved design and mandate
    reason: Names the three steps that measure, render and write. Unchanged in shape; two of its three steps change beneath it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    action: REVIEW
    summary: Measure a design, refuse it if under-determined, and render the artifacts it schedules
    reason: The act is right and its routing is unchanged. Named because what it refuses becomes stricter.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: transformation::IN_CONSTRUCTION_REQUESTED_V0
    action: REUSE
    summary: Offer an approved design and mandate for construction
    reason: What is offered is correct; what is done with it is not. Unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: transformation::RB_CONSTRUCTION_BINDINGS_V0
    action: REUSE
    summary: Runtime bindings for the construction lifecycle
    reason: Unchanged. Named because the amended contracts are bound through it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    action: REVIEW
    summary: 'Phase 7 of the change pipeline: decide whether an offered design is admissible'
    reason: Its vocabulary register states a value and its meaning and has no column for the group or the spelling. Named for `design` to extend; not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - fqdn: vocabulary::CONSTITUTION_VOCABULARY_V0
    action: REVIEW
    summary: Governs what a vocabulary is and what it must declare
    reason: The artifact the platform refused was refused against a rule this constitution carries. Unchanged; named as the authority the new vocabulary is governed by.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - fqdn: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
    action: REVIEW
    summary: Declares what the transformation domain compiles
    reason: Unchanged; named because the amended and authored artifacts are compiled under it.
    source_finding: {phase: p6, register: ownership, row: 1}
  new_artifacts:
  - capability: Reporting where each rendered value came from
    family: CT
    code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    summary: Report, for each leaf of a rendered artifact, whether the design stated it, a constitution governs it, or the renderer supplied it
    owner_subdomain: build
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 1}
  - capability: Declaring that something else governs a fact
    family: VOCAB
    code: transformation::VOCAB_FACT_PROVENANCE_V0
    summary: The origins a rendered fact may have, and which of them admit a design as complete
    owner_subdomain: build
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 3}
  rb_declarations:
  - rb_code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    binds_wf: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    cs_bindings:
    - Unchanged
    storage_structure: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
    source_finding: {phase: p6, register: ownership, row: 8}
  execution_topology: []
  cc_composition: []
  step_bindings: []
  interface_fields:
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: INPUT
    field: design_registers
    type: array
    required: 'YES'
    default: null
    meaning: Parsed P7 registers — the design semantics
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: INPUT
    field: mandate_registers
    type: array
    required: 'YES'
    default: null
    meaning: Parsed P8 registers — the build order
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: OUTPUT
    field: artifacts
    type: array
    required: 'YES'
    default: null
    meaning: One entry per artifact — path, domain, and the Machine block
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: OUTPUT
    field: documents
    type: array
    required: 'YES'
    default: null
    meaning: The same artifacts as {path, text} — what persistence is handed
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: OUTPUT
    field: artifact_count
    type: integer
    required: 'YES'
    default: null
    meaning: How many artifacts were rendered
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: OUTPUT
    field: sources
    type: object
    required: 'YES'
    default: null
    meaning: For each leaf of each rendered artifact, the register it was read from or the authority it defers to. The fact the measure needs and could not previously obtain.
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: INPUT
    field: design_registers
    type: array
    required: 'YES'
    default: null
    meaning: Parsed P7 registers — the design semantics
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: INPUT
    field: mandate_registers
    type: array
    required: 'YES'
    default: null
    meaning: Parsed P8 registers — the build order
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: INPUT
    field: threshold
    type: number
    required: 'YES'
    default: null
    meaning: Minimum Construction Completeness; 100 unless a caller deliberately relaxes it
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: INPUT
    field: provenance
    type: object
    required: 'YES'
    default: null
    meaning: One origin per leaf, as the provenance transform reported it. What the test is applied to.
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: OUTPUT
    field: completeness
    type: number
    required: 'YES'
    default: null
    meaning: The proportion of leaves whose reported origin admits a design
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: OUTPUT
    field: determined
    type: integer
    required: 'YES'
    default: null
    meaning: How many leaves the design determined
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: OUTPUT
    field: required
    type: integer
    required: 'YES'
    default: null
    meaning: How many leaves construction needs
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: OUTPUT
    field: undetermined
    type: array
    required: 'YES'
    default: null
    meaning: The leaves the design did not determine, each with the origin reported for it
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    direction: INPUT
    field: rendered
    type: object
    required: 'YES'
    default: null
    meaning: One rendered artifact, as the renderer produced it.
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    direction: INPUT
    field: sources
    type: object
    required: 'YES'
    default: null
    meaning: For each leaf the renderer wrote, the register it read or the authority it deferred to.
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    direction: OUTPUT
    field: provenance
    type: object
    required: 'YES'
    default: null
    meaning: One origin per leaf, drawn from the vocabulary of origins.
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    direction: OUTPUT
    field: governing_artifacts
    type: object
    required: 'YES'
    default: null
    meaning: 'For each leaf whose origin is governed elsewhere, the artifact that governs it. Not named `governed_by`: that key is reserved for an artifact''s own authority, and a step output spelled the same is read as one.'
  - artifact: transformation::VOCAB_FACT_PROVENANCE_V0
    direction: ATTRIBUTE
    field: symbols
    type: object
    required: 'YES'
    default: null
    meaning: Each admissible origin, what it means, and whether a design carrying it is complete.
  implementation_bindings:
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    module: transformation.implementation.capability_transforms.atoms.ct_pure_attribute_provenance_v0
    callable: execute
    operation: ATTRIBUTE_PROVENANCE
    kind: atom
    purity: ct_pure
    refusal: returns
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_ATTRIBUTE_PROVENANCE_V0}
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    module: transformation.implementation.capability_transforms.atoms.ct_pure_render_artifacts_v0
    callable: execute
    operation: PURE_RENDER_ARTIFACTS
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p7, register: existing_inventory, key: CT_PURE_RENDER_ARTIFACTS_V0}
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    module: transformation.implementation.capability_transforms.atoms.ct_pure_measure_completeness_v0
    callable: execute
    operation: PURE_MEASURE_COMPLETENESS
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding: {phase: p7, register: existing_inventory, key: CT_PURE_MEASURE_COMPLETENESS_V0}
  vocabulary_extensions:
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: stated_by_design
    meaning: A register of the design carries the value. The design determines the fact, and a design carrying only these is complete.
    source_finding: {phase: p7, register: design_resolution, row: 2}
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: governed_elsewhere
    meaning: A constitution fixes the value, and the artifact that fixes it is named. The design need not state it, and a design carrying these is complete.
    source_finding: {phase: p7, register: design_resolution, row: 5}
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: carried_from_predecessor
    meaning: The artifact already carried the value and no register of the design can express it — a prose description is the case. Preserving is not authoring, so a design carrying these is complete.
    source_finding: {phase: p7, register: design_resolution, row: 3}
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: supplied_by_renderer
    meaning: The renderer wrote the value from its own text or from a fallback, and nothing governs it. A design carrying one of these is not complete.
    source_finding: {phase: p7, register: design_resolution, row: 4}
  runtime_policies: []
  artifact_properties:
  - artifact: transformation::VOCAB_FACT_PROVENANCE_V0
    property: governed_by
    value: vocabulary::CONSTITUTION_VOCABULARY_V0
    source_finding: {phase: p7, register: new_artifacts, key: VOCAB_FACT_PROVENANCE_V0}
  - artifact: transformation::VOCAB_FACT_PROVENANCE_V0
    property: concern
    value: build
    source_finding: {phase: p6, register: ownership, row: 3}
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    property: concern
    value: build
    source_finding: {phase: p6, register: ownership, row: 1}
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: EXTEND
    subdomain: build
    count: '2'
    artifacts: transformation::CT_PURE_RENDER_ARTIFACTS_V0, transformation::CT_PURE_MEASURE_COMPLETENESS_V0
  - action: NEW
    subdomain: build
    count: '2'
    artifacts: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0, transformation::VOCAB_FACT_PROVENANCE_V0
  generation_provenance: []
  declared_reach: []
  refusal_discharge: []
  refusal_deferrals:
  - operation: Rendering an artifact
    refused_when: The design does not state a fact the artifact carries
    deferred_to: design
    until: The register that carries a vocabulary's values gains the columns for its group and its spelling. Until then a design scheduling a vocabulary reads short, which is the refusal working rather than failing.
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - operation: Writing a construction
    refused_when: An artifact was produced that the mandate did not schedule
    deferred_to: build
    until: 'Carried by this change: construction stops founding a build manifest, so nothing is produced outside a mandate. Recorded as a deferral because founding a domain the compiler can discover has no replacement yet.'
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - operation: Rendering an artifact
    refused_when: Its domain would have to be inferred from where a file or a dossier sits
    deferred_to: build
    until: 'Carried by this change: the only fact ever derived from an identity was the manifest''s domain, and the manifest leaves construction with it.'
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  refusal_governance_discharge: []
```

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

---

## 1. Design Decisions Resolution

---

## 2. Artifact Inventory — Existing Artifacts

---

## 3. Artifact Family Mapping — New Artifacts

---

## 4. Runtime Binding (RB) Declarations

---

## 5. Execution Topology

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Implementation Bindings

---

## 10. Vocabulary Extensions

---

## 11. Runtime Policies

---

## 12. Artifact Properties

---

## 13. STRUCTURE Stores

---

## 14. Transport Bindings

---

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

---

## 18. Refusal Discharge

---

## 19. Refusal Deferrals

---

## 20. Refusal Governance Discharge

---

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`47dd8edc2123…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the authoring of the two artifacts §3 declares and the amendment of
the two §2 marks EXTEND. It authorizes nothing else.

Two rows of §2 changed at this closure. The contract that writes a construction was first marked
EXTEND and is cited REVIEW: what this change removes from it — the founding of a build manifest —
happens above it, in what decides which documents to hand it, and is not stated in the artifact at
all. And the design's module path for the new transform was refused before it was right: the loader
resolves a transform by its own code, and a module the loader does not look for is a transform that
does not run.
