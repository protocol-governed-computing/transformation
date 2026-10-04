# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

**Stage:** 8 — Authoring Mandate
**CR:** cr_02_catalog
**Status:** DRAFT
**Feeds:** Artifact Authoring

Eight artifacts are scheduled — the eight the design assigns identities to. The seven the design
extends are not build steps: their identities already exist in the composition, and scheduling one
would mandate authoring an artifact that is already there. They are recorded in §3 and §7 instead.

---

## 1. Build Order

<!-- register:build_order -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | NEW | catalog | — |
| 1 | 2 | book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | NEW | catalog | — |
| 1 | 3 | book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | NEW | catalog | — |
| 1 | 4 | book_library_mgmt::EV_WORK_REGISTERED_V0 | NEW | catalog | — |
| 2 | 5 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | NEW | catalog | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 |
| 2 | 6 | book_library_mgmt::CC_RESOLVE_WORK_V0 | NEW | catalog | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 |
| 2 | 7 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | NEW | catalog | — |
| 3 | 8 | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | NEW | catalog | — |
| 4 | 9 | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | NEW | catalog | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::CC_RESOLVE_WORK_V0, book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 |

Four waves: the transforms and the business moment first, since nothing they need is authored here;
then the contracts that compose them; then the entry point; then the workflow that routes between
them. `CC_REGISTER_ADDITIONAL_EDITION_V0` depends on no new artifact — every capability it composes
is one the composition already carries.

---

## 2. Critical Path

<!-- register:critical_path -->
| Position | Code |
|----------|------|
| 1 | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 |
| 2 | book_library_mgmt::CC_RESOLVE_WORK_V0 |
| 3 | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 |

The longest chain runs through the work key: the transform that forms it, the contract that resolves
a work by it, and the workflow that cannot be built until that contract exists.

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 9 | 3 CT, 1 EV, 3 CC, 1 IN, 1 WF — every identity Stage 7 assigned |
| EXTEND | 7 | STRUCTURE_CATALOG_STORAGE_V0, RB_CATALOG_BINDINGS_V0, WF_REGISTER_BOOK_V0, CC_REGISTER_BOOK_V0, CC_VALIDATE_BOOK_SUBMISSION_V0, CC_SEARCH_CATALOG_V0 and CC_ASSEMBLE_BOOK_DETAILS_V0 — amended in place, never authored, because each identity already exists in the composition |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | catalog |
| book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | catalog |
| book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | catalog |
| book_library_mgmt::EV_WORK_REGISTERED_V0 | catalog |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | catalog |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | catalog |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | catalog |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | catalog |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | catalog |
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | catalog |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | catalog |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | catalog |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | catalog |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | catalog |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | Form the single key the registry claims for a work from its title and author, so that two registrations describing the same work resolve to one work | title:string, author:string | work_key:string |
| book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | Select the records matching stated criteria and return none when none match, so an edition the library holds no copies of can still be described | source:array, filter:object | extracted:array |
| book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | Group records by the value of a named attribute, so a search can answer once per work rather than once per matching edition | source:array, attribute:string | grouped:array |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | Admit a request to register a further edition of a work the catalog already holds | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | staff_credentials:object, authorization_rules:array, staff_id:string, title:string, author:string, publication_year:string, subject:array, edition_fields:object, edition_schema:object, work_fields:object, work_schema:object |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Reused unchanged. Reads whether the staff member is authorized from what the caller supplies and grants nothing; deciding who is authorized remains a dependency gap owned by the staff function. The operations this change adds reach it first, as every existing operation does. |
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | Extended, not authored. Gains the WORKS store and the WORK_IDENTITY_REGISTRY store. Both are written only by contracts of this subdomain, and no contract of another subdomain reads or writes either. |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | Extended, not authored. Binds the new workflow to the same three substrates and the same storage declaration the catalog already uses; no new substrate is required. |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | Extended, not authored. Gains one node — the work claim — placed after validation and before every other claim, so every claim still precedes every write. |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | Extended, not authored. The edition record it assembles now carries the key of the work the edition belongs to; its composition is otherwise unchanged. |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | Extended, not authored. Validates the work's identifying attributes alongside the edition's, before any identity is claimed. |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | Extended, not authored. Gains a grouping step after its selection step; the records it selects and the terms it accepts are unchanged. |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Extended, not authored. Gains a read of the work record, so a retrieval carries the work the edition belongs to without a second lookup. |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | Writes only into stores this subdomain declares. Its claim yields ALREADY_EXISTS when the work is already held, and the registration routes that onward rather than refusing — the one claim in this subdomain whose second attempt is not a refusal. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | p7_design_intent_book_library_mgmt_catalog_v0.md | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring (authoring tier) | per build_order | PENDING |

---

## gov_projection — Governed Handoff to Artifact Authoring

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 7 | new_artifacts · existing_inventory · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · structure_stores · artifact_summary |
| **Emits** → Artifact Authoring | build_order · critical_path · mandate_artifact_summary · field_declarations · new_capabilities · new_intents · cross_subdomain_notes |
