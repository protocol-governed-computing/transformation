# Business Intent — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
header:
  Stage: 5 — Business Intent
  CR: cr_01_catalog
  Status: DRAFT
  Feeds: Stage 6 — Governance Intent
registers:
  subdomain_purpose: |2

    The catalog governs the library's authoritative description of what it holds: each bibliographic
    work it has cataloged and each physical copy it owns. It exists because those records are kept by
    hand today, which produces inconsistent descriptions, duplicate entries and difficulty locating
    materials. It owns the description of the collection and the operations that maintain it; it does
    not govern who borrows the collection, what is ordered, or what is owed.
  purpose_provenance:
    columns:
    - Source
    - Disposition (INHERITED, REFINED)
    - Refinement
    rows:
    - Source: CR seed §0 Subdomain Purpose
      Disposition (INHERITED, REFINED): REFINED
      Refinement: States what the subdomain owns and the three functions it does not govern.
  subdomain_purposes:
    columns:
    - Subdomain
    - Purpose
    - Source Finding
    rows:
    - Subdomain: catalog
      Purpose: Governs the library's authoritative description of what it holds — the works it has cataloged and the physical copies it owns.
      Source Finding: 'S1 cr_type #1'
  scope_boundary:
    columns:
    - Capability
    - Status
    - Notes
    - Source Finding
    rows:
    - Capability: Register a book
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-01
    - Capability: Register a physical copy against one work
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-02
    - Capability: Update bibliographic information
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-03
    - Capability: Retire an obsolete record
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-04
    - Capability: Search the catalog
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-05
    - Capability: Retrieve complete book details
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-06
    - Capability: Record that a catalog operation was performed
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-07
    - Capability: Confirm the staff member is authorized
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-08
    - Capability: Declare the stores this subdomain owns
      Status: IN_SCOPE
      Notes: Authored this change request
      Source Finding: S4 authoring_scope GAP-09
    - Capability: Grant staff authorization
      Status: DEFERRED
      Notes: Owned by patron, which is not in this release
      Source Finding: S4 gap_register GAP-10
    - Capability: Borrowing, reservations, fines, acquisitions, inventory reconciliation
      Status: DEFERRED
      Notes: Declared out of scope by the business author
      Source Finding: 'S1 out_of_scope #1'
  business_objects:
    columns:
    - Store Name
    - Record Model
    - Business Rationale
    - Source Finding
    rows:
    - Store Name: Bibliographic work record
      Record Model: MUTABLE_STATE
      Business Rationale: The library requires a single authoritative record for each work
      Source Finding: S4 bm_entities Bibliographic work
    - Store Name: Physical copy record
      Record Model: MUTABLE_STATE
      Business Rationale: The library requires a single authoritative record for each copy it owns
      Source Finding: S4 bm_entities Physical copy
    - Store Name: Catalog operation record
      Record Model: APPEND_ONLY_JOURNAL
      Business Rationale: Appended at $.payload.operation for every completed call
      Source Finding: S4 bm_entities Operation record
  identity_semantics:
    columns:
    - Store Name
    - Identity Field
    - Source
    - Uniqueness Rule
    - Cross-Subdomain Relationship
    - Source Finding
    rows:
    - Store Name: Bibliographic work record
      Identity Field: Work identifier
      Source: UNRESOLVED
      Uniqueness Rule: Two registrations describing the same published title are the same work and must not produce two records
      Cross-Subdomain Relationship: None
      Source Finding: S2 entity_attributes Bibliographic Work identity
    - Store Name: Physical copy record
      Identity Field: Copy identifier
      Source: Assigned by the library when the copy is registered
      Uniqueness Rule: Each owned copy is distinct even when several copies describe one work
      Cross-Subdomain Relationship: Names exactly one bibliographic work record
      Source Finding: S2 entity_attributes Physical Copy identity
    - Store Name: Catalog operation record
      Identity Field: Operation sequence
      Source: Assigned on append
      Uniqueness Rule: Each performed operation appends exactly one record
      Cross-Subdomain Relationship: Names the staff member who performed it
      Source Finding: S4 bm_entities Operation record
  invariants:
    columns:
    - Invariant
    - Business Reason
    - Source Finding
    rows:
    - Invariant: Each physical copy belongs to exactly one bibliographic work
      Business Reason: A copy the library owns describes one published title; a copy belonging to two would make the collection uncountable
      Source Finding: 'S4 constraint_register #1'
    - Invariant: Each work and each copy has exactly one authoritative record
      Business Reason: The library requires one place to look, which is the whole point of the change
      Source Finding: 'S4 constraint_register #2'
    - Invariant: Every business operation performed is traceable and auditable
      Business Reason: The library must be able to account afterwards for what staff did to the catalog
      Source Finding: 'S4 constraint_register #3'
    - Invariant: Only authorized staff perform catalog operations
      Business Reason: The catalog is the library's authoritative description and may not be altered by anyone
      Source Finding: 'S4 constraint_register #4'
    - Invariant: A retired record is never offered as current
      Business Reason: A record retired for being obsolete would mislead if it kept appearing in results
      Source Finding: 'S4 design_decisions #5'
  actions:
    columns:
    - Action
    - Object
    - Trigger
    - Status
    - Source Finding
    rows:
    - Action: Register
      Object: Bibliographic work record
      Trigger: Authorized staff register a new book
      Status: IN_SCOPE
      Source Finding: S4 capability_graph Register a book
    - Action: Register
      Object: Physical copy record
      Trigger: Authorized staff register a copy
      Status: IN_SCOPE
      Source Finding: S4 capability_graph Register a physical copy against one work
    - Action: Update
      Object: Bibliographic work record
      Trigger: Authorized staff update a registered work
      Status: IN_SCOPE
      Source Finding: S4 capability_graph Update bibliographic information
    - Action: Retire
      Object: Bibliographic work record
      Trigger: Authorized staff retire an obsolete record
      Status: IN_SCOPE
      Source Finding: S4 capability_graph Retire an obsolete record
    - Action: Search
      Object: Bibliographic work record
      Trigger: Authorized staff search for materials
      Status: IN_SCOPE
      Source Finding: S4 capability_graph Search the catalog
    - Action: Retrieve
      Object: Bibliographic work record
      Trigger: Authorized staff request complete details
      Status: IN_SCOPE
      Source Finding: S4 capability_graph Retrieve complete book details
    - Action: Append
      Object: Catalog operation record
      Trigger: Any catalog operation completes
      Status: IN_SCOPE
      Source Finding: S4 capability_graph Record that a catalog operation was performed
  provisional_codes:
    columns:
    - Subdomain
    - Provisional Code
    - Family (AC, IN, WF, CC)
    - Summary
    - Source Finding
    rows:
    - Subdomain: catalog
      Provisional Code: AC_LIBRARY_STAFF_V0
      Family (AC, IN, WF, CC): AC
      Summary: The authorized staff member who performs a catalog operation
      Source Finding: S4 actors Authorized staff member
    - Subdomain: catalog
      Provisional Code: IN_REGISTER_BOOK_V0
      Family (AC, IN, WF, CC): IN
      Summary: A request to register a new book
      Source Finding: S4 capability_graph Register a book
    - Subdomain: catalog
      Provisional Code: IN_REGISTER_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC): IN
      Summary: A request to register a copy against a work
      Source Finding: S4 capability_graph Register a physical copy against one work
    - Subdomain: catalog
      Provisional Code: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Family (AC, IN, WF, CC): IN
      Summary: A request to update a registered work
      Source Finding: S4 capability_graph Update bibliographic information
    - Subdomain: catalog
      Provisional Code: IN_RETIRE_CATALOG_RECORD_V0
      Family (AC, IN, WF, CC): IN
      Summary: A request to retire an obsolete record
      Source Finding: S4 capability_graph Retire an obsolete record
    - Subdomain: catalog
      Provisional Code: IN_SEARCH_CATALOG_V0
      Family (AC, IN, WF, CC): IN
      Summary: A request to locate materials
      Source Finding: S4 capability_graph Search the catalog
    - Subdomain: catalog
      Provisional Code: IN_RETRIEVE_BOOK_DETAILS_V0
      Family (AC, IN, WF, CC): IN
      Summary: A request for the complete details of a book
      Source Finding: S4 capability_graph Retrieve complete book details
    - Subdomain: catalog
      Provisional Code: WF_REGISTER_BOOK_V0
      Family (AC, IN, WF, CC): WF
      Summary: Registering a book, end to end
      Source Finding: S4 capability_graph Register a book
    - Subdomain: catalog
      Provisional Code: WF_REGISTER_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC): WF
      Summary: Registering a copy against exactly one work
      Source Finding: S4 capability_graph Register a physical copy against one work
    - Subdomain: catalog
      Provisional Code: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Family (AC, IN, WF, CC): WF
      Summary: Updating the description of a registered work
      Source Finding: S4 capability_graph Update bibliographic information
    - Subdomain: catalog
      Provisional Code: WF_RETIRE_CATALOG_RECORD_V0
      Family (AC, IN, WF, CC): WF
      Summary: Retiring a record so it is no longer current
      Source Finding: S4 capability_graph Retire an obsolete record
    - Subdomain: catalog
      Provisional Code: WF_SEARCH_CATALOG_V0
      Family (AC, IN, WF, CC): CC
      Summary: Searching the catalog and recording that it happened
      Source Finding: S4 capability_graph Search the catalog
    - Subdomain: catalog
      Provisional Code: WF_RETRIEVE_BOOK_DETAILS_V0
      Family (AC, IN, WF, CC): WF
      Summary: Assembling a work with the copies belonging to it
      Source Finding: S4 capability_graph Retrieve complete book details
    - Subdomain: catalog
      Provisional Code: CC_CONFIRM_STAFF_AUTHORIZED_V0
      Family (AC, IN, WF, CC): CC
      Summary: Confirm the staff member may perform catalog operations
      Source Finding: S4 capability_graph Confirm the staff member is authorized
    - Subdomain: catalog
      Provisional Code: catalog::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0
      Family (AC, IN, WF, CC): CC
      Summary: Record a work as the catalog's authoritative description of it
      Source Finding: S4 capability_graph Register a book
    - Subdomain: catalog
      Provisional Code: CC_REGISTER_PHYSICAL_COPY_V0
      Family (AC, IN, WF, CC): CC
      Summary: Record a copy against exactly one work
      Source Finding: S4 capability_graph Register a physical copy against one work
    - Subdomain: catalog
      Provisional Code: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Family (AC, IN, WF, CC): CC
      Summary: Replace the descriptive content of a work's record
      Source Finding: S4 capability_graph Update bibliographic information
    - Subdomain: catalog
      Provisional Code: CC_RETIRE_CATALOG_RECORD_V0
      Family (AC, IN, WF, CC): CC
      Summary: Mark a record retired so it is no longer offered as current
      Source Finding: S4 capability_graph Retire an obsolete record
    - Subdomain: catalog
      Provisional Code: CC_SEARCH_CATALOG_V0
      Family (AC, IN, WF, CC): CC
      Summary: Select the current records matching the staff member's terms
      Source Finding: S4 capability_graph Search the catalog
    - Subdomain: catalog
      Provisional Code: CC_ASSEMBLE_BOOK_DETAILS_V0
      Family (AC, IN, WF, CC): CC
      Summary: Assemble a work's record with the copies belonging to it
      Source Finding: S4 capability_graph Retrieve complete book details
    - Subdomain: catalog
      Provisional Code: CC_APPEND_CATALOG_OPERATION_V0
      Family (AC, IN, WF, CC): CC
      Summary: Append a durable account of a performed catalog operation
      Source Finding: S4 capability_graph Record that a catalog operation was performed
  cross_subdomain_refs:
    columns:
    - CC Code
    - Defined In
    - Role
    - Source Finding
    rows:
    - CC Code: capability_side_effects::CS_MUTABLE_JSON_V0
      Defined In: capability_side_effects
      Role: Holds a catalog record that can be updated in place
      Source Finding: S4 dependency_graph catalog to CS_MUTABLE_JSON
    - CC Code: workload::CS_APPENDONLY_JSONL_V0
      Defined In: capability_side_effects
      Role: Appends a durable account of a performed operation
      Source Finding: S4 dependency_graph catalog to CS_APPENDONLY_JSONL
```

> P5 states the irreducible WHAT. It is the first phase to name what this change will build, using
> provisional codes — what to build, never where it will live. Placement is Stage 6's decision and
> binding identity is Stage 7's.

---

## 1. Subdomain Purpose

### Purpose of every subdomain this change touches

## 2. Scope Boundary

## 3. Business Objects

## 4. Identity Semantics

## 5. Business Invariants

## 6. Business Actions

## 7. Provisional Artifact Codes

## 8. Cross-Subdomain References
