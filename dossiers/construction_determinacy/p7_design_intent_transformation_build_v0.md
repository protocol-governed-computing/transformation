# Stage 7 — Design Intent: transformation / build
**Stage:** 7 — Design Intent
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Where provenance is determined | Only the renderer knows where a value came from, because it is the thing that put it there. | A transform reports, for each leaf of each rendered artifact, one of three origins: the design stated it, a constitution governs it, or the renderer supplied it. | S6 boundary_rules PROVENANCE_IS_THE_TEST |
| What the origins are, and which admit a design | A fact a constitution fixes may be supplied; a fact nobody governs and nobody states may not. | A vocabulary carries the three origins and states which admit a design as complete: stated by the design, and governed elsewhere. Supplied by the renderer does not. | S6 boundary_rules A_FACT_HAS_A_STATED_ORIGIN |
| What the measure tests | Testing presence cannot distinguish a value the design supplied from one the renderer did. | The measure keeps walking the renderer's output leaf by leaf, and marks a leaf determined when its reported origin is one the vocabulary admits, rather than when it is non-empty. | S6 boundary_rules THE_POPULATION_STAYS_DERIVED |
| What happens to the three defaults | A design that omits a default measures complete, which is what the two literals did. | Each default reports its origin as supplied by the renderer, so a design omitting one reads short. The fallback still produces a working artifact; it no longer produces a complete measurement. | S6 boundary_rules A_DEFAULT_IS_AN_INVENTION |
| What happens to the event's moment field | The event constitution fixes it, and a design restating what a constitution settles would state it twice. | It reports its origin as governed elsewhere, naming the constitution that fixes it. The ground moves from prose beside code into a value the measure reads. | S6 boundary_rules A_FACT_HAS_A_STATED_ORIGIN |
| What happens to the two vocabulary literals | No register carries a vocabulary's group name or spelling rule. | They report as supplied by the renderer, so every design scheduling a vocabulary reads short until the design subdomain adds the columns. The register is named for its owner; it is not amended here. | S6 boundary_rules A_REGISTER_IS_EXTENDED_BY_ITS_OWNER |
| What happens to the build manifest | Every field of it is compiler configuration and no business fact determines any of them. | Construction stops writing it. Nothing replaces it in this change, and a domain the compiler cannot yet discover is a named deferral rather than a silent gap. | S6 boundary_rules NOTHING_OUTSIDE_THE_MANDATE |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | EXTEND | Render every artifact a mandate schedules from the design that determines it | Gains the reporting of an origin per leaf. Every family it renders is answerable for each value it writes. | S6 pps_artifacts_requiring_action #1 |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | EXTEND | Measure Construction Completeness and refuse a design that does not determine its artifacts | Its population is unchanged and its test changes: a leaf is determined when its reported origin admits a design, not when it is non-empty. | S6 pps_artifacts_requiring_action #2 |
| transformation::CC_PERSIST_ARTIFACTS_V0 | REVIEW | Write a rendered construction beneath the root its runtime binding declares | Its declaration is already correct: one step, writing the documents it is handed. The founding of a build manifest happens above it, in what decides which documents to hand it, so what this change removes is not stated in this artifact. | S6 pps_artifacts_requiring_action #3 |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | REVIEW | Construct protocol artifacts from an approved design and mandate | Names the three steps that measure, render and write. Unchanged in shape; two of its three steps change beneath it. | S6 pps_artifacts_requiring_action #4 |
| transformation::WF_CONSTRUCT_ARTIFACTS_V0 | REVIEW | Measure a design, refuse it if under-determined, and render the artifacts it schedules | The act is right and its routing is unchanged. Named because what it refuses becomes stricter. | S6 pps_artifacts_requiring_action #5 |
| transformation::IN_CONSTRUCTION_REQUESTED_V0 | REUSE | Offer an approved design and mandate for construction | What is offered is correct; what is done with it is not. Unchanged. | S6 pps_artifacts_requiring_action #6 |
| transformation::RB_CONSTRUCTION_BINDINGS_V0 | REUSE | Runtime bindings for the construction lifecycle | Unchanged. Named because the amended contracts are bound through it. | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | REVIEW | Phase 7 of the change pipeline: decide whether an offered design is admissible | Its vocabulary register states a value and its meaning and has no column for the group or the spelling. Named for `design` to extend; not written here. | S6 pps_artifacts_requiring_action #8 |
| vocabulary::CONSTITUTION_VOCABULARY_V0 | REVIEW | Governs what a vocabulary is and what it must declare | The artifact the platform refused was refused against a rule this constitution carries. Unchanged; named as the authority the new vocabulary is governed by. | S6 pps_artifacts_requiring_action #9 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | REVIEW | Declares what the transformation domain compiles | Unchanged; named because the amended and authored artifacts are compiled under it. | S6 ownership #1 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family | Code | Summary | Owner Subdomain | Status | Source Finding |
|-----------|--------|------|---------|-----------------|--------|----------------|
| Reporting where each rendered value came from | CT | transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | Report, for each leaf of a rendered artifact, whether the design stated it, a constitution governs it, or the renderer supplied it | build | NEW | S6 governance_outcome #1 |
| Declaring that something else governs a fact | VOCAB | transformation::VOCAB_FACT_PROVENANCE_V0 | The origins a rendered fact may have, and which of them admit a design as complete | build | NEW | S6 governance_outcome #3 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| transformation::RB_CONSTRUCTION_BINDINGS_V0 | transformation::WF_CONSTRUCT_ARTIFACTS_V0 | Unchanged | transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | S6 ownership #8 |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|-----------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| NONE IDENTIFIED |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | INPUT | design_registers | array | YES | — | Parsed P7 registers — the design semantics |
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | INPUT | mandate_registers | array | YES | — | Parsed P8 registers — the build order |
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | OUTPUT | artifacts | array | YES | — | One entry per artifact — path, domain, and the Machine block |
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | OUTPUT | documents | array | YES | — | The same artifacts as {path, text} — what persistence is handed |
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | OUTPUT | artifact_count | integer | YES | — | How many artifacts were rendered |
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | OUTPUT | sources | object | YES | — | For each leaf of each rendered artifact, the register it was read from or the authority it defers to. The fact the measure needs and could not previously obtain. |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | INPUT | design_registers | array | YES | — | Parsed P7 registers — the design semantics |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | INPUT | mandate_registers | array | YES | — | Parsed P8 registers — the build order |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | INPUT | threshold | number | YES | — | Minimum Construction Completeness; 100 unless a caller deliberately relaxes it |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | INPUT | provenance | object | YES | — | One origin per leaf, as the provenance transform reported it. What the test is applied to. |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | OUTPUT | completeness | number | YES | — | The proportion of leaves whose reported origin admits a design |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | OUTPUT | determined | integer | YES | — | How many leaves the design determined |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | OUTPUT | required | integer | YES | — | How many leaves construction needs |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | OUTPUT | undetermined | array | YES | — | The leaves the design did not determine, each with the origin reported for it |
| transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | INPUT | rendered | object | YES | — | One rendered artifact, as the renderer produced it. |
| transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | INPUT | sources | object | YES | — | For each leaf the renderer wrote, the register it read or the authority it deferred to. |
| transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | OUTPUT | provenance | object | YES | — | One origin per leaf, drawn from the vocabulary of origins. |
| transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | OUTPUT | governing_artifacts | object | YES | — | For each leaf whose origin is governed elsewhere, the artifact that governs it. Not named `governed_by`: that key is reserved for an artifact's own authority, and a step output spelled the same is read as one. |
| transformation::VOCAB_FACT_PROVENANCE_V0 | ATTRIBUTE | symbols | object | YES | — | Each admissible origin, what it means, and whether a design carrying it is complete. |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|----------------------|-----------------------------|----------------------------------|----------------|
| transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | transformation.implementation.capability_transforms.atoms.ct_pure_attribute_provenance_v0 | execute | ATTRIBUTE_PROVENANCE | atom | ct_pure | returns | S7 new_artifacts CT_PURE_ATTRIBUTE_PROVENANCE_V0 |
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | transformation.implementation.capability_transforms.atoms.ct_pure_render_artifacts_v0 | execute | PURE_RENDER_ARTIFACTS | atom | ct_pure | raises | S7 existing_inventory CT_PURE_RENDER_ARTIFACTS_V0 |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | transformation.implementation.capability_transforms.atoms.ct_pure_measure_completeness_v0 | execute | PURE_MEASURE_COMPLETENESS | atom | ct_pure | raises | S7 existing_inventory CT_PURE_MEASURE_COMPLETENESS_V0 |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|
| transformation::VOCAB_FACT_PROVENANCE_V0 | NONE | fact_provenance | lower_snake | stated_by_design | A register of the design carries the value. The design determines the fact, and a design carrying only these is complete. | S7 design_resolution #2 |
| transformation::VOCAB_FACT_PROVENANCE_V0 | NONE | fact_provenance | lower_snake | governed_elsewhere | A constitution fixes the value, and the artifact that fixes it is named. The design need not state it, and a design carrying these is complete. | S7 design_resolution #5 |
| transformation::VOCAB_FACT_PROVENANCE_V0 | NONE | fact_provenance | lower_snake | carried_from_predecessor | The artifact already carried the value and no register of the design can express it — a prose description is the case. Preserving is not authoring, so a design carrying these is complete. | S7 design_resolution #3 |
| transformation::VOCAB_FACT_PROVENANCE_V0 | NONE | fact_provenance | lower_snake | supplied_by_renderer | The renderer wrote the value from its own text or from a fallback, and nothing governs it. A design carrying one of these is not complete. | S7 design_resolution #4 |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|-----------|-----|-------|----------------|
| NONE IDENTIFIED |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| transformation::VOCAB_FACT_PROVENANCE_V0 | governed_by | vocabulary::CONSTITUTION_VOCABULARY_V0 | S7 new_artifacts VOCAB_FACT_PROVENANCE_V0 |
| transformation::VOCAB_FACT_PROVENANCE_V0 | concern | build | S6 ownership #3 |
| transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | concern | build | S6 ownership #1 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | build | 2 | transformation::CT_PURE_RENDER_ARTIFACTS_V0, transformation::CT_PURE_MEASURE_COMPLETENESS_V0 |
| NEW | build | 2 | transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0, transformation::VOCAB_FACT_PROVENANCE_V0 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| NONE IDENTIFIED |

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| NONE IDENTIFIED |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|
| Rendering an artifact | The design does not state a fact the artifact carries | design | The register that carries a vocabulary's values gains the columns for its group and its spelling. Until then a design scheduling a vocabulary reads short, which is the refusal working rather than failing. | S1 operation_refusals #1 |
| Writing a construction | An artifact was produced that the mandate did not schedule | build | Carried by this change: construction stops founding a build manifest, so nothing is produced outside a mandate. Recorded as a deferral because founding a domain the compiler can discover has no replacement yet. | S1 operation_refusals #2 |
| Rendering an artifact | Its domain would have to be inferred from where a file or a dossier sits | build | Carried by this change: the only fact ever derived from an identity was the manifest's domain, and the manifest leaves construction with it. | S1 operation_refusals #3 |

---

## 20. Refusal Governance Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|
| NONE IDENTIFIED |

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
