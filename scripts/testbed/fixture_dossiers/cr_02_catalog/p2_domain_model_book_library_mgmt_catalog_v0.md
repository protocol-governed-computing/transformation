# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 2 — Domain Model Verification
  CR: cr_02_catalog
  Status: DRAFT
  Feeds: Stage 3 — Analysis Loop
registers:
  entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Evidence Status
    - Source Finding
    rows:
    - Entity: Work
      Description: A published work, recognizable as one thing across the editions in which it is published.
      Store Model: None — the composition holds no store for a work, and nothing groups records that describe one.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Entity: Edition
      Description: A publication of a work, identified by title, author and publication year. The record the previous change calls a book is an edition.
      Store Model: A durable record store keyed by the identifying attributes, holding one record per edition.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Entity: Physical Copy
      Description: An individual copy the library owns, belonging to exactly one edition.
      Store Model: A durable record store keyed by barcode, holding one record per copy.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #4'
    - Entity: Bibliographic Information
      Description: An edition's descriptive content.
      Store Model: Held within the edition's own record.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Entity: Edition Summary
      Description: Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean.
      Store Model: None — search results carry one edition's bibliographic information and nothing about a work.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Entity: Work Summary
      Description: A short description of the work an edition belongs to, carried in that edition's retrieval.
      Store Model: None — retrieval carries the edition and its copies and nothing about a work.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Entity: Existing Catalog Record
      Description: A catalog record written under the previous governed change, before this one.
      Store Model: The same store the edition occupies; the composition declares the store, not its contents.
      Evidence Status: INFERRED
      Source Finding: 'S2 belief_verification #7'
    - Entity: Authorized Staff
      Description: A library staff member permitted to perform catalog operations.
      Store Model: None — the catalog requires authorization and does not decide it.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Entity: Business Operation
      Description: An action performed against the catalog that must be traceable and auditable.
      Store Model: An append-only trail holding one entry per performed operation.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
  entity_attributes:
    columns:
    - Entity
    - Attribute
    - Meaning
    - Evidence Status
    - Source Finding
    rows:
    - Entity: Work
      Attribute: Title
      Meaning: The work's title, shared by every edition of it.
      Evidence Status: INFERRED
      Source Finding: 'S1 identity_and_sameness #1'
    - Entity: Work
      Attribute: Author
      Meaning: The work's author, shared by every edition of it.
      Evidence Status: INFERRED
      Source Finding: 'S1 identity_and_sameness #1'
    - Entity: Edition
      Attribute: Title
      Meaning: The edition's title, one of the three attributes that identify it.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Entity: Edition
      Attribute: Author
      Meaning: The edition's author, one of the three attributes that identify it.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Entity: Edition
      Attribute: Publication Year
      Meaning: The year of publication, the attribute that distinguishes one edition of a work from another.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Entity: Edition
      Attribute: Subject
      Meaning: What kind of material it is, stated as free text, and what staff search on.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Entity: Edition
      Attribute: State
      Meaning: Whether the edition's record is registered or retired.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #6'
    - Entity: Edition
      Attribute: Identifying Key
      Meaning: The single value formed from title, author and publication year, claimed so that no two editions share it.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Entity: Physical Copy
      Attribute: Barcode
      Meaning: The identifier the library assigns to a copy, which distinguishes it from every other copy.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #4'
    - Entity: Physical Copy
      Attribute: Edition Identity
      Meaning: The edition the copy belongs to, recorded on the copy.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #4'
    - Entity: Physical Copy
      Attribute: State
      Meaning: Whether the copy's record is registered or retired.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #6'
    - Entity: Business Operation
      Attribute: Operation Record
      Meaning: What was performed, by whom, against which record.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
  business_processes:
    columns:
    - Process
    - Initiator
    - Outcome
    - Evidence Status
    - Source Finding
    rows:
    - Process: Register an edition of a work the catalog does not yet hold
      Initiator: Authorized staff
      Outcome: The work enters the catalog with its first edition and that edition's first copy.
      Evidence Status: INFERRED
      Source Finding: 'S1 requested_outcomes #1'
    - Process: Register an additional edition of an existing work
      Initiator: Authorized staff
      Outcome: A further edition is recorded against a work the catalog already holds.
      Evidence Status: INFERRED
      Source Finding: 'S1 requested_outcomes #2'
    - Process: Search the catalog
      Initiator: Authorized staff
      Outcome: One result per matching work, carrying enough of a summary of that work's editions to choose one.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Retrieve an edition's complete details
      Initiator: Authorized staff
      Outcome: The edition's bibliographic information, the physical copies of it, and a summary of the work it belongs to.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Register a physical copy
      Initiator: Authorized staff
      Outcome: A copy is recorded against exactly one edition.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #4'
    - Process: Update bibliographic information
      Initiator: Authorized staff
      Outcome: A registered edition's descriptive content changes.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Retire a record
      Initiator: Authorized staff
      Outcome: An edition or a copy is judged obsolete and is no longer to be used.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Reinstate a record
      Initiator: Authorized staff
      Outcome: A retired edition or copy returns to the registered state.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #6'
  process_steps:
    columns:
    - Process
    - 'Step #'
    - Action
    - Record Produced
    - Evidence Status
    - Source Finding
    rows:
    - Process: Register an edition of a work the catalog does not yet hold
      'Step #': '1'
      Action: Confirm the staff member is authorized.
      Record Produced: None
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Register an edition of a work the catalog does not yet hold
      'Step #': '2'
      Action: Validate the submission carries what an edition requires.
      Record Produced: None
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Register an edition of a work the catalog does not yet hold
      'Step #': '3'
      Action: Claim the work, identified by title and author.
      Record Produced: A work record
      Evidence Status: INFERRED
      Source Finding: 'S1 identity_and_sameness #1'
    - Process: Register an edition of a work the catalog does not yet hold
      'Step #': '4'
      Action: Claim the edition's identity, so no two editions share title, author and publication year.
      Record Produced: An identity claim
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Process: Register an edition of a work the catalog does not yet hold
      'Step #': '5'
      Action: Claim the first copy's barcode.
      Record Produced: A barcode claim
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #4'
    - Process: Register an edition of a work the catalog does not yet hold
      'Step #': '6'
      Action: Write the edition record and its first copy record.
      Record Produced: An edition record and a copy record
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Process: Register an edition of a work the catalog does not yet hold
      'Step #': '7'
      Action: Record the operation in the audit trail.
      Record Produced: An operation entry
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Register an additional edition of an existing work
      'Step #': '1'
      Action: Confirm the staff member is authorized.
      Record Produced: None
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Register an additional edition of an existing work
      'Step #': '2'
      Action: Resolve the work the edition belongs to, by title and author.
      Record Produced: None
      Evidence Status: INFERRED
      Source Finding: 'S1 identity_and_sameness #1'
    - Process: Register an additional edition of an existing work
      'Step #': '3'
      Action: Claim the edition's identity, so no two editions of the work share a publication year.
      Record Produced: An identity claim
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Process: Register an additional edition of an existing work
      'Step #': '4'
      Action: Write the edition record against the resolved work.
      Record Produced: An edition record
      Evidence Status: INFERRED
      Source Finding: 'S1 requested_outcomes #2'
    - Process: Register an additional edition of an existing work
      'Step #': '5'
      Action: Record the operation in the audit trail.
      Record Produced: An operation entry
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Search the catalog
      'Step #': '1'
      Action: Confirm the staff member is authorized.
      Record Produced: None
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Search the catalog
      'Step #': '2'
      Action: Select the registered editions matching the stated subject or title, excluding retired ones.
      Record Produced: None
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Search the catalog
      'Step #': '3'
      Action: Group the matching editions by the work they belong to.
      Record Produced: None
      Evidence Status: INFERRED
      Source Finding: 'S1 requested_outcomes #3'
    - Process: Search the catalog
      'Step #': '4'
      Action: Return one result per work, carrying a summary of its matching editions.
      Record Produced: A search result
      Evidence Status: INFERRED
      Source Finding: 'S1 requested_outcomes #3'
    - Process: Retrieve an edition's complete details
      'Step #': '1'
      Action: Confirm the staff member is authorized.
      Record Produced: None
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Retrieve an edition's complete details
      'Step #': '2'
      Action: Read the named edition and the physical copies of it.
      Record Produced: None
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Process: Retrieve an edition's complete details
      'Step #': '3'
      Action: Read a summary of the work the edition belongs to.
      Record Produced: None
      Evidence Status: INFERRED
      Source Finding: 'S1 requested_outcomes #4'
    - Process: Retrieve an edition's complete details
      'Step #': '4'
      Action: Return the edition, its copies and the work summary.
      Record Produced: A retrieval result
      Evidence Status: INFERRED
      Source Finding: 'S1 requested_outcomes #4'
  belief_verification:
    columns:
    - Belief
    - Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE)
    - Evidence
    - Source Finding
    rows:
    - Belief: The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: The pinned composition declares six domains and carries forty-three artifacts in the book_library_mgmt namespace, among them book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 and book_library_mgmt::RB_CATALOG_BINDINGS_V0, which declare the subdomain's stores and bind its workflows to them.
      Source Finding: 'S1 system_beliefs #1'
    - Belief: The catalog is believed to hold bibliographic records and physical copies of library materials.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: 'book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 declares five stores: one for book records, one for physical copies, an append-only operations trail, and two uniqueness registries. book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 write the first two.'
      Source Finding: 'S1 system_beliefs #2'
    - Belief: A book is believed to be identified by title, author and publication year.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 forms one key from exactly those three attributes, and book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 claims that key so a second record carrying the same three is refused. book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 resolves a record by the same key.
      Source Finding: 'S1 system_beliefs #3'
    - Belief: A physical copy is believed to belong to exactly one book.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 records a copy against one book record, and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 claims its barcode so no two copies share one.
      Source Finding: 'S1 system_beliefs #4'
    - Belief: The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: 'Nine workflows serve them: book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0. Every one admits only an authorized staff member, through book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0.'
      Source Finding: 'S1 system_beliefs #5'
    - Belief: A retired record is believed to be reinstatable.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 return a retired record to the registered state, reached through book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0.
      Source Finding: 'S1 system_beliefs #6'
    - Belief: Records written under the previous change are believed to exist and to be readable.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): INSUFFICIENT_EVIDENCE
      Evidence: The composition declares the stores and the paths they occupy; it does not carry their contents. Whether any record was ever written is runtime state, and no inspection of a sealed snapshot can answer it. The belief is resolvable only by reading a store the previous change wrote.
      Source Finding: 'S1 system_beliefs #7'
  pps_baseline_fqdns:
    columns:
    - Capability
    - FQDN
    - What It Does
    - Fit (EXACT, PARTIAL, MISMATCH)
    - Cannot Do
    rows:
    - Capability: Catalog storage declaration
      FQDN: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      What It Does: Declares the five stores the catalog owns and the paths they occupy.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It declares no store for a work, and no store in which the grouping of editions under a work could be held.
    - Capability: Edition identity key
      FQDN: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      What It Does: Forms one key from title, author and publication year.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It forms an edition's key; the work's key of title and author alone is not a key it forms.
    - Capability: Edition identity claim
      FQDN: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      What It Does: Claims the identifying key so that no two records share title, author and publication year.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It claims one edition; it neither claims a work nor relates two editions that share a title and an author.
    - Capability: Edition identity resolution
      FQDN: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      What It Does: Resolves a registered record by its identifying key.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It resolves one edition by its own key and cannot answer which work an edition belongs to.
    - Capability: Register an edition
      FQDN: book_library_mgmt::CC_REGISTER_BOOK_V0
      What It Does: Confirms authorization, validates the submission, claims identity and barcode, writes the record and its first copy, and records the operation.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It registers an edition standing alone; nothing in it claims or resolves the work the edition belongs to.
    - Capability: Validate a submission
      FQDN: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      What It Does: Confirms a registration carries what a record requires before anything is claimed or written.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It validates an edition's own attributes and knows nothing a work would require.
    - Capability: Register a physical copy
      FQDN: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      What It Does: Records a copy against one existing record and claims its barcode.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing — a copy already belongs to exactly one edition, which is what this change requires of it.
    - Capability: Barcode claim
      FQDN: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      What It Does: Claims a copy's barcode so no two copies share one.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It is unaffected by the work abstraction.
    - Capability: Search the catalog
      FQDN: book_library_mgmt::CC_SEARCH_CATALOG_V0
      What It Does: Selects registered records matching a stated subject or title and excludes retired ones.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It returns one result per matching edition. It cannot group editions under the work they belong to, and returns three near-identical results where the library wants one.
    - Capability: Retrieve complete details
      FQDN: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      What It Does: Assembles one record's bibliographic information together with the physical copies of it.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It carries no summary of the work the record belongs to, so the work's title cannot be shown without a second lookup.
    - Capability: Update bibliographic information
      FQDN: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      What It Does: Changes a registered record's descriptive content and refuses a change that would duplicate another record.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It refuses duplication at the edition level, which is where this change leaves it.
    - Capability: Retire a record
      FQDN: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      What It Does: Retires one record and cascades to nothing.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It retires an edition, which is what this change requires; a work is not retired.
    - Capability: Retire a physical copy
      FQDN: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      What It Does: Retires one copy and leaves its record unaffected.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It is unaffected by the work abstraction.
    - Capability: Reinstate a record
      FQDN: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      What It Does: Returns a retired record to the registered state.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It is unaffected by the work abstraction.
    - Capability: Reinstate a physical copy
      FQDN: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      What It Does: Returns a retired copy to the registered state.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It is unaffected by the work abstraction.
    - Capability: Audit the operation
      FQDN: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      What It Does: Appends one performed operation to the catalog's own append-only trail.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It records whatever operation it is handed, including ones this change adds.
    - Capability: Staff authorization check
      FQDN: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      What It Does: Confirms the staff member performing an operation is authorized.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It requires authorization and does not decide it, which this change leaves unchanged.
    - Capability: Catalog entry points
      FQDN: book_library_mgmt::IN_REGISTER_BOOK_V0
      What It Does: Admits a registration request and declares what a caller must supply.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It admits an edition's attributes and names no work.
    - Capability: Search entry point
      FQDN: book_library_mgmt::IN_SEARCH_CATALOG_V0
      What It Does: Admits a search request stating a subject or a title.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It admits the search terms this change keeps; what changes is the shape of the answer.
    - Capability: Retrieval entry point
      FQDN: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      What It Does: Admits a request for one record's complete details.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It names the record to retrieve and carries nothing that would ask for the work.
    - Capability: Runtime binding declaration
      FQDN: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      What It Does: Binds the catalog's workflows to the stores and policies they use.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the five stores that exist; a store for works would have to be bound here too.
    - Capability: Business moments
      FQDN: book_library_mgmt::EV_BOOK_REGISTERED_V0
      What It Does: Declares the moment a record enters the catalog.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It names the registration of an edition; the moment a work enters the catalog has no declaration.
    - Capability: Durable record store
      FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      What It Does: Writes, reads, selects, lists, updates in place and deletes durable records.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It holds whatever it is given; it enforces no identity and no grouping.
    - Capability: Uniqueness registry
      FQDN: capability_side_effects::CS_REGISTRY_V0
      What It Does: Registers a key, resolves it, and reports whether it exists.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It enforces uniqueness on one key; grouping editions under a work is not something it expresses.
    - Capability: Record selection
      FQDN: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      What It Does: Selects the records matching stated criteria.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It selects records; it does not group the selected records by an attribute they share.
  gaps:
    columns:
    - Gap
    - Severity
    - Impact
    - Evidence Status
    - Source Finding
    rows:
    - Gap: The catalog has no work — nothing in the composition represents the thing that several editions are editions of.
      Severity: CRITICAL
      Impact: 'Every outcome this change requests rests on it: an additional edition has nothing to be registered against, a search cannot group by it, and a retrieval cannot summarise it.'
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Gap: No store holds a work, and the storage declaration has no place to put one.
      Severity: CRITICAL
      Impact: A work that is derived at read time and never recorded cannot be claimed, cannot be resolved, and cannot be shown to have exactly one authoritative record.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #1'
    - Gap: Nothing claims a work's identity of title and author, as the edition's identity of title, author and publication year is claimed.
      Severity: CRITICAL
      Impact: Without a claim, two registrations describing the same work would produce two works, and the invariant that no two works share a title and an author is unenforceable.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Gap: Search returns one result per matching edition and cannot group its results by work.
      Severity: CRITICAL
      Impact: The requested outcome is one result per work carrying a summary of its editions; the existing search answers a different question.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Gap: Retrieval carries no summary of the work a record belongs to.
      Severity: CRITICAL
      Impact: Staff selecting an edition from a search result would have to look the work up separately, which is what carrying the summary exists to avoid.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Gap: Registering an edition neither resolves nor creates the work it belongs to.
      Severity: CRITICAL
      Impact: Registering an additional edition of an existing work is the change's central operation and has no path through the existing registration.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Gap: Records written under the previous change carry no work membership, and whether any such record exists cannot be established from the composition.
      Severity: OPEN QUESTION
      Impact: The promise that existing records remain valid without recreation is about data. It is not testable against a snapshot, only against a store the previous change wrote.
      Evidence Status: INFERRED
      Source Finding: 'S2 belief_verification #7'
    - Gap: No business moment is declared for a work entering the catalog.
      Severity: MINOR
      Impact: The moments this change adds would go unrecognised while the edition's own moments continue to be declared.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #1'
    - Gap: Deciding which staff are authorized still belongs to a function that does not exist.
      Severity: MINOR
      Impact: Unchanged by this change, and deferred by the business to the staff function.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
  architectural_observations:
    columns:
    - Observation
    - Evidence
    - Evidence Status
    - Source Finding
    rows:
    - Observation: The record the previous change calls a book is identified by exactly the three attributes that identify an edition, and two records differing only in publication year are already two records. The existing catalog therefore already distinguishes editions, and what it has never had is the work above them.
      Evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 · book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Observation: A physical copy is recorded against one record and claims its own barcode, so a copy already belongs to exactly one edition and needs no change at all.
      Evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 · book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #4'
    - Observation: Uniqueness in this composition is claimed through a registry keyed on one value, and the existing edition key is formed by a pure transform before it is claimed. A work's key of title and author could be formed and claimed the same way.
      Evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 · capability_side_effects::CS_REGISTRY_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Observation: Every catalog operation is composed as an ordered pipeline that confirms authorization first and records the operation last, so an operation this change adds has a worked shape to follow.
      Evidence: book_library_mgmt::CC_REGISTER_BOOK_V0 · book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 · book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Observation: Selecting records by stated criteria is available as a pure transform, and grouping the selected records by an attribute they share is not.
      Evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Observation: The subdomain owns its five stores and binds its own workflows to them, so a store for works would be declared and bound in the subdomain's own declarations.
      Evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 · book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #1'
    - Observation: Retirement is declared on the record the previous change calls a book and cascades to nothing, which is exactly what retiring an edition independently of a work's other editions requires.
      Evidence: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 · book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #6'
  discovery_concerns:
    columns:
    - Concern
    - Evidence
    - Severity
    - Evidence Status
    - Source Finding
    rows:
    - Concern: The promise that existing records remain valid without recreation cannot be verified at this stage at all. The composition declares stores and paths; it does not carry what is in them, and a snapshot has no way to say whether the previous change ever wrote a record. The promise is a claim about data, and only execution against a store the previous change wrote can settle it.
      Evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Severity: CRITICAL
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #7'
    - Concern: The existing search is the one existing capability whose answer this change alters, and it is also the one every existing acceptance criterion about search was written against. Grouping its results by work changes the shape of what staff already receive, and the business has accepted that as an extension rather than a regression.
      Evidence: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Severity: MAJOR
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
    - Concern: The work an existing record belongs to is derivable from the record's own title and author, but deriving it at read time and recording it are different things. If a work is claimed, every record written before this change needs a claim it never made; if it is not, the work has no authoritative record.
      Evidence: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Severity: MAJOR
      Evidence Status: INFERRED
      Source Finding: 'S2 belief_verification #3'
    - Concern: The registration this change extends already claims two identities and writes two records before it audits, and it was reordered during the previous change so that every claim precedes every write. Adding a work claim to it touches the sequence that ordering was established to protect.
      Evidence: book_library_mgmt::CC_REGISTER_BOOK_V0 · book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Severity: MAJOR
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
  open_questions:
    columns:
    - Question
    - Category
    - Why It Matters
    - Source Finding
    rows: []
```

Every belief the change request declared is resolved against the pinned composition, and every other
register projects from those resolutions. This is the first change request whose baseline contains a
subdomain the pipeline itself built: what already exists here is the previous catalog change's own
output.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
