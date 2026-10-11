# Authoring Mandate — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_01_catalog
  Status: DRAFT
  Feeds: Artifact Authoring
registers:
  build_order:
    columns:
    - Wave
    - Step
    - Code
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Depends On
    rows:
    - Wave: '1'
      Step: '1'
      Code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '2'
      Code: CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '3'
      Code: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '4'
      Code: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '5'
      Code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '6'
      Code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '7'
      Code: book_library_mgmt::EV_BOOK_RETIRED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '8'
      Code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '2'
      Step: '9'
      Code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - Wave: '2'
      Step: '10'
      Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - Wave: '2'
      Step: '11'
      Code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0, capability_side_effects::CS_REGISTRY_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '12'
      Code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_side_effects::CS_REGISTRY_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '13'
      Code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_side_effects::CS_REGISTRY_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '14'
      Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '15'
      Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '16'
      Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '17'
      Code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '18'
      Code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '19'
      Code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '20'
      Code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '21'
      Code: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_side_effects::CS_MUTABLE_JSON_V0, capability_transforms::CT_PURE_FILTER_RECORDS_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '22'
      Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_side_effects::CS_MUTABLE_JSON_V0, capability_transforms::CT_PURE_FILTER_RECORDS_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '2'
      Step: '23'
      Code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: capability_side_effects::CS_APPENDONLY_JSONL_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Wave: '3'
      Step: '24'
      Code: book_library_mgmt::IN_REGISTER_BOOK_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '25'
      Code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '26'
      Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '27'
      Code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '28'
      Code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '29'
      Code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '30'
      Code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '31'
      Code: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '32'
      Code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '4'
      Step: '33'
      Code: book_library_mgmt::WF_REGISTER_BOOK_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_REGISTER_BOOK_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_BOOK_REGISTERED_V0, book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    - Wave: '4'
      Step: '34'
      Code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    - Wave: '4'
      Step: '35'
      Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0, book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    - Wave: '4'
      Step: '36'
      Code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_BOOK_RETIRED_V0
    - Wave: '4'
      Step: '37'
      Code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    - Wave: '4'
      Step: '38'
      Code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_BOOK_REGISTERED_V0
    - Wave: '4'
      Step: '39'
      Code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    - Wave: '4'
      Step: '40'
      Code: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_SEARCH_CATALOG_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Wave: '4'
      Step: '41'
      Code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Wave: '5'
      Step: '42'
      Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Position: '3'
      Code: book_library_mgmt::CC_UNSCHEDULED_STEP_V0
    - Position: '3'
      Code: book_library_mgmt::WF_REGISTER_BOOK_V0
    - Position: '4'
      Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '40'
      Description: 1 AC, 9 IN, 9 WF, 13 CC, 1 CT, 5 EV, 1 RB, 1 STRUCTURE — every identity Stage 7 assigned
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '1'
      Description: capability_side_effects::CS_MUTABLE_JSON_V0 gains an operation that publishes records; authored in the platform, not scheduled here
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::EV_BOOK_RETIRED_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REGISTER_BOOK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REGISTER_BOOK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Subdomain Field: catalog
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Purpose: Form the single key the registry claims from a book's three identifying attributes, so that a second registration of the same book is refused
      Inputs: title:string, author:string, publication_year:integer
      Outputs: identity_key:string
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: book_library_mgmt::IN_REGISTER_BOOK_V0
      Purpose: Admit a request to register a book together with its first physical copy
      Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Inputs: staff_credentials:object, authorization_rules:array, title:string, author:string, publication_year:integer, book_fields:object, book_schema:object, barcode:string, copy_fields:object, staff_id:string
    - Code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Purpose: Admit a request to register a further copy against a registered book
      Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Inputs: staff_credentials:object, authorization_rules:array, identity_key:string, barcode:string, copy_fields:object, staff_id:string
    - Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Purpose: Admit a request to change a registered book's description
      Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Inputs: staff_credentials:object, authorization_rules:array, title:string, author:string, publication_year:integer, updated_fields:object, staff_id:string
    - Code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Purpose: Admit a request to retire a book record judged obsolete
      Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Inputs: staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string
    - Code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Purpose: Admit a request to retire a lost or damaged copy
      Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Inputs: staff_credentials:object, authorization_rules:array, barcode:string, staff_id:string
    - Code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Purpose: Admit a request to return a retired book record to the registered state
      Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Inputs: staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string
    - Code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Purpose: Admit a request to return a retired copy to the registered state
      Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Inputs: staff_credentials:object, authorization_rules:array, barcode:string, staff_id:string
    - Code: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Purpose: Admit a request to locate material by subject or by title
      Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Inputs: staff_credentials:object, authorization_rules:array, search_criteria:object, staff_id:string
    - Code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Purpose: Admit a request for a book's complete details with the copies held
      Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Inputs: staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Note: Reads whether the staff member is authorized from what the caller supplies, and grants nothing. Deciding who is authorized is a dependency gap owned by the staff function, which a future change request introduces. No store of authorized staff is declared here.
    - Code: capability_side_effects::CS_MUTABLE_JSON_V0
      Note: 'Extended by this change with an operation that publishes records. A platform artifact amended by a business change request: additive, so none of its twelve consumers is affected, and authored in the platform repository rather than scheduled in this mandate.'
```

> The mandate below schedules every artifact Stage 7 designed. What is wrong is that some of it cannot be built in the order given, and some of it is already there.

The forty artifacts Stage 7 designed, scheduled in dependency order. Nothing is added here and nothing
is dropped: the mandate orders the build, it does not decide it.

---

## 1. Build Dependency Order

Wave 1 depends on nothing: the store declaration, the identity transform, the actor and the five
business moments. Wave 2 composes the thirteen capability contracts over those and over the platform
mechanisms reused as-is. Wave 3 declares the nine entry points. Wave 4 wires the nine workflows, each
over its own entry point, its contracts and the moments it recognises. Wave 5 is the runtime binding,
which binds every workflow and therefore comes last.

The platform's `capability_side_effects::CS_MUTABLE_JSON_V0` is extended, not authored, so it is
not a step here — it already exists in the composition, and a mandate schedules only what does not.
It is recorded in §3 and §7.

---

## 2. Critical Path

The longest chain runs store declaration → identity claim → the registration workflow → the runtime
binding. Nothing in the catalog can be exercised until that chain is complete.

---

## 3. Artifact Summary

---

## 4. Subdomain Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes

No catalog artifact writes into a store another subdomain owns.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | p7_design_intent_book_library_mgmt_catalog_v0.md | GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring | per build_order | PENDING |
