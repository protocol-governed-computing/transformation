# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 4 — Business Model
  CR: cr_02_catalog
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
    - Actor: Authorized staff
      Role: Performs every catalog operation, including the ones this change adds.
      Authority Class: Authorized business actor
      Source Finding: S1 authority_boundaries The judgement that an edition is obsolete
    - Actor: The catalog
      Role: Holds the authoritative record of every work, edition and physical copy.
      Authority Class: Owning subdomain
      Source Finding: S1 authority_boundaries Work record
    - Actor: The business author
      Role: Settles what an edition is and what identifies a work.
      Authority Class: Business authority, outside the system
      Source Finding: S1 authority_boundaries Whether an edition is part of a Book or a catalog entity in its own right
  bm_entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Source Finding
    rows:
    - Entity: Work
      Description: A published work, recognizable as one thing across the editions in which it is published, identified by its title and author.
      Store Model: A durable record store holding one record per work, and a registry claiming each work's identity.
      Source Finding: S2 entities Work
    - Entity: Edition
      Description: A publication of a work, identified by title, author and publication year. The record the previous change calls a book is an edition.
      Store Model: The existing durable record store, unchanged.
      Source Finding: S2 entities Edition
    - Entity: Physical Copy
      Description: An individual copy the library owns, belonging to exactly one edition.
      Store Model: The existing durable record store, unchanged.
      Source Finding: S2 entities Physical Copy
    - Entity: Bibliographic Information
      Description: An edition's descriptive content.
      Store Model: Held within the edition's own record.
      Source Finding: S2 entities Bibliographic Information
    - Entity: Edition Summary
      Description: Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean.
      Store Model: Assembled at read time; not stored.
      Source Finding: S2 entities Edition Summary
    - Entity: Work Summary
      Description: A short description of the work an edition belongs to, carried in that edition's retrieval.
      Store Model: Assembled at read time; not stored.
      Source Finding: S2 entities Work Summary
    - Entity: Existing Catalog Record
      Description: A catalog record written under the previous governed change, before this one.
      Store Model: The same store the edition occupies.
      Source Finding: S2 entities Existing Catalog Record
    - Entity: Business Operation
      Description: An action performed against the catalog that must be traceable and auditable.
      Store Model: The existing append-only trail, unchanged.
      Source Finding: S2 entities Business Operation
  resources:
    columns:
    - Resource
    - Description
    - Source Finding
    rows:
    - Resource: The work store
      Description: Holds one record per work the catalog knows.
      Source Finding: S3 authoring_decisions Hold a work record durably and update it in place
    - Resource: The work identity registry
      Description: Claims each work's identity so two registrations of one work do not produce two works.
      Source Finding: S3 authoring_decisions Enforce that one work exists per title and author
  events:
    columns:
    - Event
    - Trigger
    - Lifecycle Meaning
    - Source Finding
    rows:
    - Event: Work Registered
      Trigger: Authorized staff register an edition of a work the catalog does not yet hold.
      Lifecycle Meaning: A work enters the catalog, created by the edition that evidences it.
      Source Finding: 'S1 business_events #1'
    - Event: Edition Registered
      Trigger: Authorized staff register an additional edition of an existing work.
      Lifecycle Meaning: The catalog records a further edition of a work it already holds.
      Source Finding: 'S1 business_events #2'
  relationships:
    columns:
    - Subject
    - Verb
    - Object
    - Capability Need
    - Source Finding
    rows:
    - Subject: Work
      Verb: is published as
      Object: Edition
      Capability Need: Register an edition against the work it belongs to, creating the work when the catalog does not yet hold it
      Source Finding: S3 authoring_decisions Register an edition of a work the catalog does not yet hold
    - Subject: Edition
      Verb: belongs to
      Object: Work
      Capability Need: Resolve the work a title and author denote, so a further edition can name it
      Source Finding: S3 authoring_decisions Resolve the work an edition belongs to
    - Subject: Physical Copy
      Verb: is a copy of
      Object: Edition
      Capability Need: Register a copy against exactly one edition, unchanged from the previous change
      Source Finding: S3 authoring_decisions Register a physical copy against exactly one edition
    - Subject: Authorized staff
      Verb: searches
      Object: Work
      Capability Need: Answer a search at the level of the work, carrying a summary of its editions
      Source Finding: S3 authoring_decisions Search the catalog and answer at the level of the work
    - Subject: Authorized staff
      Verb: retrieves
      Object: Edition
      Capability Need: Return an edition's details, its copies, and a summary of the work it belongs to
      Source Finding: S3 authoring_decisions Retrieve an edition's complete details with a summary of its work
  capability_graph:
    columns:
    - Capability
    - Source Finding
    - Status
    - Gap Register Entry
    - Notes
    rows:
    - Capability: Hold a work record durably and update it in place
      Source Finding: S3 authoring_decisions Hold a work record durably and update it in place
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is from the composition; read, never modified.
    - Capability: Enforce that one work exists per title and author
      Source Finding: S3 authoring_decisions Enforce that one work exists per title and author
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is with a two-attribute key, exactly as the edition key uses it with three.
    - Capability: Form the identifying key of a work from its title and author
      Source Finding: S3 authoring_decisions Form the identifying key of a work from its title and author
      Status: CRITICAL
      Gap Register Entry: GAP-01
      Notes: The edition key transform is reached by every catalog operation and is not widened.
    - Capability: Claim a work's identity so that two registrations of one work do not produce two works
      Source Finding: S3 authoring_decisions Claim a work's identity so that two registrations of one work do not produce two works
      Status: CRITICAL
      Gap Register Entry: GAP-02
      Notes: Composed the way the edition claim is composed, against the work's own registry store.
    - Capability: Resolve the work an edition belongs to
      Source Finding: S3 authoring_decisions Resolve the work an edition belongs to
      Status: CRITICAL
      Gap Register Entry: GAP-03
      Notes: Nothing in the composition answers which work a title and author denote.
    - Capability: Group selected records by an attribute they share
      Source Finding: S3 authoring_decisions Group selected records by an attribute they share
      Status: CRITICAL
      Gap Register Entry: GAP-04
      Notes: Selection exists; grouping does not.
    - Capability: Declare the stores the catalog owns
      Source Finding: S3 authoring_decisions Declare the stores the catalog owns
      Status: CRITICAL
      Gap Register Entry: GAP-05
      Notes: Extended with the work store and the work identity registry.
    - Capability: Bind the catalog's workflows to the stores they use
      Source Finding: S3 authoring_decisions Bind the catalog's workflows to the stores they use
      Status: CRITICAL
      Gap Register Entry: GAP-06
      Notes: Extended so the new stores are reachable by the workflows that use them.
    - Capability: Register an edition of a work the catalog does not yet hold
      Source Finding: S3 authoring_decisions Register an edition of a work the catalog does not yet hold
      Status: CRITICAL
      Gap Register Entry: GAP-07
      Notes: Gains a work claim among the claims, before any write.
    - Capability: Validate that a registration carries what a work and an edition require
      Source Finding: S3 authoring_decisions Validate that a registration carries what a work and an edition require
      Status: CRITICAL
      Gap Register Entry: GAP-08
      Notes: Runs before any claim, as it does today.
    - Capability: Register an additional edition of an existing work
      Source Finding: S3 authoring_decisions Register an additional edition of an existing work
      Status: CRITICAL
      Gap Register Entry: GAP-09
      Notes: The operation this change exists to add.
    - Capability: Search the catalog and answer at the level of the work
      Source Finding: S3 authoring_decisions Search the catalog and answer at the level of the work
      Status: CRITICAL
      Gap Register Entry: GAP-10
      Notes: The search terms are unchanged; the shape of the answer is not.
    - Capability: Retrieve an edition's complete details with a summary of its work
      Source Finding: S3 authoring_decisions Retrieve an edition's complete details with a summary of its work
      Status: CRITICAL
      Gap Register Entry: GAP-11
      Notes: Retrieval stays edition retrieval and gains the work summary.
    - Capability: Admit a request to register an additional edition of an existing work
      Source Finding: S3 authoring_decisions Admit a request to register an additional edition of an existing work
      Status: CRITICAL
      Gap Register Entry: GAP-12
      Notes: A new business operation is reached through its own entry point.
    - Capability: Recognise the moment a work enters the catalog
      Source Finding: S3 authoring_decisions Recognise the moment a work enters the catalog
      Status: CRITICAL
      Gap Register Entry: GAP-13
      Notes: The catalog declares a moment for each thing that enters it.
    - Capability: Confirm the staff member performing an operation is authorized
      Source Finding: S3 authoring_decisions Confirm the staff member performing an operation is authorized
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is; the operations this change adds reach it first, as every other does.
    - Capability: Record every performed operation in the catalog's audit trail
      Source Finding: S3 authoring_decisions Record every performed operation in the catalog's audit trail
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is; the trail records whatever operation it is handed.
    - Capability: Register a physical copy against exactly one edition
      Source Finding: S3 authoring_decisions Register a physical copy against exactly one edition
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is; nothing about copies changes.
    - Capability: Retire and reinstate an edition independently of the work's other editions
      Source Finding: S3 authoring_decisions Retire and reinstate an edition independently of the work's other editions
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is; retirement already cascades to nothing.
    - Capability: Update an edition's bibliographic information
      Source Finding: S3 authoring_decisions Update an edition's bibliographic information
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Reused as-is; duplication remains an edition-level rule.
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
      Source Finding: S3 dependency_discoveries Durable record storage for works
    - From: catalog
      To: capability_side_effects::CS_REGISTRY_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Uniqueness claim for a work's identity
    - From: catalog
      To: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries The audit step every catalog operation reaches last
    - From: catalog
      To: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Dependency Type: data read
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries The store declaration that must carry the work stores
    - From: catalog
      To: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Dependency Type: data read
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries The binding declaration that must bind the work stores
    - From: catalog
      To: book_library_mgmt::CC_REGISTER_BOOK_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries The registration step that must claim the work
    - From: catalog
      To: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries The search step whose answer must be grouped by work
    - From: catalog
      To: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries The retrieval step that must carry a work summary
    - From: catalog
      To: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries The authorization check every catalog operation reaches first
    - From: catalog
      To: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries The audit step every catalog operation reaches last
    - From: catalog
      To: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Copy registration and barcode uniqueness
    - From: catalog
      To: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Retirement and reinstatement of an edition
    - From: catalog
      To: staff
      Dependency Type: capability call
      PPS Status: GAP
      Source Finding: S1 authority_deferrals Which staff are authorized
  constraint_register:
    columns:
    - '#'
    - Constraint
    - Source Finding
    - Source
    rows:
    - '#': '1'
      Constraint: No capability staff have today may be withdrawn and no existing record may become unreachable.
      Source Finding: 'S1 constraints #1'
      Source: governance rule
    - '#': '2'
      Constraint: Existing catalog records must remain valid without recreation or migration, demonstrated against records written under the previous change.
      Source Finding: 'S1 constraints #2'
      Source: governance rule
    - '#': '3'
      Constraint: Only search and retrieval may be extended; every other existing operation must behave as it does today.
      Source Finding: 'S1 constraints #3'
      Source: governance rule
    - '#': '4'
      Constraint: Multiple identifiers, governed subject taxonomy, digital resources and images must not be designed into this change.
      Source Finding: 'S1 constraints #4'
      Source: governance rule
    - '#': '5'
      Constraint: Every business operation must remain traceable and auditable.
      Source Finding: 'S1 constraints #5'
      Source: invariant
    - '#': '6'
      Constraint: Each edition belongs to exactly one work.
      Source Finding: 'S1 business_invariants #1'
      Source: invariant
    - '#': '7'
      Constraint: Each physical copy belongs to exactly one edition.
      Source Finding: 'S1 business_invariants #2'
      Source: invariant
    - '#': '8'
      Constraint: No two works share the same title and author.
      Source Finding: 'S1 business_invariants #3'
      Source: invariant
    - '#': '9'
      Constraint: No two editions of a work share the same publication year.
      Source Finding: 'S1 business_invariants #4'
      Source: invariant
    - '#': '10'
      Constraint: Every work has at least one edition.
      Source Finding: 'S1 business_invariants #5'
      Source: invariant
    - '#': '11'
      Constraint: A work is not retired; a work whose editions are all retired is simply that.
      Source Finding: S1 operation_refusals Retire a work
      Source: domain knowledge
    - '#': '12'
      Constraint: Every claim precedes every write, so a refused registration changes nothing.
      Source Finding: 'S3 analysis_findings #10'
      Source: domain knowledge
    - '#': '13'
      Constraint: The transform forming the edition key is not widened; the identity of the existing record does not change to serve a new one.
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
      Source Finding: S3 authoring_decisions Form the identifying key of a work from its title and author
      Capability: Form the identifying key of a work from its title and author
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-02
      Source Finding: S3 authoring_decisions Claim a work's identity so that two registrations of one work do not produce two works
      Capability: Claim a work's identity so that two registrations of one work do not produce two works
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-03
      Source Finding: S3 authoring_decisions Resolve the work an edition belongs to
      Capability: Resolve the work an edition belongs to
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-04
      Source Finding: S3 authoring_decisions Group selected records by an attribute they share
      Capability: Group selected records by an attribute they share
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-05
      Source Finding: S3 authoring_decisions Declare the stores the catalog owns
      Capability: Declare the stores the catalog owns
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-06
      Source Finding: S3 authoring_decisions Bind the catalog's workflows to the stores they use
      Capability: Bind the catalog's workflows to the stores they use
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-07
      Source Finding: S3 authoring_decisions Register an edition of a work the catalog does not yet hold
      Capability: Register an edition of a work the catalog does not yet hold
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-08
      Source Finding: S3 authoring_decisions Validate that a registration carries what a work and an edition require
      Capability: Validate that a registration carries what a work and an edition require
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-09
      Source Finding: S3 authoring_decisions Register an additional edition of an existing work
      Capability: Register an additional edition of an existing work
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-10
      Source Finding: S3 authoring_decisions Search the catalog and answer at the level of the work
      Capability: Search the catalog and answer at the level of the work
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-11
      Source Finding: S3 authoring_decisions Retrieve an edition's complete details with a summary of its work
      Capability: Retrieve an edition's complete details with a summary of its work
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-12
      Source Finding: S3 authoring_decisions Admit a request to register an additional edition of an existing work
      Capability: Admit a request to register an additional edition of an existing work
      Owner Subdomain: catalog
      Resolution: NEW
    - Gap Code: GAP-13
      Source Finding: S3 authoring_decisions Recognise the moment a work enters the catalog
      Capability: Recognise the moment a work enters the catalog
      Owner Subdomain: catalog
      Resolution: NEW
  design_decisions:
    columns:
    - '#'
    - Decision
    - Source Finding
    - Rationale
    - Constraints Imposed
    rows:
    - '#': '1'
      Decision: The record the previous change calls a book is an edition; the work is added above it.
      Source Finding: 'S3 analysis_findings #1'
      Rationale: The existing identity of title, author and publication year already distinguishes editions, so no existing identity, record or operation is redefined.
      Constraints Imposed: No migration of existing records; no change to the edition's identity; a record written before this change is an edition of a work with one edition.
    - '#': '2'
      Decision: The work's identity is formed by a new transform rather than by widening the existing key transform.
      Source Finding: 'S3 analysis_findings #3'
      Rationale: The edition key transform is reached by every catalog operation and 23 artifacts depend on it.
      Constraints Imposed: The two keys stay independent; a change to one cannot alter the other.
    - '#': '3'
      Decision: The work is claimed through the same registry mechanism the edition is claimed through.
      Source Finding: 'S3 analysis_findings #2'
      Rationale: Register-if-absent gives the atomic uniqueness a work identity needs, and the mechanism is read rather than modified.
      Constraints Imposed: The work claim is atomic; two registrations of one work cannot produce two works.
    - '#': '4'
      Decision: The work store and the work identity registry are declared in the catalog's own storage declaration.
      Source Finding: 'S3 analysis_findings #7'
      Rationale: A subdomain declares its stores once and binds them once, and every consumer of both declarations is inside the catalog.
      Constraints Imposed: No second storage or binding declaration for this subdomain.
    - '#': '5'
      Decision: Registering an edition of a new work extends the existing registration; registering an additional edition is a new operation.
      Source Finding: S3 authoring_decisions Register an additional edition of an existing work
      Rationale: The existing registration creates the work and requires a first copy; an additional edition does neither.
      Constraints Imposed: Two registration operations, each with its own entry point, sharing every refusal the existing one enforces.
    - '#': '6'
      Decision: The work claim is placed among the existing claims, before any write.
      Source Finding: 'S3 analysis_findings #10'
      Rationale: The previous change established the order so that a refused registration leaves nothing behind.
      Constraints Imposed: A refused registration still changes nothing, including the work.
    - '#': '7'
      Decision: Search is extended rather than duplicated, and answers at the level of the work.
      Source Finding: 'S3 analysis_findings #5'
      Rationale: Two searches would leave staff choosing which one answers their question, and the existing search's consumers are one workflow and one entry point within the subdomain.
      Constraints Imposed: The result shape changes; the search terms do not. Every existing record remains findable.
    - '#': '8'
      Decision: Retrieval stays edition retrieval and carries a summary of the work.
      Source Finding: S1 known_facts Retrieval stays edition retrieval
      Rationale: The business asked for one retrieval carrying a summary, not a second operation.
      Constraints Imposed: No work-level retrieval operation in this change.
    - '#': '9'
      Decision: A work is not retired.
      Source Finding: S1 operation_refusals Retire a work
      Rationale: A work whose editions are all retired is simply that; retirement is declared on the edition and cascades to nothing.
      Constraints Imposed: No work lifecycle beyond registered; no cascade from an edition's retirement to its work.
  authoring_scope:
    columns:
    - Capability
    - Gap Register Ref
    rows:
    - Capability: Form the identifying key of a work from its title and author
      Gap Register Ref: GAP-01
    - Capability: Claim a work's identity so that two registrations of one work do not produce two works
      Gap Register Ref: GAP-02
    - Capability: Resolve the work an edition belongs to
      Gap Register Ref: GAP-03
    - Capability: Group selected records by an attribute they share
      Gap Register Ref: GAP-04
    - Capability: Declare the stores the catalog owns
      Gap Register Ref: GAP-05
    - Capability: Bind the catalog's workflows to the stores they use
      Gap Register Ref: GAP-06
    - Capability: Register an edition of a work the catalog does not yet hold
      Gap Register Ref: GAP-07
    - Capability: Validate that a registration carries what a work and an edition require
      Gap Register Ref: GAP-08
    - Capability: Register an additional edition of an existing work
      Gap Register Ref: GAP-09
    - Capability: Search the catalog and answer at the level of the work
      Gap Register Ref: GAP-10
    - Capability: Retrieve an edition's complete details with a summary of its work
      Gap Register Ref: GAP-11
    - Capability: Admit a request to register an additional edition of an existing work
      Gap Register Ref: GAP-12
    - Capability: Recognise the moment a work enters the catalog
      Gap Register Ref: GAP-13
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies: what is reused already exists, what is extended or authored is a declared gap.
Nothing is re-litigated and nothing new is decided.

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

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Multiple identifiers for one publication | A further catalog need, deferred to a governed change of its own; what an ISBN identifies could not be answered until an edition was defined. |
| A governed subject taxonomy | A further catalog need, deferred to a governed change of its own. |
| Digital resources associated with catalog records | A further catalog need, deferred to a governed change of its own. |
| Images associated with catalog records | A further catalog need, deferred to a governed change of its own. |
| Deciding which staff are authorized | Deferred to the staff function, which a future governed change introduces. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · business_invariants · constraints · authority_boundaries · business_events · out_of_scope · authority_deferrals |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · gaps · architectural_observations |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
