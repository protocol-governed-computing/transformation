# Stage 6 — Governance Intent: book_library_mgmt / catalog
**Stage:** 6 — Governance Intent
**CR:** cr_03_catalog
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

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

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Announcing the three moments registering a book completes | catalog | OWNED | book_library_mgmt::WF_REGISTER_BOOK_V0 | S4 gap_register GAP-1 |
| Announcing the moment each remaining act completes | catalog | OWNED | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | S4 gap_register GAP-2 |
| Attaching the moment naming a registered work to the act that claims its identity | catalog | SATISFIED | book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | S4 capability_graph #3 |
| Announcing an ordered sequence at one ending | catalog | SATISFIED | workflow::CONSTITUTION_WORKFLOW_V0 | S4 capability_graph #4 |
| A moment naming a reinstatement | catalog | DEFERRED | | S4 authoring_scope deferred #1 |
| Refusing a declared moment that nothing announces | catalog | DEFERRED | | S4 authoring_scope deferred #2 |
| A moment announced per member of a collection | catalog | DEFERRED | | S4 authoring_scope deferred #3 |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| NONE IDENTIFIED |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | Admits a work, its first edition and that edition's first physical copy, and announces none of the three. | EXTEND | S4 gap_register GAP-1 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | Registers a further edition of a work the library already holds, and announces nothing. | EXTEND | S4 gap_register GAP-2 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | Registers a further copy of an edition, and announces nothing. | EXTEND | S4 gap_register GAP-2 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Corrects what the library publishes about a book, and announces nothing. | EXTEND | S4 gap_register GAP-2 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | Takes a book out of service, and announces nothing. | EXTEND | S4 gap_register GAP-2 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | Takes a physical copy out of service, and announces nothing. | EXTEND | S4 gap_register GAP-2 |
| book_library_mgmt::EV_WORK_REGISTERED_V0 | Declares the moment a work enters the catalog. Referenced by nothing. | REUSE | S4 dependency_graph #2 |
| book_library_mgmt::EV_BOOK_REGISTERED_V0 | Declares the moment a book enters the catalog. Referenced by nothing. | REUSE | S4 dependency_graph #2 |
| book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | Declares the moment a physical copy enters the catalog. Referenced by nothing. | REUSE | S4 dependency_graph #2 |
| book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | Declares the moment a book's published details are corrected. Referenced by nothing. | REUSE | S4 dependency_graph #2 |
| book_library_mgmt::EV_BOOK_RETIRED_V0 | Declares the moment a book leaves service. Referenced by nothing. | REUSE | S4 dependency_graph #2 |
| book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | Declares the moment a physical copy leaves service. Referenced by nothing. | REUSE | S4 dependency_graph #2 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | Returns a book to service. The business declares no moment for it, so it announces nothing and this change leaves it alone. | REVIEW | S4 design_decisions #4 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | Returns a physical copy to service. The same. | REVIEW | S4 design_decisions #4 |
| book_library_mgmt::AC_LIBRARY_STAFF_V0 | The actor every catalog act runs as. Unchanged by this change, and carried unchanged by every act it re-renders. | REUSE | S4 actors #2 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| AN_ACT_ANNOUNCES_WHAT_IT_COMPLETED | An act announces every moment it completed, or the business has no account of what happened. A moment that occurred and was not announced cannot be told apart afterwards from one that never occurred. | S4 constraint_register #1 |
| A_MOMENT_BELONGS_TO_THE_ACT_THAT_COMPLETES_IT | A moment is attached to the act that completes it, never to one that merely touches the same records. | S4 constraint_register #2 |
| THE_BUSINESS_IS_NOT_RESHAPED_TO_SUIT_THE_PLATFORM | The library registers a book once, as one act. It is not split into three so that each part may announce one moment. | S4 constraint_register #3 |
| ONLY_DECLARED_MOMENTS_ARE_ANNOUNCED | Only moments the business already declared are announced; a moment authored to fill a gap in an account is business content nobody decided. | S4 constraint_register #4 |
| THE_ORDER_ANNOUNCED_IS_THE_ORDER_COMPLETED | Where an act announces several, they are announced in the order the business completes them. The order is normative and a reader of the account sees it. | S4 design_decisions #2 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Announcing the three moments registering a book completes | catalog | S4 gap_register GAP-1 |
| Announcing the moment each remaining act completes | catalog | S4 gap_register GAP-2 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
