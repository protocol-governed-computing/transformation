# Stage 7 — Design Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_05_catalog
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
    - Decision: Each rule is held by the step that applies it
      Business Fact: A rule the caller supplies is a rule the caller can widen
      Resolution: The confirming contract holds the library's authorization rules; the checking contracts hold the book, work and edition descriptions
      Source Finding: 'S4 design_decisions #1'
    - Decision: Each check is followed by a rule refusing when it found anything
      Business Fact: An incomplete registration is refused
      Resolution: The submission check refuses on both its checks' violations; the book record, the edition record and the correction each gain a rule step requiring none
      Source Finding: 'S4 design_decisions #2'
    - Decision: What each registration checks is the record it writes
      Business Fact: A check of a supplied copy judges nothing that is written
      Resolution: Each registration act hands its submission check the fields it records
      Source Finding: 'S4 design_decisions #3'
    - Decision: The register act records the subject where callers send it
      Business Fact: Every present caller sends it inside the book details
      Resolution: The recorded book's subject is bound from the supplied book details
      Source Finding: 'S4 design_decisions #4'
    - Decision: A copy's registered state and a correction's state are the catalog's own
      Business Fact: A copy is registered as registered; a correction does not change state
      Resolution: The copy contract writes REGISTERED; the correction writes the state it read and checks the corrected record
      Source Finding: 'S4 design_decisions #5'
    - Decision: The gates stop requiring what the catalog holds and what no act reads
      Business Fact: A gate requiring an unread field refuses a correct request
      Resolution: Every gate drops the rules; the book gate its description; the edition gate its descriptions and supplied details
      Source Finding: 'S4 design_decisions #6'
    - Decision: Records made before this change are left as they are
      Business Fact: The record is added to and never rewritten
      Resolution: No migration, backfill or repair step is designed
      Source Finding: 'S4 design_decisions #7'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Confirm the staff member may perform catalog operations
      Reason: It takes its rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Confirms a registration carries what a work and an edition require, before any identity is claimed
      Reason: It takes its descriptions from the request and refuses nothing its checks find.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: book_library_mgmt::CC_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Validates, assembles and writes an edition record against the work it belongs to
      Reason: It takes its description from the request and ignores what its check finds.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Assembles the edition record against a resolved work and writes it
      Reason: It takes its description from the request and ignores what its check finds.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Record a copy against exactly one book
      Reason: It records the copy in the state the request gives.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Changes a registered edition's descriptive content and refuses a change that would duplicate another edition
      Reason: It writes the state the request gives and checks no description.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that registers a work, its first edition and that edition's first physical copy
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that registers a further edition of a work the library already holds
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - FQDN: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that registers a further physical copy of an edition
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Corrects what the library publishes about a registered book
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - FQDN: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that takes a book out of service
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - FQDN: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Returning a retired book record to the registered state
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - FQDN: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The governed sequence that takes a physical copy out of service
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - FQDN: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Returning a retired copy to the registered state
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - FQDN: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Assembling a book with the copies the library holds of it
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - FQDN: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Searching by subject or title, excluding retired books
      Reason: It binds the rules from the request.
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
    - FQDN: book_library_mgmt::IN_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to register a book together with its first physical copy
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #17'
    - FQDN: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The boundary that admits a request to register a further edition of a work the catalog already holds
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #18'
    - FQDN: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to register a further copy against a registered book
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #19'
    - FQDN: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to change a registered book's description
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #20'
    - FQDN: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to retire a book record judged obsolete
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #21'
    - FQDN: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to return a retired book record to the registered state
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #22'
    - FQDN: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to retire a lost or damaged copy
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #23'
    - FQDN: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to return a retired copy to the registered state
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #24'
    - FQDN: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request for a book's complete details with the copies held
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #25'
    - FQDN: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: A request to locate material by subject or by title
      Reason: It requires the rules the catalog now holds.
      Source Finding: 'S6 pps_artifacts_requiring_action #26'
    - FQDN: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #27'
    - FQDN: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #28'
    - FQDN: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #29'
    - FQDN: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #30'
    - FQDN: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #31'
    - FQDN: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #32'
    - FQDN: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #33'
    - FQDN: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #34'
    - FQDN: book_library_mgmt::CC_RESOLVE_WORK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #35'
    - FQDN: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #36'
    - FQDN: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #37'
    - FQDN: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #38'
    - FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Superseded and not in force; named by its successor, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - FQDN: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Superseded and not in force; named by its successor, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - FQDN: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Binds every catalog act, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: The actor every catalog act runs as, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::EV_BOOK_RETIRED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::EV_WORK_REGISTERED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Announced by an act this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by a contract this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by a contract this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by a contract this change redeclares, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #3'
    - FQDN: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by a contract this change redeclares, unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by a contract this change redeclares, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #1'
    - FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Run by a contract this change redeclares, unchanged.
      Source Finding: 'S6 cross_subdomain_deps #2'
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Holds the catalog's records, unchanged.
      Source Finding: 'S6 storage_governance #1'
    - FQDN: capability_side_effects::CS_REGISTRY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Holds the catalog's records, unchanged.
      Source Finding: 'S6 storage_governance #1'
    - FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Holds the catalog's records, unchanged.
      Source Finding: 'S6 storage_governance #1'
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows: []
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
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_SEARCH_CATALOG_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
  execution_topology:
    columns:
    - Workflow
    - Node
    - Runs
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::IN_REGISTER_BOOK_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; ALREADY_EXISTS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_BOOK_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_REGISTER_BOOK_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit ['book_library_mgmt::EV_WORK_REGISTERED_V0', 'book_library_mgmt::EV_BOOK_REGISTERED_V0', 'book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0']
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RESOLVE_WORK_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_RESOLVE_WORK_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit book_library_mgmt::EV_BOOK_REGISTERED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit book_library_mgmt::EV_BOOK_RETIRED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: emit book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - Workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_SEARCH_CATALOG_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: EXIT_COMPLETED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
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
    - CC Code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Step: '1'
      Step Name: confirm_authorization
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: is_authorized
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=is_authorized'
    - CC Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: '1'
      Step Name: validate_book_fields
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: record, schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=record, schema=schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: '2'
      Step Name: validate_work_fields
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: record, schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=record, schema=schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: '3'
      Step Name: require_submission_complete
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: valid
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=valid'
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
      Consumes: record, schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=record, schema=schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: '3'
      Step Name: refuse_incomplete_record
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=valid'
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: '4'
      Step Name: assemble_book_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: fields
      Produces: book_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=fields; out: record=book_record'
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: '5'
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
      Interface: 'in: key=key, value=value; out: result_status=result_status'
    - CC Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: '1'
      Step Name: validate_edition_fields
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: record, schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=record, schema=schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: '2'
      Step Name: refuse_incomplete_record
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=valid'
    - CC Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: '3'
      Step Name: assemble_edition_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: fields
      Produces: edition_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=fields; out: record=edition_record'
    - CC Code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: '4'
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
      Interface: 'in: key=key, value=value; out: result_status=result_status'
    - CC Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: '1'
      Step Name: read_book_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: BOOKS
      Consumes: key
      Produces: book_record, result_status
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=key; out: value=book_record, result_status=result_status'
    - CC Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: '2'
      Step Name: assemble_copy_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: fields
      Produces: copy_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=fields; out: record=copy_record'
    - CC Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: '3'
      Step Name: write_copy_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: WRITE
      Store: PHYSICAL_COPIES
      Consumes: key, value
      Produces: result_status
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=key, value=value; out: result_status=result_status'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '1'
      Step Name: read_book_record
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: READ
      Store: BOOKS
      Consumes: key
      Produces: book_record, result_status
      Routing: SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: key=key; out: value=book_record, result_status=result_status'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '2'
      Step Name: form_updated_identity_key
      Capability: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Kind (CT, CS): CT
      Operation: FORM_BOOK_IDENTITY_KEY
      Store: —
      Consumes: title, author, publication_year
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
      Consumes: left, right
      Produces: identity_unchanged
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: left=left, right=right; out: is_equal=identity_unchanged'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '4'
      Step Name: require_identity_unchanged
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=valid'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '5'
      Step Name: assemble_updated_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: fields
      Produces: updated_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=fields; out: record=updated_record'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '6'
      Step Name: check_corrected_record
      Capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_RECORD_STRUCTURE
      Store: —
      Consumes: record, schema
      Produces: violations
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: record=record, schema=schema; out: violations=violations'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '7'
      Step Name: refuse_incomplete_correction
      Capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Kind (CT, CS): CT
      Operation: VALIDATE_PARAMETER_RULES
      Store: —
      Consumes: parameters, rules
      Produces: valid
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=parameters, rules=rules; out: valid=valid'
    - CC Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: '8'
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
      Interface: 'in: key=key, value=value; out: result_status=result_status'
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
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: work_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author'', ''publication_year'': ''$.payload.publication_year'', ''subject'': ''$.payload.book_fields.subject''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: work_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: publication_year
      Bound To: payload.publication_year
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author'', ''publication_year'': ''$.payload.publication_year'', ''subject'': ''$.payload.book_fields.subject'', ''state'': ''REGISTERED''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_BOOK_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_BOOK_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: copy_fields
      Bound To: payload.copy_fields
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REGISTER_BOOK
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REGISTER_BOOK'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.title''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: book_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author'', ''publication_year'': ''$.payload.publication_year'', ''subject'': ''$.payload.subject''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: work_fields
      Bound To: '{''title'': ''$.payload.title'', ''author'': ''$.payload.author''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology book_library_mgmt::CC_RESOLVE_WORK_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology book_library_mgmt::CC_RESOLVE_WORK_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: publication_year
      Bound To: payload.publication_year
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: edition_fields
      Bound To: '{''identity_key'': ''$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key'', ''title'': ''$.payload.title'', ''author'': ''$.payload.author'', ''publication_year'': ''$.payload.publication_year'', ''subject'': ''$.payload.subject'', ''state'': ''REGISTERED'', ''work_key'': ''$.results.CC_RESOLVE_WORK_V0.work_key''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REGISTER_ADDITIONAL_EDITION
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REGISTER_ADDITIONAL_EDITION'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: copy_fields
      Bound To: payload.copy_fields
      Source Finding: S7 execution_topology book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REGISTER_PHYSICAL_COPY
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REGISTER_PHYSICAL_COPY'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.barcode''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: updated_fields
      Bound To: payload.updated_fields
      Source Finding: S7 execution_topology book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: UPDATE_BIBLIOGRAPHIC_INFORMATION
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''UPDATE_BIBLIOGRAPHIC_INFORMATION'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: RETIRE_BOOK_RECORD
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''RETIRE_BOOK_RECORD'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REINSTATE_BOOK_RECORD
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REINSTATE_BOOK_RECORD'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: RETIRE_PHYSICAL_COPY
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''RETIRE_PHYSICAL_COPY'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.barcode''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REINSTATE_PHYSICAL_COPY
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REINSTATE_PHYSICAL_COPY'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.barcode''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: copy_criteria
      Bound To: '{''identity_key'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: RETRIEVE_BOOK_DETAILS
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''RETRIEVE_BOOK_DETAILS'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: search_criteria
      Bound To: payload.search_criteria
      Source Finding: S7 execution_topology book_library_mgmt::CC_SEARCH_CATALOG_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: SEARCH_CATALOG
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''SEARCH_CATALOG'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.search_criteria''}'
      Source Finding: S7 execution_topology book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Step: confirm_authorization
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: inputs.staff_credentials
      Source Finding: S7 cc_composition confirm_authorization
    - Owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Step: confirm_authorization
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''staff_id'', ''op'': ''not_null''}, {''field'': ''authorized'', ''op'': ''eq'', ''value'': True}]'
      Source Finding: S7 cc_composition confirm_authorization
    - Owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Step: confirm_authorization
      Direction (INPUT, OUTPUT): OUTPUT
      Field: is_authorized
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition confirm_authorization
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
      Bound To: '{''title'': {''required'': True, ''type'': ''string''}, ''author'': {''required'': True, ''type'': ''string''}, ''publication_year'': {''required'': True, ''type'': ''integer''}, ''subject'': {''required'': True, ''type'': ''array''}}'
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_book_fields
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
      Bound To: '{''title'': {''required'': True, ''type'': ''string''}, ''author'': {''required'': True, ''type'': ''string''}}'
      Source Finding: S7 cc_composition validate_work_fields
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: validate_work_fields
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_work_fields
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: require_submission_complete
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''barcode'': ''$.inputs.barcode'', ''subject'': ''$.inputs.book_fields.subject'', ''book_violations'': ''$.results.validate_book_fields.violations'', ''work_violations'': ''$.results.validate_work_fields.violations''}'
      Source Finding: S7 cc_composition require_submission_complete
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: require_submission_complete
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''barcode'', ''op'': ''neq'', ''value'': ''''}, {''field'': ''subject'', ''op'': ''neq'', ''value'': []}, {''field'': ''book_violations'', ''op'': ''eq'', ''value'': []}, {''field'': ''work_violations'', ''op'': ''eq'', ''value'': []}]'
      Source Finding: S7 cc_composition require_submission_complete
    - Owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Step: require_submission_complete
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition require_submission_complete
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
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.book_fields
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): INPUT
      Field: schema
      Bound To: '{''title'': {''required'': True, ''type'': ''string''}, ''author'': {''required'': True, ''type'': ''string''}, ''publication_year'': {''required'': True, ''type'': ''integer''}, ''subject'': {''required'': True, ''type'': ''array''}}'
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: validate_book_fields
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_book_fields
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: refuse_incomplete_record
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''violations'': ''$.results.validate_book_fields.violations''}'
      Source Finding: S7 cc_composition refuse_incomplete_record
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: refuse_incomplete_record
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''violations'', ''op'': ''eq'', ''value'': []}]'
      Source Finding: S7 cc_composition refuse_incomplete_record
    - Owner: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: refuse_incomplete_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition refuse_incomplete_record
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
      Bound To: '{''title'': {''required'': True, ''type'': ''string''}, ''author'': {''required'': True, ''type'': ''string''}, ''publication_year'': {''required'': True, ''type'': ''integer''}, ''subject'': {''required'': True, ''type'': ''array''}}'
      Source Finding: S7 cc_composition validate_edition_fields
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: validate_edition_fields
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition validate_edition_fields
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: refuse_incomplete_record
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''violations'': ''$.results.validate_edition_fields.violations''}'
      Source Finding: S7 cc_composition refuse_incomplete_record
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: refuse_incomplete_record
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''violations'', ''op'': ''eq'', ''value'': []}]'
      Source Finding: S7 cc_composition refuse_incomplete_record
    - Owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Step: refuse_incomplete_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition refuse_incomplete_record
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
    - Owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: book_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: assemble_copy_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''barcode'': ''$.inputs.barcode'', ''state'': ''REGISTERED''}'
      Source Finding: S7 cc_composition assemble_copy_record
    - Owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: assemble_copy_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: copy_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_copy_record
    - Owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: write_copy_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.barcode
      Source Finding: S7 cc_composition write_copy_record
    - Owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: write_copy_record
      Direction (INPUT, OUTPUT): INPUT
      Field: value
      Bound To: results.assemble_copy_record.copy_record
      Source Finding: S7 cc_composition write_copy_record
    - Owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: write_copy_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition write_copy_record
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
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''title'': ''$.inputs.updated_fields.title'', ''author'': ''$.inputs.updated_fields.author'', ''publication_year'': ''$.inputs.updated_fields.publication_year'', ''subject'': ''$.inputs.updated_fields.subject'', ''state'': ''$.results.read_book_record.book_record.state'', ''work_key'': ''$.results.read_book_record.book_record.work_key''}'
      Source Finding: S7 cc_composition assemble_updated_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: assemble_updated_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_record
      Bound To: capability_result.record
      Source Finding: S7 cc_composition assemble_updated_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: check_corrected_record
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: results.assemble_updated_record.updated_record
      Source Finding: S7 cc_composition check_corrected_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: check_corrected_record
      Direction (INPUT, OUTPUT): INPUT
      Field: schema
      Bound To: '{''title'': {''required'': True, ''type'': ''string''}, ''author'': {''required'': True, ''type'': ''string''}, ''publication_year'': {''required'': True, ''type'': ''integer''}, ''subject'': {''required'': True, ''type'': ''array''}}'
      Source Finding: S7 cc_composition check_corrected_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: check_corrected_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: violations
      Bound To: capability_result.violations
      Source Finding: S7 cc_composition check_corrected_record
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: refuse_incomplete_correction
      Direction (INPUT, OUTPUT): INPUT
      Field: parameters
      Bound To: '{''violations'': ''$.results.check_corrected_record.violations'', ''subject'': ''$.results.assemble_updated_record.updated_record.subject''}'
      Source Finding: S7 cc_composition refuse_incomplete_correction
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: refuse_incomplete_correction
      Direction (INPUT, OUTPUT): INPUT
      Field: rules
      Bound To: '[{''field'': ''violations'', ''op'': ''eq'', ''value'': []}, {''field'': ''subject'', ''op'': ''neq'', ''value'': []}]'
      Source Finding: S7 cc_composition refuse_incomplete_correction
    - Owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: refuse_incomplete_correction
      Direction (INPUT, OUTPUT): OUTPUT
      Field: valid
      Bound To: capability_result.valid
      Source Finding: S7 cc_composition refuse_incomplete_correction
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
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: title
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: author
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: publication_year
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: publication year
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: book fields
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: barcode
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: copy_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: copy fields
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: title
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: author
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: publication_year
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: publication year
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: subject
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: subject
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: barcode
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: copy_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: copy fields
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: updated_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: updated fields
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: barcode
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: barcode
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: search_criteria
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: search criteria
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff id
    - Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: staff credentials
    - Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: is_authorized
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: is authorized
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: work_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: work fields
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: book fields
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'NO'
      Default: ''
      Meaning: barcode
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: valid
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: valid
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: book fields
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: book_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: book record
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: edition_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: edition fields
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: edition_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: edition record
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: barcode
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: copy_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: copy fields
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: book_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: book record
    - Artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: identity key
    - Artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: updated_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: updated fields
    - Artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: book_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: book record
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
    rows: []
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
    rows: []
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
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - Artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - Artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - Artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Property: supersedes
      Value: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - Artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BOOK_RETIRED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - Artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Property: supersedes
      Value: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #20'
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows: []
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
    rows: []
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: catalog
      Count: '26'
      Artifacts: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::IN_REGISTER_BOOK_V0, book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0, book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::IN_SEARCH_CATALOG_V0
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows: []
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows: []
  refusal_discharge:
    columns:
    - Operation
    - Refused When
    - Act
    - Step
    - Outcome
    - Source Finding
    rows:
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Act: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Registering a book
      Refused When: It lacks what the library says a book must contain
      Act: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Registering a further edition
      Refused When: It lacks what the library says an edition must contain
      Act: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #3'
  refusal_deferrals:
    columns:
    - Operation
    - Refused When
    - Deferred To
    - Until
    - Source Finding
    rows: []
  refusal_governance_discharge:
    columns:
    - Operation
    - Refused When
    - Phase
    - Governing Rule
    - Source Finding
    rows: []
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
    rows: []
  molecule_step_bindings:
    columns:
    - CT Code
    - Step
    - Role (INPUT, CARRY, UPDATE)
    - Field
    - Bound To
    - Source Finding
    rows: []
  test_cases:
    columns:
    - CT Code
    - Case
    - Expected Outcome (SUCCESS, VIOLATION)
    - Source Finding
    rows: []
  test_case_values:
    columns:
    - CT Code
    - Case
    - Role (INPUT, EXPECTED, ASSERT, RECORDED)
    - Field
    - Value
    - Source Finding
    rows: []
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows:
    - Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Fact: .core.inputs.authorization_rules
      Reason: The contract holds the library's rules itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
      Reason: The confirming contract no longer takes the rules.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Fact: .core.inputs.authorization_rules
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Fact: .core.inputs.book_schema
      Reason: The contract holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Fact: .core.inputs.work_schema
      Reason: The contract holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Fact: .core.inputs.book_schema
      Reason: The contract holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.inputs.edition_schema
      Reason: The contract holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Fact: .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.book_schema
      Reason: The check holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Fact: .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.work_schema
      Reason: The check holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Fact: .core.nodes.CC_REGISTER_BOOK_V0.inputs.book_schema
      Reason: The contract holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Fact: .core.inputs.book_schema
      Reason: The gate no longer requires what the catalog holds.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.book_schema
      Reason: The check holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.work_schema
      Reason: The check holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.nodes.CC_REGISTER_ADDITIONAL_EDITION_V0.inputs.edition_schema
      Reason: The contract holds its description itself.
      Source Finding: 'S6 boundary_rules #1'
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.inputs.edition_schema
      Reason: The gate no longer requires what the catalog holds or no act reads.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.inputs.work_schema
      Reason: The gate no longer requires what the catalog holds or no act reads.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.inputs.edition_fields
      Reason: The gate no longer requires what the catalog holds or no act reads.
      Source Finding: 'S6 boundary_rules #6'
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Fact: .core.inputs.work_fields
      Reason: The gate no longer requires what the catalog holds or no act reads.
      Source Finding: 'S6 boundary_rules #6'
```

Every binding names a field the capability declares, read from the pinned baseline
`34c8a0e8a3f2f1b90956edd08d0d878a10347fbc058348049f8348ce0d5b8a95`.

Nothing new is authored. Twenty-six artifacts the catalog already holds are redeclared whole: six
contracts hold their rules and descriptions and refuse on what they find, ten acts stop passing rules
along and check what they record, and ten gates stop requiring what the catalog holds.

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

The routing of every act is unchanged. What changes is what each node is handed, in §7.

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

---

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

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
