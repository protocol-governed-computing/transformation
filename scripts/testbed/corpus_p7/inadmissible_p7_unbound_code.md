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
| Capability | Family | Code | Owner Subdomain | Status | Source Finding |
|------------|--------|------|-----------------|--------|----------------|
| A request to register a new book | IN | book_library_mgmt::IN_REGISTER_BOOK_V0 | catalog | NEW | S5 provisional_codes IN_REGISTER_BOOK_V0 |
| A request to register a copy against a work | IN | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | catalog | NEW | S5 provisional_codes IN_REGISTER_PHYSICAL_COPY_V0 |
| A request to update a registered work | IN | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog | NEW | S5 provisional_codes IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| A request to retire an obsolete record | IN | book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | catalog | NEW | S5 provisional_codes IN_RETIRE_CATALOG_RECORD_V0 |
| A request to locate materials | IN | book_library_mgmt::IN_SEARCH_CATALOG_V0 | catalog | NEW | S5 provisional_codes IN_SEARCH_CATALOG_V0 |
| A request for the complete details of a book | IN | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | catalog | NEW | S5 provisional_codes IN_RETRIEVE_BOOK_DETAILS_V0 |
| Registering a book, end to end | WF | book_library_mgmt::WF_REGISTER_BOOK_V0 | catalog | NEW | S5 provisional_codes WF_REGISTER_BOOK_V0 |
| Registering a copy against exactly one work | WF | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | catalog | NEW | S5 provisional_codes WF_REGISTER_PHYSICAL_COPY_V0 |
| Updating the description of a registered work | WF | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog | NEW | S5 provisional_codes WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| Retiring a record so it is no longer current | WF | book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | catalog | NEW | S5 provisional_codes WF_RETIRE_CATALOG_RECORD_V0 |
| Searching the catalog and recording that it happened | WF | book_library_mgmt::WF_SEARCH_CATALOG_V0 | catalog | NEW | S5 provisional_codes WF_SEARCH_CATALOG_V0 |
| Assembling a work with the copies belonging to it | WF | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | catalog | NEW | S5 provisional_codes WF_RETRIEVE_BOOK_DETAILS_V0 |
| Confirm the staff member may perform catalog operations | CC | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | catalog | NEW | S5 provisional_codes CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| Record a work as the catalog's authoritative description | CC | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | catalog | NEW | S5 provisional_codes CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| Record a copy against exactly one work | CC | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | catalog | NEW | S5 provisional_codes CC_REGISTER_PHYSICAL_COPY_V0 |
| Replace the descriptive content of a work's record | CC | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog | NEW | S5 provisional_codes CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| Mark a record retired so it is no longer current | CC | book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | catalog | NEW | S5 provisional_codes CC_RETIRE_CATALOG_RECORD_V0 |
| Select the current records matching the staff terms | CC | book_library_mgmt::CC_SEARCH_CATALOG_V0 | catalog | NEW | S5 provisional_codes CC_SEARCH_CATALOG_V0 |
| Assemble a work's record with the copies belonging to it | CC | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | catalog | NEW | S5 provisional_codes CC_ASSEMBLE_BOOK_DETAILS_V0 |
| Append a durable account of a performed catalog operation | CC | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | catalog | NEW | S5 provisional_codes CC_APPEND_CATALOG_OPERATION_V0 |
| Bindings for every catalog workflow | RB | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | catalog | NEW | S6 storage_governance Bibliographic work records |
| The stores the catalog owns | STRUCTURE | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | catalog | NEW | S6 storage_governance Catalog operation journal |
| Interpret an observation as a required condition | CT | book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | catalog | NEW | S6 boundary_rules Authorization is read, never granted |
| The refusal a catalog operation yields when the caller is not entitled | VOCAB | book_library_mgmt::VOCAB_CATALOG_STATES_V0 | catalog | NEW | S6 boundary_rules Authorization is read, never granted |

## 4. Runtime Binding Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_BOOK_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Bibliographic work records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Physical copy records |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_SEARCH_CATALOG_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance Catalog operation journal |

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type | Routing | Source Finding |
|----------|------|-----------|---------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::IN_REGISTER_BOOK_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; WORK_NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::IN_SEARCH_CATALOG_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_SEARCH_CATALOG_V0; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0; DENIED -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXIT_COMPLETED | EXIT | — | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |

## 6. Capability Composition

<!-- register:cc_composition -->
| CC Code | Step | Capability | Kind | Operation | Consumes | Produces | Interpreted By | Semantic Status | Interface |
|---------|------|------------|------|-----------|----------|----------|----------------|-----------------|-----------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | EXISTS | staff_identity | authorized | book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | DENIED | the staff member is entitled to act |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | work_identity | existing_work | book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | ALREADY_EXISTS | work_identity to existing_work |
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | 2 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | work_identity, bibliographic_information | work_record | — | SUCCESS | the authoritative record for the work |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | work_identity | existing_work | book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0 | NOT_FOUND | confirms the work is registered |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 2 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | copy_identity, work_identity | copy_record | — | SUCCESS | the authoritative record for the copy |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | LIST | search_terms | matching_records | — | SUCCESS | current records matching the terms |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | 1 | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | staff_identity, operation_performed | operation_record | — | SUCCESS | the durable account of the operation |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | work_identity | existing_work | — | NOT_FOUND | confirms the work is registered |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 2 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | work_identity, bibliographic_information | work_record | — | SUCCESS | the updated authoritative record |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | work_identity | existing_work | — | NOT_FOUND | confirms the record exists to retire |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | 2 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | work_identity, retirement_state | retired_record | — | SUCCESS | the record marked no longer current |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | work_identity | book_details | — | SUCCESS | the work's authoritative record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 2 | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | LIST | work_identity | copies | — | SUCCESS | the copies registered against the work |

## 7. Node Input Bindings

*What each workflow node is handed and where it comes from. `payload.<field>` names a field of the starting intent; a bare literal is a constant this design fixes. Rendering the expression is construction's business — the design states the source.*

<!-- register:node_bindings -->
| Workflow | Node | Field | Bound To | Source Finding |
|----------|------|-------|----------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | work_id | payload.work_id | S7 execution_topology CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | bibliographic_information | payload.bibliographic_information | S7 execution_topology CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | operation | REGISTER_BOOK | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | subject | payload.work_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | copy_id | payload.copy_id | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | work_id | payload.work_id | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | operation | REGISTER_PHYSICAL_COPY | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | subject | payload.copy_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | work_id | payload.work_id | S7 execution_topology CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | operation | RETIRE_CATALOG_RECORD | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETIRE_CATALOG_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | subject | payload.work_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | work_id | payload.work_id | S7 execution_topology CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | operation | RETRIEVE_BOOK_DETAILS | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | subject | payload.work_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | search_terms | payload.search_terms | S7 execution_topology CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | operation | SEARCH_CATALOG | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | subject | CATALOG | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | staff_id | payload.staff_id | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | work_id | payload.work_id | S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | bibliographic_information | payload.bibliographic_information | S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | operation | UPDATE_BIBLIOGRAPHIC_INFORMATION | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | subject | payload.work_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |

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
| book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | OUTPUT | work_record | object | NO | — | work_record of CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_id | string | YES | — | copy_id of CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | work_id | string | YES | — | work_id of CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | OUTPUT | copy_record | object | NO | — | copy_record of CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | INPUT | work_id | string | YES | — | work_id of CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0 | OUTPUT | retired_record | object | NO | — | retired_record of CC_RETIRE_CATALOG_RECORD_V0 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | INPUT | search_terms | object | YES | — | search_terms of CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | OUTPUT | matching_records | array | NO | — | matching_records of CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | work_id | string | YES | — | work_id of CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | bibliographic_information | object | YES | — | bibliographic_information of CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | OUTPUT | result_status | string | NO | — | result_status of CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | OUTPUT | work_record | object | NO | — | work_record of CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
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

## 11. Structure Stores

<!-- register:structure_stores -->
| Store Name | Storage Type | Proposed Path | Used By | Source Finding |
|------------|--------------|---------------|---------|----------------|
| BIBLIOGRAPHIC_WORKS | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/bibliographic_works.json | book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | S6 storage_governance Bibliographic work records |
| PHYSICAL_COPIES | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/physical_copies.json | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | S6 storage_governance Physical copy records |
| CATALOG_OPERATIONS | CS_APPENDONLY_JSONL_V0 | book_library_mgmt/catalog/catalog_operations.jsonl | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | S6 storage_governance Catalog operation journal |

## 12. Artifact Summary

<!-- register:artifact_summary -->
| Action | Subdomain | Count | Artifacts |
|--------|-----------|-------|-----------|
| NEW | catalog | 25 | 1 AC, 6 IN, 6 WF, 8 CC, 1 CT, 1 RB, 1 STRUCTURE |
