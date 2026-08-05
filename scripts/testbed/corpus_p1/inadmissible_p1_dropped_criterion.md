# Change Request — book_library_mgmt / catalog

The P1 register. Every row restates content from the accepted seed and cites the finding it came
from; P1 classifies and traces, it does not add. Business language only — nothing here gets a code.

**Stage:** 1 — Change Request
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|----------------|-----------|----------------|
| NEW_SUBDOMAIN | The library requires a governed catalog management capability it does not have; catalog records are maintained manually today. It extends nothing that exists. | CR seed §1 CR Type |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|------|------------|----------------|
| Catalog | The library's authoritative description of the materials it holds. | CR seed §2 Business Vocabulary |
| Bibliographic Work | The subject of a single authoritative record describing a published title the library holds. | CR seed §2 Business Vocabulary |
| Book | One kind of bibliographic work: a published material the library registers in the catalog. | CR seed §2 Business Vocabulary |
| Physical Copy | An individual copy owned by the library, belonging to exactly one bibliographic work. | CR seed §2 Business Vocabulary |
| Catalog Record | The single authoritative record for one bibliographic work or one physical copy. | CR seed §2 Business Vocabulary |
| Bibliographic Information | The descriptive content of a bibliographic work's catalog record. | CR seed §2 Business Vocabulary |
| Book Details | The complete description of a registered book, as retrieved by staff. | CR seed §2 Business Vocabulary |
| Obsolete Record | A catalog record the library has determined is no longer to be used. | CR seed §2 Business Vocabulary |
| Authorized Staff | A library staff member permitted to perform catalog operations. | CR seed §2 Business Vocabulary |
| Business Operation | An action performed against the catalog that must be traceable and auditable. | CR seed §2 Business Vocabulary |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|---------|----------------|
| A single authoritative record exists for each bibliographic work the library has cataloged. | CR seed §3 Requested Outcomes #1 |
| A single authoritative record exists for each physical copy the library owns. | CR seed §3 Requested Outcomes #2 |
| Authorized staff can register new books, register physical copies, update bibliographic information, retire obsolete records, search the catalog, and retrieve complete book details. | CR seed §3 Requested Outcomes #3 |
| Catalog descriptions are consistent, and duplicate entries no longer occur. | CR seed §3 Requested Outcomes #4 |
| Materials can be located without the difficulty the manual catalog produces. | CR seed §3 Requested Outcomes #5 |
| Every business operation performed against the catalog is traceable and auditable. | CR seed §3 Requested Outcomes #6 |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|------|-----------|----------------|
| The library maintains thousands of books and other published materials. | HIGH | CR seed §4 Known Facts #1 |
| Catalog records are maintained manually today. | HIGH | CR seed §4 Known Facts #2 |
| Manual maintenance produces inconsistent descriptions, duplicate entries, and difficulty locating materials. | HIGH | CR seed §4 Known Facts #3 |
| The library requires a single authoritative record for each bibliographic work and for each physical copy it owns. | HIGH | CR seed §4 Known Facts #4 |
| A book is one kind of bibliographic work. | HIGH | CR seed §4 Known Facts #5 |
| Each physical copy belongs to exactly one bibliographic work. | HIGH | CR seed §4 Known Facts #6 |
| Every business operation must be traceable and auditable. | HIGH | CR seed §4 Known Facts #7 |
| Only authorized staff may perform catalog operations. | HIGH | CR seed §4 Known Facts #8 |
| The operations required of the catalog are: register a book, register a physical copy, update bibliographic information, retire an obsolete record, search the catalog, retrieve complete book details. | HIGH | CR seed §4 Known Facts #9 |
| Borrowing, reservations, fines, patron management, acquisitions and inventory reconciliation are excluded from this release. | HIGH | CR seed §4 Known Facts #10 |
| The excluded capabilities are expected to be introduced through future governed change requests. | HIGH | CR seed §4 Known Facts #11 |
| The excluded capabilities must not be designed into the initial solution. | HIGH | CR seed §4 Known Facts #12 |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|--------|----------------|-------------------|----------------|
| No capability in the current composition manages a library catalog. | This change exists to fill that gap; if such a capability already exists, the scope of the change is different. | Confirm no existing capability registers, describes, searches or retires a catalog record. | CR seed §5 System Beliefs #1 |
| The platform offers a governed form in which a business capability of this kind can be declared. | The library asks for a governed catalog capability; if no such form exists, the request cannot be met as stated. | Identify the governed forms available for declaring a business capability and its operations. | CR seed §5 System Beliefs #2 |
| The platform already records business operations in a way that can be audited afterwards. | Traceability and auditability are required of every operation; whether they are reused or newly required depends on what already exists. | Identify what the composition already produces as a durable record of a performed operation. | CR seed §5 System Beliefs #3 |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|------------|-------|----------------|
| Nothing in this change depends on knowing who borrows a material. | Borrowing and patron management are declared out of scope. | CR seed §6 Assumptions #1 |
| "Thousands of books" describes the size of the collection and states no performance requirement. | The statement gives no performance target. | CR seed §6 Assumptions #2 |
| The library is treated as a single collection; no branch distinction is required. | The statement names no branch. | CR seed §6 Assumptions #3 |

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|------------|--------|----------------|
| Capabilities deferred to future change requests must not be designed into this solution. | Business policy | CR seed §7 Constraints #1 |
| Only authorized staff may perform catalog operations. | Business policy | CR seed §7 Constraints #2 |
| Every business operation must leave a record that can be traced and audited. | Business policy | CR seed §7 Constraints #3 |
| A physical copy may never be recorded against more than one bibliographic work. | Business policy | CR seed §7 Constraints #4 |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|-----------|----------------|
| Each physical copy belongs to exactly one bibliographic work. | CR seed §8 Business Invariants #1 |
| Each bibliographic work the library has cataloged has exactly one authoritative record. | CR seed §8 Business Invariants #2 |
| Each physical copy the library owns has exactly one authoritative record. | CR seed §8 Business Invariants #3 |
| Every business operation performed against the catalog is traceable and auditable. | CR seed §8 Business Invariants #4 |
| Only authorized staff perform catalog operations. | CR seed §8 Business Invariants #5 |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|--------|-------|---------|----------------|
| Bibliographic Work | Registered | The work has been registered and the catalog holds its authoritative record. | CR seed §9 Lifecycle States #1 |
| Bibliographic Work | Retired | The record has been determined obsolete and retired from use. | CR seed §9 Lifecycle States #2 |
| Physical Copy | Registered | The copy has been registered against exactly one bibliographic work. | CR seed §9 Lifecycle States #3 |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-------|----------------|--------------|----------------|
| Book Registered | When authorized staff register a new book. | A bibliographic work enters the catalog and acquires its authoritative record. | CR seed §10 Business Events #1 |
| Physical Copy Registered | When authorized staff register a physical copy. | The library records a copy it owns against exactly one bibliographic work. | CR seed §10 Business Events #2 |
| Bibliographic Information Updated | When authorized staff update the bibliographic information of a registered work. | The authoritative description of a work changes. | CR seed §10 Business Events #3 |
| Record Retired | When authorized staff retire an obsolete record. | The record is no longer to be used. | CR seed §10 Business Events #4 |
| Catalog Searched | When authorized staff search the catalog for materials. | A business operation occurred that must be traceable and auditable. | CR seed §10 Business Events #5 |
| Book Details Retrieved | When authorized staff retrieve the complete details of a book. | A business operation occurred that must be traceable and auditable. | CR seed §10 Business Events #6 |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|-----------------|---------------------|----------------|
| Bibliographic work record | Catalog | CR seed §11 Authority Boundaries #1 |
| Physical copy record | Catalog | CR seed §11 Authority Boundaries #2 |
| Bibliographic information | Catalog | CR seed §11 Authority Boundaries #3 |
| The decision that a record is obsolete | Authorized staff | CR seed §11 Authority Boundaries #4 |
| The business problem statement | The person who wrote it | CR seed §11 Authority Boundaries #5 |

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|------|--------|----------------|
| Borrowing | Declared excluded from this release; expected to arrive through a future governed change request. | CR seed §12 Out of Scope #1 |
| Reservations | Declared excluded from this release; expected to arrive through a future governed change request. | CR seed §12 Out of Scope #2 |
| Fines | Declared excluded from this release; expected to arrive through a future governed change request. | CR seed §12 Out of Scope #3 |
| Patron management | Declared excluded from this release; expected to arrive through a future governed change request. | CR seed §12 Out of Scope #4 |
| Acquisitions | Declared excluded from this release; expected to arrive through a future governed change request. | CR seed §12 Out of Scope #5 |
| Inventory reconciliation | Declared excluded from this release; expected to arrive through a future governed change request. | CR seed §12 Out of Scope #6 |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, ADJACENT) | Source Finding |
|------------|----------------|----------------|
| catalog | CREATED | CR seed §13 Governance Scope #1 |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|----------|------------|----------|-------|----------------|
| Does retirement apply to physical copy records as well as to bibliographic work records? | The statement says "retire obsolete records" without saying which kind of record. | NO | HUMAN | CR seed §14 Clarification Requests #1 |
| Is a search or a retrieval a business operation that must be traceable and auditable? | Every business operation must be traceable; the statement does not say whether reads count. | NO | HUMAN | CR seed §14 Clarification Requests #2 |
| Who is authoritative for deciding which staff are authorized? | The statement requires authorized staff but names no authority that grants it, and patron management is out of scope. | NO | HUMAN | CR seed §14 Clarification Requests #3 |
| What is believed to already exist in the platform that this change should reuse? | The statement records no belief about the existing composition, so the later verification phase has few targets. | NO | SNAPSHOT | CR seed §14 Clarification Requests #4 |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|-----------|----------------|
| Authorized staff can register a new book, and the catalog then holds exactly one authoritative record for it. | CR seed §15 Acceptance Criteria #1 |
| Authorized staff can register a physical copy against exactly one bibliographic work. | CR seed §15 Acceptance Criteria #2 |
| Authorized staff can update the bibliographic information of a registered work. | CR seed §15 Acceptance Criteria #3 |
| Authorized staff can retire an obsolete record, and the retired record is no longer offered as current. | CR seed §15 Acceptance Criteria #4 |
| Authorized staff can search the catalog and locate a registered material. | CR seed §15 Acceptance Criteria #5 |
| Authorized staff can retrieve the complete details of a registered book. | CR seed §15 Acceptance Criteria #6 |
| Registering the same book twice does not produce two authoritative records for it. | CR seed §15 Acceptance Criteria #8 |
| Every catalog operation performed can be traced and audited after the fact. | CR seed §15 Acceptance Criteria #9 |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|-----------------|---------------|-----------------------|----------------|

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|--------|------------|----------|--------------|---------|----------------|

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|-----------|--------------|-----------------|----------------|

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|-----------------|-------------|-------|----------------|

---
