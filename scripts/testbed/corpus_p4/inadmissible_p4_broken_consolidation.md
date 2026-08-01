# Business Model — book_library_mgmt / catalog (deliberately inadmissible fixture)

**Stage:** 4 — Business Model
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

> P4 consolidates. P2 discovered and P3 decided; this is the canonical artifact every later phase
> projects from. Nothing is designed here that P3 did not already commit to, and every row traces
> to the finding that produced it.

---

## 1. Discovery Summary

### Actors

<!-- register:actors business_language -->
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Authorized staff member | Performs every catalog operation | Operator | S1 authority_boundaries The decision that a record is obsolete |
| Library | Owns the physical copies described by the catalog | Owner | S1 known_facts #4 |

### Entities

<!-- register:bm_entities business_language -->
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Bibliographic work | The subject of a single authoritative record describing a published title. | One durable record per work, addressable by identity and updatable in place. | S2 entities Bibliographic Work |
| Physical copy | An individual copy owned by the library, belonging to exactly one bibliographic work. | One durable record per copy, each naming the single work it belongs to. | S2 entities Physical Copy |
| Catalog record | The single authoritative record for one work or one copy. | Durable addressable state, updatable in place and markable retired. | S2 entities Catalog Record |
| Operation record | A durable account of a catalog operation that was performed. | Appended to a record that is never rewritten. | S2 entities Business Operation |

### Resources

<!-- register:resources business_language -->
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| Catalog record store | Holds the authoritative record for every work and copy. | S3 authoring_decisions Declare the stores this subdomain owns |
| Operation audit record | Holds the durable account of every operation performed. | S3 authoring_decisions Record that a catalog operation was performed |

### Events

<!-- register:events business_language -->
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| Book registered | Authorized staff register a new book | A work enters the catalog and acquires its authoritative record | S1 business_events Book Registered |
| Physical copy registered | Authorized staff register a copy | A copy is recorded against exactly one work | S1 business_events Physical Copy Registered |
| Bibliographic information updated | Authorized staff update a registered work | The authoritative description of a work changes | S1 business_events Bibliographic Information Updated |
| Record retired | Authorized staff retire an obsolete record | The record is no longer offered as current | S1 business_events Record Retired |
| Catalog searched | Authorized staff search for materials | A business operation occurred that must be auditable | S1 business_events Catalog Searched |
| Book details retrieved | Authorized staff retrieve complete details | A business operation occurred that must be auditable | S1 business_events Book Details Retrieved |

### Relationships

<!-- register:relationships business_language -->
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Physical copy | belongs to | Bibliographic work | Enforce that a copy names exactly one work | S1 business_invariants #1 |
| Authorized staff member | performs | Catalog operation | Confirm the staff member is authorized | S1 business_invariants #5 |
| Catalog operation | produces | Operation record | Record that a catalog operation was performed | S1 business_invariants #4 |
| Bibliographic work | is described by | Catalog record | Hold a catalog record that can be updated in place | S2 entities Catalog Record |

## 2. Capability Graph

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Hold a catalog record that can be updated in place | S3 authoring_decisions Hold a catalog record | SATISFIED | | Reuses keyed mutable state; the mechanism enforces no business rule. |
| Append a durable record of a performed operation | S3 authoring_decisions Append a durable record | SATISFIED | | Reuses the append-only mechanism; the shape is authored here. |
| Register a book | S3 authoring_decisions Register a book | CRITICAL | GAP-99 | |
| Register a physical copy against one work | S3 authoring_decisions Register a physical copy | CRITICAL | GAP-02 | |
| Update bibliographic information | S3 authoring_decisions Update bibliographic information | CRITICAL | GAP-03 | |
| Retire an obsolete record | S3 authoring_decisions Retire an obsolete record | CRITICAL | GAP-04 | |
| Search the catalog | S3 authoring_decisions Search the catalog | CRITICAL | GAP-05 | |
| Retrieve complete book details | S3 authoring_decisions Retrieve complete book details | CRITICAL | GAP-06 | |
| Record that a catalog operation was performed | S3 authoring_decisions Record that a catalog operation | CRITICAL | GAP-07 | |
| Confirm the staff member is authorized | S3 authoring_decisions Confirm the staff member is authorized | CRITICAL | GAP-08 | |
| Declare the stores this subdomain owns | S3 authoring_decisions Declare the stores | CRITICAL | GAP-09 | |

## 3. Dependency Graph

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| catalog | capability_side_effects::CS_MUTABLE_JSON_V0 | capability call | SATISFIED | S3 authoring_decisions Hold a catalog record |
| catalog | workload::CS_APPENDONLY_JSONL_V0 | capability call | SATISFIED | S3 authoring_decisions Append a durable record |
| catalog | patron | data read | GAP | S3 dependency_discoveries Authority granting staff authorization |

## 4. Constraint Register

<!-- register:constraint_register business_language -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Each physical copy belongs to exactly one bibliographic work. | S1 business_invariants #1 | invariant |
| 2 | Each work and each copy has exactly one authoritative record. | S1 business_invariants #2 | invariant |
| 3 | Every business operation performed is traceable and auditable. | S1 business_invariants #4 | invariant |
| 4 | Only authorized staff perform catalog operations. | S1 business_invariants #5 | invariant |
| 5 | A subdomain owns its stores exclusively and declares them itself. | S3 verification_results The audit mechanism could be reused as-is | governance rule |
| 6 | Capabilities deferred to future change requests must not be designed into this solution. | S1 constraints #1 | domain knowledge |

## 5. Gap Register

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|------------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Register a book | Register a book | catalog | Author this CR |
| GAP-02 | S3 authoring_decisions Register a physical copy | Register a physical copy against one work | catalog | Author this CR |
| GAP-03 | S3 authoring_decisions Update bibliographic information | Update bibliographic information | catalog | Author this CR |
| GAP-04 | S3 authoring_decisions Retire an obsolete record | Retire an obsolete record |  | Author this CR |
| GAP-05 | S3 authoring_decisions Search the catalog | Search the catalog | catalog | Author this CR |
| GAP-06 | S3 authoring_decisions Retrieve complete book details | Retrieve complete book details | catalog | Author this CR |
| GAP-07 | S3 authoring_decisions Record that a catalog operation | Record that a catalog operation was performed | catalog | Author this CR |
| GAP-08 | S3 authoring_decisions Confirm the staff member is authorized | Confirm the staff member is authorized | catalog | Author this CR |
| GAP-09 | S3 authoring_decisions Declare the stores | Declare the stores this subdomain owns | catalog | Author this CR |
| GAP-10 | S3 dependency_discoveries Authority granting staff authorization | Grant staff authorization | patron | Deferred to a future change request |

## 6. Design Decisions

<!-- register:design_decisions business_language -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The catalog is a new subdomain, a peer of the others, rather than an extension of anything existing. | S3 placement_decision | Nothing existing describes the library's holdings, so there is no boundary to extend. | The catalog owns its records exclusively. |
| 2 | The catalog declares its own stores rather than writing to another subdomain's. | S3 verification_results The audit mechanism could be reused as-is | A subdomain owns its stores exclusively; the existing audit contract binds a store its own subdomain declares. | The audit shape is authored here, not reused. |
| 3 | The record of a performed operation is appended, never rewritten. | S3 architectural_observations Durable state and the durable record of an action are separate mechanisms | Auditability requires that what happened cannot be edited afterwards. | Operation records are immutable once written. |
| 4 | Authorization is confirmed as a step of every operation, including the two that only read. | S3 analysis_findings S2-DC-2 | Every business operation must be traceable, and the business author confirmed reads are operations. | Search and retrieval carry the same preconditions as writes. |
| 5 | Retirement applies to the bibliographic work record; a copy is withdrawn with the work it belongs to. | S3 analysis_findings S2-OQ-1 | The business author settled it; the composition holds nothing that could. | The lifecycle has one retirable object. |

## 7. Authoring Scope

<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Register a book | GAP-01 |
| Register a physical copy against one work | GAP-02 |
| Update bibliographic information | GAP-03 |
| Retire an obsolete record | GAP-04 |
| Search the catalog | GAP-77 |
| Retrieve complete book details | GAP-06 |
| Record that a catalog operation was performed | GAP-07 |
| Confirm the staff member is authorized | GAP-08 |
| Declare the stores this subdomain owns | GAP-09 |
