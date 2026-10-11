# Stage 5 — Business Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 5 — Business Intent
  CR: cr_03_catalog
  Status: DRAFT
  Feeds: Stage 6 — Governance Intent
registers:
  subdomain_purpose: |2

    The Catalog subdomain governs what the library knows about its books: the works it carries, the
    editions of those works, and the physical copies on its shelves. It holds one record for each, the
    state that says whether each is in service or retired, and the details the library publishes about
    them. It records each thing being registered, its details being corrected, and its being retired or
    reinstated, and it announces the moments the business declared matter. It does not govern who borrows
    a book, what a borrower may do, or what the library charges.
  purpose_provenance:
    columns:
    - Source
    - Disposition (INHERITED, REFINED)
    - Refinement
    rows:
    - Source: CR seed §0 Subdomain Purpose
      Disposition (INHERITED, REFINED): INHERITED
      Refinement: The seed's paragraph, word for word. This phase adds nothing to it.
  subdomain_purposes:
    columns:
    - Subdomain
    - Purpose
    - Source Finding
    rows:
    - Subdomain: catalog
      Purpose: Governs what the library knows about its books — the works it carries, their editions, and the physical copies on its shelves.
      Source Finding: 'S1 cr_type #1'
  scope_boundary:
    columns:
    - Capability
    - Status (IN_SCOPE, DEFERRED)
    - Notes
    - Source Finding
    rows:
    - Capability: Announcing the three moments registering a book completes
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The act this change halted for.
      Source Finding: 'S4 authoring_scope #1'
    - Capability: Announcing the moment each remaining act completes
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Five acts, one moment each.
      Source Finding: 'S4 authoring_scope #2'
    - Capability: A moment naming a reinstatement
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: The business has declared none; authoring one here would invent business content.
      Source Finding: 'S4 authoring_scope deferred #1'
    - Capability: Refusing a declared moment that nothing announces
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: Its own question, and answering it here would refuse moments that are correct today.
      Source Finding: 'S4 authoring_scope deferred #2'
    - Capability: A moment announced per member of a collection
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: A different shape; this change announces a known few, named where the act is designed.
      Source Finding: 'S4 authoring_scope deferred #3'
  business_objects:
    columns:
    - Store Name
    - Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID)
    - Business Rationale
    - Source Finding
    rows:
    - Store Name: NONE IDENTIFIED
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): ''
      Business Rationale: ''
      Source Finding: ''
  identity_semantics:
    columns:
    - Store Name
    - Identity Field
    - Source
    - Uniqueness Rule
    - Cross-Subdomain Relationship
    - Source Finding
    rows:
    - Store Name: NONE IDENTIFIED
      Identity Field: ''
      Source: ''
      Uniqueness Rule: ''
      Cross-Subdomain Relationship: ''
      Source Finding: ''
  invariants:
    columns:
    - Invariant
    - Business Reason
    - Source Finding
    rows:
    - Invariant: An act announces every moment it completed, or the business has no account of what happened.
      Business Reason: An act that completes three moments and states one leaves two things that occurred with nothing saying so, and nobody reading the account afterwards can tell the difference between a moment that did not happen and one nobody announced.
      Source Finding: 'S4 constraint_register #1'
    - Invariant: A moment is attached to the act that completes it, never to one that merely touches the same records.
      Business Reason: Registering an additional edition reads the work it attaches to; announcing a work registered there would state that something happened which happened earlier and elsewhere.
      Source Finding: 'S4 constraint_register #2'
    - Invariant: The business is not reshaped to suit what the platform could express.
      Business Reason: The library registers a book once, as one act. Splitting it into three so that each could announce one moment would change what the business does in order to make it describable.
      Source Finding: 'S4 constraint_register #3'
    - Invariant: Only moments the business already declared are announced.
      Business Reason: A moment authored to fill a gap in an account is business content invented by whoever noticed the gap, rather than something the business decided occurred.
      Source Finding: 'S4 constraint_register #4'
    - Invariant: A limitation paid in silence produces no account at all, and no check anywhere notices.
      Business Reason: Faced with announcing one of three moments, this subdomain announced none — so the cost of the limitation was not a wrong account but the absence of one, and nothing anywhere reported a fault.
      Source Finding: 'S4 constraint_register #5'
  actions:
    columns:
    - Action
    - Object
    - Trigger
    - Status (IN_SCOPE, DEFERRED)
    - Source Finding
    rows:
    - Action: Announce the three moments registering a book completes
      Object: Announcement
      Trigger: A book being registered.
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: 'S4 capability_graph #1'
    - Action: Announce the moment each remaining act completes
      Object: Announcement
      Trigger: Any of the five acts completing.
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: 'S4 capability_graph #2'
  provisional_codes:
    columns:
    - Subdomain
    - Provisional Code
    - Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE)
    - Summary
    - Source Finding
    rows:
    - Subdomain: NONE IDENTIFIED
      Provisional Code: ''
      Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE): ''
      Summary: ''
      Source Finding: ''
  cross_subdomain_refs:
    columns:
    - CC Code
    - Defined In
    - Role
    - Source Finding
    rows:
    - CC Code: NONE IDENTIFIED
      Defined In: ''
      Role: ''
      Source Finding: ''
```

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

### Purpose of every subdomain this change touches

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | Capability graph, gaps, design decisions, authoring scope | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |
