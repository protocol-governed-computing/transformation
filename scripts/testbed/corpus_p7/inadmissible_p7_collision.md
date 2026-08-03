# Design Intent — book_library_mgmt / catalog

**Stage:** 7 — Design Intent
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

> P7 answers HOW. The provisional codes Stage 5 assigned become binding, domain-qualified FQDNs,
> placed in the subdomain Stage 6 chose. Each is assigned once and reused as the exact same string;
> a spelling variant would create a second, permanently misnamed artifact. Gate 1 closes here.

---

## 1. Design Resolution

<!-- register:design_resolution business_language -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Where the catalog's records live | The catalog owns its records exclusively | Two mutable stores and one append-only journal, all declared by the catalog | S6 storage_governance Bibliographic work records |
| How a copy names its work | A copy belongs to exactly one bibliographic work | The copy record carries the work's identity; the work never lists its copies | S5 invariants Each physical copy belongs to exactly one bibliographic work |
| How authorization is checked | Only authorized staff perform catalog operations | A single contract confirms authorization and every workflow calls it first | S6 boundary_rules Authorization is read, never granted |
| How an operation is recorded | Every business operation is traceable and auditable | One contract appends to the journal, called as the last step of every workflow | S6 boundary_rules Store ownership is exclusive |
| How retirement works | A retired record is never offered as current | Retirement marks the record; search excludes marked records rather than deleting them | S6 boundary_rules Retirement does not delete |

## 2. Existing Inventory

<!-- register:existing_inventory -->
| FQDN | Action | Reason | Source Finding |
|------|--------|--------|----------------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE | Holds a catalog record that can be updated in place | S6 ownership Hold a record that can be updated in place |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE | Appends a durable account of a performed operation | S6 ownership Append a durable account of a performed action |

## 3. New Artifacts

<!-- register:new_artifacts -->
| Capability | Family | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|--------|------|---------|-----------------|--------|----------------|
| The authorized staff member performing an operation | AC | book_library_mgmt::AC_LIBRARY_STAFF_V0 | Library Staff Actor | catalog | NEW | S5 provisional_codes AC_LIBRARY_STAFF_V0 |
| A request to register a new book | IN | book_library_mgmt::IN_REGISTER_BOOK_V0 | Request registration of a new book | catalog | NEW | S5 provisional_codes IN_REGISTER_BOOK_V0 |
| A request to register a copy against a work | IN | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | Request registration of a physical copy | catalog | NEW | S5 provisional_codes IN_REGISTER_PHYSICAL_COPY_V0 |
| A request to update a registered work | IN | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Request an update to a registered work | catalog | NEW | S5 provisional_codes IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| A request to retire an obsolete record | IN | book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | Request retirement of an obsolete record | catalog | NEW | S5 provisional_codes IN_RETIRE_CATALOG_RECORD_V0 |
| A request to locate materials | IN | book_library_mgmt::IN_SEARCH_CATALOG_V0 | Request a catalog search | catalog | NEW | S5 provisional_codes IN_SEARCH_CATALOG_V0 |
| A request for the complete details of a book | IN | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | Request the complete details of a book | catalog | NEW | S5 provisional_codes IN_RETRIEVE_BOOK_DETAILS_V0 |
| Registering a book, end to end | WF | book_library_mgmt::WF_REGISTER_BOOK_V0 | Register a book as an authoritative catalog record | catalog | NEW | S5 provisional_codes WF_REGISTER_BOOK_V0 |
| Registering a copy against exactly one work | WF | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | Register a physical copy against exactly one work | catalog | NEW | S5 provisional_codes WF_REGISTER_PHYSICAL_COPY_V0 |
| Updating the description of a registered work | WF | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Update the description of a registered work | catalog | NEW | S5 provisional_codes WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| Retiring a record so it is no longer current | WF | book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | Retire a record so it is no longer current | catalog | NEW | S5 provisional_codes WF_RETIRE_CATALOG_RECORD_V0 |
| Searching the catalog and recording that it happened | WF | book_library_mgmt::WF_SEARCH_CATALOG_V0 | Search the catalog and record that it happened | catalog | NEW | S5 provisional_codes WF_SEARCH_CATALOG_V0 |
| Assembling a work with the copies belonging to it | WF | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | Assemble a work with the copies belonging to it | catalog | NEW | S5 provisional_codes WF_RETRIEVE_BOOK_DETAILS_V0 |
| Confirm the staff member may perform catalog operations | CC | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Confirm the staff member is authorized | catalog | NEW | S5 provisional_codes CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| Record a work as the catalog's authoritative description | CC | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | Register a bibliographic work as an authoritative record | catalog | NEW | S5 provisional_codes CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| Record a copy against exactly one work | CC | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | Register a physical copy against exactly one work | catalog | NEW | S5 provisional_codes CC_REGISTER_PHYSICAL_COPY_V0 |
| Replace the descriptive content of a work's record | CC | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Update the bibliographic information of a registered work | catalog | NEW | S5 provisional_codes CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| Mark a record retired so it is no longer current | CC | book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | Retire a catalog record without deleting it | catalog | NEW | S5 provisional_codes CC_RETIRE_CATALOG_RECORD_V0 |
| Select the current records matching the staff terms | CC | CC_SEARCH_UNQUALIFIED_V0 | Search the catalog for current records | catalog | NEW | S5 provisional_codes CC_SEARCH_CATALOG_V0 |
| Assemble a work's record with the copies belonging to it | CC | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Assemble a work with the copies belonging to it | catalog | NEW | S5 provisional_codes CC_ASSEMBLE_BOOK_DETAILS_V0 |
| Append a durable account of a performed catalog operation | CC | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | Append a performed catalog operation to the journal | catalog | NEW | S5 provisional_codes CC_APPEND_CATALOG_OPERATION_V0 |
| Bindings for every catalog workflow | RB | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | Runtime binding of catalog capability side effects | catalog | NEW | S6 storage_governance Bibliographic work records |
| The stores the catalog owns | STRUCTURE | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | Catalog subdomain storage topology | catalog | NEW | S6 storage_governance Catalog operation journal |
| Interpret an observation as a required condition | CT | book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | Assert that an observed condition holds, refusing when it does not. | catalog | NEW | S6 boundary_rules Authorization is read, never granted |
| The refusal a catalog operation yields when the caller is not entitled | VOCAB | book_library_mgmt::VOCAB_CATALOG_STATES_V0 |  | catalog | NEW | S6 boundary_rules Authorization is read, never granted |

## 4. Runtime Binding Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_BOOK_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_MUTABLE_JSON_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_MUTABLE_JSON_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_MUTABLE_JSON_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_MUTABLE_JSON_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_SEARCH_CATALOG_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_MUTABLE_JSON_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_MUTABLE_JSON_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Bibliographic work records |

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type | Routing | Source Finding |
|----------|------|-----------|---------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::IN_REGISTER_BOOK_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0; NOT_FOUND -> EXIT_REJECTED; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHC_WORK_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; NOT_FOUND -> EXIT_REJECTED; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; WORK_NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0; NOT_FOUND -> EXIT_REJECTED; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0; NOT_FOUND -> EXIT_REJECTED; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::IN_SEARCH_CATALOG_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_SEARCH_CATALOG_V0; NOT_FOUND -> EXIT_REJECTED; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0; NOT_FOUND -> EXIT_REJECTED; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |

## 6. Capability Composition

<!-- register:cc_composition -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | 1 | append_operation | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | CATALOG_OPERATIONS | record | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 1 | read_work_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BIBLIOGRAPHIC_WORKS | key | book_details, result_status | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 2 | read_copies | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | LIST | PHYSICAL_COPIES | filter | copies, result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | 1 | read_authorization | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | CATALOG_STAFF | key | staff_record, result_status | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | DENIED | — |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | 1 | check_existing | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | EXISTS | BIBLIOGRAPHIC_WORKS | key | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | ALREADY_EXISTS | — |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | 2 | write_work_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BIBLIOGRAPHIC_WORKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 1 | confirm_work_registered | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | EXISTS | BIBLIOGRAPHIC_WORKS | key | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | NOT_FOUND | — |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 2 | write_copy_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | PHYSICAL_COPIES | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | 1 | read_work_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BIBLIOGRAPHIC_WORKS | key | result_status | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | 2 | mark_retired | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BIBLIOGRAPHIC_WORKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | 1 | select_current_records | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | LIST | BIBLIOGRAPHIC_WORKS | filter | matching_records, result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 1 | read_work_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BIBLIOGRAPHIC_WORKS | key | result_status | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 2 | write_updated_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BIBLIOGRAPHIC_WORKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |

## 7. Step Bindings

*What each workflow node is handed and where it comes from. `payload.<field>` names a field of the starting intent; a bare literal is a constant this design fixes. Rendering the expression is construction's business — the design states the source.*

<!-- register:step_bindings -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | append_operation | INPUT | record | {'staff_id': '$.inputs.staff_id', 'operation': '$.inputs.operation', 'subject': '$.inputs.subject'} | S7 cc_composition append_operation |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | append_operation | OUTPUT | result_status | result_status | S7 cc_composition append_operation |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_work_record | INPUT | key | inputs.work_id | S7 cc_composition read_work_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_work_record | OUTPUT | book_details | capability_result.value | S7 cc_composition read_work_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_work_record | OUTPUT | result_status | result_status | S7 cc_composition read_work_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_copies | INPUT | filter | {'work_id': '$.inputs.work_id'} | S7 cc_composition read_copies |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_copies | OUTPUT | copies | capability_result.keys | S7 cc_composition read_copies |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_copies | OUTPUT | result_status | result_status | S7 cc_composition read_copies |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | read_authorization | INPUT | key | inputs.staff_id | S7 cc_composition read_authorization |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | read_authorization | OUTPUT | staff_record | capability_result.value | S7 cc_composition read_authorization |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | read_authorization | OUTPUT | result_status | result_status | S7 cc_composition read_authorization |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | require_authorized | INPUT | condition | results.read_authorization.capability_result.value.authorized | S7 cc_composition require_authorized |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | require_authorized | INPUT | expected | True | S7 cc_composition require_authorized |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | require_authorized | OUTPUT | authorized | capability_result.condition_held | S7 cc_composition require_authorized |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | require_authorized | OUTPUT | result_status | result_status | S7 cc_composition require_authorized |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | check_existing | INPUT | key | inputs.work_id | S7 cc_composition check_existing |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | check_existing | OUTPUT | result_status | result_status | S7 cc_composition check_existing |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | require_absent | INPUT | condition | results.check_existing.capability_result.exists | S7 cc_composition require_absent |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | require_absent | INPUT | expected | False | S7 cc_composition require_absent |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | require_absent | OUTPUT | result_status | result_status | S7 cc_composition require_absent |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | write_work_record | INPUT | key | inputs.work_id | S7 cc_composition write_work_record |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | write_work_record | INPUT | value | {'work_id': '$.inputs.work_id', 'bibliographic_information': '$.inputs.bibliographic_information', 'retired': False} | S7 cc_composition write_work_record |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | write_work_record | OUTPUT | result_status | result_status | S7 cc_composition write_work_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | confirm_work_registered | INPUT | key | inputs.work_id | S7 cc_composition confirm_work_registered |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | confirm_work_registered | OUTPUT | result_status | result_status | S7 cc_composition confirm_work_registered |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | require_work_registered | INPUT | condition | results.confirm_work_registered.capability_result.exists | S7 cc_composition require_work_registered |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | require_work_registered | INPUT | expected | True | S7 cc_composition require_work_registered |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | require_work_registered | OUTPUT | result_status | result_status | S7 cc_composition require_work_registered |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | write_copy_record | INPUT | key | inputs.copy_id | S7 cc_composition write_copy_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | write_copy_record | INPUT | value | {'copy_id': '$.inputs.copy_id', 'work_id': '$.inputs.work_id'} | S7 cc_composition write_copy_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | write_copy_record | OUTPUT | result_status | result_status | S7 cc_composition write_copy_record |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | read_work_record | INPUT | key | inputs.work_id | S7 cc_composition read_work_record |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | read_work_record | OUTPUT | result_status | result_status | S7 cc_composition read_work_record |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | mark_retired | INPUT | key | inputs.work_id | S7 cc_composition mark_retired |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | mark_retired | INPUT | value | {'work_id': '$.inputs.work_id', 'retired': True} | S7 cc_composition mark_retired |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | mark_retired | OUTPUT | result_status | result_status | S7 cc_composition mark_retired |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_current_records | INPUT | filter | inputs.search_terms | S7 cc_composition select_current_records |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_current_records | OUTPUT | matching_records | capability_result.keys | S7 cc_composition select_current_records |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_current_records | OUTPUT | result_status | result_status | S7 cc_composition select_current_records |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | read_work_record | INPUT | key | inputs.work_id | S7 cc_composition read_work_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | read_work_record | OUTPUT | result_status | result_status | S7 cc_composition read_work_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | INPUT | key | inputs.work_id | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | INPUT | value | {'work_id': '$.inputs.work_id', 'bibliographic_information': '$.inputs.bibliographic_information', 'retired': False} | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | OUTPUT | result_status | result_status | S7 cc_composition write_updated_record |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | INPUT | work_id | payload.work_id | S7 execution_topology CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | INPUT | bibliographic_information | payload.bibliographic_information | S7 execution_topology CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_BOOK | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | subject | payload.work_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_id | payload.copy_id | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | work_id | payload.work_id | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_PHYSICAL_COPY | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | subject | payload.copy_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | INPUT | work_id | payload.work_id | S7 execution_topology CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | RETIRE_CATALOG_RECORD | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | subject | payload.work_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | work_id | payload.work_id | S7 execution_topology CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | RETRIEVE_BOOK_DETAILS | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | subject | payload.work_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | INPUT | search_terms | payload.search_terms | S7 execution_topology CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | SEARCH_CATALOG | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | subject | CATALOG | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | work_id | payload.work_id | S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | bibliographic_information | payload.bibliographic_information | S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | UPDATE_BIBLIOGRAPHIC_INFORMATION | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | subject | payload.work_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |

---

## 8. Interface Fields

*Every typed field an artifact declares. An intent's inputs, a contract's inputs and outputs, a transform's inputs and outputs and an actor's attributes are one shape, and were unexpressible for one reason: the language could describe a capability but never a field of one.*

<!-- register:interface_fields -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|-----------|-------|------|----------|---------|---------|
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | ATTRIBUTE | staff_id | string | YES | — | staff_id of AC_LIBRARY_STAFF_V0 |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | ATTRIBUTE | authorized | boolean | NO | False | authorized of AC_LIBRARY_STAFF_V0 |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | string | YES | — | staff_id of CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | string | YES | — | operation of CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | subject | string | YES | — | subject of CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | work_id | string | YES | — | work_id of CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | OUTPUT | book_details | object | NO | — | book_details of CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | OUTPUT | copies | array | NO | — | copies of CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_id | string | YES | — | staff_id of CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | OUTPUT | authorized | boolean | NO | — | authorized of CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | INPUT | work_id | string | YES | — | work_id of CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | INPUT | bibliographic_information | object | YES | — | bibliographic_information of CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_id | string | YES | — | copy_id of CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | work_id | string | YES | — | work_id of CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | INPUT | work_id | string | YES | — | work_id of CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | INPUT | search_terms | object | YES | — | search_terms of CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | OUTPUT | matching_records | array | NO | — | matching_records of CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | work_id | string | YES | — | work_id of CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | bibliographic_information | object | YES | — | bibliographic_information of CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | INPUT | condition | boolean | YES | — | The observation being interpreted |
| book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | INPUT | expected | boolean | YES | — | The value the condition must hold, so one transform serves both directions |
| book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | OUTPUT | result_status | string | NO | — | SUCCESS when the condition held; the runtime maps a raise to VIOLATION |
| book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | OUTPUT | condition_held | boolean | YES | — | True whenever this transform returns at all |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | staff_id | string | YES | — | The staff member performing the operation |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | work_id | string | YES | — | work_id of IN_REGISTER_BOOK_V0 |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | bibliographic_information | object | YES | — | bibliographic_information of IN_REGISTER_BOOK_V0 |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | staff_id | string | YES | — | The staff member performing the operation |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_id | string | YES | — | copy_id of IN_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | work_id | string | YES | — | work_id of IN_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | INPUT | staff_id | string | YES | — | The staff member performing the operation |
| book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | INPUT | work_id | string | YES | — | work_id of IN_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | staff_id | string | YES | — | The staff member performing the operation |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | work_id | string | YES | — | work_id of IN_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | staff_id | string | YES | — | The staff member performing the operation |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | search_terms | object | YES | — | search_terms of IN_SEARCH_CATALOG_V0 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | staff_id | string | YES | — | The staff member performing the operation |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | work_id | string | YES | — | work_id of IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | bibliographic_information | object | YES | — | bibliographic_information of IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |

---

## 9. Implementation Bindings

*Where a transform's code lives. A CT is the one family whose artifact points outside the composition, and the module path is declared at design time for the same reason a store path is.*

<!-- register:implementation_bindings -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Source Finding |
|---------|--------|----------|-----------|------|--------|----------------|
| book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_require_condition_v0 | execute | PURE_REQUIRE_CONDITION | atom | ct_pure | S7 new_artifacts CT_PURE_REQUIRE_CONDITION_V0 |

---

## 10. Vocabulary Extensions

*Business status names this change adds. A workflow that routes on DENIED needs DENIED to exist; the routing surface and the vocabulary admitting it are declared together.*

<!-- register:vocabulary_extensions -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|
| book_library_mgmt::VOCAB_CATALOG_STATES_V0 | fb.vocabulary::VOCAB_EXECUTION_STATES_V0 | DENIED | The catalog refuses an operation the caller is not entitled to perform. | S6 boundary_rules Authorization is read, never granted |

---

## 11. Runtime Policies

<!-- register:runtime_policies -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0 | path | {{module_data_root}}/book_library_mgmt/catalog/bibliographic_works.json | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0 | — | — | S6 storage_governance Catalog operation journal |

---

## 12. Artifact Properties

<!-- register:artifact_properties -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | type | person | S6 ownership Confirm the staff member is authorized |
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | layer | DOMAINS | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | parameters | module_data_root | S6 storage_governance Bibliographic work records |

---

## 13. Structure Stores

<!-- register:structure_stores -->
| Store Name | Storage Type | Proposed Path | Used By | Source Finding |
|------------|--------------|---------------|---------|----------------|
| BIBLIOGRAPHIC_WORKS | CS_MUTABLE_JSON_V0 |  | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | S6 storage_governance Bibliographic work records |
| PHYSICAL_COPIES | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/physical_copies.json | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | S6 storage_governance Physical copy records |
| CATALOG_OPERATIONS | CS_APPENDONLY_JSONL_V0 | book_library_mgmt/catalog/catalog_operations.jsonl | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | S6 storage_governance Catalog operation journal |
| CATALOG_STAFF | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/catalog_staff.json | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | S6 storage_governance Bibliographic work records |

## 14. Artifact Summary

<!-- register:artifact_summary -->
| Action | Subdomain | Count | Artifacts |
|--------|-----------|-------|-----------|
| NEW | catalog | 25 | 1 AC, 6 IN, 6 WF, 8 CC, 1 CT, 1 RB, 1 STRUCTURE |
