# Change Seed — book_library_mgmt / catalog

**Stage:** 0 — Change Seed
**CR:** cr_04_catalog
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

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
| catalog | MODIFY | Two operations state that they need things they do not use, and one states a publication year in a form the catalog does not hold it in. Correct requests are turned away. What each operation needs is restated to match what it does. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Operation | Something a librarian asks the catalog to do. |
| Request | One asking, with what the librarian supplied. |
| Admission | The catalog deciding whether a request may proceed. |
| Requirement | Something an operation states a request must supply. |
| Correction | Changing some details of a record the catalog already holds. |
| Further edition | Another edition of a work the library already carries. |
| Publication year | The year an edition was published, which the catalog holds as a number. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Registering a further edition asks for the publication year in the form the catalog holds it. |
| Correcting bibliographic information asks for the record and the changes, and nothing it does not use. |
| A correct request for either operation is admitted. |
| Every requirement an operation states is something that operation uses. |
| Who may perform each operation, and what they must be authorised to do, is unchanged. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The catalog holds a publication year as a number, wherever it holds one. | HIGH |
| Registering a work for the first time asks for the publication year as a number. | HIGH |
| Registering a further edition of that same work asks for it as text. | HIGH |
| A correction names the record it corrects and supplies the fields it changes. | HIGH |
| A correction does not restate the fields it leaves alone; that is what makes it a correction. | HIGH |
| Correcting bibliographic information asks for the title, author and publication year of the record. | HIGH |
| The steps that carry out a correction read the record named and the changed fields, and read none of those three. | HIGH |
| A requirement an operation does not use turns away correct requests and admits nothing extra. | HIGH |
| A librarian correcting the subject headings of a record is turned away for not resupplying its title. | HIGH |
| The library's end-to-end exercise of the catalog fails at both operations today. | HIGH |
| Both failures are the boundary behaving correctly on a wrong statement. | HIGH |
| Nothing compared what an operation asks for against what it uses, for as long as the boundary admitted everything. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number. | One half of the change. | Confirm both statements, and confirm which form the catalog records. |
| Correcting bibliographic information asks for three details it does not use. | The other half. | Confirm the three, and confirm no step of the correction reads them. |
| No other catalog operation asks for something it does not use. | Says whether this is two instances or a pattern across the subdomain. | Establish, for every catalog operation, what it asks for and what it uses. |
| Who may perform each operation is stated separately from what the operation needs. | Decides whether restating requirements can affect authorisation. | Confirm the two are separate statements. |
| The details a correction changes are supplied together, as the changed fields. | Decides whether removing three requirements loses anything. | Confirm the changed fields carry the details being corrected. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| A librarian supplies a publication year the way the catalog displays it. | The catalog holds and shows it as a number. |
| The two operations were written from a third, and the requirements were carried across without being reconsidered. | Registering a work needs the title, author and year; correcting a record does not, and asks for all three. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Every requirement an operation keeps is one that operation uses. | Business author |
| Nothing about who may perform an operation changes. | Business author |
| The records the catalog already holds are not migrated, rewritten or revalidated. | Business author |
| A publication year is a number, in every operation that names one. | Business author |
| No operation gains a requirement in this change. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| An operation requires only what it uses. |
| A publication year is stated as a number wherever an operation asks for one. |
| A correction requires the record it corrects and the changes it makes. |
| A correct request is admitted. |
| What an operation requires is stated separately from who may perform it. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Request | Admitted | The catalog accepted it and the operation proceeds. |
| Request | Turned away | The catalog refused it before anything happened. |
| Request | Correct and turned away | Everything the operation needs was supplied and it was refused anyway. This is the state this change ends. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A request was admitted | When a librarian supplied what the operation needs | The operation proceeds and the catalog changes. |
| A request was turned away | When something the operation needs was missing or in the wrong form | The librarian is told before anything happened, and the catalog is unchanged. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What each catalog operation requires | The catalog subdomain |
| The form a publication year takes | The catalog subdomain |
| Who may perform a catalog operation | The library's authorisation rules |
| Whether a request is admitted | The catalog boundary |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Who may perform any catalog operation | A separate statement, unchanged by this. |
| The records the catalog already holds | No held record changes; only what a new request must supply. |
| Operations of subdomains other than the catalog | Each subdomain's own change. |
| Whether the boundary should determine admission at all | Settled; the boundary does what it always declared. |

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
| Registering a further edition of a held work, with the publication year as a number, is admitted and the edition is registered. |
| Correcting the subject headings of a held record, naming the record and the changes only, is admitted and the record is corrected. |
| The library's end-to-end exercise of the catalog completes, with every criterion holding. |
| A request omitting something either operation still needs is turned away. |
| A librarian not authorised for either operation is refused exactly as today. |
| No catalog operation requires anything it does not use. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Record | The identity the catalog holds it under | Two requests name the same identity. |
| Requirement | The operation that states it and the thing it asks for | One operation asks for one thing once. |
| Publication year | The year itself | Two are the same year, however either was supplied. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Request | Correct and turned away | Admitted | The operation stating only what it uses. | The operation proceeds as it always would have. Nothing about the catalog's records changes. |
| Request | Admitted | Turned away | Something the operation needs being absent. | The catalog is unchanged and the librarian is told. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Registering a further edition | The publication year is not supplied | The catalog holds an edition by the work it belongs to and the year it was published, so an edition without a year cannot be placed. |
| Correcting bibliographic information | The record to correct is not named | A correction with no subject changes nothing, and the catalog would not know what to change. |
| Correcting bibliographic information | No changed fields are supplied | A correction that changes nothing is not a correction. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| What operations of other subdomains require | Each subdomain | That subdomain raises the change that needs it. |
