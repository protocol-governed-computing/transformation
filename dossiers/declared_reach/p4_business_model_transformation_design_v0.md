# Stage 4 — Business Model: transformation / design
**Stage:** 4 — Business Model
**CR:** declared_reach
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Design | States the bindings an act owns and the ones it consults. | Declaring — it is where a reviewer reads what an act reaches. | S1 business_vocabulary #6 |
| Rule set | Refuses a design that reads what it never declared, or declares what it never reads. | Refusing — the phase's authority. | S1 cr_type #1 |
| Composition | Answers which records a binding covers and which a capability reads. | Publishing — the facts a rule derives from. | S2 architectural_observations #1 |
| Construction | Emits the reach into the built act. | Rendering — what a design states is what the act carries. | S1 requested_outcomes #2 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Reach | An act reading records another part of the business owns. | The platform carries one; no design states one. | S2 entities #2 |
| Binding | What connects an act to the descriptions of the records it works against. | One per act in a design. | S2 entities #3 |
| Consulted | The records an act reads and never writes. | Nothing in a design says which these are. | S2 entities #5 |
| Derivation | A fact read from the composition rather than restated. | Used by several rules already. | S2 entities #6 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The three published surfaces | Stores with their bindings, contracts with their steps, operations with their effects — everything the new rules derive from. | S3 analysis_findings Q3 |
| The blocked change request | Raised, pinned to this composition, and stopped where it would state a reach. | S2 belief_verification #3 |
| The eight designs already written | Unchanged by this change: an act declaring no reach is judged exactly as today. | S3 impact_analysis #4 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A design declared a reach | A design states a binding its act consults | The act's whole storage surface is visible before anything is built. | S1 business_events #1 |
| A design was refused for an undeclared read | A design's act reads records it declared no reach to | The defect is caught where a reviewer sees it rather than when the act runs. | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Design | states | Reach | Stating the bindings an act consults. | S3 authoring_decisions #1 |
| Design | names | Binding | Naming a binding and deriving its records. | S3 authoring_decisions #2 |
| Rule set | refuses | Reach | Refusing a design whose act reads records it declared no reach to. | S3 authoring_decisions #3 |
| Rule set | refuses | Reach | Refusing a reach no read uses. | S3 authoring_decisions #4 |
| Composition | hands | Derivation | Passing the store surface to the phase that judges a design. | S3 authoring_decisions #5 |
| Construction | emits | Reach | Emitting the reach into the built act. | S3 authoring_decisions #6 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Stating the bindings an act consults | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The only gap that is not a rule; everything else stands on it. |
| Naming a binding and deriving its records | S3 authoring_decisions #2 | CRITICAL | GAP-2 | What keeps this change from re-creating the copy it serves. |
| Refusing a design whose act reads records it declared no reach to | S3 authoring_decisions #3 | CRITICAL | GAP-3 | Half of one statement; permits a reserve if delivered alone. |
| Refusing a reach no read uses | S3 authoring_decisions #4 | CRITICAL | GAP-4 | The other half; permits a silent reach if delivered alone. |
| Passing the store surface to the phase that judges a design | S3 authoring_decisions #5 | CRITICAL | GAP-5 | Without it every rule above reports nothing and looks like a rule that checked. |
| Emitting the reach into the built act | S3 authoring_decisions #6 | CRITICAL | GAP-6 | Or the declaration is decoration and the act is hand-finished. |
| The published facts a rule reasons from | S3 authoring_decisions #7 | CRITICAL | GAP-7 | Declared, and one of them published in a shape no rule can consume. Without it every rule above reasons from a fact it cannot reach. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| design | design | capability call | GAP | S3 analysis_findings Q1 — one declaration and three checks that stand on it. |
| design | build | data read | GAP | S3 authoring_decisions #6 — construction emits what the design states. |
| design | inspection | data read | GAP | S3 analysis_findings Q3 — the binding identities are counted and not named on the surface a rule is handed. |
| design | runtime_binding | data read | SATISFIED | S2 belief_verification #2 — the platform admits the reach this states. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Ownership and reach are structurally distinct, never one register with a column telling them apart. | S1 constraints #1 | governance rule |
| 2 | A design names a binding and never the records behind it. | S1 constraints #2 | governance rule |
| 3 | What a rule checks is derived from the composition, never inferred from a name or an implementation. | S1 constraints #3 | governance rule |
| 4 | Every declared reach is used, and every read is declared. | S1 constraints #4 | governance rule |
| 5 | A reach is never added to a built artifact by hand. | S1 constraints #5 | governance rule |
| 6 | A reach added by hand works, passes every check, and is a reach no reviewer saw. | S1 known_facts #7 | domain knowledge |
| 7 | A rule resting on a name is a convention anybody can break by naming something well. | S1 known_facts #8 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Stating the bindings an act consults | design | NEW |
| GAP-2 | S3 authoring_decisions #2 | Naming a binding and deriving its records | design | NEW |
| GAP-3 | S3 authoring_decisions #3 | Refusing a design whose act reads records it declared no reach to | design | NEW |
| GAP-4 | S3 authoring_decisions #4 | Refusing a reach no read uses | design | NEW |
| GAP-5 | S3 authoring_decisions #5 | Passing the store surface to the phase that judges a design | design | EXTEND |
| GAP-6 | S3 authoring_decisions #6 | Emitting the reach into the built act | design | EXTEND |
| GAP-7 | S3 authoring_decisions #7 | The published facts a rule reasons from | inspection | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The reach is stated in a register of its own. | S3 authoring_decisions #1 | A column distinguishing owned from consulted would put them a typo apart, with a rule reading the column the only thing between them. | Rules out widening the existing storage register. |
| 2 | A design names a binding; its records are derived. | S3 analysis_findings Q5 | Restating another part's records inside the reaching act's design is a copy maintained by someone other than their owner — the shape the platform change refused. | Rules out stating records, and fixes what a rule derives rather than reads. |
| 3 | The two refusals are delivered together. | S3 analysis_findings Q2 | Neither half checks anything alone: one permits a reserve, the other permits a silent reach. | Rules out a smaller first pass. |
| 4 | The store surface is declared among what the design phase observes. | S3 analysis_findings Q4 | Publishing a fact and passing it to a rule are different things, and rules not passed their facts have reported nothing three times. | Makes the handover part of the change rather than an assumption. |
| 5 | What a design states is what the built act carries. | S3 authoring_decisions #6 | A declaration construction ignores is decoration, and the act would be finished by hand. | Rules out delivering the register without the renderer. |
| 6 | The change is delivered through the pipeline, naming the generator of the document it amends. | S3 analysis_findings Q6 | The document is generated, a design can name its generator, and no change ever has. | The path is exercised for the first time, and its risks belong to this change. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Stating the bindings an act consults | GAP-1 |
| Naming a binding and deriving its records | GAP-2 |
| Refusing a design whose act reads records it declared no reach to | GAP-3 |
| Refusing a reach no read uses | GAP-4 |
| Passing the store surface to the phase that judges a design | GAP-5 |
| Emitting the reach into the built act | GAP-6 |
| The published facts a rule reasons from | GAP-7 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Which acts reach which records | Each domain's business, stated in its own change. |
| Whether a reach may cross a domain | Settled by the platform: it may not. |
| Refusing a design whose act writes through a reach | The platform refuses it when the act runs; whether the design layer should refuse it earlier is its own question. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
