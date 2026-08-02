# Design Intent — book_library_mgmt / catalog

**Stage:** 7 — Design Intent
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

> P7 answers HOW. The provisional codes Stage 5 assigned become binding, domain-qualified FQDNs,
> placed in the subdomain Stage 6 chose. Each is assigned once and reused as the exact same string;
> a spelling variant would create a second, permanently misnamed artifact. Gate 1 closes here.

---

## 1. Design Resolution

<!-- register:design_resolution business_language -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Where the catalog's records live | The catalog owns its records exclusively | Two mutable stores and one append-only journal, all declared by the catalog | S6 storage_governance Bibliographic work records |
| How a copy names its work | A copy belongs to exactly one bibliographic work | The copy record carries the work's identity; the work never lists its copies | S5 invariants Each physical copy belongs to exactly one bibliographic work |
| How authorization is checked | Only authorized staff perform catalog operations | A single contract confirms authorization and every workflow calls it first | S6 boundary_rules Authorization is read, never granted |
| How an operation is recorded | Every business operation is traceable and auditable | One contract appends to the journal, called as the last step of every workflow | S6 boundary_rules Store ownership is exclusive |
| How retirement works | A retired record is never offered as current | Retirement marks the record; search excludes marked records rather than deleting them | S6 boundary_rules Retirement does not delete |

## 2. Existing Inventory

<!-- register:existing_inventory -->
| FQDN | Action | Reason | Source Finding |
|------|--------|--------|----------------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE | Holds a catalog record that can be updated in place | S6 ownership Hold a record that can be updated in place |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE | Appends a durable account of a performed operation | S6 ownership Append a durable account of a performed action |

## 3. New Artifacts

<!-- register:new_artifacts -->
| Capability | Family | Code | Owner Subdomain | Status | Source Finding |
|------------|--------|------|-----------------|--------|----------------|
| A request to register a new book | IN | book_library_mgmt::IN_REGISTER_BOOK_V0 | catalog | NEW | S5 provisional_codes IN_REGISTER_BOOK_V0 |
| A request to register a copy against a work | IN | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | catalog | NEW | S5 provisional_codes IN_REGISTER_PHYSICAL_COPY_V0 |
| A request to update a registered work | IN | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog | NEW | S5 provisional_codes IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| A request to retire an obsolete record | IN | book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | catalog | NEW | S5 provisional_codes IN_RETIRE_CATALOG_RECORD_V0 |
| A request to locate materials | IN | book_library_mgmt::IN_SEARCH_CATALOG_V0 | catalog | NEW | S5 provisional_codes IN_SEARCH_CATALOG_V0 |
| A request for the complete details of a book | IN | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | catalog | NEW | S5 provisional_codes IN_RETRIEVE_BOOK_DETAILS_V0 |
| Registering a book, end to end | WF | book_library_mgmt::WF_REGISTER_BOOK_V0 | catalog | NEW | S5 provisional_codes WF_REGISTER_BOOK_V0 |
| Registering a copy against exactly one work | WF | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | catalog | NEW | S5 provisional_codes WF_REGISTER_PHYSICAL_COPY_V0 |
| Updating the description of a registered work | WF | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog | NEW | S5 provisional_codes WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| Retiring a record so it is no longer current | WF | book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | catalog | NEW | S5 provisional_codes WF_RETIRE_CATALOG_RECORD_V0 |
| Searching the catalog and recording that it happened | WF | book_library_mgmt::WF_SEARCH_CATALOG_V0 | catalog | NEW | S5 provisional_codes WF_SEARCH_CATALOG_V0 |
| Assembling a work with the copies belonging to it | WF | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | catalog | NEW | S5 provisional_codes WF_RETRIEVE_BOOK_DETAILS_V0 |
| Confirm the staff member may perform catalog operations | CC | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | catalog | NEW | S5 provisional_codes CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| Record a work as the catalog's authoritative description | CC | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | catalog | NEW | S5 provisional_codes CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| Record a copy against exactly one work | CC | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | catalog | NEW | S5 provisional_codes CC_REGISTER_PHYSICAL_COPY_V0 |
| Replace the descriptive content of a work's record | CC | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog | NEW | S5 provisional_codes CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| Mark a record retired so it is no longer current | CC | book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | catalog | NEW | S5 provisional_codes CC_RETIRE_CATALOG_RECORD_V0 |
| Select the current records matching the staff terms | CC | book_library_mgmt::CC_SEARCH_CATALOG_V0 | catalog | NEW | S5 provisional_codes CC_SEARCH_CATALOG_V0 |
| Assemble a work's record with the copies belonging to it | CC | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | catalog | NEW | S5 provisional_codes CC_ASSEMBLE_BOOK_DETAILS_V0 |
| Append a durable account of a performed catalog operation | CC | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | catalog | NEW | S5 provisional_codes CC_APPEND_CATALOG_OPERATION_V0 |
| Bindings for every catalog workflow | RB | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | catalog | NEW | S6 storage_governance Bibliographic work records |
| The stores the catalog owns | STRUCTURE | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | catalog | NEW | S6 storage_governance Catalog operation journal |
| Interpret an observation as a required condition | CT | book_library_mgmt::CT_PURE_REQUIRE_TRUE_V0 | catalog | NEW | S6 boundary_rules Authorization is read, never granted |

## 4. Runtime Binding Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_BOOK_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Physical copy records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_SEARCH_CATALOG_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Catalog operation journal |

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type | Routing | Source Finding |
|----------|------|-----------|---------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::IN_REGISTER_BOOK_V0 | IN | ACK to confirm authorization, NACK to exit | S6 governance_outcome Register a book |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS to register the work, DENIED to exit | S6 boundary_rules Authorization is read, never granted |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | CC | SUCCESS to append the operation, ALREADY_EXISTS to exit | S5 invariants Each work and each copy has exactly one authoritative record |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS to exit | S6 boundary_rules Store ownership is exclusive |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | IN | ACK to confirm authorization, NACK to exit | S6 governance_outcome Register a physical copy against one work |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS to register the copy, DENIED to exit | S6 boundary_rules Authorization is read, never granted |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | CC | SUCCESS to append the operation, WORK_NOT_FOUND to exit | S5 invariants Each physical copy belongs to exactly one bibliographic work |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS to exit | S6 boundary_rules Store ownership is exclusive |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::IN_SEARCH_CATALOG_V0 | IN | ACK to confirm authorization, NACK to exit | S6 governance_outcome Search the catalog |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS to search, DENIED to exit | S6 boundary_rules Authorization is read, never granted |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | CC | SUCCESS to append the operation | S5 actions Search |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS to exit | S6 boundary_rules Store ownership is exclusive |

## 6. Capability Composition

<!-- register:cc_composition -->
| CC Code | Step | Capability | Kind | Operation | Consumes | Produces | Interpreted By | Semantic Status | Interface |
|---------|------|------------|------|-----------|----------|----------|----------------|-----------------|-----------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | EXISTS | staff_identity | authorized | book_library_mgmt::CT_PURE_REQUIRE_TRUE_V0 | DENIED | the staff member is entitled to act |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | work_identity | existing_work | book_library_mgmt::CT_PURE_REQUIRE_TRUE_V0 | ALREADY_EXISTS | work_identity to existing_work |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | 2 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | work_identity, bibliographic_information | work_record | — | SUCCESS | the authoritative record for the work |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | work_identity | existing_work | book_library_mgmt::CT_PURE_REQUIRE_TRUE_V0 | NOT_FOUND | confirms the work is registered |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 2 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | copy_identity, work_identity | copy_record | — | SUCCESS | the authoritative record for the copy |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | search_terms | matching_records | — | SUCCESS | current records matching the terms |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | 1 | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | staff_identity, operation_performed | operation_record | — | SUCCESS | the durable account of the operation |

## 7. Structure Stores

<!-- register:structure_stores -->
| Store Name | Storage Type | Proposed Path | Used By | Source Finding |
|------------|--------------|---------------|---------|----------------|
| BIBLIOGRAPHIC_WORKS | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/bibliographic_works.json | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | S6 storage_governance Bibliographic work records |
| PHYSICAL_COPIES | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/physical_copies.json | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | S6 storage_governance Physical copy records |
| CATALOG_OPERATIONS | CS_APPENDONLY_JSONL_V0 | book_library_mgmt/catalog/catalog_operations.jsonl | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | S6 storage_governance Catalog operation journal |

## 8. Artifact Summary

<!-- register:artifact_summary -->
| Action | Subdomain | Count | Artifacts |
|--------|-----------|-------|-----------|
| NEW | catalog | 24 | 1 AC, 6 IN, 6 WF, 8 CC, 1 CT, 1 RB, 1 STRUCTURE |
