# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 4 — Business Model
  CR: cr_05_catalog
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
      Role: Performs catalog operations.
      Authority Class: Internal staff
      Source Finding: 'S1 known_facts #1'
    - Actor: The staff function
      Role: Decides which staff are authorized.
      Authority Class: Adjacent subdomain
      Source Finding: 'S1 known_facts #2'
    - Actor: The catalog
      Role: Holds the library's records, and now every rule it applies to them.
      Authority Class: Owning subdomain
      Source Finding: S3 placement_decision EXTEND
  bm_entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Source Finding
    rows:
    - Entity: The Book
      Description: Title, author, publication year, subject and state.
      Store Model: One keyed store, one record per book, unchanged.
      Source Finding: 'S2 entities #1'
    - Entity: The Physical Copy
      Description: One copy of a book, and its state.
      Store Model: One keyed store, one record per barcode, unchanged.
      Source Finding: 'S2 entities #2'
    - Entity: The Catalog's Rules
      Description: Who may perform a catalog operation, and what a book, a work and a further edition must contain.
      Store Model: Held by the catalog steps that apply them. Held by nothing today.
      Source Finding: S3 analysis_findings Q1
  resources:
    columns:
    - Resource
    - Description
    - Source Finding
    rows:
    - Resource: NONE IDENTIFIED
      Description: ''
      Source Finding: ''
  events:
    columns:
    - Event
    - Trigger
    - Lifecycle Meaning
    - Source Finding
    rows:
    - Event: NONE IDENTIFIED
      Trigger: This change recognises no new moment.
      Lifecycle Meaning: The moments the catalog announces are unchanged.
      Source Finding: 'S1 business_events #1'
  relationships:
    columns:
    - Subject
    - Verb
    - Object
    - Capability Need
    - Source Finding
    rows:
    - Subject: The catalog
      Verb: refuses
      Object: anyone the library has not authorized
      Capability Need: Refuse anyone the library has not authorized
      Source Finding: S3 authoring_decisions Refuse anyone the library has not authorized
    - Subject: The catalog
      Verb: refuses
      Object: a registration missing what it must contain
      Capability Need: Refuse a registration the catalog finds incomplete
      Source Finding: S3 authoring_decisions Refuse a registration the catalog finds incomplete
    - Subject: The catalog
      Verb: records
      Object: a copy as registered
      Capability Need: Register a copy as registered
      Source Finding: S3 authoring_decisions Register a copy as registered
  capability_graph:
    columns:
    - Capability
    - Source Finding
    - Status
    - Gap Register Entry
    - Notes
    rows:
    - Capability: Refuse anyone the library has not authorized
      Source Finding: S3 authoring_decisions Refuse anyone the library has not authorized
      Status: CRITICAL
      Gap Register Entry: GAP-01
      Notes: The confirming step holds the library's rules.
    - Capability: Refuse a registration the catalog finds incomplete
      Source Finding: S3 authoring_decisions Refuse a registration the catalog finds incomplete
      Status: CRITICAL
      Gap Register Entry: GAP-02
      Notes: A rule following each check refuses on what it found.
    - Capability: Hold what a book, a work and a further edition must contain
      Source Finding: S3 authoring_decisions Hold what a book, a work and a further edition must contain
      Status: CRITICAL
      Gap Register Entry: GAP-03
      Notes: The checking contracts hold their descriptions.
    - Capability: Check what the catalog records
      Source Finding: S3 authoring_decisions Check what the catalog records
      Status: CRITICAL
      Gap Register Entry: GAP-04
      Notes: Each registration act checks the record it writes.
    - Capability: Record the subject callers supply
      Source Finding: S3 authoring_decisions Record the subject callers supply
      Status: CRITICAL
      Gap Register Entry: GAP-05
      Notes: The register act reads the subject where callers send it.
    - Capability: Register a copy as registered
      Source Finding: S3 authoring_decisions Register a copy as registered
      Status: CRITICAL
      Gap Register Entry: GAP-06
      Notes: The copy contract writes the state itself.
    - Capability: Keep a corrected record's state, and check it against the book description
      Source Finding: S3 authoring_decisions Keep a corrected record's state, and check it against the book description
      Status: CRITICAL
      Gap Register Entry: GAP-07
      Notes: The correction keeps the state and refuses a record that fails the description.
    - Capability: Admit a request without the rules the catalog holds
      Source Finding: S3 authoring_decisions Admit a request without the rules the catalog holds
      Status: CRITICAL
      Gap Register Entry: GAP-08
      Notes: The gates stop requiring what the catalog holds and what no act reads.
  dependency_graph:
    columns:
    - From
    - To
    - Dependency Type
    - PPS Status
    - Source Finding
    rows:
    - From: catalog
      To: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Dependency Type: platform transform
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Refusing on a list of rules
    - From: catalog
      To: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Dependency Type: platform transform
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Checking a record's structure
    - From: catalog
      To: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Dependency Type: platform transform
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Assembling a record from fields
    - From: catalog
      To: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Dependency Type: amended contract
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Confirming staff
    - From: catalog
      To: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Dependency Type: amended contract
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Checking a submission
    - From: catalog
      To: book_library_mgmt::CC_REGISTER_BOOK_V0
      Dependency Type: amended contract
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Recording a book
    - From: catalog
      To: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Dependency Type: amended contract
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Recording an edition
    - From: catalog
      To: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Dependency Type: amended contract
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Recording a copy
    - From: catalog
      To: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Dependency Type: amended contract
      PPS Status: SATISFIED
      Source Finding: S3 dependency_discoveries Correcting a record
  constraint_register:
    columns:
    - '#'
    - Constraint
    - Source Finding
    - Source
    rows:
    - '#': '1'
      Constraint: Every correct request from authorized staff is admitted, with the same outcome as today.
      Source Finding: 'S1 constraints #1'
      Source: The business author
    - '#': '2'
      Constraint: Records made under a request's own rules stay as they were made.
      Source Finding: 'S1 constraints #2'
      Source: The business author
    - '#': '3'
      Constraint: What a request says about the catalog's rules is ignored, not refused.
      Source Finding: 'S1 known_facts #9'
      Source: The business author
  gap_register:
    columns:
    - Gap Code
    - Source Finding
    - Capability
    - Owner Subdomain
    - Resolution
    rows:
    - Gap Code: GAP-01
      Source Finding: S3 authoring_decisions Refuse anyone the library has not authorized
      Capability: Refuse anyone the library has not authorized
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-02
      Source Finding: S3 authoring_decisions Refuse a registration the catalog finds incomplete
      Capability: Refuse a registration the catalog finds incomplete
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-03
      Source Finding: S3 authoring_decisions Hold what a book, a work and a further edition must contain
      Capability: Hold what a book, a work and a further edition must contain
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-04
      Source Finding: S3 authoring_decisions Check what the catalog records
      Capability: Check what the catalog records
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-05
      Source Finding: S3 authoring_decisions Record the subject callers supply
      Capability: Record the subject callers supply
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-06
      Source Finding: S3 authoring_decisions Register a copy as registered
      Capability: Register a copy as registered
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-07
      Source Finding: S3 authoring_decisions Keep a corrected record's state, and check it against the book description
      Capability: Keep a corrected record's state, and check it against the book description
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-08
      Source Finding: S3 authoring_decisions Admit a request without the rules the catalog holds
      Capability: Admit a request without the rules the catalog holds
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-09
      Source Finding: S3 analysis_findings Q9
      Capability: Establish who a caller is
      Owner Subdomain: outside the catalog
      Resolution: DEFERRED
  design_decisions:
    columns:
    - '#'
    - Decision
    - Source Finding
    - Rationale
    - Constraints Imposed
    rows:
    - '#': '1'
      Decision: Each rule is held by the step that applies it, as a fixed value.
      Source Finding: S3 analysis_findings Q1
      Rationale: A rule written where it is applied holds for every act that composes the step, and no request can widen it.
      Constraints Imposed: Nothing may hand the catalog a rule the catalog holds.
    - '#': '2'
      Decision: Each check is followed by a rule refusing when it found anything.
      Source Finding: S3 analysis_findings Q2
      Rationale: The platform check stays a reporter, as ruled; the catalog's contract decides.
      Constraints Imposed: A check's report is consumed, never left unread.
    - '#': '3'
      Decision: What each registration checks is the record it writes.
      Source Finding: S3 analysis_findings Q4
      Rationale: A check of a supplied copy judges something other than what is recorded.
      Constraints Imposed: No registration checks a copy supplied beside the record.
    - '#': '4'
      Decision: The register act records the subject where callers send it.
      Source Finding: S3 analysis_findings Q5
      Rationale: Every present caller sends it there, and every book recorded today lacks one.
      Constraints Imposed: No present caller changes what it sends.
    - '#': '5'
      Decision: A copy's registered state and a correction's state are the catalog's own.
      Source Finding: S3 analysis_findings Q6
      Rationale: There is one state a copy is registered in, and a correction does not change state.
      Constraints Imposed: No request sets a registered copy's or a corrected book's state.
    - '#': '6'
      Decision: The gates stop requiring what the catalog holds and what no act reads.
      Source Finding: S3 analysis_findings Q8
      Rationale: A gate requiring an unread field refuses a correct request for its absence.
      Constraints Imposed: Every field an act reads stays required where it was.
    - '#': '7'
      Decision: Records made before this change are left as they are.
      Source Finding: S3 analysis_findings Q10
      Rationale: The record is added to and never rewritten.
      Constraints Imposed: No migration, backfill or repair step may be authored.
  authoring_scope:
    columns:
    - Capability
    - Gap Register Ref
    rows:
    - Capability: Refuse anyone the library has not authorized
      Gap Register Ref: GAP-01
    - Capability: Refuse a registration the catalog finds incomplete
      Gap Register Ref: GAP-02
    - Capability: Hold what a book, a work and a further edition must contain
      Gap Register Ref: GAP-03
    - Capability: Check what the catalog records
      Gap Register Ref: GAP-04
    - Capability: Record the subject callers supply
      Gap Register Ref: GAP-05
    - Capability: Register a copy as registered
      Gap Register Ref: GAP-06
    - Capability: Keep a corrected record's state, and check it against the book description
      Gap Register Ref: GAP-07
    - Capability: Admit a request without the rules the catalog holds
      Gap Register Ref: GAP-08
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. Every capability that changes
is an extension of one the catalog already has: each step keeps doing what it does, and holds the
rule it applies instead of being handed it.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

## 2. Capability Graph (capability_graph)

## 3. Dependency Graph (dependency_graph)

## 4. Constraint Register (constraint_register)

## 5. Gap Register (gap_register)

## 6. Design Decisions (design_decisions)

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Establish who a caller is | GAP-09. The credentials a request presents are its own; the catalog holds the rules they are judged by and does not authenticate them. |
| Records made under a request's own rules | Declined by the business: the record is added to and never rewritten. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · constraints · business_invariants · authority_boundaries · out_of_scope |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · pps_baseline_fqdns |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
