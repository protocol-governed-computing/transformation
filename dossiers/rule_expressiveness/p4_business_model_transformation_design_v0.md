# Stage 4 — Business Model: transformation / design
**Stage:** 4 — Business Model
**CR:** rule_expressiveness
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Author | Drives a change through the phases and writes the documents each requires. | Proposing — never decides admissibility. | S1 business_vocabulary #1 |
| Phase | Judges a document against the rule set it declares and renders a verdict. | Deciding — the sole arbiter of whether a document proceeds. | S1 business_vocabulary #1 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Phase | One step a change passes through, declaring a rule set and rendering a verdict. | Nine declared artifacts, one per phase. | S2 entities #1 |
| Rule | A single thing a phase requires, judged mechanically. | Declared inside the phase that requires it. | S2 entities #2 |
| Check kind | A way of judging that rules are written in. | Not an artifact. It exists where the judging is carried out. | S2 entities #3 |
| Register | A table in a document, carrying rows of one sort. | Declared by the phase that requires it. | S2 entities #4 |
| Classification | What kind of change a change request is. | A register of the change request. | S2 entities #5 |
| Span | The set of subdomains one change touches. | Nothing holds it; it is derived from the classifications. | S2 entities #6 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The dossiers already judged | Five exist against these phases and are the regression surface of this change. | S3 dependency_discoveries #8 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A document was judged | A document is checked against a phase's rule set | The verdict and its findings are what the lifecycle produces. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Classification | applies to | Subdomain | Stating which subdomain a classification applies to. | S3 authoring_decisions #1 |
| Change | touches | Span | Deriving the span of a change from its classifications. | S3 authoring_decisions #2 |
| Phase | requires | Purpose | Requiring a purpose for every subdomain a change touches. | S3 authoring_decisions #3 |
| Phase | requires | Owner | Requiring an owner for every subdomain a change touches. | S3 authoring_decisions #4 |
| Change | alters | Dependency | Recording a dependency that exists and is altered. | S3 authoring_decisions #5 |
| Rule | constrains | Register | Counting a register's rows. | S3 authoring_decisions #6 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Stating which subdomain a classification applies to | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The correction everything else follows from. |
| Deriving the span of a change from its classifications | S3 authoring_decisions #2 | CRITICAL | GAP-2 | Derived, never declared twice. |
| Requiring a purpose for every subdomain a change touches | S3 authoring_decisions #3 | CRITICAL | GAP-3 | Possible only once the span is stated. |
| Requiring an owner for every subdomain a change touches | S3 authoring_decisions #4 | CRITICAL | GAP-4 | The same. |
| Recording a dependency that exists and is altered | S3 authoring_decisions #5 | CRITICAL | GAP-5 | A fifth way of disposing of a dependency. |
| Counting a register's rows | S3 authoring_decisions #6 | CRITICAL | GAP-6 | A new way of judging, so the constraint can be written at all. |
| Applying a row count to any register | S3 authoring_decisions #7 | SATISFIED | | None is applied. The ability is what was missing. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| design | design | capability call | GAP | S3 analysis_findings Q3 — the two new requirements depend on the span being stated first. |
| design | build | data read | SATISFIED | S1 governance_scope #2 — the construction half is adjacent and untouched. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | A rule can only be written if some way of judging can express it. | S1 business_invariants #1 | invariant |
| 2 | Every subdomain a change touches has its purpose stated and its owner declared. | S1 business_invariants #2 | invariant |
| 3 | The span of a change is derived from what its classifications say, and stated nowhere else. | S1 business_invariants #3 | invariant |
| 4 | A phase judges documents only against rules it declares. | S1 business_invariants #4 | invariant |
| 5 | No existing verdict may change except where one of the three gaps caused it. | S1 constraints #1 | governance rule |
| 6 | Applying a row-count constraint to any register is a separate judgement, and none is made here. | S1 constraints #2 | governance rule |
| 7 | Only the phases that judge a design are touched. | S1 constraints #3 | governance rule |
| 8 | A change may carry more than one classification. | S1 known_facts #2 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Stating which subdomain a classification applies to | design | EXTEND |
| GAP-2 | S3 authoring_decisions #2 | Deriving the span of a change from its classifications | design | NEW |
| GAP-3 | S3 authoring_decisions #3 | Requiring a purpose for every subdomain a change touches | design | NEW |
| GAP-4 | S3 authoring_decisions #4 | Requiring an owner for every subdomain a change touches | design | NEW |
| GAP-5 | S3 authoring_decisions #5 | Recording a dependency that exists and is altered | design | EXTEND |
| GAP-6 | S3 authoring_decisions #6 | Counting a register's rows | design | NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The subdomain a classification applies to is carried on the classification itself. | S3 analysis_findings Q1 | A classification and a separately declared list of subdomains are two statements of one thing and can disagree. | Rules out a separate register of subdomains touched, and rules out a classification meaning "several subdomains". |
| 2 | The span of a change is derived, never declared. | S3 analysis_findings Q2 | Derivation has no second source to drift from. | Nothing may declare a span, and no rule may read one that was declared. |
| 3 | The two new requirements are consequences of the span being stated, and are ordered after it. | S3 analysis_findings Q3 | Neither is expressible until a phase knows which subdomains a change touches. | Rules out correcting either in isolation. |
| 4 | A dependency that exists and is altered is a fifth way of disposing of a dependency. | S3 analysis_findings Q4 | The register already records dispositions; the vocabulary was short by one. | Rules out a second register, which would leave one dependency recorded twice. |
| 5 | Counting a register's rows is a way of judging, added to the ways rules may be written in. | S3 analysis_findings Q5 | A rule can only be written if some way of judging can express it. | Rules out a bespoke constraint inside each register's own declaration. |
| 6 | The ability to count rows is added and applied to nothing. | S3 analysis_findings Q6 | Applying it anywhere would change a verdict; the capability and its use are separate acts. | The regression surface of this change is confined to the three corrections asked for. |
| 7 | Every dossier already judged is re-judged, and a verdict that moves for any other reason is a regression. | S3 impact_analysis #6 | Correcting what a phase requires makes documents that were admissible inadmissible. | Five dossiers must be re-judged before this change closes. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Stating which subdomain a classification applies to | GAP-1 |
| Deriving the span of a change from its classifications | GAP-2 |
| Requiring a purpose for every subdomain a change touches | GAP-3 |
| Requiring an owner for every subdomain a change touches | GAP-4 |
| Recording a dependency that exists and is altered | GAP-5 |
| Counting a register's rows | GAP-6 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Changes that span two domains rather than two subdomains | Nothing has needed it; a span that has never occurred cannot be specified honestly. |
| Applying a row count to any particular register | Each is its own judgement about what that register means. |
| Anything in the construction half of the lifecycle | Only the phases that judge a design are touched. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
