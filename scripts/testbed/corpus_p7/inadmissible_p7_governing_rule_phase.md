# Stage 7 — Design Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_03_catalog
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
    - Decision: Registering a book announces three moments at one ending.
      Business Fact: An act announces every moment it completed.
      Resolution: §12 declares three `emit.EXIT_COMPLETED` rows against `WF_REGISTER_BOOK_V0`. Construction renders them as an ordered sequence; the platform seals that order and the runtime keeps it.
      Source Finding: 'S4 design_decisions #1'
    - Decision: The order announced is the order the business completes them.
      Business Fact: The order is normative and a reader of the account sees it.
      Resolution: The rows are read in document order — the work, then the book, then the physical copy — which is the order the act claims each identity.
      Source Finding: 'S4 design_decisions #2'
    - Decision: Each remaining act announces the one moment it completes.
      Business Fact: An act announces every moment it completed.
      Resolution: One `emit` row each. A sequence of one renders as a single name, which is what every act announcing elsewhere in the composition carries.
      Source Finding: 'S4 design_decisions #3'
    - Decision: Reinstatement announces nothing.
      Business Fact: Only moments the business already declared are announced.
      Resolution: Neither reinstatement act appears here. The business declares no moment for a reinstatement, and authoring one would be business content this design does not own.
      Source Finding: 'S4 design_decisions #4'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that registers a work, its first edition and that edition's first physical copy
      Reason: Announces the moments it completes, where it announced nothing. Everything else about it is restated unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that registers a further edition of a work the library already holds
      Reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that registers a further physical copy of an edition
      Reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that corrects what the library publishes about a book
      Reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that takes a book out of service
      Reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that takes a physical copy out of service
      Reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The actor whose authorization every catalog operation binds
      Reason: The actor every catalog act runs as. An EXTEND re-renders an act whole, so the design must state the actor it carries or the re-rendered act would carry none.
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - FQDN: book_library_mgmt::EV_WORK_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The moment announced by the act that completes it.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The moment announced by the act that completes it.
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - FQDN: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The moment announced by the act that completes it.
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - FQDN: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The moment announced by the act that completes it.
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - FQDN: book_library_mgmt::EV_BOOK_RETIRED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The moment announced by the act that completes it.
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - FQDN: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The moment announced by the act that completes it.
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - FQDN: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_RESOLVE_WORK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::IN_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: NONE IDENTIFIED
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): ''
      Code: ''
      Summary: ''
      Owner Subdomain: ''
      Status: ''
      Source Finding: ''
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REGISTER_BOOK_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every work the library has catalogued
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
  execution_topology:
    columns:
    - Workflow
    - Node
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
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
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_REGISTER_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_COPY_BARCODE_V0
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_REGISTER_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_REGISTER_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_REGISTER_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_BOOK_IDENTITY_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_RETIRE_BOOK_RECORD_V0
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RETIRE_BOOK_RECORD_V0
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_RETIRE_BOOK_RECORD_V0
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_RETIRE_BOOK_RECORD_V0
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_RETIRE_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_RETIRE_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_RETIRE_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_RETIRE_PHYSICAL_COPY_V0
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
    - CC Code: NONE IDENTIFIED
      Step: ''
      Step Name: ''
      Capability: ''
      Kind (CT, CS): ''
      Operation: ''
      Store: ''
      Consumes: ''
      Produces: ''
      Routing: ''
      Interpreted By: ''
      Semantic Status: ''
      Interface: ''
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
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
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology CC_CLAIM_COPY_BARCODE_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: copy_fields
      Bound To: payload.copy_fields
      Source Finding: S7 execution_topology CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REGISTER_PHYSICAL_COPY
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REGISTER_PHYSICAL_COPY'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.barcode''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_RESOLVE_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: updated_fields
      Bound To: payload.updated_fields
      Source Finding: S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: UPDATE_BIBLIOGRAPHIC_INFORMATION
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''UPDATE_BIBLIOGRAPHIC_INFORMATION'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_RETIRE_BOOK_RECORD_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: RETIRE_BOOK_RECORD
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''RETIRE_BOOK_RECORD'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology CC_RETIRE_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: RETIRE_PHYSICAL_COPY
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''RETIRE_PHYSICAL_COPY'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.barcode''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
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
    - Artifact: NONE IDENTIFIED
      Direction (INPUT, OUTPUT, ATTRIBUTE): ''
      Field: ''
      Type: ''
      Required (YES, NO): ''
      Default: ''
      Meaning: ''
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
    - CT Code: NONE IDENTIFIED
      Module: ''
      Callable: ''
      Operation: ''
      Kind (atom, molecule): ''
      Purity (ct_pure, ct_impure): ''
      Refusal (raises, returns, never): ''
      Source Finding: ''
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Group
    - Casing
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: NONE IDENTIFIED
      Extends: ''
      Group: ''
      Casing: ''
      Value: ''
      Meaning: ''
      Source Finding: ''
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows:
    - RB Code: NONE IDENTIFIED
      Capability: ''
      Key: ''
      Value: ''
      Source Finding: ''
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_WORK_REGISTERED_V0
      Source Finding: 'S4 design_decisions #2'
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Source Finding: 'S4 design_decisions #2'
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Source Finding: 'S4 design_decisions #2'
    - Artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Source Finding: S4 gap_register GAP-2
    - Artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Source Finding: S4 gap_register GAP-2
    - Artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Source Finding: S4 gap_register GAP-2
    - Artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BOOK_RETIRED_V0
      Source Finding: S4 gap_register GAP-2
    - Artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Source Finding: S4 gap_register GAP-2
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: NONE IDENTIFIED
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): ''
      Proposed Path: ''
      Used By: ''
      Source Finding: ''
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
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: catalog
      Count: '6'
      Artifacts: book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Count: '0'
      Artifacts: ''
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
  refusal_discharge:
    columns:
    - Operation
    - Refused When
    - Act
    - Step
    - Outcome
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Act: ''
      Step: ''
      Outcome: ''
      Source Finding: ''
  refusal_deferrals:
    columns:
    - Operation
    - Refused When
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Deferred To: ''
      Until: ''
      Source Finding: ''
  refusal_governance_discharge:
    columns:
    - Operation
    - Refused When
    - Phase
    - Governing Rule
    - Source Finding
    rows:
    - Operation: Announcing a moment
      Refused When: The act it names did not complete
      Phase: S7
      Governing Rule: EMISSION_NOT_FROM_COMPLETING_ENDING
      Source Finding: 'S0 operation_refusals #1'
  molecule_steps:
    columns:
    - CT Code
    - Step
    - Kind (atom, molecule, loop)
    - Target
    - Over
    - Iterator
    - Emits
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Step: ''
      Kind (atom, molecule, loop): ''
      Target: ''
      Over: ''
      Iterator: ''
      Emits: ''
      Source Finding: ''
  molecule_step_bindings:
    columns:
    - CT Code
    - Step
    - Role (INPUT, CARRY, UPDATE)
    - Field
    - Bound To
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Step: ''
      Role (INPUT, CARRY, UPDATE): ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  test_cases:
    columns:
    - CT Code
    - Case
    - Expected Outcome (SUCCESS, VIOLATION)
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Case: ''
      Expected Outcome (SUCCESS, VIOLATION): ''
      Source Finding: ''
  test_case_values:
    columns:
    - CT Code
    - Case
    - Role (INPUT, EXPECTED, ASSERT, RECORDED)
    - Field
    - Value
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Case: ''
      Role (INPUT, EXPECTED, ASSERT, RECORDED): ''
      Field: ''
      Value: ''
      Source Finding: ''
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows: []
```

HOW. Binding FQDNs are assigned here; business facts and placement decisions are not repeated.

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

---

## 17. Declared Reach

---

## 18. Refusal Discharge

---

## 19. Refusal Deferrals

---

## 20. Refusal — Governance-Surface Discharge

---

## 21. Molecule Steps

---

## 22. Molecule Step Bindings

---

## 23. Test Cases

---

## 24. Test Case Values

---

## 25. Withdrawn Facts

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
