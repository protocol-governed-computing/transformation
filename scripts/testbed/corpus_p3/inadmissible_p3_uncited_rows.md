# Analysis Loop — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
header:
  Stage: 3 — Analysis Loop
  CR: cr_01_catalog
  Status: DRAFT
  Feeds: Stage 4 — Business Model
registers:
  analysis_findings:
    columns:
    - Question Id
    - Finding
    - Impact
    - Evidence Status (OBSERVED, INFERRED, OPEN)
    - Confidence (HIGH, MEDIUM, LOW)
    - Resolution Status (CLOSED, OPEN)
    - Evidence
    rows:
    - Question Id: 'S2 discovery_concerns #1'
      Finding: The only composed audit step belongs to another subdomain and appends into that subdomain's store, so reusing it would breach a subdomain's exclusive ownership of its stores. The catalog owns its audit composition and its own append-only store, and reuses the append-only mechanism beneath them.
      Impact: Two artifacts authored rather than one reused; library traceability stays independent of agent-governance semantics.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: ai_governance::CC_APPEND_AUDIT_EVENT_V0 binds capability_side_effects::CS_APPENDONLY_JSONL_V0 and writes through ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0; si.artifact.refs reports 7 direct references, all ai_governance. Decided by the business owner.
    - Question Id: 'S2 discovery_concerns #2'
      Finding: The available uniqueness mechanism keys on a single value while a book is identified by title, author and publication year together. The registry is reused with a key formed from the three attributes; forming that key is a catalog business rule, not a change to the registry.
      Impact: Duplicate prevention keeps an atomic register-if-absent guarantee; no side effect is modified, so nothing that depends on the registry is disturbed.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: capability_side_effects::CS_REGISTRY_V0 publishes REGISTER, RESOLVE, EXISTS, COUNT, DEREGISTER; si.topology.impact reports 19 impacted artifacts across ai_governance. Decided by the business owner.
    - Question Id: 'S2 discovery_concerns #3'
      Finding: Because a record moves from retired back to registered, state must be held as data on the record rather than implied by the store it occupies.
      Impact: The record store must support update in place, which the available durable-record mechanism does.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: capability_side_effects::CS_MUTABLE_JSON_V0 publishes WRITE, READ, LIST, EXISTS, UPDATE_WHERE, DELETE, DELETE_MANY.
    - Question Id: 'S2 discovery_concerns #4'
      Finding: Search excludes retired books while retrieval does not, so the same records are read under two rules. Selection by stated criteria covers both, with the state as one criterion.
      Impact: No separate mechanism is needed for the two read paths.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0 selects records matching stated criteria.
    - Question Id: 'S2 discovery_concerns #5'
      Finding: The one business actor available names an employee of another subdomain and asserts no authorization, so the catalog authors its own actor and its own authorization check while deciding who is authorized remains deferred.
      Impact: One actor and one check authored; the catalog reads authorization and never grants it.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: ai_governance::AC_EMPLOYEE_V0 exists and carries no authorization assertion; si.topology.impact reports 0 impacted artifacts.
    - Question Id: 'S2 gaps #7'
      Finding: Subject is free text, so no value-set validation applies and search by kind is only as consistent as what staff type.
      Impact: One fewer reuse candidate; nothing further to author.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: The business owner stated subject is free text; capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 therefore serves no requested outcome.
    - Question Id: S2 business_processes Search the catalog
      Finding: 'Searching by subject or title needs the book records themselves, and the durable-record mechanism publishes only keys: LIST declares no input and yields keys, UPDATE_WHERE filters but only in order to update, and no operation returns records by content. The mechanism is extended with an operation that publishes the records, which the implementation behind it already produced.'
      Impact: One additive operation on a platform side effect; the selection stays with the catalog, which is where the criteria are business knowledge.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: capability_side_effects::CS_MUTABLE_JSON_V0 publishes LIST with input [] and output [result_status, keys]; si.topology.impact reports 12 impacted artifacts. Decided by the business owner.
    - Question Id: S1 constraints — business policy limits
      Finding: No limit on copies per book, no retention period on retired records and no limit on subjects per book were stated. Nothing further constrains the design.
      Impact: No constraint rows are added at Stage 4 beyond those Stage 1 carried.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: Confirmed by the business owner at this stage.
  verification_results:
    columns:
    - Item
    - Origin
    - Result (CONFIRMED, OVERTURNED)
    - Evidence
    rows:
    - Item: book_library_mgmt does not appear to be part of the current software baseline.
      Origin: 'S2 belief_verification #1'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'Re-read at this stage: si.artifact.list for domain book_library_mgmt returns nothing, and si.snapshot.summary reports five domains — ai_governance, inspection, platform, transformation, workload — over 292 artifacts.'
    - Item: No capability in the current composition manages a library catalog.
      Origin: 'S2 belief_verification #2'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'Re-read at this stage: si.vocab.search returns no identity for book, copy, barcode, subject or title; si.store.list reports five declared stores, none holding library records.'
    - Item: Durable records can be held, read, listed and updated in place by a declared side effect.
      Origin: 'S2 architectural_observations #2'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: capability_side_effects::CS_MUTABLE_JSON_V0 publishes WRITE, READ, LIST, EXISTS, UPDATE_WHERE, DELETE, DELETE_MANY.
    - Item: Uniqueness is available as a declared side effect, keyed on a single value.
      Origin: 'S2 architectural_observations #3'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: capability_side_effects::CS_REGISTRY_V0 publishes REGISTER, RESOLVE, EXISTS, COUNT, DEREGISTER — one key per registration.
    - Item: Pure transforms exist for assembling a record, validating its shape and selecting records by criteria.
      Origin: 'S2 architectural_observations #4'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and capability_transforms::CT_PURE_FILTER_RECORDS_V0 are carried by the composition's artifact index.
    - Item: A business subdomain declares its own stores and binds its own workflows to them.
      Origin: 'S2 architectural_observations #1'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 declares that subdomain's stores; ai_governance::RB_LICENSE_BINDINGS_V0 binds its surface.
  dependency_discoveries:
    columns:
    - Dependency
    - Type
    - Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE)
    - Evidence
    rows:
    - Dependency: capability_side_effects::CS_MUTABLE_JSON_V0
      Type: Durable record storage
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: Publishes update in place, which reinstatement requires.
    - Dependency: capability_side_effects::CS_REGISTRY_V0
      Type: Uniqueness
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: Publishes register-if-absent, keyed on one value formed from the three identifying attributes.
    - Dependency: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Type: Append-only trail
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: Publishes APPEND and GET_ALL; si.topology.impact reports 21 impacted artifacts.
    - Dependency: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Type: Record assembly
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: Assembles a durable record from supplied values; 0 impacted artifacts.
    - Dependency: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Type: Record shape validation
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: Confirms a record carries its declared fields; 0 impacted artifacts.
    - Dependency: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Type: Record selection
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: Selects records matching stated criteria; 0 impacted artifacts.
    - Dependency: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Type: Parameter validation
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: Confirms supplied parameters satisfy declared rules; si.topology.impact reports 7 impacted artifacts.
    - Dependency: The catalog's own append-only audit store
      Type: Store declaration
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): AUTHOR_NEW
      Evidence: No store in the composition holds catalog records or catalog audit entries.
    - Dependency: The catalog's own audit composition
      Type: Governed operation step
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): AUTHOR_NEW
      Evidence: The only composed audit step writes through another subdomain's store declaration.
    - Dependency: A library staff actor
      Type: Business actor
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): AUTHOR_NEW
      Evidence: ai_governance::AC_EMPLOYEE_V0 names another subdomain's employee and asserts no authorization.
    - Dependency: Nine catalog operations, their entry points and their business moments
      Type: Governed operation surface
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): AUTHOR_NEW
      Evidence: Semantic vocabulary search returns no library identity of any kind.
  impact_analysis:
    columns:
    - Artifact
    - Impact Scope
    - Consumer Count
    - Evidence
    rows:
    - Artifact: capability_side_effects::CS_MUTABLE_JSON_V0
      Impact Scope: ai_governance, workload
      Consumer Count: '12'
      Evidence: si.topology.impact impacted_count 12, impacted_namespaces ai_governance and workload; si.artifact.refs ref_count 4
    - Artifact: capability_side_effects::CS_REGISTRY_V0
      Impact Scope: ai_governance
      Consumer Count: '19'
      Evidence: si.topology.impact impacted_count 19, impacted_namespaces ai_governance; si.artifact.refs ref_count 6
    - Artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
      Impact Scope: ai_governance
      Consumer Count: '21'
      Evidence: si.topology.impact impacted_count 21, impacted_namespaces ai_governance; si.artifact.refs ref_count 5
    - Artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
      Impact Scope: none
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
    - Artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      Impact Scope: none
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
    - Artifact: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Impact Scope: none
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
    - Artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      Impact Scope: ai_governance
      Consumer Count: '7'
      Evidence: si.topology.impact impacted_count 7, impacted_namespaces ai_governance; si.artifact.refs ref_count 1
    - Artifact: ai_governance::CC_APPEND_AUDIT_EVENT_V0
      Impact Scope: ai_governance
      Consumer Count: '9'
      Evidence: si.topology.impact impacted_count 9, impacted_namespaces ai_governance; si.artifact.refs ref_count 7 — examined and not reused
    - Artifact: ai_governance::AC_EMPLOYEE_V0
      Impact Scope: none
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0 — examined and not reused
  authoring_decisions:
    columns:
    - Capability
    - Decision (REUSE, EXTEND, AUTHOR_NEW)
    - Rationale
    - Alternatives Checked
    - Source Finding
    rows:
    - Capability: Hold a book record durably and update it in place
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Records must be written, read, listed and updated in place, and state must move both ways on the same record. The declared mechanism does exactly this and is read, not modified.
      Alternatives Checked: capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is; catalog::CS_APPENDONLY_JSONL_V0 was examined and rejected because an append-only trail cannot update a record in place.
      Source Finding: 'S3 analysis_findings #3'
    - Capability: Hold a physical copy record durably in CS_MUTABLE_JSON_V0 and update it in place
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: The same durability and in-place update the book record needs, for a record addressed by barcode.
      Alternatives Checked: capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is.
      Source Finding: 'S3 analysis_findings #3'
    - Capability: Enforce that one book exists per title, author and publication year
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Register-if-absent gives an atomic uniqueness guarantee. A key formed from the three identifying attributes is a catalog business rule, so nothing about the mechanism changes and nothing depending on it is disturbed.
      Alternatives Checked: capability_side_effects::CS_REGISTRY_V0 reused with a composite key; extending it to accept multi-attribute keys was examined and rejected as a change to a side effect 19 artifacts depend on. Decided by the business owner.
      Source Finding: 'S3 analysis_findings #2'
    - Capability: Enforce that one physical copy exists per barcode
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: A barcode is a single value, so the registry's own key is the business key with no convention added.
      Alternatives Checked: capability_side_effects::CS_REGISTRY_V0 satisfies it as-is.
      Source Finding: 'S2 belief_verification #99'
    - Capability: Assemble a catalog record from supplied values
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Assembling a durable record from supplied values carries no catalog meaning and is already a pure transform.
      Alternatives Checked: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 satisfies it as-is.
      Source Finding: 'S3 decision_register #1'
    - Capability: Confirm a catalog record carries its required fields
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Shape validation against a declared contract is mechanism, not business rule; which fields a book requires is stated by the catalog's own contract.
      Alternatives Checked: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 satisfies it as-is.
      Source Finding: 'S2 architectural_observations #4'
    - Capability: Select the catalog records matching stated criteria
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Search and retrieval read the same records under different criteria, including the record's state, which selection by stated criteria covers.
      Alternatives Checked: capability_transforms::CT_PURE_FILTER_RECORDS_V0 satisfies it as-is.
      Source Finding: 'S3 analysis_findings #4'
    - Capability: Confirm the parameters supplied to a catalog operation satisfy their declared rules
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Parameter validation is mechanism; the rules are declared by the catalog's own operations.
      Alternatives Checked: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 satisfies it as-is.
      Source Finding: S2 pps_baseline_fqdns Parameter rule validation
    - Capability: Append an entry to an append-only trail
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: The mechanism beneath an audit trail carries no domain meaning and is already declared.
      Alternatives Checked: capability_side_effects::CS_APPENDONLY_JSONL_V0 satisfies it as-is.
      Source Finding: 'S3 analysis_findings #1'
    - Capability: Record a performed catalog operation in the catalog's audit trail
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: The catalog owns its traceability, so that library auditing does not depend on another subdomain's semantics or write into a store that subdomain owns. The mechanism beneath it is reused.
      Alternatives Checked: 'ai_governance::CC_APPEND_AUDIT_EVENT_V0 was examined and rejected: it writes through ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0, and a subdomain owns its stores exclusively. Extending it was rejected as making a licensing artifact depend on library meaning. Decided by the business owner.'
      Source Finding: 'S3 analysis_findings #1'
    - Capability: Declare the stores the catalog owns
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: A subdomain declares its own stores; the catalog needs a book store, a copy store and an audit trail of its own.
      Alternatives Checked: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 was examined as the worked form and rejected as another subdomain's declaration.
      Source Finding: 'S2 architectural_observations #1'
    - Capability: Bind the catalog's operations to the stores and mechanisms they use
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Bindings name one subdomain's surface and cannot be shared across subdomains.
      Alternatives Checked: ai_governance::RB_LICENSE_BINDINGS_V0 was examined as the worked form and rejected as another subdomain's bindings.
      Source Finding: 'S2 architectural_observations #1'
    - Capability: A library staff actor whose authorization a catalog operation binds
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Every operation is refused unless the staff member is authorized, and nothing existing asserts that authorization.
      Alternatives Checked: 'ai_governance::AC_EMPLOYEE_V0 was examined and rejected: it names another subdomain''s employee and asserts no authorization.'
      Source Finding: 'S3 analysis_findings #5'
    - Capability: Confirm the staff member performing an operation is authorized
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: The catalog reads authorization on every operation; deciding who is authorized stays deferred to the staff function.
      Alternatives Checked: ai_governance::CC_VALIDATE_ELIGIBILITY_V0 was examined and rejected as a licensing eligibility rule, not an authorization read.
      Source Finding: 'S3 analysis_findings #5'
    - Capability: Register a book together with its first physical copy
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: No capability in the composition registers a book; the operation carries the catalog's own refusals and identity rule.
      Alternatives Checked: ai_governance::CC_PROVISION_LICENSE_V0 was examined as the worked form of a governed operation pipeline and rejected as licensing semantics.
      Source Finding: 'S2 belief_verification #2'
    - Capability: Register a further physical copy against a registered book
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Nothing existing records a copy against a book, and the operation carries the barcode uniqueness and existence refusals.
      Alternatives Checked: ai_governance::CC_PROVISION_LICENSE_V0 was examined as the worked form and rejected as licensing semantics.
      Source Finding: 'S2 belief_verification #2'
    - Capability: Update a book's bibliographic information
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Nothing existing updates a catalog record, and the operation carries the refusal that an update must not make one book a duplicate of another.
      Alternatives Checked: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0 was examined as an in-place update of a governed record and rejected as licensing semantics.
      Source Finding: 'S2 belief_verification #2'
    - Capability: Retire a book record
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Nothing existing retires a catalog record, and retirement must leave the book's copies untouched.
      Alternatives Checked: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 was examined as the worked form of withdrawing a governed record and rejected as licensing semantics.
      Source Finding: 'S2 belief_verification #2'
    - Capability: Retire a physical copy
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Nothing existing retires a copy, and retirement must leave the book record untouched even when it was the last copy.
      Alternatives Checked: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 was examined as the worked form and rejected as licensing semantics.
      Source Finding: 'S2 belief_verification #2'
    - Capability: Return a retired book record to the registered state
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Reinstatement is a business transition the composition has no counterpart for, and it must leave the book's copies untouched.
      Alternatives Checked: ai_governance::CC_PROVISION_LICENSE_V0 was examined as the worked form of restoring a governed record and rejected as licensing semantics.
      Source Finding: 'S1 lifecycle_transitions #3'
    - Capability: Return a retired physical copy to the registered state
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: The same transition for a copy, leaving the book record untouched.
      Alternatives Checked: ai_governance::CC_PROVISION_LICENSE_V0 was examined as the worked form and rejected as licensing semantics.
      Source Finding: 'S1 lifecycle_transitions #6'
    - Capability: Read every book record so that a search can select among them by content
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The records must be published before anything can select among them by content. The operation is additive, so no consumer of the mechanism is affected, and the implementation behind it already returned records — only the declaration was keys-only.
      Alternatives Checked: capability_side_effects::CS_MUTABLE_JSON_V0 is extended with an operation that publishes records; its LIST was examined and rejected as keys-only, and its UPDATE_WHERE as filtering only in order to update. Decided by the business owner.
      Source Finding: 'S3 analysis_findings #7'
    - Capability: Search the catalog by subject or title, excluding retired books
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Nothing existing searches a catalog; the operation states the criteria and the exclusion, and reuses record selection beneath.
      Alternatives Checked: capability_transforms::CT_PURE_FILTER_RECORDS_V0 is reused as the mechanism; no composed search operation exists to reuse.
      Source Finding: 'S3 analysis_findings #4'
    - Capability: Retrieve a book's complete details with the copies the library holds
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Nothing existing reads a book with its copies, and retrieval must serve retired books as well as registered ones.
      Alternatives Checked: ai_governance::CC_RESOLVE_LICENSE_TIER_V0 was examined as the worked form of a governed read and rejected as licensing semantics.
      Source Finding: 'S2 belief_verification #2'
    - Capability: A governed entry point for each catalog operation
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Each operation is requested through its own governed entry point, and none exists for any catalog operation.
      Alternatives Checked: ai_governance::IN_PROVISION_AI_LICENSE_V0 was examined as the worked form and rejected as a licensing request.
      Source Finding: S2 pps_baseline_fqdns Business entry point
    - Capability: A business moment for each of the five catalog events
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Five business moments are declared and none is recognised anywhere in the composition.
      Alternatives Checked: ai_governance::EV_LICENSE_PROVISIONED_V0 was examined as the worked form and rejected as a licensing moment.
      Source Finding: S1 business_events Book Registered
  placement_decision:
    columns:
    - Decision (NEW_SUBDOMAIN, EXTEND)
    - Subdomain
    - Rationale
    - Source Finding
    rows:
    - Decision (NEW_SUBDOMAIN, EXTEND): NEW_SUBDOMAIN
      Subdomain: catalog
      Rationale: The composition carries no artifact in the book_library_mgmt namespace and nothing that manages a library catalog, so there is no subdomain to extend. The catalog is the first of ten functions the project will govern, and the remaining nine are declared adjacent rather than touched.
      Source Finding: ''
  saturation:
    columns:
    - Criterion
    - Status (SATISFIED, NOT_SATISFIED)
    - Evidence
    rows:
    - Criterion: No unresolved CRITICAL gaps
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: 'All six CRITICAL gaps carried from Stage 2 have an authoring decision: records, operations, actor, business moments, composite uniqueness and the catalog''s own audit trail.'
    - Criterion: No open analyst questions
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: 'Stage 2 carried one open question, on whether subject is a declared value set; the business owner answered that subject is free text, and it is closed as S3 analysis_findings #6.'
    - Criterion: No dependency expansion in the last pass
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: The dependency register closed at eleven entries — seven reused, four authored — and re-reading the composition at this stage surfaced no further dependency.
    - Criterion: Verification pass complete, no OVERTURNED item unresolved
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: Six items re-verified against the composition, all CONFIRMED, none OVERTURNED.
    - Criterion: Every INFERRED finding promoted, accepted or carried forward with a reason
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: Stage 2 carried two INFERRED concerns — that state must be held as data, and that search and retrieval read under different rules. Both are re-grounded here as OBSERVED against the published operations of the mechanisms concerned.
```

> Every decision below is reached and reasoned. What is wrong with each is where it says the reason came from, or whether the alternative it weighed is there.

Every decision below is grounded in the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d`, re-read at this stage rather
than inherited from Stage 2. Two compromises could not be settled by evidence and were decided by the
business owner: how the catalog satisfies traceability, and how uniqueness on a three-attribute
identity is enforced.

---

## 1. Analysis Findings

---

## 2. Mandatory Verification Pass

---

## 3. Dependency Discoveries

---

## 4. Impact Analysis

Every reused artifact is read, never modified, so this change adds consumers and disturbs none of the
counts above.

---

## 5. Authoring Decisions

---

## 6. Subdomain Placement Decision

---

## 7. Saturation Assessment

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
