# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 1 — Change Request (Clarification & Fact Capture)
  CR: cr_01_catalog
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
      Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE): NEW_SUBDOMAIN
      Rationale: book_library_mgmt is proposed as a new project, and the library requires a governed catalog management capability it maintains manually today. It extends nothing that exists.
      Source Finding: 'CR seed §1 CR Type #1'
  business_vocabulary:
    columns:
    - Term
    - Definition
    - Source Finding
    rows:
    - Term: book_library_mgmt
      Definition: The project governing the library of books, across ten functions of which catalog is the first.
      Source Finding: 'CR seed §2 Business Vocabulary #1'
    - Term: Catalog
      Definition: The function holding the library's authoritative description of the materials it holds.
      Source Finding: 'CR seed §2 Business Vocabulary #2'
    - Term: Book
      Definition: A published material the library catalogs, identified by its title, author and publication year. The general term for anything the library catalogs, including published materials that are not books.
      Source Finding: 'CR seed §2 Business Vocabulary #3'
    - Term: Bibliographic Information
      Definition: 'A book''s descriptive content: title, author, publication year and subject.'
      Source Finding: 'CR seed §2 Business Vocabulary #4'
    - Term: Subject
      Definition: What kind of book it is, stated as free text; what staff search on when looking for material rather than for a known title.
      Source Finding: 'CR seed §2 Business Vocabulary #5'
    - Term: Physical Copy
      Definition: An individual copy the library owns, belonging to exactly one book, identified by its barcode.
      Source Finding: 'CR seed §2 Business Vocabulary #6'
    - Term: Barcode
      Definition: The identifier the library assigns to a physical copy, which distinguishes that copy from every other copy the library owns.
      Source Finding: 'CR seed §2 Business Vocabulary #7'
    - Term: Catalog Record
      Definition: The single authoritative record for one book or one physical copy.
      Source Finding: 'CR seed §2 Business Vocabulary #8'
    - Term: Book Details
      Definition: 'The complete description of a registered book: its bibliographic information and the physical copies the library holds of it.'
      Source Finding: 'CR seed §2 Business Vocabulary #9'
    - Term: Obsolete Record
      Definition: A catalog record the library has determined is no longer to be used.
      Source Finding: 'CR seed §2 Business Vocabulary #10'
    - Term: Authorized Staff
      Definition: A library staff member permitted to perform catalog operations.
      Source Finding: 'CR seed §2 Business Vocabulary #11'
    - Term: Business Operation
      Definition: An action performed against the catalog that must be traceable and auditable.
      Source Finding: 'CR seed §2 Business Vocabulary #12'
  requested_outcomes:
    columns:
    - Outcome
    - Source Finding
    rows:
    - Outcome: A single authoritative record exists for each book the library holds.
      Source Finding: 'CR seed §3 Requested Outcomes #1'
    - Outcome: A single authoritative record exists for each physical copy the library owns.
      Source Finding: 'CR seed §3 Requested Outcomes #2'
    - Outcome: Authorized staff can register new books, register physical copies, update bibliographic information, retire obsolete records, search the catalog, and retrieve complete book details.
      Source Finding: 'CR seed §3 Requested Outcomes #3'
    - Outcome: Catalog descriptions are consistent and duplicate entries no longer occur.
      Source Finding: 'CR seed §3 Requested Outcomes #4'
    - Outcome: Materials can be located by what kind of book they are, without the difficulty the manual catalog produces.
      Source Finding: 'CR seed §3 Requested Outcomes #5'
    - Outcome: Every business operation performed against the catalog is traceable and auditable.
      Source Finding: 'CR seed §3 Requested Outcomes #6'
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    - Source Finding
    rows:
    - Fact: The proposed name of the project is book_library_mgmt.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #1'
    - Fact: 'The project scope covers ten functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #2'
    - Fact: The scope of this change request is limited to the catalog function only.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #3'
    - Fact: A community library maintains thousands of books and other published materials.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #4'
    - Fact: '"Book" is the general term for anything the library catalogs, including published materials that are not books.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #5'
    - Fact: Catalog records are maintained manually today.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #6'
    - Fact: Manual maintenance produces inconsistent descriptions, duplicate entries, and difficulty locating materials.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #7'
    - Fact: The library requires a governed catalog management capability providing a single authoritative record for each book and each physical copy it owns.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #8'
    - Fact: A book's bibliographic information is its title, author, publication year and subject.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #9'
    - Fact: A book carries at least one subject and may carry several.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #10'
    - Fact: Subject says what kind of book it is, and is what staff search on when looking for material rather than for a known title.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #11'
    - Fact: A book's subject is free text; the library maintains no list of permitted subjects.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #12'
    - Fact: Staff search the catalog by subject or by title.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #13'
    - Fact: A search returns the bibliographic information of each matching registered book, and nothing about its physical copies.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #14'
    - Fact: Title, author and publication year together identify a book.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #15'
    - Fact: Title and author are compared without regard to letter case or repeated spacing; case and spacing do not change which book is meant.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #16'
    - Fact: Each physical copy belongs to exactly one book.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #17'
    - Fact: Registering a book requires at least one physical copy; a book is never registered without a copy.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #18'
    - Fact: Each physical copy carries a barcode the library assigns, which identifies that copy among all the copies the library owns.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #19'
    - Fact: A physical copy may be retired on its own, when it is lost or damaged.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #20'
    - Fact: A physical copy may be registered against a retired book.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #21'
    - Fact: A catalog record is never deleted; retirement is the only way a record leaves use.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #22'
    - Fact: Authorized staff may return a retired book record or a retired physical copy to the registered state.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #23'
    - Fact: An update to bibliographic information may change the title, author or publication year.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #24'
    - Fact: An update is refused when the changed title, author and publication year would match another registered book.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #25'
    - Fact: 'No retirement follows automatically from another: retiring a book does not retire its copies, and retiring the last copy does not retire the book.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #26'
    - Fact: A registration whose title, author and publication year match a registered book is refused, because the book already exists.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #27'
    - Fact: A retired book is excluded from search results, and its details remain retrievable.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #28'
    - Fact: Retrieving complete book details returns the book's bibliographic information and the physical copies the library holds of it.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #29'
    - Fact: The catalog does not manage which staff are authorized; it requires staff to be authorized.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #30'
    - Fact: Deciding who is authorized belongs to the staff function, which governs library employees.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #31'
    - Fact: Patrons are library users, not employees, and the patron function does not decide staff authorization.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #32'
    - Fact: Only authorized staff may perform catalog operations.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #33'
    - Fact: Every business operation must be traceable and auditable.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #34'
    - Fact: The catalog starts empty; the records staff maintain manually today are not imported by this change.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #35'
    - Fact: 'The operations required of the catalog are: register a new book, register a physical copy, update bibliographic information, retire an obsolete record, search the catalog, retrieve complete book details.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #36'
    - Fact: Borrowing, reservations, fines, patron management, acquisitions and inventory reconciliation are excluded from this release.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #37'
    - Fact: The excluded capabilities are expected to be introduced through future governed change requests.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #38'
    - Fact: The excluded capabilities must not be designed into the initial solution.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #39'
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    - Source Finding
    rows:
    - Belief: book_library_mgmt does not appear to be part of the current software baseline.
      Why It Matters: The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different.
      Verification Goal: Confirm no artifact in the pinned composition carries the book_library_mgmt namespace.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #1'
    - Belief: No capability in the current composition manages a library catalog.
      Why It Matters: This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension.
      Verification Goal: Confirm nothing in the composition registers, describes, searches or retires a catalog record.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #2'
  assumptions:
    columns:
    - Assumption
    - Basis
    - Source Finding
    rows:
    - Assumption: '"Thousands of books" describes the size of the collection and states no performance requirement.'
      Basis: Confirmed by the business author; the statement names no performance target.
      Source Finding: 'CR seed §6 Assumptions #1'
    - Assumption: The library is treated as a single collection; no branch or location distinction is required.
      Basis: Confirmed by the business author; the statement names no branch or location.
      Source Finding: 'CR seed §6 Assumptions #2'
    - Assumption: The nine remaining project functions are named to establish future scope, not to be governed by this change.
      Basis: Confirmed by the business author; the statement limits this change request to catalog only.
      Source Finding: 'CR seed §6 Assumptions #3'
  constraints:
    columns:
    - Constraint
    - Source
    - Source Finding
    rows:
    - Constraint: Capabilities deferred to future change requests must not be designed into this solution.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #1'
    - Constraint: Only authorized staff may perform catalog operations.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #2'
    - Constraint: Every business operation must leave a record that can be traced and audited.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #3'
    - Constraint: A physical copy may never be recorded against more than one book.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #4'
    - Constraint: The catalog must not import the records staff maintain manually today.
      Source: Business policy
      Source Finding: 'CR seed §7 Constraints #5'
  business_invariants:
    columns:
    - Invariant
    - Source Finding
    rows:
    - Invariant: Each physical copy belongs to exactly one book.
      Source Finding: 'CR seed §8 Business Invariants #1'
    - Invariant: Each book the library holds has exactly one authoritative record.
      Source Finding: 'CR seed §8 Business Invariants #2'
    - Invariant: Each physical copy the library owns has exactly one authoritative record.
      Source Finding: 'CR seed §8 Business Invariants #3'
    - Invariant: No two registered books share the same title, author and publication year.
      Source Finding: 'CR seed §8 Business Invariants #4'
    - Invariant: A book carries at least one subject.
      Source Finding: 'CR seed §8 Business Invariants #5'
    - Invariant: No two physical copies the library owns share the same barcode.
      Source Finding: 'CR seed §8 Business Invariants #6'
    - Invariant: No catalog record is ever deleted.
      Source Finding: 'CR seed §8 Business Invariants #7'
    - Invariant: Every business operation performed against the catalog is traceable and auditable.
      Source Finding: 'CR seed §8 Business Invariants #8'
    - Invariant: Only authorized staff perform catalog operations.
      Source Finding: 'CR seed §8 Business Invariants #9'
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    - Source Finding
    rows:
    - Object: Book
      State: Registered
      Meaning: The book has been registered and the catalog holds its authoritative record.
      Source Finding: 'CR seed §9 Lifecycle States #1'
    - Object: Book
      State: Retired
      Meaning: The record has been judged obsolete and is no longer to be used; the book is excluded from search, its details remain retrievable, and staff may return it to Registered.
      Source Finding: 'CR seed §9 Lifecycle States #2'
    - Object: Physical Copy
      State: Registered
      Meaning: The copy has been registered against exactly one book.
      Source Finding: 'CR seed §9 Lifecycle States #3'
    - Object: Physical Copy
      State: Retired
      Meaning: The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered.
      Source Finding: 'CR seed §9 Lifecycle States #4'
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    - Source Finding
    rows:
    - Event: Book Registered
      When It Occurs: When authorized staff register a new book with its first physical copy.
      Significance: A book enters the catalog and acquires its authoritative record.
      Source Finding: 'CR seed §10 Business Events #1'
    - Event: Physical Copy Registered
      When It Occurs: When authorized staff register a further copy against a registered book.
      Significance: The library records another copy it owns.
      Source Finding: 'CR seed §10 Business Events #2'
    - Event: Bibliographic Information Updated
      When It Occurs: When authorized staff update a registered book's bibliographic information.
      Significance: The authoritative description of a book changes.
      Source Finding: 'CR seed §10 Business Events #3'
    - Event: Book Retired
      When It Occurs: When authorized staff retire a book record judged obsolete.
      Significance: The record is no longer to be used.
      Source Finding: 'CR seed §10 Business Events #4'
    - Event: Physical Copy Retired
      When It Occurs: When authorized staff retire a copy that is lost or damaged.
      Significance: The library no longer holds that copy.
      Source Finding: 'CR seed §10 Business Events #5'
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    - Source Finding
    rows:
    - Business Object: Book record
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #1'
    - Business Object: Physical copy record
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #2'
    - Business Object: Bibliographic information
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #3'
    - Business Object: The judgement that a record is obsolete
      Authoritative Owner: Authorized staff
      Source Finding: 'CR seed §11 Authority Boundaries #4'
  out_of_scope:
    columns:
    - Item
    - Reason
    - Source Finding
    rows:
    - Item: Circulation
      Reason: A project function; this change request is limited to catalog only.
      Source Finding: 'CR seed §12 Out of Scope #1'
    - Item: Patron
      Reason: A project function; this change request is limited to catalog only, and patron management is declared excluded from this release.
      Source Finding: 'CR seed §12 Out of Scope #2'
    - Item: Staff
      Reason: A project function; this change request is limited to catalog only, and it is where deciding who is authorized is deferred to.
      Source Finding: 'CR seed §12 Out of Scope #3'
    - Item: Reservations
      Reason: A project function, declared excluded from this release; expected through a future governed change request.
      Source Finding: 'CR seed §12 Out of Scope #4'
    - Item: Acquisitions
      Reason: A project function, declared excluded from this release; expected through a future governed change request.
      Source Finding: 'CR seed §12 Out of Scope #5'
    - Item: Inventory
      Reason: A project function; inventory reconciliation is declared excluded from this release.
      Source Finding: 'CR seed §12 Out of Scope #6'
    - Item: Notifications
      Reason: A project function; this change request is limited to catalog only.
      Source Finding: 'CR seed §12 Out of Scope #7'
    - Item: Policy
      Reason: A project function; this change request is limited to catalog only.
      Source Finding: 'CR seed §12 Out of Scope #8'
    - Item: Reporting
      Reason: A project function; this change request is limited to catalog only.
      Source Finding: 'CR seed §12 Out of Scope #9'
    - Item: Borrowing
      Reason: Declared excluded from this release; expected through a future governed change request.
      Source Finding: 'CR seed §12 Out of Scope #10'
    - Item: Fines
      Reason: Declared excluded from this release; expected through a future governed change request.
      Source Finding: 'CR seed §12 Out of Scope #11'
    - Item: Import of the records staff maintain manually today
      Reason: The catalog starts empty.
      Source Finding: 'CR seed §12 Out of Scope #12'
  governance_scope:
    columns:
    - Scope Item
    - Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT)
    - Source Finding
    rows:
    - Scope Item: catalog
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): CREATED
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
    - Criterion: Authorized staff can register a new book with at least one physical copy, and the catalog then holds exactly one record for it.
      Source Finding: 'CR seed §15 Acceptance Criteria #1'
    - Criterion: A registration whose title, author and publication year match a registered book is refused, and the reason states that the book already exists.
      Source Finding: 'CR seed §15 Acceptance Criteria #2'
    - Criterion: A registration offering no physical copy is refused.
      Source Finding: 'CR seed §15 Acceptance Criteria #3'
    - Criterion: A registration carrying no subject is refused.
      Source Finding: 'CR seed §15 Acceptance Criteria #4'
    - Criterion: Authorized staff can register a further physical copy against a registered book, and it is recorded against that book only.
      Source Finding: 'CR seed §15 Acceptance Criteria #5'
    - Criterion: Authorized staff can update a registered book's bibliographic information, and a later retrieval returns the updated version.
      Source Finding: 'CR seed §15 Acceptance Criteria #6'
    - Criterion: Authorized staff can retire a book record, and its physical copies are unaffected.
      Source Finding: 'CR seed §15 Acceptance Criteria #7'
    - Criterion: Authorized staff can retire a physical copy, and the book record is unaffected, including when it is the last copy.
      Source Finding: 'CR seed §15 Acceptance Criteria #8'
    - Criterion: Authorized staff can search by subject and locate registered books of that kind.
      Source Finding: 'CR seed §15 Acceptance Criteria #9'
    - Criterion: Authorized staff can search by title and locate a registered book by name.
      Source Finding: 'CR seed §15 Acceptance Criteria #10'
    - Criterion: A search returns the bibliographic information of each matching book and nothing about its physical copies.
      Source Finding: 'CR seed §15 Acceptance Criteria #11'
    - Criterion: A retired book does not appear in search results, and its details can still be retrieved.
      Source Finding: 'CR seed §15 Acceptance Criteria #12'
    - Criterion: Authorized staff can retrieve the complete details of a registered book, including the physical copies the library holds of it.
      Source Finding: 'CR seed §15 Acceptance Criteria #13'
    - Criterion: Authorized staff can register a physical copy against a retired book.
      Source Finding: 'CR seed §15 Acceptance Criteria #14'
    - Criterion: Authorized staff can return a retired book record to the registered state, and it appears in search again.
      Source Finding: 'CR seed §15 Acceptance Criteria #15'
    - Criterion: Authorized staff can return a retired physical copy to the registered state.
      Source Finding: 'CR seed §15 Acceptance Criteria #16'
    - Criterion: An update that would make a book's title, author and publication year match another registered book is refused.
      Source Finding: 'CR seed §15 Acceptance Criteria #17'
    - Criterion: A copy registration whose barcode matches a copy the library already owns is refused.
      Source Finding: 'CR seed §15 Acceptance Criteria #18'
    - Criterion: A staff member who is not authorized cannot perform any catalog operation.
      Source Finding: 'CR seed §15 Acceptance Criteria #19'
    - Criterion: Every catalog operation performed can be traced and audited afterwards.
      Source Finding: 'CR seed §15 Acceptance Criteria #20'
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    - Source Finding
    rows:
    - Business Object: Book
      Identified By: Its title, author and publication year together.
      Two Are The Same When: Their publication year matches and their titles and authors match without regard to letter case or repeated spacing.
      Source Finding: 'CR seed §16 Identity and Sameness #1'
    - Business Object: Physical Copy
      Identified By: The barcode the library assigns to it.
      Two Are The Same When: Their barcodes match.
      Source Finding: 'CR seed §16 Identity and Sameness #2'
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    - Source Finding
    rows:
    - Object: Book
      From State: —
      To State: Registered
      Triggered By: Authorized staff register the book together with its first physical copy.
      Cascade: None beyond the first copy being registered with it.
      Source Finding: 'CR seed §17 Lifecycle Transitions #1'
    - Object: Book
      From State: Registered
      To State: Retired
      Triggered By: Authorized staff judge the record obsolete and retire it.
      Cascade: None — the book's physical copies are unaffected.
      Source Finding: 'CR seed §17 Lifecycle Transitions #2'
    - Object: Book
      From State: Retired
      To State: Registered
      Triggered By: Authorized staff return the retired book record to the registered state.
      Cascade: None — the book's physical copies are unaffected.
      Source Finding: 'CR seed §17 Lifecycle Transitions #3'
    - Object: Physical Copy
      From State: —
      To State: Registered
      Triggered By: Authorized staff register the copy against a registered book.
      Cascade: None.
      Source Finding: 'CR seed §17 Lifecycle Transitions #4'
    - Object: Physical Copy
      From State: Registered
      To State: Retired
      Triggered By: Authorized staff retire a copy that is lost or damaged.
      Cascade: None — the book record is unaffected, including when it is the last copy.
      Source Finding: 'CR seed §17 Lifecycle Transitions #5'
    - Object: Physical Copy
      From State: Retired
      To State: Registered
      Triggered By: Authorized staff return the retired copy to the registered state.
      Cascade: None — the book record is unaffected.
      Source Finding: 'CR seed §17 Lifecycle Transitions #6'
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    - Source Finding
    rows:
    - Operation: Register a book
      Refused When: Its title, author and publication year match a registered book.
      Business Reason: The catalog holds one record per book; the book already exists, and a further copy is what staff register instead.
      Source Finding: 'CR seed §18 Operation Refusals #1'
    - Operation: Register a book
      Refused When: No physical copy is offered with it.
      Business Reason: A book is never registered without at least one copy.
      Source Finding: 'CR seed §18 Operation Refusals #2'
    - Operation: Register a book
      Refused When: It carries no subject.
      Business Reason: A book carries at least one subject, and subject is what staff search on.
      Source Finding: 'CR seed §18 Operation Refusals #3'
    - Operation: Register a physical copy
      Refused When: The book it names is not registered.
      Business Reason: Each physical copy belongs to exactly one book.
      Source Finding: 'CR seed §18 Operation Refusals #4'
    - Operation: Register a physical copy
      Refused When: Its barcode matches a copy the library already owns.
      Business Reason: A barcode identifies one copy; no two copies share one.
      Source Finding: 'CR seed §18 Operation Refusals #5'
    - Operation: Update bibliographic information
      Refused When: The changed title, author and publication year would match another registered book.
      Business Reason: Title, author and publication year identify a book; an update must not make one book a duplicate of another.
      Source Finding: 'CR seed §18 Operation Refusals #6'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Business Reason: Only authorized staff may perform catalog operations.
      Source Finding: 'CR seed §18 Operation Refusals #7'
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Business Object: Which staff are authorized
      Deferred To: The staff function, which governs library employees
      Until: A future governed change request introduces the staff function.
      Source Finding: 'CR seed §19 Authority Deferrals #1'
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
