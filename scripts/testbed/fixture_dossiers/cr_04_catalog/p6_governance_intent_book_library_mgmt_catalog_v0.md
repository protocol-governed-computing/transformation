# Stage 6 — Governance Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 6 — Governance Intent
  CR: cr_04_catalog
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
    - Capability: Admitting a request to register a further edition
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Source Finding: S4 gap_register GAP-1
    - Capability: Admitting a request to correct bibliographic information
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Source Finding: S4 gap_register GAP-2
    - Capability: Admitting a request to register a work
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Source Finding: 'S4 authoring_scope deferred #1'
    - Capability: The three operations
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Source Finding: 'S4 capability_graph #5'
    - Capability: Deciding who may perform an operation
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Source Finding: 'S4 capability_graph #4'
    - Capability: Holding what the catalog knows
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): SATISFIED
      Existing Artifact: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Source Finding: 'S4 capability_graph #6'
    - Capability: Comparing what an operation requires against what it uses
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: 'S4 authoring_scope deferred #1'
    - Capability: Declaring the form of a detail the catalog holds
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: 'S4 authoring_scope deferred #2'
    - Capability: The operations of subdomains and domains other than the catalog
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
    - FQDN: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Current Status: Requires eleven things, all of which its operation reads, and states the publication year as a word where the other three statements of its form say number. Turns away every correct request.
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S4 gap_register GAP-1
    - FQDN: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Current Status: Requires eight things; its operation reads five. The title, the author and the publication year are read by no step, and their absence turns away every correction.
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S4 gap_register GAP-2
    - FQDN: book_library_mgmt::IN_REGISTER_BOOK_V0
      Current Status: 'Requires ten things; its operation reads eleven. The subject is read and not required, so a request without one is admitted and then cannot be carried out. Unchanged here: every present caller sends the subject nested inside the details of the book, so requiring it moves the boundary and the caller together.'
      Action (REPLACE, REVIEW, REUSE, EXTEND): REVIEW
      Source Finding: 'S4 authoring_scope deferred #1'
    - FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Current Status: Reads all eleven things its boundary requires. Correct as it stands.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 capability_graph #5'
    - FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Current Status: Reads the record named and the details being changed, across four steps. Correct as it stands.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: 'S4 capability_graph #5'
    - FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      Current Status: Reads eleven things, one of which its boundary does not require, and rebuilds the details of the book from what the request supplies at its top level rather than from the details the caller sends. Unchanged.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REVIEW
      Source Finding: 'S4 capability_graph #5'
    - FQDN: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Current Status: Declares the six stores the catalog owns and the paths they occupy, and no form for any detail it holds. Unchanged by this change and named as the reason the form rests on agreement.
      Action (REPLACE, REVIEW, REUSE, EXTEND): REVIEW
      Source Finding: 'S4 constraint_register #6'
  boundary_rules:
    columns:
    - Rule Name
    - Statement
    - Source Finding
    rows:
    - Rule Name: REQUIRES_ONLY_WHAT_IT_USES
      Statement: An operation requires only what its steps read. A requirement no step reads turns away correct requests and admits nothing extra.
      Source Finding: 'S4 constraint_register #1'
    - Rule Name: USES_ONLY_WHAT_IT_REQUIRES
      Statement: An operation reads only what its boundary requires. A use no requirement covers admits a request the operation then cannot carry out, so a declaration gap surfaces part-way through instead of as a refusal before anything happened.
      Source Finding: 'S4 constraint_register #1'
    - Rule Name: AUTHORITY_IS_UNTOUCHED
      Statement: Nothing about who may perform an operation changes. The three things that decide it are stated separately, appear in all ten operations, and are read by no step of any of them.
      Source Finding: 'S4 constraint_register #2'
    - Rule Name: HELD_RECORDS_ARE_NOT_DISTURBED
      Statement: No record the catalog already holds is migrated, rewritten or revalidated. What is wrong is what a new request must supply, not what the catalog knows.
      Source Finding: 'S4 constraint_register #3'
    - Rule Name: A_YEAR_IS_A_NUMBER
      Statement: A publication year is stated as a number wherever an operation asks for one. The catalog displays a year as a number and every request the library makes supplies one.
      Source Finding: 'S4 constraint_register #4'
    - Rule Name: NO_CORRECT_REQUEST_BECOMES_HARDER
      Statement: No requirement is added where any present caller would then fail. This is what the ruling against gaining requirements was for, and it is what defers the third correction rather than permitting it.
      Source Finding: 'S4 constraint_register #5'
    - Rule Name: AGREEMENT_IS_THE_ONLY_AUTHORITY
      Statement: Where no artifact declares the form of a detail, the correction rests on agreement among the statements of it and on the data. That is weaker than a declaration and is what exists.
      Source Finding: 'S4 constraint_register #6'
    - Rule Name: A_DEFERRAL_RECORDS_ITS_GROUND
      Statement: The third boundary is deferred with the reason written down, not dropped. A defect nobody found and a defect deferred for a stated reason are different states, and only one of them is governed.
      Source Finding: 'S4 design_decisions #5'
  governance_outcome:
    columns:
    - Capability
    - Owner Subdomain
    - Source Finding
    rows:
    - Capability: Admitting a request to register a further edition
      Owner Subdomain: catalog
      Source Finding: S4 gap_register GAP-1
    - Capability: Admitting a request to correct bibliographic information
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

## Gate 1 — Design Approval
