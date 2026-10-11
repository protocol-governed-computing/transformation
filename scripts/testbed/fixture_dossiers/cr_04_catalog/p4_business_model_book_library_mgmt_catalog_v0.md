# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 4 — Business Model
  CR: cr_04_catalog
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
    - Actor: Catalog
      Role: States what each of its operations needs, and decides whether a request may proceed.
      Authority Class: Declaring — what an operation requires is the catalog's own account of what it does.
      Source Finding: 'S1 authority_boundaries #1'
    - Actor: Library staff
      Role: Make the requests the catalog admits or turns away.
      Authority Class: Acting — unchanged by this change.
      Source Finding: 'S2 entities #2'
    - Actor: The library's authorisation rules
      Role: Decide who may perform each operation.
      Authority Class: Deciding — stated separately from what an operation needs, and untouched.
      Source Finding: 'S2 belief_verification #4'
  bm_entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Source Finding
    rows:
    - Entity: Operation
      Description: Something a librarian asks the catalog to do.
      Store Model: Ten are declared for this subdomain, each with a boundary and a workflow.
      Source Finding: 'S2 entities #1'
    - Entity: Requirement
      Description: Something an operation states a request must supply.
      Store Model: Declared at the operation's boundary, as a name and the form the value takes.
      Source Finding: 'S2 entities #3'
    - Entity: Use
      Description: A step of the operation reading something the request supplied.
      Store Model: Declared in the operation's own steps.
      Source Finding: 'S2 entities #4'
    - Entity: Request
      Description: One asking, with what the librarian supplied.
      Store Model: Not held; it is what arrives at the boundary.
      Source Finding: 'S2 entities #2'
  resources:
    columns:
    - Resource
    - Description
    - Source Finding
    rows:
    - Resource: The three boundaries being corrected
      Description: Registering a further edition, correcting bibliographic information, and registering a work.
      Source Finding: 'S3 analysis_findings #1'
    - Resource: The seven boundaries that already agree
      Description: Registering a physical copy, retiring and reinstating a book record and a physical copy, retrieving book details, and searching the catalog.
      Source Finding: 'S2 architectural_observations #1'
    - Resource: The library's end-to-end exercise of the catalog
      Description: Registering a work, adding two further editions, correcting a legacy record. Stops today at the second edition.
      Source Finding: 'S3 verification_results #6'
    - Resource: The four statements of a publication year's form
      Description: Three boundaries and the description supplied with each request. Three say number; one says word.
      Source Finding: 'S3 analysis_findings #3'
  events:
    columns:
    - Event
    - Trigger
    - Lifecycle Meaning
    - Source Finding
    rows:
    - Event: A request was admitted
      Trigger: A librarian supplying what the operation needs
      Lifecycle Meaning: The operation proceeds and the catalog changes.
      Source Finding: 'S1 business_events #1'
    - Event: A request was turned away
      Trigger: Something the operation needs being missing or in the wrong form
      Lifecycle Meaning: The librarian is told before anything happened, and the catalog is unchanged.
      Source Finding: 'S1 business_events #2'
    - Event: A correct request was turned away
      Trigger: A boundary requiring something its operation does not use, or requiring it in a form the catalog does not hold
      Lifecycle Meaning: The state this change ends. It is the present state of two of the ten operations.
      Source Finding: 'S1 lifecycle_states #3'
    - Event: A request was admitted that the operation could not carry out
      Trigger: A boundary requiring less than its operation reads
      Lifecycle Meaning: Latent in registering a work; the failure appears part-way through instead of at the boundary.
      Source Finding: 'S2 gaps #3'
  relationships:
    columns:
    - Subject
    - Verb
    - Object
    - Capability Need
    - Source Finding
    rows:
    - Subject: Operation
      Verb: requires
      Object: Requirement
      Capability Need: Admitting a request to register a further edition.
      Source Finding: 'S3 authoring_decisions #1'
    - Subject: Operation
      Verb: requires
      Object: Requirement
      Capability Need: Admitting a request to correct bibliographic information.
      Source Finding: 'S3 authoring_decisions #2'
    - Subject: Operation
      Verb: requires
      Object: Requirement
      Capability Need: Admitting a request to register a work — deferred; the requirement it lacks is one every present caller sends elsewhere.
      Source Finding: 'S3 authoring_decisions #3'
    - Subject: Operation
      Verb: uses
      Object: Requirement
      Capability Need: Agreement between what an operation requires and what its steps read.
      Source Finding: 'S3 analysis_findings #2'
  capability_graph:
    columns:
    - Capability
    - Source Finding
    - Status
    - Gap Register Entry
    - Notes
    rows:
    - Capability: Admitting a request to register a further edition
      Source Finding: 'S3 authoring_decisions #1'
      Status: CRITICAL
      Gap Register Entry: GAP-1
      Notes: Turns away every correct request today; the library's exercise stops here.
    - Capability: Admitting a request to correct bibliographic information
      Source Finding: 'S3 authoring_decisions #2'
      Status: CRITICAL
      Gap Register Entry: GAP-2
      Notes: Turns away every correction today.
    - Capability: Admitting a request to register a work
      Source Finding: 'S3 authoring_decisions #3'
      Status: DEFERRED
      Gap Register Entry: ''
      Notes: A real defect of the same kind, read in the other direction. Correcting it moves a caller, which this change's seed forbids.
    - Capability: Deciding who may perform an operation
      Source Finding: 'S3 dependency_discoveries #3'
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Declared uniformly across all ten operations and untouched.
    - Capability: The three operations
      Source Finding: 'S3 authoring_decisions #4'
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: No step is added, removed or rebound; each operation is correct.
    - Capability: Holding what the catalog knows
      Source Finding: 'S3 dependency_discoveries #4'
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: Six stores, unchanged; no held record is migrated or revalidated.
  dependency_graph:
    columns:
    - From
    - To
    - Dependency Type
    - PPS Status
    - Source Finding
    rows:
    - From: catalog
      To: catalog
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: 'S3 dependency_discoveries #2 — all three operations already run and already read what they read.'
    - From: catalog
      To: intent
      Dependency Type: data read
      PPS Status: SATISFIED
      Source Finding: 'S3 dependency_discoveries #1 — all three boundaries are declared artifacts of this subdomain.'
    - From: catalog
      To: structure
      Dependency Type: data read
      PPS Status: SATISFIED
      Source Finding: 'S3 dependency_discoveries #4 — the six stores are declared and unchanged.'
  constraint_register:
    columns:
    - '#'
    - Constraint
    - Source Finding
    - Source
    rows:
    - '#': '1'
      Constraint: An operation requires only what it uses, and uses only what it requires.
      Source Finding: 'S3 analysis_findings #2'
      Source: governance rule
    - '#': '2'
      Constraint: Nothing about who may perform an operation changes.
      Source Finding: 'S1 constraints #2'
      Source: governance rule
    - '#': '3'
      Constraint: The records the catalog already holds are not migrated, rewritten or revalidated.
      Source Finding: 'S1 constraints #3'
      Source: governance rule
    - '#': '4'
      Constraint: A publication year is stated as a number wherever an operation asks for one.
      Source Finding: 'S1 constraints #4'
      Source: governance rule
    - '#': '5'
      Constraint: No correct request becomes harder to make.
      Source Finding: 'S3 analysis_findings #1'
      Source: governance rule
    - '#': '6'
      Constraint: The form of a detail the catalog holds is settled by no artifact, so agreement among the statements of it is the only authority available.
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
    - Gap Code: GAP-1
      Source Finding: 'S3 authoring_decisions #1'
      Capability: Admitting a request to register a further edition
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-2
      Source Finding: 'S3 authoring_decisions #2'
      Capability: Admitting a request to correct bibliographic information
      Owner Subdomain: catalog
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
      Decision: Registering a further edition states the publication year as a number.
      Source Finding: 'S3 authoring_decisions #1'
      Rationale: Three of the four statements of the form say number, and every year the library supplies is a number.
      Constraints Imposed: Rules out changing the operation to accept a word, and rules out leaving the form to whichever statement is read first.
    - '#': '2'
      Decision: Correcting bibliographic information withdraws the title, the author and the publication year.
      Source Finding: 'S3 authoring_decisions #2'
      Rationale: No step of the correction reads any of the three, and a correction that restates the fields it leaves alone is not a correction.
      Constraints Imposed: Rules out making the operation read them to justify requiring them.
    - '#': '3'
      Decision: Registering a work is not corrected here.
      Source Finding: 'S3 authoring_decisions #3'
      Rationale: The act reads the subject at the top of the request and every present caller sends it nested inside the details of the book, so requiring it makes every present request fail. Constraint 5 forbids exactly that.
      Constraints Imposed: Rules out correcting a boundary whose correction moves a caller, and fixes that the defect is deferred intact rather than dropped.
    - '#': '4'
      Decision: No step of any of the three operations changes.
      Source Finding: 'S3 authoring_decisions #4'
      Rationale: What each operation does is correct; it is the boundary above it that is wrong.
      Constraints Imposed: Rules out rewriting the operations, and confines the change to three declarations.
    - '#': '5'
      Decision: The change is one act over three boundaries, not three unrelated corrections.
      Source Finding: 'S3 analysis_findings #2'
      Rationale: All three break one invariant, read in both directions; stating it one-sidedly is what let the third survive.
      Constraints Imposed: Rules out completing the change with two of the three corrected.
  authoring_scope:
    columns:
    - Capability
    - Gap Register Ref
    rows:
    - Capability: Admitting a request to register a further edition
      Gap Register Ref: GAP-1
    - Capability: Admitting a request to correct bibliographic information
      Gap Register Ref: GAP-2
```

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

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
| Admitting a request to register a work | The act reads the subject at the top of the request and every present caller sends it nested inside the details of the book. Requiring it moves the boundary and every caller together, which this change's seed forbids. Its own CR, where both move at once. |
| Comparing what an operation requires against what it uses | Nothing performs it in the composition. Whether it belongs to this subdomain or to the platform is not this change's to settle. |
| Declaring the form of a detail the catalog holds | The store declares paths and no forms. Giving the catalog an authority over forms is a larger change than bringing one boundary into agreement with three statements. |
| The operations of subdomains and domains other than the catalog | Each is its own business, and the same comparison reports findings elsewhere that were not examined here. |
