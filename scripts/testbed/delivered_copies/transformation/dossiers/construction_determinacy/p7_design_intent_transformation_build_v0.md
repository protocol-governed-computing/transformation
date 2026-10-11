# Stage 7 — Design Intent: transformation / build

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: construction_determinacy
  Status: DRAFT
  Feeds: Stage 8 — Authoring Mandate
registers:
  design_resolution:
    columns:
    - Decision
    - Business Fact
    - Resolution
    - Source Finding
    rows:
    - Decision: Where provenance is determined
      Business Fact: Only the renderer knows where a value came from, because it is the thing that put it there.
      Resolution: 'A transform reports, for each leaf of each rendered artifact, one of three origins: the design stated it, a constitution governs it, or the renderer supplied it.'
      Source Finding: S6 boundary_rules PROVENANCE_IS_THE_TEST
    - Decision: What the origins are, and which admit a design
      Business Fact: A fact a constitution fixes may be supplied; a fact nobody governs and nobody states may not.
      Resolution: 'A vocabulary carries the three origins and states which admit a design as complete: stated by the design, and governed elsewhere. Supplied by the renderer does not.'
      Source Finding: S6 boundary_rules A_FACT_HAS_A_STATED_ORIGIN
    - Decision: What the measure tests
      Business Fact: Testing presence cannot distinguish a value the design supplied from one the renderer did.
      Resolution: The measure keeps walking the renderer's output leaf by leaf, and marks a leaf determined when its reported origin is one the vocabulary admits, rather than when it is non-empty.
      Source Finding: S6 boundary_rules THE_POPULATION_STAYS_DERIVED
    - Decision: What happens to the three defaults
      Business Fact: A design that omits a default measures complete, which is what the two literals did.
      Resolution: Each default reports its origin as supplied by the renderer, so a design omitting one reads short. The fallback still produces a working artifact; it no longer produces a complete measurement.
      Source Finding: S6 boundary_rules A_DEFAULT_IS_AN_INVENTION
    - Decision: What happens to the event's moment field
      Business Fact: The event constitution fixes it, and a design restating what a constitution settles would state it twice.
      Resolution: It reports its origin as governed elsewhere, naming the constitution that fixes it. The ground moves from prose beside code into a value the measure reads.
      Source Finding: S6 boundary_rules A_FACT_HAS_A_STATED_ORIGIN
    - Decision: What happens to the two vocabulary literals
      Business Fact: No register carries a vocabulary's group name or spelling rule.
      Resolution: They report as supplied by the renderer, so every design scheduling a vocabulary reads short until the design subdomain adds the columns. The register is named for its owner; it is not amended here.
      Source Finding: S6 boundary_rules A_REGISTER_IS_EXTENDED_BY_ITS_OWNER
    - Decision: What happens to the build manifest
      Business Fact: Every field of it is compiler configuration and no business fact determines any of them.
      Resolution: Construction stops writing it. Nothing replaces it in this change, and a domain the compiler cannot yet discover is a named deferral rather than a silent gap.
      Source Finding: S6 boundary_rules NOTHING_OUTSIDE_THE_MANDATE
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Render every artifact a mandate schedules from the design that determines it
      Reason: Gains the reporting of an origin per leaf. Every family it renders is answerable for each value it writes.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Measure Construction Completeness and refuse a design that does not determine its artifacts
      Reason: 'Its population is unchanged and its test changes: a leaf is determined when its reported origin admits a design, not when it is non-empty.'
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: transformation::CC_PERSIST_ARTIFACTS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Write a rendered construction beneath the root its runtime binding declares
      Reason: 'Its declaration is already correct: one step, writing the documents it is handed. The founding of a build manifest happens above it, in what decides which documents to hand it, so what this change removes is not stated in this artifact.'
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: transformation::CC_CONSTRUCT_ARTIFACTS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Construct protocol artifacts from an approved design and mandate
      Reason: Names the three steps that measure, render and write. Unchanged in shape; two of its three steps change beneath it.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: transformation::WF_CONSTRUCT_ARTIFACTS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Measure a design, refuse it if under-determined, and render the artifacts it schedules
      Reason: The act is right and its routing is unchanged. Named because what it refuses becomes stricter.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: transformation::IN_CONSTRUCTION_REQUESTED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Offer an approved design and mandate for construction
      Reason: What is offered is correct; what is done with it is not. Unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: transformation::RB_CONSTRUCTION_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Runtime bindings for the construction lifecycle
      Reason: Unchanged. Named because the amended contracts are bound through it.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: 'Phase 7 of the change pipeline: decide whether an offered design is admissible'
      Reason: Its vocabulary register states a value and its meaning and has no column for the group or the spelling. Named for `design` to extend; not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - FQDN: vocabulary::CONSTITUTION_VOCABULARY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Governs what a vocabulary is and what it must declare
      Reason: The artifact the platform refused was refused against a rule this constitution carries. Unchanged; named as the authority the new vocabulary is governed by.
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - FQDN: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares what the transformation domain compiles
      Reason: Unchanged; named because the amended and authored artifacts are compiled under it.
      Source Finding: 'S6 ownership #1'
  new_artifacts:
    columns:
    - Capability
    - Family
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: Reporting where each rendered value came from
      Family: CT
      Code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
      Summary: Report, for each leaf of a rendered artifact, whether the design stated it, a constitution governs it, or the renderer supplied it
      Owner Subdomain: build
      Status: NEW
      Source Finding: 'S6 governance_outcome #1'
    - Capability: Declaring that something else governs a fact
      Family: VOCAB
      Code: transformation::VOCAB_FACT_PROVENANCE_V0
      Summary: The origins a rendered fact may have, and which of them admit a design as complete
      Owner Subdomain: build
      Status: NEW
      Source Finding: 'S6 governance_outcome #3'
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: transformation::RB_CONSTRUCTION_BINDINGS_V0
      Binds WF: transformation::WF_CONSTRUCT_ARTIFACTS_V0
      CS Bindings: Unchanged
      Storage Structure: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
      Source Finding: 'S6 ownership #8'
  execution_topology:
    columns:
    - Workflow
    - Node
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: NONE IDENTIFIED
      Node: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): ''
      Routing: ''
      Source Finding: ''
  cc_composition:
    columns:
    - CC Code
    - Step
    - Step Name
    - Capability
    - Kind (CT, CS)
    - Operation
    - Store
    - Consumes
    - Produces
    - Routing
    - Interpreted By
    - Semantic Status
    - Interface
    rows:
    - CC Code: NONE IDENTIFIED
      Step: ''
      Step Name: ''
      Capability: ''
      Kind (CT, CS): ''
      Operation: ''
      Store: ''
      Consumes: ''
      Produces: ''
      Routing: ''
      Interpreted By: ''
      Semantic Status: ''
      Interface: ''
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: NONE IDENTIFIED
      Step: ''
      Direction (INPUT, OUTPUT): ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  interface_fields:
    columns:
    - Artifact
    - Direction (INPUT, OUTPUT, ATTRIBUTE)
    - Field
    - Type
    - Required (YES, NO)
    - Default
    - Meaning
    rows:
    - Artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: design_registers
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: Parsed P7 registers — the design semantics
    - Artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: mandate_registers
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: Parsed P8 registers — the build order
    - Artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: artifacts
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: One entry per artifact — path, domain, and the Machine block
    - Artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: documents
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The same artifacts as {path, text} — what persistence is handed
    - Artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: artifact_count
      Type: integer
      Required (YES, NO): 'YES'
      Default: —
      Meaning: How many artifacts were rendered
    - Artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: sources
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: For each leaf of each rendered artifact, the register it was read from or the authority it defers to. The fact the measure needs and could not previously obtain.
    - Artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: design_registers
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: Parsed P7 registers — the design semantics
    - Artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: mandate_registers
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: Parsed P8 registers — the build order
    - Artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: threshold
      Type: number
      Required (YES, NO): 'YES'
      Default: —
      Meaning: Minimum Construction Completeness; 100 unless a caller deliberately relaxes it
    - Artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: provenance
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: One origin per leaf, as the provenance transform reported it. What the test is applied to.
    - Artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: completeness
      Type: number
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The proportion of leaves whose reported origin admits a design
    - Artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: determined
      Type: integer
      Required (YES, NO): 'YES'
      Default: —
      Meaning: How many leaves the design determined
    - Artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: required
      Type: integer
      Required (YES, NO): 'YES'
      Default: —
      Meaning: How many leaves construction needs
    - Artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: undetermined
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The leaves the design did not determine, each with the origin reported for it
    - Artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: rendered
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: One rendered artifact, as the renderer produced it.
    - Artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: sources
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: For each leaf the renderer wrote, the register it read or the authority it deferred to.
    - Artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: provenance
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: One origin per leaf, drawn from the vocabulary of origins.
    - Artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: governing_artifacts
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: 'For each leaf whose origin is governed elsewhere, the artifact that governs it. Not named `governed_by`: that key is reserved for an artifact''s own authority, and a step output spelled the same is read as one.'
    - Artifact: transformation::VOCAB_FACT_PROVENANCE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: symbols
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: Each admissible origin, what it means, and whether a design carrying it is complete.
  implementation_bindings:
    columns:
    - CT Code
    - Module
    - Callable
    - Operation
    - Kind (atom, molecule)
    - Purity (ct_pure, ct_impure)
    - Refusal (raises, returns, never)
    - Source Finding
    rows:
    - CT Code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
      Module: transformation.implementation.capability_transforms.atoms.ct_pure_attribute_provenance_v0
      Callable: execute
      Operation: ATTRIBUTE_PROVENANCE
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): returns
      Source Finding: S7 new_artifacts CT_PURE_ATTRIBUTE_PROVENANCE_V0
    - CT Code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Module: transformation.implementation.capability_transforms.atoms.ct_pure_render_artifacts_v0
      Callable: execute
      Operation: PURE_RENDER_ARTIFACTS
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: S7 existing_inventory CT_PURE_RENDER_ARTIFACTS_V0
    - CT Code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
      Module: transformation.implementation.capability_transforms.atoms.ct_pure_measure_completeness_v0
      Callable: execute
      Operation: PURE_MEASURE_COMPLETENESS
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): raises
      Source Finding: S7 existing_inventory CT_PURE_MEASURE_COMPLETENESS_V0
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Group
    - Casing
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: transformation::VOCAB_FACT_PROVENANCE_V0
      Extends: NONE
      Group: fact_provenance
      Casing: lower_snake
      Value: stated_by_design
      Meaning: A register of the design carries the value. The design determines the fact, and a design carrying only these is complete.
      Source Finding: 'S7 design_resolution #2'
    - Vocabulary Code: transformation::VOCAB_FACT_PROVENANCE_V0
      Extends: NONE
      Group: fact_provenance
      Casing: lower_snake
      Value: governed_elsewhere
      Meaning: A constitution fixes the value, and the artifact that fixes it is named. The design need not state it, and a design carrying these is complete.
      Source Finding: 'S7 design_resolution #5'
    - Vocabulary Code: transformation::VOCAB_FACT_PROVENANCE_V0
      Extends: NONE
      Group: fact_provenance
      Casing: lower_snake
      Value: carried_from_predecessor
      Meaning: The artifact already carried the value and no register of the design can express it — a prose description is the case. Preserving is not authoring, so a design carrying these is complete.
      Source Finding: 'S7 design_resolution #3'
    - Vocabulary Code: transformation::VOCAB_FACT_PROVENANCE_V0
      Extends: NONE
      Group: fact_provenance
      Casing: lower_snake
      Value: supplied_by_renderer
      Meaning: The renderer wrote the value from its own text or from a fallback, and nothing governs it. A design carrying one of these is not complete.
      Source Finding: 'S7 design_resolution #4'
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows:
    - RB Code: NONE IDENTIFIED
      Capability: ''
      Key: ''
      Value: ''
      Source Finding: ''
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: transformation::VOCAB_FACT_PROVENANCE_V0
      Property: governed_by
      Value: vocabulary::CONSTITUTION_VOCABULARY_V0
      Source Finding: S7 new_artifacts VOCAB_FACT_PROVENANCE_V0
    - Artifact: transformation::VOCAB_FACT_PROVENANCE_V0
      Property: concern
      Value: build
      Source Finding: 'S6 ownership #3'
    - Artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
      Property: concern
      Value: build
      Source Finding: 'S6 ownership #1'
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: NONE IDENTIFIED
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): ''
      Proposed Path: ''
      Used By: ''
      Source Finding: ''
  transport_bindings:
    columns:
    - Artifact
    - Direction (INGRESS, EGRESS)
    - Operation
    - Handler Kind (WF_INVOCATION, SNAPSHOT_READ)
    - Handler Target
    - Field
    - Bound To
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Direction (INGRESS, EGRESS): ''
      Operation: ''
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): ''
      Handler Target: ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: build
      Count: '2'
      Artifacts: transformation::CT_PURE_RENDER_ARTIFACTS_V0, transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: build
      Count: '2'
      Artifacts: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0, transformation::VOCAB_FACT_PROVENANCE_V0
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Generator: ''
      Generator Sources: ''
      Source Finding: ''
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: NONE IDENTIFIED
      Consults: ''
      Source Finding: ''
  refusal_discharge:
    columns:
    - Operation
    - Refused When
    - Act
    - Step
    - Outcome
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Act: ''
      Step: ''
      Outcome: ''
      Source Finding: ''
  refusal_deferrals:
    columns:
    - Operation
    - Refused When
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Operation: Rendering an artifact
      Refused When: The design does not state a fact the artifact carries
      Deferred To: design
      Until: The register that carries a vocabulary's values gains the columns for its group and its spelling. Until then a design scheduling a vocabulary reads short, which is the refusal working rather than failing.
      Source Finding: 'S1 operation_refusals #1'
    - Operation: Writing a construction
      Refused When: An artifact was produced that the mandate did not schedule
      Deferred To: build
      Until: 'Carried by this change: construction stops founding a build manifest, so nothing is produced outside a mandate. Recorded as a deferral because founding a domain the compiler can discover has no replacement yet.'
      Source Finding: 'S1 operation_refusals #2'
    - Operation: Rendering an artifact
      Refused When: Its domain would have to be inferred from where a file or a dossier sits
      Deferred To: build
      Until: 'Carried by this change: the only fact ever derived from an identity was the manifest''s domain, and the manifest leaves construction with it.'
      Source Finding: 'S1 operation_refusals #3'
  refusal_governance_discharge:
    columns:
    - Operation
    - Refused When
    - Phase
    - Governing Rule
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Phase: ''
      Governing Rule: ''
      Source Finding: ''
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
