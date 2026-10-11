# Business Intent — book_library_mgmt / catalog (deliberately inadmissible fixture))

## Machine

```yaml
header:
  Stage: 5 — Business Intent
  CR: cr_01_catalog
  Status: DRAFT
  Feeds: Stage 6 — Governance Intent
registers:
  subdomain_purpose: |2

    The catalog governs the library's authoritative description of what it holds: one record for each book
    it catalogs, and one for each physical copy it owns. It establishes the authority to state what the
    library has — a book exists in the collection because the catalog says so, and a copy belongs to
    exactly one book because the catalog records it that way. It manages the lifecycle of both records
    from registration through retirement and back, and it records every operation performed against it so
    that any change to the library's description of itself can be traced afterwards. It exists because
    those records are maintained by hand today, which produces inconsistent descriptions, duplicate
    entries and difficulty locating materials. It does not govern who borrows the collection, what is
    ordered, who the library's patrons are, or which staff are authorized.
  purpose_provenance:
    columns:
    - Source
    - Disposition (INHERITED, REFINED)
    - Refinement
    rows:
    - Source: CR seed §0 Subdomain Purpose
      Disposition (INHERITED, REFINED): INHERITED
      Refinement: States the authority the subdomain establishes — a book exists in the collection because the catalog says so — the lifecycle it manages from registration through retirement and back, and the four functions it explicitly does not govern. The seed states what the catalog is for and why it exists; none of these four additions contradicts it.
  subdomain_purposes:
    columns:
    - Subdomain
    - Purpose
    - Source Finding
    rows:
    - Subdomain: circulation
      Purpose: Governs the library's authoritative description of what it holds — one record per book it catalogs and one per physical copy it owns — and the lifecycle of both from registration through retirement and back.
      Source Finding: 'S1 cr_type #1'
  scope_boundary:
    columns:
    - Capability
    - Status (IN_SCOPE, DEFERRED)
    - Notes
    - Source Finding
    rows:
    - Capability: Register a book together with its first physical copy
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: A book is never registered without a copy
      Source Finding: S4 authoring_scope GAP-05
    - Capability: Register a further physical copy against a registered book
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Refused if the barcode is already owned or the book is not registered
      Source Finding: S4 authoring_scope GAP-06
    - Capability: Update a book's bibliographic information
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Refused if the change would make the book a duplicate of another
      Source Finding: S4 authoring_scope GAP-07
    - Capability: Retire a book record
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Leaves the book's copies untouched
      Source Finding: S4 authoring_scope GAP-08
    - Capability: Retire a physical copy
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Leaves the book record untouched, including when it was the last copy
      Source Finding: S4 authoring_scope GAP-09
    - Capability: Return a retired book record to the registered state
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Reinstatement is explicit, never derived
      Source Finding: S4 authoring_scope GAP-10
    - Capability: Return a retired physical copy to the registered state
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Reinstatement is explicit, never derived
      Source Finding: S4 authoring_scope GAP-11
    - Capability: Search the catalog by subject or title
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Retired books are excluded from results
      Source Finding: S4 authoring_scope GAP-12
    - Capability: Retrieve a book's complete details with the copies held
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Serves retired books as well as registered ones
      Source Finding: S4 authoring_scope GAP-13
    - Capability: Confirm the staff member performing an operation is authorized
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The catalog reads authorization; it never grants it
      Source Finding: S4 authoring_scope GAP-04
    - Capability: Record every performed catalog operation in the catalog's own audit trail
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The catalog owns the trail it appends to
      Source Finding: S4 authoring_scope GAP-01
    - Capability: Read every book record so that a search can select among them by content
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: An existing mechanism amended to publish records; owned by platform, not by the catalog
      Source Finding: S4 authoring_scope GAP-17
    - Capability: Deciding which staff are authorized
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: Belongs to the staff function, which a future change request introduces
      Source Finding: 'S1 authority_deferrals #1'
    - Capability: Deleting a catalog record
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: 'Not deferred but excluded: a record is never deleted, so no capability is authored for it'
      Source Finding: 'S1 business_invariants #9'
    - Capability: Importing the records staff maintain manually today
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: The catalog starts empty
      Source Finding: S1 out_of_scope Import of the records staff maintain manually today
    - Capability: Circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy and reporting
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: The nine remaining project functions, adjacent and untouched
      Source Finding: 'S1 governance_scope #2'
  business_objects:
    columns:
    - Store Name
    - Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID)
    - Business Rationale
    - Source Finding
    rows:
    - Store Name: Book record
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): MUTABLE_STATE
      Business Rationale: The library requires one authoritative record per book, its bibliographic information is correctable, and its state moves from registered to retired and back on the same record
      Source Finding: S4 bm_entities Book
    - Store Name: Physical copy record
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): MUTABLE_STATE
      Business Rationale: The library requires one authoritative record per copy it owns, and a copy's state moves both ways on the same record
      Source Finding: S4 bm_entities Physical Copy
    - Store Name: Catalog audit trail
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): APPEND_ONLY_JOURNAL
      Business Rationale: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence
      Source Finding: S4 resources Catalog audit trail
    - Store Name: Book identity registry
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): IDENTITY_REGISTRY
      Business Rationale: Duplicate prevention needs an atomic claim on a book's identity at the moment of registration
      Source Finding: 'S4 design_decisions #3'
    - Store Name: Copy barcode registry
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): IDENTITY_REGISTRY
      Business Rationale: No two copies the library owns may share a barcode, and the claim must hold at the moment of registration
      Source Finding: 'S1 business_invariants #6'
  identity_semantics:
    columns:
    - Store Name
    - Identity Field
    - Source
    - Uniqueness Rule
    - Cross-Subdomain Relationship
    - Source Finding
    rows:
    - Store Name: Book record
      Identity Field: Title, author and publication year together
      Source: Supplied by the staff member registering the book
      Uniqueness Rule: Two registrations carrying the same publication year, and the same title and author without regard to letter case or repeated spacing, describe the same book, and the second is refused
      Cross-Subdomain Relationship: None
      Source Finding: 'S1 identity_and_sameness #1'
    - Store Name: Physical copy record
      Identity Field: Barcode
      Source: Assigned by the library and supplied when the copy is registered
      Uniqueness Rule: Two records carrying the same barcode describe the same copy, and the second is refused
      Cross-Subdomain Relationship: Names exactly one book record
      Source Finding: 'S1 identity_and_sameness #2'
    - Store Name: Catalog audit trail
      Identity Field: Append position
      Source: Assigned when the entry is appended
      Uniqueness Rule: Each performed operation appends exactly one entry, and no entry is amended or removed
      Cross-Subdomain Relationship: Names the staff member who performed the operation
      Source Finding: S4 resources Catalog audit trail
    - Store Name: Book identity registry
      Identity Field: The key formed from title, author and publication year
      Source: Formed by the catalog, comparing title and author without regard to letter case or repeated spacing
      Uniqueness Rule: The key is claimed once; a second claim on it fails and the registration is refused
      Cross-Subdomain Relationship: None
      Source Finding: 'S4 design_decisions #3'
    - Store Name: Copy barcode registry
      Identity Field: Barcode
      Source: Assigned by the library
      Uniqueness Rule: The barcode is claimed once; a second claim on it fails and the copy registration is refused
      Cross-Subdomain Relationship: None
      Source Finding: 'S1 business_invariants #6'
  invariants:
    columns:
    - Invariant
    - Business Reason
    - Source Finding
    rows:
    - Invariant: Each physical copy belongs to exactly one book
      Business Reason: A copy the library owns is a copy of one published thing; a copy recorded against two books would make the collection's description untrue
      Source Finding: 'S1 business_invariants #1'
    - Invariant: Each book the library holds has exactly one authoritative record
      Business Reason: The library needs one place that says what it holds, which is the whole point of a governed catalog
      Source Finding: 'S1 business_invariants #2'
    - Invariant: Each physical copy the library owns has exactly one authoritative record
      Business Reason: Two records for one copy would make the library's count of what it owns unreliable
      Source Finding: 'S1 business_invariants #3'
    - Invariant: No two registered books share the same title, author and publication year
      Business Reason: Duplicate entries are the pain this change exists to remove
      Source Finding: 'S1 business_invariants #4'
    - Invariant: A book carries at least one subject
      Business Reason: Subject is what staff search on when looking for material rather than a known title, so a book with none could not be found that way
      Source Finding: 'S1 business_invariants #5'
    - Invariant: No two physical copies the library owns share the same barcode
      Business Reason: A barcode is how staff name one copy among several of the same book, including when retiring one
      Source Finding: 'S1 business_invariants #6'
    - Invariant: Every business operation performed against the catalog is traceable and auditable
      Business Reason: The library must be able to account afterwards for every change to its description of itself
      Source Finding: 'S1 business_invariants #7'
    - Invariant: Only authorized staff perform catalog operations
      Business Reason: The catalog is the library's authoritative record, and an unauthorized change to it would not be authoritative
      Source Finding: 'S1 business_invariants #8'
    - Invariant: No catalog record is ever deleted
      Business Reason: Retirement is the only way a record leaves use; a deleted record would leave its audit trail pointing at nothing
      Source Finding: 'S1 business_invariants #9'
    - Invariant: A registered book always has at the moment of registration at least one physical copy
      Business Reason: The library catalogs what it holds, and a book it holds no copy of is not a holding
      Source Finding: 'S1 operation_refusals #2'
  actions:
    columns:
    - Action
    - Object
    - Trigger
    - Status (IN_SCOPE, DEFERRED)
    - Source Finding
    rows:
    - Action: Register
      Object: Book, with its first physical copy
      Trigger: An authorized staff member registers a book the library has acquired
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Register a book together with its first physical copy
    - Action: Register
      Object: Physical copy
      Trigger: An authorized staff member records a further copy of a registered book
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Register a further physical copy against a registered book
    - Action: Update
      Object: Book's bibliographic information
      Trigger: An authorized staff member corrects or changes a book's description
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Update a book's bibliographic information
    - Action: Retire
      Object: Book record
      Trigger: An authorized staff member judges the record obsolete
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Retire a book record
    - Action: Retire
      Object: Physical copy
      Trigger: A copy is lost or damaged
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Retire a physical copy
    - Action: Reinstate
      Object: Book record
      Trigger: An authorized staff member returns a retired book to use
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Return a retired book record to the registered state
    - Action: Reinstate
      Object: Physical copy
      Trigger: An authorized staff member returns a retired copy to use
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Return a retired physical copy to the registered state
    - Action: Search
      Object: Catalog
      Trigger: An authorized staff member looks for material by subject or by title
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Search the catalog by subject or title, excluding retired books
    - Action: Retrieve
      Object: Book's complete details
      Trigger: An authorized staff member asks what the library holds of one book
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Retrieve a book's complete details with the copies the library holds
    - Action: Delete
      Object: Book record or physical copy
      Trigger: Never — no trigger exists, because a record is never deleted
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Source Finding: 'S1 business_invariants #9'
  provisional_codes:
    columns:
    - Subdomain
    - Provisional Code
    - Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE)
    - Summary
    - Source Finding
    rows:
    - Subdomain: circulation
      Provisional Code: AC_LIBRARY_STAFF_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): AC
      Summary: The authorized staff member who performs a catalog operation
      Source Finding: S4 actors Authorized staff member
    - Subdomain: circulation
      Provisional Code: IN_REGISTER_BOOK_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request to register a book together with its first physical copy
      Source Finding: S5 actions Register
    - Subdomain: circulation
      Provisional Code: IN_REGISTER_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request to register a further copy against a registered book
      Source Finding: S5 actions Register
    - Subdomain: circulation
      Provisional Code: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request to change a registered book's description
      Source Finding: S5 actions Update
    - Subdomain: circulation
      Provisional Code: IN_RETIRE_BOOK_RECORD_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request to retire a book record judged obsolete
      Source Finding: S5 actions Retire
    - Subdomain: circulation
      Provisional Code: IN_RETIRE_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request to retire a lost or damaged copy
      Source Finding: S5 actions Retire
    - Subdomain: circulation
      Provisional Code: IN_REINSTATE_BOOK_RECORD_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request to return a retired book record to the registered state
      Source Finding: S5 actions Reinstate
    - Subdomain: circulation
      Provisional Code: IN_REINSTATE_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request to return a retired copy to the registered state
      Source Finding: S5 actions Reinstate
    - Subdomain: circulation
      Provisional Code: IN_SEARCH_CATALOG_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request to locate material by subject or by title
      Source Finding: S5 actions Search
    - Subdomain: circulation
      Provisional Code: IN_RETRIEVE_BOOK_DETAILS_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): IN
      Summary: A request for a book's complete details with the copies held
      Source Finding: S5 actions Retrieve
    - Subdomain: circulation
      Provisional Code: WF_REGISTER_BOOK_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Registering a book and its first copy, end to end
      Source Finding: S4 capability_graph Register a book together with its first physical copy
    - Subdomain: circulation
      Provisional Code: WF_REGISTER_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Registering a further copy against a registered book
      Source Finding: S4 capability_graph Register a further physical copy against a registered book
    - Subdomain: circulation
      Provisional Code: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Changing a book's description without making it a duplicate
      Source Finding: S4 capability_graph Update a book's bibliographic information
    - Subdomain: circulation
      Provisional Code: WF_RETIRE_BOOK_RECORD_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Retiring a book record, leaving its copies untouched
      Source Finding: S4 capability_graph Retire a book record
    - Subdomain: circulation
      Provisional Code: WF_RETIRE_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Retiring a copy, leaving the book record untouched
      Source Finding: S4 capability_graph Retire a physical copy
    - Subdomain: circulation
      Provisional Code: WF_REINSTATE_BOOK_RECORD_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Returning a retired book record to the registered state
      Source Finding: S4 capability_graph Return a retired book record to the registered state
    - Subdomain: circulation
      Provisional Code: WF_REINSTATE_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Returning a retired copy to the registered state
      Source Finding: S4 capability_graph Return a retired physical copy to the registered state
    - Subdomain: circulation
      Provisional Code: WF_SEARCH_CATALOG_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Searching by subject or title, excluding retired books, and recording that it happened
      Source Finding: S4 capability_graph Search the catalog by subject or title, excluding retired books
    - Subdomain: circulation
      Provisional Code: WF_RETRIEVE_BOOK_DETAILS_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): WF
      Summary: Assembling a book with the copies the library holds of it
      Source Finding: S4 capability_graph Retrieve a book's complete details with the copies the library holds
    - Subdomain: circulation
      Provisional Code: CC_CONFIRM_STAFF_AUTHORIZED_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Confirm the staff member may perform catalog operations
      Source Finding: S4 capability_graph Confirm the staff member performing an operation is authorized
    - Subdomain: circulation
      Provisional Code: CC_CLAIM_BOOK_IDENTITY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Claim a book's identity so a second registration of the same book is refused
      Source Finding: S4 capability_graph Enforce that one book exists per title, author and publication year
    - Subdomain: circulation
      Provisional Code: CC_CLAIM_COPY_BARCODE_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Claim a copy's barcode so a second copy carrying it is refused
      Source Finding: S4 capability_graph Enforce that one physical copy exists per barcode
    - Subdomain: circulation
      Provisional Code: CC_REGISTER_BOOK_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Record a book's bibliographic information as the catalog's authoritative description of it
      Source Finding: S4 capability_graph Register a book together with its first physical copy
    - Subdomain: circulation
      Provisional Code: CC_REGISTER_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Record a copy against exactly one book
      Source Finding: S4 capability_graph Register a further physical copy against a registered book
    - Subdomain: circulation
      Provisional Code: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Replace a book's descriptive content, refusing a change that duplicates another book
      Source Finding: S4 capability_graph Update a book's bibliographic information
    - Subdomain: circulation
      Provisional Code: CC_RETIRE_BOOK_RECORD_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Mark a book record retired so it is no longer offered as current
      Source Finding: S4 capability_graph Retire a book record
    - Subdomain: circulation
      Provisional Code: CC_RETIRE_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Mark a copy retired so the library no longer holds it
      Source Finding: S4 capability_graph Retire a physical copy
    - Subdomain: circulation
      Provisional Code: CC_REINSTATE_BOOK_RECORD_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Mark a retired book record registered again
      Source Finding: S4 capability_graph Return a retired book record to the registered state
    - Subdomain: circulation
      Provisional Code: CC_REINSTATE_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Mark a retired copy registered again
      Source Finding: S4 capability_graph Return a retired physical copy to the registered state
    - Subdomain: circulation
      Provisional Code: CC_SEARCH_CATALOG_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Select the registered books matching a subject or title, excluding retired ones
      Source Finding: S4 capability_graph Search the catalog by subject or title, excluding retired books
    - Subdomain: circulation
      Provisional Code: CC_ASSEMBLE_BOOK_DETAILS_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Assemble a book's record with the copies recorded against it
      Source Finding: S4 capability_graph Retrieve a book's complete details with the copies the library holds
    - Subdomain: circulation
      Provisional Code: CC_APPEND_CATALOG_OPERATION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Append a durable account of a performed operation to the catalog's own audit trail
      Source Finding: S4 capability_graph Record a performed catalog operation in the catalog's audit trail
    - Subdomain: circulation
      Provisional Code: CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CT
      Summary: Forms the single key claimed for a book from its title, author and publication year
      Source Finding: S4 gap_register GAP-06
    - Subdomain: circulation
      Provisional Code: CC_VALIDATE_BOOK_SUBMISSION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Confirms a registration carries what a book record requires, before any identity is claimed
      Source Finding: S4 gap_register GAP-06
    - Subdomain: circulation
      Provisional Code: CC_RESOLVE_BOOK_IDENTITY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): CC
      Summary: Resolves a registered book by its identifying key, so an update names the book independently of the attributes it changes
      Source Finding: S4 gap_register GAP-08
    - Subdomain: circulation
      Provisional Code: EV_BOOK_REGISTRATION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): EV
      Summary: The moment a book enters the catalog
      Source Finding: S4 gap_register GAP-16
    - Subdomain: circulation
      Provisional Code: EV_PHYSICAL_COPY_REGISTERED_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): EV
      Summary: The moment the library records another copy it owns
      Source Finding: S4 gap_register GAP-16
    - Subdomain: circulation
      Provisional Code: EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): EV
      Summary: The moment a book's authoritative description changes
      Source Finding: S4 gap_register GAP-16
    - Subdomain: circulation
      Provisional Code: EV_BOOK_RETIRED_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): EV
      Summary: The moment a book record is judged obsolete
      Source Finding: S4 gap_register GAP-16
    - Subdomain: circulation
      Provisional Code: EV_PHYSICAL_COPY_RETIRED_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): EV
      Summary: The moment the library no longer holds a copy
      Source Finding: S4 gap_register GAP-16
    - Subdomain: circulation
      Provisional Code: RB_CATALOG_BINDINGS_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): RB
      Summary: Binds the catalog's operations to the stores and mechanisms they use
      Source Finding: S4 gap_register GAP-03
    - Subdomain: circulation
      Provisional Code: STRUCTURE_CATALOG_STORAGE_V0
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): STRUCTURE
      Summary: Declares the stores the catalog owns and the paths they occupy
      Source Finding: S4 gap_register GAP-02
  cross_subdomain_refs:
    columns:
    - CC Code
    - Defined In
    - Role
    - Source Finding
    rows: []
```

> The change request declares it touches the catalog. This document answers for a different subdomain, and declares its purpose inherited while restating it.

---

## 1. Subdomain Purpose

### Purpose of every subdomain this change touches

---

## 2. Scope Boundary

---

## 3. Business Objects

No record is ever deleted. Retirement is the only way a record leaves use, and it is reversible, which
is why both record stores hold state as data rather than by which store a record occupies.

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

No capability contract from another subdomain is referenced. The catalog reuses declared mechanisms —
durable records, uniqueness, an append-only trail and four pure transforms — and composes them itself,
so that no catalog operation depends on another subdomain's semantics or writes into its stores.

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
