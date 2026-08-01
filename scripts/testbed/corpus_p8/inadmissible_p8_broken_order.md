# Authoring Mandate — book_library_mgmt / catalog (deliberately inadmissible fixture)

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
| 1 | 1 | catalog::STRUCTURE_CATALOG_STORAGE_V0 | NEW | catalog | catalog::RB_CATALOG_BINDINGS_V0 |
| 1 | 2 | catalog::AC_LIBRARY_STAFF_V0 | NEW | catalog | — |
| 2 | 3 | catalog::CC_CONFIRM_STAFF_AUTHORIZED_V0 | NEW | catalog | catalog::AC_LIBRARY_STAFF_V0 |
| 2 | 4 | catalog::CC_APPEND_CATALOG_OPERATION_V0 | NEW | catalog | catalog::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 5 | catalog::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | NEW | catalog | catalog::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 6 | catalog::CC_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | catalog::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 8 | catalog::CC_RETIRE_CATALOG_RECORD_V0 | NEW | catalog | catalog::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 9 | catalog::CC_SEARCH_CATALOG_V0 | NEW | catalog | catalog::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 10 | catalog::CC_ASSEMBLE_BOOK_DETAILS_V0 | NEW | catalog | catalog::STRUCTURE_CATALOG_STORAGE_V0 |
| 3 | 11 | catalog::RB_CATALOG_BINDINGS_V0 | NEW | catalog | catalog::STRUCTURE_CATALOG_STORAGE_V0 |
| 4 | 12 | catalog::WF_REGISTER_BOOK_V0 | NEW | catalog | catalog::RB_CATALOG_BINDINGS_V0; catalog::CC_CONFIRM_STAFF_AUTHORIZED_V0; catalog::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0; catalog::CC_APPEND_CATALOG_OPERATION_V0 |
| 4 | 13 | catalog::WF_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | catalog::RB_CATALOG_BINDINGS_V0; catalog::CC_CONFIRM_STAFF_AUTHORIZED_V0; catalog::CC_REGISTER_PHYSICAL_COPY_V0; catalog::CC_APPEND_CATALOG_OPERATION_V0 |
| 4 | 14 | catalog::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | NEW | catalog | catalog::RB_CATALOG_BINDINGS_V0; catalog::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| 4 | 15 | catalog::WF_RETIRE_CATALOG_RECORD_V0 | NEW | catalog | catalog::RB_CATALOG_BINDINGS_V0; catalog::CC_RETIRE_CATALOG_RECORD_V0 |
| 4 | 16 | catalog::WF_SEARCH_CATALOG_V0 | NEW | catalog | catalog::RB_CATALOG_BINDINGS_V0; catalog::CC_SEARCH_CATALOG_V0 |
| 4 | 17 | catalog::WF_RETRIEVE_BOOK_DETAILS_V0 | NEW | catalog | catalog::RB_CATALOG_BINDINGS_V0; catalog::CC_ASSEMBLE_BOOK_DETAILS_V0 |
| 5 | 18 | catalog::IN_REGISTER_BOOK_V0 | NEW | catalog | catalog::WF_REGISTER_BOOK_V0 |
| 5 | 19 | catalog::IN_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | catalog::WF_REGISTER_PHYSICAL_COPY_V0 |
| 5 | 20 | catalog::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | NEW | catalog | catalog::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| 5 | 21 | catalog::IN_RETIRE_CATALOG_RECORD_V0 | NEW | catalog | catalog::WF_RETIRE_CATALOG_RECORD_V0 |
| 5 | 22 | catalog::IN_SEARCH_CATALOG_V0 | NEW | catalog | catalog::WF_SEARCH_CATALOG_V0 |
| 5 | 23 | catalog::IN_RETRIEVE_BOOK_DETAILS_V0 | NEW | catalog | catalog::WF_RETRIEVE_BOOK_DETAILS_V0 |

## 2. Critical Path

<!-- register:critical_path -->
| Position | Code |
|----------|------|
| 1 | catalog::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | catalog::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| 3 | catalog::CC_VALIDATE_ISBN_V0 |
| 4 | catalog::WF_REGISTER_BOOK_V0 |
| 5 | catalog::IN_REGISTER_BOOK_V0 |

## 3. Mandate Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action | Count | Description |
|--------|-------|-------------|
| NEW | 23 | 1 STRUCTURE, 1 AC, 8 CC, 1 RB, 6 WF, 6 IN — all owned by catalog |

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| catalog::STRUCTURE_CATALOG_STORAGE_V0 | catalog |
| catalog::RB_CATALOG_BINDINGS_V0 | catalog |
| catalog::WF_REGISTER_BOOK_V0 | catalog |
| catalog::WF_REGISTER_PHYSICAL_COPY_V0 | catalog |
| catalog::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog |
| catalog::WF_RETIRE_CATALOG_RECORD_V0 | catalog |
| catalog::WF_SEARCH_CATALOG_V0 | catalog |
| catalog::WF_RETRIEVE_BOOK_DETAILS_V0 | catalog |

## 5. New Capabilities

<!-- register:new_capabilities -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| catalog::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Confirm the staff member may perform catalog operations | staff_identity | authorization_decision |
| catalog::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | Record a work as the catalog's authoritative description of it | work_identity, bibliographic_information | work_record |
| catalog::CC_REGISTER_PHYSICAL_COPY_V0 | Record a copy against exactly one bibliographic work | copy_identity, work_identity | copy_record |
| catalog::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Replace the descriptive content of a work's record | work_identity, bibliographic_information | work_record |
| catalog::CC_RETIRE_CATALOG_RECORD_V0 | Mark a record retired so it is no longer offered as current | work_identity | retired_record |
| catalog::CC_SEARCH_CATALOG_V0 | Select the current records matching the staff member's terms | search_terms | matching_records |
| catalog::CC_ASSEMBLE_BOOK_DETAILS_V0 | Assemble a work's record with the copies belonging to it | work_identity | book_details |
| catalog::CC_APPEND_CATALOG_OPERATION_V0 | Append a durable account of a performed catalog operation | staff_identity, operation_performed | operation_record |

## 6. New Intents

<!-- register:new_intents -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| catalog::IN_REGISTER_BOOK_V0 | A request to register a new book | catalog::WF_REGISTER_BOOK_V0 | staff_identity, bibliographic_information |
| catalog::IN_REGISTER_PHYSICAL_COPY_V0 | A request to register a copy against a work | catalog::WF_REGISTER_PHYSICAL_COPY_V0 | staff_identity, copy_identity, work_identity |
| catalog::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | A request to update a registered work | catalog::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | staff_identity, work_identity, bibliographic_information |
| catalog::IN_RETIRE_CATALOG_RECORD_V0 | A request to retire an obsolete record | catalog::WF_RETIRE_CATALOG_RECORD_V0 | staff_identity, work_identity |
| catalog::IN_SEARCH_CATALOG_V0 | A request to locate materials | catalog::WF_SEARCH_CATALOG_V0 | staff_identity, search_terms |
| catalog::IN_RETRIEVE_BOOK_DETAILS_V0 | A request for the complete details of a book | catalog::WF_RETRIEVE_BOOK_DETAILS_V0 | staff_identity, work_identity |

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes -->
| Code | Note |
|------|------|
| catalog::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Reads authorization; deciding who is authorized belongs to patron and is deferred to a future change request. |
| catalog::CC_APPEND_CATALOG_OPERATION_V0 | Appends only to the catalog's own journal; no peer store is written. |
