# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_03_catalog
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was said in.
S1 interrogates and does not author.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|-----------|----------------|-----------|--------------|
| catalog | MODIFY | The catalog exists and works. It declares six moments it announces and announces none of them, against a rule the business set when the function was established. | CR seed §1 CR Type #1 |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|------|------------|--------------|
| Work | Something the library carries, independent of any particular edition of it. | CR seed §2 Business Vocabulary #1 |
| Book | An edition of a work. | CR seed §2 Business Vocabulary #2 |
| Physical copy | One copy of a book, on a shelf. | CR seed §2 Business Vocabulary #3 |
| Bibliographic information | What the library publishes about a book. | CR seed §2 Business Vocabulary #4 |
| Retirement | Taking a book or a copy out of service, without removing what is known about it. | CR seed §2 Business Vocabulary #5 |
| Reinstatement | Returning a retired book or copy to service. | CR seed §2 Business Vocabulary #6 |
| Moment | Something the catalog announces because the business declared it matters. | CR seed §2 Business Vocabulary #7 |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|---------|--------------|
| Each of the six declared moments is announced when the act it names completes. | CR seed §3 Requested Outcomes #1 |
| That they are announced is checked, so the silence cannot return unnoticed. | CR seed §3 Requested Outcomes #2 |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|------|-----------|--------------|
| The business decided the catalog announces the moments that matter. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Six moments are declared: a work registered, a book registered, a physical copy registered, bibliographic information updated, a book retired, a physical copy retired. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A moment is announced when the act it names has completed, and not before. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A refusal announces nothing. Nothing happened that anyone need be told about. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Reinstatement is silent. The catalog performs it, records it, and announces nothing. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| The six declared moments are the complete set. No seventh is added by this change. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| An announcement carries which thing it concerns and when it occurred, and nothing further. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| Nobody is expected to hear these announcements today. The moment exists for the record. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| The catalog does not go back and announce moments that occurred before this change. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| This is a defect, not a new requirement. | HIGH | CR seed §4 Known Facts — Business Truths #10 |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|--------|----------------|-------------------|--------------|
| The catalog declares six moments and announces none of them. | The whole of this change. | Confirm the six are declared, and establish whether anything refers to any of them. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The catalog performs registration, correction, retirement and reinstatement, each as its own act. | Each declared moment must attach to the act it names. | Confirm which acts the catalog performs. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Nothing checks whether a declared moment is ever announced. | Explains how the silence went unnoticed and says what the check must add. | Establish whether any rule relates a declared moment to an announcement of it. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Reinstatement has no declared moment of its own. | The business has ruled it silent; if a moment exists, the ruling and the system disagree. | Confirm no moment is declared for reinstatement. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|------------|-------|--------------|
| Each declared moment corresponds to exactly one act the catalog performs. | The six are named after acts the catalog is known to perform. | CR seed §6 Assumptions #1 |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source | Source Finding |
|------------|--------|--------------|
| Nothing a caller sends or is told back changes. This is invisible from outside. | Business author | CR seed §7 Constraints #1 |
| No moment is added and none is removed. The six are the complete set. | Business author | CR seed §7 Constraints #2 |
| Nothing outside the catalog is touched. | Business author | CR seed §7 Constraints #3 |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|-----------|--------------|
| A declared moment is announced when the act it names completes. | CR seed §8 Business Invariants #1 |
| A refused act announces nothing. | CR seed §8 Business Invariants #2 |
| An announcement carries which thing it concerns and when it occurred. | CR seed §8 Business Invariants #3 |
| A recorded moment is never changed or removed. | CR seed §8 Business Invariants #4 |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|--------|-------|---------|--------------|
| Book | In service | The library carries it. | CR seed §9 Lifecycle States #1 |
| Book | Retired | Taken out of service; what is known about it is kept. | CR seed §9 Lifecycle States #2 |
| Physical copy | In service | On the shelf. | CR seed §9 Lifecycle States #3 |
| Physical copy | Retired | Taken out of service. | CR seed §9 Lifecycle States #4 |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-------|----------------|--------------|--------------|
| A work was registered | When the library first carries a work | The library can show when it began carrying it. | CR seed §10 Business Events #1 |
| A book was registered | When an edition of a work is registered | The library can show when the edition entered the catalog. | CR seed §10 Business Events #2 |
| A physical copy was registered | When a copy is put on a shelf | The library can show when the copy became available. | CR seed §10 Business Events #3 |
| Bibliographic information was updated | When what the library publishes about a book is corrected | The library can show when the record changed. | CR seed §10 Business Events #4 |
| A book was retired | When an edition is taken out of service | The library can show when it stopped carrying it. | CR seed §10 Business Events #5 |
| A physical copy was retired | When a copy is taken out of service | The library can show when the copy left the shelf. | CR seed §10 Business Events #6 |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|-----------------|---------------------|--------------|
| Work, book and physical copy | catalog | CR seed §11 Authority Boundaries #1 |
| Bibliographic information | catalog | CR seed §11 Authority Boundaries #2 |
| The moments the catalog announces | catalog | CR seed §11 Authority Boundaries #3 |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason | Source Finding |
|------|--------|--------------|
| What any listener does with an announcement | The catalog announces the moment; who attends to it is a later question. | CR seed §12 Out of Scope #1 |
| Whether the six are the right six | They are the moments the business already declared. | CR seed §12 Out of Scope #2 |
| A moment for reinstatement | The business has ruled reinstatement silent. | CR seed §12 Out of Scope #3 |
| Anything about what the catalog holds or how it is searched | Only the announcing is touched. | CR seed §12 Out of Scope #4 |
| Anything outside the catalog | No other subdomain is touched. | CR seed §12 Out of Scope #5 |
| Moments that occurred before this change | The record is added to and never rewritten. | CR seed §12 Out of Scope #6 |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|------------|--------------|--------------|
| catalog | MODIFIED | CR seed §13 Governance Scope #1 |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|----------|------------|----------|-------|--------------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|-----------|--------------|
| Registering a work announces that a work was registered. | CR seed §15 Acceptance Criteria #1 |
| Registering a book announces that a book was registered. | CR seed §15 Acceptance Criteria #2 |
| Registering a physical copy announces that a physical copy was registered. | CR seed §15 Acceptance Criteria #3 |
| Correcting bibliographic information announces that it was updated. | CR seed §15 Acceptance Criteria #4 |
| Retiring a book announces that a book was retired. | CR seed §15 Acceptance Criteria #5 |
| Retiring a physical copy announces that a physical copy was retired. | CR seed §15 Acceptance Criteria #6 |
| A refused act announces nothing. | CR seed §15 Acceptance Criteria #7 |
| Reinstating a book or a copy announces nothing. | CR seed §15 Acceptance Criteria #8 |
| Each announcement carries which thing it concerns and when it occurred. | CR seed §15 Acceptance Criteria #9 |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|-----------------|---------------|-----------------------|--------------|
| Moment | The act it names | They name the same act of the catalog. | CR seed §16 Identity and Sameness #1 |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|--------|------------|----------|--------------|---------|--------------|
| Book | In service | Retired | The library retiring it. | A moment is announced. Nothing else follows. | CR seed §17 Lifecycle Transitions #1 |
| Book | Retired | In service | The library reinstating it. | NONE. Reinstatement is silent. | CR seed §17 Lifecycle Transitions #2 |
| Physical copy | In service | Retired | The library retiring it. | A moment is announced. Nothing else follows. | CR seed §17 Lifecycle Transitions #3 |
| Physical copy | Retired | In service | The library reinstating it. | NONE. Reinstatement is silent. | CR seed §17 Lifecycle Transitions #4 |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|-----------|--------------|-----------------|--------------|
| Announcing a moment | The act it names did not complete | A moment names something that happened; announcing one for an act that failed would state something untrue. | CR seed §18 Operation Refusals #1 |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|-----------------|-------------|-------|--------------|
| What a listener does with an announcement | A later change | The business decides who is told and how. | CR seed §19 Authority Deferrals #1 |

