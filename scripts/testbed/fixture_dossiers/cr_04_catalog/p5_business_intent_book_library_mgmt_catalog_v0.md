# Stage 5 — Business Intent: book_library_mgmt / catalog
**Stage:** 5 — Business Intent
**CR:** cr_04_catalog
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
| catalog | Governs what the library knows about its books — the works it carries, their editions, and the physical copies on its shelves — and states what each of its operations needs from the person performing it. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Admitting a request to register a further edition | IN_SCOPE | The publication year is stated as a number, as the other three statements of its form already say. | S4 authoring_scope #1 |
| Admitting a request to correct bibliographic information | IN_SCOPE | The title, the author and the publication year are withdrawn; no step reads them. A boundary is stated whole, so withdrawing a requirement authors a successor rather than amending the boundary to say less than it said. | S4 authoring_scope #2 |
| Admitting a request to register a work | DEFERRED | The act reads the subject at the top of the request and every present caller sends it nested inside the details of the book. Requiring it moves the boundary and every caller together, which this change's seed forbids. | S4 authoring_scope deferred #1 |
| Comparing what an operation requires against what it uses | DEFERRED | Nothing performs it in the composition. Whether it belongs to this subdomain or to the platform is not this change's to settle. | S4 authoring_scope deferred #1 |
| Declaring the form of a detail the catalog holds | DEFERRED | The store declares paths and no forms. Giving the catalog an authority over forms is a larger change than bringing one boundary into agreement with three statements. | S4 authoring_scope deferred #2 |
| The operations of subdomains and domains other than the catalog | DEFERRED | Each is its own business, and the same comparison reports findings elsewhere that were not examined here. | S4 authoring_scope deferred #3 |

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
| An operation requires only what it uses, and uses only what it requires. | A requirement no step reads turns away correct requests and admits nothing extra; a use no requirement covers admits a request the operation then cannot carry out. Both are one disagreement between two statements of one fact, and stating the rule in only one direction is what let the third defect survive discovery of the first two. | S4 constraint_register #1 |
| Nothing about who may perform an operation changes. | The three things that decide who may act are stated separately from what an operation needs, appear in all ten operations, and are read by no step of any of them. Restating what an operation needs cannot reach them, and a change that quietly did would be a relaxation rather than a correction. | S4 constraint_register #2 |
| The records the catalog already holds are not migrated, rewritten or revalidated. | What is wrong is what a request must supply, not what the catalog knows. A record registered before this change is as good afterwards. | S4 constraint_register #3 |
| A publication year is stated as a number wherever an operation asks for one. | The catalog displays a year as a number and every request the library makes supplies one, so a librarian who types the year they see is turned away by the only boundary that disagrees. | S4 constraint_register #4 |
| No correct request becomes harder to make. | This is what the ruling against gaining requirements was for, and it decided the shape of this change. Requiring the subject looked like it added nothing a requester was not already sending; the requester sends it nested inside the details of the book and the act reads it at the top of the request, so requiring it makes every present request fail. The ruling holds and the correction is deferred. | S4 constraint_register #5 |
| The form of a detail the catalog holds is settled by no artifact, so agreement among the statements of it is the only authority available. | There is nothing to defer to. The store declares six paths and no forms, so the correction rests on three statements agreeing and the data agreeing with them, which is weaker than a declaration and is what exists. | S4 constraint_register #6 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Admit a request to register a further edition | Request | A librarian registering a further edition of a held work. | IN_SCOPE | S4 capability_graph #1 |
| Admit a request to correct bibliographic information | Request | A librarian correcting the details of a held record. | IN_SCOPE | S4 capability_graph #2 |
| Admit a request to register a work | Request | A librarian registering a work the library does not yet carry. | DEFERRED | S4 capability_graph #3 |
| Turn away a request that does not supply what the operation needs | Request | Something the operation needs being absent or in the wrong form. | IN_SCOPE | S1 operation_refusals #1 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| catalog | IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | IN | The boundary that admits a correction, requiring the record named and the details being changed and nothing else | S4 gap_register GAP-2 |
| catalog | WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | WF | The act that corrects a held record, admitted by the successor boundary. Its steps are those of the act it supersedes | S4 gap_register GAP-2 |

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
