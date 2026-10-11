# Stage 6 — Governance Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 6 — Governance Intent
  CR: cr_05_catalog
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
    - Capability: Refuse anyone the library has not authorized
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Refuse anyone the library has not authorized
    - Capability: Refuse a registration the catalog finds incomplete
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Refuse a registration the catalog finds incomplete
    - Capability: Hold what a book, a work and a further edition must contain
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Hold what a book, a work and a further edition must contain
    - Capability: Check what the catalog records
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Check what the catalog records
    - Capability: Record the subject callers supply
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Record the subject callers supply
    - Capability: Register a copy as registered
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Register a copy as registered
    - Capability: Keep a corrected record's state, and check it against the book description
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Keep a corrected record's state, and check it against the book description
    - Capability: Admit a request without the rules the catalog holds
      Owner Subdomain: catalog
      Disposition (OWNED, SATISFIED, DEFERRED): OWNED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Admit a request without the rules the catalog holds
    - Capability: Establish who a caller is
      Owner Subdomain: outside the catalog
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Establish who a caller is
    - Capability: Records made under a request's own rules
      Owner Subdomain: nowhere; the business declines to rewrite them
      Disposition (OWNED, SATISFIED, DEFERRED): DEFERRED
      Existing Artifact: ''
      Source Finding: S5 scope_boundary Records made under a request's own rules
  storage_governance:
    columns:
    - Storage Need
    - Purpose
    - Subdomain
    - Source Finding
    rows:
    - Storage Need: A durable record of every book, with its bibliographic information and state
      Purpose: 'Unchanged by this change, and named because what may be written into it changes: a book only as described, with its subject, and a correction only with the state the record has'
      Subdomain: catalog
      Source Finding: S5 business_objects Book record
    - Storage Need: A durable record of every physical copy and its state
      Purpose: Unchanged by this change, and named because a copy is written only as registered
      Subdomain: catalog
      Source Finding: S5 business_objects Copy record
  cross_subdomain_deps:
    columns:
    - Dependency
    - Direction
    - Existing Artifact
    - Status (SATISFIED, GAP)
    - Source Finding
    rows:
    - Dependency: Refusing on a list of rules
      Direction: catalog -> platform
      Existing Artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Status (SATISFIED, GAP): SATISFIED
      Source Finding: S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    - Dependency: Checking a record's structure
      Direction: catalog -> platform
      Existing Artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Status (SATISFIED, GAP): SATISFIED
      Source Finding: S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    - Dependency: Assembling a record from fields
      Direction: catalog -> platform
      Existing Artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Status (SATISFIED, GAP): SATISFIED
      Source Finding: S4 dependency_graph capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
  pps_artifacts_requiring_action:
    columns:
    - FQDN
    - Current Status
    - Action (REPLACE, REVIEW, REUSE, EXTEND)
    - Source Finding
    rows:
    - FQDN: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Current Status: Present; takes its rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries Confirming staff
    - FQDN: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Current Status: Present; takes its descriptions from the request and refuses nothing its checks find
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries Checking a submission
    - FQDN: book_library_mgmt::CC_REGISTER_BOOK_V0
      Current Status: Present; takes its description from the request and ignores what its check finds
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries Recording a book
    - FQDN: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Current Status: Present; takes its description from the request and ignores what its check finds
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries Recording an edition
    - FQDN: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Current Status: Present; records the copy in the state the request gives
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries Recording a copy
    - FQDN: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Current Status: Present; writes the state the request gives and checks no description
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries Correcting a record
    - FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Current Status: Present; binds the rules from the request
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::IN_REGISTER_BOOK_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Current Status: Present; requires the rules the catalog will hold
      Action (REPLACE, REVIEW, REUSE, EXTEND): EXTEND
      Source Finding: S3 dependency_discoveries The ten gates
    - FQDN: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_RESOLVE_WORK_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
    - FQDN: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Current Status: Present and reused unchanged
      Action (REPLACE, REVIEW, REUSE, EXTEND): REUSE
      Source Finding: S3 dependency_discoveries The ten acts
  boundary_rules:
    columns:
    - Rule Name
    - Statement
    - Source Finding
    rows:
    - Rule Name: A_RULE_IS_HELD_WHERE_IT_IS_APPLIED
      Statement: Each of the catalog's rules is a fixed value of the step that applies it. No act and no request hands the catalog a rule.
      Source Finding: 'S4 design_decisions #1'
    - Rule Name: A_CHECK_THAT_FINDS_REFUSES
      Statement: A check's report is consumed by a rule that refuses when it found anything. The platform check reports; the catalog decides.
      Source Finding: 'S4 design_decisions #2'
    - Rule Name: WHAT_IS_CHECKED_IS_WHAT_IS_RECORDED
      Statement: Each registration checks the record it writes, never a copy supplied beside it.
      Source Finding: 'S4 design_decisions #3'
    - Rule Name: THE_SUBJECT_IS_THE_ONE_SUPPLIED
      Statement: The register act records the subject where callers send it.
      Source Finding: 'S4 design_decisions #4'
    - Rule Name: STATE_IS_THE_CATALOGS
      Statement: A copy is registered as registered, and a correction keeps the state the record has.
      Source Finding: 'S4 design_decisions #5'
    - Rule Name: A_GATE_REQUIRES_WHAT_IS_READ
      Statement: A gate requires what its act reads, and nothing the catalog holds or no act reads.
      Source Finding: 'S4 design_decisions #6'
    - Rule Name: THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN
      Statement: Records made before this change are left as they are.
      Source Finding: 'S4 design_decisions #7'
  governance_outcome:
    columns:
    - Capability
    - Owner Subdomain
    - Source Finding
    rows:
    - Capability: Refuse anyone the library has not authorized
      Owner Subdomain: catalog
      Source Finding: S6 ownership Refuse anyone the library has not authorized
    - Capability: Refuse a registration the catalog finds incomplete
      Owner Subdomain: catalog
      Source Finding: S6 ownership Refuse a registration the catalog finds incomplete
    - Capability: Hold what a book, a work and a further edition must contain
      Owner Subdomain: catalog
      Source Finding: S6 ownership Hold what a book, a work and a further edition must contain
    - Capability: Check what the catalog records
      Owner Subdomain: catalog
      Source Finding: S6 ownership Check what the catalog records
    - Capability: Record the subject callers supply
      Owner Subdomain: catalog
      Source Finding: S6 ownership Record the subject callers supply
    - Capability: Register a copy as registered
      Owner Subdomain: catalog
      Source Finding: S6 ownership Register a copy as registered
    - Capability: Keep a corrected record's state, and check it against the book description
      Owner Subdomain: catalog
      Source Finding: S6 ownership Keep a corrected record's state, and check it against the book description
    - Capability: Admit a request without the rules the catalog holds
      Owner Subdomain: catalog
      Source Finding: S6 ownership Admit a request without the rules the catalog holds
```

Placement of rules. Nothing moves and nothing is added: every step that changes already belongs to
the catalog. What is placed here is each of the catalog's rules, with the step that applies it, so
that the catalog holds them however it is reached.

---

## 1. Ownership

---

## 2. Storage Governance

---

## 3. Cross-Subdomain Dependencies

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
