# Stage 7 — Design Intent: book_library_mgmt / catalog

**Stage:** 7 — Design Intent
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Every binding names a field the capability declares, read from the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d`.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The catalog is a new subdomain | Nothing in the composition manages a library catalog | A new subdomain namespace with its own actor, stores, bindings and operations | S4 design_decisions #1 |
| The catalog owns its audit trail | A subdomain owns its stores exclusively | An own append-only store and an own composed append step, reusing only the append mechanism | S4 design_decisions #2 |
| Uniqueness by composite key | Title, author and publication year identify a book | A pure transform forms one key from the three attributes; the registry claims it atomically, and ALREADY_EXISTS is the duplicate refusal | S4 design_decisions #3 |
| State is data on the record | Retirement is reversible | Both record stores hold state as a field; retirement and reinstatement are writes, never moves between stores | S4 design_decisions #4 |
| Reads are audited, raise no event | Nothing reacts to a read | Search and retrieval append to the trail and declare no EV artifact | S4 design_decisions #5 |
| Registration includes the first copy | A book is never registered without a copy | One workflow claims both identities and writes both records before appending | S4 design_decisions #6 |
| Retirement never cascades | Staff retire each record explicitly | Four separate workflows, each writing one record and leaving the other alone | S4 design_decisions #7 |
| Authorization is read, never granted | Deciding who is authorized belongs to the staff function | One contract validates supplied credentials against supplied rules; no store of authorized staff is declared | S4 design_decisions #8 |
| Subject is free text | The business chose free text | No value-set validation is bound; search criteria match on the subject as typed | S4 design_decisions #9 |
| Search excludes retired, retrieval serves them | A retired record stays auditable and retrievable | Search filters on state; retrieval reads by key without a state criterion | S4 design_decisions #10 |
| The record mechanism is extended, not duplicated | The implementation already returned records | One additive operation on the platform side effect; the catalog holds no second copy of a book | S4 design_decisions #11 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | REVIEW | Writes, reads, selects, lists, updates in place and deletes durable records | Extended with an operation that publishes the records themselves, so a search can select among them by content; the implementation behind it already returned them. | S6 pps_artifacts_requiring_action capability_side_effects::CS_MUTABLE_JSON_V0 |
| capability_side_effects::CS_REGISTRY_V0 | REUSE |  | Register-if-absent gives the atomic claim duplicate prevention needs, on a key the catalog forms. | S6 ownership Claim a value once so a second claim on it fails |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE |  | Appends an entry to a trail that cannot be amended. | S6 ownership Append an entry to a trail that cannot be amended |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE |  | Assembles a durable record from supplied values. | S6 ownership Assemble a durable record from supplied values |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | REUSE |  | Confirms a record carries the fields its contract declares. | S6 ownership Confirm a record carries the fields its contract declares |
| capability_transforms::CT_PURE_FILTER_RECORDS_V0 | REUSE |  | Selects the records matching stated criteria, and interprets a read of the store into a decision. | S6 ownership Select the records matching stated criteria |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | REUSE |  | Confirms supplied parameters satisfy declared rules, and interprets a read into a decision. | S6 ownership Confirm supplied parameters satisfy declared rules |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | REUSE |  | Decides whether the identity an update would produce is the identity the book already has. | S6 ownership Confirm supplied parameters satisfy declared rules |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| The authorized staff member who performs a catalog operation | AC | book_library_mgmt::AC_LIBRARY_STAFF_V0 | The actor whose authorization every catalog operation binds | catalog | NEW | S5 provisional_codes AC_LIBRARY_STAFF_V0 |
| A request to register a book together with its first physical copy | IN | book_library_mgmt::IN_REGISTER_BOOK_V0 | A request to register a book together with its first physical copy | catalog | NEW | S5 provisional_codes IN_REGISTER_BOOK_V0 |
| A request to register a further copy against a registered book | IN | book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | A request to register a further copy against a registered book | catalog | NEW | S5 provisional_codes IN_REGISTER_PHYSICAL_COPY_V0 |
| A request to change a registered book's description | IN | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | A request to change a registered book's description | catalog | NEW | S5 provisional_codes IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| A request to retire a book record judged obsolete | IN | book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | A request to retire a book record judged obsolete | catalog | NEW | S5 provisional_codes IN_RETIRE_BOOK_RECORD_V0 |
| A request to retire a lost or damaged copy | IN | book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | A request to retire a lost or damaged copy | catalog | NEW | S5 provisional_codes IN_RETIRE_PHYSICAL_COPY_V0 |
| A request to return a retired book record to the registered state | IN | book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | A request to return a retired book record to the registered state | catalog | NEW | S5 provisional_codes IN_REINSTATE_BOOK_RECORD_V0 |
| A request to return a retired copy to the registered state | IN | book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | A request to return a retired copy to the registered state | catalog | NEW | S5 provisional_codes IN_REINSTATE_PHYSICAL_COPY_V0 |
| A request to locate material by subject or by title | IN | book_library_mgmt::IN_SEARCH_CATALOG_V0 | A request to locate material by subject or by title | catalog | NEW | S5 provisional_codes IN_SEARCH_CATALOG_V0 |
| A request for a book's complete details with the copies held | IN | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | A request for a book's complete details with the copies held | catalog | NEW | S5 provisional_codes IN_RETRIEVE_BOOK_DETAILS_V0 |
| Registering a book and its first copy, end to end | WF | book_library_mgmt::WF_REGISTER_BOOK_V0 | Registering a book and its first copy, end to end | catalog | NEW | S5 provisional_codes WF_REGISTER_BOOK_V0 |
| Registering a further copy against a registered book | WF | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | Registering a further copy against a registered book | catalog | NEW | S5 provisional_codes WF_REGISTER_PHYSICAL_COPY_V0 |
| Changing a book's description without making it a duplicate | WF | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Changing a book's description without making it a duplicate | catalog | NEW | S5 provisional_codes WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| Retiring a book record, leaving its copies untouched | WF | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | Retiring a book record, leaving its copies untouched | catalog | NEW | S5 provisional_codes WF_RETIRE_BOOK_RECORD_V0 |
| Retiring a copy, leaving the book record untouched | WF | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | Retiring a copy, leaving the book record untouched | catalog | NEW | S5 provisional_codes WF_RETIRE_PHYSICAL_COPY_V0 |
| Returning a retired book record to the registered state | WF | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | Returning a retired book record to the registered state | catalog | NEW | S5 provisional_codes WF_REINSTATE_BOOK_RECORD_V0 |
| Returning a retired copy to the registered state | WF | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | Returning a retired copy to the registered state | catalog | NEW | S5 provisional_codes WF_REINSTATE_PHYSICAL_COPY_V0 |
| Searching by subject or title, excluding retired books | WF | book_library_mgmt::WF_SEARCH_CATALOG_V0 | Searching by subject or title, excluding retired books | catalog | NEW | S5 provisional_codes WF_SEARCH_CATALOG_V0 |
| Assembling a book with the copies the library holds of it | WF | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | Assembling a book with the copies the library holds of it | catalog | NEW | S5 provisional_codes WF_RETRIEVE_BOOK_DETAILS_V0 |
| Confirm the staff member may perform catalog operations | CC | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Confirm the staff member may perform catalog operations | catalog | NEW | S5 provisional_codes CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| Judge a registration admissible before anything is claimed or written | CC | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | Validate a book submission is complete | catalog | NEW | S5 provisional_codes CC_REGISTER_BOOK_V0 |
| Resolve a registered book's identity without claiming it | CC | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | Resolve a registered book's identity key | catalog | NEW | S5 provisional_codes CC_CLAIM_BOOK_IDENTITY_V0 |
| Claim a book's identity so a second registration of the same book is refused | CC | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | Claim a book's identity so a second registration of the same book is refused | catalog | NEW | S5 provisional_codes CC_CLAIM_BOOK_IDENTITY_V0 |
| Claim a copy's barcode so a second copy carrying it is refused | CC | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | Claim a copy's barcode so a second copy carrying it is refused | catalog | NEW | S5 provisional_codes CC_CLAIM_COPY_BARCODE_V0 |
| Record a book's bibliographic information as the catalog's authoritative description | CC | book_library_mgmt::CC_REGISTER_BOOK_V0 | Record a book's bibliographic information as the catalog's authoritative description | catalog | NEW | S5 provisional_codes CC_REGISTER_BOOK_V0 |
| Record a copy against exactly one book | CC | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | Record a copy against exactly one book | catalog | NEW | S5 provisional_codes CC_REGISTER_PHYSICAL_COPY_V0 |
| Replace a book's descriptive content in place | CC | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Replace a book's descriptive content in place | catalog | NEW | S5 provisional_codes CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| Mark a book record retired so it is no longer offered as current | CC | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | Mark a book record retired so it is no longer offered as current | catalog | NEW | S5 provisional_codes CC_RETIRE_BOOK_RECORD_V0 |
| Mark a copy retired so the library no longer holds it | CC | book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | Mark a copy retired so the library no longer holds it | catalog | NEW | S5 provisional_codes CC_RETIRE_PHYSICAL_COPY_V0 |
| Mark a retired book record registered again | CC | book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | Mark a retired book record registered again | catalog | NEW | S5 provisional_codes CC_REINSTATE_BOOK_RECORD_V0 |
| Mark a retired copy registered again | CC | book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | Mark a retired copy registered again | catalog | NEW | S5 provisional_codes CC_REINSTATE_PHYSICAL_COPY_V0 |
| Select the registered books matching a subject or title, excluding retired ones | CC | book_library_mgmt::CC_SEARCH_CATALOG_V0 | Select the registered books matching a subject or title, excluding retired ones | catalog | NEW | S5 provisional_codes CC_SEARCH_CATALOG_V0 |
| Assemble a book's record with the copies recorded against it | CC | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Assemble a book's record with the copies recorded against it | catalog | NEW | S5 provisional_codes CC_ASSEMBLE_BOOK_DETAILS_V0 |
| Append a durable account of a performed operation to the catalog's own trail | CC | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | Append a durable account of a performed operation to the catalog's own trail | catalog | NEW | S5 provisional_codes CC_APPEND_CATALOG_OPERATION_V0 |
| Form one identity key from a book's title, author and publication year | CT | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | Forms the single key the registry claims from the three identifying attributes | catalog | NEW | S3 authoring_decisions Enforce that one book exists per title, author and publication year |
| A book entered the catalog and acquired its authoritative record | EV | book_library_mgmt::EV_BOOK_REGISTERED_V0 | A book entered the catalog and acquired its authoritative record | catalog | NEW | S4 events Book registered |
| The library recorded another copy it owns | EV | book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | The library recorded another copy it owns | catalog | NEW | S4 events Physical copy registered |
| The authoritative description of a book changed | EV | book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | The authoritative description of a book changed | catalog | NEW | S4 events Bibliographic information updated |
| A book record is no longer to be used | EV | book_library_mgmt::EV_BOOK_RETIRED_V0 | A book record is no longer to be used | catalog | NEW | S4 events Book retired |
| The library no longer holds that copy | EV | book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | The library no longer holds that copy | catalog | NEW | S4 events Physical copy retired |
| Bind the catalog's operations to the stores and mechanisms they use | RB | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | Binds every catalog workflow to the mechanisms and stores it uses | catalog | NEW | S6 ownership Record a performed catalog operation in the catalog's audit trail |
| Declare the stores the catalog owns | STRUCTURE | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | Declares the five stores the catalog owns and the paths they occupy | catalog | NEW | S6 storage_governance A durable record of every book the library catalogs |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_BOOK_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_SEARCH_CATALOG_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every book the library catalogs |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::IN_REGISTER_BOOK_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_BOOK_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CLAIM_COPY_BARCODE_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_BOOK_V0 |
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
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REINSTATE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REINSTATE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_REINSTATE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REINSTATE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REINSTATE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REINSTATE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_REINSTATE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REINSTATE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::IN_SEARCH_CATALOG_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> book_library_mgmt::CC_SEARCH_CATALOG_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | CC | SUCCESS -> EXIT_COMPLETED; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_RETRIEVE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_RETRIEVE_BOOK_DETAILS_V0 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | 1 | confirm_authorization | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | staff_credentials, authorization_rules | is_authorized | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=staff_credentials, rules=authorization_rules; out: valid=is_authorized |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | 1 | validate_book_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | book_fields, book_schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=book_fields, schema=book_schema; out: violations=violations | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | 2 | require_submission_complete | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | barcode, book_fields | valid | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=barcode, rules=rules; out: valid=valid | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | 1 | form_identity_key | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | CT | FORM_BOOK_IDENTITY_KEY | — | title, author, publication_year | identity_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author, publication_year=publication_year; out: identity_key=identity_key |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | 2 | claim_identity | capability_side_effects::CS_REGISTRY_V0 | CS | REGISTER | BOOK_IDENTITY_REGISTRY | key, target_cs, target_ref | address | SUCCESS -> exit; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | ALREADY_EXISTS | — |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | 1 | resolve_identity | capability_side_effects::CS_REGISTRY_V0 | CS | RESOLVE | BOOK_IDENTITY_REGISTRY | key_or_address | target_ref | SUCCESS -> exit; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — | S7 cc_composition resolve_identity |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | 1 | claim_barcode | capability_side_effects::CS_REGISTRY_V0 | CS | REGISTER | COPY_BARCODE_REGISTRY | key, target_cs, target_ref | address | SUCCESS -> exit; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | ALREADY_EXISTS | — |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 1 | validate_book_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | book_fields, book_schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=book_fields, schema=book_schema; out: violations=violations |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 2 | assemble_book_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | book_fields | book_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=book_fields; out: record=book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 3 | write_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BOOKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 1 | read_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BOOKS | key | book_record | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 2 | assemble_copy_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | copy_fields | copy_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=copy_fields; out: record=copy_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | 3 | write_copy_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | PHYSICAL_COPIES | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 1 | read_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BOOKS | key | book_record | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 2 | form_updated_identity_key | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | CT | FORM_BOOK_IDENTITY_KEY | — | updated_fields | updated_identity_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author, publication_year=publication_year; out: identity_key=updated_identity_key | S7 cc_composition form_updated_identity_key |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 3 | compare_identity | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | CT | COMPARE_EQUAL | — | identity_key, updated_identity_key | identity_unchanged | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: left=identity_key, right=updated_identity_key; out: is_equal=identity_unchanged | S7 cc_composition compare_identity |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 4 | require_identity_unchanged | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | identity_unchanged | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=identity_unchanged, rules=rules; out: valid=valid | S7 cc_composition require_identity_unchanged |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 5 | assemble_updated_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | updated_fields | updated_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=updated_fields; out: record=updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 6 | write_updated_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BOOKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | 1 | select_book_records | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | SELECT | BOOKS | — | records | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | 2 | select_matching_books | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | CT | FILTER_RECORDS | — | records, search_criteria | matching_books | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: source=records, filter=search_criteria; out: extracted=matching_books |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 1 | read_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BOOKS | key | book_record | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 2 | select_copy_records | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | SELECT | PHYSICAL_COPIES | — | records | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 3 | select_copies_of_book | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | CT | FILTER_RECORDS | — | records, copy_criteria | copies_held | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: source=records, filter=copy_criteria; out: extracted=copies_held |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | 1 | set_record_state | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE_WHERE | PHYSICAL_COPIES | filter, updates | matched_keys, updated_count | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | 1 | set_record_state | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE_WHERE | PHYSICAL_COPIES | filter, updates | matched_keys, updated_count | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | 1 | set_record_state | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE_WHERE | BOOKS | filter, updates | matched_keys, updated_count | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | 1 | set_record_state | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE_WHERE | BOOKS | filter, updates | matched_keys, updated_count | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — | S7 cc_composition set_record_state |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | 1 | append_operation | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | CATALOG_OPERATIONS | record, stream_id, actor_id | record_id, sequence_number | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | confirm_authorization | INPUT | parameters | inputs.staff_credentials | S7 cc_composition confirm_authorization |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | confirm_authorization | INPUT | rules | inputs.authorization_rules | S7 cc_composition confirm_authorization |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | confirm_authorization | OUTPUT | is_authorized | capability_result.valid | S7 cc_composition confirm_authorization |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | INPUT | record | inputs.book_fields | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | INPUT | schema | inputs.book_schema | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | INPUT | parameters | {'barcode': '$.inputs.barcode', 'subject': '$.inputs.book_fields.subject'} | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | INPUT | rules | [{'field': 'barcode', 'op': 'neq', 'value': ''}, {'field': 'subject', 'op': 'neq', 'value': []}] | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | OUTPUT | valid | capability_result.valid | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | form_identity_key | INPUT | title | inputs.title | S7 cc_composition form_identity_key |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | form_identity_key | INPUT | author | inputs.author | S7 cc_composition form_identity_key |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | form_identity_key | INPUT | publication_year | inputs.publication_year | S7 cc_composition form_identity_key |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | form_identity_key | OUTPUT | identity_key | capability_result.identity_key | S7 cc_composition form_identity_key |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | claim_identity | INPUT | key | results.form_identity_key.identity_key | S7 cc_composition claim_identity |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | claim_identity | INPUT | target_cs | CS_MUTABLE_JSON_V0 | S7 cc_composition claim_identity |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | claim_identity | INPUT | target_ref | BOOKS | S7 cc_composition claim_identity |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | claim_identity | OUTPUT | address | capability_result.address | S7 cc_composition claim_identity |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | claim_identity | OUTPUT | result_status | result_status | S7 cc_composition claim_identity |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | resolve_identity | INPUT | key_or_address | inputs.identity_key | S7 cc_composition resolve_identity |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | resolve_identity | OUTPUT | target_ref | capability_result.target_ref | S7 cc_composition resolve_identity |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | resolve_identity | OUTPUT | result_status | result_status | S7 cc_composition resolve_identity |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | claim_barcode | INPUT | key | inputs.barcode | S7 cc_composition claim_barcode |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | claim_barcode | INPUT | target_cs | CS_MUTABLE_JSON_V0 | S7 cc_composition claim_barcode |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | claim_barcode | INPUT | target_ref | PHYSICAL_COPIES | S7 cc_composition claim_barcode |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | claim_barcode | OUTPUT | address | capability_result.address | S7 cc_composition claim_barcode |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | claim_barcode | OUTPUT | result_status | result_status | S7 cc_composition claim_barcode |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | INPUT | record | inputs.book_fields | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | INPUT | schema | inputs.book_schema | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | assemble_book_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'title': '$.inputs.book_fields.title', 'author': '$.inputs.book_fields.author', 'publication_year': '$.inputs.book_fields.publication_year', 'subject': '$.inputs.book_fields.subject', 'state': '$.inputs.book_fields.state'} | S7 cc_composition assemble_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | assemble_book_record | OUTPUT | book_record | capability_result.record | S7 cc_composition assemble_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | INPUT | key | inputs.identity_key | S7 cc_composition write_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | INPUT | value | results.assemble_book_record.book_record | S7 cc_composition write_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | OUTPUT | result_status | result_status | S7 cc_composition write_book_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | read_book_record | INPUT | key | inputs.identity_key | S7 cc_composition read_book_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | read_book_record | OUTPUT | book_record | capability_result.value | S7 cc_composition read_book_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | read_book_record | OUTPUT | result_status | result_status | S7 cc_composition read_book_record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | assemble_copy_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'barcode': '$.inputs.barcode', 'state': '$.inputs.copy_fields.state'} | S7 cc_composition assemble_copy_record |
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
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | assemble_updated_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'title': '$.inputs.updated_fields.title', 'author': '$.inputs.updated_fields.author', 'publication_year': '$.inputs.updated_fields.publication_year', 'subject': '$.inputs.updated_fields.subject', 'state': '$.inputs.updated_fields.state'} | S7 cc_composition assemble_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | assemble_updated_record | OUTPUT | updated_record | capability_result.record | S7 cc_composition assemble_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | INPUT | key | inputs.identity_key | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | INPUT | value | results.assemble_updated_record.updated_record | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | OUTPUT | result_status | result_status | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_book_records | OUTPUT | records | capability_result.records | S7 cc_composition select_book_records |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_book_records | OUTPUT | result_status | result_status | S7 cc_composition select_book_records |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_matching_books | INPUT | source | results.select_book_records.records | S7 cc_composition select_matching_books |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_matching_books | INPUT | filter | inputs.search_criteria | S7 cc_composition select_matching_books |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_matching_books | OUTPUT | matching_books | capability_result.extracted | S7 cc_composition select_matching_books |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_book_record | INPUT | key | inputs.identity_key | S7 cc_composition read_book_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_book_record | OUTPUT | book_record | capability_result.value | S7 cc_composition read_book_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_book_record | OUTPUT | result_status | result_status | S7 cc_composition read_book_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copy_records | OUTPUT | records | capability_result.records | S7 cc_composition select_copy_records |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copy_records | OUTPUT | result_status | result_status | S7 cc_composition select_copy_records |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | INPUT | source | results.select_copy_records.records | S7 cc_composition select_copies_of_book |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | INPUT | filter | inputs.copy_criteria | S7 cc_composition select_copies_of_book |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | OUTPUT | copies_held | capability_result.extracted | S7 cc_composition select_copies_of_book |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | set_record_state | INPUT | filter | {'barcode': '$.inputs.barcode'} | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | set_record_state | INPUT | updates | {'state': 'REGISTERED'} | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | set_record_state | OUTPUT | matched_keys | capability_result.matched_keys | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | set_record_state | OUTPUT | updated_count | capability_result.updated_count | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | set_record_state | OUTPUT | result_status | result_status | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | set_record_state | INPUT | filter | {'barcode': '$.inputs.barcode'} | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | set_record_state | INPUT | updates | {'state': 'RETIRED'} | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | set_record_state | OUTPUT | matched_keys | capability_result.matched_keys | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | set_record_state | OUTPUT | updated_count | capability_result.updated_count | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | set_record_state | OUTPUT | result_status | result_status | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | set_record_state | INPUT | filter | {'identity_key': '$.inputs.identity_key'} | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | set_record_state | INPUT | updates | {'state': 'REGISTERED'} | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | set_record_state | OUTPUT | matched_keys | capability_result.matched_keys | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | set_record_state | OUTPUT | updated_count | capability_result.updated_count | S7 cc_composition set_record_state |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | set_record_state | OUTPUT | result_status | result_status | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | set_record_state | INPUT | filter | {'identity_key': '$.inputs.identity_key'} | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | set_record_state | INPUT | updates | {'state': 'RETIRED'} | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | set_record_state | OUTPUT | matched_keys | capability_result.matched_keys | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | set_record_state | OUTPUT | updated_count | capability_result.updated_count | S7 cc_composition set_record_state |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | set_record_state | OUTPUT | result_status | result_status | S7 cc_composition set_record_state |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | append_operation | INPUT | record | inputs.record | S7 cc_composition append_operation |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | append_operation | INPUT | stream_id | CATALOG_OPERATIONS | S7 cc_composition append_operation |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | append_operation | INPUT | actor_id | inputs.staff_id | S7 cc_composition append_operation |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | append_operation | OUTPUT | record_id | capability_result.record_id | S7 cc_composition append_operation |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | append_operation | OUTPUT | sequence_number | capability_result.sequence_number | S7 cc_composition append_operation |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | payload.book_fields | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_schema | payload.book_schema | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | title | payload.title | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | author | payload.author | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | publication_year | payload.publication_year | S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_fields | payload.book_fields | S7 execution_topology CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_schema | payload.book_schema | S7 execution_topology CC_REGISTER_BOOK_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_CLAIM_COPY_BARCODE_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | payload.copy_fields | S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REGISTER_BOOK | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_BOOK', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.title'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
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
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_REINSTATE_BOOK_RECORD_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REINSTATE_BOOK_RECORD | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REINSTATE_BOOK_RECORD', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | INPUT | barcode | payload.barcode | S7 execution_topology CC_REINSTATE_PHYSICAL_COPY_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | REINSTATE_PHYSICAL_COPY | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'REINSTATE_PHYSICAL_COPY', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.barcode'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_SEARCH_CATALOG_V0 | INPUT | search_criteria | payload.search_criteria | S7 execution_topology CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | SEARCH_CATALOG | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'SEARCH_CATALOG', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.search_criteria'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | copy_criteria | {'identity_key': '$.payload.identity_key'} | S7 execution_topology CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | RETRIEVE_BOOK_DETAILS | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | {'operation': 'RETRIEVE_BOOK_DETAILS', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0 |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | title | string | YES |  | The title the book is published under |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | author | string | YES |  | The author the book is published under |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | publication_year | integer | YES |  | The year this edition was published |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | book_fields | object | YES |  | The book's bibliographic information |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | book_schema | object | YES |  | The fields a book record must carry, as the rules its structure is validated against |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | copy_fields | object | YES |  | The copy's recorded detail |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | object | YES |  | The copy's recorded detail |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | title | string | YES |  | The title the book is published under |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | author | string | YES |  | The author the book is published under |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | publication_year | integer | YES |  | The year this edition was published |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | updated_fields | object | YES |  | The changed bibliographic information |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | search_criteria | object | YES |  | What staff are searching by, and the states to include |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | OUTPUT | is_authorized | boolean | YES |  | Whether the staff member may perform catalog operations |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | object | YES |  | The book's bibliographic information |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_schema | object | YES |  | The fields a book record must carry, as the rules its structure is validated against |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | OUTPUT | valid | boolean | YES |  | Whether the submission may proceed to be claimed and written |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | title | string | YES |  | The title the book is published under |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | author | string | YES |  | The author the book is published under |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | INPUT | publication_year | integer | YES |  | The year this edition was published |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | OUTPUT | address | string | YES |  | Where the claimed key resolves to |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | OUTPUT | target_ref | string | YES |  | Where the registered key resolves to |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | OUTPUT | address | string | YES |  | Where the claimed key resolves to |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_fields | object | YES |  | The book's bibliographic information |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_schema | object | YES |  | The fields a book record must carry, as the rules its structure is validated against |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | OUTPUT | book_record | object | YES |  | The book's authoritative record |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | INPUT | copy_fields | object | YES |  | The copy's recorded detail |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | OUTPUT | book_record | object | YES |  | The book's authoritative record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | updated_fields | object | YES |  | The changed bibliographic information |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | OUTPUT | book_record | object | YES |  | The book's authoritative record |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | OUTPUT | updated_count | integer | YES |  | How many records the state change matched and updated |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | OUTPUT | updated_count | integer | YES |  | How many records the state change matched and updated |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | OUTPUT | updated_count | integer | YES |  | How many records the state change matched and updated |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | INPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | OUTPUT | updated_count | integer | YES |  | How many records the state change matched and updated |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | INPUT | search_criteria | object | YES |  | What staff are searching by, and the states to include |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | OUTPUT | matching_books | array | YES |  | The registered books matching what was searched for |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | copy_criteria | object | YES |  | Which copies belong to the book being retrieved |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | OUTPUT | book_record | object | YES |  | The book's authoritative record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | OUTPUT | copies_held | array | YES |  | The copies the library holds of the book |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | record | object | YES |  | The account of the performed operation |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | INPUT | operation | string | YES |  | operation |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | OUTPUT | record_id | string | YES |  | The identity of the appended trail entry |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | OUTPUT | sequence_number | integer | YES |  | The entry's position in the trail |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | OUTPUT | title | string | YES |  | The title the book is published under |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | OUTPUT | author | string | YES |  | The author the book is published under |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | OUTPUT | publication_year | integer | YES |  | The year this edition was published |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | OUTPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | OUTPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | OUTPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | OUTPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | OUTPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::EV_BOOK_RETIRED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::EV_BOOK_RETIRED_V0 | OUTPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | OUTPUT | barcode | string | YES |  | The barcode the library assigned to the copy |
| book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | OUTPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | INPUT | title | string | YES |  | The title the book is published under |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | INPUT | author | string | YES |  | The author the book is published under |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | INPUT | publication_year | integer | YES |  | The year this edition was published |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | ATTRIBUTE | staff_id | string | YES |  | The staff member's identity as the library knows it |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | ATTRIBUTE | authorized | boolean | NO | false | Whether the staff member may perform catalog operations; decided by the staff function, read here |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
| --------- | -------- | ---------- | ----------- | ----------------------- | ----------------------------- | -------------------------------- | ---------------- |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_form_book_identity_key_v0 | execute | PURE_FORM_BOOK_IDENTITY_KEY | atom | ct_pure | never | S7 new_artifacts CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|

Every status this design routes on — ACK, NACK, SUCCESS, NOT_FOUND, ALREADY_EXISTS, DENIED, VIOLATION,
BACKEND_ERROR — is already admitted, so no vocabulary is extended.

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0 | structure | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S7 rb_declarations RB_CATALOG_BINDINGS_V0 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | capability_side_effects::CS_REGISTRY_V0 | structure | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S7 rb_declarations RB_CATALOG_BINDINGS_V0 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0 | structure | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S7 rb_declarations RB_CATALOG_BINDINGS_V0 |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | type | ENDUSER | S5 provisional_codes AC_LIBRARY_STAFF_V0 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|-----------------------------------------------------------|---------------|---------|----------------|
| BOOKS | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/books.json | book_library_mgmt::CC_REGISTER_BOOK_V0 | S6 storage_governance A durable record of every book the library catalogs |
| PHYSICAL_COPIES | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/physical_copies.json | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | S6 storage_governance A durable record of every physical copy the library owns |
| CATALOG_OPERATIONS | CS_APPENDONLY_JSONL_V0 | book_library_mgmt/catalog/catalog_operations.jsonl | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | S6 storage_governance A trail of performed operations that cannot be amended |
| BOOK_IDENTITY_REGISTRY | CS_REGISTRY_V0 | book_library_mgmt/catalog/book_identity_registry.jsonl | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | S6 storage_governance A claim on each book's identity, held once |
| COPY_BARCODE_REGISTRY | CS_REGISTRY_V0 | book_library_mgmt/catalog/copy_barcode_registry.jsonl | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | S6 storage_governance A claim on each copy's barcode, held once |

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
| NEW | catalog | 40 | 1 AC, 9 IN, 9 WF, 13 CC, 1 CT, 5 EV, 1 RB, 1 STRUCTURE |
| EXTEND | platform | 1 | capability_side_effects::CS_MUTABLE_JSON_V0 |

---

## 16. Generation Provenance

*Every artifact this design schedules is authored: construction renders it from the registers
above and it is its own source of truth. Nothing here is reached by invoking a generator.*

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
| Register a book | Its title, author and publication year match a registered book. | book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | SUCCESS | S0 operation_refusals #1 |
| Register a book | No physical copy is offered with it. | book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | VIOLATION | S0 operation_refusals #2 |
| Register a book | It carries no subject. | book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | VIOLATION | S0 operation_refusals #3 |
| Register a physical copy | The book it names is not registered. | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | NOT_FOUND | S0 operation_refusals #4 |
| Register a physical copy | Its barcode matches a copy the library already owns. | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | ALREADY_EXISTS | S0 operation_refusals #5 |
| Update bibliographic information | The changed title, author and publication year would match another registered book. | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | VIOLATION | S0 operation_refusals #6 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_REGISTER_BOOK_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_SEARCH_CATALOG_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |
| Any catalog operation | The staff member performing it is not authorized. | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #7 |

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
| NONE IDENTIFIED |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
