# Design Intent — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: cr_01_catalog
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
    - Decision: The catalog is a new subdomain
      Business Fact: Nothing in the composition manages a library catalog
      Resolution: A new subdomain namespace with its own actor, stores, bindings and operations
      Source Finding: 'S4 design_decisions #1'
    - Decision: The catalog owns its audit trail
      Business Fact: A subdomain owns its stores exclusively
      Resolution: An own append-only store and an own composed append step, reusing only the append mechanism
      Source Finding: 'S4 design_decisions #2'
    - Decision: Uniqueness by composite key
      Business Fact: Title, author and publication year identify a book
      Resolution: A pure transform forms one key from the three attributes; the registry claims it atomically, and ALREADY_EXISTS is the duplicate refusal
      Source Finding: 'S4 design_decisions #3'
    - Decision: State is data on the record
      Business Fact: Retirement is reversible
      Resolution: Both record stores hold state as a field; retirement and reinstatement are writes, never moves between stores
      Source Finding: 'S4 design_decisions #4'
    - Decision: Reads are audited, raise no event
      Business Fact: Nothing reacts to a read
      Resolution: Search and retrieval append to the trail and declare no EV artifact
      Source Finding: 'S4 design_decisions #5'
    - Decision: Registration includes the first copy
      Business Fact: A book is never registered without a copy
      Resolution: One workflow claims both identities and writes both records before appending
      Source Finding: 'S4 design_decisions #6'
    - Decision: Retirement never cascades
      Business Fact: Staff retire each record explicitly
      Resolution: Four separate workflows, each writing one record and leaving the other alone
      Source Finding: 'S4 design_decisions #7'
    - Decision: Authorization is read, never granted
      Business Fact: Deciding who is authorized belongs to the staff function
      Resolution: One contract validates supplied credentials against supplied rules; no store of authorized staff is declared
      Source Finding: 'S4 design_decisions #8'
    - Decision: Subject is free text
      Business Fact: The business chose free text
      Resolution: No value-set validation is bound; search criteria match on the subject as typed
      Source Finding: 'S4 design_decisions #9'
    - Decision: Search excludes retired, retrieval serves them
      Business Fact: A retired record stays auditable and retrievable
      Resolution: Search filters on state; retrieval reads by key without a state criterion
      Source Finding: 'S4 design_decisions #10'
    - Decision: The record mechanism is extended, not duplicated
      Business Fact: The implementation already returned records
      Resolution: One additive operation on the platform side effect; the catalog holds no second copy of a book
      Source Finding: 'S4 design_decisions #11'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REPLACE
      Summary: Writes, reads, selects, lists, updates in place and deletes durable records
      Reason: Extended with an operation that publishes the records themselves, so a search can select among them by content; the implementation behind it already returned them.
      Source Finding: S6 pps_artifacts_requiring_action capability_side_effects::CS_MUTABLE_JSON_V0
    - FQDN: catalog::CS_REGISTRY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Register-if-absent gives the atomic claim duplicate prevention needs, on a key the catalog forms.
      Source Finding: S6 ownership Claim a value once so a second claim on it fails
    - FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: ''
      Reason: Appends an entry to a trail that cannot be amended.
      Source Finding: S6 ownership Append an entry to a trail that cannot be amended
    - FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Assembles a durable record from supplied values.
      Source Finding: S6 ownership Assemble a durable record from supplied values
    - FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Confirms a record carries the fields its contract declares.
      Source Finding: S6 ownership Confirm a record carries the fields its contract declares
    - FQDN: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Selects the records matching stated criteria, and interprets a read of the store into a decision.
      Source Finding: S6 ownership Select the records matching stated criteria
    - FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Confirms supplied parameters satisfy declared rules, and interprets a read into a decision.
      Source Finding: S6 ownership Confirm supplied parameters satisfy declared rules
    - FQDN: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Decides whether the identity an update would produce is the identity the book already has.
      Source Finding: S6 ownership Confirm supplied parameters satisfy declared rules
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
    - Capability: A moment the library records a loan
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: book_library_mgmt::EV_BOOK_LOAN_V0
      Summary: The moment a book leaves the shelf
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes AC_LIBRARY_STAFF_V0
    - Capability: The authorized staff member who performs a catalog operation
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): AC
      Code: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Summary: The actor whose authorization every catalog operation binds
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes AC_LIBRARY_STAFF_V0
    - Capability: A request to register a book together with its first physical copy
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_REGISTER_BOOK_V0
      Summary: A request to register a book together with its first physical copy
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_REGISTER_BOOK_V0
    - Capability: A request to register a further copy against a registered book
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Summary: A request to register a further copy against a registered book
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_REGISTER_PHYSICAL_COPY_V0
    - Capability: A request to change a registered book's description
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Summary: A request to change a registered book's description
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Capability: A request to retire a book record judged obsolete
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Summary: A request to retire a book record judged obsolete
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_RETIRE_BOOK_RECORD_V0
    - Capability: A request to retire a lost or damaged copy
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Summary: A request to retire a lost or damaged copy
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_RETIRE_PHYSICAL_COPY_V0
    - Capability: A request to return a retired book record to the registered state
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Summary: A request to return a retired book record to the registered state
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_REINSTATE_BOOK_RECORD_V0
    - Capability: A request to return a retired copy to the registered state
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Summary: A request to return a retired copy to the registered state
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_REINSTATE_PHYSICAL_COPY_V0
    - Capability: A request to locate material by subject or by title
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Summary: A request to locate material by subject or by title
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_SEARCH_CATALOG_V0
    - Capability: A request for a book's complete details with the copies held
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): IN
      Code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Summary: A request for a book's complete details with the copies held
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes IN_RETRIEVE_BOOK_DETAILS_V0
    - Capability: Registering a book and its first copy, end to end
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_REGISTER_BOOK_V0
      Summary: Registering a book and its first copy, end to end
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_REGISTER_BOOK_V0
    - Capability: Registering a further copy against a registered book
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Summary: Registering a further copy against a registered book
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_REGISTER_PHYSICAL_COPY_V0
    - Capability: Changing a book's description without making it a duplicate
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Summary: Changing a book's description without making it a duplicate
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Capability: Retiring a book record, leaving its copies untouched
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Summary: Retiring a book record, leaving its copies untouched
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_RETIRE_BOOK_RECORD_V0
    - Capability: Retiring a copy, leaving the book record untouched
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Summary: Retiring a copy, leaving the book record untouched
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_RETIRE_PHYSICAL_COPY_V0
    - Capability: Returning a retired book record to the registered state
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Summary: Returning a retired book record to the registered state
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_REINSTATE_BOOK_RECORD_V0
    - Capability: Returning a retired copy to the registered state
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Summary: Returning a retired copy to the registered state
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_REINSTATE_PHYSICAL_COPY_V0
    - Capability: Searching by subject or title, excluding retired books
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Summary: Searching by subject or title, excluding retired books
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_SEARCH_CATALOG_V0
    - Capability: Assembling a book with the copies the library holds of it
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): WF
      Code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Summary: Assembling a book with the copies the library holds of it
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes WF_RETRIEVE_BOOK_DETAILS_V0
    - Capability: Confirm the staff member may perform catalog operations
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Summary: Confirm the staff member may perform catalog operations
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Capability: Judge a registration admissible before anything is claimed or written
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Summary: Validate a book submission is complete
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_REGISTER_BOOK_V0
    - Capability: Resolve a registered book's identity without claiming it
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Summary: Resolve a registered book's identity key
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_CLAIM_BOOK_IDENTITY_V0
    - Capability: Claim a book's identity so a second registration of the same book is refused
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Summary: Claim a book's identity so a second registration of the same book is refused
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_CLAIM_BOOK_IDENTITY_V0
    - Capability: Claim a copy's barcode so a second copy carrying it is refused
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Summary: Claim a copy's barcode so a second copy carrying it is refused
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_CLAIM_COPY_BARCODE_V0
    - Capability: Record a book's bibliographic information as the catalog's authoritative description
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Summary: Record a book's bibliographic information as the catalog's authoritative description
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_REGISTER_BOOK_V0
    - Capability: Record a copy against exactly one book
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Summary: Record a copy against exactly one book
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_REGISTER_PHYSICAL_COPY_V0
    - Capability: Replace a book's descriptive content in place
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Summary: Replace a book's descriptive content in place
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - Capability: Mark a book record retired so it is no longer offered as current
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Summary: Mark a book record retired so it is no longer offered as current
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_RETIRE_BOOK_RECORD_V0
    - Capability: Mark a copy retired so the library no longer holds it
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Summary: Mark a copy retired so the library no longer holds it
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_RETIRE_PHYSICAL_COPY_V0
    - Capability: Mark a retired book record registered again
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Summary: Mark a retired book record registered again
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_REINSTATE_BOOK_RECORD_V0
    - Capability: Mark a retired copy registered again
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Summary: Mark a retired copy registered again
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_REINSTATE_PHYSICAL_COPY_V0
    - Capability: Select the registered books matching a subject or title, excluding retired ones
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Summary: Select the registered books matching a subject or title, excluding retired ones
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_SEARCH_CATALOG_V0
    - Capability: Assemble a book's record with the copies recorded against it
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Summary: Assemble a book's record with the copies recorded against it
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_ASSEMBLE_BOOK_DETAILS_V0
    - Capability: Append a durable account of a performed operation to the catalog's own trail
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CC
      Code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Summary: Append a durable account of a performed operation to the catalog's own trail
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S5 provisional_codes CC_APPEND_CATALOG_OPERATION_V0
    - Capability: Form one identity key from a book's title, author and publication year
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): CT
      Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Summary: Forms the single key the registry claims from the three identifying attributes
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S3 authoring_decisions Enforce that one book exists per title, author and publication year
    - Capability: A book entered the catalog and acquired its authoritative record
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Summary: A book entered the catalog and acquired its authoritative record
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S4 events Book registered
    - Capability: The library recorded another copy it owns
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Summary: The library recorded another copy it owns
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S4 events Physical copy registered
    - Capability: The authoritative description of a book changed
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Summary: The authoritative description of a book changed
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S4 events Bibliographic information updated
    - Capability: A book record is no longer to be used
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: book_library_mgmt::EV_BOOK_RETIRED_V0
      Summary: A book record is no longer to be used
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S4 events Book retired
    - Capability: The library no longer holds that copy
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): EV
      Code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Summary: The library no longer holds that copy
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S4 events Physical copy retired
    - Capability: Bind the catalog's operations to the stores and mechanisms they use
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): RB
      Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Summary: Binds every catalog workflow to the mechanisms and stores it uses
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S6 ownership Record a performed catalog operation in the catalog's audit trail
    - Capability: Declare the stores the catalog owns
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE): STRUCTURE
      Code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Summary: Declares the five stores the catalog owns and the paths they occupy
      Owner Subdomain: catalog
      Status: NEW
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
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
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_SEARCH_CATALOG_V0
      CS Bindings: capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0
      Storage Structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: S6 storage_governance A durable record of every book the library catalogs
    - RB Code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Binds WF: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
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
      Source Finding: S7 new_artifacts IN_REGISTER_BOOK_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_VALIDATE_BOOK_SUBMISSION_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_BOOK_IDENTITY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_REGISTER_BOOK_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_REGISTER_BOOK_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REGISTER_BOOK_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CLAIM_COPY_BARCODE_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_REGISTER_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
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
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_REINSTATE_BOOK_RECORD_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_REINSTATE_BOOK_RECORD_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_REINSTATE_BOOK_RECORD_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_REINSTATE_BOOK_RECORD_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_REINSTATE_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_REINSTATE_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_REINSTATE_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_REINSTATE_PHYSICAL_COPY_V0
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_SEARCH_CATALOG_V0
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_SEARCH_CATALOG_V0
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_SEARCH_CATALOG_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_SEARCH_CATALOG_V0
    - Workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_SEARCH_CATALOG_V0
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED
      Source Finding: S7 new_artifacts IN_RETRIEVE_BOOK_DETAILS_V0
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_COMPLETED; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_ASSEMBLE_BOOK_DETAILS_V0
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED
      Source Finding: S7 new_artifacts CC_APPEND_CATALOG_OPERATION_V0
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: EXIT_COMPLETED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: S7 execution_topology WF_RETRIEVE_BOOK_DETAILS_V0
    - Workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Node: EXIT_REJECTED
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: S7 execution_topology WF_RETRIEVE_BOOK_DETAILS_V0
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
      Consumes: staff_credentials, authorization_rules
      Produces: is_authorized
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: parameters=staff_credentials, rules=authorization_rules; out: valid=is_authorized'
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
    - CC Code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: '1'
      Step Name: form_identity_key
      Capability: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Kind (CT, CS): CT
      Operation: FORM_BOOK_IDENTITY_KEY
      Store: —
      Consumes: title, author, publication_year
      Produces: identity_key
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: title=title, author=author, publication_year=publication_year; out: identity_key=identity_key'
    - CC Code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: '2'
      Step Name: claim_identity
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: BOOK_IDENTITY_REGISTRY
      Consumes: key, target_cs, target_ref
      Produces: address
      Routing: SUCCESS -> exit; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: ALREADY_EXISTS
      Interface: —
    - CC Code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Step: '1'
      Step Name: resolve_identity
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: RESOLVE
      Store: BOOK_IDENTITY_REGISTRY
      Consumes: key_or_address
      Produces: target_ref
      Routing: SUCCESS -> exit; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Step: '1'
      Step Name: claim_barcode
      Capability: capability_side_effects::CS_REGISTRY_V0
      Kind (CT, CS): CS
      Operation: REGISTER
      Store: COPY_BARCODE_REGISTRY
      Consumes: key, target_cs, target_ref
      Produces: address
      Routing: SUCCESS -> exit; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: ALREADY_EXISTS
      Interface: —
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
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
    - CC Code: book_library_mgmt::CC_REGISTER_BOOK_V0
      Step: '2'
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
      Step: '3'
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
    - CC Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
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
    - CC Code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Step: '2'
      Step Name: assemble_copy_record
      Capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Kind (CT, CS): CT
      Operation: ASSEMBLE_RECORD
      Store: —
      Consumes: copy_fields
      Produces: copy_record
      Routing: SUCCESS -> continue; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: fields=copy_fields; out: record=copy_record'
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
      Interface: —
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
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: source=records, filter=search_criteria; out: extracted=matching_books'
    - CC Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
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
    - CC Code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: '2'
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
      Step: '3'
      Step Name: select_copies_of_book
      Capability: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Kind (CT, CS): CT
      Operation: FILTER_RECORDS
      Store: —
      Consumes: records, copy_criteria
      Produces: copies_held
      Routing: SUCCESS -> exit; VIOLATION -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: 'in: source=records, filter=copy_criteria; out: extracted=copies_held'
    - CC Code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Step: '1'
      Step Name: set_record_state
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: UPDATE_WHERE
      Store: PHYSICAL_COPIES
      Consumes: filter, updates
      Produces: matched_keys, updated_count
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Step: '1'
      Step Name: set_record_state
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: UPDATE_WHERE
      Store: PHYSICAL_COPIES
      Consumes: filter, updates
      Produces: matched_keys, updated_count
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Step: '1'
      Step Name: set_record_state
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: UPDATE_WHERE
      Store: BOOKS
      Consumes: filter, updates
      Produces: matched_keys, updated_count
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Step: '1'
      Step Name: set_record_state
      Capability: capability_side_effects::CS_MUTABLE_JSON_V0
      Kind (CT, CS): CS
      Operation: UPDATE_WHERE
      Store: BOOKS
      Consumes: filter, updates
      Produces: matched_keys, updated_count
      Routing: SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit
      Interpreted By: —
      Semantic Status: SUCCESS
      Interface: —
    - CC Code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Step: '1'
      Step Name: append_operation
      Capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Kind (CT, CS): CS
      Operation: APPEND
      Store: CATALOG_OPERATIONS
      Consumes: record, stream_id, actor_id
      Produces: record_id, sequence_number
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
      Bound To: inputs.authorization_rules
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
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: form_identity_key
      Direction (INPUT, OUTPUT): INPUT
      Field: title
      Bound To: inputs.title
      Source Finding: S7 cc_composition form_identity_key
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: form_identity_key
      Direction (INPUT, OUTPUT): INPUT
      Field: author
      Bound To: inputs.author
      Source Finding: S7 cc_composition form_identity_key
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: form_identity_key
      Direction (INPUT, OUTPUT): INPUT
      Field: publication_year
      Bound To: inputs.publication_year
      Source Finding: S7 cc_composition form_identity_key
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: form_identity_key
      Direction (INPUT, OUTPUT): OUTPUT
      Field: identity_key
      Bound To: capability_result.identity_key
      Source Finding: S7 cc_composition form_identity_key
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: results.form_identity_key.identity_key
      Source Finding: S7 cc_composition claim_identity
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: target_cs
      Bound To: CS_MUTABLE_JSON_V0
      Source Finding: S7 cc_composition claim_identity
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: target_ref
      Bound To: BOOKS
      Source Finding: S7 cc_composition claim_identity
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: address
      Bound To: capability_result.address
      Source Finding: S7 cc_composition claim_identity
    - Owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Step: claim_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition claim_identity
    - Owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Step: resolve_identity
      Direction (INPUT, OUTPUT): INPUT
      Field: key_or_address
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition resolve_identity
    - Owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Step: resolve_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: target_ref
      Bound To: capability_result.target_ref
      Source Finding: S7 cc_composition resolve_identity
    - Owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Step: resolve_identity
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition resolve_identity
    - Owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Step: claim_barcode
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.barcode
      Source Finding: S7 cc_composition claim_barcode
    - Owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Step: claim_barcode
      Direction (INPUT, OUTPUT): INPUT
      Field: target_cs
      Bound To: CS_MUTABLE_JSON_V0
      Source Finding: S7 cc_composition claim_barcode
    - Owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Step: claim_barcode
      Direction (INPUT, OUTPUT): INPUT
      Field: target_ref
      Bound To: PHYSICAL_COPIES
      Source Finding: S7 cc_composition claim_barcode
    - Owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Step: claim_barcode
      Direction (INPUT, OUTPUT): OUTPUT
      Field: address
      Bound To: capability_result.address
      Source Finding: S7 cc_composition claim_barcode
    - Owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Step: claim_barcode
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition claim_barcode
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
      Step: assemble_book_record
      Direction (INPUT, OUTPUT): INPUT
      Field: fields
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''title'': ''$.inputs.book_fields.title'', ''author'': ''$.inputs.book_fields.author'', ''publication_year'': ''$.inputs.book_fields.publication_year'', ''subject'': ''$.inputs.book_fields.subject'', ''state'': ''$.inputs.book_fields.state''}'
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
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''barcode'': ''$.inputs.barcode'', ''state'': ''$.inputs.copy_fields.state''}'
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
      Bound To: '{''identity_key'': ''$.inputs.identity_key'', ''title'': ''$.inputs.updated_fields.title'', ''author'': ''$.inputs.updated_fields.author'', ''publication_year'': ''$.inputs.updated_fields.publication_year'', ''subject'': ''$.inputs.updated_fields.subject'', ''state'': ''$.inputs.updated_fields.state''}'
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
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): INPUT
      Field: key
      Bound To: inputs.identity_key
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: book_record
      Bound To: capability_result.value
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: read_book_record
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition read_book_record
    - Owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Step: select_copy_records
      Direction (INPUT, OUTPUT): OUTPUT
      Field: records
      Bound To: capability_result.records
      Source Finding: S7 cc_composition select_copy_records
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
    - Owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: '{''barcode'': ''$.inputs.barcode''}'
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): INPUT
      Field: updates
      Bound To: '{''state'': ''REGISTERED''}'
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: matched_keys
      Bound To: capability_result.matched_keys
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_count
      Bound To: capability_result.updated_count
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: '{''barcode'': ''$.inputs.barcode''}'
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): INPUT
      Field: updates
      Bound To: '{''state'': ''RETIRED''}'
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: matched_keys
      Bound To: capability_result.matched_keys
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_count
      Bound To: capability_result.updated_count
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: '{''identity_key'': ''$.inputs.identity_key''}'
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): INPUT
      Field: updates
      Bound To: '{''state'': ''REGISTERED''}'
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: matched_keys
      Bound To: capability_result.matched_keys
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_count
      Bound To: capability_result.updated_count
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): INPUT
      Field: filter
      Bound To: '{''identity_key'': ''$.inputs.identity_key''}'
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): INPUT
      Field: updates
      Bound To: '{''state'': ''RETIRED''}'
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: matched_keys
      Bound To: capability_result.matched_keys
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: updated_count
      Bound To: capability_result.updated_count
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Step: set_record_state
      Direction (INPUT, OUTPUT): OUTPUT
      Field: result_status
      Bound To: result_status
      Source Finding: S7 cc_composition set_record_state
    - Owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: inputs.record
      Source Finding: S7 cc_composition append_operation
    - Owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): INPUT
      Field: stream_id
      Bound To: CATALOG_OPERATIONS
      Source Finding: S7 cc_composition append_operation
    - Owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): INPUT
      Field: actor_id
      Bound To: inputs.staff_id
      Source Finding: S7 cc_composition append_operation
    - Owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): OUTPUT
      Field: record_id
      Bound To: capability_result.record_id
      Source Finding: S7 cc_composition append_operation
    - Owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Step: append_operation
      Direction (INPUT, OUTPUT): OUTPUT
      Field: sequence_number
      Bound To: capability_result.sequence_number
      Source Finding: S7 cc_composition append_operation
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
      Field: book_fields
      Bound To: payload.book_fields
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
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_REINSTATE_BOOK_RECORD_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REINSTATE_BOOK_RECORD
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REINSTATE_BOOK_RECORD'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: barcode
      Bound To: payload.barcode
      Source Finding: S7 execution_topology CC_REINSTATE_PHYSICAL_COPY_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: REINSTATE_PHYSICAL_COPY
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''REINSTATE_PHYSICAL_COPY'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.barcode''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: search_criteria
      Bound To: payload.search_criteria
      Source Finding: S7 execution_topology CC_SEARCH_CATALOG_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: SEARCH_CATALOG
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''SEARCH_CATALOG'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.search_criteria''}'
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_credentials
      Bound To: payload.staff_credentials
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: authorization_rules
      Bound To: payload.authorization_rules
      Source Finding: S7 execution_topology CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: identity_key
      Bound To: payload.identity_key
      Source Finding: S7 execution_topology CC_ASSEMBLE_BOOK_DETAILS_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: copy_criteria
      Bound To: '{''identity_key'': ''$.payload.identity_key''}'
      Source Finding: S7 execution_topology CC_ASSEMBLE_BOOK_DETAILS_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: staff_id
      Bound To: payload.staff_id
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: operation
      Bound To: RETRIEVE_BOOK_DETAILS
      Source Finding: S7 execution_topology CC_APPEND_CATALOG_OPERATION_V0
    - Owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT): INPUT
      Field: record
      Bound To: '{''operation'': ''RETRIEVE_BOOK_DETAILS'', ''staff_id'': ''$.payload.staff_id'', ''subject'': ''$.payload.identity_key''}'
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
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The title the book is published under
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The author the book is published under
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: publication_year
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The year this edition was published
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The book's bibliographic information
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields a book record must carry, as the rules its structure is validated against
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: copy_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The copy's recorded detail
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: copy_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The copy's recorded detail
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The title the book is published under
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The author the book is published under
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: publication_year
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The year this edition was published
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: updated_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The changed bibliographic information
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: search_criteria
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: What staff are searching by, and the states to include
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_credentials
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Who is performing the operation, as the catalog receives it
    - Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: authorization_rules
      Type: array
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The rules the staff member's credentials are checked against
    - Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: is_authorized
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the staff member may perform catalog operations
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
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: valid
      Type: boolean
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Whether the submission may proceed to be claimed and written
    - Artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The title the book is published under
    - Artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The author the book is published under
    - Artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: publication_year
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The year this edition was published
    - Artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Where the claimed key resolves to
    - Artifact: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: target_ref
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Where the registered key resolves to
    - Artifact: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: address
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: Where the claimed key resolves to
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The book's bibliographic information
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: book_schema
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The fields a book record must carry, as the rules its structure is validated against
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: book_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The book's authoritative record
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: copy_fields
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The copy's recorded detail
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: book_record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The book's authoritative record
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
    - Artifact: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: updated_count
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many records the state change matched and updated
    - Artifact: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: updated_count
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many records the state change matched and updated
    - Artifact: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: updated_count
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many records the state change matched and updated
    - Artifact: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: updated_count
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: How many records the state change matched and updated
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
    - Artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: record
      Type: object
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The account of the performed operation
    - Artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: operation
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: operation
    - Artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: record_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The identity of the appended trail entry
    - Artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: sequence_number
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The entry's position in the trail
    - Artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The title the book is published under
    - Artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The author the book is published under
    - Artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: publication_year
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The year this edition was published
    - Artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::EV_BOOK_RETIRED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::EV_BOOK_RETIRED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: barcode
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The barcode the library assigned to the copy
    - Artifact: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member recorded against the operation in the audit trail
    - Artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: title
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The title the book is published under
    - Artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: author
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The author the book is published under
    - Artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): INPUT
      Field: publication_year
      Type: integer
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The year this edition was published
    - Artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): OUTPUT
      Field: identity_key
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The key formed from a book's title, author and publication year
    - Artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: staff_id
      Type: string
      Required (YES, NO): 'YES'
      Default: ''
      Meaning: The staff member's identity as the library knows it
    - Artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: authorized
      Type: boolean
      Required (YES, NO): 'NO'
      Default: 'false'
      Meaning: Whether the staff member may perform catalog operations; decided by the staff function, read here
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
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Module: book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_form_book_identity_key_v0
      Callable: execute
      Operation: PURE_FORM_BOOK_IDENTITY_KEY
      Kind (atom, molecule): atom
      Purity (ct_pure, ct_impure): ct_pure
      Refusal (raises, returns, never): never
      Source Finding: S7 new_artifacts CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
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
    - Artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Property: type
      Value: ENDUSER
      Source Finding: S5 provisional_codes AC_LIBRARY_STAFF_V0
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
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
      Count: '40'
      Artifacts: 1 AC, 9 IN, 9 WF, 13 CC, 1 CT, 5 EV, 1 RB, 1 STRUCTURE
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: platform
      Count: '1'
      Artifacts: capability_side_effects::CS_MUTABLE_JSON_V0
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
    - Operation: Register a book
      Refused When: Its title, author and publication year match a registered book.
      Act: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Outcome: ALREADY_EXISTS
      Source Finding: 'S0 operation_refusals #1'
    - Operation: Register a book
      Refused When: No physical copy is offered with it.
      Act: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #2'
    - Operation: Register a book
      Refused When: It carries no subject.
      Act: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #3'
    - Operation: Register a physical copy
      Refused When: The book it names is not registered.
      Act: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Outcome: NOT_FOUND
      Source Finding: 'S0 operation_refusals #4'
    - Operation: Register a physical copy
      Refused When: Its barcode matches a copy the library already owns.
      Act: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Outcome: ALREADY_EXISTS
      Source Finding: 'S0 operation_refusals #5'
    - Operation: Update bibliographic information
      Refused When: The changed title, author and publication year would match another registered book.
      Act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #6'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_REGISTER_BOOK_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
    - Operation: Any catalog operation
      Refused When: The staff member performing it is not authorized.
      Act: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Outcome: VIOLATION
      Source Finding: 'S0 operation_refusals #7'
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
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Expected Outcome (SUCCESS, VIOLATION): SUCCESS
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: refuses_blank_title
      Expected Outcome (SUCCESS, VIOLATION): VIOLATION
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
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: title
      Value: '"THE ODYSSEY"'
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: author
      Value: Homer
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: publication_year
      Value: '1614'
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: forms_normalized_key
      Role (INPUT, EXPECTED, ASSERT, RECORDED): EXPECTED
      Field: identity_key
      Value: the odyssey|homer|1614
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: refuses_blank_title
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: title
      Value: '" "'
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: refuses_blank_title
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: author
      Value: Homer
      Source Finding: human decision
    - CT Code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Case: refuses_blank_title
      Role (INPUT, EXPECTED, ASSERT, RECORDED): INPUT
      Field: publication_year
      Value: '1614'
      Source Finding: human decision
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows: []
```

> Every artifact below is either designed new or inventoried as existing. What is wrong is which side of that line each one falls on.

Every binding names a field the capability declares, read from the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d`.

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

Every status this design routes on — ACK, NACK, SUCCESS, NOT_FOUND, ALREADY_EXISTS, DENIED, VIOLATION,
BACKEND_ERROR — is already admitted, so no vocabulary is extended.

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

*Every artifact this design schedules is authored: construction renders it from the registers
above and it is its own source of truth. Nothing here is reached by invoking a generator.*

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
