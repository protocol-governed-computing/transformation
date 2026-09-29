# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

**Stage:** 8 — Authoring Mandate
**CR:** cr_05_catalog
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the twenty-six redeclared artifacts are authored
whole in their subdomain.

---

## 1. Build Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| EXTEND | 26 | The catalog's six rule-applying contracts, its ten acts and their ten gates, redeclared whole so that the catalog holds every rule it applies and checks what it records. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | catalog |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | catalog |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | catalog |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | catalog |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | catalog |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | catalog |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | catalog |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | catalog |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | catalog |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | catalog |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | catalog |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Confirm the staff member may perform catalog operations | staff_credentials | is_authorized |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | Confirms a registration carries what a work and an edition require, before any identity is claimed | work_fields, book_fields, barcode | valid |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | Validates, assembles and writes an edition record against the work it belongs to | book_fields, identity_key | book_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | Assembles the edition record against a resolved work and writes it | identity_key, edition_fields | edition_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | Record a copy against exactly one book | identity_key, barcode, copy_fields | book_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Changes a registered edition's descriptive content and refuses a change that would duplicate another edition | identity_key, updated_fields | book_record |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| book_library_mgmt::IN_REGISTER_BOOK_V0 | A request to register a book together with its first physical copy | book_library_mgmt::WF_REGISTER_BOOK_V0 | staff_credentials, title, author, publication_year, book_fields, barcode, copy_fields, staff_id |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | The boundary that admits a request to register a further edition of a work the catalog already holds | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | staff_credentials, staff_id, title, author, publication_year, subject |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | A request to register a further copy against a registered book | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | staff_credentials, identity_key, barcode, copy_fields, staff_id |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | A request to change a registered book's description | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | staff_credentials, staff_id, identity_key, updated_fields |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | A request to retire a book record judged obsolete | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | staff_credentials, identity_key, staff_id |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | A request to return a retired book record to the registered state | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | staff_credentials, identity_key, staff_id |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | A request to retire a lost or damaged copy | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | staff_credentials, barcode, staff_id |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | A request to return a retired copy to the registered state | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | staff_credentials, barcode, staff_id |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | A request for a book's complete details with the copies held | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | staff_credentials, identity_key, staff_id |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | A request to locate material by subject or by title | book_library_mgmt::WF_SEARCH_CATALOG_V0 | staff_credentials, search_criteria, staff_id |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Superseded and not in force; left unchanged. It still names the rules its contract no longer takes, which a superseded act may. |
