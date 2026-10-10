# Stage 4 — Business Model: transformation / build
**Stage:** 4 — Business Model
**CR:** quoted_literals
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Construction | Renders each artifact from what the design states. | Rendering — decides nothing about what a design contains. | S1 authority_boundaries #1 |
| Design | States what a literal is and which value each binding fixes. | Declaring — the authority over what a literal is. | S1 authority_boundaries #2 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Binding | A design's statement of where a step's input comes from. | A row of the Design Intent's step-bindings register, rendered into the input of a node or step. | S2 entities #1 |
| Literal | A binding to a value the design fixes. | Rendered by the same reading of a value that renders a field's default and an artifact's property. | S2 entities #2 |
| Quoted literal | A literal written inside quote marks, as a value with a dot in it must be. | Rendered as its text, quote marks included. | S2 entities #3 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The reproduction of every delivered artifact | The acceptance test: every artifact construction reproduces today reproduces unchanged. | S3 dependency_discoveries #4 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A binding was rendered | Construction produces an artifact from a design | The artifact carries the value the design states. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Construction | renders | Quoted literal | Rendering a quoted literal as the value inside its quotes. | S3 authoring_decisions #1 |
| Construction | renders | Literal | Rendering a decimal number as a number. | S3 authoring_decisions #2 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Rendering a quoted literal as the value inside its quotes | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The rendering of a binding alone. |
| Rendering a decimal number as a number | S3 authoring_decisions #2 | CRITICAL | GAP-2 | The same. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| build | design | data read | SATISFIED | S1 governance_scope #2 — construction reads the design; what a literal is stays the design's. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | The runtime receives the value a design states. | S1 business_invariants #1 | invariant |
| 2 | No delivered artifact changes. | S1 business_invariants #2 | invariant |
| 3 | No delivered artifact changes. Every artifact construction reproduces today, it reproduces unchanged. | S1 constraints #1 | governance rule |
| 4 | The rule-effectivity change waits for this one, and resumes once it is delivered. | S1 constraints #2 | governance rule |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Rendering a quoted literal as the value inside its quotes | build | EXTEND |
| GAP-2 | S3 authoring_decisions #2 | Rendering a decimal number as a number | build | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Only the rendering of a binding changes. | S3 analysis_findings Q1 | A field's default and an artifact's property share the reading of a value and were not found wrong. | Rules out changing the shared reading. |
| 2 | A quoted literal renders as the text between its quotes; a decimal number renders as a number; every other binding renders as today. | S3 analysis_findings Q2 | No delivered binding is quoted or decimal. | Every delivered artifact reproduces unchanged. |
| 3 | No artifact is replaced or extended; the render transform's implementation is corrected. | S3 analysis_findings Q3 | Its declaration states nothing about how a literal is rendered, so no declaration changes meaning. | The change schedules nothing for construction to render. |
| 4 | The keyed-node probe expects the value, not the quoted text. | S3 analysis_findings Q4 | It recorded the defect as intended. | The probe proves the correction. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Rendering a quoted literal as the value inside its quotes | GAP-1 |
| Rendering a decimal number as a number | GAP-2 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| The rule-effectivity change | It waits for this one, and resumes once it is delivered. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
