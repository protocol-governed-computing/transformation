# Design Intent: book_library_mgmt / catalog

**Stage:** 7 — Design Intent
**CR:** cr_02_catalog
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Eight artifacts are authored and six existing ones are extended. The extended six carry identities
the composition already holds, so they are inventoried rather than assigned — a design that assigned
them again would create a second artifact under the same name.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The record the previous change calls a book is an edition; the work is added above it | Editions of one work share a title and an author and differ by publication year | No existing identity changes. A work store and a work identity registry are added, and the edition record gains the key of the work it belongs to | S4 design_decisions #1 |
| The work's identity is formed by a new transform | The edition key transform is reached by every catalog operation and 23 artifacts depend on it | A second transform forms the work key from title and author; the two are independent and neither can alter the other | S4 design_decisions #2 |
| The work is claimed through the same registry mechanism the edition is claimed through | Register-if-absent gives the atomic uniqueness a work identity needs | A registry store claims the work key; a claim that finds the key already held yields ALREADY_EXISTS, which the registration treats as the work having been found rather than as a refusal | S4 design_decisions #3 |
| The work store and the work identity registry are declared in the catalog's own storage declaration | A subdomain declares its stores once and binds them once | Both stores are added to the existing storage declaration and reached through the existing runtime binding | S4 design_decisions #4 |
| Registering an edition of a new work extends the existing registration; registering an additional edition is a new operation | The existing registration creates the work and requires a first copy; an additional edition does neither | The existing workflow gains a work claim before its claims; a second workflow resolves an existing work and claims only the edition | S4 design_decisions #5 |
| The work claim is placed among the existing claims, before any write | A refused registration must leave nothing behind | The work claim runs after validation and before the edition and barcode claims, so every claim still precedes every write | S4 design_decisions #6 |
| Search is extended rather than duplicated, and answers at the level of the work | Two searches would leave staff choosing which one answers their question | The existing search gains a grouping step after its selection step; the search terms and the records it selects are unchanged | S4 design_decisions #7 |
| Retrieval stays edition retrieval and carries a summary of the work | The business asked for one retrieval carrying a summary, not a second operation | The existing retrieval gains a read of the work record; the edition and its copies are assembled as before | S4 design_decisions #8 |
| A work is never retired | A work whose editions are all retired is simply that | No retirement operation names the work, and no routing reaches the work store from a retirement | S4 design_decisions #9 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | EXTEND | Declares the stores the catalog owns and the paths they occupy | Gains the work record store and the work identity registry alongside the five stores the catalog already owns | S6 pps_artifacts_requiring_action book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | EXTEND | Binds the catalog's workflows to the stores and mechanisms they use | Binds the new workflow to the same substrates and the same storage declaration the catalog already uses | S6 pps_artifacts_requiring_action book_library_mgmt::RB_CATALOG_BINDINGS_V0 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | EXTEND | Registers a work with its first edition and that edition's first physical copy | Gains one node: the work claim, placed after validation and before every other claim | S6 ownership Register an edition of a work the catalog does not yet hold |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | EXTEND | Validates, assembles and writes an edition record against the work it belongs to | The edition record it assembles now carries the key of the work the edition belongs to | S6 pps_artifacts_requiring_action book_library_mgmt::CC_REGISTER_BOOK_V0 |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | EXTEND | Confirms a registration carries what a work and an edition require, before any identity is claimed | Confirms the submission carries what a work requires as well as what an edition requires | S6 pps_artifacts_requiring_action book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | EXTEND | Selects the registered editions matching a subject or title and groups them under their work | Groups the matching editions under the work they belong to, so the answer is one result per work | S6 pps_artifacts_requiring_action book_library_mgmt::CC_SEARCH_CATALOG_V0 |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | EXTEND | Assembles an edition, the physical copies of it, and the record of the work it belongs to | Reads the work record so the retrieval carries a summary of the work the edition belongs to | S6 pps_artifacts_requiring_action book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | REUSE |  | The actor every catalog workflow runs as, including the one this change adds — authorization is read from what the caller supplies and granted nowhere | S6 ownership Confirm the staff member performing an operation is authorized |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | REUSE |  | The registration's entry point is unchanged — what a caller supplies is what it supplied before, and only the sequence it starts gains a node | S6 pps_artifacts_requiring_action book_library_mgmt::CC_REGISTER_BOOK_V0 |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | REVIEW |  | Examined and deliberately not widened; it continues to form the edition key from three attributes | S6 pps_artifacts_requiring_action book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | REUSE |  | Claims the edition's identity unchanged, and is the precedent the work claim follows | S6 pps_artifacts_requiring_action book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | REUSE |  | Every operation this change adds reaches it first, as every existing operation does | S6 ownership Confirm the staff member performing an operation is authorized |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | REUSE |  | Records the operations this change adds into the trail it already appends to | S6 ownership Record every performed operation in the catalog's audit trail |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | REUSE |  | A copy already belongs to exactly one record, and that record is an edition | S6 ownership Register a physical copy against exactly one edition |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | REUSE |  | Barcode uniqueness is unaffected by the work abstraction | S6 ownership Register a physical copy against exactly one edition |
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE |  | Holds the work record as it holds the edition and copy records | S6 pps_artifacts_requiring_action capability_side_effects::CS_MUTABLE_JSON_V0 |
| capability_side_effects::CS_REGISTRY_V0 | REUSE |  | Claims the work key as it claims the edition key and the barcode | S6 pps_artifacts_requiring_action capability_side_effects::CS_REGISTRY_V0 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE |  | Appends the operations this change adds to the catalog's trail | S6 storage_governance An unamendable trail of every operation performed |
| capability_transforms::CT_PURE_FILTER_RECORDS_V0 | REVIEW |  | Examined and not extended; it selects records and the grouping is a separate transform | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_FILTER_RECORDS_V0 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE |  | Assembles the work record as it assembles the edition and copy records | S6 storage_governance A durable record of every work the library has catalogued |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | REUSE |  | Confirms a submission carries the fields its schema declares, for the work as for the edition | S6 ownership Validate that a registration carries what a work and an edition require |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | REUSE |  | Compares two values for equality, unchanged — the update uses it to confirm an edition's identity did not change | S6 pps_artifacts_requiring_action book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | REUSE |  | Turns a validation result into a refusal, unchanged | S6 ownership Validate that a registration carries what a work and an edition require |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | EXTEND | Changes a registered edition's descriptive content and refuses a change that would duplicate another edition | The record it writes back now carries the work the edition belongs to, which it previously dropped | S6 pps_artifacts_requiring_action book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| Form the identifying key of a work from its title and author | CT | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | Forms the single key claimed for a work from its title and author | catalog | NEW | S5 provisional_codes CT_PURE_FORM_WORK_IDENTITY_KEY_V0 |
| Select records matching criteria, answering none when none match | CT | book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | Selects the records matching stated criteria and returns none when none match | catalog | NEW | S5 provisional_codes CT_PURE_SELECT_RECORDS_V0 |
| Group selected records by an attribute they share | CT | book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | Groups records by the value of a named attribute, returning one group per distinct value | catalog | NEW | S5 provisional_codes CT_PURE_GROUP_RECORDS_V0 |
| Claim a work's identity so that two registrations of one work do not produce two works | CC | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | Forms the work key, claims it, and writes the work record when the claim is new | catalog | NEW | S5 provisional_codes CC_CLAIM_WORK_IDENTITY_V0 |
| Resolve the work an edition belongs to | CC | book_library_mgmt::CC_RESOLVE_WORK_V0 | Forms the work key, resolves it against the registry, and reads the work record it names | catalog | NEW | S5 provisional_codes CC_RESOLVE_WORK_V0 |
| Register an additional edition of an existing work | CC | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | Assembles the edition record against a resolved work and writes it | catalog | NEW | S5 provisional_codes CC_REGISTER_ADDITIONAL_EDITION_V0 |
| Admit a request to register an additional edition of an existing work | IN | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | A request to register a further edition of a work the catalog already holds | catalog | NEW | S5 provisional_codes IN_REGISTER_ADDITIONAL_EDITION_V0 |
| Register an additional edition of an existing work | WF | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | The governed sequence that registers a further edition of an existing work | catalog | NEW | S5 provisional_codes WF_REGISTER_ADDITIONAL_EDITION_V0 |
| Recognise the moment a work enters the catalog | EV | book_library_mgmt::EV_WORK_REGISTERED_V0 | The moment a work enters the catalog, created by the edition that evidences it | catalog | NEW | S5 provisional_codes EV_WORK_REGISTERED_V0 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance A durable record of every work the library has catalogued |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | book_library_mgmt::WF_REGISTER_BOOK_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S6 storage_governance An atomic claim on each work's identity |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | IN | ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_CONFIRM_STAFF_AUTHORIZED_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | CC | SUCCESS -> book_library_mgmt::CC_RESOLVE_WORK_V0; VIOLATION -> EXIT_REJECTED | S7 existing_inventory CC_VALIDATE_BOOK_SUBMISSION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_RESOLVE_WORK_V0 | CC | SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RESOLVE_WORK_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | CC | SUCCESS -> book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_CLAIM_BOOK_IDENTITY_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | CC | SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | CC | SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 existing_inventory CC_APPEND_CATALOG_OPERATION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXIT_COMPLETED | EXIT_SUCCESS | — | S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | EXIT_REJECTED | EXIT | — | S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0 |
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

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | 1 | form_work_key | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | CT | FORM_WORK_IDENTITY_KEY | — | title, author | work_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author; out: work_key=work_key |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | 2 | claim_work | capability_side_effects::CS_REGISTRY_V0 | CS | REGISTER | WORK_IDENTITY_REGISTRY | key, target_cs, target_ref | address | SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | ALREADY_EXISTS | — |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | 3 | assemble_work_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | work_fields | work_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=work_fields; out: record=work_record |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | 4 | write_work_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | WORKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | 1 | form_work_key | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | CT | FORM_WORK_IDENTITY_KEY | — | title, author | work_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author; out: work_key=work_key |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | 2 | resolve_work_claim | capability_side_effects::CS_REGISTRY_V0 | CS | RESOLVE | WORK_IDENTITY_REGISTRY | key_or_address | target_ref | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | 3 | read_work_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | WORKS | key | value | SUCCESS -> exit; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | 1 | validate_edition_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | edition_fields, edition_schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=edition_fields, schema=edition_schema; out: violations=violations |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | 2 | assemble_edition_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | edition_fields | edition_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=edition_fields; out: record=edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | 3 | write_edition_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BOOKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 1 | form_work_key | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | CT | FORM_WORK_IDENTITY_KEY | — | title, author | work_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author; out: work_key=work_key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 2 | validate_book_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | book_fields, book_schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=book_fields, schema=book_schema; out: violations=violations |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 3 | assemble_book_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | book_fields | book_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=book_fields; out: record=book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | 4 | write_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BOOKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | 1 | validate_book_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | book_fields, book_schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=book_fields, schema=book_schema; out: violations=violations |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | 2 | validate_work_fields | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | work_fields, work_schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=work_fields, schema=work_schema; out: violations=violations |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | 3 | require_submission_complete | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | barcode, book_fields | valid | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=barcode, rules=rules; out: valid=valid |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | 1 | select_book_records | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | SELECT | BOOKS | — | records | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | 2 | select_matching_books | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | CT | FILTER_RECORDS | — | records, search_criteria | matching_books | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: source=records, filter=search_criteria; out: extracted=matching_books |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | 3 | group_editions_by_work | book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | CT | GROUP_RECORDS | — | matching_books, group_by | matching_works | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: source=matching_books, attribute=group_by; out: grouped=matching_works |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 1 | read_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BOOKS | key | value | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 2 | form_work_key | book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | CT | FORM_WORK_IDENTITY_KEY | — | title, author | work_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author; out: work_key=work_key |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 3 | read_work_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | WORKS | key | value | SUCCESS -> continue; NOT_FOUND -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 4 | select_copy_records | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | SELECT | PHYSICAL_COPIES | — | records | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS | — |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | 5 | select_copies_of_book | book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | CT | SELECT_RECORDS | — | records, copy_criteria | copies_held | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: source=records, filter=copy_criteria; out: extracted=copies_held |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 1 | read_book_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | BOOKS | key | book_record | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 2 | form_updated_identity_key | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | CT | FORM_BOOK_IDENTITY_KEY | — | updated_fields | updated_identity_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: title=title, author=author, publication_year=publication_year; out: identity_key=updated_identity_key |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 3 | compare_identity | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | CT | COMPARE_EQUAL | — | identity_key, updated_identity_key | identity_unchanged | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: left=identity_key, right=updated_identity_key; out: is_equal=identity_unchanged |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 4 | require_identity_unchanged | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | identity_unchanged | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=identity_unchanged, rules=rules; out: valid=valid |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 5 | assemble_updated_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | updated_fields | updated_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=updated_fields; out: record=updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | 6 | write_updated_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | BOOKS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | form_work_key | INPUT | title | inputs.title | S7 cc_composition form_work_key |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | form_work_key | INPUT | author | inputs.author | S7 cc_composition form_work_key |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | form_work_key | OUTPUT | work_key | capability_result.work_key | S7 cc_composition form_work_key |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | claim_work | INPUT | key | results.form_work_key.work_key | S7 cc_composition claim_work |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | claim_work | INPUT | target_cs | CS_MUTABLE_JSON_V0 | S7 cc_composition claim_work |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | claim_work | INPUT | target_ref | WORKS | S7 cc_composition claim_work |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | claim_work | OUTPUT | address | capability_result.address | S7 cc_composition claim_work |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | claim_work | OUTPUT | result_status | result_status | S7 cc_composition claim_work |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | assemble_work_record | INPUT | fields | inputs.work_fields | S7 cc_composition assemble_work_record |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | assemble_work_record | OUTPUT | work_record | capability_result.record | S7 cc_composition assemble_work_record |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | write_work_record | INPUT | key | results.form_work_key.work_key | S7 cc_composition write_work_record |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | write_work_record | INPUT | value | results.assemble_work_record.work_record | S7 cc_composition write_work_record |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | write_work_record | OUTPUT | result_status | result_status | S7 cc_composition write_work_record |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | form_work_key | INPUT | title | inputs.title | S7 cc_composition form_work_key |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | form_work_key | INPUT | author | inputs.author | S7 cc_composition form_work_key |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | form_work_key | OUTPUT | work_key | capability_result.work_key | S7 cc_composition form_work_key |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | resolve_work_claim | INPUT | key_or_address | results.form_work_key.work_key | S7 cc_composition resolve_work_claim |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | resolve_work_claim | OUTPUT | target_ref | capability_result.target_ref | S7 cc_composition resolve_work_claim |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | resolve_work_claim | OUTPUT | result_status | result_status | S7 cc_composition resolve_work_claim |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | read_work_record | INPUT | key | results.form_work_key.work_key | S7 cc_composition read_work_record |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | read_work_record | OUTPUT | work_record | capability_result.value | S7 cc_composition read_work_record |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | read_work_record | OUTPUT | result_status | result_status | S7 cc_composition read_work_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | validate_edition_fields | INPUT | record | inputs.edition_fields | S7 cc_composition validate_edition_fields |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | validate_edition_fields | INPUT | schema | inputs.edition_schema | S7 cc_composition validate_edition_fields |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | validate_edition_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_edition_fields |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | assemble_edition_record | INPUT | fields | inputs.edition_fields | S7 cc_composition assemble_edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | assemble_edition_record | OUTPUT | edition_record | capability_result.record | S7 cc_composition assemble_edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | write_edition_record | INPUT | key | inputs.identity_key | S7 cc_composition write_edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | write_edition_record | INPUT | value | results.assemble_edition_record.edition_record | S7 cc_composition write_edition_record |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | write_edition_record | OUTPUT | result_status | result_status | S7 cc_composition write_edition_record |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_book_records | OUTPUT | records | capability_result.records | S7 cc_composition select_book_records |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_book_records | OUTPUT | result_status | result_status | S7 cc_composition select_book_records |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_matching_books | INPUT | source | results.select_book_records.records | S7 cc_composition select_matching_books |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_matching_books | INPUT | filter | inputs.search_criteria | S7 cc_composition select_matching_books |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | select_matching_books | OUTPUT | matching_books | capability_result.extracted | S7 cc_composition select_matching_books |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | group_editions_by_work | INPUT | source | results.select_matching_books.matching_books | S7 cc_composition group_editions_by_work |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | group_editions_by_work | INPUT | attribute | work_key | S7 cc_composition group_editions_by_work |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | group_editions_by_work | OUTPUT | matching_works | capability_result.grouped | S7 cc_composition group_editions_by_work |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_book_record | INPUT | key | inputs.identity_key | S7 cc_composition read_book_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_book_record | OUTPUT | value | capability_result.value | S7 cc_composition read_book_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_book_record | OUTPUT | result_status | result_status | S7 cc_composition read_book_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | form_work_key | INPUT | title | results.read_book_record.value.title | S7 cc_composition form_work_key |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | form_work_key | INPUT | author | results.read_book_record.value.author | S7 cc_composition form_work_key |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | form_work_key | OUTPUT | work_key | capability_result.work_key | S7 cc_composition form_work_key |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_work_record | INPUT | key | results.form_work_key.work_key | S7 cc_composition read_work_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_work_record | OUTPUT | work_record | capability_result.value | S7 cc_composition read_work_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copy_records | OUTPUT | records | capability_result.records | S7 cc_composition select_copy_records |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | INPUT | source | results.select_copy_records.records | S7 cc_composition select_copies_of_book |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | INPUT | filter | inputs.copy_criteria | S7 cc_composition select_copies_of_book |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | OUTPUT | copies_held | capability_result.extracted | S7 cc_composition select_copies_of_book |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_work_fields | INPUT | record | inputs.work_fields | S7 cc_composition validate_work_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_work_fields | INPUT | schema | inputs.work_schema | S7 cc_composition validate_work_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_work_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_work_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | form_work_key | INPUT | title | inputs.book_fields.title | S7 cc_composition form_work_key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | form_work_key | INPUT | author | inputs.book_fields.author | S7 cc_composition form_work_key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | form_work_key | OUTPUT | work_key | capability_result.work_key | S7 cc_composition form_work_key |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | assemble_book_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'title': '$.inputs.book_fields.title', 'author': '$.inputs.book_fields.author', 'publication_year': '$.inputs.book_fields.publication_year', 'subject': '$.inputs.book_fields.subject', 'state': '$.inputs.book_fields.state', 'work_key': '$.results.form_work_key.work_key'} | S7 cc_composition assemble_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | assemble_book_record | OUTPUT | book_record | capability_result.record | S7 cc_composition assemble_book_record |
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
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | INPUT | record | inputs.book_fields | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | INPUT | schema | inputs.book_schema | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | validate_book_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | INPUT | parameters | {'barcode': '$.inputs.barcode', 'subject': '$.inputs.book_fields.subject'} | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | INPUT | rules | [{'field': 'barcode', 'op': 'neq', 'value': ''}, {'field': 'subject', 'op': 'neq', 'value': []}] | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | require_submission_complete | OUTPUT | valid | capability_result.valid | S7 cc_composition require_submission_complete |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | INPUT | record | inputs.book_fields | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | INPUT | schema | inputs.book_schema | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | validate_book_fields | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_book_fields |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | INPUT | key | inputs.identity_key | S7 cc_composition write_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | INPUT | value | results.assemble_book_record.book_record | S7 cc_composition write_book_record |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | write_book_record | OUTPUT | result_status | result_status | S7 cc_composition write_book_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | read_book_record | OUTPUT | book_record | capability_result.value | S7 cc_composition read_book_record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copy_records | OUTPUT | result_status | result_status | S7 cc_composition select_copy_records |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | INPUT | source | results.select_copy_records.records | S7 cc_composition select_copies_of_book |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | INPUT | filter | inputs.copy_criteria | S7 cc_composition select_copies_of_book |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | select_copies_of_book | OUTPUT | copies_held | capability_result.extracted | S7 cc_composition select_copies_of_book |
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
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | assemble_updated_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'title': '$.inputs.updated_fields.title', 'author': '$.inputs.updated_fields.author', 'publication_year': '$.inputs.updated_fields.publication_year', 'subject': '$.inputs.updated_fields.subject', 'state': '$.inputs.updated_fields.state', 'work_key': '$.results.read_book_record.book_record.work_key'} | S7 cc_composition assemble_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | assemble_updated_record | OUTPUT | updated_record | capability_result.record | S7 cc_composition assemble_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | INPUT | key | inputs.identity_key | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | INPUT | value | results.assemble_updated_record.updated_record | S7 cc_composition write_updated_record |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | write_updated_record | OUTPUT | result_status | result_status | S7 cc_composition write_updated_record |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the catalog receives it |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the audit trail |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | title | string | YES |  | The title of the work the edition belongs to, and of the edition itself |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | author | string | YES |  | The author of the work the edition belongs to |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | publication_year | string | YES |  | The year that distinguishes this edition from the work's other editions |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | subject | array | YES |  | What kind of material the edition is, as free text |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_fields | object | YES |  | The edition's descriptive content as submitted |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_schema | object | YES |  | The fields an edition record is required to carry |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | work_fields | object | YES |  | The work's identifying attributes as submitted |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | work_schema | object | YES |  | The fields a work record is required to carry |
| book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | INPUT | title | string | YES |  | The work's title, compared without regard to letter case or repeated spacing |
| book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | INPUT | author | string | YES |  | The work's author, compared the same way |
| book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | OUTPUT | work_key | string | YES |  | The single key claimed for the work |
| book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | INPUT | source | array | YES |  | The records to select from |
| book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | INPUT | filter | object | YES |  | The criteria a record must match on every key |
| book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | OUTPUT | extracted | array | YES |  | The records that matched, possibly none |
| book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | INPUT | source | array | YES |  | The records to group |
| book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | INPUT | attribute | string | YES |  | The attribute whose value decides which group a record belongs to |
| book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | OUTPUT | grouped | array | YES |  | One group per distinct value, each carrying the records that share it |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | title | string | YES |  | The work's title |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | author | string | YES |  | The work's author |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | INPUT | work_fields | object | YES |  | The work record's content, written when the claim is new |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | OUTPUT | work_key | string | YES |  | The key claimed for the work, whether the claim was new or already held |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | INPUT | title | string | YES |  | The title of the work to resolve |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | INPUT | author | string | YES |  | The author of the work to resolve |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | OUTPUT | work_key | string | YES |  | The key of the work that was resolved |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | OUTPUT | work_record | object | NO |  | The work record the key names, when the work exists |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | identity_key | string | YES |  | The edition's claimed identity, which is the key its record occupies |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_fields | object | YES |  | The edition record's content, including the key of the work it belongs to |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | INPUT | edition_schema | object | YES |  | The fields an edition record is required to carry |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | OUTPUT | edition_record | object | YES |  | The edition record as written |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_fields | object | YES |  | The work's identifying attributes, validated alongside the edition's |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | work_schema | object | YES |  | The fields a work record is required to carry |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | OUTPUT | valid | boolean | YES |  | Whether the submission may proceed to be claimed and written |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | OUTPUT | book_record | object | YES |  | The edition's authoritative record, carrying the key of the work it belongs to |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_fields | object | YES |  | The edition record's content, now including the key of the work it belongs to |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | OUTPUT | matching_works | array | YES |  | One entry per matching work, each carrying the editions of it that matched |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | OUTPUT | work_record | object | YES |  | The record of the work the edition belongs to — its title and author — so the work need not be looked up separately |
| book_library_mgmt::EV_WORK_REGISTERED_V0 | ATTRIBUTE | work_key | string | YES |  | The work that entered the catalog |
| book_library_mgmt::EV_WORK_REGISTERED_V0 | ATTRIBUTE | title | string | YES |  | The work's title |
| book_library_mgmt::EV_WORK_REGISTERED_V0 | ATTRIBUTE | author | string | YES |  | The work's author |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_fields | object | YES |  | The book's bibliographic information |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | book_schema | object | YES |  | The fields a book record must carry, as the rules its structure is validated against |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | INPUT | barcode | string | NO |  | The barcode the library assigned to the copy, when the registration carries one — an additional edition of an existing work does not |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | INPUT | book_schema | object | YES |  | The fields a book record must carry, as the rules its structure is validated against |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | INPUT | search_criteria | object | YES |  | What staff are searching by, and the states to include |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | OUTPUT | matching_books | array | YES |  | The registered books matching what was searched for |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | INPUT | copy_criteria | object | YES |  | Which copies belong to the book being retrieved |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | OUTPUT | book_record | object | YES |  | The book's authoritative record |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | OUTPUT | copies_held | array | YES |  | The copies the library holds of the book |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | identity_key | string | YES |  | The key formed from a book's title, author and publication year |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | INPUT | updated_fields | object | YES |  | The changed bibliographic information |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | OUTPUT | book_record | object | YES |  | The book's authoritative record |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
| --------- | -------- | ---------- | ----------- | ----------------------- | ----------------------------- | -------------------------------- | ---------------- |
| book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_form_work_identity_key_v0 | execute | PURE_FORM_WORK_IDENTITY_KEY | atom | ct_pure | never | S7 new_artifacts CT_PURE_FORM_WORK_IDENTITY_KEY_V0 |
| book_library_mgmt::CT_PURE_SELECT_RECORDS_V0 | book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_select_records_v0 | execute | PURE_SELECT_RECORDS | atom | ct_pure | never | S7 new_artifacts CT_PURE_SELECT_RECORDS_V0 |
| book_library_mgmt::CT_PURE_GROUP_RECORDS_V0 | book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_group_records_v0 | execute | PURE_GROUP_RECORDS | atom | ct_pure | never | S7 new_artifacts CT_PURE_GROUP_RECORDS_V0 |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|

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
| book_library_mgmt::EV_WORK_REGISTERED_V0 | type | BUSINESS_MOMENT | S5 provisional_codes EV_WORK_REGISTERED_V0 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|-----------------------------------------------------------|---------------|---------|----------------|
| WORKS | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/works.json | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | S6 storage_governance A durable record of every work the library has catalogued |
| WORK_IDENTITY_REGISTRY | CS_REGISTRY_V0 | book_library_mgmt/catalog/work_identity_registry.jsonl | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | S6 storage_governance An atomic claim on each work's identity |
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
| NEW | catalog | 8 | 1 IN, 1 WF, 3 CC, 2 CT, 1 EV |
| EXTEND | catalog | 7 | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0, book_library_mgmt::RB_CATALOG_BINDINGS_V0, book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 |

---

## 16. Generation Provenance

*Every artifact this design schedules or amends is authored: construction renders each from the
registers above and it is its own source of truth. Nothing here is reached by invoking a
generator.*

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

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | p5_business_intent_book_library_mgmt_catalog_v0.md | COMPLETE |
| Stage 6 — Governance Intent | p6_governance_intent_book_library_mgmt_catalog_v0.md | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
| Stage 8 — Authoring Mandate | Pending | — |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes |
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary |
