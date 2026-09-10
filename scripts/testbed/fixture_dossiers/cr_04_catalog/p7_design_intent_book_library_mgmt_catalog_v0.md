# Stage 7 — Design Intent: book_library_mgmt / catalog
**Stage:** 7 — Design Intent
**CR:** cr_04_catalog
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The form the publication year takes at the boundary of registering a further edition | Three of the four statements of the form say number, and every year the library supplies is a number. | `publication_year` is declared `integer` in `book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0`, matching its two sibling boundaries. | S6 boundary_rules A_YEAR_IS_A_NUMBER |
| Which requirements a correction keeps | Its four steps read the record named and the details being changed, and nothing else the request supplied. | `book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1` is authored requiring the five its steps read, and supersedes `..._V0`. A boundary is rendered whole from the design, so a requirement is withdrawn by authoring the successor that does not carry it, never by amending the predecessor to say less than it said. | S6 boundary_rules REQUIRES_ONLY_WHAT_IT_USES |
| Whether registering a work is corrected here | Its steps read `subject` at the top of the request and rebuild the details of the book themselves; every present caller sends `subject` nested inside the details it supplies. | `book_library_mgmt::IN_REGISTER_BOOK_V0` is unchanged. Requiring `subject` moves the boundary and every caller together, and no caller moves inside this change. | S6 boundary_rules NO_CORRECT_REQUEST_BECOMES_HARDER |
| Whether any workflow changes | The three operations read exactly what they read today. | No workflow, capability contract, capability transform, side effect or store is altered. Each of the three boundaries is re-rendered whole; the act it admits is restated unchanged. | S6 pps_artifacts_requiring_action #4 |
| Whether authority is reached | The three things that decide who may perform an operation are read by no step of any of the subdomain's ten operations. | `staff_credentials`, `authorization_rules` and `staff_id` are restated unchanged in all three boundaries, in the same form and with the same requiredness. | S6 boundary_rules AUTHORITY_IS_UNTOUCHED |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | EXTEND | The boundary that admits a request to register a further edition of a work the catalog already holds | One requirement changes form; the other ten are restated unchanged, because an EXTEND re-renders the boundary whole. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | REPLACE |  | Requires three things no step of its operation reads. Stood down and superseded, because withdrawing a requirement makes the boundary say less than it said, and an amendment may only say more. | S6 pps_artifacts_requiring_action #2 |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | REVIEW | The boundary that admits a request to register a work, its first edition and that edition's first physical copy | Requires ten things where its act reads eleven. Unchanged: the missing requirement is one every present caller sends nested inside the details of the book rather than where the act reads it. | S6 pps_artifacts_requiring_action #3 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | REUSE | The governed sequence that registers a further edition of a work already held | Reads all eleven things its boundary requires. Named because the boundary is its entry node and an EXTEND must state the act it admits. | S6 pps_artifacts_requiring_action #4 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | REPLACE |  | Names the boundary being superseded as its entry. An act states the boundary that admits it, so a successor boundary means a successor act. Nothing consumes this act, so the substitution reaches nothing further. | S6 pps_artifacts_requiring_action #5 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | REVIEW | The governed sequence that registers a work, its first edition and that edition's first physical copy | Reads eleven things, one of which its boundary does not require, and rebuilds the details of the book from the top of the request. Unchanged, and named as the evidence that the third correction reaches a caller. | S6 pps_artifacts_requiring_action #6 |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | REUSE | The actor whose authorization every catalog operation binds | The actor all three acts run as. Named because an EXTEND re-renders the boundary and the act it admits must state its actor. | S6 ownership #5 |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | REUSE | Decides whether the staff member may perform the operation | The first act of all three sequences, and what consumes the three authority requirements. Unchanged. | S6 ownership #5 |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | REUSE | Checks a submitted description against the schema supplied with it | Named by two of the three acts; what reads `publication_year` in the form the boundary declares. | S6 pps_artifacts_requiring_action #4 |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | REUSE | Resolves the record a correction names | What reads `identity_key`, one of the five requirements the correction keeps. | S6 pps_artifacts_requiring_action #5 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | REUSE | Changes the details of a resolved record | What reads `updated_fields`, and what reads none of the three requirements withdrawn. | S6 pps_artifacts_requiring_action #5 |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | REUSE | Records that a catalog operation occurred | The last act of all three sequences. Unchanged. | S6 pps_artifacts_requiring_action #4 |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | REUSE | Resolves the work a further edition attaches to | Named by the act that registers a further edition; unchanged, and restated because the boundary above it is re-rendered whole. | S6 pps_artifacts_requiring_action #4 |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | REUSE | Claims the identity of an edition | Named by two of the three acts; what reads the title, the author and the publication year. | S6 pps_artifacts_requiring_action #4 |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | REUSE | Registers a further edition against a resolved work | Named by the act that registers a further edition; unchanged. | S6 pps_artifacts_requiring_action #4 |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | REUSE | Claims the identity of a work | Named by the act that registers a work; unchanged. | S6 pps_artifacts_requiring_action #6 |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | REUSE | Claims the barcode of a physical copy | Named by the act that registers a work; unchanged. | S6 pps_artifacts_requiring_action #6 |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | REUSE | Registers an edition against a claimed identity | Named by the act that registers a work; what reads the subject the boundary now requires. | S6 pps_artifacts_requiring_action #6 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | REUSE | Puts a physical copy on a shelf | Named by the act that registers a work; unchanged. | S6 pps_artifacts_requiring_action #6 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | REUSE | Binds the catalog's acts to the capabilities and stores that carry them | Named because the three acts are bound through it; unchanged by this change. | S6 ownership #6 |
| book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | REUSE | The moment the act announces when a correction completes | Announced at the act's successful ending. Unchanged, and named because an EXTEND re-renders the act whole and the announcement must be restated with it. | S6 pps_artifacts_requiring_action #5 |
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | REVIEW | Declares the six stores the catalog owns and the paths they occupy | Declares no form for any detail it holds, which is why the form of a publication year rests on agreement rather than on a declaration. Unchanged by this change. | S6 pps_artifacts_requiring_action #7 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family | Code | Summary | Owner Subdomain | Status | Source Finding |
|-----------|--------|------|---------|-----------------|--------|----------------|
| Admitting a request to correct bibliographic information | IN | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | A request to change a registered book's description | catalog | NEW | S6 governance_outcome #2 |
| The three operations | WF | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | Corrects what the library publishes about a registered book | catalog | NEW | S6 governance_outcome #2 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | Unchanged | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 ownership #6 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | Unchanged | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 ownership #6 |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 existing_inventory IN_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | CC | SUCCESS -> book_library_mgmt::CC_RESOLVE_WORK_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | CC | SUCCESS -> book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_RESOLVE_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|-----------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| NONE IDENTIFIED |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_ADDITIONAL_EDITION | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_ADDITIONAL_EDITION', 'staff_id': '$.payload.staff_id', 'subject': '$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | author | payload.author | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | publication_year | payload.publication_year | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | title | payload.title | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_fields | {'author': '$.payload.author', 'identity_key': '$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key', 'publication_year': '$.payload.publication_year', 'state': 'REGISTERED', 'subject': '$.payload.subject', 'title': '$.payload.title', 'work_key': '$.results.CC_RESOLVE_WORK_V0.work_key'} | S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_schema | payload.edition_schema | S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | INPUT | author | payload.author | S7 execution_topology CC_RESOLVE_WORK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | INPUT | title | payload.title | S7 execution_topology CC_RESOLVE_WORK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | payload.edition_fields | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_schema | payload.edition_schema | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_fields | payload.work_fields | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_schema | payload.work_schema | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | UPDATE_BIBLIOGRAPHIC_INFORMATION | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'UPDATE_BIBLIOGRAPHIC_INFORMATION', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_RESOLVE_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | updated_fields | payload.updated_fields | S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | staff_credentials | object | YES | — | The credentials of the staff member making the request. Consumed by the decision about who may act. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | authorization_rules | array | YES | — | The rules that decide whether this staff member may perform the operation. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | staff_id | string | YES | — | The staff member accountable for the request. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | title | string | YES | — | The title of the work the edition belongs to. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | author | string | YES | — | The author of the work the edition belongs to. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | publication_year | integer | YES | — | The year the edition was published. Stated as a number, as the catalog holds it and as both sibling boundaries declare it. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | subject | array | YES | — | The subject headings of the edition. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_fields | object | YES | — | The details of the edition being registered. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_schema | object | YES | — | The description the edition is checked against. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | work_fields | object | YES | — | The details of the work the edition is attached to. |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | work_schema | object | YES | — | The description the work is checked against. |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | staff_credentials | object | YES | — | The credentials of the staff member making the request. Consumed by the decision about who may act. |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | authorization_rules | array | YES | — | The rules that decide whether this staff member may perform the operation. |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | staff_id | string | YES | — | The staff member accountable for the request. |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | identity_key | string | YES | — | The record being corrected. |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | updated_fields | object | YES | — | The details being changed. A correction supplies these and does not restate the fields it leaves alone. |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|----------------------|-----------------------------|----------------------------------|----------------|
| NONE IDENTIFIED |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|
| NONE IDENTIFIED |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|-----------|-----|-------|----------------|
| NONE IDENTIFIED |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | core.workflow | WF_REGISTER_ADDITIONAL_EDITION_V0 | S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | core.workflow | WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | S7 existing_inventory WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | supersedes | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | S7 existing_inventory IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | supersedes | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | S7 existing_inventory WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | catalog | 1 | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 |
| REPLACE | catalog | 2 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| NEW | catalog | 2 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| NONE IDENTIFIED |

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| Registering a further edition | The publication year is not supplied | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | NACK | S1 operation_refusals #1 |
| Correcting bibliographic information | The record to correct is not named | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | NACK | S1 operation_refusals #2 |
| Correcting bibliographic information | No changed fields are supplied | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | NACK | S1 operation_refusals #3 |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|
| NONE IDENTIFIED |

---

## 20. Refusal Governance Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|
| NONE IDENTIFIED |

---

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`10aa26e1582f…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the amendment of the one boundary §2 marks EXTEND, the authoring of
the successor boundary and successor act §3 declares, and the standing down of the two artifacts §2
marks REPLACE. It authorizes nothing else, and in particular it does not authorize requiring the
subject at the boundary that registers a work.

That third correction was designed, emitted and withdrawn, and the withdrawal is the reason this
closure differs from the one first written. The act reads the subject at the top of the request and
rebuilds the details of the book itself; every caller sends the subject nested inside the details it
supplies. Requiring it turned the library's own exercise of the catalog from failing at the second
edition to failing at the first registration. The defect is real and is deferred with its ground
recorded, to a change where the boundary and its callers move together.

The shape of §2 changed at this closure and the reason is worth naming. A boundary is rendered whole
from the design, so an amendment may say more than its predecessor and may never say less; withdrawing
three requirements no step reads is therefore a supersession, not an amendment. The act that named the
withdrawn boundary as its entry is superseded with it, because an act states the boundary that admits
it. Nothing consumes that act, so the substitution stops there.

One decision of §1 is worth naming at this closure, because it reads against a constraint the seed
states. The seed rules that no operation gains a requirement in this change. Registering a work
gains one. The approval takes the constraint to protect a requester rather than a declaration: the
act already reads the subject, and every request the library makes already supplies it, so no correct
request becomes harder to make. A requirement that asked for something new would not be permitted by
the same reading.
