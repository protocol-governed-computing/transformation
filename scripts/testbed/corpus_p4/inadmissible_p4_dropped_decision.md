# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 4 — Business Model
  CR: cr_01_catalog
  Status: DRAFT
  Feeds: Stage 5 — Business Intent
registers:
  actors:
    columns:
    - Actor
    - Role
    - Authority Class
    - Source Finding
    rows:
    - Actor: Authorized staff member
      Role: Performs every catalog operation, and judges when a record is obsolete
      Authority Class: Operator
      Source Finding: S1 authority_boundaries The judgement that a record is obsolete
    - Actor: Library
      Role: Owns the physical copies the catalog describes, and assigns each copy its barcode
      Authority Class: Owner
      Source Finding: 'S1 identity_and_sameness #2'
    - Actor: Staff function
      Role: Decides which staff are authorized; not part of this change
      Authority Class: Deferred authority
      Source Finding: 'S1 authority_deferrals #1'
  bm_entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Source Finding
    rows:
    - Entity: Book
      Description: A published material the library catalogs — the general term for anything it catalogs
      Store Model: One durable record per book, addressed by title, author and publication year together, updatable in place, carrying its own state
      Source Finding: S2 entities Book
    - Entity: Physical Copy
      Description: An individual copy the library owns, belonging to exactly one book
      Store Model: One durable record per copy, addressed by its barcode, naming the one book it belongs to, carrying its own state
      Source Finding: S2 entities Physical Copy
  resources:
    columns:
    - Resource
    - Description
    - Source Finding
    rows:
    - Resource: Book records
      Description: The catalog's authoritative description of every book the library holds
      Source Finding: S2 entities Book
    - Resource: Physical copy records
      Description: The catalog's authoritative record of every copy the library owns
      Source Finding: S2 entities Physical Copy
    - Resource: Catalog audit trail
      Description: The catalog's own durable record of every operation performed against it
      Source Finding: 'S3 analysis_findings #1'
  events:
    columns:
    - Event
    - Trigger
    - Lifecycle Meaning
    - Source Finding
    rows:
    - Event: Book registered
      Trigger: Authorized staff register a new book together with its first physical copy
      Lifecycle Meaning: A book enters the catalog and acquires its authoritative record
      Source Finding: S1 business_events Book Registered
    - Event: Physical copy registered
      Trigger: Authorized staff register a further copy against a registered book
      Lifecycle Meaning: The library records another copy it owns
      Source Finding: S1 business_events Physical Copy Registered
    - Event: Bibliographic information updated
      Trigger: Authorized staff update a registered book's information
      Lifecycle Meaning: The authoritative description of a book changes
      Source Finding: S1 business_events Bibliographic Information Updated
    - Event: Book retired
      Trigger: Authorized staff retire a book record judged obsolete
      Lifecycle Meaning: The record is no longer to be used, and is excluded from search
      Source Finding: S1 business_events Book Retired
    - Event: Physical copy retired
      Trigger: Authorized staff retire a copy that is lost or damaged
      Lifecycle Meaning: The library no longer holds that copy
      Source Finding: S1 business_events Physical Copy Retired
  relationships:
    columns:
    - Subject
    - Verb
    - Object
    - Capability Need
    - Source Finding
    rows:
    - Subject: Physical copy
      Verb: belongs to
      Object: Book
      Capability Need: Record a copy against exactly one registered book
      Source Finding: S1 business_invariants — each physical copy belongs to exactly one book
    - Subject: Book
      Verb: is identified by
      Object: Title, author and publication year
      Capability Need: Refuse a registration whose three identifying attributes match a registered book
      Source Finding: 'S1 identity_and_sameness #1'
    - Subject: Physical copy
      Verb: is identified by
      Object: Barcode
      Capability Need: Refuse a copy registration whose barcode is already owned
      Source Finding: 'S1 identity_and_sameness #2'
    - Subject: Authorized staff member
      Verb: performs
      Object: Catalog operation
      Capability Need: Confirm the staff member is authorized before any operation
      Source Finding: 'S1 operation_refusals #7'
    - Subject: Catalog operation
      Verb: is recorded in
      Object: Catalog audit trail
      Capability Need: Record every performed operation durably in the catalog's own trail
      Source Finding: S1 business_invariants — every business operation is traceable and auditable
    - Subject: Book
      Verb: carries
      Object: Subject
      Capability Need: Select registered books by the subject or title staff search for
      Source Finding: S1 known_facts — staff search the catalog by subject or by title
  capability_graph:
    columns:
    - Capability
    - Source Finding
    - Status
    - Gap Register Entry
    - Notes
    rows:
    - Capability: Hold a book record durably and update it in place
      Source Finding: S3 authoring_decisions Hold a book record durably and update it in place
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Hold a physical copy record durably and update it in place
      Source Finding: S3 authoring_decisions Hold a physical copy record durably and update it in place
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Enforce that one book exists per title, author and publication year
      Source Finding: S3 authoring_decisions Enforce that one book exists per title, author and publication year
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Enforce that one physical copy exists per barcode
      Source Finding: S3 authoring_decisions Enforce that one physical copy exists per barcode
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Assemble a catalog record from supplied values
      Source Finding: S3 authoring_decisions Assemble a catalog record from supplied values
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Confirm a catalog record carries its required fields
      Source Finding: S3 authoring_decisions Confirm a catalog record carries its required fields
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Select the catalog records matching stated criteria
      Source Finding: S3 authoring_decisions Select the catalog records matching stated criteria
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Confirm the parameters supplied to a catalog operation satisfy their declared rules
      Source Finding: S3 authoring_decisions Confirm the parameters supplied to a catalog operation satisfy their declared rules
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Append an entry to an append-only trail
      Source Finding: S3 authoring_decisions Append an entry to an append-only trail
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Record a performed catalog operation in the catalog's audit trail
      Source Finding: S3 authoring_decisions Record a performed catalog operation in the catalog's audit trail
      Status: CRITICAL
      Gap Register Entry: GAP-01
      Notes: Nothing in the composition satisfies it.
    - Capability: Declare the stores the catalog owns
      Source Finding: S3 authoring_decisions Declare the stores the catalog owns
      Status: CRITICAL
      Gap Register Entry: GAP-02
      Notes: Nothing in the composition satisfies it.
    - Capability: Bind the catalog's operations to the stores and mechanisms they use
      Source Finding: S3 authoring_decisions Bind the catalog's operations to the stores and mechanisms they use
      Status: CRITICAL
      Gap Register Entry: GAP-03
      Notes: Nothing in the composition satisfies it.
    - Capability: A library staff actor whose authorization a catalog operation binds
      Source Finding: S3 authoring_decisions A library staff actor whose authorization a catalog operation binds
      Status: CRITICAL
      Gap Register Entry: GAP-04
      Notes: Nothing in the composition satisfies it.
    - Capability: Confirm the staff member performing an operation is authorized
      Source Finding: S3 authoring_decisions Confirm the staff member performing an operation is authorized
      Status: CRITICAL
      Gap Register Entry: GAP-05
      Notes: Nothing in the composition satisfies it.
    - Capability: Register a book together with its first physical copy
      Source Finding: S3 authoring_decisions Register a book together with its first physical copy
      Status: CRITICAL
      Gap Register Entry: GAP-06
      Notes: Nothing in the composition satisfies it.
    - Capability: Register a further physical copy against a registered book
      Source Finding: S3 authoring_decisions Register a further physical copy against a registered book
      Status: CRITICAL
      Gap Register Entry: GAP-07
      Notes: Nothing in the composition satisfies it.
    - Capability: Update a book's bibliographic information
      Source Finding: S3 authoring_decisions Update a book's bibliographic information
      Status: CRITICAL
      Gap Register Entry: GAP-08
      Notes: Nothing in the composition satisfies it.
    - Capability: Retire a book record
      Source Finding: S3 authoring_decisions Retire a book record
      Status: CRITICAL
      Gap Register Entry: GAP-09
      Notes: Nothing in the composition satisfies it.
    - Capability: Retire a physical copy
      Source Finding: S3 authoring_decisions Retire a physical copy
      Status: CRITICAL
      Gap Register Entry: GAP-10
      Notes: Nothing in the composition satisfies it.
    - Capability: Return a retired book record to the registered state
      Source Finding: S3 authoring_decisions Return a retired book record to the registered state
      Status: CRITICAL
      Gap Register Entry: GAP-11
      Notes: Nothing in the composition satisfies it.
    - Capability: Return a retired physical copy to the registered state
      Source Finding: S3 authoring_decisions Return a retired physical copy to the registered state
      Status: CRITICAL
      Gap Register Entry: GAP-12
      Notes: Nothing in the composition satisfies it.
    - Capability: Read every book record so that a search can select among them by content
      Source Finding: S3 authoring_decisions Read every book record so that a search can select among them by content
      Status: CRITICAL
      Gap Register Entry: GAP-17
      Notes: 'Owned by platform: an existing mechanism amended to publish records.'
    - Capability: Search the catalog by subject or title, excluding retired books
      Source Finding: S3 authoring_decisions Search the catalog by subject or title, excluding retired books
      Status: CRITICAL
      Gap Register Entry: GAP-13
      Notes: Nothing in the composition satisfies it.
    - Capability: A governed entry point for each catalog operation
      Source Finding: S3 authoring_decisions A governed entry point for each catalog operation
      Status: CRITICAL
      Gap Register Entry: GAP-15
      Notes: Nothing in the composition satisfies it.
    - Capability: A business moment for each of the five catalog events
      Source Finding: S3 authoring_decisions A business moment for each of the five catalog events
      Status: CRITICAL
      Gap Register Entry: GAP-16
      Notes: Nothing in the composition satisfies it.
  dependency_graph:
    columns:
    - From
    - To
    - Dependency Type
    - PPS Status
    - Source Finding
    rows:
    - From: catalog
      To: capability_side_effects::CS_MUTABLE_JSON_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Durable record storage
    - From: catalog
      To: capability_side_effects::CS_REGISTRY_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Uniqueness
    - From: catalog
      To: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Append-only trail
    - From: catalog
      To: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Record assembly
    - From: catalog
      To: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Record shape validation
    - From: catalog
      To: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Record selection
    - From: catalog
      To: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Parameter validation
    - From: catalog
      To: staff
      Dependency Type: data read
      PPS Status: GAP
      Source Finding: 'S1 authority_deferrals #1'
  constraint_register:
    columns:
    - '#'
    - Constraint
    - Source Finding
    - Source
    rows:
    - '#': '1'
      Constraint: Each physical copy belongs to exactly one book.
      Source Finding: 'S1 business_invariants #1'
      Source: invariant
    - '#': '2'
      Constraint: Each book the library holds has exactly one authoritative record.
      Source Finding: 'S1 business_invariants #2'
      Source: invariant
    - '#': '3'
      Constraint: Each physical copy the library owns has exactly one authoritative record.
      Source Finding: 'S1 business_invariants #3'
      Source: invariant
    - '#': '4'
      Constraint: No two registered books share the same title, author and publication year.
      Source Finding: 'S1 business_invariants #4'
      Source: invariant
    - '#': '5'
      Constraint: A book carries at least one subject.
      Source Finding: 'S1 business_invariants #5'
      Source: invariant
    - '#': '6'
      Constraint: No two physical copies the library owns share the same barcode.
      Source Finding: 'S1 business_invariants #6'
      Source: invariant
    - '#': '7'
      Constraint: Every business operation performed against the catalog is traceable and auditable.
      Source Finding: 'S1 business_invariants #7'
      Source: invariant
    - '#': '8'
      Constraint: Only authorized staff perform catalog operations.
      Source Finding: 'S1 business_invariants #8'
      Source: invariant
    - '#': '9'
      Constraint: Capabilities deferred to future change requests must not be designed into this solution.
      Source Finding: 'S1 constraints #1'
      Source: governance rule
    - '#': '10'
      Constraint: A physical copy may never be recorded against more than one book.
      Source Finding: 'S1 constraints #4'
      Source: business policy
    - '#': '11'
      Constraint: The catalog must not import the records staff maintain manually today.
      Source Finding: 'S1 constraints #5'
      Source: business policy
    - '#': '12'
      Constraint: The catalog appends only to a store it owns; it never writes into another subdomain's store.
      Source Finding: 'S3 analysis_findings #1'
      Source: governance rule
    - '#': '13'
      Constraint: A record's state is held as data on the record, because retirement is reversible in both directions.
      Source Finding: 'S3 analysis_findings #3'
      Source: domain knowledge
  gap_register:
    columns:
    - Gap Code
    - Source Finding
    - Capability
    - Owner Subdomain
    - Resolution
    rows:
    - Gap Code: GAP-01
      Source Finding: S3 authoring_decisions Record a performed catalog operation in the catalog's audit trail
      Capability: Record a performed catalog operation in the catalog's audit trail
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-02
      Source Finding: S3 authoring_decisions Declare the stores the catalog owns
      Capability: Declare the stores the catalog owns
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-03
      Source Finding: S3 authoring_decisions Bind the catalog's operations to the stores and mechanisms they use
      Capability: Bind the catalog's operations to the stores and mechanisms they use
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-04
      Source Finding: S3 authoring_decisions A library staff actor whose authorization a catalog operation binds
      Capability: A library staff actor whose authorization a catalog operation binds
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-05
      Source Finding: S3 authoring_decisions Confirm the staff member performing an operation is authorized
      Capability: Confirm the staff member performing an operation is authorized
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-06
      Source Finding: S3 authoring_decisions Register a book together with its first physical copy
      Capability: Register a book together with its first physical copy
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-07
      Source Finding: S3 authoring_decisions Register a further physical copy against a registered book
      Capability: Register a further physical copy against a registered book
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-08
      Source Finding: S3 authoring_decisions Update a book's bibliographic information
      Capability: Update a book's bibliographic information
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-09
      Source Finding: S3 authoring_decisions Retire a book record
      Capability: Retire a book record
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-10
      Source Finding: S3 authoring_decisions Retire a physical copy
      Capability: Retire a physical copy
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-11
      Source Finding: S3 authoring_decisions Return a retired book record to the registered state
      Capability: Return a retired book record to the registered state
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-12
      Source Finding: S3 authoring_decisions Return a retired physical copy to the registered state
      Capability: Return a retired physical copy to the registered state
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-13
      Source Finding: S3 authoring_decisions Search the catalog by subject or title, excluding retired books
      Capability: Search the catalog by subject or title, excluding retired books
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-14
      Source Finding: S3 authoring_decisions Retrieve a book's complete details with the copies the library holds
      Capability: Retrieve a book's complete details with the copies the library holds
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-15
      Source Finding: S3 authoring_decisions A governed entry point for each catalog operation
      Capability: A governed entry point for each catalog operation
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-16
      Source Finding: S3 authoring_decisions A business moment for each of the five catalog events
      Capability: A business moment for each of the five catalog events
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-17
      Source Finding: S3 authoring_decisions Read every book record so that a search can select among them by content
      Capability: Read every book record so that a search can select among them by content
      Owner Subdomain: platform
      Resolution: EXTEND
  design_decisions:
    columns:
    - '#'
    - Decision
    - Source Finding
    - Rationale
    - Constraints Imposed
    rows:
    - '#': '1'
      Decision: The catalog is a new subdomain, a peer of the nine other project functions, rather than an extension of anything existing.
      Source Finding: S3 placement_decision
      Rationale: Nothing in the composition carries the project's namespace or manages a library catalog, so there is no boundary to extend.
      Constraints Imposed: The catalog owns its records exclusively; the nine remaining functions stay adjacent and untouched.
    - '#': '2'
      Decision: The catalog owns its audit composition and its own append-only audit store, reusing only the append-only mechanism beneath them.
      Source Finding: 'S3 analysis_findings #1'
      Rationale: A subdomain owns its stores exclusively, and library traceability must not depend on agent-governance semantics. Decided by the business owner.
      Constraints Imposed: Two artifacts are authored rather than one reused; no catalog operation writes into another subdomain's store.
    - '#': '3'
      Decision: Uniqueness on a book is enforced by reusing the registry with a key formed from title, author and publication year.
      Source Finding: 'S3 analysis_findings #2'
      Rationale: Register-if-absent gives an atomic guarantee, and forming the key is a catalog business rule rather than a change to a side effect nineteen artifacts depend on. Decided by the business owner.
      Constraints Imposed: The composite key is stated by the catalog; the registry itself is read, never modified.
    - '#': '4'
      Decision: A record's state is data on the record, not the store it occupies.
      Source Finding: 'S3 analysis_findings #3'
      Rationale: Retirement is reversible, so a record must move from registered to retired and back without moving between stores.
      Constraints Imposed: The record store must support update in place; state is never implied by location.
    - '#': '5'
      Decision: Search and retrieval are audited but raise no business event.
      Source Finding: S1 business_events Book Registered
      Rationale: Every operation must be traceable, while an event is a moment another function may react to, and nothing reacts to a read.
      Constraints Imposed: Five business moments are authored, not seven; the audit trail records all nine operations.
    - '#': '6'
      Decision: Registering a book registers its first physical copy in the same operation.
      Source Finding: S1 known_facts — registering a book requires at least one physical copy
      Rationale: A book is never registered without a copy, so the two records come into existence together.
      Constraints Imposed: Registering a book raises one business moment, not two; a registration offering no copy is refused.
    - '#': '7'
      Decision: Retirement never cascades in either direction.
      Source Finding: 'S1 lifecycle_transitions #2'
      Rationale: Staff retire each record explicitly; nothing happens in the catalog that a staff member did not do.
      Constraints Imposed: No derived state change exists to design, and the audit trail needs no staff-versus-system distinction.
    - '#': '8'
      Decision: Authorization is read on every operation and granted nowhere in this change.
      Source Finding: 'S1 authority_deferrals #1'
      Rationale: The catalog requires staff to be authorized; deciding who is authorized belongs to the staff function, which a future change request introduces.
      Constraints Imposed: The catalog authors an authorization read and no authorization grant; the dependency on the staff function is that peer's gap.
    - '#': '9'
      Decision: Subject is free text, so no value-set validation applies.
      Source Finding: 'S3 analysis_findings #6'
      Rationale: The business chose free text. Decided by the business owner.
      Constraints Imposed: One fewer reuse candidate; search by kind is only as consistent as what staff type.
    - '#': '10'
      Decision: Search excludes retired books while retrieval serves them.
      Source Finding: 'S3 analysis_findings #4'
      Rationale: A retired record must stay auditable and retrievable without appearing as current stock.
      Constraints Imposed: Both read paths select by stated criteria, with the record's state as one of them.
    - '#': '11'
      Decision: The durable-record mechanism is extended to publish records, rather than the catalog keeping a second copy of every book for searching.
      Source Finding: 'S3 analysis_findings #7'
      Rationale: The implementation already returned records and only the declaration withheld them; a projection store would duplicate every book and need syncing on every update, retirement and reinstatement. Decided by the business owner.
      Constraints Imposed: One additive operation on a platform side effect; the catalog holds no second copy of a book.
  authoring_scope:
    columns:
    - Capability
    - Gap Register Ref
    rows:
    - Capability: Record a performed catalog operation in the catalog's audit trail
      Gap Register Ref: GAP-01
    - Capability: Declare the stores the catalog owns
      Gap Register Ref: GAP-02
    - Capability: Bind the catalog's operations to the stores and mechanisms they use
      Gap Register Ref: GAP-03
    - Capability: A library staff actor whose authorization a catalog operation binds
      Gap Register Ref: GAP-04
    - Capability: Confirm the staff member performing an operation is authorized
      Gap Register Ref: GAP-05
    - Capability: Register a book together with its first physical copy
      Gap Register Ref: GAP-06
    - Capability: Register a further physical copy against a registered book
      Gap Register Ref: GAP-07
    - Capability: Update a book's bibliographic information
      Gap Register Ref: GAP-08
    - Capability: Retire a book record
      Gap Register Ref: GAP-09
    - Capability: Retire a physical copy
      Gap Register Ref: GAP-10
    - Capability: Return a retired book record to the registered state
      Gap Register Ref: GAP-11
    - Capability: Return a retired physical copy to the registered state
      Gap Register Ref: GAP-12
    - Capability: Search the catalog by subject or title, excluding retired books
      Gap Register Ref: GAP-13
    - Capability: Retrieve a book's complete details with the copies the library holds
      Gap Register Ref: GAP-14
    - Capability: A governed entry point for each catalog operation
      Gap Register Ref: GAP-15
    - Capability: A business moment for each of the five catalog events
      Gap Register Ref: GAP-16
```

This document consolidates Stages 1 to 3. It re-litigates nothing and introduces no design: every
row carries the prior-stage finding it came from, and every capability Stage 3 committed appears in
the capability graph exactly as Stage 3 stated it.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

---

## 2. Capability Graph (capability_graph)

---

## 3. Dependency Graph (dependency_graph)

The dependency on the staff function is a gap owned by that peer, not by this change: the catalog
reads whether a staff member is authorized and never decides it.

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

| Read every book record so that a search can select among them by content | GAP-17 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Circulation | A project function; this change request is limited to catalog only |
| Patron | A project function, and patron management is declared excluded from this release |
| Staff | A project function; it is where deciding who is authorized is deferred to |
| Reservations | Declared excluded from this release |
| Acquisitions | Declared excluded from this release |
| Inventory | A project function; inventory reconciliation is declared excluded from this release |
| Notifications | A project function; this change request is limited to catalog only |
| Policy | A project function; this change request is limited to catalog only |
| Reporting | A project function; this change request is limited to catalog only |
| Borrowing | Declared excluded from this release |
| Fines | Declared excluded from this release |
| Import of the records staff maintain manually today | The catalog starts empty |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
