# Governance Intent — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
header:
  Stage: 6 — Governance Intent
  CR: cr_01_catalog
  Status: IN_REVIEW
registers:
  ownership:
    columns:
    - Capability
    - Owner Subdomain
    - Disposition (OWNED, SATISFIED, DEFERRED)
    - Existing Artifact
    - Source Finding
    rows:
    - Capability: Register a book together with its first physical copy
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-05
    - Capability: Register a further physical copy against a registered book
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-06
    - Capability: Update a book's bibliographic information
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-07
    - Capability: Retire a book record
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-08
    - Capability: Retire a physical copy
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-09
    - Capability: Return a retired book record to the registered state
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-10
    - Capability: Return a retired physical copy to the registered state
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-11
    - Capability: Search the catalog by subject or title
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-12
    - Capability: Retrieve a book's complete details with the copies held
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-13
    - Capability: Confirm the staff member performing an operation is authorized
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-04
    - Capability: Record every performed catalog operation in the catalog's own audit trail
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-01
    - Capability: Read every book record so that a search can select among them by content
      Owner Subdomain: platform
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S4 authoring_scope GAP-17
    - Capability: Hold a durable record that can be read, listed and updated in place
      Owner Subdomain: platform
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_side_effects::CS_MUTABLE_JSON_V0
      Source Finding: S3 authoring_decisions Hold a book record durably and update it in place
    - Capability: Claim a value once so a second claim on it fails
      Owner Subdomain: platform
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_side_effects::CS_REGISTRY_V0
      Source Finding: S3 authoring_decisions Enforce that one book exists per title, author and publication year
    - Capability: Append an entry to a trail that cannot be amended
      Owner Subdomain: platform
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Source Finding: S3 authoring_decisions Append an entry to an append-only trail
    - Capability: Assemble a durable record from supplied values
      Owner Subdomain: platform
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Source Finding: S3 authoring_decisions Assemble a catalog record from supplied values
    - Capability: Confirm a record carries the fields its contract declares
      Owner Subdomain: platform
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Source Finding: S3 authoring_decisions Confirm a catalog record carries its required fields
    - Capability: Select the records matching stated criteria
      Owner Subdomain: platform
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Source Finding: S3 authoring_decisions Select the catalog records matching stated criteria
    - Capability: Confirm supplied parameters satisfy declared rules
      Owner Subdomain: platform
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Source Finding: S3 authoring_decisions Confirm the parameters supplied to a catalog operation satisfy their declared rules
    - Capability: Deciding which staff are authorized
      Owner Subdomain: staff
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: 'S1 authority_deferrals #1'
    - Capability: Deleting a catalog record
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: 'S1 business_invariants #9'
  storage_governance:
    columns:
    - Storage Need
    - Purpose
    - Subdomain
    - Source Finding
    rows:
    - Storage Need: A durable record of every book the library catalogs
      Purpose: The library requires one authoritative description per book, correctable in place, carrying its own registered-or-retired state
      Subdomain: catalog
      Source Finding: S5 business_objects Book record
    - Storage Need: A durable record of every physical copy the library owns
      Purpose: The library requires one authoritative record per copy, each naming the one book it belongs to and carrying its own state
      Subdomain: catalog
      Source Finding: S5 business_objects Physical copy record
    - Storage Need: A trail of performed operations that cannot be amended
      Purpose: Every operation must be traceable afterwards, and a trail that could be rewritten would not be evidence
      Subdomain: catalog
      Source Finding: S5 business_objects Catalog audit trail
    - Storage Need: A claim on each book's identity, held once
      Purpose: Duplicate prevention needs the claim on title, author and publication year to hold at the moment of registration
      Subdomain: catalog
      Source Finding: S5 business_objects Book identity registry
    - Storage Need: A claim on each copy's barcode, held once
      Purpose: Held by STRUCTURE_CATALOG_STORAGE_V0 so no two copies carry the same barcode
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
      Source Finding: 'S1 authority_deferrals #1'
  pps_artifacts_requiring_action:
    columns:
    - FQDN
    - Current Status
    - Action (REPLACE, REVIEW, REUSE)
    - Source Finding
    rows:
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Current Status: Declared and in use by ai_governance and workload
      Action (REPLACE, REVIEW, REUSE): EXTEND
      Source Finding: S3 impact_analysis capability_side_effects::CS_MUTABLE_JSON_V0
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Current Status: Declared and in use by ai_governance
      Action (REPLACE, REVIEW, REUSE): REUSE
      Source Finding: S3 impact_analysis capability_side_effects::CS_REGISTRY_V0
    - FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Current Status: Declared and in use by ai_governance
      Action (REPLACE, REVIEW, REUSE): REUSE
      Source Finding: S3 impact_analysis capability_side_effects::CS_APPENDONLY_JSONL_V0
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Current Status: Declared, no current consumer
      Action (REPLACE, REVIEW, REUSE): REUSE
      Source Finding: S3 impact_analysis capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Current Status: Declared, no current consumer
      Action (REPLACE, REVIEW, REUSE): REUSE
      Source Finding: S3 impact_analysis capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    - FQDN: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Current Status: Declared, no current consumer
      Action (REPLACE, REVIEW, REUSE): REUSE
      Source Finding: S3 impact_analysis capability_transforms::CT_PURE_FILTER_RECORDS_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Current Status: Declared and in use by ai_governance
      Action (REPLACE, REVIEW, REUSE): REUSE
      Source Finding: S3 impact_analysis capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
  boundary_rules: |2

    ---
  governance_outcome:
    columns:
    - Capability
    - Source Finding
    rows:
    - Capability: Register a book together with its first physical copy
      Source Finding: S6 ownership Register a book together with its first physical copy
    - Capability: Register a further physical copy against a registered book
      Source Finding: S6 ownership Register a further physical copy against a registered book
    - Capability: Update a book's bibliographic information
      Source Finding: S6 ownership Update a book's bibliographic information
    - Capability: Retire a book record
      Source Finding: S6 ownership Retire a book record
    - Capability: Retire a physical copy
      Source Finding: S6 ownership Retire a physical copy
    - Capability: Return a retired book record to the registered state
      Source Finding: S6 ownership Return a retired book record to the registered state
    - Capability: Return a retired physical copy to the registered state
      Source Finding: S6 ownership Return a retired physical copy to the registered state
    - Capability: Search the catalog by subject or title
      Source Finding: S6 ownership Search the catalog by subject or title
    - Capability: Retrieve a book's complete details with the copies held
      Source Finding: S6 ownership Retrieve a book's complete details with the copies held
    - Capability: Confirm the staff member performing an operation is authorized
      Source Finding: S6 ownership Confirm the staff member performing an operation is authorized
    - Capability: Record every performed catalog operation in the catalog's own audit trail
      Source Finding: S6 ownership Record every performed catalog operation in the catalog's own audit trail
```

> The governance decisions below are the admissible document's. What is wrong is the shape they are carried in — and one of them names a design identity where a business need belongs.

---

## Domain Placement

| Field | Value |
| --- | --- |
| Domain | `book_library_mgmt` |
| Primary subdomain | `catalog` — NEW — declared by this CR |
| Authority class | new actor type: the authorized library staff member |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

The catalog stands alone rather than nesting under an existing subdomain because nothing in the
composition describes what a library holds: there is no boundary to extend, and the nine remaining
project functions do not exist yet to nest beneath. A new actor type is required because the one
business actor in the composition names another subdomain's employee and asserts no authorization to
perform catalog operations.

---

## 1. Subdomain Boundary — Ownership

Eleven capabilities are owned by the catalog and authored by this change. Seven are satisfied by
mechanisms the platform already declares, reused as-is. Two are deferred: one to a function that does
not exist yet, and one that will never exist because a record is never deleted.

---

## 2. Storage Governance Requirements

Every store named here is owned by the catalog and written only by the catalog's own operations.

---

## 3. Cross-Subdomain Dependency Declaration

The catalog reads authorization and never grants it, so the capability that decides who is authorized
is a gap owned by the staff function rather than work this change performs. No catalog operation
writes into a store another subdomain owns, and no capability contract from another subdomain is
called.

---

## 4. PPS Artifacts Requiring Action

Every artifact is read, never modified, so no consumer of any of them is affected by this change.

---

## 5. Governance Boundary Rules

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
