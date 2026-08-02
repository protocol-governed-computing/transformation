# Governance Intent — book_library_mgmt / catalog

**Stage:** 6 — Governance Intent
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

> P6 answers WHERE. Capabilities are placed in subdomains and named in business language; the
> provisional codes Stage 5 assigned are deliberately absent, and binding identities are Stage 7's.
> Existing artifacts are cited by exact FQDN, because citing what exists is observation.

---

## 1. Ownership

<!-- register:ownership business_language -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Register a book | catalog | OWNED | | S5 scope_boundary Register a book |
| Register a physical copy against one work | catalog | OWNED | | S5 scope_boundary Register a physical copy |
| Update bibliographic information | catalog | OWNED | | S5 scope_boundary Update bibliographic information |
| Retire an obsolete record | catalog | OWNED | | S5 scope_boundary Retire an obsolete record |
| Search the catalog | catalog | OWNED | | S5 scope_boundary Search the catalog |
| Retrieve complete book details | catalog | OWNED | | S5 scope_boundary Retrieve complete book details |
| Record that a catalog operation was performed | catalog | OWNED | | S5 scope_boundary Record that a catalog operation |
| Confirm the staff member is authorized | catalog | OWNED | | S5 scope_boundary Confirm the staff member is authorized |
| Hold a record that can be updated in place | capability_side_effects | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S5 cross_subdomain_refs CS_MUTABLE_JSON |
| Append a durable account of a performed action | capability_side_effects | SATISFIED | capability_side_effects::CS_APPENDONLY_JSONL_V0 | S5 cross_subdomain_refs CS_APPENDONLY_JSONL |
| Grant staff authorization | patron | DEFERRED | | S5 scope_boundary Grant staff authorization |

## 2. Storage Governance

<!-- register:storage_governance business_language -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| Bibliographic work records | The authoritative description of each cataloged work | catalog | S5 business_objects Bibliographic work record |
| Physical copy records | The authoritative record of each copy the library owns | catalog | S5 business_objects Physical copy record |
| Catalog operation journal | The durable account of every operation performed | catalog | S5 business_objects Catalog operation record |

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Hold a record that can be updated in place | catalog -> capability_side_effects | capability_side_effects::CS_MUTABLE_JSON_V0 | SATISFIED | S5 cross_subdomain_refs CS_MUTABLE_JSON |
| Append a durable account of a performed action | catalog -> capability_side_effects | capability_side_effects::CS_APPENDONLY_JSONL_V0 | SATISFIED | S5 cross_subdomain_refs CS_APPENDONLY_JSONL |
| Decide which staff members are authorized | catalog -> patron | | GAP | S4 gap_register GAP-10 |

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action -->
| FQDN | Current Status | Action | Source Finding |
|------|----------------|--------|----------------|
| NONE IDENTIFIED | | | |

## 5. Boundary Rules

<!-- register:boundary_rules business_language -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| Store ownership is exclusive | The catalog's records are written only by capabilities the catalog owns; no peer writes them. | S4 constraint_register #5 |
| Authorization is read, never granted | The catalog confirms a staff member is authorized; deciding who is authorized belongs to patron. | S4 gap_register GAP-10 |
| Copies name one work | A copy record names exactly one work record, and the catalog owns both sides of that relationship. | S5 invariants Each physical copy belongs to exactly one bibliographic work |
| Retirement does not delete | A retired record remains for audit and is withheld from current results rather than removed. | S5 invariants A retired record is never offered as current |

## 6. Governance Outcome

<!-- register:governance_outcome business_language -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Register a book | catalog | S6 ownership Register a book |
| Register a physical copy against one work | catalog | S6 ownership Register a physical copy against one work |
| Update bibliographic information | catalog | S6 ownership Update bibliographic information |
| Retire an obsolete record | catalog | S6 ownership Retire an obsolete record |
| Search the catalog | catalog | S6 ownership Search the catalog |
| Retrieve complete book details | catalog | S6 ownership Retrieve complete book details |
| Record that a catalog operation was performed | catalog | S6 ownership Record that a catalog operation was performed |
| Confirm the staff member is authorized | catalog | S6 ownership Confirm the staff member is authorized |
