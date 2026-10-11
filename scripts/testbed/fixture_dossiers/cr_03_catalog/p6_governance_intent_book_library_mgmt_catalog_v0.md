# Stage 6 — Governance Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 6 — Governance Intent
  CR: cr_03_catalog
  Status: DRAFT
  Feeds: Stage 7 — Design Intent
registers:
  ownership:
    columns:
    - Capability
    - Owner Subdomain
    - Disposition (OWNED, SATISFIED, DEFERRED)
    - Existing Artifact
    - Source Finding
    rows:
    - Capability: Announcing the three moments registering a book completes
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Source Finding: S4 gap_register GAP-1
    - Capability: Announcing the moment each remaining act completes
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Source Finding: S4 gap_register GAP-2
    - Capability: Attaching the moment naming a registered work to the act that claims its identity
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Source Finding: 'S4 capability_graph #3'
    - Capability: Announcing an ordered sequence at one ending
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: workflow::CONSTITUTION_WORKFLOW_V0
      Source Finding: 'S4 capability_graph #4'
    - Capability: A moment naming a reinstatement
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: 'S4 authoring_scope deferred #1'
    - Capability: Refusing a declared moment that nothing announces
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: 'S4 authoring_scope deferred #2'
    - Capability: A moment announced per member of a collection
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: 'S4 authoring_scope deferred #3'
  storage_governance:
    columns:
    - Storage Need
    - Purpose
    - Subdomain
    - Source Finding
    rows:
    - Storage Need: NONE IDENTIFIED
      Purpose: ''
      Subdomain: ''
      Source Finding: ''
  cross_subdomain_deps:
    columns:
    - Dependency
    - Direction
    - Existing Artifact
    - Status (SATISFIED, GAP)
    - Source Finding
    rows:
    - Dependency: NONE IDENTIFIED
      Direction: ''
      Existing Artifact: ''
      Status (SATISFIED, GAP): ''
      Source Finding: ''
  pps_artifacts_requiring_action:
    columns:
    - FQDN
    - Current Status
    - Action (REPLACE, REVIEW, REUSE, EXTEND)
    - Source Finding
    rows:
    - FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      Current Status: Admits a work, its first edition and that edition's first physical copy, and announces none of the three.
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S4 gap_register GAP-1
    - FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Current Status: Registers a further edition of a work the library already holds, and announces nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S4 gap_register GAP-2
    - FQDN: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Current Status: Registers a further copy of an edition, and announces nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S4 gap_register GAP-2
    - FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Current Status: Corrects what the library publishes about a book, and announces nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S4 gap_register GAP-2
    - FQDN: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Current Status: Takes a book out of service, and announces nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S4 gap_register GAP-2
    - FQDN: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Current Status: Takes a physical copy out of service, and announces nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S4 gap_register GAP-2
    - FQDN: book_library_mgmt::EV_WORK_REGISTERED_V0
      Current Status: Declares the moment a work enters the catalog. Referenced by nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 dependency_graph #2'
    - FQDN: book_library_mgmt::EV_BOOK_REGISTERED_V0
      Current Status: Declares the moment a book enters the catalog. Referenced by nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 dependency_graph #2'
    - FQDN: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      Current Status: Declares the moment a physical copy enters the catalog. Referenced by nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 dependency_graph #2'
    - FQDN: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      Current Status: Declares the moment a book's published details are corrected. Referenced by nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 dependency_graph #2'
    - FQDN: book_library_mgmt::EV_BOOK_RETIRED_V0
      Current Status: Declares the moment a book leaves service. Referenced by nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 dependency_graph #2'
    - FQDN: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      Current Status: Declares the moment a physical copy leaves service. Referenced by nothing.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 dependency_graph #2'
    - FQDN: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Current Status: Returns a book to service. The business declares no moment for it, so it announces nothing and this change leaves it alone.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REVIEW
      Source Finding: 'S4 design_decisions #4'
    - FQDN: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Current Status: Returns a physical copy to service. The same.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REVIEW
      Source Finding: 'S4 design_decisions #4'
    - FQDN: book_library_mgmt::AC_LIBRARY_STAFF_V0
      Current Status: The actor every catalog act runs as. Unchanged by this change, and carried unchanged by every act it re-renders.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 actors #2'
  boundary_rules:
    columns:
    - Rule Name
    - Statement
    - Source Finding
    rows:
    - Rule Name: AN_ACT_ANNOUNCES_WHAT_IT_COMPLETED
      Statement: An act announces every moment it completed, or the business has no account of what happened. A moment that occurred and was not announced cannot be told apart afterwards from one that never occurred.
      Source Finding: 'S4 constraint_register #1'
    - Rule Name: A_MOMENT_BELONGS_TO_THE_ACT_THAT_COMPLETES_IT
      Statement: A moment is attached to the act that completes it, never to one that merely touches the same records.
      Source Finding: 'S4 constraint_register #2'
    - Rule Name: THE_BUSINESS_IS_NOT_RESHAPED_TO_SUIT_THE_PLATFORM
      Statement: The library registers a book once, as one act. It is not split into three so that each part may announce one moment.
      Source Finding: 'S4 constraint_register #3'
    - Rule Name: ONLY_DECLARED_MOMENTS_ARE_ANNOUNCED
      Statement: Only moments the business already declared are announced; a moment authored to fill a gap in an account is business content nobody decided.
      Source Finding: 'S4 constraint_register #4'
    - Rule Name: THE_ORDER_ANNOUNCED_IS_THE_ORDER_COMPLETED
      Statement: Where an act announces several, they are announced in the order the business completes them. The order is normative and a reader of the account sees it.
      Source Finding: 'S4 design_decisions #2'
  governance_outcome:
    columns:
    - Capability
    - Owner Subdomain
    - Source Finding
    rows:
    - Capability: Announcing the three moments registering a book completes
      Owner Subdomain: catalog
      Source Finding: S4 gap_register GAP-1
    - Capability: Announcing the moment each remaining act completes
      Owner Subdomain: catalog
      Source Finding: S4 gap_register GAP-2
```

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `book_library_mgmt` |
| Primary subdomain | `catalog` — EXISTING — modified by this CR |
| Authority class | reuse existing — an act announces what it completed; no new actor type |
| Governing constitutions | `workflow::CONSTITUTION_WORKFLOW_V0`, `event::CONSTITUTION_EVENT_V0`, `fb.constitution::CONSTITUTION_GOVERNANCE_V0` |

Every act and every moment belongs to catalog already. What changes is what its acts state about
what they did, declared in the acts themselves. No subdomain is created.

---

## 1. Subdomain Boundary — Ownership

---

## 2. Storage Governance Requirements

---

## 3. Cross-Subdomain Dependency Declaration

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
