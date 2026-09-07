# Change Seed — book_library_mgmt / catalog

**Stage:** 0 — Change Seed
**CR:** cr_02_catalog
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Catalog subdomain governs the library's authoritative record of the materials it holds. A
previous governed change established that catalog, containing bibliographic records and physical
copies of library materials. This change exists to let the catalog represent a published work that
exists in more than one edition. As the collection grows, staff increasingly meet works published in
multiple editions that differ in publication date, publisher, format or content revision while
remaining recognizably the same work, and the catalog cannot distinguish them without creating
separate book records or compromising bibliographic accuracy. The library has settled what an edition
is: the record the previous change calls a Book is an edition and always was, and what this change
adds is the Work above it — the abstraction that says three records describe one published work. No
existing record is redefined and no existing operation is withdrawn.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| catalog | EXTEND_SUBDOMAIN | The change extends the existing catalog function of the existing book_library_mgmt project. It introduces no new library function, adds the Work above the records the previous change established, and withdraws no capability staff have today. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| book_library_mgmt | The existing project governing the library of books, across ten functions of which catalog is one. |
| Catalog | The function holding the library's authoritative description of the materials it holds. |
| Work | A published work, recognizable as one thing across the editions in which it is published, identified by its title and author. |
| Edition | A publication of a work, identified by its title, author and publication year; editions of one work share a title and an author and differ by publication year. The record the previous change calls a Book is an edition. |
| Book | The name the previous change gives to what this change calls an edition. |
| Edition Summary | Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean. |
| Work Summary | A short description of the work an edition belongs to, carried in that edition's retrieval so the work's title need not be looked up separately. |
| Bibliographic Information | An edition's descriptive content, as established by the previous change. |
| Bibliographic Accuracy | The catalog describing what the library holds as it actually is, which creating separate book records for editions of one work compromises. |
| Physical Copy | An individual copy the library owns, belonging to exactly one edition. |
| Existing Catalog Record | A catalog record written under the previous governed change, before this one. |
| Authorized Staff | A library staff member permitted to perform catalog operations. |
| Business Operation | An action performed against the catalog that must be traceable and auditable. |
| Capability Loss | An operation withdrawn from staff or a record made unreachable; what this change promises will not happen, as distinct from a behavior deliberately extended. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The catalog can represent a published work that exists in more than one edition. |
| Authorized staff can register additional editions of an existing work. |
| Authorized staff can search the catalog and receive one result per matching work rather than one per edition. |
| Authorized staff can choose the edition they mean from a search result and retrieve that edition's complete details. |
| No capability staff have today is withdrawn and no existing record becomes unreachable. |
| Records written under the previous governed change remain valid and continue to function without recreation or migration. |
| Every business operation remains traceable and auditable. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| This change extends the existing book_library_mgmt system. | HIGH |
| The overall project scope continues to cover ten library functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting. | HIGH |
| This change extends the existing catalog function and introduces no new library function. | HIGH |
| The purpose of the change is to allow the catalog to represent a published work that exists in more than one edition. | HIGH |
| Many published works exist in multiple editions. | HIGH |
| Editions of one work differ in publication date, publisher, format or content revision while remaining recognizably the same work. | HIGH |
| The current catalog cannot distinguish editions without creating separate book records or compromising bibliographic accuracy. | HIGH |
| The current catalog adequately manages books, physical copies and basic bibliographic information. | HIGH |
| As the collection grows, staff increasingly meet situations that cannot be represented accurately within the current model. | HIGH |
| The record the previous change calls a Book is an edition, and always was; the library did not discover this until it met a work published more than once. | HIGH |
| What this change adds is the Work, the abstraction above the existing record. | HIGH |
| No existing record is redefined, no existing operation is withdrawn, and nothing already catalogued needs recreating. | HIGH |
| An edition is identified by its title, author and publication year — the identity the previous change already established. | HIGH |
| Editions of one work share a title and an author and differ by publication year. | HIGH |
| The identity of title, author and publication year distinguishes editions today and continues to; it was never an identity for the work. | HIGH |
| A work is identified by its title and author. | HIGH |
| Two works are the same work when their titles and authors match. | HIGH |
| A physical copy belongs to exactly one edition, exactly as it belongs to exactly one book today. | HIGH |
| Multiple editions do not share physical copies. | HIGH |
| Retiring an edition is what retiring a book is today, it cascades to nothing, and an edition may be retired independently of the work's other editions. | HIGH |
| A work is not retired; a work whose editions are all retired is simply that. | HIGH |
| The first edition creates the work; a work is never registered without an edition, exactly as a book is never registered without a copy. | HIGH |
| A search returns one result per matching work, carrying enough of a summary of that work's editions for staff to choose the edition they mean. | HIGH |
| Three near-identical results for one work is what the library is trying to stop seeing. | HIGH |
| Retrieval stays edition retrieval: staff select an edition and receive that edition's complete details and the physical copies of it, together with a short summary of the work it belongs to. | HIGH |
| Each existing catalog record is an edition, grouped under the work its title and author name. | HIGH |
| No migration is required; existing records remain valid as written. | HIGH |
| A record written before this change is an edition of a work with one edition. | HIGH |
| No capability is lost and no existing record becomes unreachable. | HIGH |
| Search and retrieval are deliberately extended: search groups its results by work, and retrieval carries a summary of the work. | HIGH |
| Every other existing operation behaves as it does today. | HIGH |
| The promise of no regression is a promise that nothing is lost, not that nothing changes. | HIGH |
| Registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete details are the capabilities that must survive this change. | HIGH |
| Every business operation shall remain traceable and auditable. | HIGH |
| The promise that existing records remain valid is about records written under the previous change and read under this one, and is not satisfied by the catalog merely continuing to compile. | HIGH |
| A record written before this change must still be found by search, retrieved in full, updated, retired and reinstated. | HIGH |
| Multiple identifiers, a governed subject taxonomy, digital resources and images are further catalog needs the library has, each excluded from this change because each rests on the edition question and could not be settled before it was. | HIGH |
| Different publishers, distributors or historical editions may assign different ISBN values to the same publication, and the catalog currently assumes a single identifying value. | HIGH |
| What an ISBN identifies — a work, an edition or a printing — is not answerable until an edition is defined. | HIGH |
| The library wishes to organize its collection using a governed taxonomy rather than unrestricted subject text, for consistency of cataloging and more accurate searching and reporting. | HIGH |
| Library collections increasingly include electronic editions, supplementary downloadable material, publisher resources and external reference links, which staff require the ability to associate with catalog records without changing the circulation model. | HIGH |
| Staff require the ability to associate one or more images, such as cover images or scanned illustrations, with catalog records. | HIGH |
| Each deferred need is a governed change of its own, in the order the business chooses. | HIGH |
| Circulation, patron management, reservations, acquisitions, inventory management, notifications, reporting and staff authorization are excluded from this release, except where existing catalog behavior depends upon them. | HIGH |
| The remaining project functions are named, planned, and outside the scope of this governed extension. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change. | The change is classified EXTEND_SUBDOMAIN on that basis; if the catalog is not present, this is not an extension. | Confirm the pinned composition carries the book_library_mgmt catalog. |
| The catalog is believed to hold bibliographic records and physical copies of library materials. | The change rests on what the existing record describes: the claim that a Book record is already an edition is a claim about those records. | Confirm what the catalog's records describe in the pinned composition. |
| A book is believed to be identified by title, author and publication year. | The whole shape of this change follows from that identity being the edition's and not the work's. If the composition identifies a book differently, editions are not already distinguished. | Confirm how the composition identifies a book. |
| A physical copy is believed to belong to exactly one book. | It is what makes a copy already a copy of an edition, with no change to copies at all. | Confirm what a physical copy is registered against in the composition. |
| The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details. | These are the capabilities that must survive; the claim that nothing is lost cannot be tested against capabilities that do not exist as believed. | Confirm which catalog operations the composition provides. |
| A retired record is believed to be reinstatable. | The existing-records promise requires a record written before this change to be retired and reinstated after it. | Confirm whether the composition provides reinstatement. |
| Records written under the previous change are believed to exist and to be readable. | The existing-records promise is about data, and is unfalsifiable if no such data exists. | Confirm that records written by the previous catalog capability can be read. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| The ten project functions and the deferred catalog needs are named to establish future scope, not to be governed by this change. | The statement names them and declares each excluded from this change. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No capability staff have today may be withdrawn and no existing record may become unreachable. | Business policy |
| Existing catalog records must remain valid without recreation or migration, demonstrated against records written under the previous change. | Business policy |
| Only search and retrieval may be extended; every other existing operation must behave as it does today. | Business policy |
| Multiple identifiers, governed subject taxonomy, digital resources and images must not be designed into this change. | Business policy |
| Every business operation must remain traceable and auditable. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Each edition belongs to exactly one work. |
| Each physical copy belongs to exactly one edition. |
| No two works share the same title and author. |
| No two editions of a work share the same publication year. |
| Every work has at least one edition. |
| A record written under the previous change remains valid and usable without recreation. |
| Every business operation performed against the catalog is traceable and auditable. |
| The catalog describes what the library holds without compromising bibliographic accuracy. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Work | Registered | The work has been registered with its first edition and the catalog holds its authoritative record. |
| Edition | Registered | The edition has been registered against exactly one work; this is what the previous change calls a registered book. |
| Edition | Retired | The edition's record has been judged obsolete and is no longer to be used; this is what the previous change calls a retired book, and staff may return it to Registered. |
| Physical Copy | Registered | The copy has been registered against exactly one edition. |
| Physical Copy | Retired | The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| Work Registered | When authorized staff register an edition of a work the catalog does not yet hold. | A work enters the catalog, created by the edition that evidences it. |
| Edition Registered | When authorized staff register an additional edition of an existing work. | The catalog records a further edition of a work it already holds. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Work record | Catalog |
| Edition record | Catalog |
| Physical copy record | Catalog |
| Existing catalog records | Catalog |
| The judgement that an edition is obsolete | Authorized staff |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Multiple identifiers | A further catalog need, deferred to a governed change of its own; what an ISBN identifies could not be answered until an edition was defined. |
| Governed subject taxonomy | A further catalog need, deferred to a governed change of its own. |
| Digital resources | A further catalog need, deferred to a governed change of its own. |
| Images | A further catalog need, deferred to a governed change of its own. |
| Retirement of a work | A work is not retired; a work whose editions are all retired is simply that. |
| Migration of existing records | No migration is required; existing records remain valid as written. |
| Circulation | Excluded from this release, except where existing catalog behavior depends upon it. |
| Patron management | Excluded from this release, except where existing catalog behavior depends upon it. |
| Reservations | Excluded from this release, except where existing catalog behavior depends upon it. |
| Acquisitions | Excluded from this release, except where existing catalog behavior depends upon it. |
| Inventory management | Excluded from this release, except where existing catalog behavior depends upon it. |
| Notifications | Excluded from this release, except where existing catalog behavior depends upon it. |
| Reporting | Excluded from this release, except where existing catalog behavior depends upon it. |
| Staff authorization | Excluded from this release, except where existing catalog behavior depends upon it. |
| Policy | A project function, adjacent to this change and outside its scope. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| catalog | EXTENDED |
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

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Authorized staff can register an edition of a work the catalog does not yet hold, and the catalog then holds one work with one edition. |
| Authorized staff can register an additional edition of an existing work, and it is recorded against that work only. |
| A registration whose title, author and publication year match a registered edition is refused. |
| Two editions sharing a title and an author, differing by publication year, are grouped under one work. |
| A search for a work with three editions returns one result, not three. |
| A search result carries enough of a summary of the work's editions for staff to choose the edition they mean. |
| Authorized staff can select an edition from a search result and retrieve that edition's complete details and the physical copies of it. |
| A retrieval carries a summary of the work the edition belongs to, so the work's title need not be looked up separately. |
| Authorized staff can register a physical copy against an edition, and it is recorded against that edition only. |
| Authorized staff can retire an edition, and the work's other editions are unaffected. |
| Authorized staff can return a retired edition to the registered state. |
| Registering a physical copy behaves as it did before this change. |
| Updating bibliographic information behaves as it did before this change. |
| Retiring a record behaves as it did before this change. |
| A record written under the previous change is found by search after this change, without having been recreated or migrated. |
| A record written under the previous change is retrieved in full after this change, without having been recreated or migrated. |
| A record written under the previous change can be updated after this change. |
| A record written under the previous change can be retired after this change. |
| A record written under the previous change can be reinstated after this change. |
| A record written under the previous change appears as an edition of a work with one edition. |
| No operation staff had before this change has been withdrawn. |
| Every business operation performed against the extended catalog can be traced and audited afterwards. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Work | Its title and author together. | Their titles and authors match. |
| Edition | Its title, author and publication year together, as the previous change established. | Their publication year matches and their titles and authors match. |
| Physical Copy | The barcode the library assigns to it. | Their barcodes match. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Work | — | Registered | Authorized staff register an edition of a work the catalog does not yet hold. | None beyond the first edition being registered with it. |
| Edition | — | Registered | Authorized staff register an edition against a work, existing or created by this registration. | None — the work's other editions are unaffected. |
| Edition | Registered | Retired | Authorized staff judge the edition's record obsolete and retire it. | None — the work's other editions and the edition's physical copies are unaffected. |
| Edition | Retired | Registered | Authorized staff return the retired edition to the registered state. | None. |
| Physical Copy | — | Registered | Authorized staff register the copy against a registered edition. | None. |
| Physical Copy | Registered | Retired | Authorized staff retire a copy that is lost or damaged. | None — the edition is unaffected, including when it is the last copy. |
| Physical Copy | Retired | Registered | Authorized staff return the retired copy to the registered state. | None. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Register an edition | Its title, author and publication year match a registered edition. | That identity identifies an edition; the edition already exists, and a further copy is what staff register instead. |
| Register an edition | No work is named and none is created with it. | Every edition belongs to exactly one work. |
| Register a work | No edition is offered with it. | The first edition creates the work; a work is never registered without an edition. |
| Register a physical copy | The edition it names is not registered. | Each physical copy belongs to exactly one edition. |
| Retire a work | Always. | A work is not retired; a work whose editions are all retired is simply that. |
| Any catalog operation | The staff member performing it is not authorized. | Only authorized staff may perform catalog operations. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Identifiers assigned to a publication, including multiple ISBN values | A follow-on governed change for identifiers | This change defines an edition. |
| A governed subject taxonomy | A follow-on governed change for taxonomy | The business chooses to take it up. |
| Digital resources associated with catalog records | A follow-on governed change for digital resources | The business chooses to take it up. |
| Images associated with catalog records | A follow-on governed change for images | The business chooses to take it up. |
| Which staff are authorized | The staff function | A future governed change introduces staff authorization. |

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
