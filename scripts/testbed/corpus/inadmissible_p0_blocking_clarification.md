# Change Seed — book_library_mgmt / catalog

**Stage:** 0 — Change Seed
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Catalog subdomain governs the library's single authoritative record for each book it holds and
each physical copy it owns. It exists because a community library holding thousands of books and other
published materials maintains its catalog records manually, which produces inconsistent descriptions,
duplicate entries, and difficulty locating materials. It is the first of ten functions the
book_library_mgmt project will govern; it owns the description of what the library holds and the
operations that maintain that description, and it governs none of the nine remaining functions.

## 1. CR Type

<!-- register:cr_type business_language -->
| Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|----------------|-----------|
| NEW_SUBDOMAIN | book_library_mgmt is proposed as a new project, and the library requires a governed catalog management capability it maintains manually today. It extends nothing that exists. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| book_library_mgmt | The project governing the library of books, across ten functions of which catalog is the first. |
| Catalog | The function holding the library's authoritative description of the materials it holds. |
| Book | A published material the library catalogs, identified by its title, author and publication year. The general term for anything the library catalogs, including published materials that are not books. |
| Bibliographic Information | A book's descriptive content: title, author, publication year and subject. |
| Subject | What kind of book it is, stated as free text; what staff search on when looking for material rather than for a known title. |
| Physical Copy | An individual copy the library owns, belonging to exactly one book, identified by its barcode. |
| Barcode | The identifier the library assigns to a physical copy, which distinguishes that copy from every other copy the library owns. |
| Catalog Record | The single authoritative record for one book or one physical copy. |
| Book Details | The complete description of a registered book: its bibliographic information and the physical copies the library holds of it. |
| Obsolete Record | A catalog record the library has determined is no longer to be used. |
| Authorized Staff | A library staff member permitted to perform catalog operations. |
| Business Operation | An action performed against the catalog that must be traceable and auditable. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A single authoritative record exists for each book the library holds. |
| A single authoritative record exists for each physical copy the library owns. |
| Authorized staff can register new books, register physical copies, update bibliographic information, retire obsolete records, search the catalog, and retrieve complete book details. |
| Catalog descriptions are consistent and duplicate entries no longer occur. |
| Materials can be located by what kind of book they are, without the difficulty the manual catalog produces. |
| Every business operation performed against the catalog is traceable and auditable. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The proposed name of the project is book_library_mgmt. | HIGH |
| The project scope covers ten functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting. | HIGH |
| The scope of this change request is limited to the catalog function only. | HIGH |
| A community library maintains thousands of books and other published materials. | HIGH |
| "Book" is the general term for anything the library catalogs, including published materials that are not books. | HIGH |
| Catalog records are maintained manually today. | HIGH |
| Manual maintenance produces inconsistent descriptions, duplicate entries, and difficulty locating materials. | HIGH |
| The library requires a governed catalog management capability providing a single authoritative record for each book and each physical copy it owns. | HIGH |
| A book's bibliographic information is its title, author, publication year and subject. | HIGH |
| A book carries at least one subject and may carry several. | HIGH |
| Subject says what kind of book it is, and is what staff search on when looking for material rather than for a known title. | HIGH |
| A book's subject is free text; the library maintains no list of permitted subjects. | HIGH |
| Staff search the catalog by subject or by title. | HIGH |
| A search returns the bibliographic information of each matching registered book, and nothing about its physical copies. | HIGH |
| Title, author and publication year together identify a book. | HIGH |
| Title and author are compared without regard to letter case or repeated spacing; case and spacing do not change which book is meant. | HIGH |
| Each physical copy belongs to exactly one book. | HIGH |
| Registering a book requires at least one physical copy; a book is never registered without a copy. | HIGH |
| Each physical copy carries a barcode the library assigns, which identifies that copy among all the copies the library owns. | HIGH |
| A physical copy may be retired on its own, when it is lost or damaged. | HIGH |
| A physical copy may be registered against a retired book. | HIGH |
| A catalog record is never deleted; retirement is the only way a record leaves use. | HIGH |
| Authorized staff may return a retired book record or a retired physical copy to the registered state. | HIGH |
| An update to bibliographic information may change the title, author or publication year. | HIGH |
| An update is refused when the changed title, author and publication year would match another registered book. | HIGH |
| No retirement follows automatically from another: retiring a book does not retire its copies, and retiring the last copy does not retire the book. | HIGH |
| A registration whose title, author and publication year match a registered book is refused, because the book already exists. | HIGH |
| A retired book is excluded from search results, and its details remain retrievable. | HIGH |
| Retrieving complete book details returns the book's bibliographic information and the physical copies the library holds of it. | HIGH |
| The catalog does not manage which staff are authorized; it requires staff to be authorized. | HIGH |
| Deciding who is authorized belongs to the staff function, which governs library employees. | HIGH |
| Patrons are library users, not employees, and the patron function does not decide staff authorization. | HIGH |
| Only authorized staff may perform catalog operations. | HIGH |
| Every business operation must be traceable and auditable. | HIGH |
| The catalog starts empty; the records staff maintain manually today are not imported by this change. | HIGH |
| The operations required of the catalog are: register a new book, register a physical copy, update bibliographic information, retire an obsolete record, search the catalog, retrieve complete book details. | HIGH |
| Borrowing, reservations, fines, patron management, acquisitions and inventory reconciliation are excluded from this release. | HIGH |
| The excluded capabilities are expected to be introduced through future governed change requests. | HIGH |
| The excluded capabilities must not be designed into the initial solution. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| book_library_mgmt does not appear to be part of the current software baseline. | The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different. | Confirm no artifact in the pinned composition carries the book_library_mgmt namespace. |
| No capability in the current composition manages a library catalog. | This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension. | Confirm nothing in the composition registers, describes, searches or retires a catalog record. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| "Thousands of books" describes the size of the collection and states no performance requirement. | Confirmed by the business author; the statement names no performance target. |
| The library is treated as a single collection; no branch or location distinction is required. | Confirmed by the business author; the statement names no branch or location. |
| The nine remaining project functions are named to establish future scope, not to be governed by this change. | Confirmed by the business author; the statement limits this change request to catalog only. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Capabilities deferred to future change requests must not be designed into this solution. | Business policy |
| Only authorized staff may perform catalog operations. | Business policy |
| Every business operation must leave a record that can be traced and audited. | Business policy |
| A physical copy may never be recorded against more than one book. | Business policy |
| The catalog must not import the records staff maintain manually today. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Each physical copy belongs to exactly one book. |
| Each book the library holds has exactly one authoritative record. |
| Each physical copy the library owns has exactly one authoritative record. |
| No two registered books share the same title, author and publication year. |
| A book carries at least one subject. |
| No two physical copies the library owns share the same barcode. |
| No catalog record is ever deleted. |
| Every business operation performed against the catalog is traceable and auditable. |
| Only authorized staff perform catalog operations. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Book | Registered | The book has been registered and the catalog holds its authoritative record. |
| Book | Retired | The record has been judged obsolete and is no longer to be used; the book is excluded from search, its details remain retrievable, and staff may return it to Registered. |
| Physical Copy | Registered | The copy has been registered against exactly one book. |
| Physical Copy | Retired | The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| Book Registered | When authorized staff register a new book with its first physical copy. | A book enters the catalog and acquires its authoritative record. |
| Physical Copy Registered | When authorized staff register a further copy against a registered book. | The library records another copy it owns. |
| Bibliographic Information Updated | When authorized staff update a registered book's bibliographic information. | The authoritative description of a book changes. |
| Book Retired | When authorized staff retire a book record judged obsolete. | The record is no longer to be used. |
| Physical Copy Retired | When authorized staff retire a copy that is lost or damaged. | The library no longer holds that copy. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Book record | Catalog |
| Physical copy record | Catalog |
| Bibliographic information | Catalog |
| The judgement that a record is obsolete | Authorized staff |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Circulation | A project function; this change request is limited to catalog only. |
| Patron | A project function; this change request is limited to catalog only, and patron management is declared excluded from this release. |
| Staff | A project function; this change request is limited to catalog only, and it is where deciding who is authorized is deferred to. |
| Reservations | A project function, declared excluded from this release; expected through a future governed change request. |
| Acquisitions | A project function, declared excluded from this release; expected through a future governed change request. |
| Inventory | A project function; inventory reconciliation is declared excluded from this release. |
| Notifications | A project function; this change request is limited to catalog only. |
| Policy | A project function; this change request is limited to catalog only. |
| Reporting | A project function; this change request is limited to catalog only. |
| Borrowing | Declared excluded from this release; expected through a future governed change request. |
| Fines | Declared excluded from this release; expected through a future governed change request. |
| Import of the records staff maintain manually today | The catalog starts empty. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| catalog | CREATED |
| circulation | ADJACENT |
| patron | ADJACENT |
| staff | ADJACENT |
| reservations | ADJACENT |
| acquisitions | ADJACENT |
| inventory | ADJACENT |
| notifications | ADJACENT |
| policy | ADJACENT |
| reporting | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| Does a physical copy belong to the book or to the library branch holding it? | Registration cannot be designed until a copy's owner is settled. | YES | HUMAN |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Authorized staff can register a new book with at least one physical copy, and the catalog then holds exactly one record for it. |
| A registration whose title, author and publication year match a registered book is refused, and the reason states that the book already exists. |
| A registration offering no physical copy is refused. |
| A registration carrying no subject is refused. |
| Authorized staff can register a further physical copy against a registered book, and it is recorded against that book only. |
| Authorized staff can update a registered book's bibliographic information, and a later retrieval returns the updated version. |
| Authorized staff can retire a book record, and its physical copies are unaffected. |
| Authorized staff can retire a physical copy, and the book record is unaffected, including when it is the last copy. |
| Authorized staff can search by subject and locate registered books of that kind. |
| Authorized staff can search by title and locate a registered book by name. |
| A search returns the bibliographic information of each matching book and nothing about its physical copies. |
| A retired book does not appear in search results, and its details can still be retrieved. |
| Authorized staff can retrieve the complete details of a registered book, including the physical copies the library holds of it. |
| Authorized staff can register a physical copy against a retired book. |
| Authorized staff can return a retired book record to the registered state, and it appears in search again. |
| Authorized staff can return a retired physical copy to the registered state. |
| An update that would make a book's title, author and publication year match another registered book is refused. |
| A copy registration whose barcode matches a copy the library already owns is refused. |
| A staff member who is not authorized cannot perform any catalog operation. |
| Every catalog operation performed can be traced and audited afterwards. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Book | Its title, author and publication year together. | Their publication year matches and their titles and authors match without regard to letter case or repeated spacing. |
| Physical Copy | The barcode the library assigns to it. | Their barcodes match. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Book | — | Registered | Authorized staff register the book together with its first physical copy. | None beyond the first copy being registered with it. |
| Book | Registered | Retired | Authorized staff judge the record obsolete and retire it. | None — the book's physical copies are unaffected. |
| Book | Retired | Registered | Authorized staff return the retired book record to the registered state. | None — the book's physical copies are unaffected. |
| Physical Copy | — | Registered | Authorized staff register the copy against a registered book. | None. |
| Physical Copy | Registered | Retired | Authorized staff retire a copy that is lost or damaged. | None — the book record is unaffected, including when it is the last copy. |
| Physical Copy | Retired | Registered | Authorized staff return the retired copy to the registered state. | None — the book record is unaffected. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Register a book | Its title, author and publication year match a registered book. | The catalog holds one record per book; the book already exists, and a further copy is what staff register instead. |
| Register a book | No physical copy is offered with it. | A book is never registered without at least one copy. |
| Register a book | It carries no subject. | A book carries at least one subject, and subject is what staff search on. |
| Register a physical copy | The book it names is not registered. | Each physical copy belongs to exactly one book. |
| Register a physical copy | Its barcode matches a copy the library already owns. | A barcode identifies one copy; no two copies share one. |
| Update bibliographic information | The changed title, author and publication year would match another registered book. | Title, author and publication year identify a book; an update must not make one book a duplicate of another. |
| Any catalog operation | The staff member performing it is not authorized. | Only authorized staff may perform catalog operations. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Which staff are authorized | The staff function, which governs library employees | A future governed change request introduces the staff function. |

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |