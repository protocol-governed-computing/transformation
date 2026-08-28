# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_04_catalog
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
| catalog | MODIFY | Two operations state that they need things they do not use, and one states a publication year in a form the catalog does not hold it in. Correct requests are turned away. What each operation needs is restated to match what it does. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Operation | Something a librarian asks the catalog to do. | CR seed §2 Business Vocabulary #1 |
| Request | One asking, with what the librarian supplied. | CR seed §2 Business Vocabulary #2 |
| Admission | The catalog deciding whether a request may proceed. | CR seed §2 Business Vocabulary #3 |
| Requirement | Something an operation states a request must supply. | CR seed §2 Business Vocabulary #4 |
| Correction | Changing some details of a record the catalog already holds. | CR seed §2 Business Vocabulary #5 |
| Further edition | Another edition of a work the library already carries. | CR seed §2 Business Vocabulary #6 |
| Publication year | The year an edition was published, which the catalog holds as a number. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Registering a further edition asks for the publication year in the form the catalog holds it. | CR seed §3 Requested Outcomes #1 |
| Correcting bibliographic information asks for the record and the changes, and nothing it does not use. | CR seed §3 Requested Outcomes #2 |
| A correct request for either operation is admitted. | CR seed §3 Requested Outcomes #3 |
| Every requirement an operation states is something that operation uses. | CR seed §3 Requested Outcomes #4 |
| Who may perform each operation, and what they must be authorised to do, is unchanged. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| The catalog holds a publication year as a number, wherever it holds one. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Registering a work for the first time asks for the publication year as a number. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Registering a further edition of that same work asks for it as text. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A correction names the record it corrects and supplies the fields it changes. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A correction does not restate the fields it leaves alone; that is what makes it a correction. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Correcting bibliographic information asks for the title, author and publication year of the record. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The steps that carry out a correction read the record named and the changed fields, and read none of those three. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A requirement an operation does not use turns away correct requests and admits nothing extra. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A librarian correcting the subject headings of a record is turned away for not resupplying its title. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| The library's end-to-end exercise of the catalog fails at both operations today. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| Both failures are the boundary behaving correctly on a wrong statement. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| Nothing compared what an operation asks for against what it uses, for as long as the boundary admitted everything. | HIGH | CR seed §4 Known Facts — Business Truths #12 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number. | One half of the change. | Confirm both statements, and confirm which form the catalog records. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Correcting bibliographic information asks for three details it does not use. | The other half. | Confirm the three, and confirm no step of the correction reads them. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| No other catalog operation asks for something it does not use. | Says whether this is two instances or a pattern across the subdomain. | Establish, for every catalog operation, what it asks for and what it uses. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Who may perform each operation is stated separately from what the operation needs. | Decides whether restating requirements can affect authorisation. | Confirm the two are separate statements. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The details a correction changes are supplied together, as the changed fields. | Decides whether removing three requirements loses anything. | Confirm the changed fields carry the details being corrected. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| A librarian supplies a publication year the way the catalog displays it. | The catalog holds and shows it as a number. | CR seed §6 Assumptions #1 |
| The two operations were written from a third, and the requirements were carried across without being reconsidered. | Registering a work needs the title, author and year; correcting a record does not, and asks for all three. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Every requirement an operation keeps is one that operation uses. | Business author | CR seed §7 Constraints #1 |
| Nothing about who may perform an operation changes. | Business author | CR seed §7 Constraints #2 |
| The records the catalog already holds are not migrated, rewritten or revalidated. | Business author | CR seed §7 Constraints #3 |
| A publication year is a number, in every operation that names one. | Business author | CR seed §7 Constraints #4 |
| No operation gains a requirement in this change. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| An operation requires only what it uses. | CR seed §8 Business Invariants #1 |
| A publication year is stated as a number wherever an operation asks for one. | CR seed §8 Business Invariants #2 |
| A correction requires the record it corrects and the changes it makes. | CR seed §8 Business Invariants #3 |
| A correct request is admitted. | CR seed §8 Business Invariants #4 |
| What an operation requires is stated separately from who may perform it. | CR seed §8 Business Invariants #5 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Request | Admitted | The catalog accepted it and the operation proceeds. | CR seed §9 Lifecycle States #1 |
| Request | Turned away | The catalog refused it before anything happened. | CR seed §9 Lifecycle States #2 |
| Request | Correct and turned away | Everything the operation needs was supplied and it was refused anyway. This is the state this change ends. | CR seed §9 Lifecycle States #3 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A request was admitted | When a librarian supplied what the operation needs | The operation proceeds and the catalog changes. | CR seed §10 Business Events #1 |
| A request was turned away | When something the operation needs was missing or in the wrong form | The librarian is told before anything happened, and the catalog is unchanged. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What each catalog operation requires | The catalog subdomain | CR seed §11 Authority Boundaries #1 |
| The form a publication year takes | The catalog subdomain | CR seed §11 Authority Boundaries #2 |
| Who may perform a catalog operation | The library's authorisation rules | CR seed §11 Authority Boundaries #3 |
| Whether a request is admitted | The catalog boundary | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Who may perform any catalog operation | A separate statement, unchanged by this. | CR seed §12 Out of Scope #1 |
| The records the catalog already holds | No held record changes; only what a new request must supply. | CR seed §12 Out of Scope #2 |
| Operations of subdomains other than the catalog | Each subdomain's own change. | CR seed §12 Out of Scope #3 |
| Whether the boundary should determine admission at all | Settled; the boundary does what it always declared. | CR seed §12 Out of Scope #4 |

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
| Registering a further edition of a held work, with the publication year as a number, is admitted and the edition is registered. | CR seed §15 Acceptance Criteria #1 |
| Correcting the subject headings of a held record, naming the record and the changes only, is admitted and the record is corrected. | CR seed §15 Acceptance Criteria #2 |
| The library's end-to-end exercise of the catalog completes, with every criterion holding. | CR seed §15 Acceptance Criteria #3 |
| A request omitting something either operation still needs is turned away. | CR seed §15 Acceptance Criteria #4 |
| A librarian not authorised for either operation is refused exactly as today. | CR seed §15 Acceptance Criteria #5 |
| No catalog operation requires anything it does not use. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Record | The identity the catalog holds it under | Two requests name the same identity. | CR seed §16 Identity and Sameness #1 |
| Requirement | The operation that states it and the thing it asks for | One operation asks for one thing once. | CR seed §16 Identity and Sameness #2 |
| Publication year | The year itself | Two are the same year, however either was supplied. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Request | Correct and turned away | Admitted | The operation stating only what it uses. | The operation proceeds as it always would have. Nothing about the catalog's records changes. | CR seed §17 Lifecycle Transitions #1 |
| Request | Admitted | Turned away | Something the operation needs being absent. | The catalog is unchanged and the librarian is told. | CR seed §17 Lifecycle Transitions #2 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Registering a further edition | The publication year is not supplied | The catalog holds an edition by the work it belongs to and the year it was published, so an edition without a year cannot be placed. | CR seed §18 Operation Refusals #1 |
| Correcting bibliographic information | The record to correct is not named | A correction with no subject changes nothing, and the catalog would not know what to change. | CR seed §18 Operation Refusals #2 |
| Correcting bibliographic information | No changed fields are supplied | A correction that changes nothing is not a correction. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| What operations of other subdomains require | Each subdomain | That subdomain raises the change that needs it. | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
