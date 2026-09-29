# Change Seed — book_library_mgmt / catalog

**Stage:** 0 — Change Seed
**CR:** cr_05_catalog
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Catalog subdomain governs what the library knows about its books: the works it carries, the
editions of those works, and the physical copies on its shelves. It holds one record for each, the
state that says whether each is in service or retired, and the details the library publishes about
them. It records each thing being registered, its details being corrected, and its being retired or
reinstated, and it announces the moments the business declared matter. It does not govern who borrows
a book, what a borrower may do, or what the library charges.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| catalog | MODIFY | The catalog is built. It applies its rules as each request states them rather than holding them itself, registers what its own check found incomplete, and checks a copy of the book rather than the book it records. Nothing is added to what the catalog does; its own rules are made to hold however it is reached. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Authorized staff | A library staff member permitted to perform catalog operations. |
| Staff credentials | What a request presents about the person performing it. |
| Description | What the library says a book, a work or a further edition must contain. |
| Business rule | Something the library decided about the catalog: who may perform an operation, and what a book, a work or a further edition must contain. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The catalog holds the rules that decide who is authorized to perform a catalog operation, and refuses anyone they do not admit, whatever the request says. |
| The catalog holds what a book, a work and a further edition must contain, and refuses a registration that does not meet it. |
| The catalog checks the book, work or edition it records, not a copy supplied beside it. |
| The catalog registers a physical copy as registered, whatever state the request gives it. |
| Every correct request from authorized staff is admitted, with the same outcome as today. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| Only authorized staff perform catalog operations. | HIGH |
| The catalog does not decide who is authorized; it requires that they are. | HIGH |
| A book's bibliographic information is its title, author, publication year and subject. | HIGH |
| A book carries at least one subject. | HIGH |
| The catalog records a publication year as a number. | HIGH |
| A work names its title and author. | HIGH |
| A further edition is described as a book is. | HIGH |
| A registration that does not meet the library's description is refused. | HIGH |
| What a request says about the catalog's rules is ignored, not refused; it is not part of the request. | HIGH |
| A physical copy's registration leads to registered, whatever the request carries. | HIGH |
| Every rule of the catalog's own is held by the catalog. | HIGH |
| The library adds to its record and does not rewrite it. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Every catalog operation confirms the person performing it is authorized, against rules the request supplies. | This is the hole the library most needs closed: a request supplying no rules is confirmed whoever sends it. | Establish where each operation reads its authorization rules from. |
| The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds. | A check nothing acts on refuses nothing. | Establish what each registration does with what its check finds. |
| The catalog checks a copy of the book supplied beside it, not the book it records. | A check of the wrong thing would judge something other than what is written, even if it refused. | Establish what each check reads, and what each registration writes. |
| The descriptions a book, a work and a further edition are checked against come from the request. | A request supplying an empty description has nothing checked against it. | Establish where each description is read from. |
| A physical copy is registered in whatever state the request gives it. | A copy was registered already retired. | Establish where a copy's registered state comes from. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Every correct request from authorized staff is admitted, with the same outcome as today. | Business author |
| Records made under a request's own rules stay as they were made. | Business author — the record is added to, never rewritten. |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No catalog operation is performed by anyone the library has not authorized. |
| No book, work or further edition is registered without what the library says it must contain. |
| What the catalog checks is what it records. |
| No physical copy is registered in any state but registered. |
| A business rule of the catalog's is held by the catalog, and no request changes it. |
| A refusal changes no record. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Physical copy | Registered | On the shelf and in service. The only state a copy is registered in. |
| Physical copy | Retired | Taken out of service; unchanged by this change. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A work was registered | When authorized staff register a complete book | Unchanged by this change. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| The rules a catalog operation's staff credentials are judged by | Catalog |
| What a book, a work and a further edition must contain | Catalog |
| Which staff are authorized | The staff function |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Who a caller is, and whether the credentials a request presents are genuine | The catalog holds the rules credentials are judged by; it does not authenticate them. |
| Which staff are authorized | That belongs to the staff function. |
| Loans, members and every function other than the catalog | Not this change. |
| Records already in the catalog | The library adds to its record and does not rewrite it. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| catalog | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A catalog operation requested by anyone the library has not authorized is refused, whatever rules the request states, and no record changes. |
| A book, a work or a further edition missing what the library says it must contain is refused, whatever description the request states, and nothing is registered by it. |
| What the catalog checks for a registration is what it records. |
| A physical copy is registered as registered, whatever state the request gives it. |
| A request stating rules of its own is judged by the catalog's rules, and is not refused for stating them. |
| Every correct request from authorized staff is admitted, with the same outcome as before this change. |
| Records made before this change are unchanged by it. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED | | |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Physical copy | Does not exist | Registered | Authorized staff registering it | Unchanged by this change. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Any catalog operation | The person performing it is not authorized staff | Only authorized staff perform catalog operations. |
| Registering a book | It lacks what the library says a book must contain | The library said the parts are required. |
| Registering a further edition | It lacks what the library says an edition must contain | The library said the parts are required. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Which staff are authorized | The staff function | Always; it is not the catalog's to decide. |
