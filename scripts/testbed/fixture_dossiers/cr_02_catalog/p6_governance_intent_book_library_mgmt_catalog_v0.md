# Stage 6 — Governance Intent: book_library_mgmt / catalog

**Stage:** 6 — Governance Intent
**CR:** cr_02_catalog
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Form the identifying key of a work from its title and author | catalog | OWNED |  | S5 scope_boundary Form the identifying key of a work from its title and author |
| Claim a work's identity so that two registrations of one work do not produce two works | catalog | OWNED |  | S5 scope_boundary Claim a work's identity so that two registrations of one work do not produce two works |
| Resolve the work an edition belongs to | catalog | OWNED |  | S5 scope_boundary Resolve the work an edition belongs to |
| Group selected records by an attribute they share | catalog | OWNED |  | S5 scope_boundary Group selected records by an attribute they share |
| Declare the stores the catalog owns | catalog | OWNED |  | S5 scope_boundary Declare the stores the catalog owns |
| Bind the catalog's workflows to the stores they use | catalog | OWNED |  | S5 scope_boundary Bind the catalog's workflows to the stores they use |
| Register an edition of a work the catalog does not yet hold | catalog | OWNED |  | S5 scope_boundary Register an edition of a work the catalog does not yet hold |
| Validate that a registration carries what a work and an edition require | catalog | OWNED |  | S5 scope_boundary Validate that a registration carries what a work and an edition require |
| Register an additional edition of an existing work | catalog | OWNED |  | S5 scope_boundary Register an additional edition of an existing work |
| Search the catalog and answer at the level of the work | catalog | OWNED |  | S5 scope_boundary Search the catalog and answer at the level of the work |
| Retrieve an edition's complete details with a summary of its work | catalog | OWNED |  | S5 scope_boundary Retrieve an edition's complete details with a summary of its work |
| Admit a request to register an additional edition of an existing work | catalog | OWNED |  | S5 scope_boundary Admit a request to register an additional edition of an existing work |
| Recognise the moment a work enters the catalog | catalog | OWNED |  | S5 scope_boundary Recognise the moment a work enters the catalog |
| Hold a record durably and update it in place | catalog | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S4 capability_graph Hold a work record durably and update it in place |
| Claim an identity atomically so that a second claim cannot succeed unnoticed | catalog | SATISFIED | capability_side_effects::CS_REGISTRY_V0 | S4 capability_graph Enforce that one work exists per title and author |
| Confirm the staff member performing an operation is authorized | catalog | SATISFIED | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | S4 capability_graph Confirm the staff member performing an operation is authorized |
| Record every performed operation in the catalog's audit trail | catalog | SATISFIED | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | S4 capability_graph Record every performed operation in the catalog's audit trail |
| Register a physical copy against exactly one edition | catalog | SATISFIED | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | S4 capability_graph Register a physical copy against exactly one edition |
| Retire and reinstate an edition independently of the work's other editions | catalog | SATISFIED | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | S4 capability_graph Retire and reinstate an edition independently of the work's other editions |
| Update an edition's bibliographic information | catalog | SATISFIED | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | S4 capability_graph Update an edition's bibliographic information |
| Deciding which staff are authorized | staff | DEFERRED |  | S5 scope_boundary Deciding which staff are authorized |
| Multiple identifiers for one publication | catalog | DEFERRED |  | S5 scope_boundary Multiple identifiers for one publication |
| A governed subject taxonomy | catalog | DEFERRED |  | S5 scope_boundary A governed subject taxonomy |
| Digital resources associated with catalog records | catalog | DEFERRED |  | S5 scope_boundary Digital resources associated with catalog records |
| Images associated with catalog records | catalog | DEFERRED |  | S5 scope_boundary Images associated with catalog records |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of every work the library has catalogued | The library requires one authoritative description per work, correctable in place, so that several editions can be said to be editions of one thing | catalog | S5 business_objects Work record |
| An atomic claim on each work's identity | Two registrations describing the same work must resolve to one work, and only a claim taken at the moment of registration can guarantee it | catalog | S5 business_objects Work identity registry |
| A durable record of every edition the library holds | Unchanged from the previous change: one authoritative description per edition, correctable in place and carrying its own registered-or-retired state | catalog | S5 business_objects Edition record |
| A durable record of every physical copy the library owns | Unchanged from the previous change: one authoritative record per copy, each naming the one edition it belongs to | catalog | S5 business_objects Physical copy record |
| An unamendable trail of every operation performed | Unchanged from the previous change: an operation that has been performed cannot be un-performed, so its record is never amended | catalog | S5 business_objects Catalog audit trail |
| An atomic claim on each edition's identity | Unchanged from the previous change: no two editions share a title, author and publication year | catalog | S5 business_objects Edition identity registry |
| An atomic claim on each copy's barcode | Unchanged from the previous change: no two copies the library owns share a barcode | catalog | S5 business_objects Copy barcode registry |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Read whether a staff member is authorized to perform catalog operations | catalog → staff |  | GAP | S4 dependency_graph catalog → staff |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE) | Source Finding |
|------|----------------|----------------------------------|----------------|
| book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | Declares the five stores the catalog owns; every consumer is inside the subdomain | EXTEND | S4 gap_register GAP-05 |
| book_library_mgmt::RB_CATALOG_BINDINGS_V0 | Binds the catalog's workflows to the stores they use; referenced by nine artifacts, all within the subdomain | EXTEND | S4 gap_register GAP-06 |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | Registers a record together with its first copy, claiming two identities before any write | EXTEND | S4 gap_register GAP-07 |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | Confirms a registration carries what a record requires, before any claim | EXTEND | S4 gap_register GAP-08 |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | Selects registered records by subject or title and excludes retired ones | EXTEND | S4 gap_register GAP-10 |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Assembles one record with the physical copies of it | EXTEND | S4 gap_register GAP-11 |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | Forms the three-attribute key every catalog operation reaches; 23 artifacts depend on it | REVIEW | S3 authoring_decisions Form the identifying key of a work from its title and author |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | Claims the edition's identity; read as the precedent the work claim follows | REVIEW | S3 authoring_decisions Claim a work's identity so that two registrations of one work do not produce two works |
| capability_side_effects::CS_MUTABLE_JSON_V0 | Declared and in use by ai_governance, book_library_mgmt and workload | REUSE | S3 impact_analysis capability_side_effects::CS_MUTABLE_JSON_V0 |
| capability_side_effects::CS_REGISTRY_V0 | Declared and in use by ai_governance and book_library_mgmt | REUSE | S3 impact_analysis capability_side_effects::CS_REGISTRY_V0 |
| capability_transforms::CT_PURE_FILTER_RECORDS_V0 | Selects records by stated criteria; examined and not extended | REVIEW | S3 impact_analysis capability_transforms::CT_PURE_FILTER_RECORDS_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| CATALOG_OWNS_ITS_STORES | Every store the catalog reads or writes is declared by the catalog, including the two this change adds, and no catalog operation writes into a store another subdomain owns. | S3 analysis_findings #7 |
| AUTHORIZATION_IS_READ_NEVER_GRANTED | The catalog confirms a staff member is authorized on every operation, including the ones this change adds, and grants authorization nowhere. | S4 constraint_register #1 |
| EVERY_CLAIM_PRECEDES_EVERY_WRITE | A registration claims every identity it needs — the work, the edition and the barcode — before it writes any record, so a refused registration leaves nothing behind. | S4 constraint_register #12 |
| EDITION_IDENTITY_IS_NOT_WIDENED | The key that identifies an existing record is not changed to serve the work; the work's key is formed independently and the two cannot alter each other. | S4 constraint_register #13 |
| NO_CAPABILITY_IS_WITHDRAWN | Every operation staff had before this change remains reachable and every existing record remains findable; search and retrieval are extended in the shape of their answers and in nothing else. | S4 constraint_register #1 |
| A_WORK_IS_NEVER_RETIRED | Retirement is declared on the edition and on the copy; a work whose editions are all retired is simply that, and no cascade reaches it. | S4 constraint_register #11 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Form the identifying key of a work from its title and author | catalog | S6 ownership Form the identifying key of a work from its title and author |
| Claim a work's identity so that two registrations of one work do not produce two works | catalog | S6 ownership Claim a work's identity so that two registrations of one work do not produce two works |
| Resolve the work an edition belongs to | catalog | S6 ownership Resolve the work an edition belongs to |
| Group selected records by an attribute they share | catalog | S6 ownership Group selected records by an attribute they share |
| Declare the stores the catalog owns | catalog | S6 ownership Declare the stores the catalog owns |
| Bind the catalog's workflows to the stores they use | catalog | S6 ownership Bind the catalog's workflows to the stores they use |
| Register an edition of a work the catalog does not yet hold | catalog | S6 ownership Register an edition of a work the catalog does not yet hold |
| Validate that a registration carries what a work and an edition require | catalog | S6 ownership Validate that a registration carries what a work and an edition require |
| Register an additional edition of an existing work | catalog | S6 ownership Register an additional edition of an existing work |
| Search the catalog and answer at the level of the work | catalog | S6 ownership Search the catalog and answer at the level of the work |
| Retrieve an edition's complete details with a summary of its work | catalog | S6 ownership Retrieve an edition's complete details with a summary of its work |
| Admit a request to register an additional edition of an existing work | catalog | S6 ownership Admit a request to register an additional edition of an existing work |
| Recognise the moment a work enters the catalog | catalog | S6 ownership Recognise the moment a work enters the catalog |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
