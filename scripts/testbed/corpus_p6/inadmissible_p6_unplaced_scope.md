# Stage 6 — Governance Intent: book_library_mgmt / catalog

**Stage:** 6 — Governance Intent
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

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

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Register a book together with its first physical copy | catalog | OWNED |  | S4 authoring_scope GAP-05 |
| Register a further physical copy against a registered book | catalog | OWNED |  | S4 authoring_scope GAP-06 |
| Update a book's bibliographic information | catalog | OWNED |  | S4 authoring_scope GAP-07 |
| Retire a book record | catalog | OWNED |  | S4 authoring_scope GAP-08 |
| Return a retired book record to the registered state | catalog | OWNED |  | S4 authoring_scope GAP-10 |
| Return a retired physical copy to the registered state | catalog | OWNED |  | S4 authoring_scope GAP-11 |
| Search the catalog by subject or title | catalog | OWNED |  | S4 authoring_scope GAP-12 |
| Retrieve a book's complete details with the copies held | catalog | OWNED |  | S4 authoring_scope GAP-13 |
| Confirm the staff member performing an operation is authorized | catalog | OWNED |  | S4 authoring_scope GAP-04 |
| Record every performed catalog operation in the catalog's own audit trail | catalog | OWNED |  | S4 authoring_scope GAP-01 |
| Read every book record so that a search can select among them by content | platform | OWNED |  | S4 authoring_scope GAP-17 |
| Hold a durable record that can be read, listed and updated in place | platform | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S3 authoring_decisions Hold a book record durably and update it in place |
| Claim a value once so a second claim on it fails | platform | SATISFIED | capability_side_effects::CS_REGISTRY_V0 | S3 authoring_decisions Enforce that one book exists per title, author and publication year |
| Append an entry to a trail that cannot be amended | platform | SATISFIED | capability_side_effects::CS_APPENDONLY_JSONL_V0 | S3 authoring_decisions Append an entry to an append-only trail |
| Assemble a durable record from supplied values | platform | SATISFIED | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | S3 authoring_decisions Assemble a catalog record from supplied values |
| Confirm a record carries the fields its contract declares | platform | SATISFIED | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | S3 authoring_decisions Confirm a catalog record carries its required fields |
| Select the records matching stated criteria | platform | SATISFIED | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | S3 authoring_decisions Select the catalog records matching stated criteria |
| Confirm supplied parameters satisfy declared rules | platform | SATISFIED | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | S3 authoring_decisions Confirm the parameters supplied to a catalog operation satisfy their declared rules |
| Deciding which staff are authorized | staff | DEFERRED |  | S1 authority_deferrals #1 |
| Deleting a catalog record | catalog | DEFERRED |  | S1 business_invariants #9 |

Eleven capabilities are owned by the catalog and authored by this change. Seven are satisfied by
mechanisms the platform already declares, reused as-is. Two are deferred: one to a function that does
not exist yet, and one that will never exist because a record is never deleted.

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of every book the library catalogs | The library requires one authoritative description per book, correctable in place, carrying its own registered-or-retired state | catalog | S5 business_objects Book record |
| A durable record of every physical copy the library owns | The library requires one authoritative record per copy, each naming the one book it belongs to and carrying its own state | catalog | S5 business_objects Physical copy record |
| A trail of performed operations that cannot be amended | Every operation must be traceable afterwards, and a trail that could be rewritten would not be evidence | catalog | S5 business_objects Catalog audit trail |
| A claim on each book's identity, held once | Duplicate prevention needs the claim on title, author and publication year to hold at the moment of registration | catalog | S5 business_objects Book identity registry |
| A claim on each copy's barcode, held once | No two copies the library owns may carry the same barcode | catalog | S5 business_objects Copy barcode registry |

Every store named here is owned by the catalog and written only by the catalog's own operations.

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Read whether a staff member is authorized to perform catalog operations | catalog → staff |  | GAP | S1 authority_deferrals #1 |

The catalog reads authorization and never grants it, so the capability that decides who is authorized
is a gap owned by the staff function rather than work this change performs. No catalog operation
writes into a store another subdomain owns, and no capability contract from another subdomain is
called.

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE) | Source Finding |
|------|----------------|----------------------------------|----------------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | Declared and in use by ai_governance and workload | EXTEND | S3 impact_analysis capability_side_effects::CS_MUTABLE_JSON_V0 |
| capability_side_effects::CS_REGISTRY_V0 | Declared and in use by ai_governance | REUSE | S3 impact_analysis capability_side_effects::CS_REGISTRY_V0 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | Declared and in use by ai_governance | REUSE | S3 impact_analysis capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Declared, no current consumer | REUSE | S3 impact_analysis capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Declared, no current consumer | REUSE | S3 impact_analysis capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| capability_transforms::CT_PURE_FILTER_RECORDS_V0 | Declared, no current consumer | REUSE | S3 impact_analysis capability_transforms::CT_PURE_FILTER_RECORDS_V0 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Declared and in use by ai_governance | REUSE | S3 impact_analysis capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |

Every artifact is read, never modified, so no consumer of any of them is affected by this change.

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| CATALOG_OWNS_ITS_STORES | Every store the catalog reads or writes is declared by the catalog, and no catalog operation writes into a store another subdomain owns. | S4 constraint_register #12 |
| AUTHORIZATION_IS_READ_NEVER_GRANTED | The catalog confirms a staff member is authorized on every operation and grants authorization nowhere. | S4 design_decisions #8 |
| NO_RECORD_IS_DELETED | No catalog operation removes a record. Retirement is the only way a record leaves use, and it is reversible. | S1 business_invariants #9 |
| STATE_IS_DATA_ON_THE_RECORD | A record's registered-or-retired state is held as data on the record, never implied by which store it occupies. | S4 design_decisions #4 |
| RETIREMENT_NEVER_CASCADES | Retiring a book leaves its copies untouched and retiring the last copy leaves the book registered; no state change is derived from another. | S4 design_decisions #7 |
| EVERY_OPERATION_IS_APPENDED | Every performed catalog operation appends one entry to the catalog's own trail, including searches and retrievals. | S1 business_invariants #7 |
| READS_RAISE_NO_EVENT | Searching and retrieving are audited but recognise no business moment, because nothing reacts to a read. | S4 design_decisions #5 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Register a book together with its first physical copy | catalog | S6 ownership Register a book together with its first physical copy |
| Register a further physical copy against a registered book | catalog | S6 ownership Register a further physical copy against a registered book |
| Update a book's bibliographic information | catalog | S6 ownership Update a book's bibliographic information |
| Retire a book record | catalog | S6 ownership Retire a book record |
| Retire a physical copy | catalog | S6 ownership Retire a physical copy |
| Return a retired book record to the registered state | catalog | S6 ownership Return a retired book record to the registered state |
| Return a retired physical copy to the registered state | catalog | S6 ownership Return a retired physical copy to the registered state |
| Search the catalog by subject or title | catalog | S6 ownership Search the catalog by subject or title |
| Retrieve a book's complete details with the copies held | catalog | S6 ownership Retrieve a book's complete details with the copies held |
| Confirm the staff member performing an operation is authorized | catalog | S6 ownership Confirm the staff member performing an operation is authorized |
| Record every performed catalog operation in the catalog's own audit trail | catalog | S6 ownership Record every performed catalog operation in the catalog's own audit trail |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
