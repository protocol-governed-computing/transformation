# Stage 4 — Business Model: transformation / design

**Stage:** 4 — Business Model

**CR:** semantic_change

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Design | Decides what a design may say, including that it re-points a reference. | Owning subdomain | S3 placement_decision design |
| Build | Decides whether a design may be built: compares amendments and accounts for what a replacement reaches. | Owning subdomain | S3 analysis_findings Q1 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Amendment | A change that restates an artifact under the identity it has. | Stated by a design. | S2 entities #1 |
| The Replacement | A change that gives an artifact a new identity. | Stated by a design. | S2 entities #2 |
| The Referrer | An artifact that names another. | Part of the composition. | S2 entities #3 |
| The Phase Rule Set | The rules a phase judges a document by. | Sealed in the phase's workflow. | S2 entities #4 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Design | admits | a re-point | Judge a design | S3 authoring_decisions Judge a design |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Judge a design | S3 authoring_decisions Judge a design | MAJOR | GAP-01 | Its rules admit a re-point and no withdrawal, in a new version of its workflow. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| build | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | vocabulary | SATISFIED | S3 dependency_discoveries How two declarations compare |
| design | transformation::IN_DESIGN_INTENT_SUBMITTED_V0 | intent | SATISFIED | S3 dependency_discoveries Offering a design |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | A re-point changes the one reference and nothing else in the referring artifact. | S1 constraints #1 | The business author |
| 2 | Every change that is built today and keeps its meaning is built exactly as it is today. | S1 constraints #2 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Judge a design | Judge a design | design | AUTHOR_NEW |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Construction compares every amendment, written or generated, with the composition by the platform's declaration, and refuses any change of meaning. | S3 analysis_findings Q1 | A change of meaning is a new identity. | The comparison of what an amendment loses folds into it. |
| 2 | A design that amends, replaces or re-points is refused without the composition. | S3 analysis_findings Q2 | No amendment is built uncompared. | None. |
| 3 | The design phase admits no withdrawal. | S3 analysis_findings Q3 | A withdrawal is a change of meaning. | Designs that withdrew facts are re-cut later. |
| 4 | The design phase admits a re-point; construction rewrites only the references to what the design replaces. | S3 analysis_findings Q4 | A referrer follows a replacement without restatement. | Only declared reference parts are rewritten. |
| 5 | Every live referrer of a replaced artifact is replaced, amended or re-pointed by the design. | S3 analysis_findings Q5 | What a replacement reaches is accounted for before it is built. | A referrer in another domain moves first. |
| 6 | Inspection answers who refers to an artifact from the record of references. | S3 analysis_findings Q6 | Every referrer is reported. | None. |
| 7 | The workflow that judges a design is replaced by a new version, and its intent re-pointed by hand. | S3 analysis_findings Q7; S3 analysis_findings Q8 | This change follows the rule it builds. | The generator maps the design phase to the new version. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Judge a design | GAP-01 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| NONE IDENTIFIED | |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · constraints · business_invariants · authority_boundaries · out_of_scope |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · pps_baseline_fqdns |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
