# Stage 7 — Design Intent: book_library_mgmt / catalog
**Stage:** 7 — Design Intent
**CR:** cr_03_catalog
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW. Binding FQDNs are assigned here; business facts and placement decisions are not repeated.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Registering a book announces three moments at one ending. | An act announces every moment it completed. | §12 declares three `emit.EXIT_COMPLETED` rows against `WF_REGISTER_BOOK_V0`. Construction renders them as an ordered sequence; the platform seals that order and the runtime keeps it. | S4 design_decisions #1 |
| The order announced is the order the business completes them. | The order is normative and a reader of the account sees it. | The rows are read in document order — the work, then the book, then the physical copy — which is the order the act claims each identity. | S4 design_decisions #2 |
| Each remaining act announces the one moment it completes. | An act announces every moment it completed. | One `emit` row each. A sequence of one renders as a single name, which is what every act announcing elsewhere in the composition carries. | S4 design_decisions #3 |
| Reinstatement announces nothing. | Only moments the business already declared are announced. | Neither reinstatement act appears here. The business declares no moment for a reinstatement, and authoring one would be business content this design does not own. | S4 design_decisions #4 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXTEND | The governed sequence that registers a work, its first edition and that edition's first physical copy | Announces the moments it completes, where it announced nothing. Everything else about it is restated unchanged. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXTEND | The governed sequence that registers a further edition of a work the library already holds | Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged. | S6 pps_artifacts_requiring_action #2 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXTEND | The governed sequence that registers a further physical copy of an edition | Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged. | S6 pps_artifacts_requiring_action #3 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXTEND | The governed sequence that corrects what the library publishes about a book | Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged. | S6 pps_artifacts_requiring_action #4 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | EXTEND | The governed sequence that takes a book out of service | Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged. | S6 pps_artifacts_requiring_action #5 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | EXTEND | The governed sequence that takes a physical copy out of service | Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged. | S6 pps_artifacts_requiring_action #6 |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | REUSE | The actor whose authorization every catalog operation binds | The actor every catalog act runs as. An EXTEND re-renders an act whole, so the design must state the actor it carries or the re-rendered act would carry none. | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::EV_WORK_REGISTERED_V0 | REUSE | | The moment announced by the act that completes it. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | REUSE | | The moment announced by the act that completes it. | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | REUSE | | The moment announced by the act that completes it. | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | REUSE | | The moment announced by the act that completes it. | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::EV_BOOK_RETIRED_V0 | REUSE | | The moment announced by the act that completes it. | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | REUSE | | The moment announced by the act that completes it. | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | REUSE | | Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration. | S6 pps_artifacts_requiring_action #1 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| NONE IDENTIFIED |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_BOOK_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every work the library has catalogued |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::IN_REGISTER_BOOK_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 existing_inventory WF_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; ALREADY_EXISTS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CLAIM_WORK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_BOOK_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_CLAIM_COPY_BARCODE_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | CC | SUCCESS -> book_library_mgmt::CC_RESOLVE_WORK_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RESOLVE_WORK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CLAIM_COPY_BARCODE_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | CC | SUCCESS -> book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RETIRE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RETIRE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_RETIRE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_RETIRE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RETIRE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RETIRE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_RETIRE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_RETIRE_PHYSICAL_COPY_V0 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| NONE IDENTIFIED |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | title | payload.title | S7 execution_topology CC_CLAIM_WORK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | author | payload.author | S7 execution_topology CC_CLAIM_WORK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | work_fields | {'title': '$.payload.title', 'author': '$.payload.author'} | S7 execution_topology CC_CLAIM_WORK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_fields | {'title': '$.payload.title', 'author': '$.payload.author'} | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_schema | {'required': ['title', 'author']} | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_fields | {'title': '$.payload.title', 'author': '$.payload.author', 'publication_year': '$.payload.publication_year', 'subject': '$.payload.subject', 'state': 'REGISTERED'} | S7 execution_topology CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | payload.book_fields | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_schema | payload.book_schema | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | title | payload.title | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | author | payload.author | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | publication_year | payload.publication_year | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_schema | payload.book_schema | S7 execution_topology CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_CLAIM_COPY_BARCODE_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | payload.copy_fields | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_BOOK | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_BOOK', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.title'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | payload.edition_fields | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_schema | payload.edition_schema | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_fields | payload.work_fields | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_schema | payload.work_schema | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | INPUT | title | payload.title | S7 execution_topology CC_RESOLVE_WORK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | INPUT | author | payload.author | S7 execution_topology CC_RESOLVE_WORK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | title | payload.title | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | author | payload.author | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | publication_year | payload.publication_year | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_schema | payload.edition_schema | S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_fields | {'identity_key': '$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key', 'title': '$.payload.title', 'author': '$.payload.author', 'publication_year': '$.payload.publication_year', 'subject': '$.payload.subject', 'state': 'REGISTERED', 'work_key': '$.results.CC_RESOLVE_WORK_V0.work_key'} | S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_ADDITIONAL_EDITION | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_ADDITIONAL_EDITION', 'staff_id': '$.payload.staff_id', 'subject': '$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_CLAIM_COPY_BARCODE_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | payload.copy_fields | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_PHYSICAL_COPY | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_PHYSICAL_COPY', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.barcode'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_RESOLVE_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | updated_fields | payload.updated_fields | S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | UPDATE_BIBLIOGRAPHIC_INFORMATION | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'UPDATE_BIBLIOGRAPHIC_INFORMATION', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_RETIRE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | RETIRE_BOOK_RECORD | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'RETIRE_BOOK_RECORD', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_RETIRE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | RETIRE_PHYSICAL_COPY | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'RETIRE_PHYSICAL_COPY', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.barcode'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| NONE IDENTIFIED |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|
| NONE IDENTIFIED |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|
| NONE IDENTIFIED |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| NONE IDENTIFIED |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_WORK_REGISTERED_V0 | S4 design_decisions #2 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BOOK_REGISTERED_V0 | S4 design_decisions #2 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | S4 design_decisions #2 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BOOK_REGISTERED_V0 | S4 gap_register GAP-2 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | S4 gap_register GAP-2 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | S4 gap_register GAP-2 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BOOK_RETIRED_V0 | S4 gap_register GAP-2 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | S4 gap_register GAP-2 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|-----------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | catalog | 6 | book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 |
| NEW | catalog | 0 | |

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
| NONE IDENTIFIED |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|
| NONE IDENTIFIED |

---

## 20. Refusal — Governance-Surface Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|
| Announcing a moment | The act it names did not complete | p7 |  | S0 operation_refusals #1 |

---

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`9c2c693d882e…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the amendment of the six acts §2 marks EXTEND, each re-rendered whole
from this design, and nothing else.

One row of §2 was added before this closure and is the reason it is worth naming: the design
inventoried the six acts and the six moments and not the actor those acts run as. Every act carries
`book_library_mgmt::AC_LIBRARY_STAFF_V0` in the composition, and an EXTEND re-renders an act whole
from the design — so a design silent about the actor re-renders six acts with none. Construction
Completeness refused the design at 98.2% and named the missing fact six times. The row states what
was always true and changes no decision this dossier took.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | Ownership, artifacts requiring action | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
