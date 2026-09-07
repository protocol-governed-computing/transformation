# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|---------|-------------------------------------------------------------------|---------|--------------|
| catalog | NEW_SUBDOMAIN | book_library_mgmt is proposed as a new project, and the library requires a governed catalog management capability it maintains manually today. It extends nothing that exists. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| book_library_mgmt | The project governing the library of books, across ten functions of which catalog is the first. | CR seed §2 Business Vocabulary #1 |
| Catalog | The function holding the library's authoritative description of the materials it holds. | CR seed §2 Business Vocabulary #2 |
| Book | A published material the library catalogs, identified by its title, author and publication year. The general term for anything the library catalogs, including published materials that are not books. | CR seed §2 Business Vocabulary #3 |
| Bibliographic Information | A book's descriptive content: title, author, publication year and subject. | CR seed §2 Business Vocabulary #4 |
| Subject | What kind of book it is, stated as free text; what staff search on when looking for material rather than for a known title. | CR seed §2 Business Vocabulary #5 |
| Physical Copy | An individual copy the library owns, belonging to exactly one book, identified by its barcode. | CR seed §2 Business Vocabulary #6 |
| Barcode | The identifier the library assigns to a physical copy, which distinguishes that copy from every other copy the library owns. | CR seed §2 Business Vocabulary #7 |
| Catalog Record | The single authoritative record for one book or one physical copy. | CR seed §2 Business Vocabulary #8 |
| Book Details | The complete description of a registered book: its bibliographic information and the physical copies the library holds of it. | CR seed §2 Business Vocabulary #9 |
| Obsolete Record | A catalog record the library has determined is no longer to be used. | CR seed §2 Business Vocabulary #10 |
| Authorized Staff | A library staff member permitted to perform catalog operations. | CR seed §2 Business Vocabulary #11 |
| Business Operation | An action performed against the catalog that must be traceable and auditable. | CR seed §2 Business Vocabulary #12 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A single authoritative record exists for each book the library holds. | CR seed §3 Requested Outcomes #1 |
| A single authoritative record exists for each physical copy the library owns. | CR seed §3 Requested Outcomes #2 |
| Authorized staff can register new books, register physical copies, update bibliographic information, retire obsolete records, search the catalog, and retrieve complete book details. | CR seed §3 Requested Outcomes #3 |
| Catalog descriptions are consistent and duplicate entries no longer occur. | CR seed §3 Requested Outcomes #4 |
| Materials can be located by what kind of book they are, without the difficulty the manual catalog produces. | CR seed §3 Requested Outcomes #5 |
| Every business operation performed against the catalog is traceable and auditable. | CR seed §3 Requested Outcomes #6 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| The proposed name of the project is book_library_mgmt. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| The project scope covers ten functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| The scope of this change request is limited to the catalog function only. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A community library maintains thousands of books and other published materials. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| "Book" is the general term for anything the library catalogs, including published materials that are not books. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Catalog records are maintained manually today. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Manual maintenance produces inconsistent descriptions, duplicate entries, and difficulty locating materials. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| The library requires a governed catalog management capability providing a single authoritative record for each book and each physical copy it owns. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A book's bibliographic information is its title, author, publication year and subject. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A book carries at least one subject and may carry several. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| Subject says what kind of book it is, and is what staff search on when looking for material rather than for a known title. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| A book's subject is free text; the library maintains no list of permitted subjects. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| Staff search the catalog by subject or by title. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| A search returns the bibliographic information of each matching registered book, and nothing about its physical copies. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| Title, author and publication year together identify a book. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| Title and author are compared without regard to letter case or repeated spacing; case and spacing do not change which book is meant. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| Each physical copy belongs to exactly one book. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| Registering a book requires at least one physical copy; a book is never registered without a copy. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| Each physical copy carries a barcode the library assigns, which identifies that copy among all the copies the library owns. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| A physical copy may be retired on its own, when it is lost or damaged. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| A physical copy may be registered against a retired book. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| A catalog record is never deleted; retirement is the only way a record leaves use. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| Authorized staff may return a retired book record or a retired physical copy to the registered state. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| An update to bibliographic information may change the title, author or publication year. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| An update is refused when the changed title, author and publication year would match another registered book. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| No retirement follows automatically from another: retiring a book does not retire its copies, and retiring the last copy does not retire the book. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| A registration whose title, author and publication year match a registered book is refused, because the book already exists. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| A retired book is excluded from search results, and its details remain retrievable. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| Retrieving complete book details returns the book's bibliographic information and the physical copies the library holds of it. | HIGH | CR seed §4 Known Facts — Business Truths #29 |
| The catalog does not manage which staff are authorized; it requires staff to be authorized. | HIGH | CR seed §4 Known Facts — Business Truths #30 |
| Deciding who is authorized belongs to the staff function, which governs library employees. | HIGH | CR seed §4 Known Facts — Business Truths #31 |
| Patrons are library users, not employees, and the patron function does not decide staff authorization. | HIGH | CR seed §4 Known Facts — Business Truths #32 |
| Only authorized staff may perform catalog operations. | HIGH | CR seed §4 Known Facts — Business Truths #33 |
| Every business operation must be traceable and auditable. | HIGH | CR seed §4 Known Facts — Business Truths #34 |
| The catalog starts empty; the records staff maintain manually today are not imported by this change. | HIGH | CR seed §4 Known Facts — Business Truths #35 |
| The operations required of the catalog are: register a new book, register a physical copy, update bibliographic information, retire an obsolete record, search the catalog, retrieve complete book details. | HIGH | CR seed §4 Known Facts — Business Truths #36 |
| Borrowing, reservations, fines, patron management, acquisitions and inventory reconciliation are excluded from this release. | HIGH | CR seed §4 Known Facts — Business Truths #37 |
| The excluded capabilities are expected to be introduced through future governed change requests. | HIGH | CR seed §4 Known Facts — Business Truths #38 |
| The excluded capabilities must not be designed into the initial solution. | HIGH | CR seed §4 Known Facts — Business Truths #39 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| book_library_mgmt does not appear to be part of the current software baseline. | The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different. | Confirm no artifact in the pinned composition carries the book_library_mgmt namespace. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| No capability in the current composition manages a library catalog. | This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension. | Confirm nothing in the composition registers, describes, searches or retires a catalog record. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| "Thousands of books" describes the size of the collection and states no performance requirement. | Confirmed by the business author; the statement names no performance target. | CR seed §6 Assumptions #1 |
| The library is treated as a single collection; no branch or location distinction is required. | Confirmed by the business author; the statement names no branch or location. | CR seed §6 Assumptions #2 |
| The nine remaining project functions are named to establish future scope, not to be governed by this change. | Confirmed by the business author; the statement limits this change request to catalog only. | CR seed §6 Assumptions #3 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Capabilities deferred to future change requests must not be designed into this solution. | Business policy | CR seed §7 Constraints #1 |
| Only authorized staff may perform catalog operations. | Business policy | CR seed §7 Constraints #2 |
| Every business operation must leave a record that can be traced and audited. | Business policy | CR seed §7 Constraints #3 |
| A physical copy may never be recorded against more than one book. | Business policy | CR seed §7 Constraints #4 |
| The catalog must not import the records staff maintain manually today. | Business policy | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Each physical copy belongs to exactly one book. | CR seed §8 Business Invariants #1 |
| Each book the library holds has exactly one authoritative record. | CR seed §8 Business Invariants #2 |
| Each physical copy the library owns has exactly one authoritative record. | CR seed §8 Business Invariants #3 |
| No two registered books share the same title, author and publication year. | CR seed §8 Business Invariants #4 |
| A book carries at least one subject. | CR seed §8 Business Invariants #5 |
| No two physical copies the library owns share the same barcode. | CR seed §8 Business Invariants #6 |
| No catalog record is ever deleted. | CR seed §8 Business Invariants #7 |
| Every business operation performed against the catalog is traceable and auditable. | CR seed §8 Business Invariants #8 |
| Only authorized staff perform catalog operations. | CR seed §8 Business Invariants #9 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Book | Registered | The book has been registered and the catalog holds its authoritative record. | CR seed §9 Lifecycle States #1 |
| Book | Retired | The record has been judged obsolete and is no longer to be used; the book is excluded from search, its details remain retrievable, and staff may return it to Registered. | CR seed §9 Lifecycle States #2 |
| Physical Copy | Registered | The copy has been registered against exactly one book. | CR seed §9 Lifecycle States #3 |
| Physical Copy | Retired | The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| Book Registered | When authorized staff register a new book with its first physical copy. | A book enters the catalog and acquires its authoritative record. | CR seed §10 Business Events #1 |
| Physical Copy Registered | When authorized staff register a further copy against a registered book. | The library records another copy it owns. | CR seed §10 Business Events #2 |
| Bibliographic Information Updated | When authorized staff update a registered book's bibliographic information. | The authoritative description of a book changes. | CR seed §10 Business Events #3 |
| Book Retired | When authorized staff retire a book record judged obsolete. | The record is no longer to be used. | CR seed §10 Business Events #4 |
| Physical Copy Retired | When authorized staff retire a copy that is lost or damaged. | The library no longer holds that copy. | CR seed §10 Business Events #5 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Book record | Catalog | CR seed §11 Authority Boundaries #1 |
| Physical copy record | Catalog | CR seed §11 Authority Boundaries #2 |
| Bibliographic information | Catalog | CR seed §11 Authority Boundaries #3 |
| The judgement that a record is obsolete | Authorized staff | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Circulation | A project function; this change request is limited to catalog only. | CR seed §12 Out of Scope #1 |
| Patron | A project function; this change request is limited to catalog only, and patron management is declared excluded from this release. | CR seed §12 Out of Scope #2 |
| Staff | A project function; this change request is limited to catalog only, and it is where deciding who is authorized is deferred to. | CR seed §12 Out of Scope #3 |
| Reservations | A project function, declared excluded from this release; expected through a future governed change request. | CR seed §12 Out of Scope #4 |
| Acquisitions | A project function, declared excluded from this release; expected through a future governed change request. | CR seed §12 Out of Scope #5 |
| Inventory | A project function; inventory reconciliation is declared excluded from this release. | CR seed §12 Out of Scope #6 |
| Notifications | A project function; this change request is limited to catalog only. | CR seed §12 Out of Scope #7 |
| Policy | A project function; this change request is limited to catalog only. | CR seed §12 Out of Scope #8 |
| Reporting | A project function; this change request is limited to catalog only. | CR seed §12 Out of Scope #9 |
| Borrowing | Declared excluded from this release; expected through a future governed change request. | CR seed §12 Out of Scope #10 |
| Fines | Declared excluded from this release; expected through a future governed change request. | CR seed §12 Out of Scope #11 |
| Import of the records staff maintain manually today | The catalog starts empty. | CR seed §12 Out of Scope #12 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| catalog | CREATED | CR seed §13 Governance Scope #1 |
| circulation | ADJACENT | CR seed §13 Governance Scope #2 |
| patron | ADJACENT | CR seed §13 Governance Scope #3 |
| staff | ADJACENT | CR seed §13 Governance Scope #4 |
| reservations | ADJACENT | CR seed §13 Governance Scope #5 |
| acquisitions | ADJACENT | CR seed §13 Governance Scope #6 |
| inventory | ADJACENT | CR seed §13 Governance Scope #7 |
| notifications | ADJACENT | CR seed §13 Governance Scope #8 |
| policy | ADJACENT | CR seed §13 Governance Scope #9 |
| reporting | ADJACENT | CR seed §13 Governance Scope #10 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| Authorized staff can register a new book with at least one physical copy, and the catalog then holds exactly one record for it. | CR seed §15 Acceptance Criteria #1 |
| A registration whose title, author and publication year match a registered book is refused, and the reason states that the book already exists. | CR seed §15 Acceptance Criteria #2 |
| A registration offering no physical copy is refused. | CR seed §15 Acceptance Criteria #3 |
| A registration carrying no subject is refused. | CR seed §15 Acceptance Criteria #4 |
| Authorized staff can register a further physical copy against a registered book, and it is recorded against that book only. | CR seed §15 Acceptance Criteria #5 |
| Authorized staff can update a registered book's bibliographic information, and a later retrieval returns the updated version. | CR seed §15 Acceptance Criteria #6 |
| Authorized staff can retire a book record, and its physical copies are unaffected. | CR seed §15 Acceptance Criteria #7 |
| Authorized staff can retire a physical copy, and the book record is unaffected, including when it is the last copy. | CR seed §15 Acceptance Criteria #8 |
| Authorized staff can search by subject and locate registered books of that kind. | CR seed §15 Acceptance Criteria #9 |
| Authorized staff can search by title and locate a registered book by name. | CR seed §15 Acceptance Criteria #10 |
| A search returns the bibliographic information of each matching book and nothing about its physical copies. | CR seed §15 Acceptance Criteria #11 |
| A retired book does not appear in search results, and its details can still be retrieved. | CR seed §15 Acceptance Criteria #12 |
| Authorized staff can retrieve the complete details of a registered book, including the physical copies the library holds of it. | CR seed §15 Acceptance Criteria #13 |
| Authorized staff can register a physical copy against a retired book. | CR seed §15 Acceptance Criteria #14 |
| Authorized staff can return a retired book record to the registered state, and it appears in search again. | CR seed §15 Acceptance Criteria #15 |
| Authorized staff can return a retired physical copy to the registered state. | CR seed §15 Acceptance Criteria #16 |
| An update that would make a book's title, author and publication year match another registered book is refused. | CR seed §15 Acceptance Criteria #17 |
| A copy registration whose barcode matches a copy the library already owns is refused. | CR seed §15 Acceptance Criteria #18 |
| A staff member who is not authorized cannot perform any catalog operation. | CR seed §15 Acceptance Criteria #19 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Book | Its title, author and publication year together. | Their publication year matches and their titles and authors match without regard to letter case or repeated spacing. | CR seed §16 Identity and Sameness #1 |
| Physical Copy | The barcode the library assigns to it. | Their barcodes match. | CR seed §16 Identity and Sameness #2 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Book | — | Registered | Authorized staff register the book together with its first physical copy. | None beyond the first copy being registered with it. | CR seed §17 Lifecycle Transitions #1 |
| Book | Registered | Retired | Authorized staff judge the record obsolete and retire it. | None — the book's physical copies are unaffected. | CR seed §17 Lifecycle Transitions #2 |
| Book | Retired | Registered | Authorized staff return the retired book record to the registered state. | None — the book's physical copies are unaffected. | CR seed §17 Lifecycle Transitions #3 |
| Physical Copy | — | Registered | Authorized staff register the copy against a registered book. | None. | CR seed §17 Lifecycle Transitions #4 |
| Physical Copy | Registered | Retired | Authorized staff retire a copy that is lost or damaged. | None — the book record is unaffected, including when it is the last copy. | CR seed §17 Lifecycle Transitions #5 |
| Physical Copy | Retired | Registered | Authorized staff return the retired copy to the registered state. | None — the book record is unaffected. | CR seed §17 Lifecycle Transitions #6 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Register a book | Its title, author and publication year match a registered book. | The catalog holds one record per book; the book already exists, and a further copy is what staff register instead. | CR seed §18 Operation Refusals #1 |
| Register a book | No physical copy is offered with it. | A book is never registered without at least one copy. | CR seed §18 Operation Refusals #2 |
| Register a book | It carries no subject. | A book carries at least one subject, and subject is what staff search on. | CR seed §18 Operation Refusals #3 |
| Register a physical copy | The book it names is not registered. | Each physical copy belongs to exactly one book. | CR seed §18 Operation Refusals #4 |
| Register a physical copy | Its barcode matches a copy the library already owns. | A barcode identifies one copy; no two copies share one. | CR seed §18 Operation Refusals #5 |
| Update bibliographic information | The changed title, author and publication year would match another registered book. | Title, author and publication year identify a book; an update must not make one book a duplicate of another. | CR seed §18 Operation Refusals #6 |
| Any catalog operation | The staff member performing it is not authorized. | Only authorized staff may perform catalog operations. | CR seed §18 Operation Refusals #7 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Which staff are authorized | The staff function, which governs library employees | A future governed change request introduces the staff function. | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
