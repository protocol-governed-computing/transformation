# Stage 7 — Design Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_04_catalog
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
    - Decision: The form the publication year takes at the boundary of registering a further edition
      Business Fact: Three of the four statements of the form say number, and every year the library supplies is a number.
      Resolution: '`publication_year` is declared `integer` in `book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0`, matching its two sibling boundaries.'
      Source Finding: S6 boundary_rules A_YEAR_IS_A_NUMBER
    - Decision: Which requirements a correction keeps
      Business Fact: Its four steps read the record named and the details being changed, and nothing else the request supplied.
      Resolution: '`book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1` is authored requiring the five its steps read, and supersedes `..._V0`. A boundary is rendered whole from the design, so a requirement is withdrawn by authoring the successor that does not carry it, never by amending the predecessor to say less than it said.'
      Source Finding: S6 boundary_rules REQUIRES_ONLY_WHAT_IT_USES
    - Decision: Whether registering a work is corrected here
      Business Fact: Its steps read `subject` at the top of the request and rebuild the details of the book themselves; every present caller sends `subject` nested inside the details it supplies.
      Resolution: '`book_library_mgmt::IN_REGISTER_BOOK_V0` is unchanged. Requiring `subject` moves the boundary and every caller together, and no caller moves inside this change.'
      Source Finding: S6 boundary_rules NO_CORRECT_REQUEST_BECOMES_HARDER
    - Decision: Whether any workflow changes
      Business Fact: The three operations read exactly what they read today.
      Resolution: No workflow, capability contract, capability transform, side effect or store is altered. Each of the three boundaries is re-rendered whole; the act it admits is restated unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - Decision: Whether authority is reached
      Business Fact: The three things that decide who may perform an operation are read by no step of any of the subdomain's ten operations.
      Resolution: '`staff_credentials`, `authorization_rules` and `staff_id` are restated unchanged in all three boundaries, in the same form and with the same requiredness.'
      Source Finding: S6 boundary_rules AUTHORITY_IS_UNTOUCHED
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: The boundary that admits a request to register a further edition of a work the catalog already holds
      Reason: One requirement changes form; the other ten are restated unchanged, because an EXTEND re-renders the boundary whole.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REPLACE
      Summary: ''
      Reason: Requires three things no step of its operation reads. Stood down and superseded, because withdrawing a requirement makes the boundary say less than it said, and an amendment may only say more.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: book_library_mgmt::IN_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: The boundary that admits a request to register a work, its first edition and that edition's first physical copy
      Reason: 'Requires ten things where its act reads eleven. Unchanged: the missing requirement is one every present caller sends nested inside the details of the book rather than where the act reads it.'
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The governed sequence that registers a further edition of a work already held
      Reason: Reads all eleven things its boundary requires. Named because the boundary is its entry node and an EXTEND must state the act it admits.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REPLACE
      Summary: ''
      Reason: Names the boundary being superseded as its entry. An act states the boundary that admits it, so a successor boundary means a successor act. Nothing consumes this act, so the substitution reaches nothing further.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: The governed sequence that registers a work, its first edition and that edition's first physical copy
      Reason: Reads eleven things, one of which its boundary does not require, and rebuilds the details of the book from the top of the request. Unchanged, and named as the evidence that the third correction reaches a caller.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The actor whose authorization every catalog operation binds
      Reason: The actor all three acts run as. Named because an EXTEND re-renders the boundary and the act it admits must state its actor.
      Source Finding: 'S6 ownership #5'
    - FQDN: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Decides whether the staff member may perform the operation
      Reason: The first act of all three sequences, and what consumes the three authority requirements. Unchanged.
      Source Finding: 'S6 ownership #5'
    - FQDN: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Checks a submitted description against the schema supplied with it
      Reason: Named by two of the three acts; what reads `publication_year` in the form the boundary declares.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Resolves the record a correction names
      Reason: What reads `identity_key`, one of the five requirements the correction keeps.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Changes the details of a resolved record
      Reason: What reads `updated_fields`, and what reads none of the three requirements withdrawn.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Records that a catalog operation occurred
      Reason: The last act of all three sequences. Unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: book_library_mgmt::CC_RESOLVE_WORK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Resolves the work a further edition attaches to
      Reason: Named by the act that registers a further edition; unchanged, and restated because the boundary above it is re-rendered whole.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Claims the identity of an edition
      Reason: Named by two of the three acts; what reads the title, the author and the publication year.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Registers a further edition against a resolved work
      Reason: Named by the act that registers a further edition; unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Claims the identity of a work
      Reason: Named by the act that registers a work; unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Claims the barcode of a physical copy
      Reason: Named by the act that registers a work; unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: book_library_mgmt::CC_REGISTER_BOOK_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Registers an edition against a claimed identity
      Reason: Named by the act that registers a work; what reads the subject the boundary now requires.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Puts a physical copy on a shelf
      Reason: Named by the act that registers a work; unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Binds the catalog's acts to the capabilities and stores that carry them
      Reason: Named because the three acts are bound through it; unchanged by this change.
      Source Finding: 'S6 ownership #6'
    - FQDN: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: The moment the act announces when a correction completes
      Reason: Announced at the act's successful ending. Unchanged, and named because an EXTEND re-renders the act whole and the announcement must be restated with it.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares the six stores the catalog owns and the paths they occupy
      Reason: Declares no form for any detail it holds, which is why the form of a publication year rests on agreement rather than on a declaration. Unchanged by this change.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
  new_artifacts:
    columns:
    - Capability
    - Family
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: Admitting a request to correct bibliographic information
      Family: IN
      Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Summary: A request to change a registered book's description
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: 'S6 governance_outcome #2'
    - Capability: The three operations
      Family: WF
      Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Summary: Corrects what the library publishes about a registered book
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: 'S6 governance_outcome #2'
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
      CS Bindings: Unchanged
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 ownership #6'
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      CS Bindings: Unchanged
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S6 ownership #6'
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
      Source Finding: S7 existing_inventory IN_REGISTER_ADDITIONAL_EDITION_V0
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
      Source Finding: S7 existing_inventory WF_REGISTER_ADDITIONAL_EDITION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory WF_REGISTER_ADDITIONAL_EDITION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Node: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory WF_REGISTER_ADDITIONAL_EDITION_V0
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
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_RESOLVE_BOOK_IDENTITY_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 existing_inventory CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
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
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
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
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology CC_CLAIM_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: edition_fields
      Bound To: '{''author'': ''$.payload.author'', ''identity_key'': ''$.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key'', ''publication_year'': ''$.payload.publication_year'', ''state'': ''REGISTERED'', ''subject'': ''$.payload.subject'', ''title'': ''$.payload.title'', ''work_key'': ''$.results.CC_RESOLVE_WORK_V0.work_key''}'
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
      Field: identity_key
      Bound To: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
      Source Finding: S7 execution_topology CC_REGISTER_ADDITIONAL_EDITION_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: payload.author
      Source Finding: S7 execution_topology CC_RESOLVE_WORK_V0
    - Owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::CC_RESOLVE_WORK_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: payload.title
      Source Finding: S7 execution_topology CC_RESOLVE_WORK_V0
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
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: UPDATE_BIBLIOGRAPHIC_INFORMATION
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''UPDATE_BIBLIOGRAPHIC_INFORMATION'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_RESOLVE_BOOK_IDENTITY_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: updated_fields
      Bound To: payload.updated_fields
      Source Finding: S7 execution_topology CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
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
      Default: —
      Meaning: The credentials of the staff member making the request. Consumed by the decision about who may act.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The rules that decide whether this staff member may perform the operation.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The staff member accountable for the request.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The title of the work the edition belongs to.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The author of the work the edition belongs to.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: publication_year
      Type: integer
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The year the edition was published. Stated as a number, as the catalog holds it and as both sibling boundaries declare it.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: subject
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The subject headings of the edition.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: edition_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The details of the edition being registered.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: edition_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The description the edition is checked against.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: work_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The details of the work the edition is attached to.
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: work_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The description the work is checked against.
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The credentials of the staff member making the request. Consumed by the decision about who may act.
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The rules that decide whether this staff member may perform the operation.
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The staff member accountable for the request.
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The record being corrected.
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: updated_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The details being changed. A correction supplies these and does not restate the fields it leaves alone.
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
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: NONE IDENTIFIED
      Extends: ''
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
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Property: core.workflow
      Value: WF_REGISTER_ADDITIONAL_EDITION_V0
      Source Finding: S7 execution_topology WF_REGISTER_ADDITIONAL_EDITION_V0
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Property: core.workflow
      Value: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Source Finding: S7 execution_topology WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Property: emit.EXIT_COMPLETED
      Value: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Source Finding: S7 existing_inventory WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Property: supersedes
      Value: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Source Finding: S7 existing_inventory IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Property: supersedes
      Value: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Source Finding: S7 existing_inventory WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
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
      Count: '1'
      Artifacts: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Subdomain: catalog
      Count: '2'
      Artifacts: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Count: '2'
      Artifacts: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
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
    - Operation: Registering a further edition
      Refused When: The publication year is not supplied
      Act: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Step: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Outcome: NACK
      Source Finding: 'S1 operation_refusals #1'
    - Operation: Correcting bibliographic information
      Refused When: The record to correct is not named
      Act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Outcome: NACK
      Source Finding: 'S1 operation_refusals #2'
    - Operation: Correcting bibliographic information
      Refused When: No changed fields are supplied
      Act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Step: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Outcome: NACK
      Source Finding: 'S1 operation_refusals #3'
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
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Phase: ''
      Governing Rule: ''
      Source Finding: ''
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

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

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

## 20. Refusal Governance Discharge

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
