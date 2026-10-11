# Stage 6 — Governance Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 6 — Governance Intent
  CR: cr_02_catalog
  Status: DRAFT
  Feeds: Stage 7 — Design Intent
registers:
  ownership:
    columns:
    - Capability
    - Owner Subdomain
    - Disposition (OWNED, SATISFIED, DEFERRED)
    - Existing Artifact
    - Source Finding
    rows:
    - Capability: Form the identifying key of a work from its title and author
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Form the identifying key of a work from its title and author
    - Capability: Claim a work's identity so that two registrations of one work do not produce two works
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Claim a work's identity so that two registrations of one work do not produce two works
    - Capability: Resolve the work an edition belongs to
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Resolve the work an edition belongs to
    - Capability: Group selected records by an attribute they share
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Group selected records by an attribute they share
    - Capability: Declare the stores the catalog owns
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Declare the stores the catalog owns
    - Capability: Bind the catalog's workflows to the stores they use
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Bind the catalog's workflows to the stores they use
    - Capability: Register an edition of a work the catalog does not yet hold
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Register an edition of a work the catalog does not yet hold
    - Capability: Validate that a registration carries what a work and an edition require
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Validate that a registration carries what a work and an edition require
    - Capability: Register an additional edition of an existing work
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Register an additional edition of an existing work
    - Capability: Search the catalog and answer at the level of the work
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Search the catalog and answer at the level of the work
    - Capability: Retrieve an edition's complete details with a summary of its work
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Retrieve an edition's complete details with a summary of its work
    - Capability: Admit a request to register an additional edition of an existing work
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Admit a request to register an additional edition of an existing work
    - Capability: Recognise the moment a work enters the catalog
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Recognise the moment a work enters the catalog
    - Capability: Hold a record durably and update it in place
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_side_effects::CS_MUTABLE_JSON_V0
      Source Finding: S4 capability_graph Hold a work record durably and update it in place
    - Capability: Claim an identity atomically so that a second claim cannot succeed unnoticed
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_side_effects::CS_REGISTRY_V0
      Source Finding: S4 capability_graph Enforce that one work exists per title and author
    - Capability: Confirm the staff member performing an operation is authorized
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Source Finding: S4 capability_graph Confirm the staff member performing an operation is authorized
    - Capability: Record every performed operation in the catalog's audit trail
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Source Finding: S4 capability_graph Record every performed operation in the catalog's audit trail
    - Capability: Register a physical copy against exactly one edition
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Source Finding: S4 capability_graph Register a physical copy against exactly one edition
    - Capability: Retire and reinstate an edition independently of the work's other editions
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Source Finding: S4 capability_graph Retire and reinstate an edition independently of the work's other editions
    - Capability: Update an edition's bibliographic information
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Source Finding: S4 capability_graph Update an edition's bibliographic information
    - Capability: Deciding which staff are authorized
      Owner Subdomain: staff
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Deciding which staff are authorized
    - Capability: Multiple identifiers for one publication
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Multiple identifiers for one publication
    - Capability: A governed subject taxonomy
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary A governed subject taxonomy
    - Capability: Digital resources associated with catalog records
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Digital resources associated with catalog records
    - Capability: Images associated with catalog records
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Images associated with catalog records
  storage_governance:
    columns:
    - Storage Need
    - Purpose
    - Subdomain
    - Source Finding
    rows:
    - Storage Need: A durable record of every work the library has catalogued
      Purpose: The library requires one authoritative description per work, correctable in place, so that several editions can be said to be editions of one thing
      Subdomain: catalog
      Source Finding: S5 business_objects Work record
    - Storage Need: An atomic claim on each work's identity
      Purpose: Two registrations describing the same work must resolve to one work, and only a claim taken at the moment of registration can guarantee it
      Subdomain: catalog
      Source Finding: S5 business_objects Work identity registry
    - Storage Need: A durable record of every edition the library holds
      Purpose: 'Unchanged from the previous change: one authoritative description per edition, correctable in place and carrying its own registered-or-retired state'
      Subdomain: catalog
      Source Finding: S5 business_objects Edition record
    - Storage Need: A durable record of every physical copy the library owns
      Purpose: 'Unchanged from the previous change: one authoritative record per copy, each naming the one edition it belongs to'
      Subdomain: catalog
      Source Finding: S5 business_objects Physical copy record
    - Storage Need: An unamendable trail of every operation performed
      Purpose: 'Unchanged from the previous change: an operation that has been performed cannot be un-performed, so its record is never amended'
      Subdomain: catalog
      Source Finding: S5 business_objects Catalog audit trail
    - Storage Need: An atomic claim on each edition's identity
      Purpose: 'Unchanged from the previous change: no two editions share a title, author and publication year'
      Subdomain: catalog
      Source Finding: S5 business_objects Edition identity registry
    - Storage Need: An atomic claim on each copy's barcode
      Purpose: 'Unchanged from the previous change: no two copies the library owns share a barcode'
      Subdomain: catalog
      Source Finding: S5 business_objects Copy barcode registry
  cross_subdomain_deps:
    columns:
    - Dependency
    - Direction
    - Existing Artifact
    - Status (SATISFIED, GAP)
    - Source Finding
    rows:
    - Dependency: Read whether a staff member is authorized to perform catalog operations
      Direction: catalog → staff
      Existing Artifact: ''
      Status (SATISFIED, GAP): GAP
      Source Finding: S4 dependency_graph catalog → staff
  pps_artifacts_requiring_action:
    columns:
    - FQDN
    - Current Status
    - Action (REPLACE, REVIEW, REUSE)
    - Source Finding
    rows:
    - FQDN: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Current Status: Declares the five stores the catalog owns; every consumer is inside the subdomain
      Action (REPLACE, REVIEW, REUSE): EXTEND
      Source Finding: S4 gap_register GAP-05
    - FQDN: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Current Status: Binds the catalog's workflows to the stores they use; referenced by nine artifacts, all within the subdomain
      Action (REPLACE, REVIEW, REUSE): EXTEND
      Source Finding: S4 gap_register GAP-06
    - FQDN: book_library_mgmt::CC_REGISTER_BOOK_V0
      Current Status: Registers a record together with its first copy, claiming two identities before any write
      Action (REPLACE, REVIEW, REUSE): EXTEND
      Source Finding: S4 gap_register GAP-07
    - FQDN: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Current Status: Confirms a registration carries what a record requires, before any claim
      Action (REPLACE, REVIEW, REUSE): EXTEND
      Source Finding: S4 gap_register GAP-08
    - FQDN: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Current Status: Selects registered records by subject or title and excludes retired ones
      Action (REPLACE, REVIEW, REUSE): EXTEND
      Source Finding: S4 gap_register GAP-10
    - FQDN: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Current Status: Assembles one record with the physical copies of it
      Action (REPLACE, REVIEW, REUSE): EXTEND
      Source Finding: S4 gap_register GAP-11
    - FQDN: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Current Status: Forms the three-attribute key every catalog operation reaches; 23 artifacts depend on it
      Action (REPLACE, REVIEW, REUSE): REVIEW
      Source Finding: S3 authoring_decisions Form the identifying key of a work from its title and author
    - FQDN: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Current Status: Claims the edition's identity; read as the precedent the work claim follows
      Action (REPLACE, REVIEW, REUSE): REVIEW
      Source Finding: S3 authoring_decisions Claim a work's identity so that two registrations of one work do not produce two works
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Current Status: Declared and in use by ai_governance, book_library_mgmt and workload
      Action (REPLACE, REVIEW, REUSE): REUSE
      Source Finding: S3 impact_analysis capability_side_effects::CS_MUTABLE_JSON_V0
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Current Status: Declared and in use by ai_governance and book_library_mgmt
      Action (REPLACE, REVIEW, REUSE): REUSE
      Source Finding: S3 impact_analysis capability_side_effects::CS_REGISTRY_V0
    - FQDN: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Current Status: Selects records by stated criteria; examined and not extended
      Action (REPLACE, REVIEW, REUSE): REVIEW
      Source Finding: S3 impact_analysis capability_transforms::CT_PURE_FILTER_RECORDS_V0
  boundary_rules:
    columns:
    - Rule Name
    - Statement
    - Source Finding
    rows:
    - Rule Name: CATALOG_OWNS_ITS_STORES
      Statement: Every store the catalog reads or writes is declared by the catalog, including the two this change adds, and no catalog operation writes into a store another subdomain owns.
      Source Finding: 'S3 analysis_findings #7'
    - Rule Name: AUTHORIZATION_IS_READ_NEVER_GRANTED
      Statement: The catalog confirms a staff member is authorized on every operation, including the ones this change adds, and grants authorization nowhere.
      Source Finding: 'S4 constraint_register #1'
    - Rule Name: EVERY_CLAIM_PRECEDES_EVERY_WRITE
      Statement: A registration claims every identity it needs — the work, the edition and the barcode — before it writes any record, so a refused registration leaves nothing behind.
      Source Finding: 'S4 constraint_register #12'
    - Rule Name: EDITION_IDENTITY_IS_NOT_WIDENED
      Statement: The key that identifies an existing record is not changed to serve the work; the work's key is formed independently and the two cannot alter each other.
      Source Finding: 'S4 constraint_register #13'
    - Rule Name: NO_CAPABILITY_IS_WITHDRAWN
      Statement: Every operation staff had before this change remains reachable and every existing record remains findable; search and retrieval are extended in the shape of their answers and in nothing else.
      Source Finding: 'S4 constraint_register #1'
    - Rule Name: A_WORK_IS_NEVER_RETIRED
      Statement: Retirement is declared on the edition and on the copy; a work whose editions are all retired is simply that, and no cascade reaches it.
      Source Finding: 'S4 constraint_register #11'
  governance_outcome:
    columns:
    - Capability
    - Owner Subdomain
    - Source Finding
    rows:
    - Capability: Form the identifying key of a work from its title and author
      Owner Subdomain: catalog
      Source Finding: S6 ownership Form the identifying key of a work from its title and author
    - Capability: Claim a work's identity so that two registrations of one work do not produce two works
      Owner Subdomain: catalog
      Source Finding: S6 ownership Claim a work's identity so that two registrations of one work do not produce two works
    - Capability: Resolve the work an edition belongs to
      Owner Subdomain: catalog
      Source Finding: S6 ownership Resolve the work an edition belongs to
    - Capability: Group selected records by an attribute they share
      Owner Subdomain: catalog
      Source Finding: S6 ownership Group selected records by an attribute they share
    - Capability: Declare the stores the catalog owns
      Owner Subdomain: catalog
      Source Finding: S6 ownership Declare the stores the catalog owns
    - Capability: Bind the catalog's workflows to the stores they use
      Owner Subdomain: catalog
      Source Finding: S6 ownership Bind the catalog's workflows to the stores they use
    - Capability: Register an edition of a work the catalog does not yet hold
      Owner Subdomain: catalog
      Source Finding: S6 ownership Register an edition of a work the catalog does not yet hold
    - Capability: Validate that a registration carries what a work and an edition require
      Owner Subdomain: catalog
      Source Finding: S6 ownership Validate that a registration carries what a work and an edition require
    - Capability: Register an additional edition of an existing work
      Owner Subdomain: catalog
      Source Finding: S6 ownership Register an additional edition of an existing work
    - Capability: Search the catalog and answer at the level of the work
      Owner Subdomain: catalog
      Source Finding: S6 ownership Search the catalog and answer at the level of the work
    - Capability: Retrieve an edition's complete details with a summary of its work
      Owner Subdomain: catalog
      Source Finding: S6 ownership Retrieve an edition's complete details with a summary of its work
    - Capability: Admit a request to register an additional edition of an existing work
      Owner Subdomain: catalog
      Source Finding: S6 ownership Admit a request to register an additional edition of an existing work
    - Capability: Recognise the moment a work enters the catalog
      Owner Subdomain: catalog
      Source Finding: S6 ownership Recognise the moment a work enters the catalog
```

---

## 1. Subdomain Boundary — Ownership

---

## 2. Storage Governance Requirements

---

## 3. Cross-Subdomain Dependency Declaration

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
