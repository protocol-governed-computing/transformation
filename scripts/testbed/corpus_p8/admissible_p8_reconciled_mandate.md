# Authoring Mandate — book_library_mgmt / catalog

**Stage:** 8 — Authoring Mandate
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** artifact authoring

> P8 adds nothing and drops nothing. It orders what Stage 7 assigned into the only sequence the
> dependency graph admits — storage before the bindings that resolve it, capabilities before the
> workflows that compose them, workflows before the intents that start them. Every code is copied
> verbatim. Gate 2 closes here.

---

## 1. Build Order

<!-- register:build_order -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | NEW | catalog | — |
| 1 | 2 | book_library_mgmt::AC_LIBRARY_STAFF_V0 | NEW | catalog | — |
| 2 | 3 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | NEW | catalog | book_library_mgmt::AC_LIBRARY_STAFF_V0 |
| 2 | 4 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | NEW | catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 5 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | NEW | catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 6 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 7 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | NEW | catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 8 | book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | NEW | catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 9 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | NEW | catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 10 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | NEW | catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 3 | 11 | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | NEW | catalog | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 4 | 12 | book_library_mgmt::WF_REGISTER_BOOK_V0 | NEW | catalog | book_library_mgmt::RB_CATALOG_BINDINGS_V0; book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0; book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| 4 | 13 | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | book_library_mgmt::RB_CATALOG_BINDINGS_V0; book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| 4 | 14 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | NEW | catalog | book_library_mgmt::RB_CATALOG_BINDINGS_V0; book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| 4 | 15 | book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | NEW | catalog | book_library_mgmt::RB_CATALOG_BINDINGS_V0; book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 |
| 4 | 16 | book_library_mgmt::WF_SEARCH_CATALOG_V0 | NEW | catalog | book_library_mgmt::RB_CATALOG_BINDINGS_V0; book_library_mgmt::CC_SEARCH_CATALOG_V0 |
| 4 | 17 | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | NEW | catalog | book_library_mgmt::RB_CATALOG_BINDINGS_V0; book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 |
| 5 | 18 | book_library_mgmt::IN_REGISTER_BOOK_V0 | NEW | catalog | book_library_mgmt::WF_REGISTER_BOOK_V0 |
| 5 | 19 | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 |
| 5 | 20 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | NEW | catalog | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| 5 | 21 | book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | NEW | catalog | book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 |
| 5 | 22 | book_library_mgmt::IN_SEARCH_CATALOG_V0 | NEW | catalog | book_library_mgmt::WF_SEARCH_CATALOG_V0 |
| 5 | 23 | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | NEW | catalog | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 |
| 5 | 24 | book_library_mgmt::CT_PURE_REQUIRE_TRUE_V0 | NEW | catalog | — |

## 2. Critical Path

<!-- register:critical_path -->
| Position | Code |
|----------|------|
| 1 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| 3 | book_library_mgmt::RB_CATALOG_BINDINGS_V0 |
| 4 | book_library_mgmt::WF_REGISTER_BOOK_V0 |
| 5 | book_library_mgmt::IN_REGISTER_BOOK_V0 |

## 3. Mandate Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action | Count | Description |
|--------|-------|-------------|
| NEW | 24 | 1 STRUCTURE, 1 AC, 1 CT, 8 CC, 1 RB, 6 WF, 6 IN — all owned by catalog |

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | catalog |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | catalog |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | catalog |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | catalog |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | catalog |

## 5. New Capabilities

<!-- register:new_capabilities -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Confirm the staff member may perform catalog operations | staff_identity | authorization_decision |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | Record a work as the catalog's authoritative description of it | work_identity, bibliographic_information | work_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | Record a copy against exactly one bibliographic work | copy_identity, work_identity | copy_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Replace the descriptive content of a work's record | work_identity, bibliographic_information | work_record |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | Mark a record retired so it is no longer offered as current | work_identity | retired_record |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | Select the current records matching the staff member's terms | search_terms | matching_records |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Assemble a work's record with the copies belonging to it | work_identity | book_details |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | Append a durable account of a performed catalog operation | staff_identity, operation_performed | operation_record |

## 6. New Intents

<!-- register:new_intents -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| book_library_mgmt::IN_REGISTER_BOOK_V0 | A request to register a new book | book_library_mgmt::WF_REGISTER_BOOK_V0 | staff_identity, bibliographic_information |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | A request to register a copy against a work | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | staff_identity, copy_identity, work_identity |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | A request to update a registered work | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | staff_identity, work_identity, bibliographic_information |
| book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | A request to retire an obsolete record | book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | staff_identity, work_identity |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | A request to locate materials | book_library_mgmt::WF_SEARCH_CATALOG_V0 | staff_identity, search_terms |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | A request for the complete details of a book | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | staff_identity, work_identity |

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes -->
| Code | Note |
|------|------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Reads authorization; deciding who is authorized belongs to patron and is deferred to a future change request. |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | Appends only to the catalog's own journal; no peer store is written. |
