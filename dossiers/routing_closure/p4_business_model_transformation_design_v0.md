# Stage 4 — Business Model: transformation / design

**Stage:** 4 — Business Model

**CR:** routing_closure

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The author of a change | Offers a document for a phase to judge. Unchanged by this change. | Ordinary participant | S2 business_processes #1 |
| Design | Judges each document, and rejects one whose observation found nothing. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Phase | One stage a document passes through. | Declared once and carried by its workflow. | S2 entities #1 |
| The Observation | A question a phase asks the composition. | Asked of one governed capability. | S2 entities #2 |
| The Judgement | A phase's verdict, judged or rejected. | Recorded in the trace, unchanged. | S2 entities #3 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | A phase announces nothing new. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Design | answers | every way an observation can answer | Answer every way an observation can answer | S3 authoring_decisions Answer every way an observation can answer |
| Design | rejects | a judgement whose observation found nothing | Reject a judgement whose observation found nothing | S3 authoring_decisions Reject a judgement whose observation found nothing |
| Design | generates | the answers and the routing | Generate the answers and the routing | S3 authoring_decisions Generate the answers and the routing |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Answer every way an observation can answer | S3 authoring_decisions Answer every way an observation can answer | CRITICAL | GAP-01 | Eight observing steps end their contract on nothing found. |
| Reject a judgement whose observation found nothing | S3 authoring_decisions Reject a judgement whose observation found nothing | CRITICAL | GAP-02 | Seven phases route it to the rejected ending. |
| Generate the answers and the routing | S3 authoring_decisions Generate the answers and the routing | CRITICAL | GAP-03 | The generator writes both, from what the capability and the contracts declare. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| design | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | amended contract | SATISFIED | S3 dependency_discoveries The judging contracts |
| design | transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 | amended contract | SATISFIED | S3 dependency_discoveries The judging contracts |
| design | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | platform capability | SATISFIED | S3 dependency_discoveries The observing capability |
| design | transformation::CC_JUDGE_DOCUMENT_V0 | capability contract | SATISFIED | S3 dependency_discoveries Judging a document alone |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Every judgement on observations that succeed is unchanged. | S1 constraints #1 | The business author |
| 2 | No phase gains an ending. | S1 constraints #2 | The business author |
| 3 | The answers are generated, not written beside the generator. | S1 constraints #3 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Answer every way an observation can answer | Answer every way an observation can answer | design | EXTEND |
| GAP-02 | S3 authoring_decisions Reject a judgement whose observation found nothing | Reject a judgement whose observation found nothing | design | EXTEND |
| GAP-03 | S3 authoring_decisions Generate the answers and the routing | Generate the answers and the routing | design | EXTEND |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Each observing step ends its contract on any answer but success. | S3 analysis_findings Q1 | A phase must not judge against an observation that did not arrive. | Every observing step answers every outcome its capability declares. |
| 2 | Each judging contract declares every outcome its steps can end it with. | S3 analysis_findings Q2 | A contract states how it can end. | No contract ends with an outcome it does not declare. |
| 3 | Each phase workflow routes every outcome its judging contract declares; SUCCESS keeps its ending, and every other outcome is rejected. | S3 analysis_findings Q3 | A phase judges or rejects. | Every outcome a judging contract declares has a route. |
| 4 | The generator writes the answers, the declared outcomes and the routing. | S3 analysis_findings Q4 | A hand-kept copy falls behind the thing it copies. | `tc phase emit --check` refuses a build in which an artifact and the generator disagree. |
| 5 | The capability's outcomes are held once in the generator, and the compiler checks them against the declaration. | S3 analysis_findings Q5 | The declarations are not shipped with the platform's package. | Once the platform's step check is in place, a step whose answers disagree with its capability does not compile. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Answer every way an observation can answer | GAP-01 |
| Reject a judgement whose observation found nothing | GAP-02 |
| Generate the answers and the routing | GAP-03 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Reading the capability's outcomes from its declaration | The platform's declarations are not shipped with its package; the compiler checks the copy. |

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
