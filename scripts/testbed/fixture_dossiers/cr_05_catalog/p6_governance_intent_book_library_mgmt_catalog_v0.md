# Stage 6 — Governance Intent: book_library_mgmt / catalog

**Stage:** 6 — Governance Intent

**CR:** cr_05_catalog

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. Nothing moves and nothing is added: every step that changes already belongs to
the catalog. What is placed here is each of the catalog's rules, with the step that applies it, so
that the catalog holds them however it is reached.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Refuse anyone the library has not authorized | catalog | OWNED |  | S5 scope_boundary Refuse anyone the library has not authorized |
| Refuse a registration the catalog finds incomplete | catalog | OWNED |  | S5 scope_boundary Refuse a registration the catalog finds incomplete |
| Hold what a book, a work and a further edition must contain | catalog | OWNED |  | S5 scope_boundary Hold what a book, a work and a further edition must contain |
| Check what the catalog records | catalog | OWNED |  | S5 scope_boundary Check what the catalog records |
| Record the subject callers supply | catalog | OWNED |  | S5 scope_boundary Record the subject callers supply |
| Register a copy as registered | catalog | OWNED |  | S5 scope_boundary Register a copy as registered |
| Keep a corrected record's state, and check it against the book description | catalog | OWNED |  | S5 scope_boundary Keep a corrected record's state, and check it against the book description |
| Admit a request without the rules the catalog holds | catalog | OWNED |  | S5 scope_boundary Admit a request without the rules the catalog holds |
| Establish who a caller is | outside the catalog | DEFERRED |  | S5 scope_boundary Establish who a caller is |
| Records made under a request's own rules | nowhere; the business declines to rewrite them | DEFERRED |  | S5 scope_boundary Records made under a request's own rules |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of every book, with its bibliographic information and state | Unchanged by this change, and named because what may be written into it changes: a book only as described, with its subject, and a correction only with the state the record has | catalog | S5 business_objects Book record |
| A durable record of every physical copy and its state | Unchanged by this change, and named because a copy is written only as registered | catalog | S5 business_objects Copy record |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Refusing on a list of rules | catalog -> platform | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| Checking a record's structure | catalog -> platform | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| Assembling a record from fields | catalog -> platform | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Present; takes its rules from the request | EXTEND | S3 dependency_discoveries Confirming staff |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | Present; takes its descriptions from the request and refuses nothing its checks find | EXTEND | S3 dependency_discoveries Checking a submission |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | Present; takes its description from the request and ignores what its check finds | EXTEND | S3 dependency_discoveries Recording a book |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | Present; takes its description from the request and ignores what its check finds | EXTEND | S3 dependency_discoveries Recording an edition |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | Present; records the copy in the state the request gives | EXTEND | S3 dependency_discoveries Recording a copy |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Present; writes the state the request gives and checks no description | EXTEND | S3 dependency_discoveries Correcting a record |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | Present; binds the rules from the request | EXTEND | S3 dependency_discoveries The ten acts |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | Present; requires the rules the catalog will hold | EXTEND | S3 dependency_discoveries The ten gates |
| book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_RESOLVE_WORK_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The ten acts |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_RULE_IS_HELD_WHERE_IT_IS_APPLIED | Each of the catalog's rules is a fixed value of the step that applies it. No act and no request hands the catalog a rule. | S4 design_decisions #1 |
| A_CHECK_THAT_FINDS_REFUSES | A check's report is consumed by a rule that refuses when it found anything. The platform check reports; the catalog decides. | S4 design_decisions #2 |
| WHAT_IS_CHECKED_IS_WHAT_IS_RECORDED | Each registration checks the record it writes, never a copy supplied beside it. | S4 design_decisions #3 |
| THE_SUBJECT_IS_THE_ONE_SUPPLIED | The register act records the subject where callers send it. | S4 design_decisions #4 |
| STATE_IS_THE_CATALOGS | A copy is registered as registered, and a correction keeps the state the record has. | S4 design_decisions #5 |
| A_GATE_REQUIRES_WHAT_IS_READ | A gate requires what its act reads, and nothing the catalog holds or no act reads. | S4 design_decisions #6 |
| THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN | Records made before this change are left as they are. | S4 design_decisions #7 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Refuse anyone the library has not authorized | catalog | S6 ownership Refuse anyone the library has not authorized |
| Refuse a registration the catalog finds incomplete | catalog | S6 ownership Refuse a registration the catalog finds incomplete |
| Hold what a book, a work and a further edition must contain | catalog | S6 ownership Hold what a book, a work and a further edition must contain |
| Check what the catalog records | catalog | S6 ownership Check what the catalog records |
| Record the subject callers supply | catalog | S6 ownership Record the subject callers supply |
| Register a copy as registered | catalog | S6 ownership Register a copy as registered |
| Keep a corrected record's state, and check it against the book description | catalog | S6 ownership Keep a corrected record's state, and check it against the book description |
| Admit a request without the rules the catalog holds | catalog | S6 ownership Admit a request without the rules the catalog holds |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
