# Stage 4 — Business Model: book_library_mgmt / catalog
**Stage:** 4 — Business Model
**CR:** cr_03_catalog
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Catalog | Performs the acts, and states what each of them completed. | Declaring — an announcement is the act's own account of what it did. | S1 cr_type #1 |
| Library staff | Perform the acts the catalog admits. | Acting — unchanged by this change. | S2 actors #1 |
| The platform | Seals the moments an act announces, in order, and announces each when the act reaches its ending. | Enabling — the capability this change waited for. | S3 analysis_findings Q3 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Moment | Something the business declares occurred, stated by the act that completed it. | Six are declared; none is announced. | S2 entities #1 |
| Act | Something the catalog does as one unit, which completes or is refused. | Nine, each admitted by its own intent. | S2 entities #2 |
| Announcement | What an act states at its ending about the moments it completed. | None exists anywhere in this subdomain. | S3 analysis_findings Q2 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The six declared moments | Registered work, registered book, registered physical copy, updated bibliographic information, retired book, retired physical copy. Referenced by nothing. | S2 belief_verification #1 |
| The act that completes three | Registering a book admits a work, its first edition and that edition's first physical copy. | S3 analysis_findings Q2 |
| The capability the platform now holds | An ordered sequence announced at one ending, a repeat refused, an announcement that cannot be made reported. | S3 analysis_findings Q3 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| An act announced what it completed | An act reaching an ending it declares announcements for | The business has an account of what happened, which it has never had. | S1 business_events #1 |
| A declared moment stayed silent | An act completing a moment and stating nothing | The state this change ends; it is the present state of every act. | S2 belief_verification #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Act | announces | Moment | Announcing the three moments registering a book completes. | S3 authoring_decisions #1 |
| Act | announces | Moment | Announcing the moment each remaining act completes. | S3 authoring_decisions #2 |
| Catalog | attaches | Moment | Attaching the moment naming a registered work to the act that claims its identity. | S3 authoring_decisions #3 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Announcing the three moments registering a book completes | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The act this dossier halted for; three moments at one ending. |
| Announcing the moment each remaining act completes | S3 authoring_decisions #2 | CRITICAL | GAP-2 | Five acts, one moment each — a sequence of one. |
| Attaching the moment naming a registered work to the act that claims its identity | S3 authoring_decisions #3 | SATISFIED | | The composition decides it: one act claims the work, the other resolves it. |
| Announcing an ordered sequence at one ending | S3 dependency_discoveries #1 | SATISFIED | | The platform states the model, holds it, seals the order and keeps it. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| catalog | workflow | data read | SATISFIED | S3 dependency_discoveries #1 — the platform admits and seals what an act announces. |
| catalog | event | data read | SATISFIED | S3 dependency_discoveries #2 — all six moments are declared artifacts already. |
| catalog | catalog | capability call | SATISFIED | S3 dependency_discoveries #3 — every act exists and runs; what it lacks is the statement. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | An act announces every moment it completed, or the business has no account of what happened. | S1 constraints #1 | governance rule |
| 2 | A moment is attached to the act that completes it, never to one that merely touches the same records. | S3 analysis_findings Q1 | governance rule |
| 3 | The business is not reshaped to suit what the platform could express. | S1 constraints #2 | governance rule |
| 4 | Only moments the business already declared are announced. | S3 verification_results #4 | governance rule |
| 5 | A limitation paid in silence produces no account at all, and no check anywhere notices. | S2 belief_verification #3 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Announcing the three moments registering a book completes | catalog | EXTEND |
| GAP-2 | S3 authoring_decisions #2 | Announcing the moment each remaining act completes | catalog | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Registering a book announces three moments at one ending. | S3 authoring_decisions #1 | The act completes all three and is the only act that does. | Rules out announcing one and leaving two silent, and rules out splitting the act. |
| 2 | The order announced is the order the business completes them: the work, then the book, then the physical copy. | S3 analysis_findings Q3 | The order is normative and a reader of the account sees it; the business's own order is the one that reads correctly. | Fixes the order in the design rather than leaving it to how the composition was sealed. |
| 3 | Each remaining act announces the one moment it completes. | S3 authoring_decisions #2 | Five acts complete one moment each and can say so; a sequence of one is what the platform already ran. | Rules out leaving any declared moment silent. |
| 4 | Reinstatement announces nothing. | S3 verification_results #4 | The business declared no moment for it, and this change announces only moments the business already declared. | Rules out authoring a moment to fill a gap the business has not stated. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Announcing the three moments registering a book completes | GAP-1 |
| Announcing the moment each remaining act completes | GAP-2 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| A moment naming a reinstatement | The business has declared none; authoring one here would invent business content. |
| Refusing a declared moment that nothing announces | Its own question, and answering it here would refuse moments that are correct today. |
| A moment announced per member of a collection | A different shape; this change announces a known few, named where the act is designed. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
