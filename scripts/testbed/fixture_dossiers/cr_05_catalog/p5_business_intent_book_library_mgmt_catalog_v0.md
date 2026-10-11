# Stage 5 — Business Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 5 — Business Intent
  CR: cr_05_catalog
  Status: DRAFT
  Feeds: Stage 6 — Governance Intent
registers:
  subdomain_purpose: |2

    The Catalog subdomain governs what the library knows about its books: the works it carries, the
    editions of those works, and the physical copies on its shelves. It holds one record for each, the
    state that says whether each is in service or retired, and the details the library publishes about
    them. It records each thing being registered, its details being corrected, and its being retired or
    reinstated, and it announces the moments the business declared matter. It does not govern who borrows
    a book, what a borrower may do, or what the library charges.
  purpose_provenance:
    columns:
    - Source
    - Disposition (INHERITED, REFINED)
    - Refinement
    rows:
    - Source: CR seed §0 Subdomain Purpose
      Disposition (INHERITED, REFINED): INHERITED
      Refinement: ''
  subdomain_purposes:
    columns:
    - Subdomain
    - Purpose
    - Source Finding
    rows:
    - Subdomain: catalog
      Purpose: Governs what the library knows about its books, and now holds every rule it applies to them.
      Source Finding: S4 bm_entities The Catalog's Rules
  scope_boundary:
    columns:
    - Capability
    - Status (IN_SCOPE, DEFERRED)
    - Notes
    - Source Finding
    rows:
    - Capability: Refuse anyone the library has not authorized
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The confirming step holds the library's rules; every act composes it.
      Source Finding: S4 authoring_scope GAP-01
    - Capability: Refuse a registration the catalog finds incomplete
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: A rule following each check refuses on what it found.
      Source Finding: S4 authoring_scope GAP-02
    - Capability: Hold what a book, a work and a further edition must contain
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The checking contracts hold their descriptions.
      Source Finding: S4 authoring_scope GAP-03
    - Capability: Check what the catalog records
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Each registration act checks the record it writes.
      Source Finding: S4 authoring_scope GAP-04
    - Capability: Record the subject callers supply
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The register act reads the subject where callers send it.
      Source Finding: S4 authoring_scope GAP-05
    - Capability: Register a copy as registered
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The copy contract writes the state itself.
      Source Finding: S4 authoring_scope GAP-06
    - Capability: Keep a corrected record's state, and check it against the book description
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The correction keeps the state and refuses a record that fails the description.
      Source Finding: S4 authoring_scope GAP-07
    - Capability: Admit a request without the rules the catalog holds
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The gates stop requiring what the catalog holds and what no act reads; nothing a caller sends needs to change.
      Source Finding: S4 authoring_scope GAP-08
    - Capability: Establish who a caller is
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: The credentials a request presents stay its own.
      Source Finding: S4 authoring_scope Establish who a caller is
    - Capability: Records made under a request's own rules
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: Declined by the business; the record is added to and never rewritten.
      Source Finding: S4 authoring_scope Records made under a request's own rules
  business_objects:
    columns:
    - Store Name
    - Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID)
    - Business Rationale
    - Source Finding
    rows:
    - Store Name: Book record
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): MUTABLE_STATE
      Business Rationale: 'Unchanged by this change, and named because what may be written into it changes: only a book meeting the description, with the subject callers supply, and a correction only with the state the record has.'
      Source Finding: S4 bm_entities The Book
    - Store Name: Copy record
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): MUTABLE_STATE
      Business Rationale: Unchanged by this change, and named because a copy is written only as registered.
      Source Finding: S4 bm_entities The Physical Copy
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
      Identity Field: Title, author and publication year
      Source: Supplied by staff registering the book
      Uniqueness Rule: No two registered books share them; unchanged by this change.
      Cross-Subdomain Relationship: None
      Source Finding: S4 bm_entities The Book
    - Store Name: Copy record
      Identity Field: Barcode
      Source: Supplied by staff registering the copy
      Uniqueness Rule: No two copies share a barcode; unchanged by this change.
      Cross-Subdomain Relationship: None
      Source Finding: S4 bm_entities The Physical Copy
  invariants:
    columns:
    - Invariant
    - Business Reason
    - Source Finding
    rows:
    - Invariant: No catalog operation is performed by anyone the library has not authorized.
      Business Reason: Only authorized staff perform catalog operations.
      Source Finding: 'S1 business_invariants #1'
    - Invariant: No book, work or further edition is registered without what the library says it must contain.
      Business Reason: The library said the parts are required.
      Source Finding: 'S1 business_invariants #2'
    - Invariant: What the catalog checks is what it records.
      Business Reason: A check of anything else judges nothing that is written.
      Source Finding: 'S1 business_invariants #3'
    - Invariant: No physical copy is registered in any state but registered.
      Business Reason: There is one state a copy is registered in.
      Source Finding: 'S1 business_invariants #4'
    - Invariant: A business rule of the catalog's is held by the catalog, and no request changes it.
      Business Reason: A business rule the caller supplies is a business rule the caller can widen.
      Source Finding: 'S1 business_invariants #5'
    - Invariant: A refusal changes no record.
      Business Reason: A refused request leaves the catalog as it found it.
      Source Finding: 'S1 business_invariants #6'
  actions:
    columns:
    - Action
    - Object
    - Trigger
    - Status (IN_SCOPE, DEFERRED)
    - Source Finding
    rows:
    - Action: Refuse
      Object: A request from anyone the library has not authorized
      Trigger: Any catalog request
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Refuse anyone the library has not authorized
    - Action: Refuse
      Object: A book, work or further edition lacking what it must contain
      Trigger: A registration
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Refuse a registration the catalog finds incomplete
    - Action: Register
      Object: A copy, as registered
      Trigger: A copy registration
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Register a copy as registered
    - Action: Correct
      Object: A book's bibliographic information, keeping its state
      Trigger: A correction
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Keep a corrected record's state, and check it against the book description
  provisional_codes:
    columns:
    - Subdomain
    - Provisional Code
    - Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE)
    - Summary
    - Source Finding
    rows: []
  cross_subdomain_refs:
    columns:
    - CC Code
    - Defined In
    - Role
    - Source Finding
    rows:
    - CC Code: NONE IDENTIFIED
      Defined In: ''
      Role: ''
      Source Finding: ''
```

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Invariants

---

## 6. Actions

---

## 7. Provisional Codes

---

## 8. Cross-Subdomain References

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
