# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 4 — Business Model
  CR: cr_03_catalog
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
      Role: Performs the acts, and states what each of them completed.
      Authority Class: Declaring — an announcement is the act's own account of what it did.
      Source Finding: 'S1 cr_type #1'
    - Actor: Library staff
      Role: Perform the acts the catalog admits.
      Authority Class: Acting — unchanged by this change.
      Source Finding: 'S2 actors #1'
    - Actor: The platform
      Role: Seals the moments an act announces, in order, and announces each when the act reaches its ending.
      Authority Class: Enabling — the capability this change waited for.
      Source Finding: S3 analysis_findings Q3
  bm_entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Source Finding
    rows:
    - Entity: Moment
      Description: Something the business declares occurred, stated by the act that completed it.
      Store Model: Six are declared; none is announced.
      Source Finding: 'S2 entities #1'
    - Entity: Act
      Description: Something the catalog does as one unit, which completes or is refused.
      Store Model: Nine, each admitted by its own intent.
      Source Finding: 'S2 entities #2'
    - Entity: Announcement
      Description: What an act states at its ending about the moments it completed.
      Store Model: None exists anywhere in this subdomain.
      Source Finding: S3 analysis_findings Q2
  resources:
    columns:
    - Resource
    - Description
    - Source Finding
    rows:
    - Resource: The six declared moments
      Description: Registered work, registered book, registered physical copy, updated bibliographic information, retired book, retired physical copy. Referenced by nothing.
      Source Finding: 'S2 belief_verification #1'
    - Resource: The act that completes three
      Description: Registering a book admits a work, its first edition and that edition's first physical copy.
      Source Finding: S3 analysis_findings Q2
    - Resource: The capability the platform now holds
      Description: An ordered sequence announced at one ending, a repeat refused, an announcement that cannot be made reported.
      Source Finding: S3 analysis_findings Q3
  events:
    columns:
    - Event
    - Trigger
    - Lifecycle Meaning
    - Source Finding
    rows:
    - Event: An act announced what it completed
      Trigger: An act reaching an ending it declares announcements for
      Lifecycle Meaning: The business has an account of what happened, which it has never had.
      Source Finding: 'S1 business_events #1'
    - Event: A declared moment stayed silent
      Trigger: An act completing a moment and stating nothing
      Lifecycle Meaning: The state this change ends; it is the present state of every act.
      Source Finding: 'S2 belief_verification #1'
  relationships:
    columns:
    - Subject
    - Verb
    - Object
    - Capability Need
    - Source Finding
    rows:
    - Subject: Act
      Verb: announces
      Object: Moment
      Capability Need: Announcing the three moments registering a book completes.
      Source Finding: 'S3 authoring_decisions #1'
    - Subject: Act
      Verb: announces
      Object: Moment
      Capability Need: Announcing the moment each remaining act completes.
      Source Finding: 'S3 authoring_decisions #2'
    - Subject: Catalog
      Verb: attaches
      Object: Moment
      Capability Need: Attaching the moment naming a registered work to the act that claims its identity.
      Source Finding: 'S3 authoring_decisions #3'
  capability_graph:
    columns:
    - Capability
    - Source Finding
    - Status
    - Gap Register Entry
    - Notes
    rows:
    - Capability: Announcing the three moments registering a book completes
      Source Finding: 'S3 authoring_decisions #1'
      Status: CRITICAL
      Gap Register Entry: GAP-1
      Notes: The act this dossier halted for; three moments at one ending.
    - Capability: Announcing the moment each remaining act completes
      Source Finding: 'S3 authoring_decisions #2'
      Status: CRITICAL
      Gap Register Entry: GAP-2
      Notes: Five acts, one moment each — a sequence of one.
    - Capability: Attaching the moment naming a registered work to the act that claims its identity
      Source Finding: 'S3 authoring_decisions #3'
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: 'The composition decides it: one act claims the work, the other resolves it.'
    - Capability: Announcing an ordered sequence at one ending
      Source Finding: 'S3 dependency_discoveries #1'
      Status: SATISFIED
      Gap Register Entry: ''
      Notes: The platform states the model, holds it, seals the order and keeps it.
  dependency_graph:
    columns:
    - From
    - To
    - Dependency Type
    - PPS Status
    - Source Finding
    rows:
    - From: catalog
      To: workflow
      Dependency Type: data read
      PPS Status: SATISFIED
      Source Finding: 'S3 dependency_discoveries #1 — the platform admits and seals what an act announces.'
    - From: catalog
      To: event
      Dependency Type: data read
      PPS Status: SATISFIED
      Source Finding: 'S3 dependency_discoveries #2 — all six moments are declared artifacts already.'
    - From: catalog
      To: catalog
      Dependency Type: capability call
      PPS Status: SATISFIED
      Source Finding: 'S3 dependency_discoveries #3 — every act exists and runs; what it lacks is the statement.'
  constraint_register:
    columns:
    - '#'
    - Constraint
    - Source Finding
    - Source
    rows:
    - '#': '1'
      Constraint: An act announces every moment it completed, or the business has no account of what happened.
      Source Finding: 'S1 constraints #1'
      Source: governance rule
    - '#': '2'
      Constraint: A moment is attached to the act that completes it, never to one that merely touches the same records.
      Source Finding: S3 analysis_findings Q1
      Source: governance rule
    - '#': '3'
      Constraint: The business is not reshaped to suit what the platform could express.
      Source Finding: 'S1 constraints #2'
      Source: governance rule
    - '#': '4'
      Constraint: Only moments the business already declared are announced.
      Source Finding: 'S3 verification_results #4'
      Source: governance rule
    - '#': '5'
      Constraint: A limitation paid in silence produces no account at all, and no check anywhere notices.
      Source Finding: 'S2 belief_verification #3'
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
      Capability: Announcing the three moments registering a book completes
      Owner Subdomain: catalog
      Resolution: EXTEND
    - Gap Code: GAP-2
      Source Finding: 'S3 authoring_decisions #2'
      Capability: Announcing the moment each remaining act completes
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
      Decision: Registering a book announces three moments at one ending.
      Source Finding: 'S3 authoring_decisions #1'
      Rationale: The act completes all three and is the only act that does.
      Constraints Imposed: Rules out announcing one and leaving two silent, and rules out splitting the act.
    - '#': '2'
      Decision: 'The order announced is the order the business completes them: the work, then the book, then the physical copy.'
      Source Finding: S3 analysis_findings Q3
      Rationale: The order is normative and a reader of the account sees it; the business's own order is the one that reads correctly.
      Constraints Imposed: Fixes the order in the design rather than leaving it to how the composition was sealed.
    - '#': '3'
      Decision: Each remaining act announces the one moment it completes.
      Source Finding: 'S3 authoring_decisions #2'
      Rationale: Five acts complete one moment each and can say so; a sequence of one is what the platform already ran.
      Constraints Imposed: Rules out leaving any declared moment silent.
    - '#': '4'
      Decision: Reinstatement announces nothing.
      Source Finding: 'S3 verification_results #4'
      Rationale: The business declared no moment for it, and this change announces only moments the business already declared.
      Constraints Imposed: Rules out authoring a moment to fill a gap the business has not stated.
  authoring_scope:
    columns:
    - Capability
    - Gap Register Ref
    rows:
    - Capability: Announcing the three moments registering a book completes
      Gap Register Ref: GAP-1
    - Capability: Announcing the moment each remaining act completes
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
| A moment naming a reinstatement | The business has declared none; authoring one here would invent business content. |
| Refusing a declared moment that nothing announces | Its own question, and answering it here would refuse moments that are correct today. |
| A moment announced per member of a collection | A different shape; this change announces a known few, named where the act is designed. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
