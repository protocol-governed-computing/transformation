# Stage 4 — Business Model: transformation / design
**Stage:** 4 — Business Model
**CR:** binding_literals
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Author | Writes a design and states where each input's value comes from. | Proposing — never decides admissibility. | S1 business_events #1 |
| Phase | Judges every binding a design states against the rules it declares. | Deciding — the sole arbiter of whether a design is admissible. | S1 authority_boundaries #1 |
| Generator | Produces an artifact in place of construction, determining the values the design says it does. | Determining — only what the design names it for. | S1 authority_boundaries #2 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Binding | A design's statement of where a step's input comes from. | A row of the Design Intent's step-bindings register: an owner, a step, a direction, a field and a source. | S2 entities #1 |
| Reference | A binding to a value the runtime offers: the starting intent, the contract's own inputs, or an earlier step's result. | A source rooted in one of five names the runtime offers. | S2 entities #2 |
| Literal | A binding to a value the design fixes. | A source no rule roots. Two rules decide separately what counts as one. | S2 entities #3 |
| Generator | What produces an artifact in place of construction writing it. | A row of the Design Intent's generation-provenance register, naming the generator and everything it reads. | S2 entities #4 |
| Generated value | An input whose value the generator of the artifact that holds it determines. | Nothing states it. | S2 entities #5 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The Design Intent's test documents | Each new admission and the new refusal needs a document that shows it. | S3 dependency_discoveries #6 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A binding was judged | A design intent is checked | Every rule that judges a binding reads a literal the same way. | S1 business_events #1 |
| A value was declared generated | A design states that the generator determines an input | It is admitted only where the design names that generator. | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Rule | reads | Literal | Giving a literal one meaning across every rule that judges a binding. | S3 authoring_decisions #1 |
| Binding | names | Generator | Stating that a generator determines a value. | S3 authoring_decisions #2 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Giving a literal one meaning across every rule that judges a binding | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The wider definition is kept; the narrower rules are widened to it. |
| Stating that a generator determines a value | S3 authoring_decisions #2 | CRITICAL | GAP-2 | A reserved source, held to an owner listed as generated. |
| Judging a document against declared rules | S3 dependency_discoveries #5 | SATISFIED | | Applies whatever rules it is handed; unchanged. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| design | design | capability call | SATISFIED | S3 analysis_findings Q3 — the new rule is written in a way of judging that exists. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | A literal has one meaning across every rule that judges a binding. | S1 business_invariants #1 | invariant |
| 2 | A generator determines only what the design says it does. | S1 business_invariants #2 | invariant |
| 3 | No admissible design becomes inadmissible. | S1 business_invariants #3 | invariant |
| 4 | No admissible design becomes inadmissible. This correction only admits statements that were refused. It is not retroactive. | S1 constraints #1 | governance rule |
| 5 | Saying a value is generated is admissible only for an artifact the design lists as generated. | S1 constraints #2 | governance rule |
| 6 | The rule-effectivity change is parked at its governance intent and resumes against the composition this change produces. | S1 constraints #3 | governance rule |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Giving a literal one meaning across every rule that judges a binding | design | EXTEND |
| GAP-2 | S3 authoring_decisions #2 | Stating that a generator determines a value | design | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | A literal is a single word, a qualified identity, a number, or a value opening with a quote, bracket or brace, and every rule that judges a binding reads it so. | S3 analysis_findings Q1 | It is the definition the rooting rule already applies, and the widest of the three. | Rules out narrowing any rule, which would make admitted designs inadmissible. |
| 2 | Widening the narrower rules changes no admitted binding's meaning. | S3 analysis_findings Q2 | No delivered design binds a value they refuse. | The correction is declared not retroactive. |
| 3 | The source generated states that the generator of the binding's owner determines the value, and is admitted only where the owner is listed as generated. | S3 analysis_findings Q3 | A reserved source says it on the one row it concerns. | Rules out a column that most rows leave empty, and a new way of judging. |
| 4 | Reserving the word generated changes no admitted binding's meaning. | S3 analysis_findings Q4 | No delivered design binds it as a literal. | A design that means the word itself writes it quoted. |
| 5 | The Design Intent's workflow is replaced by a new version, and its intent names the successor. | S3 analysis_findings Q5 | Its sealed rule set changes, and a change of meaning is a new identity. | Rules out extending the workflow in place. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Giving a literal one meaning across every rule that judges a binding | GAP-1 |
| Stating that a generator determines a value | GAP-2 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| The rule-effectivity change | It is parked and resumes against the composition this change produces. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
