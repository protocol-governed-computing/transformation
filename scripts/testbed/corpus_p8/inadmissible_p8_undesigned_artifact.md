# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

**Stage:** 8 — Authoring Mandate
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Artifact Authoring

The forty artifacts Stage 7 designed, scheduled in dependency order. Nothing is added here and nothing
is dropped: the mandate orders the build, it does not decide it.

---

## 1. Build Dependency Order

<!-- register:build_order -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | NEW | catalog | — |
| 1 | 2 | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | NEW | catalog | — |
| 1 | 3 | book_library_mgmt::AC_LIBRARY_STAFF_V0 | NEW | catalog | — |
| 1 | 4 | book_library_mgmt::EV_BOOK_REGISTERED_V0 | NEW | catalog | — |
| 1 | 5 | book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | NEW | catalog | — |
| 1 | 6 | book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | NEW | catalog | — |
| 1 | 7 | book_library_mgmt::EV_BOOK_RETIRED_V0 | NEW | catalog | — |
| 1 | 8 | book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | NEW | catalog | — |
| 2 | 9 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | NEW | catalog | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| 2 | 10 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | NEW | catalog | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| 2 | 11 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | NEW | catalog | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0, capability_side_effects::CS_REGISTRY_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 12 | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | NEW | catalog | capability_side_effects::CS_REGISTRY_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 13 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | NEW | catalog | capability_side_effects::CS_REGISTRY_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 14 | book_library_mgmt::CC_REGISTER_BOOK_V0 | NEW | catalog | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 15 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 16 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | NEW | catalog | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 17 | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | NEW | catalog | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 18 | book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | NEW | catalog | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 19 | book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | NEW | catalog | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 20 | book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | NEW | catalog | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 21 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | NEW | catalog | capability_side_effects::CS_MUTABLE_JSON_V0, capability_transforms::CT_PURE_FILTER_RECORDS_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 22 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | NEW | catalog | capability_side_effects::CS_MUTABLE_JSON_V0, capability_transforms::CT_PURE_FILTER_RECORDS_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | 23 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | NEW | catalog | capability_side_effects::CS_APPENDONLY_JSONL_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 3 | 24 | book_library_mgmt::IN_REGISTER_BOOK_V0 | NEW | catalog | — |
| 3 | 25 | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | — |
| 3 | 26 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | NEW | catalog | — |
| 3 | 27 | book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | NEW | catalog | — |
| 3 | 28 | book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | NEW | catalog | — |
| 3 | 29 | book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | NEW | catalog | — |
| 3 | 30 | book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | NEW | catalog | — |
| 3 | 31 | book_library_mgmt::IN_SEARCH_CATALOG_V0 | NEW | catalog | — |
| 3 | 32 | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | NEW | catalog | — |
| 4 | 33 | book_library_mgmt::WF_REGISTER_BOOK_V0 | NEW | catalog | book_library_mgmt::IN_REGISTER_BOOK_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_BOOK_REGISTERED_V0, book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 |
| 4 | 34 | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | NEW | catalog | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 |
| 4 | 35 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | NEW | catalog | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0, book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 |
| 4 | 36 | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | NEW | catalog | book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_BOOK_RETIRED_V0 |
| 4 | 37 | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | NEW | catalog | book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 |
| 4 | 38 | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | NEW | catalog | book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_BOOK_REGISTERED_V0 |
| 4 | 39 | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | NEW | catalog | book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0, book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 |
| 4 | 40 | book_library_mgmt::WF_SEARCH_CATALOG_V0 | NEW | catalog | book_library_mgmt::IN_SEARCH_CATALOG_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| 4 | 41 | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | NEW | catalog | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| 5 | 42 | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | NEW | catalog | book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 5 | 43 | book_library_mgmt::CC_ARCHIVE_CATALOG_RECORD_V0 | NEW | catalog | — |

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

<!-- register:critical_path -->
| Position | Code |
|----------|------|
| 1 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| 2 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |
| 3 | book_library_mgmt::WF_REGISTER_BOOK_V0 |
| 4 | book_library_mgmt::RB_CATALOG_BINDINGS_V0 |

The longest chain runs store declaration → identity claim → the registration workflow → the runtime
binding. Nothing in the catalog can be exercised until that chain is complete.

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 40 | 1 AC, 9 IN, 9 WF, 13 CC, 1 CT, 5 EV, 1 RB, 1 STRUCTURE — every identity Stage 7 assigned |
| EXTEND | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 gains an operation that publishes records; authored in the platform, not scheduled here |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | catalog |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | catalog |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | catalog |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | catalog |
| book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | catalog |
| book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | catalog |
| book_library_mgmt::EV_BOOK_RETIRED_V0 | catalog |
| book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | catalog |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | catalog |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | catalog |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | catalog |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | catalog |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | catalog |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | catalog |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | catalog |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | catalog |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | catalog |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | catalog |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | catalog |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | catalog |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | catalog |
| book_library_mgmt::CC_ARCHIVE_CATALOG_RECORD_V0 | catalog |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | Form the single key the registry claims from a book's three identifying attributes, so that a second registration of the same book is refused | title:string, author:string, publication_year:integer | identity_key:string |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| book_library_mgmt::IN_REGISTER_BOOK_V0 | Admit a request to register a book together with its first physical copy | book_library_mgmt::WF_REGISTER_BOOK_V0 | staff_credentials:object, authorization_rules:array, title:string, author:string, publication_year:integer, book_fields:object, book_schema:object, barcode:string, copy_fields:object, staff_id:string |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | Admit a request to register a further copy against a registered book | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | staff_credentials:object, authorization_rules:array, identity_key:string, barcode:string, copy_fields:object, staff_id:string |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Admit a request to change a registered book's description | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | staff_credentials:object, authorization_rules:array, title:string, author:string, publication_year:integer, updated_fields:object, staff_id:string |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | Admit a request to retire a book record judged obsolete | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | Admit a request to retire a lost or damaged copy | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | staff_credentials:object, authorization_rules:array, barcode:string, staff_id:string |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | Admit a request to return a retired book record to the registered state | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | Admit a request to return a retired copy to the registered state | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | staff_credentials:object, authorization_rules:array, barcode:string, staff_id:string |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | Admit a request to locate material by subject or by title | book_library_mgmt::WF_SEARCH_CATALOG_V0 | staff_credentials:object, authorization_rules:array, search_criteria:object, staff_id:string |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | Admit a request for a book's complete details with the copies held | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Reads whether the staff member is authorized from what the caller supplies, and grants nothing. Deciding who is authorized is a dependency gap owned by the staff function, which a future change request introduces. No store of authorized staff is declared here. |
| capability_side_effects::CS_MUTABLE_JSON_V0 | Extended by this change with an operation that publishes records. A platform artifact amended by a business change request: additive, so none of its twelve consumers is affected, and authored in the platform repository rather than scheduled in this mandate. |

No catalog artifact writes into a store another subdomain owns.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | p7_design_intent_book_library_mgmt_catalog_v0.md | GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring | per build_order | PENDING |
