# Business Intent — book_library_mgmt / catalog (deliberately inadmissible fixture)

**Stage:** 5 — Business Intent
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

> P5 states the irreducible WHAT. It is the first phase to name what this change will build, using
> provisional codes — what to build, never where it will live. Placement is Stage 6's decision and
> binding identity is Stage 7's.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The catalog governs the library's authoritative description of what it holds: each bibliographic
work it has cataloged and each physical copy it owns. It exists because those records are kept by
hand today, which produces inconsistent descriptions, duplicate entries and difficulty locating
materials. It owns the description of the collection and the operations that maintain it; it does
not govern who borrows the collection, what is ordered, or what is owed.

## 2. Scope Boundary

<!-- register:scope_boundary business_language -->
| Capability | Status | Notes | Source Finding |
|------------|--------|-------|----------------|
| Register a book | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-01 |
| Register a physical copy against one work | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-02 |
| Update bibliographic information | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-03 |
| Retire an obsolete record | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-04 |
| Search the catalog | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-05 |
| Retrieve complete book details | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-06 |
| Record that a catalog operation was performed | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-07 |
| Confirm the staff member is authorized | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-08 |
| Declare the stores this subdomain owns | IN_SCOPE | Authored this change request | S4 authoring_scope GAP-09 |
| Grant staff authorization | DEFERRED | Owned by patron, which is not in this release | S4 gap_register GAP-10 |
| Borrowing, reservations, fines, acquisitions, inventory reconciliation | DEFERRED | Declared out of scope by the business author | S1 out_of_scope #1 |

## 3. Business Objects

<!-- register:business_objects business_language -->
| Store Name | Record Model | Business Rationale | Source Finding |
|------------|--------------|--------------------|----------------|
| Bibliographic work record | MUTABLE_STATE | The library requires a single authoritative record for each work | S4 bm_entities Bibliographic work |
| Physical copy record | MUTABLE_STATE | The library requires a single authoritative record for each copy it owns | S4 bm_entities Physical copy |
| Catalog operation record | APPEND_ONLY_JOURNAL | Appended at $.payload.operation for every completed call | S4 bm_entities Operation record |

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Bibliographic work record | Work identifier | UNRESOLVED | Two registrations describing the same published title are the same work and must not produce two records | None | S2 entity_attributes Bibliographic Work identity |
| Physical copy record | Copy identifier | Assigned by the library when the copy is registered | Each owned copy is distinct even when several copies describe one work | Names exactly one bibliographic work record | S2 entity_attributes Physical Copy identity |
| Catalog operation record | Operation sequence | Assigned on append | Each performed operation appends exactly one record | Names the staff member who performed it | S4 bm_entities Operation record |

## 5. Business Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| Each physical copy belongs to exactly one bibliographic work | A copy the library owns describes one published title; a copy belonging to two would make the collection uncountable | S4 constraint_register #1 |
| Each work and each copy has exactly one authoritative record | The library requires one place to look, which is the whole point of the change | S4 constraint_register #2 |
| Every business operation performed is traceable and auditable | The library must be able to account afterwards for what staff did to the catalog | S4 constraint_register #3 |
| Only authorized staff perform catalog operations | The catalog is the library's authoritative description and may not be altered by anyone | S4 constraint_register #4 |
| A retired record is never offered as current | A record retired for being obsolete would mislead if it kept appearing in results | S4 design_decisions #5 |

## 6. Business Actions

<!-- register:actions business_language -->
| Action | Object | Trigger | Status | Source Finding |
|--------|--------|---------|--------|----------------|
| Register | Bibliographic work record | Authorized staff register a new book | IN_SCOPE | S4 capability_graph Register a book |
| Register | Physical copy record | Authorized staff register a copy | IN_SCOPE | S4 capability_graph Register a physical copy against one work |
| Update | Bibliographic work record | Authorized staff update a registered work | IN_SCOPE | S4 capability_graph Update bibliographic information |
| Retire | Bibliographic work record | Authorized staff retire an obsolete record | IN_SCOPE | S4 capability_graph Retire an obsolete record |
| Search | Bibliographic work record | Authorized staff search for materials | IN_SCOPE | S4 capability_graph Search the catalog |
| Retrieve | Bibliographic work record | Authorized staff request complete details | IN_SCOPE | S4 capability_graph Retrieve complete book details |
| Append | Catalog operation record | Any catalog operation completes | IN_SCOPE | S4 capability_graph Record that a catalog operation was performed |

## 7. Provisional Artifact Codes

<!-- register:provisional_codes business_language=summary -->
| Provisional Code | Family (AC, IN, WF, CC) | Summary | Source Finding |
|------------------|--------------------------|---------|----------------|
| AC_LIBRARY_STAFF_V0 | AC | The authorized staff member who performs a catalog operation | S4 actors Authorized staff member |
| IN_REGISTER_BOOK_V0 | IN | A request to register a new book | S4 capability_graph Register a book |
| IN_REGISTER_PHYSICAL_COPY_V0 | IN | A request to register a copy against a work | S4 capability_graph Register a physical copy against one work |
| IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | IN | A request to update a registered work | S4 capability_graph Update bibliographic information |
| IN_RETIRE_CATALOG_RECORD_V0 | IN | A request to retire an obsolete record | S4 capability_graph Retire an obsolete record |
| IN_SEARCH_CATALOG_V0 | IN | A request to locate materials | S4 capability_graph Search the catalog |
| IN_RETRIEVE_BOOK_DETAILS_V0 | IN | A request for the complete details of a book | S4 capability_graph Retrieve complete book details |
| WF_REGISTER_BOOK_V0 | WF | Registering a book, end to end | S4 capability_graph Register a book |
| WF_REGISTER_PHYSICAL_COPY_V0 | WF | Registering a copy against exactly one work | S4 capability_graph Register a physical copy against one work |
| WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | WF | Updating the description of a registered work | S4 capability_graph Update bibliographic information |
| WF_RETIRE_CATALOG_RECORD_V0 | WF | Retiring a record so it is no longer current | S4 capability_graph Retire an obsolete record |
| WF_SEARCH_CATALOG_V0 | CC | Searching the catalog and recording that it happened | S4 capability_graph Search the catalog |
| WF_RETRIEVE_BOOK_DETAILS_V0 | WF | Assembling a work with the copies belonging to it | S4 capability_graph Retrieve complete book details |
| CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | Confirm the staff member may perform catalog operations | S4 capability_graph Confirm the staff member is authorized |
| catalog::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | CC | Record a work as the catalog's authoritative description of it | S4 capability_graph Register a book |
| CC_REGISTER_PHYSICAL_COPY_V0 | CC | Record a copy against exactly one work | S4 capability_graph Register a physical copy against one work |
| CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | CC | Replace the descriptive content of a work's record | S4 capability_graph Update bibliographic information |
| CC_RETIRE_CATALOG_RECORD_V0 | CC | Mark a record retired so it is no longer offered as current | S4 capability_graph Retire an obsolete record |
| CC_SEARCH_CATALOG_V0 | CC | Select the current records matching the staff member's terms | S4 capability_graph Search the catalog |
| CC_ASSEMBLE_BOOK_DETAILS_V0 | CC | Assemble a work's record with the copies belonging to it | S4 capability_graph Retrieve complete book details |
| CC_APPEND_CATALOG_OPERATION_V0 | CC | Append a durable account of a performed catalog operation | S4 capability_graph Record that a catalog operation was performed |

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | capability_side_effects | Holds a catalog record that can be updated in place | S4 dependency_graph catalog to CS_MUTABLE_JSON |
| workload::CS_APPENDONLY_JSONL_V0 | capability_side_effects | Appends a durable account of a performed operation | S4 dependency_graph catalog to CS_APPENDONLY_JSONL |
