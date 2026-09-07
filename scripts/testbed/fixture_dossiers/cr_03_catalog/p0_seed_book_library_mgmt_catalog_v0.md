# Change Seed — book_library_mgmt / catalog

**Stage:** 0 — Change Seed
**CR:** cr_03_catalog
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
| catalog | MODIFY | The catalog exists and works. It declares six moments it announces and announces none of them, against a rule the business set when the function was established. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Work | Something the library carries, independent of any particular edition of it. |
| Book | An edition of a work. |
| Physical copy | One copy of a book, on a shelf. |
| Bibliographic information | What the library publishes about a book. |
| Retirement | Taking a book or a copy out of service, without removing what is known about it. |
| Reinstatement | Returning a retired book or copy to service. |
| Moment | Something the catalog announces because the business declared it matters. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Each of the six declared moments is announced when the act it names completes. |
| That they are announced is checked, so the silence cannot return unnoticed. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The business decided the catalog announces the moments that matter. | HIGH |
| Six moments are declared: a work registered, a book registered, a physical copy registered, bibliographic information updated, a book retired, a physical copy retired. | HIGH |
| A moment is announced when the act it names has completed, and not before. | HIGH |
| A refusal announces nothing. Nothing happened that anyone need be told about. | HIGH |
| Reinstatement is silent. The catalog performs it, records it, and announces nothing. | HIGH |
| The six declared moments are the complete set. No seventh is added by this change. | HIGH |
| An announcement carries which thing it concerns and when it occurred, and nothing further. | HIGH |
| Nobody is expected to hear these announcements today. The moment exists for the record. | HIGH |
| The catalog does not go back and announce moments that occurred before this change. | HIGH |
| This is a defect, not a new requirement. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The catalog declares six moments and announces none of them. | The whole of this change. | Confirm the six are declared, and establish whether anything refers to any of them. |
| The catalog performs registration, correction, retirement and reinstatement, each as its own act. | Each declared moment must attach to the act it names. | Confirm which acts the catalog performs. |
| Nothing checks whether a declared moment is ever announced. | Explains how the silence went unnoticed and says what the check must add. | Establish whether any rule relates a declared moment to an announcement of it. |
| Reinstatement has no declared moment of its own. | The business has ruled it silent; if a moment exists, the ruling and the system disagree. | Confirm no moment is declared for reinstatement. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| Each declared moment corresponds to exactly one act the catalog performs. | The six are named after acts the catalog is known to perform. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Nothing a caller sends or is told back changes. This is invisible from outside. | Business author |
| No moment is added and none is removed. The six are the complete set. | Business author |
| Nothing outside the catalog is touched. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A declared moment is announced when the act it names completes. |
| A refused act announces nothing. |
| An announcement carries which thing it concerns and when it occurred. |
| A recorded moment is never changed or removed. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Book | In service | The library carries it. |
| Book | Retired | Taken out of service; what is known about it is kept. |
| Physical copy | In service | On the shelf. |
| Physical copy | Retired | Taken out of service. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A work was registered | When the library first carries a work | The library can show when it began carrying it. |
| A book was registered | When an edition of a work is registered | The library can show when the edition entered the catalog. |
| A physical copy was registered | When a copy is put on a shelf | The library can show when the copy became available. |
| Bibliographic information was updated | When what the library publishes about a book is corrected | The library can show when the record changed. |
| A book was retired | When an edition is taken out of service | The library can show when it stopped carrying it. |
| A physical copy was retired | When a copy is taken out of service | The library can show when the copy left the shelf. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Work, book and physical copy | catalog |
| Bibliographic information | catalog |
| The moments the catalog announces | catalog |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| What any listener does with an announcement | The catalog announces the moment; who attends to it is a later question. |
| Whether the six are the right six | They are the moments the business already declared. |
| A moment for reinstatement | The business has ruled reinstatement silent. |
| Anything about what the catalog holds or how it is searched | Only the announcing is touched. |
| Anything outside the catalog | No other subdomain is touched. |
| Moments that occurred before this change | The record is added to and never rewritten. |

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
| Registering a work announces that a work was registered. |
| Registering a book announces that a book was registered. |
| Registering a physical copy announces that a physical copy was registered. |
| Correcting bibliographic information announces that it was updated. |
| Retiring a book announces that a book was retired. |
| Retiring a physical copy announces that a physical copy was retired. |
| A refused act announces nothing. |
| Reinstating a book or a copy announces nothing. |
| Each announcement carries which thing it concerns and when it occurred. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Moment | The act it names | They name the same act of the catalog. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Book | In service | Retired | The library retiring it. | A moment is announced. Nothing else follows. |
| Book | Retired | In service | The library reinstating it. | NONE. Reinstatement is silent. |
| Physical copy | In service | Retired | The library retiring it. | A moment is announced. Nothing else follows. |
| Physical copy | Retired | In service | The library reinstating it. | NONE. Reinstatement is silent. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Announcing a moment | The act it names did not complete | A moment names something that happened; announcing one for an act that failed would state something untrue. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| What a listener does with an announcement | A later change | The business decides who is told and how. |
