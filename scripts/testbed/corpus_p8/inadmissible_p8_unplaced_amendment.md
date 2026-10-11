# Authoring Mandate — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_02_catalog
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
      Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '2'
      Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '3'
      Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '1'
      Step: '4'
      Code: book_library_mgmt::EV_WORK_REGISTERED_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '2'
      Step: '5'
      Code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    - Wave: '2'
      Step: '6'
      Code: book_library_mgmt::CC_RESOLVE_WORK_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    - Wave: '2'
      Step: '7'
      Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '3'
      Step: '8'
      Code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '4'
      Step: '9'
      Code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::CC_RESOLVE_WORK_V0, book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    - Position: '2'
      Code: book_library_mgmt::CC_RESOLVE_WORK_V0
    - Position: '3'
      Code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '9'
      Description: 3 CT, 1 EV, 3 CC, 1 IN, 1 WF — every identity Stage 7 assigned
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '7'
      Description: STRUCTURE_CATALOG_STORAGE_V0, RB_CATALOG_BINDINGS_V0, WF_REGISTER_BOOK_V0, CC_REGISTER_BOOK_V0, CC_VALIDATE_BOOK_SUBMISSION_V0, CC_SEARCH_CATALOG_V0 and CC_ASSEMBLE_BOOK_DETAILS_V0 — amended in place, never authored, because each identity already exists in the composition
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::EV_WORK_REGISTERED_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_RESOLVE_WORK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_REGISTER_BOOK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Subdomain Field: catalog
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Purpose: Form the single key the registry claims for a work from its title and author, so that two registrations describing the same work resolve to one work
      Inputs: title:string, author:string
      Outputs: work_key:string
    - Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Purpose: Select the records matching stated criteria and return none when none match, so an edition the library holds no copies of can still be described
      Inputs: source:array, filter:object
      Outputs: extracted:array
    - Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Purpose: Group records by the value of a named attribute, so a search can answer once per work rather than once per matching edition
      Inputs: source:array, attribute:string
      Outputs: grouped:array
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Purpose: Admit a request to register a further edition of a work the catalog already holds
      Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Inputs: staff_credentials:object, authorization_rules:array, staff_id:string, title:string, author:string, publication_year:string, subject:array, edition_fields:object, edition_schema:object, work_fields:object, work_schema:object
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Note: Reused unchanged. Reads whether the staff member is authorized from what the caller supplies and grants nothing; deciding who is authorized remains a dependency gap owned by the staff function. The operations this change adds reach it first, as every existing operation does.
    - Code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Note: Extended, not authored. Gains the WORKS store and the WORK_IDENTITY_REGISTRY store. Both are written only by contracts of this subdomain, and no contract of another subdomain reads or writes either.
    - Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Note: Extended, not authored. Binds the new workflow to the same three substrates and the same storage declaration the catalog already uses; no new substrate is required.
    - Code: book_library_mgmt::WF_REGISTER_BOOK_V0
      Note: Extended, not authored. Gains one node — the work claim — placed after validation and before every other claim, so every claim still precedes every write.
    - Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Note: Extended, not authored. The edition record it assembles now carries the key of the work the edition belongs to; its composition is otherwise unchanged.
    - Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Note: Extended, not authored. Validates the work's identifying attributes alongside the edition's, before any identity is claimed.
    - Code: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Note: Extended, not authored. Gains a grouping step after its selection step; the records it selects and the terms it accepts are unchanged.
    - Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Note: Extended, not authored. Gains a read of the work record, so a retrieval carries the work the edition belongs to without a second lookup.
    - Code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Note: Writes only into stores this subdomain declares. Its claim yields ALREADY_EXISTS when the work is already held, and the registration routes that onward rather than refusing — the one claim in this subdomain whose second attempt is not a refusal.
```

> Stage 7 declared nine artifacts amended by this change. The mandate below places every artifact it schedules and forgets one of the artifacts it amends.

Eight artifacts are scheduled — the eight the design assigns identities to. The seven the design
extends are not build steps: their identities already exist in the composition, and scheduling one
would mandate authoring an artifact that is already there. They are recorded in §3 and §7 instead.

---

## 1. Build Order

Four waves: the transforms and the business moment first, since nothing they need is authored here;
then the contracts that compose them; then the entry point; then the workflow that routes between
them. `CC_REGISTER_ADDITIONAL_EDITION_V0` depends on no new artifact — every capability it composes
is one the composition already carries.

---

## 2. Critical Path

The longest chain runs through the work key: the transform that forms it, the contract that resolves
a work by it, and the workflow that cannot be built until that contract exists.

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
