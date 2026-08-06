# Stage 4 — Business Model: book_library_mgmt / catalog

**Stage:** 4 — Business Model
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

This document consolidates Stages 1 to 3. It re-litigates nothing and introduces no design: every
row carries the prior-stage finding it came from, and every capability Stage 3 committed appears in
the capability graph exactly as Stage 3 stated it.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Authorized staff member | Performs every catalog operation, and judges when a record is obsolete | Operator | S1 authority_boundaries The judgement that a record is obsolete |
| Library | Owns the physical copies the catalog describes, and assigns each copy its barcode | Owner | S1 identity_and_sameness #2 |
| Staff function | Decides which staff are authorized; not part of this change | Deferred authority | S1 authority_deferrals #1 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Book | A published material the library catalogs — the general term for anything it catalogs | One durable record per book, addressed by title, author and publication year together, updatable in place, carrying its own state | S2 entities Book |
| Physical Copy | An individual copy the library owns, belonging to exactly one book | One durable record per copy, addressed by its barcode, naming the one book it belongs to, carrying its own state | S2 entities Physical Copy |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| Book records | The catalog's authoritative description of every book the library holds | S2 entities Book |
| Physical copy records | The catalog's authoritative record of every copy the library owns | S2 entities Physical Copy |
| Catalog audit trail | The catalog's own durable record of every operation performed against it | S3 analysis_findings #1 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| Book registered | Authorized staff register a new book together with its first physical copy | A book enters the catalog and acquires its authoritative record | S1 business_events Book Registered |
| Physical copy registered | Authorized staff register a further copy against a registered book | The library records another copy it owns | S1 business_events Physical Copy Registered |
| Bibliographic information updated | Authorized staff update a registered book's information | The authoritative description of a book changes | S1 business_events Bibliographic Information Updated |
| Book retired | Authorized staff retire a book record judged obsolete | The record is no longer to be used, and is excluded from search | S1 business_events Book Retired |
| Physical copy retired | Authorized staff retire a copy that is lost or damaged | The library no longer holds that copy | S1 business_events Physical Copy Retired |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Physical copy | belongs to | Book | Record a copy against exactly one registered book | S1 business_invariants — each physical copy belongs to exactly one book |
| Book | is identified by | Title, author and publication year | Refuse a registration whose three identifying attributes match a registered book | S1 identity_and_sameness #1 |
| Physical copy | is identified by | Barcode | Refuse a copy registration whose barcode is already owned | S1 identity_and_sameness #2 |
| Authorized staff member | performs | Catalog operation | Confirm the staff member is authorized before any operation | S1 operation_refusals #7 |
| Catalog operation | is recorded in | Catalog audit trail | Record every performed operation durably in the catalog's own trail | S1 business_invariants — every business operation is traceable and auditable |
| Book | carries | Subject | Select registered books by the subject or title staff search for | S1 known_facts — staff search the catalog by subject or by title |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Hold a book record durably and update it in place | S3 authoring_decisions Hold a book record durably and update it in place | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Hold a physical copy record durably and update it in place | S3 authoring_decisions Hold a physical copy record durably and update it in place | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Enforce that one book exists per title, author and publication year | S3 authoring_decisions Enforce that one book exists per title, author and publication year | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Enforce that one physical copy exists per barcode | S3 authoring_decisions Enforce that one physical copy exists per barcode | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Assemble a catalog record from supplied values | S3 authoring_decisions Assemble a catalog record from supplied values | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Confirm a catalog record carries its required fields | S3 authoring_decisions Confirm a catalog record carries its required fields | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Select the catalog records matching stated criteria | S3 authoring_decisions Select the catalog records matching stated criteria | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Confirm the parameters supplied to a catalog operation satisfy their declared rules | S3 authoring_decisions Confirm the parameters supplied to a catalog operation satisfy their declared rules | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Append an entry to an append-only trail | S3 authoring_decisions Append an entry to an append-only trail | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Record a performed catalog operation in the catalog's audit trail | S3 authoring_decisions Record a performed catalog operation in the catalog's audit trail | CRITICAL | GAP-01 | Nothing in the composition satisfies it. |
| Declare the stores the catalog owns | S3 authoring_decisions Declare the stores the catalog owns | CRITICAL | GAP-02 | Nothing in the composition satisfies it. |
| Bind the catalog's operations to the stores and mechanisms they use | S3 authoring_decisions Bind the catalog's operations to the stores and mechanisms they use | CRITICAL | GAP-03 | Nothing in the composition satisfies it. |
| A library staff actor whose authorization a catalog operation binds | S3 authoring_decisions A library staff actor whose authorization a catalog operation binds | CRITICAL | GAP-04 | Nothing in the composition satisfies it. |
| Confirm the staff member performing an operation is authorized | S3 authoring_decisions Confirm the staff member performing an operation is authorized | CRITICAL | GAP-05 | Nothing in the composition satisfies it. |
| Register a book together with its first physical copy | S3 authoring_decisions Register a book together with its first physical copy | CRITICAL | GAP-06 | Nothing in the composition satisfies it. |
| Register a further physical copy against a registered book | S3 authoring_decisions Register a further physical copy against a registered book | CRITICAL | GAP-07 | Nothing in the composition satisfies it. |
| Update a book's bibliographic information | S3 authoring_decisions Update a book's bibliographic information | CRITICAL | GAP-08 | Nothing in the composition satisfies it. |
| Retire a book record | S3 authoring_decisions Retire a book record | CRITICAL | GAP-09 | Nothing in the composition satisfies it. |
| Retire a physical copy | S3 authoring_decisions Retire a physical copy | CRITICAL | GAP-10 | Nothing in the composition satisfies it. |
| Return a retired book record to the registered state | S3 authoring_decisions Return a retired book record to the registered state | CRITICAL | GAP-11 | Nothing in the composition satisfies it. |
| Return a retired physical copy to the registered state | S3 authoring_decisions Return a retired physical copy to the registered state | CRITICAL | GAP-12 | Nothing in the composition satisfies it. |
| Read every book record so that a search can select among them by content | S3 authoring_decisions Read every book record so that a search can select among them by content | CRITICAL | GAP-17 | Owned by platform: an existing mechanism amended to publish records. |
| Search the catalog by subject or title, excluding retired books | S3 authoring_decisions Search the catalog by subject or title, excluding retired books | CRITICAL | GAP-13 | Nothing in the composition satisfies it. |
| A governed entry point for each catalog operation | S3 authoring_decisions A governed entry point for each catalog operation | CRITICAL | GAP-15 | Nothing in the composition satisfies it. |
| A business moment for each of the five catalog events | S3 authoring_decisions A business moment for each of the five catalog events | CRITICAL | GAP-16 | Nothing in the composition satisfies it. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| catalog | capability_side_effects::CS_MUTABLE_JSON_V0 | capability call | SATISFIED | S3 dependency_discoveries Durable record storage |
| catalog | capability_side_effects::CS_REGISTRY_V0 | capability call | SATISFIED | S3 dependency_discoveries Uniqueness |
| catalog | capability_side_effects::CS_APPENDONLY_JSONL_V0 | capability call | SATISFIED | S3 dependency_discoveries Append-only trail |
| catalog | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | capability call | SATISFIED | S3 dependency_discoveries Record assembly |
| catalog | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | capability call | SATISFIED | S3 dependency_discoveries Record shape validation |
| catalog | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | capability call | SATISFIED | S3 dependency_discoveries Record selection |
| catalog | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | capability call | SATISFIED | S3 dependency_discoveries Parameter validation |
| catalog | staff | data read | GAP | S1 authority_deferrals #1 |

The dependency on the staff function is a gap owned by that peer, not by this change: the catalog
reads whether a staff member is authorized and never decides it.

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Each physical copy belongs to exactly one book. | S1 business_invariants #1 | invariant |
| 2 | Each book the library holds has exactly one authoritative record. | S1 business_invariants #2 | invariant |
| 3 | Each physical copy the library owns has exactly one authoritative record. | S1 business_invariants #3 | invariant |
| 4 | No two registered books share the same title, author and publication year. | S1 business_invariants #4 | invariant |
| 5 | A book carries at least one subject. | S1 business_invariants #5 | invariant |
| 6 | No two physical copies the library owns share the same barcode. | S1 business_invariants #6 | invariant |
| 7 | Every business operation performed against the catalog is traceable and auditable. | S1 business_invariants #7 | invariant |
| 8 | Only authorized staff perform catalog operations. | S1 business_invariants #8 | invariant |
| 9 | Capabilities deferred to future change requests must not be designed into this solution. | S1 constraints #1 | governance rule |
| 10 | A physical copy may never be recorded against more than one book. | S1 constraints #4 | business policy |
| 11 | The catalog must not import the records staff maintain manually today. | S1 constraints #5 | business policy |
| 12 | The catalog appends only to a store it owns; it never writes into another subdomain's store. | S3 analysis_findings #1 | governance rule |
| 13 | A record's state is held as data on the record, because retirement is reversible in both directions. | S3 analysis_findings #3 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Record a performed catalog operation in the catalog's audit trail | Record a performed catalog operation in the catalog's audit trail | catalog | NEW |
| GAP-02 | S3 authoring_decisions Declare the stores the catalog owns | Declare the stores the catalog owns | catalog | NEW |
| GAP-03 | S3 authoring_decisions Bind the catalog's operations to the stores and mechanisms they use | Bind the catalog's operations to the stores and mechanisms they use | catalog | NEW |
| GAP-04 | S3 authoring_decisions A library staff actor whose authorization a catalog operation binds | A library staff actor whose authorization a catalog operation binds | catalog | NEW |
| GAP-05 | S3 authoring_decisions Confirm the staff member performing an operation is authorized | Confirm the staff member performing an operation is authorized | catalog | NEW |
| GAP-06 | S3 authoring_decisions Register a book together with its first physical copy | Register a book together with its first physical copy | catalog | NEW |
| GAP-07 | S3 authoring_decisions Register a further physical copy against a registered book | Register a further physical copy against a registered book | catalog | NEW |
| GAP-08 | S3 authoring_decisions Update a book's bibliographic information | Update a book's bibliographic information | catalog | NEW |
| GAP-09 | S3 authoring_decisions Retire a book record | Retire a book record | catalog | NEW |
| GAP-10 | S3 authoring_decisions Retire a physical copy | Retire a physical copy | catalog | NEW |
| GAP-11 | S3 authoring_decisions Return a retired book record to the registered state | Return a retired book record to the registered state | catalog | NEW |
| GAP-12 | S3 authoring_decisions Return a retired physical copy to the registered state | Return a retired physical copy to the registered state | catalog | NEW |
| GAP-13 | S3 authoring_decisions Search the catalog by subject or title, excluding retired books | Search the catalog by subject or title, excluding retired books | catalog | NEW |
| GAP-14 | S3 authoring_decisions Retrieve a book's complete details with the copies the library holds | Retrieve a book's complete details with the copies the library holds | catalog | NEW |
| GAP-15 | S3 authoring_decisions A governed entry point for each catalog operation | A governed entry point for each catalog operation | catalog | NEW |
| GAP-16 | S3 authoring_decisions A business moment for each of the five catalog events | A business moment for each of the five catalog events | catalog | NEW |
| GAP-17 | S3 authoring_decisions Read every book record so that a search can select among them by content | Read every book record so that a search can select among them by content | platform | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The catalog is a new subdomain, a peer of the nine other project functions, rather than an extension of anything existing. | S3 placement_decision | Nothing in the composition carries the project's namespace or manages a library catalog, so there is no boundary to extend. | The catalog owns its records exclusively; the nine remaining functions stay adjacent and untouched. |
| 2 | The catalog owns its audit composition and its own append-only audit store, reusing only the append-only mechanism beneath them. | S3 analysis_findings #1 | A subdomain owns its stores exclusively, and library traceability must not depend on agent-governance semantics. Decided by the business owner. | Two artifacts are authored rather than one reused; no catalog operation writes into another subdomain's store. |
| 3 | Uniqueness on a book is enforced by reusing the registry with a key formed from title, author and publication year. | S3 analysis_findings #2 | Register-if-absent gives an atomic guarantee, and forming the key is a catalog business rule rather than a change to a side effect nineteen artifacts depend on. Decided by the business owner. | The composite key is stated by the catalog; the registry itself is read, never modified. |
| 4 | A record's state is data on the record, not the store it occupies. | S3 analysis_findings #3 | Retirement is reversible, so a record must move from registered to retired and back without moving between stores. | The record store must support update in place; state is never implied by location. |
| 5 | Search and retrieval are audited but raise no business event. | S1 business_events Book Registered | Every operation must be traceable, while an event is a moment another function may react to, and nothing reacts to a read. | Five business moments are authored, not seven; the audit trail records all nine operations. |
| 6 | Registering a book registers its first physical copy in the same operation. | S1 known_facts — registering a book requires at least one physical copy | A book is never registered without a copy, so the two records come into existence together. | Registering a book raises one business moment, not two; a registration offering no copy is refused. |
| 7 | Retirement never cascades in either direction. | S1 lifecycle_transitions #2 | Staff retire each record explicitly; nothing happens in the catalog that a staff member did not do. | No derived state change exists to design, and the audit trail needs no staff-versus-system distinction. |
| 8 | Authorization is read on every operation and granted nowhere in this change. | S1 authority_deferrals #1 | The catalog requires staff to be authorized; deciding who is authorized belongs to the staff function, which a future change request introduces. | The catalog authors an authorization read and no authorization grant; the dependency on the staff function is that peer's gap. |
| 9 | Subject is free text, so no value-set validation applies. | S3 analysis_findings #6 | The business chose free text. Decided by the business owner. | One fewer reuse candidate; search by kind is only as consistent as what staff type. |
| 10 | Search excludes retired books while retrieval serves them. | S3 analysis_findings #4 | A retired record must stay auditable and retrievable without appearing as current stock. | Both read paths select by stated criteria, with the record's state as one of them. |
| 11 | The durable-record mechanism is extended to publish records, rather than the catalog keeping a second copy of every book for searching. | S3 analysis_findings #7 | The implementation already returned records and only the declaration withheld them; a projection store would duplicate every book and need syncing on every update, retirement and reinstatement. Decided by the business owner. | One additive operation on a platform side effect; the catalog holds no second copy of a book. |

---

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Record a performed catalog operation in the catalog's audit trail | GAP-01 |
| Declare the stores the catalog owns | GAP-02 |
| Bind the catalog's operations to the stores and mechanisms they use | GAP-03 |
| A library staff actor whose authorization a catalog operation binds | GAP-04 |
| Confirm the staff member performing an operation is authorized | GAP-05 |
| Register a book together with its first physical copy | GAP-06 |
| Register a further physical copy against a registered book | GAP-07 |
| Update a book's bibliographic information | GAP-08 |
| Retire a book record | GAP-09 |
| Retire a physical copy | GAP-10 |
| Return a retired book record to the registered state | GAP-11 |
| Return a retired physical copy to the registered state | GAP-12 |
| Search the catalog by subject or title, excluding retired books | GAP-13 |
| Retrieve a book's complete details with the copies the library holds | GAP-14 |
| A governed entry point for each catalog operation | GAP-15 |
| A business moment for each of the five catalog events | GAP-16 |

| Read every book record so that a search can select among them by content | GAP-17 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Circulation | A project function; this change request is limited to catalog only |
| Patron | A project function, and patron management is declared excluded from this release |
| Staff | A project function; it is where deciding who is authorized is deferred to |
| Reservations | Declared excluded from this release |
| Acquisitions | Declared excluded from this release |
| Inventory | A project function; inventory reconciliation is declared excluded from this release |
| Notifications | A project function; this change request is limited to catalog only |
| Policy | A project function; this change request is limited to catalog only |
| Reporting | A project function; this change request is limited to catalog only |
| Borrowing | Declared excluded from this release |
| Fines | Declared excluded from this release |
| Import of the records staff maintain manually today | The catalog starts empty |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
