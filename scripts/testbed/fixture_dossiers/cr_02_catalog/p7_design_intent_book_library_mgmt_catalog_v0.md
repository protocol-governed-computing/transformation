# Design Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_02_catalog
  Status: DRAFT
  Feeds: Stage 8 — Authoring Mandate
registers:
  design_resolution:
    columns:
    - Decision
    - Business Fact
    - Resolution
    - Source Finding
    rows:
    - Decision: The record the previous change calls a book is an edition; the work is added above it
      Business Fact: Editions of one work share a title and an author and differ by publication year
      Resolution: No existing identity changes. A work store and a work identity registry are added, and the edition record gains the key of the work it belongs to
      Source Finding: 'S4 design_decisions #1'
    - Decision: The work's identity is formed by a new transform
      Business Fact: The edition key transform is reached by every catalog operation and 23 artifacts depend on it
      Resolution: A second transform forms the work key from title and author; the two are independent and neither can alter the other
      Source Finding: 'S4 design_decisions #2'
    - Decision: The work is claimed through the same registry mechanism the edition is claimed through
      Business Fact: Register-if-absent gives the atomic uniqueness a work identity needs
      Resolution: A registry store claims the work key; a claim that finds the key already held yields ALREADY_EXISTS, which the registration treats as the work having been found rather than as a refusal
      Source Finding: 'S4 design_decisions #3'
    - Decision: The work store and the work identity registry are declared in the catalog's own storage declaration
      Business Fact: A subdomain declares its stores once and binds them once
      Resolution: Both stores are added to the existing storage declaration and reached through the existing runtime binding
      Source Finding: 'S4 design_decisions #4'
    - Decision: Registering an edition of a new work extends the existing registration; registering an additional edition is a new operation
      Business Fact: The existing registration creates the work and requires a first copy; an additional edition does neither
      Resolution: The existing workflow gains a work claim before its claims; a second workflow resolves an existing work and claims only the edition
      Source Finding: 'S4 design_decisions #5'
    - Decision: The work claim is placed among the existing claims, before any write
      Business Fact: A refused registration must leave nothing behind
      Resolution: The work claim runs after validation and before the edition and barcode claims, so every claim still precedes every write
      Source Finding: 'S4 design_decisions #6'
    - Decision: Search is extended rather than duplicated, and answers at the level of the work
      Business Fact: Two searches would leave staff choosing which one answers their question
      Resolution: The existing search gains a grouping step after its selection step; the search terms and the records it selects are unchanged
      Source Finding: 'S4 design_decisions #7'
    - Decision: Retrieval stays edition retrieval and carries a summary of the work
      Business Fact: The business asked for one retrieval carrying a summary, not a second operation
      Resolution: The existing retrieval gains a read of the work record; the edition and its copies are assembled as before
      Source Finding: 'S4 design_decisions #8'
    - Decision: A work is never retired
      Business Fact: A work whose editions are all retired is simply that
      Resolution: No retirement operation names the work, and no routing reaches the work store from a retirement
      Source Finding: 'S4 design_decisions #9'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Declares the stores the catalog owns and the paths they occupy
      Reason: Gains the work record store and the work identity registry alongside the five stores the catalog already owns
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - FQDN: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Binds the catalog's workflows to the stores and mechanisms they use
      Reason: Binds the new workflow to the same substrates and the same storage declaration the catalog already uses
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Registers a work with its first edition and that edition's first physical copy
      Reason: 'Gains one node: the work claim, placed after validation and before every other claim'
      Source Finding: S6 ownership Register an edition of a work the catalog does not yet hold
    - FQDN: book_library_mgmt::CC_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Validates, assembles and writes an edition record against the work it belongs to
      Reason: The edition record it assembles now carries the key of the work the edition belongs to
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CC_REGISTER_BOOK_V0
    - FQDN: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Confirms a registration carries what a work and an edition require, before any identity is claimed
      Reason: Confirms the submission carries what a work requires as well as what an edition requires
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - FQDN: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Selects the registered editions matching a subject or title and groups them under their work
      Reason: Groups the matching editions under the work they belong to, so the answer is one result per work
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CC_SEARCH_CATALOG_V0
    - FQDN: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Assembles an edition, the physical copies of it, and the record of the work it belongs to
      Reason: Reads the work record so the retrieval carries a summary of the work the edition belongs to
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    - FQDN: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The actor every catalog workflow runs as, including the one this change adds — authorization is read from what the caller supplies and granted nowhere
      Source Finding: S6 ownership Confirm the staff member performing an operation is authorized
    - FQDN: book_library_mgmt::IN_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The registration's entry point is unchanged — what a caller supplies is what it supplied before, and only the sequence it starts gains a node
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CC_REGISTER_BOOK_V0
    - FQDN: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: ''
      Reason: Examined and deliberately not widened; it continues to form the edition key from three attributes
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    - FQDN: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Claims the edition's identity unchanged, and is the precedent the work claim follows
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - FQDN: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Every operation this change adds reaches it first, as every existing operation does
      Source Finding: S6 ownership Confirm the staff member performing an operation is authorized
    - FQDN: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Records the operations this change adds into the trail it already appends to
      Source Finding: S6 ownership Record every performed operation in the catalog's audit trail
    - FQDN: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: A copy already belongs to exactly one record, and that record is an edition
      Source Finding: S6 ownership Register a physical copy against exactly one edition
    - FQDN: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Barcode uniqueness is unaffected by the work abstraction
      Source Finding: S6 ownership Register a physical copy against exactly one edition
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Holds the work record as it holds the edition and copy records
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_MUTABLE_JSON_V0
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Claims the work key as it claims the edition key and the barcode
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_REGISTRY_V0
    - FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Appends the operations this change adds to the catalog's trail
      Source Finding: S6 storage_governance An unamendable trail of every operation performed
    - FQDN: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: ''
      Reason: Examined and not extended; it selects records and the grouping is a separate transform
      Source Finding: S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_FILTER_RECORDS_V0
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Assembles the work record as it assembles the edition and copy records
      Source Finding: S6 storage_governance A durable record of every work the library has catalogued
    - FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Confirms a submission carries the fields its schema declares, for the work as for the edition
      Source Finding: S6 ownership Validate that a registration carries what a work and an edition require
    - FQDN: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Compares two values for equality, unchanged — the update uses it to confirm an edition's identity did not change
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Turns a validation result into a refusal, unchanged
      Source Finding: S6 ownership Validate that a registration carries what a work and an edition require
    - FQDN: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Changes a registered edition's descriptive content and refuses a change that would duplicate another edition
      Reason: The record it writes back now carries the work the edition belongs to, which it previously dropped
      Source Finding: S6 pps_artifacts_requiring_action book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: Form the identifying key of a work from its title and author
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CT
      Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Summary: Forms the single key claimed for a work from its title and author
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    - Capability: Select records matching criteria, answering none when none match
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CT
      Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Summary: Selects the records matching stated criteria and returns none when none match
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_SELECT_RECORDS_V0
    - Capability: Group selected records by an attribute they share
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CT
      Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Summary: Groups records by the value of a named attribute, returning one group per distinct value
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CT_PURE_GROUP_RECORDS_V0
    - Capability: Claim a work's identity so that two registrations of one work do not produce two works
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Summary: Forms the work key, claims it, and writes the work record when the claim is new
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_CLAIM_WORK_IDENTITY_V0
    - Capability: Resolve the work an edition belongs to
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_RESOLVE_WORK_V0
      Summary: Forms the work key, resolves it against the registry, and reads the work record it names
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_RESOLVE_WORK_V0
    - Capability: Register an additional edition of an existing work
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Summary: Assembles the edition record against a resolved work and writes it
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_REGISTER_ADDITIONAL_EDITION_V0
    - Capability: Admit a request to register an additional edition of an existing work
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Summary: A request to register a further edition of a work the catalog already holds
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_REGISTER_ADDITIONAL_EDITION_V0
    - Capability: Register an additional edition of an existing work
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Summary: The governed sequence that registers a further edition of an existing work
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_REGISTER_ADDITIONAL_EDITION_V0
    - Capability: Recognise the moment a work enters the catalog
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: book_library_mgmt::EV_WORK_REGISTERED_V0
      Summary: The moment a work enters the catalog, created by the edition that evidences it
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes EV_WORK_REGISTERED_V0
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every work the library has catalogued
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REGISTER_BOOK_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance An atomic claim on each work's identity
  execution_topology:
    columns:
    - Workflow
    - Node
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_REGISTER_ADDITIONAL_EDITION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RESOLVE_WORK_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_VALIDATE_BOOK_SUBMISSION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_RESOLVE_WORK_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RESOLVE_WORK_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_CLAIM_BOOK_IDENTITY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_REGISTER_ADDITIONAL_EDITION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::IN_REGISTER_BOOK_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 existing_inventory WF_REGISTER_BOOK_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_VALIDATE_BOOK_SUBMISSION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; ALREADY_EXISTS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_WORK_IDENTITY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_CLAIM_BOOK_IDENTITY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_BOOK_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_CLAIM_COPY_BARCODE_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_REGISTER_BOOK_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_REGISTER_BOOK_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_REGISTER_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_REGISTER_BOOK_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_REGISTER_BOOK_V0
  cc_composition:
    columns:
    - CC Code
    - Step
    - Step Name
    - Capability
    - Kind (CT, CS)
    - Operation
    - Store
    - Consumes
    - Produces
    - Routing
    - Interpreted By
    - Semantic Status
    - Interface
    rows:
    - CC Code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: '1'
      Step Name: form_work_key
      Capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Kind (CT, CS): CT
      Operation: FORM_WORK_IDENTITY_KEY
      Store: —
      Consumes: title, author
      Produces: work_key
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: title=title, author=author; out: work_key=work_key'
    - CC Code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: '2'
      Step Name: claim_work
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: WORK_IDENTITY_REGISTRY
      Consumes: key, target_cs, target_ref
      Produces: address
      Routing: SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: ALREADY_EXISTS
      Interface: —
    - CC Code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: '3'
      Step Name: assemble_work_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: work_fields
      Produces: work_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=work_fields; out: record=work_record'
    - CC Code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: '4'
      Step Name: write_work_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: WORKS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: '1'
      Step Name: form_work_key
      Capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Kind (CT, CS): CT
      Operation: FORM_WORK_IDENTITY_KEY
      Store: —
      Consumes: title, author
      Produces: work_key
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: title=title, author=author; out: work_key=work_key'
    - CC Code: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: '2'
      Step Name: resolve_work_claim
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: RESOLVE
      Store: WORK_IDENTITY_REGISTRY
      Consumes: key_or_address
      Produces: target_ref
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: '3'
      Step Name: read_work_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: WORKS
      Consumes: key
      Produces: value
      Routing: SUCCESS -> exit; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: '1'
      Step Name: validate_edition_fields
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: edition_fields, edition_schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=edition_fields, schema=edition_schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: '2'
      Step Name: assemble_edition_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: edition_fields
      Produces: edition_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=edition_fields; out: record=edition_record'
    - CC Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: '3'
      Step Name: write_edition_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: BOOKS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: '1'
      Step Name: form_work_key
      Capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Kind (CT, CS): CT
      Operation: FORM_WORK_IDENTITY_KEY
      Store: —
      Consumes: title, author
      Produces: work_key
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: title=title, author=author; out: work_key=work_key'
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: '2'
      Step Name: validate_book_fields
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: book_fields, book_schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=book_fields, schema=book_schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: '3'
      Step Name: assemble_book_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: book_fields
      Produces: book_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=book_fields; out: record=book_record'
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: '4'
      Step Name: write_book_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: BOOKS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: '1'
      Step Name: validate_book_fields
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: book_fields, book_schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=book_fields, schema=book_schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: '2'
      Step Name: validate_work_fields
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: work_fields, work_schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=work_fields, schema=work_schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: '3'
      Step Name: require_submission_complete
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: barcode, book_fields
      Produces: valid
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=barcode, rules=rules; out: valid=valid'
    - CC Code: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: '1'
      Step Name: select_book_records
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: SELECT
      Store: BOOKS
      Consumes: —
      Produces: records
      Routing: SUCCESS -> continue; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: '2'
      Step Name: select_matching_books
      Capability: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Kind (CT, CS): CT
      Operation: FILTER_RECORDS
      Store: —
      Consumes: records, search_criteria
      Produces: matching_books
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: source=records, filter=search_criteria; out: extracted=matching_books'
    - CC Code: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: '3'
      Step Name: group_editions_by_work
      Capability: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Kind (CT, CS): CT
      Operation: GROUP_RECORDS
      Store: —
      Consumes: matching_books, group_by
      Produces: matching_works
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: source=matching_books, attribute=group_by; out: grouped=matching_works'
    - CC Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: '1'
      Step Name: read_book_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: BOOKS
      Consumes: key
      Produces: value
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: '2'
      Step Name: form_work_key
      Capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Kind (CT, CS): CT
      Operation: FORM_WORK_IDENTITY_KEY
      Store: —
      Consumes: title, author
      Produces: work_key
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: title=title, author=author; out: work_key=work_key'
    - CC Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: '3'
      Step Name: read_work_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: WORKS
      Consumes: key
      Produces: value
      Routing: SUCCESS -> continue; NOT_FOUND -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: '4'
      Step Name: select_copy_records
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: SELECT
      Store: PHYSICAL_COPIES
      Consumes: —
      Produces: records
      Routing: SUCCESS -> continue; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: '5'
      Step Name: select_copies_of_book
      Capability: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Kind (CT, CS): CT
      Operation: SELECT_RECORDS
      Store: —
      Consumes: records, copy_criteria
      Produces: copies_held
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: source=records, filter=copy_criteria; out: extracted=copies_held'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '1'
      Step Name: read_book_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: BOOKS
      Consumes: key
      Produces: book_record
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: NOT_FOUND
      Interface: —
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '2'
      Step Name: form_updated_identity_key
      Capability: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Kind (CT, CS): CT
      Operation: FORM_BOOK_IDENTITY_KEY
      Store: —
      Consumes: updated_fields
      Produces: updated_identity_key
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: title=title, author=author, publication_year=publication_year; out: identity_key=updated_identity_key'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '3'
      Step Name: compare_identity
      Capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
      Kind (CT, CS): CT
      Operation: COMPARE_EQUAL
      Store: —
      Consumes: identity_key, updated_identity_key
      Produces: identity_unchanged
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: left=identity_key, right=updated_identity_key; out: is_equal=identity_unchanged'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '4'
      Step Name: require_identity_unchanged
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: identity_unchanged
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=identity_unchanged, rules=rules; out: valid=valid'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '5'
      Step Name: assemble_updated_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: updated_fields
      Produces: updated_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=updated_fields; out: record=updated_record'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '6'
      Step Name: write_updated_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: BOOKS
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: inputs.title
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: inputs.author
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): OUTPUT
      Field: work_key
      Bound To: capability_result.work_key
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: claim_work
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: results.form_work_key.work_key
      Source Finding: S7 cc_composition claim_work
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: claim_work
      Direction (INPUT, OUTPUT): INPUT
      Field: target_cs
      Bound To: CS_MUTABLE_JSON_V0
      Source Finding: S7 cc_composition claim_work
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: claim_work
      Direction (INPUT, OUTPUT): INPUT
      Field: target_ref
      Bound To: WORKS
      Source Finding: S7 cc_composition claim_work
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: claim_work
      Direction (INPUT, OUTPUT): OUTPUT
      Field: address
      Bound To: capability_result.address
      Source Finding: S7 cc_composition claim_work
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: claim_work
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition claim_work
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: assemble_work_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: inputs.work_fields
      Source Finding: S7 cc_composition assemble_work_record
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: assemble_work_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: work_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_work_record
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: write_work_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: results.form_work_key.work_key
      Source Finding: S7 cc_composition write_work_record
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: write_work_record
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_work_record.work_record
      Source Finding: S7 cc_composition write_work_record
    - Owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Step: write_work_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_work_record
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: inputs.title
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: inputs.author
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): OUTPUT
      Field: work_key
      Bound To: capability_result.work_key
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: resolve_work_claim
      Direction (INPUT, OUTPUT): INPUT
      Field: key_or_address
      Bound To: results.form_work_key.work_key
      Source Finding: S7 cc_composition resolve_work_claim
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: resolve_work_claim
      Direction (INPUT, OUTPUT): OUTPUT
      Field: target_ref
      Bound To: capability_result.target_ref
      Source Finding: S7 cc_composition resolve_work_claim
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: resolve_work_claim
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition resolve_work_claim
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: read_work_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: results.form_work_key.work_key
      Source Finding: S7 cc_composition read_work_record
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: read_work_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: work_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_work_record
    - Owner: book_library_mgmt::CC_RESOLVE_WORK_V0
      Step: read_work_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_work_record
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: validate_edition_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.edition_fields
      Source Finding: S7 cc_composition validate_edition_fields
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: validate_edition_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: schema
      Bound To: inputs.edition_schema
      Source Finding: S7 cc_composition validate_edition_fields
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: validate_edition_fields
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_edition_fields
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: assemble_edition_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: inputs.edition_fields
      Source Finding: S7 cc_composition assemble_edition_record
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: assemble_edition_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: edition_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_edition_record
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: write_edition_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition write_edition_record
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: write_edition_record
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_edition_record.edition_record
      Source Finding: S7 cc_composition write_edition_record
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: write_edition_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_edition_record
    - Owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: select_book_records
      Direction (INPUT, OUTPUT): OUTPUT
      Field: records
      Bound To: capability_result.records
      Source Finding: S7 cc_composition select_book_records
    - Owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: select_book_records
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition select_book_records
    - Owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: select_matching_books
      Direction (INPUT, OUTPUT): INPUT
      Field: source
      Bound To: results.select_book_records.records
      Source Finding: S7 cc_composition select_matching_books
    - Owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: select_matching_books
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: inputs.search_criteria
      Source Finding: S7 cc_composition select_matching_books
    - Owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: select_matching_books
      Direction (INPUT, OUTPUT): OUTPUT
      Field: matching_books
      Bound To: capability_result.extracted
      Source Finding: S7 cc_composition select_matching_books
    - Owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: group_editions_by_work
      Direction (INPUT, OUTPUT): INPUT
      Field: source
      Bound To: results.select_matching_books.matching_books
      Source Finding: S7 cc_composition group_editions_by_work
    - Owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: group_editions_by_work
      Direction (INPUT, OUTPUT): INPUT
      Field: attribute
      Bound To: work_key
      Source Finding: S7 cc_composition group_editions_by_work
    - Owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Step: group_editions_by_work
      Direction (INPUT, OUTPUT): OUTPUT
      Field: matching_works
      Bound To: capability_result.grouped
      Source Finding: S7 cc_composition group_editions_by_work
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: value
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: results.read_book_record.value.title
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: results.read_book_record.value.author
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): OUTPUT
      Field: work_key
      Bound To: capability_result.work_key
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_work_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: results.form_work_key.work_key
      Source Finding: S7 cc_composition read_work_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_work_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: work_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_work_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copy_records
      Direction (INPUT, OUTPUT): OUTPUT
      Field: records
      Bound To: capability_result.records
      Source Finding: S7 cc_composition select_copy_records
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copies_of_book
      Direction (INPUT, OUTPUT): INPUT
      Field: source
      Bound To: results.select_copy_records.records
      Source Finding: S7 cc_composition select_copies_of_book
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copies_of_book
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: inputs.copy_criteria
      Source Finding: S7 cc_composition select_copies_of_book
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copies_of_book
      Direction (INPUT, OUTPUT): OUTPUT
      Field: copies_held
      Bound To: capability_result.extracted
      Source Finding: S7 cc_composition select_copies_of_book
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: validate_work_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.work_fields
      Source Finding: S7 cc_composition validate_work_fields
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: validate_work_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: schema
      Bound To: inputs.work_schema
      Source Finding: S7 cc_composition validate_work_fields
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: validate_work_fields
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_work_fields
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: inputs.book_fields.title
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: inputs.book_fields.author
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: form_work_key
      Direction (INPUT, OUTPUT): OUTPUT
      Field: work_key
      Bound To: capability_result.work_key
      Source Finding: S7 cc_composition form_work_key
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: assemble_book_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''title'': ''$.inputs.book_fields.title'', ''author'': ''$.inputs.book_fields.author'', ''publication_year'': ''$.inputs.book_fields.publication_year'', ''subject'': ''$.inputs.book_fields.subject'', ''state'': ''$.inputs.book_fields.state'', ''work_key'': ''$.results.form_work_key.work_key''}'
      Source Finding: S7 cc_composition assemble_book_record
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: assemble_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: book_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_book_record
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_fields
      Bound To: payload.edition_fields
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_schema
      Bound To: payload.edition_schema
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: work_fields
      Bound To: payload.work_fields
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: work_schema
      Bound To: payload.work_schema
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology CC_RESOLVE_WORK_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology CC_RESOLVE_WORK_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: publication_year
      Bound To: payload.publication_year
      Source Finding: S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
      Source Finding: S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: edition_schema
      Bound To: payload.edition_schema
      Source Finding: S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: edition_fields
      Bound To: '{''identity_key'': ''$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key'', ''title'': ''$.payload.title'', ''author'': ''$.payload.author'', ''publication_year'': ''$.payload.publication_year'', ''subject'': ''$.payload.subject'', ''state'': ''REGISTERED'', ''work_key'': ''$.results.CC_RESOLVE_WORK_V0.work_key''}'
      Source Finding: S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REGISTER_ADDITIONAL_EDITION
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REGISTER_ADDITIONAL_EDITION'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology CC_CLAIM_WORK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology CC_CLAIM_WORK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: work_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author''}'
      Source Finding: S7 execution_topology CC_CLAIM_WORK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: work_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author''}'
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: work_schema
      Bound To: '{''required'': [''title'', ''author'']}'
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author'', ''publication_year'': ''$.payload.publication_year'', ''subject'': ''$.payload.subject'', ''state'': ''REGISTERED''}'
      Source Finding: S7 execution_topology CC_REGISTER_BOOK_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_fields
      Bound To: payload.book_fields
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_schema
      Bound To: payload.book_schema
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: publication_year
      Bound To: payload.publication_year
      Source Finding: S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
      Source Finding: S7 execution_topology CC_REGISTER_BOOK_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_schema
      Bound To: payload.book_schema
      Source Finding: S7 execution_topology CC_REGISTER_BOOK_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology CC_CLAIM_COPY_BARCODE_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
      Source Finding: S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: copy_fields
      Bound To: payload.copy_fields
      Source Finding: S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REGISTER_BOOK
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REGISTER_BOOK'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.title''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.book_fields
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: schema
      Bound To: inputs.book_schema
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: require_submission_complete
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''barcode'': ''$.inputs.barcode'', ''subject'': ''$.inputs.book_fields.subject''}'
      Source Finding: S7 cc_composition require_submission_complete
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: require_submission_complete
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''barcode'', ''op'': ''neq'', ''value'': ''''}, {''field'': ''subject'', ''op'': ''neq'', ''value'': []}]'
      Source Finding: S7 cc_composition require_submission_complete
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: require_submission_complete
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_submission_complete
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.book_fields
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: schema
      Bound To: inputs.book_schema
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: write_book_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition write_book_record
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: write_book_record
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_book_record.book_record
      Source Finding: S7 cc_composition write_book_record
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: write_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_book_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: book_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copy_records
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition select_copy_records
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copies_of_book
      Direction (INPUT, OUTPUT): INPUT
      Field: source
      Bound To: results.select_copy_records.records
      Source Finding: S7 cc_composition select_copies_of_book
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copies_of_book
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: inputs.copy_criteria
      Source Finding: S7 cc_composition select_copies_of_book
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copies_of_book
      Direction (INPUT, OUTPUT): OUTPUT
      Field: copies_held
      Bound To: capability_result.extracted
      Source Finding: S7 cc_composition select_copies_of_book
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: book_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: form_updated_identity_key
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: inputs.updated_fields.title
      Source Finding: S7 cc_composition form_updated_identity_key
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: form_updated_identity_key
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: inputs.updated_fields.author
      Source Finding: S7 cc_composition form_updated_identity_key
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: form_updated_identity_key
      Direction (INPUT, OUTPUT): INPUT
      Field: publication_year
      Bound To: inputs.updated_fields.publication_year
      Source Finding: S7 cc_composition form_updated_identity_key
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: form_updated_identity_key
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_identity_key
      Bound To: capability_result.identity_key
      Source Finding: S7 cc_composition form_updated_identity_key
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: compare_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: left
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition compare_identity
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: compare_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: right
      Bound To: results.form_updated_identity_key.updated_identity_key
      Source Finding: S7 cc_composition compare_identity
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: compare_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: identity_unchanged
      Bound To: capability_result.is_equal
      Source Finding: S7 cc_composition compare_identity
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: require_identity_unchanged
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''identity_unchanged'': ''$.results.compare_identity.identity_unchanged''}'
      Source Finding: S7 cc_composition require_identity_unchanged
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: require_identity_unchanged
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''identity_unchanged'', ''op'': ''eq'', ''value'': True}]'
      Source Finding: S7 cc_composition require_identity_unchanged
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: require_identity_unchanged
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_identity_unchanged
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: assemble_updated_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''title'': ''$.inputs.updated_fields.title'', ''author'': ''$.inputs.updated_fields.author'', ''publication_year'': ''$.inputs.updated_fields.publication_year'', ''subject'': ''$.inputs.updated_fields.subject'', ''state'': ''$.inputs.updated_fields.state'', ''work_key'': ''$.results.read_book_record.book_record.work_key''}'
      Source Finding: S7 cc_composition assemble_updated_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: assemble_updated_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_updated_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: write_updated_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition write_updated_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: write_updated_record
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_updated_record.updated_record
      Source Finding: S7 cc_composition write_updated_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: write_updated_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_updated_record
  interface_fields:
    columns:
    - Artifact
    - Direction (INPUT, OUTPUT, ATTRIBUTE)
    - Field
    - Type
    - Required (YES, NO)
    - Default
    - Meaning
    rows:
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The title of the work the edition belongs to, and of the edition itself
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The author of the work the edition belongs to
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: publication_year
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The year that distinguishes this edition from the work's other editions
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: subject
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What kind of material the edition is, as free text
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: edition_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The edition's descriptive content as submitted
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: edition_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields an edition record is required to carry
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: work_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work's identifying attributes as submitted
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: work_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields a work record is required to carry
    - Artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work's title, compared without regard to letter case or repeated spacing
    - Artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work's author, compared the same way
    - Artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: work_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The single key claimed for the work
    - Artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: source
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The records to select from
    - Artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: filter
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The criteria a record must match on every key
    - Artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: extracted
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The records that matched, possibly none
    - Artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: source
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The records to group
    - Artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: attribute
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The attribute whose value decides which group a record belongs to
    - Artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: grouped
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: One group per distinct value, each carrying the records that share it
    - Artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work's title
    - Artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work's author
    - Artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: work_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work record's content, written when the claim is new
    - Artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: work_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key claimed for the work, whether the claim was new or already held
    - Artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The title of the work to resolve
    - Artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The author of the work to resolve
    - Artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: work_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key of the work that was resolved
    - Artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: work_record
      Type: object
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The work record the key names, when the work exists
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The edition's claimed identity, which is the key its record occupies
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: edition_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The edition record's content, including the key of the work it belongs to
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: edition_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields an edition record is required to carry
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: edition_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The edition record as written
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: work_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work's identifying attributes, validated alongside the edition's
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: work_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields a work record is required to carry
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: valid
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the submission may proceed to be claimed and written
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: book_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The edition's authoritative record, carrying the key of the work it belongs to
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The edition record's content, now including the key of the work it belongs to
    - Artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: matching_works
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: One entry per matching work, each carrying the editions of it that matched
    - Artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: work_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The record of the work the edition belongs to — its title and author — so the work need not be looked up separately
    - Artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: work_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work that entered the catalog
    - Artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work's title
    - Artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The work's author
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The book's bibliographic information
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields a book record must carry, as the rules its structure is validated against
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: The barcode the library assigned to the copy, when the registration carries one — an additional edition of an existing work does not
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields a book record must carry, as the rules its structure is validated against
    - Artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: search_criteria
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What staff are searching by, and the states to include
    - Artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: matching_books
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The registered books matching what was searched for
    - Artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: copy_criteria
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Which copies belong to the book being retrieved
    - Artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: book_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The book's authoritative record
    - Artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: copies_held
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The copies the library holds of the book
    - Artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: updated_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The changed bibliographic information
    - Artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: book_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The book's authoritative record
  implementation_bindings:
    columns:
    - CT Code
    - Module
    - Callable
    - Operation
    - Kind (atom, molecule)
    - Purity (ct_pure, ct_impure)
    - Refusal (raises, returns, never)
    - Source Finding
    rows:
    - CT Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Module: book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_form_work_identity_key_v0
      Callable: execute
      Operation: PURE_FORM_WORK_IDENTITY_KEY
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): never
      Source Finding: S7 new_artifacts CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    - CT Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Module: book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_select_records_v0
      Callable: execute
      Operation: PURE_SELECT_RECORDS
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): never
      Source Finding: S7 new_artifacts CT_PURE_SELECT_RECORDS_V0
    - CT Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Module: book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_group_records_v0
      Callable: execute
      Operation: PURE_GROUP_RECORDS
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): never
      Source Finding: S7 new_artifacts CT_PURE_GROUP_RECORDS_V0
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Group
    - Casing
    - Value
    - Meaning
    - Source Finding
    rows: []
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows:
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Key: structure
      Value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S7 rb_declarations RB_CATALOG_BINDINGS_V0
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Capability: capability_side_effects::CS_REGISTRY_V0
      Key: structure
      Value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S7 rb_declarations RB_CATALOG_BINDINGS_V0
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Key: structure
      Value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S7 rb_declarations RB_CATALOG_BINDINGS_V0
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
      Property: type
      Value: BUSINESS_MOMENT
      Source Finding: S5 provisional_codes EV_WORK_REGISTERED_V0
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: WORKS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_MUTABLE_JSON_V0
      Proposed Path: book_library_mgmt/catalog/works.json
      Used By: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Source Finding: S6 storage_governance A durable record of every work the library has catalogued
    - Store Name: WORK_IDENTITY_REGISTRY
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: book_library_mgmt/catalog/work_identity_registry.jsonl
      Used By: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Source Finding: S6 storage_governance An atomic claim on each work's identity
    - Store Name: BOOKS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_MUTABLE_JSON_V0
      Proposed Path: book_library_mgmt/catalog/books.json
      Used By: book_library_mgmt::CC_REGISTER_BOOK_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
    - Store Name: PHYSICAL_COPIES
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_MUTABLE_JSON_V0
      Proposed Path: book_library_mgmt/catalog/physical_copies.json
      Used By: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Source Finding: S6 storage_governance A durable record of every physical copy the library owns
    - Store Name: CATALOG_OPERATIONS
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_APPENDONLY_JSONL_V0
      Proposed Path: book_library_mgmt/catalog/catalog_operations.jsonl
      Used By: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Source Finding: S6 storage_governance A trail of performed operations that cannot be amended
    - Store Name: BOOK_IDENTITY_REGISTRY
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: book_library_mgmt/catalog/book_identity_registry.jsonl
      Used By: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Source Finding: S6 storage_governance A claim on each book's identity, held once
    - Store Name: COPY_BARCODE_REGISTRY
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): CS_REGISTRY_V0
      Proposed Path: book_library_mgmt/catalog/copy_barcode_registry.jsonl
      Used By: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Source Finding: S6 storage_governance A claim on each copy's barcode, held once
  transport_bindings:
    columns:
    - Artifact
    - Direction (INGRESS, EGRESS)
    - Operation
    - Handler Kind (WF_INVOCATION, SNAPSHOT_READ)
    - Handler Target
    - Field
    - Bound To
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Direction (INGRESS, EGRESS): ''
      Operation: ''
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): ''
      Handler Target: ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Count: '8'
      Artifacts: 1 IN, 1 WF, 3 CC, 2 CT, 1 EV
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: catalog
      Count: '7'
      Artifacts: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0, book_library_mgmt::RB_CATALOG_BINDINGS_V0, book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Generator: ''
      Generator Sources: ''
      Source Finding: ''
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: NONE IDENTIFIED
      Consults: ''
      Source Finding: ''
  test_cases:
    columns:
    - CT Code
    - Case
    - Expected Outcome (SUCCESS, VIOLATION)
    - Source Finding
    rows:
    - CT Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Case: selects_matching_records
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Case: groups_by_attribute
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
  test_case_values:
    columns:
    - CT Code
    - Case
    - Role (INPUT, EXPECTED, ASSERT, RECORDED)
    - Field
    - Value
    - Source Finding
    rows:
    - CT Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: title
      Value: The Odyssey
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: author
      Value: Homer
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: work_key
      Value: the odyssey|homer
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Case: selects_matching_records
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: source
      Value: '[{author: Homer, title: Iliad}, {author: Virgil, title: Aeneid}]'
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Case: selects_matching_records
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: filter
      Value: '{author: Homer}'
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
      Case: selects_matching_records
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: extracted
      Value: '[{author: Homer, title: Iliad}]'
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Case: groups_by_attribute
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: source
      Value: '[{work: w1, edition: 1}, {work: w2, edition: 1}, {work: w1, edition: 2}]'
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Case: groups_by_attribute
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: attribute
      Value: work
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
      Case: groups_by_attribute
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: grouped
      Value: '[{key: w1, records: [{work: w1, edition: 1}, {work: w1, edition: 2}]}, {key: w2, records: [{work: w2, edition: 1}]}]'
      Source Finding: human decision
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows: []
```

Eight artifacts are authored and six existing ones are extended. The extended six carry identities
the composition already holds, so they are inventoried rather than assigned — a design that assigned
them again would create a second artifact under the same name.

---

## 1. Design Decisions Resolution

---

## 2. Artifact Inventory — Existing Artifacts

---

## 3. Artifact Family Mapping — New Artifacts

---

## 4. Runtime Binding (RB) Declarations

---

## 5. Execution Topology

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Implementation Bindings

---

## 10. Vocabulary Extensions

---

## 11. Runtime Policies

---

## 12. Artifact Properties

---

## 13. STRUCTURE Stores

---

## 14. Transport Bindings

## 15. Artifact Summary

---

## 16. Generation Provenance

*Every artifact this design schedules or amends is authored: construction renders each from the
registers above and it is its own source of truth. Nothing here is reached by invoking a
generator.*

---

## 17. Declared Reach

---

## 23. Test Cases

---

## 24. Test Case Values

---

## 25. Withdrawn Facts

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
