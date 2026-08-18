# Stage 4 — Business Model: book_library_mgmt / catalog

**Stage:** 4 — Business Model
**CR:** cr_02_catalog
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies: what is reused already exists, what is extended or authored is a declared gap.
Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Authorized staff | Performs every catalog operation, including the ones this change adds. | Authorized business actor | S1 authority_boundaries The judgement that an edition is obsolete |
| The catalog | Holds the authoritative record of every work, edition and physical copy. | Owning subdomain | S1 authority_boundaries Work record |
| The business author | Settles what an edition is and what identifies a work. | Business authority, outside the system | S1 authority_boundaries Whether an edition is part of a Book or a catalog entity in its own right |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Work | A published work, recognizable as one thing across the editions in which it is published, identified by its title and author. | A durable record store holding one record per work, and a registry claiming each work's identity. | S2 entities Work |
| Edition | A publication of a work, identified by title, author and publication year. The record the previous change calls a book is an edition. | The existing durable record store, unchanged. | S2 entities Edition |
| Physical Copy | An individual copy the library owns, belonging to exactly one edition. | The existing durable record store, unchanged. | S2 entities Physical Copy |
| Bibliographic Information | An edition's descriptive content. | Held within the edition's own record. | S2 entities Bibliographic Information |
| Edition Summary | Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean. | Assembled at read time; not stored. | S2 entities Edition Summary |
| Work Summary | A short description of the work an edition belongs to, carried in that edition's retrieval. | Assembled at read time; not stored. | S2 entities Work Summary |
| Existing Catalog Record | A catalog record written under the previous governed change, before this one. | The same store the edition occupies. | S2 entities Existing Catalog Record |
| Business Operation | An action performed against the catalog that must be traceable and auditable. | The existing append-only trail, unchanged. | S2 entities Business Operation |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The work store | Holds one record per work the catalog knows. | S3 authoring_decisions Hold a work record durably and update it in place |
| The work identity registry | Claims each work's identity so two registrations of one work do not produce two works. | S3 authoring_decisions Enforce that one work exists per title and author |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| Work Registered | Authorized staff register an edition of a work the catalog does not yet hold. | A work enters the catalog, created by the edition that evidences it. | S1 business_events #1 |
| Edition Registered | Authorized staff register an additional edition of an existing work. | The catalog records a further edition of a work it already holds. | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Work | is published as | Edition | Register an edition against the work it belongs to, creating the work when the catalog does not yet hold it | S3 authoring_decisions Register an edition of a work the catalog does not yet hold |
| Edition | belongs to | Work | Resolve the work a title and author denote, so a further edition can name it | S3 authoring_decisions Resolve the work an edition belongs to |
| Physical Copy | is a copy of | Edition | Register a copy against exactly one edition, unchanged from the previous change | S3 authoring_decisions Register a physical copy against exactly one edition |
| Authorized staff | searches | Work | Answer a search at the level of the work, carrying a summary of its editions | S3 authoring_decisions Search the catalog and answer at the level of the work |
| Authorized staff | retrieves | Edition | Return an edition's details, its copies, and a summary of the work it belongs to | S3 authoring_decisions Retrieve an edition's complete details with a summary of its work |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Hold a work record durably and update it in place | S3 authoring_decisions Hold a work record durably and update it in place | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Enforce that one work exists per title and author | S3 authoring_decisions Enforce that one work exists per title and author | SATISFIED |  | Reused as-is with a two-attribute key, exactly as the edition key uses it with three. |
| Form the identifying key of a work from its title and author | S3 authoring_decisions Form the identifying key of a work from its title and author | CRITICAL | GAP-01 | The edition key transform is reached by every catalog operation and is not widened. |
| Claim a work's identity so that two registrations of one work do not produce two works | S3 authoring_decisions Claim a work's identity so that two registrations of one work do not produce two works | CRITICAL | GAP-02 | Composed the way the edition claim is composed, against the work's own registry store. |
| Resolve the work an edition belongs to | S3 authoring_decisions Resolve the work an edition belongs to | CRITICAL | GAP-03 | Nothing in the composition answers which work a title and author denote. |
| Group selected records by an attribute they share | S3 authoring_decisions Group selected records by an attribute they share | CRITICAL | GAP-04 | Selection exists; grouping does not. |
| Declare the stores the catalog owns | S3 authoring_decisions Declare the stores the catalog owns | CRITICAL | GAP-05 | Extended with the work store and the work identity registry. |
| Bind the catalog's workflows to the stores they use | S3 authoring_decisions Bind the catalog's workflows to the stores they use | CRITICAL | GAP-06 | Extended so the new stores are reachable by the workflows that use them. |
| Register an edition of a work the catalog does not yet hold | S3 authoring_decisions Register an edition of a work the catalog does not yet hold | CRITICAL | GAP-07 | Gains a work claim among the claims, before any write. |
| Validate that a registration carries what a work and an edition require | S3 authoring_decisions Validate that a registration carries what a work and an edition require | CRITICAL | GAP-08 | Runs before any claim, as it does today. |
| Register an additional edition of an existing work | S3 authoring_decisions Register an additional edition of an existing work | CRITICAL | GAP-09 | The operation this change exists to add. |
| Search the catalog and answer at the level of the work | S3 authoring_decisions Search the catalog and answer at the level of the work | CRITICAL | GAP-10 | The search terms are unchanged; the shape of the answer is not. |
| Retrieve an edition's complete details with a summary of its work | S3 authoring_decisions Retrieve an edition's complete details with a summary of its work | CRITICAL | GAP-11 | Retrieval stays edition retrieval and gains the work summary. |
| Admit a request to register an additional edition of an existing work | S3 authoring_decisions Admit a request to register an additional edition of an existing work | CRITICAL | GAP-12 | A new business operation is reached through its own entry point. |
| Recognise the moment a work enters the catalog | S3 authoring_decisions Recognise the moment a work enters the catalog | CRITICAL | GAP-13 | The catalog declares a moment for each thing that enters it. |
| Confirm the staff member performing an operation is authorized | S3 authoring_decisions Confirm the staff member performing an operation is authorized | SATISFIED |  | Reused as-is; the operations this change adds reach it first, as every other does. |
| Record every performed operation in the catalog's audit trail | S3 authoring_decisions Record every performed operation in the catalog's audit trail | SATISFIED |  | Reused as-is; the trail records whatever operation it is handed. |
| Register a physical copy against exactly one edition | S3 authoring_decisions Register a physical copy against exactly one edition | SATISFIED |  | Reused as-is; nothing about copies changes. |
| Retire and reinstate an edition independently of the work's other editions | S3 authoring_decisions Retire and reinstate an edition independently of the work's other editions | SATISFIED |  | Reused as-is; retirement already cascades to nothing. |
| Update an edition's bibliographic information | S3 authoring_decisions Update an edition's bibliographic information | SATISFIED |  | Reused as-is; duplication remains an edition-level rule. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| catalog | capability_side_effects::CS_MUTABLE_JSON_V0 | capability call | SATISFIED | S3 dependency_discoveries Durable record storage for works |
| catalog | capability_side_effects::CS_REGISTRY_V0 | capability call | SATISFIED | S3 dependency_discoveries Uniqueness claim for a work's identity |
| catalog | capability_side_effects::CS_APPENDONLY_JSONL_V0 | capability call | SATISFIED | S3 dependency_discoveries The audit step every catalog operation reaches last |
| catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | data read | SATISFIED | S3 dependency_discoveries The store declaration that must carry the work stores |
| catalog | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | data read | SATISFIED | S3 dependency_discoveries The binding declaration that must bind the work stores |
| catalog | book_library_mgmt::CC_REGISTER_BOOK_V0 | capability call | SATISFIED | S3 dependency_discoveries The registration step that must claim the work |
| catalog | book_library_mgmt::CC_SEARCH_CATALOG_V0 | capability call | SATISFIED | S3 dependency_discoveries The search step whose answer must be grouped by work |
| catalog | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | capability call | SATISFIED | S3 dependency_discoveries The retrieval step that must carry a work summary |
| catalog | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | capability call | SATISFIED | S3 dependency_discoveries The authorization check every catalog operation reaches first |
| catalog | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | capability call | SATISFIED | S3 dependency_discoveries The audit step every catalog operation reaches last |
| catalog | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | capability call | SATISFIED | S3 dependency_discoveries Copy registration and barcode uniqueness |
| catalog | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | capability call | SATISFIED | S3 dependency_discoveries Retirement and reinstatement of an edition |
| catalog | staff | capability call | GAP | S1 authority_deferrals Which staff are authorized |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | No capability staff have today may be withdrawn and no existing record may become unreachable. | S1 constraints #1 | governance rule |
| 2 | Existing catalog records must remain valid without recreation or migration, demonstrated against records written under the previous change. | S1 constraints #2 | governance rule |
| 3 | Only search and retrieval may be extended; every other existing operation must behave as it does today. | S1 constraints #3 | governance rule |
| 4 | Multiple identifiers, governed subject taxonomy, digital resources and images must not be designed into this change. | S1 constraints #4 | governance rule |
| 5 | Every business operation must remain traceable and auditable. | S1 constraints #5 | invariant |
| 6 | Each edition belongs to exactly one work. | S1 business_invariants #1 | invariant |
| 7 | Each physical copy belongs to exactly one edition. | S1 business_invariants #2 | invariant |
| 8 | No two works share the same title and author. | S1 business_invariants #3 | invariant |
| 9 | No two editions of a work share the same publication year. | S1 business_invariants #4 | invariant |
| 10 | Every work has at least one edition. | S1 business_invariants #5 | invariant |
| 11 | A work is not retired; a work whose editions are all retired is simply that. | S1 operation_refusals Retire a work | domain knowledge |
| 12 | Every claim precedes every write, so a refused registration changes nothing. | S3 analysis_findings #10 | domain knowledge |
| 13 | The transform forming the edition key is not widened; the identity of the existing record does not change to serve a new one. | S3 analysis_findings #3 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Form the identifying key of a work from its title and author | Form the identifying key of a work from its title and author | catalog | NEW |
| GAP-02 | S3 authoring_decisions Claim a work's identity so that two registrations of one work do not produce two works | Claim a work's identity so that two registrations of one work do not produce two works | catalog | NEW |
| GAP-03 | S3 authoring_decisions Resolve the work an edition belongs to | Resolve the work an edition belongs to | catalog | NEW |
| GAP-04 | S3 authoring_decisions Group selected records by an attribute they share | Group selected records by an attribute they share | catalog | NEW |
| GAP-05 | S3 authoring_decisions Declare the stores the catalog owns | Declare the stores the catalog owns | catalog | EXTEND |
| GAP-06 | S3 authoring_decisions Bind the catalog's workflows to the stores they use | Bind the catalog's workflows to the stores they use | catalog | EXTEND |
| GAP-07 | S3 authoring_decisions Register an edition of a work the catalog does not yet hold | Register an edition of a work the catalog does not yet hold | catalog | EXTEND |
| GAP-08 | S3 authoring_decisions Validate that a registration carries what a work and an edition require | Validate that a registration carries what a work and an edition require | catalog | EXTEND |
| GAP-09 | S3 authoring_decisions Register an additional edition of an existing work | Register an additional edition of an existing work | catalog | NEW |
| GAP-10 | S3 authoring_decisions Search the catalog and answer at the level of the work | Search the catalog and answer at the level of the work | catalog | EXTEND |
| GAP-11 | S3 authoring_decisions Retrieve an edition's complete details with a summary of its work | Retrieve an edition's complete details with a summary of its work | catalog | EXTEND |
| GAP-12 | S3 authoring_decisions Admit a request to register an additional edition of an existing work | Admit a request to register an additional edition of an existing work | catalog | NEW |
| GAP-13 | S3 authoring_decisions Recognise the moment a work enters the catalog | Recognise the moment a work enters the catalog | catalog | NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The record the previous change calls a book is an edition; the work is added above it. | S3 analysis_findings #1 | The existing identity of title, author and publication year already distinguishes editions, so no existing identity, record or operation is redefined. | No migration of existing records; no change to the edition's identity; a record written before this change is an edition of a work with one edition. |
| 2 | The work's identity is formed by a new transform rather than by widening the existing key transform. | S3 analysis_findings #3 | The edition key transform is reached by every catalog operation and 23 artifacts depend on it. | The two keys stay independent; a change to one cannot alter the other. |
| 3 | The work is claimed through the same registry mechanism the edition is claimed through. | S3 analysis_findings #2 | Register-if-absent gives the atomic uniqueness a work identity needs, and the mechanism is read rather than modified. | The work claim is atomic; two registrations of one work cannot produce two works. |
| 4 | The work store and the work identity registry are declared in the catalog's own storage declaration. | S3 analysis_findings #7 | A subdomain declares its stores once and binds them once, and every consumer of both declarations is inside the catalog. | No second storage or binding declaration for this subdomain. |
| 5 | Registering an edition of a new work extends the existing registration; registering an additional edition is a new operation. | S3 authoring_decisions Register an additional edition of an existing work | The existing registration creates the work and requires a first copy; an additional edition does neither. | Two registration operations, each with its own entry point, sharing every refusal the existing one enforces. |
| 6 | The work claim is placed among the existing claims, before any write. | S3 analysis_findings #10 | The previous change established the order so that a refused registration leaves nothing behind. | A refused registration still changes nothing, including the work. |
| 7 | Search is extended rather than duplicated, and answers at the level of the work. | S3 analysis_findings #5 | Two searches would leave staff choosing which one answers their question, and the existing search's consumers are one workflow and one entry point within the subdomain. | The result shape changes; the search terms do not. Every existing record remains findable. |
| 8 | Retrieval stays edition retrieval and carries a summary of the work. | S1 known_facts Retrieval stays edition retrieval | The business asked for one retrieval carrying a summary, not a second operation. | No work-level retrieval operation in this change. |
| 9 | A work is not retired. | S1 operation_refusals Retire a work | A work whose editions are all retired is simply that; retirement is declared on the edition and cascades to nothing. | No work lifecycle beyond registered; no cascade from an edition's retirement to its work. |

---

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Form the identifying key of a work from its title and author | GAP-01 |
| Claim a work's identity so that two registrations of one work do not produce two works | GAP-02 |
| Resolve the work an edition belongs to | GAP-03 |
| Group selected records by an attribute they share | GAP-04 |
| Declare the stores the catalog owns | GAP-05 |
| Bind the catalog's workflows to the stores they use | GAP-06 |
| Register an edition of a work the catalog does not yet hold | GAP-07 |
| Validate that a registration carries what a work and an edition require | GAP-08 |
| Register an additional edition of an existing work | GAP-09 |
| Search the catalog and answer at the level of the work | GAP-10 |
| Retrieve an edition's complete details with a summary of its work | GAP-11 |
| Admit a request to register an additional edition of an existing work | GAP-12 |
| Recognise the moment a work enters the catalog | GAP-13 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Multiple identifiers for one publication | A further catalog need, deferred to a governed change of its own; what an ISBN identifies could not be answered until an edition was defined. |
| A governed subject taxonomy | A further catalog need, deferred to a governed change of its own. |
| Digital resources associated with catalog records | A further catalog need, deferred to a governed change of its own. |
| Images associated with catalog records | A further catalog need, deferred to a governed change of its own. |
| Deciding which staff are authorized | Deferred to the staff function, which a future governed change introduces. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · business_invariants · constraints · authority_boundaries · business_events · out_of_scope · authority_deferrals |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · gaps · architectural_observations |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
