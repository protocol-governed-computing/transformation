# Stage 7 — Design Intent: book_library_mgmt / catalog

**Stage:** 7 — Design Intent
**CR:** cr_05_catalog
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Every binding names a field the capability declares, read from the pinned baseline
`34c8a0e8a3f2f1b90956edd08d0d878a10347fbc058348049f8348ce0d5b8a95`.

Nothing new is authored. Twenty-six artifacts the catalog already holds are redeclared whole: six
contracts hold their rules and descriptions and refuse on what they find, ten acts stop passing rules
along and check what they record, and ten gates stop requiring what the catalog holds.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Each rule is held by the step that applies it | A rule the caller supplies is a rule the caller can widen | The confirming contract holds the library's authorization rules; the checking contracts hold the book, work and edition descriptions | S4 design_decisions #1 |
| Each check is followed by a rule refusing when it found anything | An incomplete registration is refused | The submission check refuses on both its checks' violations; the book record, the edition record and the correction each gain a rule step requiring none | S4 design_decisions #2 |
| What each registration checks is the record it writes | A check of a supplied copy judges nothing that is written | Each registration act hands its submission check the fields it records | S4 design_decisions #3 |
| The register act records the subject where callers send it | Every present caller sends it inside the book details | The recorded book's subject is bound from the supplied book details | S4 design_decisions #4 |
| A copy's registered state and a correction's state are the catalog's own | A copy is registered as registered; a correction does not change state | The copy contract writes REGISTERED; the correction writes the state it read and checks the corrected record | S4 design_decisions #5 |
| The gates stop requiring what the catalog holds and what no act reads | A gate requiring an unread field refuses a correct request | Every gate drops the rules; the book gate its description; the edition gate its descriptions and supplied details | S4 design_decisions #6 |
| Records made before this change are left as they are | The record is added to and never rewritten | No migration, backfill or repair step is designed | S4 design_decisions #7 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|-----------------------------------------|---------|--------|----------------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | EXTEND | Confirm the staff member may perform catalog operations | It takes its rules from the request. | S6 pps_artifacts_requiring_action #1 |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | EXTEND | Confirms a registration carries what a work and an edition require, before any identity is claimed | It takes its descriptions from the request and refuses nothing its checks find. | S6 pps_artifacts_requiring_action #2 |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | EXTEND | Validates, assembles and writes an edition record against the work it belongs to | It takes its description from the request and ignores what its check finds. | S6 pps_artifacts_requiring_action #3 |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | EXTEND | Assembles the edition record against a resolved work and writes it | It takes its description from the request and ignores what its check finds. | S6 pps_artifacts_requiring_action #4 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | EXTEND | Record a copy against exactly one book | It records the copy in the state the request gives. | S6 pps_artifacts_requiring_action #5 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXTEND | Changes a registered edition's descriptive content and refuses a change that would duplicate another edition | It writes the state the request gives and checks no description. | S6 pps_artifacts_requiring_action #6 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXTEND | The governed sequence that registers a work, its first edition and that edition's first physical copy | It binds the rules from the request. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXTEND | The governed sequence that registers a further edition of a work the library already holds | It binds the rules from the request. | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXTEND | The governed sequence that registers a further physical copy of an edition | It binds the rules from the request. | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | EXTEND | Corrects what the library publishes about a registered book | It binds the rules from the request. | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | EXTEND | The governed sequence that takes a book out of service | It binds the rules from the request. | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | EXTEND | Returning a retired book record to the registered state | It binds the rules from the request. | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | EXTEND | The governed sequence that takes a physical copy out of service | It binds the rules from the request. | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | EXTEND | Returning a retired copy to the registered state | It binds the rules from the request. | S6 pps_artifacts_requiring_action #14 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXTEND | Assembling a book with the copies the library holds of it | It binds the rules from the request. | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXTEND | Searching by subject or title, excluding retired books | It binds the rules from the request. | S6 pps_artifacts_requiring_action #16 |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | EXTEND | A request to register a book together with its first physical copy | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #17 |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | EXTEND | The boundary that admits a request to register a further edition of a work the catalog already holds | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #18 |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | EXTEND | A request to register a further copy against a registered book | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #19 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | EXTEND | A request to change a registered book's description | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #20 |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | EXTEND | A request to retire a book record judged obsolete | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #21 |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | EXTEND | A request to return a retired book record to the registered state | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #22 |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | EXTEND | A request to retire a lost or damaged copy | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #23 |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | EXTEND | A request to return a retired copy to the registered state | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #24 |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | EXTEND | A request for a book's complete details with the copies held | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #25 |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | EXTEND | A request to locate material by subject or by title | It requires the rules the catalog now holds. | S6 pps_artifacts_requiring_action #26 |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #27 |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #28 |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #29 |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #30 |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #31 |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #32 |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #33 |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #34 |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #35 |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #36 |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #37 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | REUSE |  | Run by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #38 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | REUSE |  | Superseded and not in force; named by its successor, unchanged. | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | REUSE |  | Superseded and not in force; named by its successor, unchanged. | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | REUSE |  | Binds every catalog act, unchanged. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | REUSE |  | The actor every catalog act runs as, unchanged. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | REUSE |  | Announced by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | REUSE |  | Announced by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::EV_BOOK_RETIRED_V0 | REUSE |  | Announced by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | REUSE |  | Announced by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | REUSE |  | Announced by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::EV_WORK_REGISTERED_V0 | REUSE |  | Announced by an act this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | REUSE |  | Run by a contract this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #3 |
| book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | REUSE |  | Run by a contract this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #3 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE |  | Run by a contract this change redeclares, unchanged. | S6 cross_subdomain_deps #3 |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | REUSE |  | Run by a contract this change redeclares, unchanged. | S6 pps_artifacts_requiring_action #3 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | REUSE |  | Run by a contract this change redeclares, unchanged. | S6 cross_subdomain_deps #1 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | REUSE |  | Run by a contract this change redeclares, unchanged. | S6 cross_subdomain_deps #2 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE |  | Holds the catalog's records, unchanged. | S6 storage_governance #1 |
| capability_side_effects::CS_REGISTRY_V0 | REUSE |  | Holds the catalog's records, unchanged. | S6 storage_governance #1 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE |  | Holds the catalog's records, unchanged. | S6 storage_governance #1 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|---------------------------------------------------------------|------|---------|-----------------|--------|----------------|

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_BOOK_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #14 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_SEARCH_CATALOG_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 pps_artifacts_requiring_action #16 |

---

## 5. Execution Topology

The routing of every act is unchanged. What changes is what each node is handed, in §7.

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::IN_REGISTER_BOOK_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; ALREADY_EXISTS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_BOOK_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_COMPLETED |  | EXIT_SUCCESS | emit ['book_library_mgmt::EV_WORK_REGISTERED_V0', 'book_library_mgmt::EV_BOOK_REGISTERED_V0', 'book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0'] | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_RESOLVE_WORK_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXIT_COMPLETED |  | EXIT_SUCCESS | emit book_library_mgmt::EV_BOOK_REGISTERED_V0 | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXIT_COMPLETED |  | EXIT_SUCCESS | emit book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | EXIT_COMPLETED |  | EXIT_SUCCESS | emit book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | EXIT_COMPLETED |  | EXIT_SUCCESS | emit book_library_mgmt::EV_BOOK_RETIRED_V0 | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | EXIT_COMPLETED |  | EXIT | — | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #12 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | EXIT_COMPLETED |  | EXIT_SUCCESS | emit book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | EXIT_COMPLETED |  | EXIT | — | S6 pps_artifacts_requiring_action #14 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #14 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXIT_COMPLETED |  | EXIT | — | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #15 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::IN_SEARCH_CATALOG_V0 |  | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #16 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #16 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 |  | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #16 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |  | CC | SUCCESS -> book_library_mgmt::CC_SEARCH_CATALOG_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #16 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXIT_COMPLETED |  | EXIT | — | S6 pps_artifacts_requiring_action #16 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #16 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | 1 | confirm_authorization | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | parameters, rules | is_authorized | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=parameters, rules=rules; out: valid=is_authorized |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | 1 | validate_book_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | record, schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=record, schema=schema; out: violations=violations |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | 2 | validate_work_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | record, schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=record, schema=schema; out: violations=violations |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | 3 | require_submission_complete | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | parameters, rules | valid | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=parameters, rules=rules; out: valid=valid |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 1 | form_work_key | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | CT | FORM_WORK_IDENTITY_KEY | — | title, author | work_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author; out: work_key=work_key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 2 | validate_book_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | record, schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=record, schema=schema; out: violations=violations |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 3 | refuse_incomplete_record | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | parameters, rules | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=parameters, rules=rules; out: valid=valid |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 4 | assemble_book_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | book_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 5 | write_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BOOKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=key, value=value; out: result_status=result_status |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | 1 | validate_edition_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | record, schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=record, schema=schema; out: violations=violations |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | 2 | refuse_incomplete_record | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | parameters, rules | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=parameters, rules=rules; out: valid=valid |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | 3 | assemble_edition_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | edition_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | 4 | write_edition_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BOOKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=key, value=value; out: result_status=result_status |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 1 | read_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BOOKS | key | book_record, result_status | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=key; out: value=book_record, result_status=result_status |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 2 | assemble_copy_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | copy_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=copy_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 3 | write_copy_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | PHYSICAL_COPIES | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=key, value=value; out: result_status=result_status |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 1 | read_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BOOKS | key | book_record, result_status | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=key; out: value=book_record, result_status=result_status |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 2 | form_updated_identity_key | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | CT | FORM_BOOK_IDENTITY_KEY | — | title, author, publication_year | updated_identity_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author, publication_year=publication_year; out: identity_key=updated_identity_key |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 3 | compare_identity | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | CT | COMPARE_EQUAL | — | left, right | identity_unchanged | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: left=left, right=right; out: is_equal=identity_unchanged |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 4 | require_identity_unchanged | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | parameters, rules | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=parameters, rules=rules; out: valid=valid |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 5 | assemble_updated_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | updated_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 6 | check_corrected_record | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | record, schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=record, schema=schema; out: violations=violations |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 7 | refuse_incomplete_correction | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | parameters, rules | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=parameters, rules=rules; out: valid=valid |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 8 | write_updated_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BOOKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=key, value=value; out: result_status=result_status |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_fields | {'title': '$.payload.title', 'author': '$.payload.author'} | S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | {'title': '$.payload.title', 'author': '$.payload.author', 'publication_year': '$.payload.publication_year', 'subject': '$.payload.book_fields.subject'} | S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | barcode | payload.barcode | S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | title | payload.title | S7 execution_topology book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | author | payload.author | S7 execution_topology book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | work_fields | {'title': '$.payload.title', 'author': '$.payload.author'} | S7 execution_topology book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | title | payload.title | S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | author | payload.author | S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | publication_year | payload.publication_year | S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | INPUT | barcode | payload.barcode | S7 execution_topology book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_fields | {'title': '$.payload.title', 'author': '$.payload.author', 'publication_year': '$.payload.publication_year', 'subject': '$.payload.book_fields.subject', 'state': 'REGISTERED'} | S7 execution_topology book_library_mgmt::CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology book_library_mgmt::CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | payload.copy_fields | S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_BOOK | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_BOOK', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.title'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | {'title': '$.payload.title', 'author': '$.payload.author', 'publication_year': '$.payload.publication_year', 'subject': '$.payload.subject'} | S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_fields | {'title': '$.payload.title', 'author': '$.payload.author'} | S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | INPUT | title | payload.title | S7 execution_topology book_library_mgmt::CC_RESOLVE_WORK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | INPUT | author | payload.author | S7 execution_topology book_library_mgmt::CC_RESOLVE_WORK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | title | payload.title | S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | author | payload.author | S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | publication_year | payload.publication_year | S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_fields | {'identity_key': '$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key', 'title': '$.payload.title', 'author': '$.payload.author', 'publication_year': '$.payload.publication_year', 'subject': '$.payload.subject', 'state': 'REGISTERED', 'work_key': '$.results.CC_RESOLVE_WORK_V0.work_key'} | S7 execution_topology book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_ADDITIONAL_EDITION | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_ADDITIONAL_EDITION', 'staff_id': '$.payload.staff_id', 'subject': '$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | INPUT | barcode | payload.barcode | S7 execution_topology book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | payload.copy_fields | S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_PHYSICAL_COPY | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_PHYSICAL_COPY', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.barcode'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | updated_fields | payload.updated_fields | S7 execution_topology book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | UPDATE_BIBLIOGRAPHIC_INFORMATION | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'UPDATE_BIBLIOGRAPHIC_INFORMATION', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | RETIRE_BOOK_RECORD | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'RETIRE_BOOK_RECORD', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REINSTATE_BOOK_RECORD | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REINSTATE_BOOK_RECORD', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | RETIRE_PHYSICAL_COPY | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'RETIRE_PHYSICAL_COPY', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.barcode'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REINSTATE_PHYSICAL_COPY | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REINSTATE_PHYSICAL_COPY', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.barcode'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | copy_criteria | {'identity_key': '$.payload.identity_key'} | S7 execution_topology book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | RETRIEVE_BOOK_DETAILS | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'RETRIEVE_BOOK_DETAILS', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | INPUT | search_criteria | payload.search_criteria | S7 execution_topology book_library_mgmt::CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | SEARCH_CATALOG | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'SEARCH_CATALOG', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.search_criteria'} | S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | confirm_authorization | INPUT | parameters | inputs.staff_credentials | S7 cc_composition confirm_authorization |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | confirm_authorization | INPUT | rules | [{'field': 'staff_id', 'op': 'not_null'}, {'field': 'authorized', 'op': 'eq', 'value': True}] | S7 cc_composition confirm_authorization |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | confirm_authorization | OUTPUT | is_authorized | capability_result.valid | S7 cc_composition confirm_authorization |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | INPUT | record | inputs.book_fields | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | INPUT | schema | {'title': {'required': True, 'type': 'string'}, 'author': {'required': True, 'type': 'string'}, 'publication_year': {'required': True, 'type': 'integer'}, 'subject': {'required': True, 'type': 'array'}} | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_work_fields | INPUT | record | inputs.work_fields | S7 cc_composition validate_work_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_work_fields | INPUT | schema | {'title': {'required': True, 'type': 'string'}, 'author': {'required': True, 'type': 'string'}} | S7 cc_composition validate_work_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_work_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_work_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | INPUT | parameters | {'barcode': '$.inputs.barcode', 'subject': '$.inputs.book_fields.subject', 'book_violations': '$.results.validate_book_fields.violations', 'work_violations': '$.results.validate_work_fields.violations'} | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | INPUT | rules | [{'field': 'barcode', 'op': 'neq', 'value': ''}, {'field': 'subject', 'op': 'neq', 'value': []}, {'field': 'book_violations', 'op': 'eq', 'value': []}, {'field': 'work_violations', 'op': 'eq', 'value': []}] | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | OUTPUT | valid | capability_result.valid | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | form_work_key | INPUT | title | inputs.book_fields.title | S7 cc_composition form_work_key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | form_work_key | INPUT | author | inputs.book_fields.author | S7 cc_composition form_work_key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | form_work_key | OUTPUT | work_key | capability_result.work_key | S7 cc_composition form_work_key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | INPUT | record | inputs.book_fields | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | INPUT | schema | {'title': {'required': True, 'type': 'string'}, 'author': {'required': True, 'type': 'string'}, 'publication_year': {'required': True, 'type': 'integer'}, 'subject': {'required': True, 'type': 'array'}} | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | refuse_incomplete_record | INPUT | parameters | {'violations': '$.results.validate_book_fields.violations'} | S7 cc_composition refuse_incomplete_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | refuse_incomplete_record | INPUT | rules | [{'field': 'violations', 'op': 'eq', 'value': []}] | S7 cc_composition refuse_incomplete_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | refuse_incomplete_record | OUTPUT | valid | capability_result.valid | S7 cc_composition refuse_incomplete_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | assemble_book_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'title': '$.inputs.book_fields.title', 'author': '$.inputs.book_fields.author', 'publication_year': '$.inputs.book_fields.publication_year', 'subject': '$.inputs.book_fields.subject', 'state': '$.inputs.book_fields.state', 'work_key': '$.results.form_work_key.work_key'} | S7 cc_composition assemble_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | assemble_book_record | OUTPUT | book_record | capability_result.record | S7 cc_composition assemble_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | INPUT | key | inputs.identity_key | S7 cc_composition write_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | INPUT | value | results.assemble_book_record.book_record | S7 cc_composition write_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | OUTPUT | result_status | result_status | S7 cc_composition write_book_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | validate_edition_fields | INPUT | record | inputs.edition_fields | S7 cc_composition validate_edition_fields |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | validate_edition_fields | INPUT | schema | {'title': {'required': True, 'type': 'string'}, 'author': {'required': True, 'type': 'string'}, 'publication_year': {'required': True, 'type': 'integer'}, 'subject': {'required': True, 'type': 'array'}} | S7 cc_composition validate_edition_fields |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | validate_edition_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_edition_fields |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | refuse_incomplete_record | INPUT | parameters | {'violations': '$.results.validate_edition_fields.violations'} | S7 cc_composition refuse_incomplete_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | refuse_incomplete_record | INPUT | rules | [{'field': 'violations', 'op': 'eq', 'value': []}] | S7 cc_composition refuse_incomplete_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | refuse_incomplete_record | OUTPUT | valid | capability_result.valid | S7 cc_composition refuse_incomplete_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | assemble_edition_record | INPUT | fields | inputs.edition_fields | S7 cc_composition assemble_edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | assemble_edition_record | OUTPUT | edition_record | capability_result.record | S7 cc_composition assemble_edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | write_edition_record | INPUT | key | inputs.identity_key | S7 cc_composition write_edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | write_edition_record | INPUT | value | results.assemble_edition_record.edition_record | S7 cc_composition write_edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | write_edition_record | OUTPUT | result_status | result_status | S7 cc_composition write_edition_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | read_book_record | INPUT | key | inputs.identity_key | S7 cc_composition read_book_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | read_book_record | OUTPUT | book_record | capability_result.value | S7 cc_composition read_book_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | read_book_record | OUTPUT | result_status | result_status | S7 cc_composition read_book_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | assemble_copy_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'barcode': '$.inputs.barcode', 'state': 'REGISTERED'} | S7 cc_composition assemble_copy_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | assemble_copy_record | OUTPUT | copy_record | capability_result.record | S7 cc_composition assemble_copy_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | write_copy_record | INPUT | key | inputs.barcode | S7 cc_composition write_copy_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | write_copy_record | INPUT | value | results.assemble_copy_record.copy_record | S7 cc_composition write_copy_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | write_copy_record | OUTPUT | result_status | result_status | S7 cc_composition write_copy_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | read_book_record | INPUT | key | inputs.identity_key | S7 cc_composition read_book_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | read_book_record | OUTPUT | book_record | capability_result.value | S7 cc_composition read_book_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | read_book_record | OUTPUT | result_status | result_status | S7 cc_composition read_book_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | form_updated_identity_key | INPUT | title | inputs.updated_fields.title | S7 cc_composition form_updated_identity_key |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | form_updated_identity_key | INPUT | author | inputs.updated_fields.author | S7 cc_composition form_updated_identity_key |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | form_updated_identity_key | INPUT | publication_year | inputs.updated_fields.publication_year | S7 cc_composition form_updated_identity_key |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | form_updated_identity_key | OUTPUT | updated_identity_key | capability_result.identity_key | S7 cc_composition form_updated_identity_key |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | compare_identity | INPUT | left | inputs.identity_key | S7 cc_composition compare_identity |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | compare_identity | INPUT | right | results.form_updated_identity_key.updated_identity_key | S7 cc_composition compare_identity |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | compare_identity | OUTPUT | identity_unchanged | capability_result.is_equal | S7 cc_composition compare_identity |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | require_identity_unchanged | INPUT | parameters | {'identity_unchanged': '$.results.compare_identity.identity_unchanged'} | S7 cc_composition require_identity_unchanged |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | require_identity_unchanged | INPUT | rules | [{'field': 'identity_unchanged', 'op': 'eq', 'value': True}] | S7 cc_composition require_identity_unchanged |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | require_identity_unchanged | OUTPUT | valid | capability_result.valid | S7 cc_composition require_identity_unchanged |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | assemble_updated_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'title': '$.inputs.updated_fields.title', 'author': '$.inputs.updated_fields.author', 'publication_year': '$.inputs.updated_fields.publication_year', 'subject': '$.inputs.updated_fields.subject', 'state': '$.results.read_book_record.book_record.state', 'work_key': '$.results.read_book_record.book_record.work_key'} | S7 cc_composition assemble_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | assemble_updated_record | OUTPUT | updated_record | capability_result.record | S7 cc_composition assemble_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | check_corrected_record | INPUT | record | results.assemble_updated_record.updated_record | S7 cc_composition check_corrected_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | check_corrected_record | INPUT | schema | {'title': {'required': True, 'type': 'string'}, 'author': {'required': True, 'type': 'string'}, 'publication_year': {'required': True, 'type': 'integer'}, 'subject': {'required': True, 'type': 'array'}} | S7 cc_composition check_corrected_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | check_corrected_record | OUTPUT | violations | capability_result.violations | S7 cc_composition check_corrected_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | refuse_incomplete_correction | INPUT | parameters | {'violations': '$.results.check_corrected_record.violations', 'subject': '$.results.assemble_updated_record.updated_record.subject'} | S7 cc_composition refuse_incomplete_correction |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | refuse_incomplete_correction | INPUT | rules | [{'field': 'violations', 'op': 'eq', 'value': []}, {'field': 'subject', 'op': 'neq', 'value': []}] | S7 cc_composition refuse_incomplete_correction |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | refuse_incomplete_correction | OUTPUT | valid | capability_result.valid | S7 cc_composition refuse_incomplete_correction |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | INPUT | key | inputs.identity_key | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | INPUT | value | results.assemble_updated_record.updated_record | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | OUTPUT | result_status | result_status | S7 cc_composition write_updated_record |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | title | string | YES |  | title |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | author | string | YES |  | author |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | publication_year | integer | YES |  | publication year |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | book_fields | object | YES |  | book fields |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | barcode | string | YES |  | barcode |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | copy_fields | object | YES |  | copy fields |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | title | string | YES |  | title |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | author | string | YES |  | author |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | publication_year | integer | YES |  | publication year |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | subject | array | YES |  | subject |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | barcode |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | object | YES |  | copy fields |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | INPUT | updated_fields | object | YES |  | updated fields |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | barcode |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | barcode |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | search_criteria | object | YES |  | search criteria |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | staff_id | string | YES |  | staff id |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | object | YES |  | staff credentials |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | OUTPUT | is_authorized | boolean | YES |  | is authorized |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_fields | object | YES |  | work fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | object | YES |  | book fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | barcode | string | NO |  | barcode |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | OUTPUT | valid | boolean | YES |  | valid |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_fields | object | YES |  | book fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | OUTPUT | book_record | object | YES |  | book record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_fields | object | YES |  | edition fields |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | OUTPUT | edition_record | object | YES |  | edition record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | barcode |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | object | YES |  | copy fields |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | OUTPUT | book_record | object | YES |  | book record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | identity_key | string | YES |  | identity key |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | updated_fields | object | YES |  | updated fields |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | OUTPUT | book_record | object | YES |  | book record |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_WORK_REGISTERED_V0 | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BOOK_REGISTERED_V0 | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | S6 pps_artifacts_requiring_action #7 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BOOK_REGISTERED_V0 | S6 pps_artifacts_requiring_action #8 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | S6 pps_artifacts_requiring_action #9 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | supersedes | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | S6 pps_artifacts_requiring_action #10 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_BOOK_RETIRED_V0 | S6 pps_artifacts_requiring_action #11 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | emit.EXIT_COMPLETED | book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | S6 pps_artifacts_requiring_action #13 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | supersedes | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | S6 pps_artifacts_requiring_action #20 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | catalog | 26 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::IN_REGISTER_BOOK_V0, book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0, book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::IN_SEARCH_CATALOG_V0 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Any catalog operation | The person performing it is not authorized staff | book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #1 |
| Registering a book | It lacks what the library says a book must contain | book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | VIOLATION | S0 operation_refusals #2 |
| Registering a further edition | It lacks what the library says an edition must contain | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | VIOLATION | S0 operation_refusals #3 |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|

---

## 20. Refusal — Governance-Surface Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|

---

## 21. Molecule Steps

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---------|------|-----------------------------|--------|------|----------|-------|----------------|

---

## 22. Molecule Step Bindings

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---------|------|-----------------------------|-------|----------|----------------|

---

## 23. Test Cases

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---------|------|---------------------------------------|----------------|

---

## 24. Test Case Values

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---------|------|------------------------------------------|-------|-------|----------------|

---

## 25. Withdrawn Facts

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|----------|------|--------|----------------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | .core.inputs.authorization_rules | The contract holds the library's rules itself. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules | The confirming contract no longer takes the rules. | S6 boundary_rules #1 |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | .core.inputs.authorization_rules | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | .core.inputs.book_schema | The contract holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | .core.inputs.work_schema | The contract holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | .core.inputs.book_schema | The contract holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | .core.inputs.edition_schema | The contract holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.book_schema | The check holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.work_schema | The check holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | .core.nodes.CC_REGISTER_BOOK_V0.inputs.book_schema | The contract holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | .core.inputs.book_schema | The gate no longer requires what the catalog holds. | S6 boundary_rules #6 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.book_schema | The check holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.work_schema | The check holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | .core.nodes.CC_REGISTER_ADDITIONAL_EDITION_V0.inputs.edition_schema | The contract holds its description itself. | S6 boundary_rules #1 |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | .core.inputs.edition_schema | The gate no longer requires what the catalog holds or no act reads. | S6 boundary_rules #6 |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | .core.inputs.work_schema | The gate no longer requires what the catalog holds or no act reads. | S6 boundary_rules #6 |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | .core.inputs.edition_fields | The gate no longer requires what the catalog holds or no act reads. | S6 boundary_rules #6 |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | .core.inputs.work_fields | The gate no longer requires what the catalog holds or no act reads. | S6 boundary_rules #6 |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
