# Stage 5 — Business Intent: book_library_mgmt / catalog

**Stage:** 5 — Business Intent

**CR:** cr_05_catalog

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

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
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| catalog | Governs what the library knows about its books, and now holds every rule it applies to them. | S4 bm_entities The Catalog's Rules |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Refuse anyone the library has not authorized | IN_SCOPE | The confirming step holds the library's rules; every act composes it. | S4 authoring_scope GAP-01 |
| Refuse a registration the catalog finds incomplete | IN_SCOPE | A rule following each check refuses on what it found. | S4 authoring_scope GAP-02 |
| Hold what a book, a work and a further edition must contain | IN_SCOPE | The checking contracts hold their descriptions. | S4 authoring_scope GAP-03 |
| Check what the catalog records | IN_SCOPE | Each registration act checks the record it writes. | S4 authoring_scope GAP-04 |
| Record the subject callers supply | IN_SCOPE | The register act reads the subject where callers send it. | S4 authoring_scope GAP-05 |
| Register a copy as registered | IN_SCOPE | The copy contract writes the state itself. | S4 authoring_scope GAP-06 |
| Keep a corrected record's state, and check it against the book description | IN_SCOPE | The correction keeps the state and refuses a record that fails the description. | S4 authoring_scope GAP-07 |
| Admit a request without the rules the catalog holds | IN_SCOPE | The gates stop requiring what the catalog holds and what no act reads; nothing a caller sends needs to change. | S4 authoring_scope GAP-08 |
| Establish who a caller is | DEFERRED | The credentials a request presents stay its own. | S4 authoring_scope Establish who a caller is |
| Records made under a request's own rules | DEFERRED | Declined by the business; the record is added to and never rewritten. | S4 authoring_scope Records made under a request's own rules |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Book record | MUTABLE_STATE | Unchanged by this change, and named because what may be written into it changes: only a book meeting the description, with the subject callers supply, and a correction only with the state the record has. | S4 bm_entities The Book |
| Copy record | MUTABLE_STATE | Unchanged by this change, and named because a copy is written only as registered. | S4 bm_entities The Physical Copy |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Book record | Title, author and publication year | Supplied by staff registering the book | No two registered books share them; unchanged by this change. | None | S4 bm_entities The Book |
| Copy record | Barcode | Supplied by staff registering the copy | No two copies share a barcode; unchanged by this change. | None | S4 bm_entities The Physical Copy |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| No catalog operation is performed by anyone the library has not authorized. | Only authorized staff perform catalog operations. | S1 business_invariants #1 |
| No book, work or further edition is registered without what the library says it must contain. | The library said the parts are required. | S1 business_invariants #2 |
| What the catalog checks is what it records. | A check of anything else judges nothing that is written. | S1 business_invariants #3 |
| No physical copy is registered in any state but registered. | There is one state a copy is registered in. | S1 business_invariants #4 |
| A business rule of the catalog's is held by the catalog, and no request changes it. | A business rule the caller supplies is a business rule the caller can widen. | S1 business_invariants #5 |
| A refusal changes no record. | A refused request leaves the catalog as it found it. | S1 business_invariants #6 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Refuse | A request from anyone the library has not authorized | Any catalog request | IN_SCOPE | S4 capability_graph Refuse anyone the library has not authorized |
| Refuse | A book, work or further edition lacking what it must contain | A registration | IN_SCOPE | S4 capability_graph Refuse a registration the catalog finds incomplete |
| Register | A copy, as registered | A copy registration | IN_SCOPE | S4 capability_graph Register a copy as registered |
| Correct | A book's bibliographic information, keeping its state | A correction | IN_SCOPE | S4 capability_graph Keep a corrected record's state, and check it against the book description |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|-----------|------|----------------|
| NONE IDENTIFIED | | | |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
