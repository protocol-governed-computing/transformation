# Stage 6 — Governance Intent: book_library_mgmt / catalog
**Stage:** 6 — Governance Intent
**CR:** cr_04_catalog
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `book_library_mgmt` |
| Primary subdomain | `catalog` — EXISTING — modified by this CR |
| Authority class | reuse existing — a librarian requests, the catalog admits or turns away, the library's rules decide who may act; no new actor type |
| Governing constitutions | `intent::CONSTITUTION_INTENT_V0` |

What each catalog operation requires is the catalog's own account of what it does, so all three
corrections belong to the subdomain that declares them. Nothing new stands on its own; no artifact is
authored and no subdomain is created.

**No artifact outside this subdomain is touched.** Each of the three boundaries is reached by exactly
one artifact — the workflow it admits — and by nothing else. The three things that decide who may
perform an operation are read by no step of any of the subdomain's ten operations and are not
reached by restating what an operation needs.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Admitting a request to register a further edition | catalog | OWNED | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | S4 gap_register GAP-1 |
| Admitting a request to correct bibliographic information | catalog | OWNED | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | S4 gap_register GAP-2 |
| Admitting a request to register a work | catalog | DEFERRED | book_library_mgmt::IN_REGISTER_BOOK_V0 | S4 authoring_scope deferred #1 |
| The three operations | catalog | SATISFIED | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | S4 capability_graph #5 |
| Deciding who may perform an operation | catalog | SATISFIED | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | S4 capability_graph #4 |
| Holding what the catalog knows | catalog | SATISFIED | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | S4 capability_graph #6 |
| Comparing what an operation requires against what it uses | catalog | DEFERRED | | S4 authoring_scope deferred #1 |
| Declaring the form of a detail the catalog holds | catalog | DEFERRED | | S4 authoring_scope deferred #2 |
| The operations of subdomains and domains other than the catalog | catalog | DEFERRED | | S4 authoring_scope deferred #3 |

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
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | Requires eleven things, all of which its operation reads, and states the publication year as a word where the other three statements of its form say number. Turns away every correct request. | EXTEND | S4 gap_register GAP-1 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Requires eight things; its operation reads five. The title, the author and the publication year are read by no step, and their absence turns away every correction. | EXTEND | S4 gap_register GAP-2 |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | Requires ten things; its operation reads eleven. The subject is read and not required, so a request without one is admitted and then cannot be carried out. Unchanged here: every present caller sends the subject nested inside the details of the book, so requiring it moves the boundary and the caller together. | REVIEW | S4 authoring_scope deferred #1 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | Reads all eleven things its boundary requires. Correct as it stands. | REUSE | S4 capability_graph #5 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Reads the record named and the details being changed, across four steps. Correct as it stands. | REUSE | S4 capability_graph #5 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | Reads eleven things, one of which its boundary does not require, and rebuilds the details of the book from what the request supplies at its top level rather than from the details the caller sends. Unchanged. | REVIEW | S4 capability_graph #5 |
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | Declares the six stores the catalog owns and the paths they occupy, and no form for any detail it holds. Unchanged by this change and named as the reason the form rests on agreement. | REVIEW | S4 constraint_register #6 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| REQUIRES_ONLY_WHAT_IT_USES | An operation requires only what its steps read. A requirement no step reads turns away correct requests and admits nothing extra. | S4 constraint_register #1 |
| USES_ONLY_WHAT_IT_REQUIRES | An operation reads only what its boundary requires. A use no requirement covers admits a request the operation then cannot carry out, so a declaration gap surfaces part-way through instead of as a refusal before anything happened. | S4 constraint_register #1 |
| AUTHORITY_IS_UNTOUCHED | Nothing about who may perform an operation changes. The three things that decide it are stated separately, appear in all ten operations, and are read by no step of any of them. | S4 constraint_register #2 |
| HELD_RECORDS_ARE_NOT_DISTURBED | No record the catalog already holds is migrated, rewritten or revalidated. What is wrong is what a new request must supply, not what the catalog knows. | S4 constraint_register #3 |
| A_YEAR_IS_A_NUMBER | A publication year is stated as a number wherever an operation asks for one. The catalog displays a year as a number and every request the library makes supplies one. | S4 constraint_register #4 |
| NO_CORRECT_REQUEST_BECOMES_HARDER | No requirement is added where any present caller would then fail. This is what the ruling against gaining requirements was for, and it is what defers the third correction rather than permitting it. | S4 constraint_register #5 |
| AGREEMENT_IS_THE_ONLY_AUTHORITY | Where no artifact declares the form of a detail, the correction rests on agreement among the statements of it and on the data. That is weaker than a declaration and is what exists. | S4 constraint_register #6 |
| A_DEFERRAL_RECORDS_ITS_GROUND | The third boundary is deferred with the reason written down, not dropped. A defect nobody found and a defect deferred for a stated reason are different states, and only one of them is governed. | S4 design_decisions #5 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Admitting a request to register a further edition | catalog | S4 gap_register GAP-1 |
| Admitting a request to correct bibliographic information | catalog | S4 gap_register GAP-2 |

---

## Gate 1 — Design Approval
