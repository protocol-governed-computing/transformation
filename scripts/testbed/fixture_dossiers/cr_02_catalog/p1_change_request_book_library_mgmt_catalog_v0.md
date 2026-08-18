# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_02_catalog
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
| catalog | EXTEND_SUBDOMAIN | The change extends the existing catalog function of the existing book_library_mgmt project. It introduces no new library function, adds the Work above the records the previous change established, and withdraws no capability staff have today. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| book_library_mgmt | The existing project governing the library of books, across ten functions of which catalog is one. | CR seed §2 Business Vocabulary #1 |
| Catalog | The function holding the library's authoritative description of the materials it holds. | CR seed §2 Business Vocabulary #2 |
| Work | A published work, recognizable as one thing across the editions in which it is published, identified by its title and author. | CR seed §2 Business Vocabulary #3 |
| Edition | A publication of a work, identified by its title, author and publication year; editions of one work share a title and an author and differ by publication year. The record the previous change calls a Book is an edition. | CR seed §2 Business Vocabulary #4 |
| Book | The name the previous change gives to what this change calls an edition. | CR seed §2 Business Vocabulary #5 |
| Edition Summary | Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean. | CR seed §2 Business Vocabulary #6 |
| Work Summary | A short description of the work an edition belongs to, carried in that edition's retrieval so the work's title need not be looked up separately. | CR seed §2 Business Vocabulary #7 |
| Bibliographic Information | An edition's descriptive content, as established by the previous change. | CR seed §2 Business Vocabulary #8 |
| Bibliographic Accuracy | The catalog describing what the library holds as it actually is, which creating separate book records for editions of one work compromises. | CR seed §2 Business Vocabulary #9 |
| Physical Copy | An individual copy the library owns, belonging to exactly one edition. | CR seed §2 Business Vocabulary #10 |
| Existing Catalog Record | A catalog record written under the previous governed change, before this one. | CR seed §2 Business Vocabulary #11 |
| Authorized Staff | A library staff member permitted to perform catalog operations. | CR seed §2 Business Vocabulary #12 |
| Business Operation | An action performed against the catalog that must be traceable and auditable. | CR seed §2 Business Vocabulary #13 |
| Capability Loss | An operation withdrawn from staff or a record made unreachable; what this change promises will not happen, as distinct from a behavior deliberately extended. | CR seed §2 Business Vocabulary #14 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| The catalog can represent a published work that exists in more than one edition. | CR seed §3 Requested Outcomes #1 |
| Authorized staff can register additional editions of an existing work. | CR seed §3 Requested Outcomes #2 |
| Authorized staff can search the catalog and receive one result per matching work rather than one per edition. | CR seed §3 Requested Outcomes #3 |
| Authorized staff can choose the edition they mean from a search result and retrieve that edition's complete details. | CR seed §3 Requested Outcomes #4 |
| No capability staff have today is withdrawn and no existing record becomes unreachable. | CR seed §3 Requested Outcomes #5 |
| Records written under the previous governed change remain valid and continue to function without recreation or migration. | CR seed §3 Requested Outcomes #6 |
| Every business operation remains traceable and auditable. | CR seed §3 Requested Outcomes #7 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| This change extends the existing book_library_mgmt system. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| The overall project scope continues to cover ten library functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| This change extends the existing catalog function and introduces no new library function. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The purpose of the change is to allow the catalog to represent a published work that exists in more than one edition. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Many published works exist in multiple editions. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Editions of one work differ in publication date, publisher, format or content revision while remaining recognizably the same work. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The current catalog cannot distinguish editions without creating separate book records or compromising bibliographic accuracy. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| The current catalog adequately manages books, physical copies and basic bibliographic information. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| As the collection grows, staff increasingly meet situations that cannot be represented accurately within the current model. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| The record the previous change calls a Book is an edition, and always was; the library did not discover this until it met a work published more than once. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| What this change adds is the Work, the abstraction above the existing record. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| No existing record is redefined, no existing operation is withdrawn, and nothing already catalogued needs recreating. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| An edition is identified by its title, author and publication year — the identity the previous change already established. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| Editions of one work share a title and an author and differ by publication year. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| The identity of title, author and publication year distinguishes editions today and continues to; it was never an identity for the work. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| A work is identified by its title and author. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| Two works are the same work when their titles and authors match. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| A physical copy belongs to exactly one edition, exactly as it belongs to exactly one book today. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| Multiple editions do not share physical copies. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| Retiring an edition is what retiring a book is today, it cascades to nothing, and an edition may be retired independently of the work's other editions. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| A work is not retired; a work whose editions are all retired is simply that. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| The first edition creates the work; a work is never registered without an edition, exactly as a book is never registered without a copy. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| A search returns one result per matching work, carrying enough of a summary of that work's editions for staff to choose the edition they mean. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| Three near-identical results for one work is what the library is trying to stop seeing. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| Retrieval stays edition retrieval: staff select an edition and receive that edition's complete details and the physical copies of it, together with a short summary of the work it belongs to. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| Each existing catalog record is an edition, grouped under the work its title and author name. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| No migration is required; existing records remain valid as written. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| A record written before this change is an edition of a work with one edition. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| No capability is lost and no existing record becomes unreachable. | HIGH | CR seed §4 Known Facts — Business Truths #29 |
| Search and retrieval are deliberately extended: search groups its results by work, and retrieval carries a summary of the work. | HIGH | CR seed §4 Known Facts — Business Truths #30 |
| Every other existing operation behaves as it does today. | HIGH | CR seed §4 Known Facts — Business Truths #31 |
| The promise of no regression is a promise that nothing is lost, not that nothing changes. | HIGH | CR seed §4 Known Facts — Business Truths #32 |
| Registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete details are the capabilities that must survive this change. | HIGH | CR seed §4 Known Facts — Business Truths #33 |
| Every business operation shall remain traceable and auditable. | HIGH | CR seed §4 Known Facts — Business Truths #34 |
| The promise that existing records remain valid is about records written under the previous change and read under this one, and is not satisfied by the catalog merely continuing to compile. | HIGH | CR seed §4 Known Facts — Business Truths #35 |
| A record written before this change must still be found by search, retrieved in full, updated, retired and reinstated. | HIGH | CR seed §4 Known Facts — Business Truths #36 |
| Multiple identifiers, a governed subject taxonomy, digital resources and images are further catalog needs the library has, each excluded from this change because each rests on the edition question and could not be settled before it was. | HIGH | CR seed §4 Known Facts — Business Truths #37 |
| Different publishers, distributors or historical editions may assign different ISBN values to the same publication, and the catalog currently assumes a single identifying value. | HIGH | CR seed §4 Known Facts — Business Truths #38 |
| What an ISBN identifies — a work, an edition or a printing — is not answerable until an edition is defined. | HIGH | CR seed §4 Known Facts — Business Truths #39 |
| The library wishes to organize its collection using a governed taxonomy rather than unrestricted subject text, for consistency of cataloging and more accurate searching and reporting. | HIGH | CR seed §4 Known Facts — Business Truths #40 |
| Library collections increasingly include electronic editions, supplementary downloadable material, publisher resources and external reference links, which staff require the ability to associate with catalog records without changing the circulation model. | HIGH | CR seed §4 Known Facts — Business Truths #41 |
| Staff require the ability to associate one or more images, such as cover images or scanned illustrations, with catalog records. | HIGH | CR seed §4 Known Facts — Business Truths #42 |
| Each deferred need is a governed change of its own, in the order the business chooses. | HIGH | CR seed §4 Known Facts — Business Truths #43 |
| Circulation, patron management, reservations, acquisitions, inventory management, notifications, reporting and staff authorization are excluded from this release, except where existing catalog behavior depends upon them. | HIGH | CR seed §4 Known Facts — Business Truths #44 |
| The remaining project functions are named, planned, and outside the scope of this governed extension. | HIGH | CR seed §4 Known Facts — Business Truths #45 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change. | The change is classified EXTEND_SUBDOMAIN on that basis; if the catalog is not present, this is not an extension. | Confirm the pinned composition carries the book_library_mgmt catalog. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The catalog is believed to hold bibliographic records and physical copies of library materials. | The change rests on what the existing record describes: the claim that a Book record is already an edition is a claim about those records. | Confirm what the catalog's records describe in the pinned composition. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| A book is believed to be identified by title, author and publication year. | The whole shape of this change follows from that identity being the edition's and not the work's. If the composition identifies a book differently, editions are not already distinguished. | Confirm how the composition identifies a book. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| A physical copy is believed to belong to exactly one book. | It is what makes a copy already a copy of an edition, with no change to copies at all. | Confirm what a physical copy is registered against in the composition. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details. | These are the capabilities that must survive; the claim that nothing is lost cannot be tested against capabilities that do not exist as believed. | Confirm which catalog operations the composition provides. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| A retired record is believed to be reinstatable. | The existing-records promise requires a record written before this change to be retired and reinstated after it. | Confirm whether the composition provides reinstatement. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |
| Records written under the previous change are believed to exist and to be readable. | The existing-records promise is about data, and is unfalsifiable if no such data exists. | Confirm that records written by the previous catalog capability can be read. | CR seed §5 Existing-System Beliefs — Requiring Verification #7 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| The ten project functions and the deferred catalog needs are named to establish future scope, not to be governed by this change. | The statement names them and declares each excluded from this change. | CR seed §6 Assumptions #1 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| No capability staff have today may be withdrawn and no existing record may become unreachable. | Business policy | CR seed §7 Constraints #1 |
| Existing catalog records must remain valid without recreation or migration, demonstrated against records written under the previous change. | Business policy | CR seed §7 Constraints #2 |
| Only search and retrieval may be extended; every other existing operation must behave as it does today. | Business policy | CR seed §7 Constraints #3 |
| Multiple identifiers, governed subject taxonomy, digital resources and images must not be designed into this change. | Business policy | CR seed §7 Constraints #4 |
| Every business operation must remain traceable and auditable. | Business policy | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Each edition belongs to exactly one work. | CR seed §8 Business Invariants #1 |
| Each physical copy belongs to exactly one edition. | CR seed §8 Business Invariants #2 |
| No two works share the same title and author. | CR seed §8 Business Invariants #3 |
| No two editions of a work share the same publication year. | CR seed §8 Business Invariants #4 |
| Every work has at least one edition. | CR seed §8 Business Invariants #5 |
| A record written under the previous change remains valid and usable without recreation. | CR seed §8 Business Invariants #6 |
| Every business operation performed against the catalog is traceable and auditable. | CR seed §8 Business Invariants #7 |
| The catalog describes what the library holds without compromising bibliographic accuracy. | CR seed §8 Business Invariants #8 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Work | Registered | The work has been registered with its first edition and the catalog holds its authoritative record. | CR seed §9 Lifecycle States #1 |
| Edition | Registered | The edition has been registered against exactly one work; this is what the previous change calls a registered book. | CR seed §9 Lifecycle States #2 |
| Edition | Retired | The edition's record has been judged obsolete and is no longer to be used; this is what the previous change calls a retired book, and staff may return it to Registered. | CR seed §9 Lifecycle States #3 |
| Physical Copy | Registered | The copy has been registered against exactly one edition. | CR seed §9 Lifecycle States #4 |
| Physical Copy | Retired | The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered. | CR seed §9 Lifecycle States #5 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| Work Registered | When authorized staff register an edition of a work the catalog does not yet hold. | A work enters the catalog, created by the edition that evidences it. | CR seed §10 Business Events #1 |
| Edition Registered | When authorized staff register an additional edition of an existing work. | The catalog records a further edition of a work it already holds. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Work record | Catalog | CR seed §11 Authority Boundaries #1 |
| Edition record | Catalog | CR seed §11 Authority Boundaries #2 |
| Physical copy record | Catalog | CR seed §11 Authority Boundaries #3 |
| Existing catalog records | Catalog | CR seed §11 Authority Boundaries #4 |
| The judgement that an edition is obsolete | Authorized staff | CR seed §11 Authority Boundaries #5 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Multiple identifiers | A further catalog need, deferred to a governed change of its own; what an ISBN identifies could not be answered until an edition was defined. | CR seed §12 Out of Scope #1 |
| Governed subject taxonomy | A further catalog need, deferred to a governed change of its own. | CR seed §12 Out of Scope #2 |
| Digital resources | A further catalog need, deferred to a governed change of its own. | CR seed §12 Out of Scope #3 |
| Images | A further catalog need, deferred to a governed change of its own. | CR seed §12 Out of Scope #4 |
| Retirement of a work | A work is not retired; a work whose editions are all retired is simply that. | CR seed §12 Out of Scope #5 |
| Migration of existing records | No migration is required; existing records remain valid as written. | CR seed §12 Out of Scope #6 |
| Circulation | Excluded from this release, except where existing catalog behavior depends upon it. | CR seed §12 Out of Scope #7 |
| Patron management | Excluded from this release, except where existing catalog behavior depends upon it. | CR seed §12 Out of Scope #8 |
| Reservations | Excluded from this release, except where existing catalog behavior depends upon it. | CR seed §12 Out of Scope #9 |
| Acquisitions | Excluded from this release, except where existing catalog behavior depends upon it. | CR seed §12 Out of Scope #10 |
| Inventory management | Excluded from this release, except where existing catalog behavior depends upon it. | CR seed §12 Out of Scope #11 |
| Notifications | Excluded from this release, except where existing catalog behavior depends upon it. | CR seed §12 Out of Scope #12 |
| Reporting | Excluded from this release, except where existing catalog behavior depends upon it. | CR seed §12 Out of Scope #13 |
| Staff authorization | Excluded from this release, except where existing catalog behavior depends upon it. | CR seed §12 Out of Scope #14 |
| Policy | A project function, adjacent to this change and outside its scope. | CR seed §12 Out of Scope #15 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| catalog | EXTENDED | CR seed §13 Governance Scope #1 |
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
| Authorized staff can register an edition of a work the catalog does not yet hold, and the catalog then holds one work with one edition. | CR seed §15 Acceptance Criteria #1 |
| Authorized staff can register an additional edition of an existing work, and it is recorded against that work only. | CR seed §15 Acceptance Criteria #2 |
| A registration whose title, author and publication year match a registered edition is refused. | CR seed §15 Acceptance Criteria #3 |
| Two editions sharing a title and an author, differing by publication year, are grouped under one work. | CR seed §15 Acceptance Criteria #4 |
| A search for a work with three editions returns one result, not three. | CR seed §15 Acceptance Criteria #5 |
| A search result carries enough of a summary of the work's editions for staff to choose the edition they mean. | CR seed §15 Acceptance Criteria #6 |
| Authorized staff can select an edition from a search result and retrieve that edition's complete details and the physical copies of it. | CR seed §15 Acceptance Criteria #7 |
| A retrieval carries a summary of the work the edition belongs to, so the work's title need not be looked up separately. | CR seed §15 Acceptance Criteria #8 |
| Authorized staff can register a physical copy against an edition, and it is recorded against that edition only. | CR seed §15 Acceptance Criteria #9 |
| Authorized staff can retire an edition, and the work's other editions are unaffected. | CR seed §15 Acceptance Criteria #10 |
| Authorized staff can return a retired edition to the registered state. | CR seed §15 Acceptance Criteria #11 |
| Registering a physical copy behaves as it did before this change. | CR seed §15 Acceptance Criteria #12 |
| Updating bibliographic information behaves as it did before this change. | CR seed §15 Acceptance Criteria #13 |
| Retiring a record behaves as it did before this change. | CR seed §15 Acceptance Criteria #14 |
| A record written under the previous change is found by search after this change, without having been recreated or migrated. | CR seed §15 Acceptance Criteria #15 |
| A record written under the previous change is retrieved in full after this change, without having been recreated or migrated. | CR seed §15 Acceptance Criteria #16 |
| A record written under the previous change can be updated after this change. | CR seed §15 Acceptance Criteria #17 |
| A record written under the previous change can be retired after this change. | CR seed §15 Acceptance Criteria #18 |
| A record written under the previous change can be reinstated after this change. | CR seed §15 Acceptance Criteria #19 |
| A record written under the previous change appears as an edition of a work with one edition. | CR seed §15 Acceptance Criteria #20 |
| No operation staff had before this change has been withdrawn. | CR seed §15 Acceptance Criteria #21 |
| Every business operation performed against the extended catalog can be traced and audited afterwards. | CR seed §15 Acceptance Criteria #22 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Work | Its title and author together. | Their titles and authors match. | CR seed §16 Identity and Sameness #1 |
| Edition | Its title, author and publication year together, as the previous change established. | Their publication year matches and their titles and authors match. | CR seed §16 Identity and Sameness #2 |
| Physical Copy | The barcode the library assigns to it. | Their barcodes match. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Work | — | Registered | Authorized staff register an edition of a work the catalog does not yet hold. | None beyond the first edition being registered with it. | CR seed §17 Lifecycle Transitions #1 |
| Edition | — | Registered | Authorized staff register an edition against a work, existing or created by this registration. | None — the work's other editions are unaffected. | CR seed §17 Lifecycle Transitions #2 |
| Edition | Registered | Retired | Authorized staff judge the edition's record obsolete and retire it. | None — the work's other editions and the edition's physical copies are unaffected. | CR seed §17 Lifecycle Transitions #3 |
| Edition | Retired | Registered | Authorized staff return the retired edition to the registered state. | None. | CR seed §17 Lifecycle Transitions #4 |
| Physical Copy | — | Registered | Authorized staff register the copy against a registered edition. | None. | CR seed §17 Lifecycle Transitions #5 |
| Physical Copy | Registered | Retired | Authorized staff retire a copy that is lost or damaged. | None — the edition is unaffected, including when it is the last copy. | CR seed §17 Lifecycle Transitions #6 |
| Physical Copy | Retired | Registered | Authorized staff return the retired copy to the registered state. | None. | CR seed §17 Lifecycle Transitions #7 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Register an edition | Its title, author and publication year match a registered edition. | That identity identifies an edition; the edition already exists, and a further copy is what staff register instead. | CR seed §18 Operation Refusals #1 |
| Register an edition | No work is named and none is created with it. | Every edition belongs to exactly one work. | CR seed §18 Operation Refusals #2 |
| Register a work | No edition is offered with it. | The first edition creates the work; a work is never registered without an edition. | CR seed §18 Operation Refusals #3 |
| Register a physical copy | The edition it names is not registered. | Each physical copy belongs to exactly one edition. | CR seed §18 Operation Refusals #4 |
| Retire a work | Always. | A work is not retired; a work whose editions are all retired is simply that. | CR seed §18 Operation Refusals #5 |
| Any catalog operation | The staff member performing it is not authorized. | Only authorized staff may perform catalog operations. | CR seed §18 Operation Refusals #6 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Identifiers assigned to a publication, including multiple ISBN values | A follow-on governed change for identifiers | This change defines an edition. | CR seed §19 Authority Deferrals #1 |
| A governed subject taxonomy | A follow-on governed change for taxonomy | The business chooses to take it up. | CR seed §19 Authority Deferrals #2 |
| Digital resources associated with catalog records | A follow-on governed change for digital resources | The business chooses to take it up. | CR seed §19 Authority Deferrals #3 |
| Images associated with catalog records | A follow-on governed change for images | The business chooses to take it up. | CR seed §19 Authority Deferrals #4 |
| Which staff are authorized | The staff function | A future governed change introduces staff authorization. | CR seed §19 Authority Deferrals #5 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
