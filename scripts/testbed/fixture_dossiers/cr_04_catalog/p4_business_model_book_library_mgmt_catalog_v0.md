# Stage 4 — Business Model: book_library_mgmt / catalog
**Stage:** 4 — Business Model
**CR:** cr_04_catalog
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Catalog | States what each of its operations needs, and decides whether a request may proceed. | Declaring — what an operation requires is the catalog's own account of what it does. | S1 authority_boundaries #1 |
| Library staff | Make the requests the catalog admits or turns away. | Acting — unchanged by this change. | S2 entities #2 |
| The library's authorisation rules | Decide who may perform each operation. | Deciding — stated separately from what an operation needs, and untouched. | S2 belief_verification #4 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Operation | Something a librarian asks the catalog to do. | Ten are declared for this subdomain, each with a boundary and a workflow. | S2 entities #1 |
| Requirement | Something an operation states a request must supply. | Declared at the operation's boundary, as a name and the form the value takes. | S2 entities #3 |
| Use | A step of the operation reading something the request supplied. | Declared in the operation's own steps. | S2 entities #4 |
| Request | One asking, with what the librarian supplied. | Not held; it is what arrives at the boundary. | S2 entities #2 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The three boundaries being corrected | Registering a further edition, correcting bibliographic information, and registering a work. | S3 analysis_findings #1 |
| The seven boundaries that already agree | Registering a physical copy, retiring and reinstating a book record and a physical copy, retrieving book details, and searching the catalog. | S2 architectural_observations #1 |
| The library's end-to-end exercise of the catalog | Registering a work, adding two further editions, correcting a legacy record. Stops today at the second edition. | S3 verification_results #6 |
| The four statements of a publication year's form | Three boundaries and the description supplied with each request. Three say number; one says word. | S3 analysis_findings #3 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A request was admitted | A librarian supplying what the operation needs | The operation proceeds and the catalog changes. | S1 business_events #1 |
| A request was turned away | Something the operation needs being missing or in the wrong form | The librarian is told before anything happened, and the catalog is unchanged. | S1 business_events #2 |
| A correct request was turned away | A boundary requiring something its operation does not use, or requiring it in a form the catalog does not hold | The state this change ends. It is the present state of two of the ten operations. | S1 lifecycle_states #3 |
| A request was admitted that the operation could not carry out | A boundary requiring less than its operation reads | Latent in registering a work; the failure appears part-way through instead of at the boundary. | S2 gaps #3 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Operation | requires | Requirement | Admitting a request to register a further edition. | S3 authoring_decisions #1 |
| Operation | requires | Requirement | Admitting a request to correct bibliographic information. | S3 authoring_decisions #2 |
| Operation | requires | Requirement | Admitting a request to register a work — deferred; the requirement it lacks is one every present caller sends elsewhere. | S3 authoring_decisions #3 |
| Operation | uses | Requirement | Agreement between what an operation requires and what its steps read. | S3 analysis_findings #2 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Admitting a request to register a further edition | S3 authoring_decisions #1 | CRITICAL | GAP-1 | Turns away every correct request today; the library's exercise stops here. |
| Admitting a request to correct bibliographic information | S3 authoring_decisions #2 | CRITICAL | GAP-2 | Turns away every correction today. |
| Admitting a request to register a work | S3 authoring_decisions #3 | DEFERRED |  | A real defect of the same kind, read in the other direction. Correcting it moves a caller, which this change's seed forbids. |
| Deciding who may perform an operation | S3 dependency_discoveries #3 | SATISFIED | | Declared uniformly across all ten operations and untouched. |
| The three operations | S3 authoring_decisions #4 | SATISFIED | | No step is added, removed or rebound; each operation is correct. |
| Holding what the catalog knows | S3 dependency_discoveries #4 | SATISFIED | | Six stores, unchanged; no held record is migrated or revalidated. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| catalog | catalog | capability call | SATISFIED | S3 dependency_discoveries #2 — all three operations already run and already read what they read. |
| catalog | intent | data read | SATISFIED | S3 dependency_discoveries #1 — all three boundaries are declared artifacts of this subdomain. |
| catalog | structure | data read | SATISFIED | S3 dependency_discoveries #4 — the six stores are declared and unchanged. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | An operation requires only what it uses, and uses only what it requires. | S3 analysis_findings #2 | governance rule |
| 2 | Nothing about who may perform an operation changes. | S1 constraints #2 | governance rule |
| 3 | The records the catalog already holds are not migrated, rewritten or revalidated. | S1 constraints #3 | governance rule |
| 4 | A publication year is stated as a number wherever an operation asks for one. | S1 constraints #4 | governance rule |
| 5 | No correct request becomes harder to make. | S3 analysis_findings #1 | governance rule |
| 6 | The form of a detail the catalog holds is settled by no artifact, so agreement among the statements of it is the only authority available. | S3 analysis_findings #3 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Admitting a request to register a further edition | catalog | EXTEND |
| GAP-2 | S3 authoring_decisions #2 | Admitting a request to correct bibliographic information | catalog | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Registering a further edition states the publication year as a number. | S3 authoring_decisions #1 | Three of the four statements of the form say number, and every year the library supplies is a number. | Rules out changing the operation to accept a word, and rules out leaving the form to whichever statement is read first. |
| 2 | Correcting bibliographic information withdraws the title, the author and the publication year. | S3 authoring_decisions #2 | No step of the correction reads any of the three, and a correction that restates the fields it leaves alone is not a correction. | Rules out making the operation read them to justify requiring them. |
| 3 | Registering a work is not corrected here. | S3 authoring_decisions #3 | The act reads the subject at the top of the request and every present caller sends it nested inside the details of the book, so requiring it makes every present request fail. Constraint 5 forbids exactly that. | Rules out correcting a boundary whose correction moves a caller, and fixes that the defect is deferred intact rather than dropped. |
| 4 | No step of any of the three operations changes. | S3 authoring_decisions #4 | What each operation does is correct; it is the boundary above it that is wrong. | Rules out rewriting the operations, and confines the change to three declarations. |
| 5 | The change is one act over three boundaries, not three unrelated corrections. | S3 analysis_findings #2 | All three break one invariant, read in both directions; stating it one-sidedly is what let the third survive. | Rules out completing the change with two of the three corrected. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Admitting a request to register a further edition | GAP-1 |
| Admitting a request to correct bibliographic information | GAP-2 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Admitting a request to register a work | The act reads the subject at the top of the request and every present caller sends it nested inside the details of the book. Requiring it moves the boundary and every caller together, which this change's seed forbids. Its own CR, where both move at once. |
| Comparing what an operation requires against what it uses | Nothing performs it in the composition. Whether it belongs to this subdomain or to the platform is not this change's to settle. |
| Declaring the form of a detail the catalog holds | The store declares paths and no forms. Giving the catalog an authority over forms is a larger change than bringing one boundary into agreement with three statements. |
| The operations of subdomains and domains other than the catalog | Each is its own business, and the same comparison reports findings elsewhere that were not examined here. |
