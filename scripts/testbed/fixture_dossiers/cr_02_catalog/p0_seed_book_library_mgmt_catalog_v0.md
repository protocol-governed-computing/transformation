# Change Seed — book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 0 — Change Seed
  CR: cr_02_catalog
  Status: DRAFT
  Feeds: Stage 1 — Change Request
registers:
  subdomain_purpose: |2

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
  cr_type:
    columns:
    - Subdomain
    - Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE)
    - Rationale
    rows:
    - Subdomain: catalog
      Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE): EXTEND_SUBDOMAIN
      Rationale: The change extends the existing catalog function of the existing book_library_mgmt project. It introduces no new library function, adds the Work above the records the previous change established, and withdraws no capability staff have today.
  business_vocabulary:
    columns:
    - Term
    - Definition
    rows:
    - Term: book_library_mgmt
      Definition: The existing project governing the library of books, across ten functions of which catalog is one.
    - Term: Catalog
      Definition: The function holding the library's authoritative description of the materials it holds.
    - Term: Work
      Definition: A published work, recognizable as one thing across the editions in which it is published, identified by its title and author.
    - Term: Edition
      Definition: A publication of a work, identified by its title, author and publication year; editions of one work share a title and an author and differ by publication year. The record the previous change calls a Book is an edition.
    - Term: Book
      Definition: The name the previous change gives to what this change calls an edition.
    - Term: Edition Summary
      Definition: Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean.
    - Term: Work Summary
      Definition: A short description of the work an edition belongs to, carried in that edition's retrieval so the work's title need not be looked up separately.
    - Term: Bibliographic Information
      Definition: An edition's descriptive content, as established by the previous change.
    - Term: Bibliographic Accuracy
      Definition: The catalog describing what the library holds as it actually is, which creating separate book records for editions of one work compromises.
    - Term: Physical Copy
      Definition: An individual copy the library owns, belonging to exactly one edition.
    - Term: Existing Catalog Record
      Definition: A catalog record written under the previous governed change, before this one.
    - Term: Authorized Staff
      Definition: A library staff member permitted to perform catalog operations.
    - Term: Business Operation
      Definition: An action performed against the catalog that must be traceable and auditable.
    - Term: Capability Loss
      Definition: An operation withdrawn from staff or a record made unreachable; what this change promises will not happen, as distinct from a behavior deliberately extended.
  requested_outcomes:
    columns:
    - Outcome
    rows:
    - Outcome: The catalog can represent a published work that exists in more than one edition.
    - Outcome: Authorized staff can register additional editions of an existing work.
    - Outcome: Authorized staff can search the catalog and receive one result per matching work rather than one per edition.
    - Outcome: Authorized staff can choose the edition they mean from a search result and retrieve that edition's complete details.
    - Outcome: No capability staff have today is withdrawn and no existing record becomes unreachable.
    - Outcome: Records written under the previous governed change remain valid and continue to function without recreation or migration.
    - Outcome: Every business operation remains traceable and auditable.
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    rows:
    - Fact: This change extends the existing book_library_mgmt system.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: 'The overall project scope continues to cover ten library functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: This change extends the existing catalog function and introduces no new library function.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The purpose of the change is to allow the catalog to represent a published work that exists in more than one edition.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Many published works exist in multiple editions.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Editions of one work differ in publication date, publisher, format or content revision while remaining recognizably the same work.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The current catalog cannot distinguish editions without creating separate book records or compromising bibliographic accuracy.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The current catalog adequately manages books, physical copies and basic bibliographic information.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: As the collection grows, staff increasingly meet situations that cannot be represented accurately within the current model.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The record the previous change calls a Book is an edition, and always was; the library did not discover this until it met a work published more than once.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: What this change adds is the Work, the abstraction above the existing record.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: No existing record is redefined, no existing operation is withdrawn, and nothing already catalogued needs recreating.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: An edition is identified by its title, author and publication year — the identity the previous change already established.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Editions of one work share a title and an author and differ by publication year.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The identity of title, author and publication year distinguishes editions today and continues to; it was never an identity for the work.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A work is identified by its title and author.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Two works are the same work when their titles and authors match.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A physical copy belongs to exactly one edition, exactly as it belongs to exactly one book today.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Multiple editions do not share physical copies.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Retiring an edition is what retiring a book is today, it cascades to nothing, and an edition may be retired independently of the work's other editions.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A work is not retired; a work whose editions are all retired is simply that.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The first edition creates the work; a work is never registered without an edition, exactly as a book is never registered without a copy.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A search returns one result per matching work, carrying enough of a summary of that work's editions for staff to choose the edition they mean.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Three near-identical results for one work is what the library is trying to stop seeing.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: 'Retrieval stays edition retrieval: staff select an edition and receive that edition''s complete details and the physical copies of it, together with a short summary of the work it belongs to.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Each existing catalog record is an edition, grouped under the work its title and author name.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: No migration is required; existing records remain valid as written.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A record written before this change is an edition of a work with one edition.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: No capability is lost and no existing record becomes unreachable.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: 'Search and retrieval are deliberately extended: search groups its results by work, and retrieval carries a summary of the work.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Every other existing operation behaves as it does today.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The promise of no regression is a promise that nothing is lost, not that nothing changes.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete details are the capabilities that must survive this change.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Every business operation shall remain traceable and auditable.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The promise that existing records remain valid is about records written under the previous change and read under this one, and is not satisfied by the catalog merely continuing to compile.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A record written before this change must still be found by search, retrieved in full, updated, retired and reinstated.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Multiple identifiers, a governed subject taxonomy, digital resources and images are further catalog needs the library has, each excluded from this change because each rests on the edition question and could not be settled before it was.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Different publishers, distributors or historical editions may assign different ISBN values to the same publication, and the catalog currently assumes a single identifying value.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: What an ISBN identifies — a work, an edition or a printing — is not answerable until an edition is defined.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The library wishes to organize its collection using a governed taxonomy rather than unrestricted subject text, for consistency of cataloging and more accurate searching and reporting.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Library collections increasingly include electronic editions, supplementary downloadable material, publisher resources and external reference links, which staff require the ability to associate with catalog records without changing the circulation model.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Staff require the ability to associate one or more images, such as cover images or scanned illustrations, with catalog records.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Each deferred need is a governed change of its own, in the order the business chooses.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Circulation, patron management, reservations, acquisitions, inventory management, notifications, reporting and staff authorization are excluded from this release, except where existing catalog behavior depends upon them.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The remaining project functions are named, planned, and outside the scope of this governed extension.
      Certainty (HIGH, MEDIUM, LOW): HIGH
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    rows:
    - Belief: The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change.
      Why It Matters: The change is classified EXTEND_SUBDOMAIN on that basis; if the catalog is not present, this is not an extension.
      Verification Goal: Confirm the pinned composition carries the book_library_mgmt catalog.
    - Belief: The catalog is believed to hold bibliographic records and physical copies of library materials.
      Why It Matters: 'The change rests on what the existing record describes: the claim that a Book record is already an edition is a claim about those records.'
      Verification Goal: Confirm what the catalog's records describe in the pinned composition.
    - Belief: A book is believed to be identified by title, author and publication year.
      Why It Matters: The whole shape of this change follows from that identity being the edition's and not the work's. If the composition identifies a book differently, editions are not already distinguished.
      Verification Goal: Confirm how the composition identifies a book.
    - Belief: A physical copy is believed to belong to exactly one book.
      Why It Matters: It is what makes a copy already a copy of an edition, with no change to copies at all.
      Verification Goal: Confirm what a physical copy is registered against in the composition.
    - Belief: The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details.
      Why It Matters: These are the capabilities that must survive; the claim that nothing is lost cannot be tested against capabilities that do not exist as believed.
      Verification Goal: Confirm which catalog operations the composition provides.
    - Belief: A retired record is believed to be reinstatable.
      Why It Matters: The existing-records promise requires a record written before this change to be retired and reinstated after it.
      Verification Goal: Confirm whether the composition provides reinstatement.
    - Belief: Records written under the previous change are believed to exist and to be readable.
      Why It Matters: The existing-records promise is about data, and is unfalsifiable if no such data exists.
      Verification Goal: Confirm that records written by the previous catalog capability can be read.
  assumptions:
    columns:
    - Assumption
    - Basis
    rows:
    - Assumption: The ten project functions and the deferred catalog needs are named to establish future scope, not to be governed by this change.
      Basis: The statement names them and declares each excluded from this change.
  constraints:
    columns:
    - Constraint
    - Source
    rows:
    - Constraint: No capability staff have today may be withdrawn and no existing record may become unreachable.
      Source: Business policy
    - Constraint: Existing catalog records must remain valid without recreation or migration, demonstrated against records written under the previous change.
      Source: Business policy
    - Constraint: Only search and retrieval may be extended; every other existing operation must behave as it does today.
      Source: Business policy
    - Constraint: Multiple identifiers, governed subject taxonomy, digital resources and images must not be designed into this change.
      Source: Business policy
    - Constraint: Every business operation must remain traceable and auditable.
      Source: Business policy
  business_invariants:
    columns:
    - Invariant
    rows:
    - Invariant: Each edition belongs to exactly one work.
    - Invariant: Each physical copy belongs to exactly one edition.
    - Invariant: No two works share the same title and author.
    - Invariant: No two editions of a work share the same publication year.
    - Invariant: Every work has at least one edition.
    - Invariant: A record written under the previous change remains valid and usable without recreation.
    - Invariant: Every business operation performed against the catalog is traceable and auditable.
    - Invariant: The catalog describes what the library holds without compromising bibliographic accuracy.
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    rows:
    - Object: Work
      State: Registered
      Meaning: The work has been registered with its first edition and the catalog holds its authoritative record.
    - Object: Edition
      State: Registered
      Meaning: The edition has been registered against exactly one work; this is what the previous change calls a registered book.
    - Object: Edition
      State: Retired
      Meaning: The edition's record has been judged obsolete and is no longer to be used; this is what the previous change calls a retired book, and staff may return it to Registered.
    - Object: Physical Copy
      State: Registered
      Meaning: The copy has been registered against exactly one edition.
    - Object: Physical Copy
      State: Retired
      Meaning: The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered.
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    rows:
    - Event: Work Registered
      When It Occurs: When authorized staff register an edition of a work the catalog does not yet hold.
      Significance: A work enters the catalog, created by the edition that evidences it.
    - Event: Edition Registered
      When It Occurs: When authorized staff register an additional edition of an existing work.
      Significance: The catalog records a further edition of a work it already holds.
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    rows:
    - Business Object: Work record
      Authoritative Owner: Catalog
    - Business Object: Edition record
      Authoritative Owner: Catalog
    - Business Object: Physical copy record
      Authoritative Owner: Catalog
    - Business Object: Existing catalog records
      Authoritative Owner: Catalog
    - Business Object: The judgement that an edition is obsolete
      Authoritative Owner: Authorized staff
  out_of_scope:
    columns:
    - Item
    - Reason
    rows:
    - Item: Multiple identifiers
      Reason: A further catalog need, deferred to a governed change of its own; what an ISBN identifies could not be answered until an edition was defined.
    - Item: Governed subject taxonomy
      Reason: A further catalog need, deferred to a governed change of its own.
    - Item: Digital resources
      Reason: A further catalog need, deferred to a governed change of its own.
    - Item: Images
      Reason: A further catalog need, deferred to a governed change of its own.
    - Item: Retirement of a work
      Reason: A work is not retired; a work whose editions are all retired is simply that.
    - Item: Migration of existing records
      Reason: No migration is required; existing records remain valid as written.
    - Item: Circulation
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
    - Item: Patron management
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
    - Item: Reservations
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
    - Item: Acquisitions
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
    - Item: Inventory management
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
    - Item: Notifications
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
    - Item: Reporting
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
    - Item: Staff authorization
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
    - Item: Policy
      Reason: A project function, adjacent to this change and outside its scope.
  governance_scope:
    columns:
    - Scope Item
    - Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT)
    rows:
    - Scope Item: catalog
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): EXTENDED
    - Scope Item: circulation
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: patron
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: staff
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: reservations
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: acquisitions
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: inventory
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: notifications
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: policy
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: reporting
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
  clarification_requests:
    columns:
    - Question
    - Why Needed
    - Blocking (YES, NO)
    - Owner (HUMAN, SNAPSHOT, GOVERNANCE)
    rows: []
  acceptance_criteria:
    columns:
    - Criterion
    rows:
    - Criterion: Authorized staff can register an edition of a work the catalog does not yet hold, and the catalog then holds one work with one edition.
    - Criterion: Authorized staff can register an additional edition of an existing work, and it is recorded against that work only.
    - Criterion: A registration whose title, author and publication year match a registered edition is refused.
    - Criterion: Two editions sharing a title and an author, differing by publication year, are grouped under one work.
    - Criterion: A search for a work with three editions returns one result, not three.
    - Criterion: A search result carries enough of a summary of the work's editions for staff to choose the edition they mean.
    - Criterion: Authorized staff can select an edition from a search result and retrieve that edition's complete details and the physical copies of it.
    - Criterion: A retrieval carries a summary of the work the edition belongs to, so the work's title need not be looked up separately.
    - Criterion: Authorized staff can register a physical copy against an edition, and it is recorded against that edition only.
    - Criterion: Authorized staff can retire an edition, and the work's other editions are unaffected.
    - Criterion: Authorized staff can return a retired edition to the registered state.
    - Criterion: Registering a physical copy behaves as it did before this change.
    - Criterion: Updating bibliographic information behaves as it did before this change.
    - Criterion: Retiring a record behaves as it did before this change.
    - Criterion: A record written under the previous change is found by search after this change, without having been recreated or migrated.
    - Criterion: A record written under the previous change is retrieved in full after this change, without having been recreated or migrated.
    - Criterion: A record written under the previous change can be updated after this change.
    - Criterion: A record written under the previous change can be retired after this change.
    - Criterion: A record written under the previous change can be reinstated after this change.
    - Criterion: A record written under the previous change appears as an edition of a work with one edition.
    - Criterion: No operation staff had before this change has been withdrawn.
    - Criterion: Every business operation performed against the extended catalog can be traced and audited afterwards.
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    rows:
    - Business Object: Work
      Identified By: Its title and author together.
      Two Are The Same When: Their titles and authors match.
    - Business Object: Edition
      Identified By: Its title, author and publication year together, as the previous change established.
      Two Are The Same When: Their publication year matches and their titles and authors match.
    - Business Object: Physical Copy
      Identified By: The barcode the library assigns to it.
      Two Are The Same When: Their barcodes match.
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    rows:
    - Object: Work
      From State: —
      To State: Registered
      Triggered By: Authorized staff register an edition of a work the catalog does not yet hold.
      Cascade: None beyond the first edition being registered with it.
    - Object: Edition
      From State: —
      To State: Registered
      Triggered By: Authorized staff register an edition against a work, existing or created by this registration.
      Cascade: None — the work's other editions are unaffected.
    - Object: Edition
      From State: Registered
      To State: Retired
      Triggered By: Authorized staff judge the edition's record obsolete and retire it.
      Cascade: None — the work's other editions and the edition's physical copies are unaffected.
    - Object: Edition
      From State: Retired
      To State: Registered
      Triggered By: Authorized staff return the retired edition to the registered state.
      Cascade: None.
    - Object: Physical Copy
      From State: —
      To State: Registered
      Triggered By: Authorized staff register the copy against a registered edition.
      Cascade: None.
    - Object: Physical Copy
      From State: Registered
      To State: Retired
      Triggered By: Authorized staff retire a copy that is lost or damaged.
      Cascade: None — the edition is unaffected, including when it is the last copy.
    - Object: Physical Copy
      From State: Retired
      To State: Registered
      Triggered By: Authorized staff return the retired copy to the registered state.
      Cascade: None.
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    rows:
    - Operation: Register an edition
      Refused When: Its title, author and publication year match a registered edition.
      Business Reason: That identity identifies an edition; the edition already exists, and a further copy is what staff register instead.
    - Operation: Register an edition
      Refused When: No work is named and none is created with it.
      Business Reason: Every edition belongs to exactly one work.
    - Operation: Register a work
      Refused When: No edition is offered with it.
      Business Reason: The first edition creates the work; a work is never registered without an edition.
    - Operation: Register a physical copy
      Refused When: The edition it names is not registered.
      Business Reason: Each physical copy belongs to exactly one edition.
    - Operation: Retire a work
      Refused When: Always.
      Business Reason: A work is not retired; a work whose editions are all retired is simply that.
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Business Reason: Only authorized staff may perform catalog operations.
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    rows:
    - Business Object: Identifiers assigned to a publication, including multiple ISBN values
      Deferred To: A follow-on governed change for identifiers
      Until: This change defines an edition.
    - Business Object: A governed subject taxonomy
      Deferred To: A follow-on governed change for taxonomy
      Until: The business chooses to take it up.
    - Business Object: Digital resources associated with catalog records
      Deferred To: A follow-on governed change for digital resources
      Until: The business chooses to take it up.
    - Business Object: Images associated with catalog records
      Deferred To: A follow-on governed change for images
      Until: The business chooses to take it up.
    - Business Object: Which staff are authorized
      Deferred To: The staff function
      Until: A future governed change introduces staff authorization.
```

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
