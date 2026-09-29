# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_05_catalog
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
| catalog | MODIFY | The catalog is built. It applies its rules as each request states them rather than holding them itself, registers what its own check found incomplete, and checks a copy of the book rather than the book it records. Nothing is added to what the catalog does; its own rules are made to hold however it is reached. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Authorized staff | A library staff member permitted to perform catalog operations. | CR seed §2 Business Vocabulary #1 |
| Staff credentials | What a request presents about the person performing it. | CR seed §2 Business Vocabulary #2 |
| Description | What the library says a book, a work or a further edition must contain. | CR seed §2 Business Vocabulary #3 |
| Business rule | Something the library decided about the catalog: who may perform an operation, and what a book, a work or a further edition must contain. | CR seed §2 Business Vocabulary #4 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| The catalog holds the rules that decide who is authorized to perform a catalog operation, and refuses anyone they do not admit, whatever the request says. | CR seed §3 Requested Outcomes #1 |
| The catalog holds what a book, a work and a further edition must contain, and refuses a registration that does not meet it. | CR seed §3 Requested Outcomes #2 |
| The catalog checks the book, work or edition it records, not a copy supplied beside it. | CR seed §3 Requested Outcomes #3 |
| The catalog registers a physical copy as registered, whatever state the request gives it. | CR seed §3 Requested Outcomes #4 |
| Every correct request from authorized staff is admitted, with the same outcome as today. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| Only authorized staff perform catalog operations. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| The catalog does not decide who is authorized; it requires that they are. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A book's bibliographic information is its title, author, publication year and subject. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A book carries at least one subject. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| The catalog records a publication year as a number. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A work names its title and author. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| A further edition is described as a book is. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A registration that does not meet the library's description is refused. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| What a request says about the catalog's rules is ignored, not refused; it is not part of the request. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A physical copy's registration leads to registered, whatever the request carries. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| Every rule of the catalog's own is held by the catalog. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| The library adds to its record and does not rewrite it. | HIGH | CR seed §4 Known Facts — Business Truths #12 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Every catalog operation confirms the person performing it is authorized, against rules the request supplies. | This is the hole the library most needs closed: a request supplying no rules is confirmed whoever sends it. | Establish where each operation reads its authorization rules from. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds. | A check nothing acts on refuses nothing. | Establish what each registration does with what its check finds. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The catalog checks a copy of the book supplied beside it, not the book it records. | A check of the wrong thing would judge something other than what is written, even if it refused. | Establish what each check reads, and what each registration writes. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The descriptions a book, a work and a further edition are checked against come from the request. | A request supplying an empty description has nothing checked against it. | Establish where each description is read from. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| A physical copy is registered in whatever state the request gives it. | A copy was registered already retired. | Establish where a copy's registered state comes from. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| NONE IDENTIFIED |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Every correct request from authorized staff is admitted, with the same outcome as today. | Business author | CR seed §7 Constraints #1 |
| Records made under a request's own rules stay as they were made. | Business author — the record is added to, never rewritten. | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No catalog operation is performed by anyone the library has not authorized. | CR seed §8 Business Invariants #1 |
| No book, work or further edition is registered without what the library says it must contain. | CR seed §8 Business Invariants #2 |
| What the catalog checks is what it records. | CR seed §8 Business Invariants #3 |
| No physical copy is registered in any state but registered. | CR seed §8 Business Invariants #4 |
| A business rule of the catalog's is held by the catalog, and no request changes it. | CR seed §8 Business Invariants #5 |
| A refusal changes no record. | CR seed §8 Business Invariants #6 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Physical copy | Registered | On the shelf and in service. The only state a copy is registered in. | CR seed §9 Lifecycle States #1 |
| Physical copy | Retired | Taken out of service; unchanged by this change. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A work was registered | When authorized staff register a complete book | Unchanged by this change. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| The rules a catalog operation's staff credentials are judged by | Catalog | CR seed §11 Authority Boundaries #1 |
| What a book, a work and a further edition must contain | Catalog | CR seed §11 Authority Boundaries #2 |
| Which staff are authorized | The staff function | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Who a caller is, and whether the credentials a request presents are genuine | The catalog holds the rules credentials are judged by; it does not authenticate them. | CR seed §12 Out of Scope #1 |
| Which staff are authorized | That belongs to the staff function. | CR seed §12 Out of Scope #2 |
| Loans, members and every function other than the catalog | Not this change. | CR seed §12 Out of Scope #3 |
| Records already in the catalog | The library adds to its record and does not rewrite it. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| catalog | MODIFIED | CR seed §13 Governance Scope #1 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| NONE IDENTIFIED |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| A catalog operation requested by anyone the library has not authorized is refused, whatever rules the request states, and no record changes. | CR seed §15 Acceptance Criteria #1 |
| A book, a work or a further edition missing what the library says it must contain is refused, whatever description the request states, and nothing is registered by it. | CR seed §15 Acceptance Criteria #2 |
| What the catalog checks for a registration is what it records. | CR seed §15 Acceptance Criteria #3 |
| A physical copy is registered as registered, whatever state the request gives it. | CR seed §15 Acceptance Criteria #4 |
| A request stating rules of its own is judged by the catalog's rules, and is not refused for stating them. | CR seed §15 Acceptance Criteria #5 |
| Every correct request from authorized staff is admitted, with the same outcome as before this change. | CR seed §15 Acceptance Criteria #6 |
| Records made before this change are unchanged by it. | CR seed §15 Acceptance Criteria #7 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| NONE IDENTIFIED |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Physical copy | Does not exist | Registered | Authorized staff registering it | Unchanged by this change. | CR seed §17 Lifecycle Transitions #1 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Any catalog operation | The person performing it is not authorized staff | Only authorized staff perform catalog operations. | CR seed §18 Operation Refusals #1 |
| Registering a book | It lacks what the library says a book must contain | The library said the parts are required. | CR seed §18 Operation Refusals #2 |
| Registering a further edition | It lacks what the library says an edition must contain | The library said the parts are required. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Which staff are authorized | The staff function | Always; it is not the catalog's to decide. | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
