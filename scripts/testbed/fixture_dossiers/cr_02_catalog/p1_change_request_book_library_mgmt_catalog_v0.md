# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 1 — Change Request (Clarification & Fact Capture)
  CR: cr_02_catalog
  Status: DRAFT
  Feeds: Stage 2 — Domain Model Discovery
registers:
  cr_type:
    columns:
    - Subdomain
    - Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE)
    - Rationale
    - Source Finding
    rows:
    - Subdomain: catalog
      Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE): EXTEND_SUBDOMAIN
      Rationale: The change extends the existing catalog function of the existing book_library_mgmt project. It introduces no new library function, adds the Work above the records the previous change established, and withdraws no capability staff have today.
      Source Finding: 'CR seed §1 CR Type #1'
  business_vocabulary:
    columns:
    - Term
    - Definition
    - Source Finding
    rows:
    - Term: book_library_mgmt
      Definition: The existing project governing the library of books, across ten functions of which catalog is one.
      Source Finding: 'CR seed §2 Business Vocabulary #1'
    - Term: Catalog
      Definition: The function holding the library's authoritative description of the materials it holds.
      Source Finding: 'CR seed §2 Business Vocabulary #2'
    - Term: Work
      Definition: A published work, recognizable as one thing across the editions in which it is published, identified by its title and author.
      Source Finding: 'CR seed §2 Business Vocabulary #3'
    - Term: Edition
      Definition: A publication of a work, identified by its title, author and publication year; editions of one work share a title and an author and differ by publication year. The record the previous change calls a Book is an edition.
      Source Finding: 'CR seed §2 Business Vocabulary #4'
    - Term: Book
      Definition: The name the previous change gives to what this change calls an edition.
      Source Finding: 'CR seed §2 Business Vocabulary #5'
    - Term: Edition Summary
      Definition: Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean.
      Source Finding: 'CR seed §2 Business Vocabulary #6'
    - Term: Work Summary
      Definition: A short description of the work an edition belongs to, carried in that edition's retrieval so the work's title need not be looked up separately.
      Source Finding: 'CR seed §2 Business Vocabulary #7'
    - Term: Bibliographic Information
      Definition: An edition's descriptive content, as established by the previous change.
      Source Finding: 'CR seed §2 Business Vocabulary #8'
    - Term: Bibliographic Accuracy
      Definition: The catalog describing what the library holds as it actually is, which creating separate book records for editions of one work compromises.
      Source Finding: 'CR seed §2 Business Vocabulary #9'
    - Term: Physical Copy
      Definition: An individual copy the library owns, belonging to exactly one edition.
      Source Finding: 'CR seed §2 Business Vocabulary #10'
    - Term: Existing Catalog Record
      Definition: A catalog record written under the previous governed change, before this one.
      Source Finding: 'CR seed §2 Business Vocabulary #11'
    - Term: Authorized Staff
      Definition: A library staff member permitted to perform catalog operations.
      Source Finding: 'CR seed §2 Business Vocabulary #12'
    - Term: Business Operation
      Definition: An action performed against the catalog that must be traceable and auditable.
      Source Finding: 'CR seed §2 Business Vocabulary #13'
    - Term: Capability Loss
      Definition: An operation withdrawn from staff or a record made unreachable; what this change promises will not happen, as distinct from a behavior deliberately extended.
      Source Finding: 'CR seed §2 Business Vocabulary #14'
  requested_outcomes:
    columns:
    - Outcome
    - Source Finding
    rows:
    - Outcome: The catalog can represent a published work that exists in more than one edition.
      Source Finding: 'CR seed §3 Requested Outcomes #1'
    - Outcome: Authorized staff can register additional editions of an existing work.
      Source Finding: 'CR seed §3 Requested Outcomes #2'
    - Outcome: Authorized staff can search the catalog and receive one result per matching work rather than one per edition.
      Source Finding: 'CR seed §3 Requested Outcomes #3'
    - Outcome: Authorized staff can choose the edition they mean from a search result and retrieve that edition's complete details.
      Source Finding: 'CR seed §3 Requested Outcomes #4'
    - Outcome: No capability staff have today is withdrawn and no existing record becomes unreachable.
      Source Finding: 'CR seed §3 Requested Outcomes #5'
    - Outcome: Records written under the previous governed change remain valid and continue to function without recreation or migration.
      Source Finding: 'CR seed §3 Requested Outcomes #6'
    - Outcome: Every business operation remains traceable and auditable.
      Source Finding: 'CR seed §3 Requested Outcomes #7'
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    - Source Finding
    rows:
    - Fact: This change extends the existing book_library_mgmt system.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #1'
    - Fact: 'The overall project scope continues to cover ten library functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #2'
    - Fact: This change extends the existing catalog function and introduces no new library function.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #3'
    - Fact: The purpose of the change is to allow the catalog to represent a published work that exists in more than one edition.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #4'
    - Fact: Many published works exist in multiple editions.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #5'
    - Fact: Editions of one work differ in publication date, publisher, format or content revision while remaining recognizably the same work.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #6'
    - Fact: The current catalog cannot distinguish editions without creating separate book records or compromising bibliographic accuracy.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #7'
    - Fact: The current catalog adequately manages books, physical copies and basic bibliographic information.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #8'
    - Fact: As the collection grows, staff increasingly meet situations that cannot be represented accurately within the current model.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #9'
    - Fact: The record the previous change calls a Book is an edition, and always was; the library did not discover this until it met a work published more than once.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #10'
    - Fact: What this change adds is the Work, the abstraction above the existing record.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #11'
    - Fact: No existing record is redefined, no existing operation is withdrawn, and nothing already catalogued needs recreating.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #12'
    - Fact: An edition is identified by its title, author and publication year — the identity the previous change already established.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #13'
    - Fact: Editions of one work share a title and an author and differ by publication year.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #14'
    - Fact: The identity of title, author and publication year distinguishes editions today and continues to; it was never an identity for the work.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #15'
    - Fact: A work is identified by its title and author.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #16'
    - Fact: Two works are the same work when their titles and authors match.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #17'
    - Fact: A physical copy belongs to exactly one edition, exactly as it belongs to exactly one book today.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #18'
    - Fact: Multiple editions do not share physical copies.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #19'
    - Fact: Retiring an edition is what retiring a book is today, it cascades to nothing, and an edition may be retired independently of the work's other editions.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #20'
    - Fact: A work is not retired; a work whose editions are all retired is simply that.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #21'
    - Fact: The first edition creates the work; a work is never registered without an edition, exactly as a book is never registered without a copy.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #22'
    - Fact: A search returns one result per matching work, carrying enough of a summary of that work's editions for staff to choose the edition they mean.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #23'
    - Fact: Three near-identical results for one work is what the library is trying to stop seeing.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #24'
    - Fact: 'Retrieval stays edition retrieval: staff select an edition and receive that edition''s complete details and the physical copies of it, together with a short summary of the work it belongs to.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #25'
    - Fact: Each existing catalog record is an edition, grouped under the work its title and author name.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #26'
    - Fact: No migration is required; existing records remain valid as written.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #27'
    - Fact: A record written before this change is an edition of a work with one edition.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #28'
    - Fact: No capability is lost and no existing record becomes unreachable.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #29'
    - Fact: 'Search and retrieval are deliberately extended: search groups its results by work, and retrieval carries a summary of the work.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #30'
    - Fact: Every other existing operation behaves as it does today.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #31'
    - Fact: The promise of no regression is a promise that nothing is lost, not that nothing changes.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #32'
    - Fact: Registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete details are the capabilities that must survive this change.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #33'
    - Fact: Every business operation shall remain traceable and auditable.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #34'
    - Fact: The promise that existing records remain valid is about records written under the previous change and read under this one, and is not satisfied by the catalog merely continuing to compile.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #35'
    - Fact: A record written before this change must still be found by search, retrieved in full, updated, retired and reinstated.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #36'
    - Fact: Multiple identifiers, a governed subject taxonomy, digital resources and images are further catalog needs the library has, each excluded from this change because each rests on the edition question and could not be settled before it was.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #37'
    - Fact: Different publishers, distributors or historical editions may assign different ISBN values to the same publication, and the catalog currently assumes a single identifying value.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #38'
    - Fact: What an ISBN identifies — a work, an edition or a printing — is not answerable until an edition is defined.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #39'
    - Fact: The library wishes to organize its collection using a governed taxonomy rather than unrestricted subject text, for consistency of cataloging and more accurate searching and reporting.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #40'
    - Fact: Library collections increasingly include electronic editions, supplementary downloadable material, publisher resources and external reference links, which staff require the ability to associate with catalog records without changing the circulation model.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #41'
    - Fact: Staff require the ability to associate one or more images, such as cover images or scanned illustrations, with catalog records.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #42'
    - Fact: Each deferred need is a governed change of its own, in the order the business chooses.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #43'
    - Fact: Circulation, patron management, reservations, acquisitions, inventory management, notifications, reporting and staff authorization are excluded from this release, except where existing catalog behavior depends upon them.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #44'
    - Fact: The remaining project functions are named, planned, and outside the scope of this governed extension.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #45'
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    - Source Finding
    rows:
    - Belief: The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change.
      Why It Matters: The change is classified EXTEND_SUBDOMAIN on that basis; if the catalog is not present, this is not an extension.
      Verification Goal: Confirm the pinned composition carries the book_library_mgmt catalog.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #1'
    - Belief: The catalog is believed to hold bibliographic records and physical copies of library materials.
      Why It Matters: 'The change rests on what the existing record describes: the claim that a Book record is already an edition is a claim about those records.'
      Verification Goal: Confirm what the catalog's records describe in the pinned composition.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #2'
    - Belief: A book is believed to be identified by title, author and publication year.
      Why It Matters: The whole shape of this change follows from that identity being the edition's and not the work's. If the composition identifies a book differently, editions are not already distinguished.
      Verification Goal: Confirm how the composition identifies a book.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #3'
    - Belief: A physical copy is believed to belong to exactly one book.
      Why It Matters: It is what makes a copy already a copy of an edition, with no change to copies at all.
      Verification Goal: Confirm what a physical copy is registered against in the composition.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #4'
    - Belief: The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details.
      Why It Matters: These are the capabilities that must survive; the claim that nothing is lost cannot be tested against capabilities that do not exist as believed.
      Verification Goal: Confirm which catalog operations the composition provides.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #5'
    - Belief: A retired record is believed to be reinstatable.
      Why It Matters: The existing-records promise requires a record written before this change to be retired and reinstated after it.
      Verification Goal: Confirm whether the composition provides reinstatement.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #6'
    - Belief: Records written under the previous change are believed to exist and to be readable.
      Why It Matters: The existing-records promise is about data, and is unfalsifiable if no such data exists.
      Verification Goal: Confirm that records written by the previous catalog capability can be read.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #7'
  assumptions:
    columns:
    - Assumption
    - Basis
    - Source Finding
    rows:
    - Assumption: The ten project functions and the deferred catalog needs are named to establish future scope, not to be governed by this change.
      Basis: The statement names them and declares each excluded from this change.
      Source Finding: 'CR seed §6 Assumptions #1'
  constraints:
    columns:
    - Constraint
    - Source
    - Source Finding
    rows:
    - Constraint: No capability staff have today may be withdrawn and no existing record may become unreachable.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #1'
    - Constraint: Existing catalog records must remain valid without recreation or migration, demonstrated against records written under the previous change.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #2'
    - Constraint: Only search and retrieval may be extended; every other existing operation must behave as it does today.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #3'
    - Constraint: Multiple identifiers, governed subject taxonomy, digital resources and images must not be designed into this change.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #4'
    - Constraint: Every business operation must remain traceable and auditable.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #5'
  business_invariants:
    columns:
    - Invariant
    - Source Finding
    rows:
    - Invariant: Each edition belongs to exactly one work.
      Source Finding: 'CR seed §8 Business Invariants #1'
    - Invariant: Each physical copy belongs to exactly one edition.
      Source Finding: 'CR seed §8 Business Invariants #2'
    - Invariant: No two works share the same title and author.
      Source Finding: 'CR seed §8 Business Invariants #3'
    - Invariant: No two editions of a work share the same publication year.
      Source Finding: 'CR seed §8 Business Invariants #4'
    - Invariant: Every work has at least one edition.
      Source Finding: 'CR seed §8 Business Invariants #5'
    - Invariant: A record written under the previous change remains valid and usable without recreation.
      Source Finding: 'CR seed §8 Business Invariants #6'
    - Invariant: Every business operation performed against the catalog is traceable and auditable.
      Source Finding: 'CR seed §8 Business Invariants #7'
    - Invariant: The catalog describes what the library holds without compromising bibliographic accuracy.
      Source Finding: 'CR seed §8 Business Invariants #8'
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    - Source Finding
    rows:
    - Object: Work
      State: Registered
      Meaning: The work has been registered with its first edition and the catalog holds its authoritative record.
      Source Finding: 'CR seed §9 Lifecycle States #1'
    - Object: Edition
      State: Registered
      Meaning: The edition has been registered against exactly one work; this is what the previous change calls a registered book.
      Source Finding: 'CR seed §9 Lifecycle States #2'
    - Object: Edition
      State: Retired
      Meaning: The edition's record has been judged obsolete and is no longer to be used; this is what the previous change calls a retired book, and staff may return it to Registered.
      Source Finding: 'CR seed §9 Lifecycle States #3'
    - Object: Physical Copy
      State: Registered
      Meaning: The copy has been registered against exactly one edition.
      Source Finding: 'CR seed §9 Lifecycle States #4'
    - Object: Physical Copy
      State: Retired
      Meaning: The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered.
      Source Finding: 'CR seed §9 Lifecycle States #5'
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    - Source Finding
    rows:
    - Event: Work Registered
      When It Occurs: When authorized staff register an edition of a work the catalog does not yet hold.
      Significance: A work enters the catalog, created by the edition that evidences it.
      Source Finding: 'CR seed §10 Business Events #1'
    - Event: Edition Registered
      When It Occurs: When authorized staff register an additional edition of an existing work.
      Significance: The catalog records a further edition of a work it already holds.
      Source Finding: 'CR seed §10 Business Events #2'
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    - Source Finding
    rows:
    - Business Object: Work record
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #1'
    - Business Object: Edition record
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #2'
    - Business Object: Physical copy record
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #3'
    - Business Object: Existing catalog records
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #4'
    - Business Object: The judgement that an edition is obsolete
      Authoritative Owner: Authorized staff
      Source Finding: 'CR seed §11 Authority Boundaries #5'
  out_of_scope:
    columns:
    - Item
    - Reason
    - Source Finding
    rows:
    - Item: Multiple identifiers
      Reason: A further catalog need, deferred to a governed change of its own; what an ISBN identifies could not be answered until an edition was defined.
      Source Finding: 'CR seed §12 Out of Scope #1'
    - Item: Governed subject taxonomy
      Reason: A further catalog need, deferred to a governed change of its own.
      Source Finding: 'CR seed §12 Out of Scope #2'
    - Item: Digital resources
      Reason: A further catalog need, deferred to a governed change of its own.
      Source Finding: 'CR seed §12 Out of Scope #3'
    - Item: Images
      Reason: A further catalog need, deferred to a governed change of its own.
      Source Finding: 'CR seed §12 Out of Scope #4'
    - Item: Retirement of a work
      Reason: A work is not retired; a work whose editions are all retired is simply that.
      Source Finding: 'CR seed §12 Out of Scope #5'
    - Item: Migration of existing records
      Reason: No migration is required; existing records remain valid as written.
      Source Finding: 'CR seed §12 Out of Scope #6'
    - Item: Circulation
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
      Source Finding: 'CR seed §12 Out of Scope #7'
    - Item: Patron management
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
      Source Finding: 'CR seed §12 Out of Scope #8'
    - Item: Reservations
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
      Source Finding: 'CR seed §12 Out of Scope #9'
    - Item: Acquisitions
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
      Source Finding: 'CR seed §12 Out of Scope #10'
    - Item: Inventory management
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
      Source Finding: 'CR seed §12 Out of Scope #11'
    - Item: Notifications
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
      Source Finding: 'CR seed §12 Out of Scope #12'
    - Item: Reporting
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
      Source Finding: 'CR seed §12 Out of Scope #13'
    - Item: Staff authorization
      Reason: Excluded from this release, except where existing catalog behavior depends upon it.
      Source Finding: 'CR seed §12 Out of Scope #14'
    - Item: Policy
      Reason: A project function, adjacent to this change and outside its scope.
      Source Finding: 'CR seed §12 Out of Scope #15'
  governance_scope:
    columns:
    - Scope Item
    - Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT)
    - Source Finding
    rows:
    - Scope Item: catalog
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): EXTENDED
      Source Finding: 'CR seed §13 Governance Scope #1'
    - Scope Item: circulation
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #2'
    - Scope Item: patron
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #3'
    - Scope Item: staff
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #4'
    - Scope Item: reservations
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #5'
    - Scope Item: acquisitions
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #6'
    - Scope Item: inventory
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #7'
    - Scope Item: notifications
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #8'
    - Scope Item: policy
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #9'
    - Scope Item: reporting
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
      Source Finding: 'CR seed §13 Governance Scope #10'
  clarification_requests:
    columns:
    - Question
    - Why Needed
    - Blocking (YES, NO)
    - Owner (HUMAN, SNAPSHOT, GOVERNANCE)
    - Source Finding
    rows: []
  acceptance_criteria:
    columns:
    - Criterion
    - Source Finding
    rows:
    - Criterion: Authorized staff can register an edition of a work the catalog does not yet hold, and the catalog then holds one work with one edition.
      Source Finding: 'CR seed §15 Acceptance Criteria #1'
    - Criterion: Authorized staff can register an additional edition of an existing work, and it is recorded against that work only.
      Source Finding: 'CR seed §15 Acceptance Criteria #2'
    - Criterion: A registration whose title, author and publication year match a registered edition is refused.
      Source Finding: 'CR seed §15 Acceptance Criteria #3'
    - Criterion: Two editions sharing a title and an author, differing by publication year, are grouped under one work.
      Source Finding: 'CR seed §15 Acceptance Criteria #4'
    - Criterion: A search for a work with three editions returns one result, not three.
      Source Finding: 'CR seed §15 Acceptance Criteria #5'
    - Criterion: A search result carries enough of a summary of the work's editions for staff to choose the edition they mean.
      Source Finding: 'CR seed §15 Acceptance Criteria #6'
    - Criterion: Authorized staff can select an edition from a search result and retrieve that edition's complete details and the physical copies of it.
      Source Finding: 'CR seed §15 Acceptance Criteria #7'
    - Criterion: A retrieval carries a summary of the work the edition belongs to, so the work's title need not be looked up separately.
      Source Finding: 'CR seed §15 Acceptance Criteria #8'
    - Criterion: Authorized staff can register a physical copy against an edition, and it is recorded against that edition only.
      Source Finding: 'CR seed §15 Acceptance Criteria #9'
    - Criterion: Authorized staff can retire an edition, and the work's other editions are unaffected.
      Source Finding: 'CR seed §15 Acceptance Criteria #10'
    - Criterion: Authorized staff can return a retired edition to the registered state.
      Source Finding: 'CR seed §15 Acceptance Criteria #11'
    - Criterion: Registering a physical copy behaves as it did before this change.
      Source Finding: 'CR seed §15 Acceptance Criteria #12'
    - Criterion: Updating bibliographic information behaves as it did before this change.
      Source Finding: 'CR seed §15 Acceptance Criteria #13'
    - Criterion: Retiring a record behaves as it did before this change.
      Source Finding: 'CR seed §15 Acceptance Criteria #14'
    - Criterion: A record written under the previous change is found by search after this change, without having been recreated or migrated.
      Source Finding: 'CR seed §15 Acceptance Criteria #15'
    - Criterion: A record written under the previous change is retrieved in full after this change, without having been recreated or migrated.
      Source Finding: 'CR seed §15 Acceptance Criteria #16'
    - Criterion: A record written under the previous change can be updated after this change.
      Source Finding: 'CR seed §15 Acceptance Criteria #17'
    - Criterion: A record written under the previous change can be retired after this change.
      Source Finding: 'CR seed §15 Acceptance Criteria #18'
    - Criterion: A record written under the previous change can be reinstated after this change.
      Source Finding: 'CR seed §15 Acceptance Criteria #19'
    - Criterion: A record written under the previous change appears as an edition of a work with one edition.
      Source Finding: 'CR seed §15 Acceptance Criteria #20'
    - Criterion: No operation staff had before this change has been withdrawn.
      Source Finding: 'CR seed §15 Acceptance Criteria #21'
    - Criterion: Every business operation performed against the extended catalog can be traced and audited afterwards.
      Source Finding: 'CR seed §15 Acceptance Criteria #22'
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    - Source Finding
    rows:
    - Business Object: Work
      Identified By: Its title and author together.
      Two Are The Same When: Their titles and authors match.
      Source Finding: 'CR seed §16 Identity and Sameness #1'
    - Business Object: Edition
      Identified By: Its title, author and publication year together, as the previous change established.
      Two Are The Same When: Their publication year matches and their titles and authors match.
      Source Finding: 'CR seed §16 Identity and Sameness #2'
    - Business Object: Physical Copy
      Identified By: The barcode the library assigns to it.
      Two Are The Same When: Their barcodes match.
      Source Finding: 'CR seed §16 Identity and Sameness #3'
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    - Source Finding
    rows:
    - Object: Work
      From State: —
      To State: Registered
      Triggered By: Authorized staff register an edition of a work the catalog does not yet hold.
      Cascade: None beyond the first edition being registered with it.
      Source Finding: 'CR seed §17 Lifecycle Transitions #1'
    - Object: Edition
      From State: —
      To State: Registered
      Triggered By: Authorized staff register an edition against a work, existing or created by this registration.
      Cascade: None — the work's other editions are unaffected.
      Source Finding: 'CR seed §17 Lifecycle Transitions #2'
    - Object: Edition
      From State: Registered
      To State: Retired
      Triggered By: Authorized staff judge the edition's record obsolete and retire it.
      Cascade: None — the work's other editions and the edition's physical copies are unaffected.
      Source Finding: 'CR seed §17 Lifecycle Transitions #3'
    - Object: Edition
      From State: Retired
      To State: Registered
      Triggered By: Authorized staff return the retired edition to the registered state.
      Cascade: None.
      Source Finding: 'CR seed §17 Lifecycle Transitions #4'
    - Object: Physical Copy
      From State: —
      To State: Registered
      Triggered By: Authorized staff register the copy against a registered edition.
      Cascade: None.
      Source Finding: 'CR seed §17 Lifecycle Transitions #5'
    - Object: Physical Copy
      From State: Registered
      To State: Retired
      Triggered By: Authorized staff retire a copy that is lost or damaged.
      Cascade: None — the edition is unaffected, including when it is the last copy.
      Source Finding: 'CR seed §17 Lifecycle Transitions #6'
    - Object: Physical Copy
      From State: Retired
      To State: Registered
      Triggered By: Authorized staff return the retired copy to the registered state.
      Cascade: None.
      Source Finding: 'CR seed §17 Lifecycle Transitions #7'
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    - Source Finding
    rows:
    - Operation: Register an edition
      Refused When: Its title, author and publication year match a registered edition.
      Business Reason: That identity identifies an edition; the edition already exists, and a further copy is what staff register instead.
      Source Finding: 'CR seed §18 Operation Refusals #1'
    - Operation: Register an edition
      Refused When: No work is named and none is created with it.
      Business Reason: Every edition belongs to exactly one work.
      Source Finding: 'CR seed §18 Operation Refusals #2'
    - Operation: Register a work
      Refused When: No edition is offered with it.
      Business Reason: The first edition creates the work; a work is never registered without an edition.
      Source Finding: 'CR seed §18 Operation Refusals #3'
    - Operation: Register a physical copy
      Refused When: The edition it names is not registered.
      Business Reason: Each physical copy belongs to exactly one edition.
      Source Finding: 'CR seed §18 Operation Refusals #4'
    - Operation: Retire a work
      Refused When: Always.
      Business Reason: A work is not retired; a work whose editions are all retired is simply that.
      Source Finding: 'CR seed §18 Operation Refusals #5'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Business Reason: Only authorized staff may perform catalog operations.
      Source Finding: 'CR seed §18 Operation Refusals #6'
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Business Object: Identifiers assigned to a publication, including multiple ISBN values
      Deferred To: A follow-on governed change for identifiers
      Until: This change defines an edition.
      Source Finding: 'CR seed §19 Authority Deferrals #1'
    - Business Object: A governed subject taxonomy
      Deferred To: A follow-on governed change for taxonomy
      Until: The business chooses to take it up.
      Source Finding: 'CR seed §19 Authority Deferrals #2'
    - Business Object: Digital resources associated with catalog records
      Deferred To: A follow-on governed change for digital resources
      Until: The business chooses to take it up.
      Source Finding: 'CR seed §19 Authority Deferrals #3'
    - Business Object: Images associated with catalog records
      Deferred To: A follow-on governed change for images
      Until: The business chooses to take it up.
      Source Finding: 'CR seed §19 Authority Deferrals #4'
    - Business Object: Which staff are authorized
      Deferred To: The staff function
      Until: A future governed change introduces staff authorization.
      Source Finding: 'CR seed §19 Authority Deferrals #5'
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
