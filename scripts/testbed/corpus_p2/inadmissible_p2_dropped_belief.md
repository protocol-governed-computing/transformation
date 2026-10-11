# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 2 — Domain Model Verification
  CR: cr_01_catalog
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
    - Entity: Book
      Description: A published material the library catalogs — the general term for anything it catalogs, including materials that are not books.
      Store Model: One durable record per book, addressed by its title, author and publication year together, updatable in place, and markable retired and registered again.
      Evidence Status: INFERRED
      Source Finding: 'S1 business_vocabulary Book · S1 identity_and_sameness #1'
    - Entity: Physical Copy
      Description: An individual copy the library owns, belonging to exactly one book.
      Store Model: One durable record per copy, addressed by its barcode, naming the single book it belongs to, and markable retired and registered again.
      Evidence Status: INFERRED
      Source Finding: 'S1 business_vocabulary Physical Copy · S1 identity_and_sameness #2'
  entity_attributes:
    columns:
    - Entity
    - Attribute
    - Meaning
    - Evidence Status
    - Source Finding
    rows:
    - Entity: Book
      Attribute: Title
      Meaning: The title the book is published under; part of what identifies it.
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — a book's bibliographic information is title, author, publication year and subject
    - Entity: Book
      Attribute: Author
      Meaning: The author the book is published under; part of what identifies it.
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — bibliographic information
    - Entity: Book
      Attribute: Publication Year
      Meaning: The year this edition was published; part of what identifies it, and what distinguishes one edition from another.
      Evidence Status: INFERRED
      Source Finding: 'S1 identity_and_sameness #1'
    - Entity: Book
      Attribute: Subject
      Meaning: What kind of book it is. A book carries at least one and may carry several.
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — a book carries at least one subject and may carry several
    - Entity: Book
      Attribute: State
      Meaning: Whether the book is registered or retired.
      Evidence Status: INFERRED
      Source Finding: S1 lifecycle_states Book
    - Entity: Physical Copy
      Attribute: Barcode
      Meaning: The identifier the library assigns to this copy; what identifies it among all copies the library owns.
      Evidence Status: INFERRED
      Source Finding: 'S1 identity_and_sameness #2'
    - Entity: Physical Copy
      Attribute: Book
      Meaning: The single book this copy belongs to.
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — each physical copy belongs to exactly one book
    - Entity: Physical Copy
      Attribute: State
      Meaning: Whether the copy is registered or retired.
      Evidence Status: INFERRED
      Source Finding: S1 lifecycle_states Physical Copy
  business_processes:
    columns:
    - Process
    - Initiator
    - Outcome
    - Evidence Status
    - Source Finding
    rows:
    - Process: Register a book
      Initiator: Authorized staff
      Outcome: The catalog holds one authoritative record for the book, and one for the physical copy registered with it.
      Evidence Status: INFERRED
      Source Finding: S1 business_events Book Registered
    - Process: Register a physical copy
      Initiator: Authorized staff
      Outcome: The catalog holds one authoritative record for a further copy of a registered book.
      Evidence Status: INFERRED
      Source Finding: S1 business_events Physical Copy Registered
    - Process: Update bibliographic information
      Initiator: Authorized staff
      Outcome: The book's authoritative description reflects the change, or the update is refused for making the book a duplicate of another.
      Evidence Status: INFERRED
      Source Finding: S1 business_events Bibliographic Information Updated
    - Process: Retire a book record
      Initiator: Authorized staff
      Outcome: The book record is retired, excluded from search, still retrievable, and its copies unaffected.
      Evidence Status: INFERRED
      Source Finding: S1 business_events Book Retired
    - Process: Retire a physical copy
      Initiator: Authorized staff
      Outcome: The copy record is retired and the book record is unaffected, including when it was the last copy.
      Evidence Status: INFERRED
      Source Finding: S1 business_events Physical Copy Retired
    - Process: Reinstate a book record
      Initiator: Authorized staff
      Outcome: The retired book record is registered again and appears in search.
      Evidence Status: INFERRED
      Source Finding: 'S1 lifecycle_transitions #3'
    - Process: Reinstate a physical copy
      Initiator: Authorized staff
      Outcome: The retired copy record is registered again.
      Evidence Status: INFERRED
      Source Finding: 'S1 lifecycle_transitions #6'
    - Process: Search the catalog
      Initiator: Authorized staff
      Outcome: The bibliographic information of each registered book matching the subject or title searched for.
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — staff search the catalog by subject or by title
    - Process: Retrieve complete book details
      Initiator: Authorized staff
      Outcome: The book's bibliographic information and the physical copies the library holds of it.
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — retrieving complete book details returns the bibliographic information and the copies
  process_steps:
    columns:
    - Process
    - 'Step #'
    - Action
    - Record Produced
    - Evidence Status
    - Source Finding
    rows:
    - Process: Register a book
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Register a book
      'Step #': '2'
      Action: Confirm at least one physical copy is offered with the book
      Record Produced: A completeness decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #2'
    - Process: Register a book
      'Step #': '3'
      Action: Confirm the book carries at least one subject
      Record Produced: A completeness decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #3'
    - Process: Register a book
      'Step #': '4'
      Action: Confirm no registered book already carries this title, author and publication year
      Record Produced: A sameness decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #1'
    - Process: Register a book
      'Step #': '5'
      Action: Record the book's bibliographic information as its authoritative record, registered
      Record Produced: The book record
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — each book has exactly one authoritative record
    - Process: Register a book
      'Step #': '6'
      Action: Record the offered copy against the book, registered
      Record Produced: The physical copy record
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — registering a book requires at least one physical copy
    - Process: Register a book
      'Step #': '7'
      Action: Record that the book was registered
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — every business operation is traceable and auditable
    - Process: Register a physical copy
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Register a physical copy
      'Step #': '2'
      Action: Confirm the book the copy names is registered in the catalog
      Record Produced: An existence decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #4'
    - Process: Register a physical copy
      'Step #': '3'
      Action: Confirm no copy the library owns already carries this barcode
      Record Produced: A sameness decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #5'
    - Process: Register a physical copy
      'Step #': '4'
      Action: Record the copy against that book, registered
      Record Produced: The physical copy record
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — each copy has exactly one authoritative record
    - Process: Register a physical copy
      'Step #': '5'
      Action: Record that the copy was registered
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — traceable and auditable
    - Process: Update bibliographic information
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Update bibliographic information
      'Step #': '2'
      Action: Confirm the changed title, author and publication year would not match another registered book
      Record Produced: A sameness decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #6'
    - Process: Update bibliographic information
      'Step #': '3'
      Action: Record the changed bibliographic information as the book's authoritative description
      Record Produced: The updated book record
      Evidence Status: INFERRED
      Source Finding: S1 business_events Bibliographic Information Updated
    - Process: Update bibliographic information
      'Step #': '4'
      Action: Record that the book's information was updated
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — traceable and auditable
    - Process: Retire a book record
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Retire a book record
      'Step #': '2'
      Action: Record the book record as retired, leaving its copies as they are
      Record Produced: The retired book record
      Evidence Status: INFERRED
      Source Finding: 'S1 lifecycle_transitions #2'
    - Process: Retire a book record
      'Step #': '3'
      Action: Record that the book was retired
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — traceable and auditable
    - Process: Retire a physical copy
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Retire a physical copy
      'Step #': '2'
      Action: Record the copy as retired, leaving the book record as it is
      Record Produced: The retired copy record
      Evidence Status: INFERRED
      Source Finding: 'S1 lifecycle_transitions #5'
    - Process: Retire a physical copy
      'Step #': '3'
      Action: Record that the copy was retired
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — traceable and auditable
    - Process: Reinstate a book record
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Reinstate a book record
      'Step #': '2'
      Action: Record the retired book record as registered again
      Record Produced: The registered book record
      Evidence Status: INFERRED
      Source Finding: 'S1 lifecycle_transitions #3'
    - Process: Reinstate a book record
      'Step #': '3'
      Action: Record that the book was returned to the registered state
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — traceable and auditable
    - Process: Reinstate a physical copy
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Reinstate a physical copy
      'Step #': '2'
      Action: Record the retired copy as registered again
      Record Produced: The registered copy record
      Evidence Status: INFERRED
      Source Finding: 'S1 lifecycle_transitions #6'
    - Process: Reinstate a physical copy
      'Step #': '3'
      Action: Record that the copy was returned to the registered state
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — traceable and auditable
    - Process: Search the catalog
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Search the catalog
      'Step #': '2'
      Action: Select the registered books whose subject or title matches what was searched for, excluding retired books
      Record Produced: The matching set
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — a retired book is excluded from search results
    - Process: Search the catalog
      'Step #': '3'
      Action: Return the bibliographic information of each matching book, and nothing about its copies
      Record Produced: The search result
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — a search returns the bibliographic information of each matching book
    - Process: Search the catalog
      'Step #': '4'
      Action: Record that the catalog was searched
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — traceable and auditable
    - Process: Retrieve complete book details
      'Step #': '1'
      Action: Confirm the staff member is authorized to perform catalog operations
      Record Produced: An authorization decision
      Evidence Status: INFERRED
      Source Finding: 'S1 operation_refusals #7'
    - Process: Retrieve complete book details
      'Step #': '2'
      Action: Read the book's authoritative record, whether registered or retired
      Record Produced: The book record
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — a retired book's details remain retrievable
    - Process: Retrieve complete book details
      'Step #': '3'
      Action: Read the physical copies recorded against that book
      Record Produced: The copies held
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — complete details return the copies the library holds
    - Process: Retrieve complete book details
      'Step #': '4'
      Action: Record that the book's details were retrieved
      Record Produced: A durable, auditable record of the operation
      Evidence Status: INFERRED
      Source Finding: S1 business_invariants — traceable and auditable
  belief_verification:
    columns:
    - Belief
    - Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE)
    - Evidence
    - Source Finding
    rows:
    - Belief: book_library_mgmt does not appear to be part of the current software baseline.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): NOT_FOUND
      Evidence: The composition declares five domains — ai_governance, inspection, platform, transformation, workload — and its artifact index carries no identity in the book_library_mgmt namespace.
      Source Finding: 'S1 system_beliefs #1'
  pps_baseline_fqdns:
    columns:
    - Capability
    - FQDN
    - What It Does
    - Fit (EXACT, PARTIAL, MISMATCH)
    - Cannot Do
    rows:
    - Capability: Uniqueness registry
      FQDN: capability_side_effects::CS_REGISTRY_V0
      What It Does: Registers a key, resolves it, reports whether it exists, counts and deregisters.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It enforces uniqueness on one key; a book is identified by title, author and publication year together, and the composite is not a key it forms.
    - Capability: Durable record store
      FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      What It Does: Writes, reads, lists, updates in place and deletes durable records.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It holds whatever it is given; it enforces no identity, no state and no authorization.
    - Capability: Append-only trail
      FQDN: capability_side_effects::CS_APPENDONLY_JSONL_V0
      What It Does: Appends an entry and returns the whole trail.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It appends what it is handed; it does not decide which operations must be recorded.
    - Capability: Audit composition
      FQDN: ai_governance::CC_APPEND_AUDIT_EVENT_V0
      What It Does: Composes the recording of a performed action into an append-only store.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It carries agent-governance semantics and appends to another subdomain's store; a subdomain owns its stores exclusively.
    - Capability: Record shape validation
      FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      What It Does: Confirms a record carries the fields its contract declares.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It does not know which fields a book or a copy requires.
    - Capability: Record assembly
      FQDN: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      What It Does: Assembles a durable record from supplied values.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It applies no identity rule and decides no sameness.
    - Capability: Record selection
      FQDN: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      What It Does: Selects the records matching stated criteria.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It knows nothing of registered and retired, so exclusion of retired books must be stated as criteria.
    - Capability: Parameter rule validation
      FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      What It Does: Confirms supplied parameters satisfy declared rules.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It carries no catalog rule of its own.
    - Capability: Business actor
      FQDN: ai_governance::AC_EMPLOYEE_V0
      What It Does: Declares a business actor whose identity an operation binds.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It names an employee of another subdomain and asserts no authorization to perform catalog operations.
    - Capability: Business entry point
      FQDN: ai_governance::IN_PROVISION_AI_LICENSE_V0
      What It Does: Declares the governed entry point through which a business operation is requested.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It admits a licensing request, not a catalog operation.
    - Capability: Governed operation pipeline
      FQDN: ai_governance::CC_PROVISION_LICENSE_V0
      What It Does: Composes one business operation as an ordered pipeline of governed steps.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It carries licensing semantics; the catalog's operations must be authored.
    - Capability: Subdomain storage declaration
      FQDN: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
      What It Does: Declares the stores a business subdomain owns and the paths they occupy.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It declares another subdomain's stores.
    - Capability: Runtime binding declaration
      FQDN: ai_governance::RB_LICENSE_BINDINGS_V0
      What It Does: Binds a subdomain's workflows to the stores and policies they use.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It binds another subdomain's surface.
    - Capability: Business moment
      FQDN: ai_governance::EV_LICENSE_PROVISIONED_V0
      What It Does: Declares a business moment the domain recognises when an operation completes.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: It names a licensing moment, not a catalog one.
  gaps:
    columns:
    - Gap
    - Severity
    - Impact
    - Evidence Status
    - Source Finding
    rows:
    - Gap: Nothing in the composition holds a book record or a copy record.
      Severity: CRITICAL
      Impact: Every requested outcome depends on a durable authoritative record per book and per copy; the store mechanisms exist, the catalog's own stores do not.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Gap: No capability registers a book, registers a copy, updates bibliographic information, retires a record, reinstates a record, searches, or retrieves book details.
      Severity: CRITICAL
      Impact: The nine business processes have no counterpart in the composition and must all be authored.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Gap: No actor exists for library staff, and none asserts authorization to perform catalog operations.
      Severity: CRITICAL
      Impact: Every operation is refused unless the staff member is authorized, and there is nothing to bind that decision to.
      Evidence Status: OBSERVED
      Source Finding: 'S1 operation_refusals #7'
    - Gap: No business moment exists for a book or copy being registered, updated, retired or reinstated.
      Severity: CRITICAL
      Impact: Five business events are declared and none is recognised anywhere in the composition.
      Evidence Status: OBSERVED
      Source Finding: S1 business_events Book Registered
    - Gap: Uniqueness on a composite of title, author and publication year has no counterpart in the composition.
      Severity: CRITICAL
      Impact: Duplicate prevention is the business problem this change exists to solve, and the registry available enforces uniqueness on a single key.
      Evidence Status: OBSERVED
      Source Finding: 'S1 identity_and_sameness #1'
    - Gap: No audit trail belongs to the catalog; the only audit composition belongs to another subdomain.
      Severity: CRITICAL
      Impact: Every operation must be traceable, and a subdomain owns its stores exclusively.
      Evidence Status: OBSERVED
      Source Finding: S1 business_invariants — every business operation is traceable and auditable
    - Gap: Subject is free text, so searching by kind of book is only as consistent as what staff type into it.
      Severity: MINOR
      Impact: 'Noted, not modelled: the business has chosen free text, and no value-set validation applies.'
      Evidence Status: OBSERVED
      Source Finding: S1 known_facts — a book's subject is free text
    - Gap: Deciding which staff are authorized is deferred to the staff function, which does not exist.
      Severity: MINOR
      Impact: 'Noted, not modelled: the catalog reads authorization and never grants it.'
      Evidence Status: OBSERVED
      Source Finding: 'S1 authority_deferrals #1'
  architectural_observations:
    columns:
    - Observation
    - Evidence
    - Evidence Status
    - Source Finding
    rows:
    - Observation: A business subdomain in this composition declares its own stores and binds its own workflows to them, so a new subdomain has a worked precedent for owning its records.
      Evidence: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 · ai_governance::RB_LICENSE_BINDINGS_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #1'
    - Observation: Durable records that are written, read, listed and updated in place are available as a declared side effect, as is an append-only trail.
      Evidence: capability_side_effects::CS_MUTABLE_JSON_V0 · capability_side_effects::CS_APPENDONLY_JSONL_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Observation: Uniqueness is available as a declared side effect, keyed on a single value.
      Evidence: capability_side_effects::CS_REGISTRY_V0
      Evidence Status: OBSERVED
      Source Finding: 'S1 identity_and_sameness #1'
    - Observation: Pure transforms already exist for assembling a record, validating its shape, and selecting records by criteria.
      Evidence: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 · capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 · capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Observation: Recording a performed action into an append-only trail is already composed as a governed step, within another subdomain.
      Evidence: ai_governance::CC_APPEND_AUDIT_EVENT_V0
      Evidence Status: OBSERVED
      Source Finding: S1 business_invariants — traceable and auditable
    - Observation: 'The composition carries no business vocabulary for a library: no identity claims book, library, copy, subject, title or barcode.'
      Evidence: inspection::TI_SI_CATALOG_V0
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
  discovery_concerns:
    columns:
    - Concern
    - Evidence
    - Severity
    - Evidence Status
    - Source Finding
    rows:
    - Concern: The only composed audit step belongs to another subdomain, so satisfying traceability by reusing it would cross a subdomain's ownership of its own stores.
      Evidence: ai_governance::CC_APPEND_AUDIT_EVENT_V0 · ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
      Severity: MAJOR
      Evidence Status: OBSERVED
      Source Finding: S1 business_invariants — traceable and auditable
    - Concern: The available uniqueness mechanism is keyed on one value while a book is identified by three attributes together, so duplicate prevention needs a stated key rather than a direct reuse.
      Evidence: capability_side_effects::CS_REGISTRY_V0
      Severity: MAJOR
      Evidence Status: OBSERVED
      Source Finding: 'S1 identity_and_sameness #1'
    - Concern: Reinstatement means a record's state moves both ways, so state must be held as data on the record rather than implied by which store it is in.
      Evidence: capability_side_effects::CS_MUTABLE_JSON_V0
      Severity: MAJOR
      Evidence Status: INFERRED
      Source Finding: 'S1 lifecycle_transitions #3'
    - Concern: Search must exclude retired books while retrieval must not, so the same records are read under two different rules.
      Evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Severity: MINOR
      Evidence Status: INFERRED
      Source Finding: S1 known_facts — a retired book is excluded from search results
    - Concern: The one business actor available names an employee of another subdomain and asserts no authorization, so authorization has nothing to bind to until the staff function exists.
      Evidence: ai_governance::AC_EMPLOYEE_V0
      Severity: MINOR
      Evidence Status: OBSERVED
      Source Finding: 'S1 authority_deferrals #1'
  open_questions:
    columns:
    - Question
    - Category
    - Why It Matters
    - Source Finding
    rows: []
```

Every claim about what exists is grounded in the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d` — 292 artifacts across
ai_governance, inspection, platform, transformation, workload — read through the inspection interface.
The semantic model is inherited from Stage 1 and confirmed here, never re-derived.

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
