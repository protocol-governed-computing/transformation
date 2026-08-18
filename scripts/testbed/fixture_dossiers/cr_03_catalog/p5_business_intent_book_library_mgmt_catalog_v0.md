# Stage 5 — Business Intent: book_library_mgmt / catalog
**Stage:** 5 — Business Intent
**CR:** cr_03_catalog
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Catalog subdomain governs what the library knows about its books: the works it carries, the
editions of those works, and the physical copies on its shelves. It holds one record for each, the
state that says whether each is in service or retired, and the details the library publishes about
them. It records each thing being registered, its details being corrected, and its being retired or
reinstated, and it announces the moments the business declared matter. It does not govern who borrows
a book, what a borrower may do, or what the library charges.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| catalog | Governs what the library knows about its books — the works it carries, their editions, and the physical copies on its shelves. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Announcing the three moments registering a book completes | IN_SCOPE | The act this change halted for. | S4 authoring_scope #1 |
| Announcing the moment each remaining act completes | IN_SCOPE | Five acts, one moment each. | S4 authoring_scope #2 |
| A moment naming a reinstatement | DEFERRED | The business has declared none; authoring one here would invent business content. | S4 authoring_scope deferred #1 |
| Refusing a declared moment that nothing announces | DEFERRED | Its own question, and answering it here would refuse moments that are correct today. | S4 authoring_scope deferred #2 |
| A moment announced per member of a collection | DEFERRED | A different shape; this change announces a known few, named where the act is designed. | S4 authoring_scope deferred #3 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| NONE IDENTIFIED |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| An act announces every moment it completed, or the business has no account of what happened. | An act that completes three moments and states one leaves two things that occurred with nothing saying so, and nobody reading the account afterwards can tell the difference between a moment that did not happen and one nobody announced. | S4 constraint_register #1 |
| A moment is attached to the act that completes it, never to one that merely touches the same records. | Registering an additional edition reads the work it attaches to; announcing a work registered there would state that something happened which happened earlier and elsewhere. | S4 constraint_register #2 |
| The business is not reshaped to suit what the platform could express. | The library registers a book once, as one act. Splitting it into three so that each could announce one moment would change what the business does in order to make it describable. | S4 constraint_register #3 |
| Only moments the business already declared are announced. | A moment authored to fill a gap in an account is business content invented by whoever noticed the gap, rather than something the business decided occurred. | S4 constraint_register #4 |
| A limitation paid in silence produces no account at all, and no check anywhere notices. | Faced with announcing one of three moments, this subdomain announced none — so the cost of the limitation was not a wrong account but the absence of one, and nothing anywhere reported a fault. | S4 constraint_register #5 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Announce the three moments registering a book completes | Announcement | A book being registered. | IN_SCOPE | S4 capability_graph #1 |
| Announce the moment each remaining act completes | Announcement | Any of the five acts completing. | IN_SCOPE | S4 capability_graph #2 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|
| NONE IDENTIFIED |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | Capability graph, gaps, design decisions, authoring scope | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |
