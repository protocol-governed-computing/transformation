# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_05_catalog
  Status: DRAFT
  Feeds: Construction
registers:
  build_order:
    columns:
    - Wave
    - Step
    - Code
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Depends On
    rows: []
  critical_path:
    columns:
    - Position
    - Code
    rows: []
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '26'
      Description: The catalog's six rule-applying contracts, its ten acts and their ten gates, redeclared whole so that the catalog holds every rule it applies and checks what it records.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REGISTER_BOOK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REGISTER_BOOK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Subdomain Field: catalog
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Purpose: Confirm the staff member may perform catalog operations
      Inputs: staff_credentials
      Outputs: is_authorized
    - Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Purpose: Confirms a registration carries what a work and an edition require, before any identity is claimed
      Inputs: work_fields, book_fields, barcode
      Outputs: valid
    - Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Purpose: Validates, assembles and writes an edition record against the work it belongs to
      Inputs: book_fields, identity_key
      Outputs: book_record
    - Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Purpose: Assembles the edition record against a resolved work and writes it
      Inputs: identity_key, edition_fields
      Outputs: edition_record
    - Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Purpose: Record a copy against exactly one book
      Inputs: identity_key, barcode, copy_fields
      Outputs: book_record
    - Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Purpose: Changes a registered edition's descriptive content and refuses a change that would duplicate another edition
      Inputs: identity_key, updated_fields
      Outputs: book_record
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: book_library_mgmt::IN_REGISTER_BOOK_V0
      Purpose: A request to register a book together with its first physical copy
      Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Inputs: staff_credentials, title, author, publication_year, book_fields, barcode, copy_fields, staff_id
    - Code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Purpose: The boundary that admits a request to register a further edition of a work the catalog already holds
      Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Inputs: staff_credentials, staff_id, title, author, publication_year, subject
    - Code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Purpose: A request to register a further copy against a registered book
      Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Inputs: staff_credentials, identity_key, barcode, copy_fields, staff_id
    - Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Purpose: A request to change a registered book's description
      Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Inputs: staff_credentials, staff_id, identity_key, updated_fields
    - Code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Purpose: A request to retire a book record judged obsolete
      Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Inputs: staff_credentials, identity_key, staff_id
    - Code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Purpose: A request to return a retired book record to the registered state
      Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Inputs: staff_credentials, identity_key, staff_id
    - Code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Purpose: A request to retire a lost or damaged copy
      Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Inputs: staff_credentials, barcode, staff_id
    - Code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Purpose: A request to return a retired copy to the registered state
      Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Inputs: staff_credentials, barcode, staff_id
    - Code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Purpose: A request for a book's complete details with the copies held
      Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Inputs: staff_credentials, identity_key, staff_id
    - Code: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Purpose: A request to locate material by subject or by title
      Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Inputs: staff_credentials, search_criteria, staff_id
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Note: Superseded and not in force; left unchanged. It still names the rules its contract no longer takes, which a superseded act may.
```

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the twenty-six redeclared artifacts are authored
whole in their subdomain.

---

## 1. Build Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes
