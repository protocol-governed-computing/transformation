# Stage 4 — Business Model: transformation / design
**Stage:** 4 — Business Model
**CR:** generated_artifacts
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Author | Drives a change and writes the documents each phase requires. | Proposing — never decides admissibility. | S1 business_vocabulary #6 |
| Generator | Produces an artifact from what determines it. | Authoritative over the artifact it produces. | S1 business_vocabulary #3 |
| Build | Refuses when an artifact and its generator disagree. | Deciding — the sole arbiter of agreement. | S1 business_vocabulary #5 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Generated artifact | One a tool produces from something else, carrying a copy of what determines it. | Nine, one per phase. | S2 entities #1 |
| Generator | What an artifact is produced from, with the mechanism that produces it. | A template and a declaration, read together. | S2 entities #2 |
| Provenance | The record of which generator an artifact came from. | Nothing holds it. | S2 entities #4 |
| Agreement | Whether an artifact still matches what generated it. | Checkable, and required by no build. | S2 entities #5 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The nine phase workflows | The artifacts this change makes governable. Each carries a sealed rule set produced from elsewhere. | S2 belief_verification #1 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| An artifact was regenerated | A generator is invoked and its artifact rewritten | The artifact and its generator agree again. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Generated artifact | declares | Provenance | Stating, on an artifact, that it is generated and by what. | S3 authoring_decisions #1 |
| Design | names | Generator | Naming, in a design, the generator an artifact is reached by. | S3 authoring_decisions #2 |
| Construction | invokes | Generator | Reaching a generated artifact by invoking its generator. | S3 authoring_decisions #3 |
| Build | refuses | Disagreement | Refusing a build when an artifact and its generator disagree. | S3 authoring_decisions #4 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Stating, on an artifact, that it is generated and by what | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The fact belongs to the artifact, not to the tool that writes it. |
| Naming, in a design, the generator an artifact is reached by | S3 authoring_decisions #2 | CRITICAL | GAP-2 | One more thing said about an artifact the design already describes. |
| Reaching a generated artifact by invoking its generator | S3 authoring_decisions #3 | CRITICAL | GAP-3 | The only arrangement with a single producer. |
| Refusing a build when an artifact and its generator disagree | S3 authoring_decisions #4 | CRITICAL | GAP-4 | The check exists and reports correctly; nothing acts on it. |
| Delivering this change by hand, once, and recording it | S3 authoring_decisions #5 | CRITICAL | GAP-5 | The last change requiring an exception. |
| Reporting whether an artifact agrees with its generator | S3 dependency_discoveries #2 | SATISFIED | | Exists, reports per artifact, returns non-zero. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| design | design | capability call | GAP | S3 analysis_findings Q2 — construction cannot invoke what a design cannot name. |
| design | build | data read | SATISFIED | S1 governance_scope #2 — the construction half is adjacent and its rendering is extended, not replaced. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | A generator is authoritative over the artifact it produces. | S1 business_invariants #1 | invariant |
| 2 | An artifact and the generator that produced it agree, and the build refuses when they do not. | S1 business_invariants #2 | invariant |
| 3 | One artifact has one generator. | S1 business_invariants #3 | invariant |
| 4 | A change to a generated artifact is delivered by changing its generator. | S1 business_invariants #4 | invariant |
| 5 | A generated artifact is never edited directly. | S1 constraints #1 | governance rule |
| 6 | Construction may not become a second producer of an artifact a generator already produces. | S1 constraints #2 | governance rule |
| 7 | No verdict changes for an authored artifact. | S1 constraints #3 | governance rule |
| 8 | A template and the declaration it is read with are one generator, not two. | S1 known_facts #5 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Stating, on an artifact, that it is generated and by what | design | NEW |
| GAP-2 | S3 authoring_decisions #2 | Naming, in a design, the generator an artifact is reached by | design | EXTEND |
| GAP-3 | S3 authoring_decisions #3 | Reaching a generated artifact by invoking its generator | design | EXTEND |
| GAP-4 | S3 authoring_decisions #4 | Refusing a build when an artifact and its generator disagree | design | EXTEND |
| GAP-5 | S3 authoring_decisions #5 | Delivering this change by hand, once, and recording it | design | NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Provenance is stated on the artifact. | S3 analysis_findings Q1 | Whether an artifact is generated is a fact about that artifact. Held elsewhere it is a second statement of one truth, able to disagree with the thing it describes. | Rules out a list held by the tool — which is what exists, and why nothing else can know. |
| 2 | A design schedules the artifact and names the generator as the means. | S3 analysis_findings Q2 | The artifact is what enters a composition; a generator never does. | Rules out scheduling a generator, and rules out a second register describing the same artifact. |
| 3 | Construction invokes the generator. | S3 analysis_findings Q3 | The only arrangement with a single producer. | Rules out refusing outright, which leaves delivery ungoverned; rules out rendering directly, which creates a second producer. |
| 4 | The existing agreement check is required, not replaced. | S3 analysis_findings Q4 | It exists and reports correctly. What is missing is that nothing acts on it. | Rules out writing a second checker of one property — the defect this change exists to prevent. |
| 5 | A template and its declaration are one generator. | S3 analysis_findings Q6 | Neither determines the artifact alone. | Rules out naming either separately, which would permit regenerating from a stale pairing. |
| 6 | This change is delivered by hand, once, and recorded as the last such exception. | S3 analysis_findings Q5 | The path it creates does not exist until it is delivered. | Rules out waiting for the capability, which is circular; rules out delivering silently, which happened twice and was explained once. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Stating, on an artifact, that it is generated and by what | GAP-1 |
| Naming, in a design, the generator an artifact is reached by | GAP-2 |
| Reaching a generated artifact by invoking its generator | GAP-3 |
| Refusing a build when an artifact and its generator disagree | GAP-4 |
| Delivering this change by hand, once, and recording it | GAP-5 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Generated artifacts outside this lifecycle | Nothing outside it is generated yet. |
| Whether a design can state an artifact it amends | A separate problem with its own change. |
| How a document authored under one rule set is judged under a later one | A separate problem with its own change. |
| Judging whether generating an artifact is a good idea | It is done today; this change governs it rather than judging it. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
