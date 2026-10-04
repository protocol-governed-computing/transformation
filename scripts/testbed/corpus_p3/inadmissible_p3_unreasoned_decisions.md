# Analysis Loop — book_library_mgmt / catalog (deliberately inadmissible fixture)

> Every register below is present and correctly shaped. Each records a decision or a claim with the cell that justifies it left empty, or hedged.

**Stage:** 3 — Analysis Loop
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every decision below is grounded in the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d`, re-read at this stage rather
than inherited from Stage 2. Two compromises could not be settled by evidence and were decided by the
business owner: how the catalog satisfies traceability, and how uniqueness on a three-attribute
identity is enforced.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| S2 discovery_concerns #1 | The only composed audit step belongs to another subdomain and appends into that subdomain's store, so reusing it would breach a subdomain's exclusive ownership of its stores. The catalog owns its audit composition and its own append-only store, and reuses the append-only mechanism beneath them. | Two artifacts authored rather than one reused; library traceability stays independent of agent-governance semantics. | OBSERVED | HIGH | CLOSED | ai_governance::CC_APPEND_AUDIT_EVENT_V0 binds capability_side_effects::CS_APPENDONLY_JSONL_V0 and writes through ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0; si.artifact.refs reports 7 direct references, all ai_governance. Decided by the business owner. |
| S2 discovery_concerns #2 | The available uniqueness mechanism keys on a single value while a book is identified by title, author and publication year together. The registry is reused with a key formed from the three attributes; forming that key is a catalog business rule, not a change to the registry. | Duplicate prevention keeps an atomic register-if-absent guarantee; no side effect is modified, so nothing that depends on the registry is disturbed. | OBSERVED | HIGH | CLOSED | capability_side_effects::CS_REGISTRY_V0 publishes REGISTER, RESOLVE, EXISTS, COUNT, DEREGISTER; si.topology.impact reports 19 impacted artifacts across ai_governance. Decided by the business owner. |
| S2 discovery_concerns #3 | Because a record moves from retired back to registered, state must be held as data on the record rather than implied by the store it occupies. | The record store must support update in place, which the available durable-record mechanism does. | OBSERVED | HIGH | CLOSED | capability_side_effects::CS_MUTABLE_JSON_V0 publishes WRITE, READ, LIST, EXISTS, UPDATE_WHERE, DELETE, DELETE_MANY. |
| S2 discovery_concerns #4 | Search excludes retired books while retrieval does not, so the same records are read under two rules. Selection by stated criteria covers both, with the state as one criterion. | No separate mechanism is needed for the two read paths. | OBSERVED | HIGH | CLOSED | capability_transforms::CT_PURE_FILTER_RECORDS_V0 selects records matching stated criteria. |
| S2 discovery_concerns #5 | The one business actor available names an employee of another subdomain and asserts no authorization, so the catalog authors its own actor and its own authorization check while deciding who is authorized remains deferred. | One actor and one check authored; the catalog reads authorization and never grants it. | OBSERVED | HIGH | CLOSED | ai_governance::AC_EMPLOYEE_V0 exists and carries no authorization assertion; si.topology.impact reports 0 impacted artifacts. |
| S2 gaps #7 | Subject is free text, so no value-set validation applies and search by kind is only as consistent as what staff type. | One fewer reuse candidate; nothing further to author. | OBSERVED | HIGH | CLOSED | The business owner stated subject is free text; capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 therefore serves no requested outcome. |
| S2 business_processes Search the catalog | Searching by subject or title needs the book records themselves, and the durable-record mechanism publishes only keys: LIST declares no input and yields keys, UPDATE_WHERE filters but only in order to update, and no operation returns records by content. The mechanism is extended with an operation that publishes the records, which the implementation behind it already produced. | One additive operation on a platform side effect; the selection stays with the catalog, which is where the criteria are business knowledge. | OBSERVED | HIGH | CLOSED | capability_side_effects::CS_MUTABLE_JSON_V0 publishes LIST with input [] and output [result_status, keys]; si.topology.impact reports 12 impacted artifacts. Decided by the business owner. |
| S1 constraints — business policy limits | No limit on copies per book, no retention period on retired records and no limit on subjects per book were stated. Nothing further constrains the design. | No constraint rows are added at Stage 4 beyond those Stage 1 carried. | OBSERVED | HIGH | CLOSED | Confirmed by the business owner at this stage. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| book_library_mgmt does not appear to be part of the current software baseline. | S2 belief_verification #1 | CONFIRMED | Re-read at this stage: si.artifact.list for domain book_library_mgmt returns nothing, and si.snapshot.summary reports five domains — ai_governance, inspection, platform, transformation, workload — over 292 artifacts. |
| No capability in the current composition manages a library catalog. | S2 belief_verification #2 | CONFIRMED | Re-read at this stage: si.vocab.search returns no identity for book, copy, barcode, subject or title; si.store.list reports five declared stores, none holding library records. |
| Durable records can be held, read, listed and updated in place by a declared side effect. | S2 architectural_observations #2 | CONFIRMED | capability_side_effects::CS_MUTABLE_JSON_V0 publishes WRITE, READ, LIST, EXISTS, UPDATE_WHERE, DELETE, DELETE_MANY. |
| Uniqueness is available as a declared side effect, keyed on a single value. | S2 architectural_observations #3 | CONFIRMED |  |
| Pure transforms exist for assembling a record, validating its shape and selecting records by criteria. | S2 architectural_observations #4 | CONFIRMED | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and capability_transforms::CT_PURE_FILTER_RECORDS_V0 are carried by the composition's artifact index. |
| A business subdomain declares its own stores and binds its own workflows to them. | S2 architectural_observations #1 | CONFIRMED | ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 declares that subdomain's stores; ai_governance::RB_LICENSE_BINDINGS_V0 binds its surface. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | Durable record storage | REUSE | Publishes update in place, which reinstatement requires. |
| capability_side_effects::CS_REGISTRY_V0 | Uniqueness | REUSE | Publishes register-if-absent, keyed on one value formed from the three identifying attributes. |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | Append-only trail | REUSE | Publishes APPEND and GET_ALL; si.topology.impact reports 21 impacted artifacts. |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Record assembly | REUSE | Assembles a durable record from supplied values; 0 impacted artifacts. |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Record shape validation | REUSE | Confirms a record carries its declared fields; 0 impacted artifacts. |
| capability_transforms::CT_PURE_FILTER_RECORDS_V0 | Record selection | REUSE | Selects records matching stated criteria; 0 impacted artifacts. |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Parameter validation | REUSE | Confirms supplied parameters satisfy declared rules; si.topology.impact reports 7 impacted artifacts. |
| The catalog's own append-only audit store | Store declaration | AUTHOR_NEW | No store in the composition holds catalog records or catalog audit entries. |
| The catalog's own audit composition | Governed operation step | AUTHOR_NEW | The only composed audit step writes through another subdomain's store declaration. |
| A library staff actor | Business actor | AUTHOR_NEW | ai_governance::AC_EMPLOYEE_V0 names another subdomain's employee and asserts no authorization. |
| Nine catalog operations, their entry points and their business moments | Governed operation surface | AUTHOR_NEW | Semantic vocabulary search returns no library identity of any kind. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | ai_governance, workload | 12 | si.topology.impact impacted_count 12, impacted_namespaces ai_governance and workload; si.artifact.refs ref_count 4 |
| capability_side_effects::CS_REGISTRY_V0 | ai_governance | 19 | si.topology.impact impacted_count 19, impacted_namespaces ai_governance; si.artifact.refs ref_count 6 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | ai_governance | 21 |  |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | none | 0 | si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | none | 0 | si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0 |
| capability_transforms::CT_PURE_FILTER_RECORDS_V0 | none | 0 | si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | ai_governance | 7 | si.topology.impact impacted_count 7, impacted_namespaces ai_governance; si.artifact.refs ref_count 1 |
| ai_governance::CC_APPEND_AUDIT_EVENT_V0 | ai_governance | 9 | si.topology.impact impacted_count 9, impacted_namespaces ai_governance; si.artifact.refs ref_count 7 — examined and not reused |
| ai_governance::AC_EMPLOYEE_V0 | none | 0 | si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0 — examined and not reused |

Every reused artifact is read, never modified, so this change adds consumers and disturbs none of the
counts above.

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Hold a book record durably and update it in place | REUSE | Records must be written, read, listed and updated in place, and state must move both ways on the same record. The declared mechanism does exactly this and is read, not modified. | capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is; capability_side_effects::CS_APPENDONLY_JSONL_V0 was examined and rejected because an append-only trail cannot update a record in place. | S3 analysis_findings #3 |
| Hold a physical copy record durably and update it in place | REUSE |  | capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is. | S3 analysis_findings #3 |
| Enforce that one book exists per title, author and publication year | REUSE | Register-if-absent gives an atomic uniqueness guarantee. A key formed from the three identifying attributes is a catalog business rule, so nothing about the mechanism changes and nothing depending on it is disturbed. | capability_side_effects::CS_REGISTRY_V0 reused with a composite key; extending it to accept multi-attribute keys was examined and rejected as a change to a side effect 19 artifacts depend on. Decided by the business owner. | S3 analysis_findings #2 |
| Enforce that one physical copy exists per barcode | REUSE | A barcode is a single value, so the registry's own key is the business key with no convention added. |  | S3 analysis_findings #2 |
| Assemble a catalog record from supplied values | UNRESOLVED | Assembling a durable record from supplied values carries no catalog meaning and is already a pure transform. | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 satisfies it as-is. | S2 architectural_observations #4 |
| Confirm a catalog record carries its required fields | REUSE | Shape validation against a declared contract is mechanism, not business rule; which fields a book requires is stated by the catalog's own contract. | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 satisfies it as-is. | S2 architectural_observations #4 |
| Select the catalog records matching stated criteria | REUSE | Search and retrieval read the same records under different criteria, including the record's state, which selection by stated criteria covers. | capability_transforms::CT_PURE_FILTER_RECORDS_V0 satisfies it as-is. | S3 analysis_findings #4 |
| Confirm the parameters supplied to a catalog operation satisfy their declared rules | REUSE | Parameter validation is mechanism; the rules are declared by the catalog's own operations. | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 satisfies it as-is. | S2 pps_baseline_fqdns Parameter rule validation |
| Append an entry to an append-only trail | REUSE | The mechanism beneath an audit trail carries no domain meaning and is already declared. | capability_side_effects::CS_APPENDONLY_JSONL_V0 satisfies it as-is. | S3 analysis_findings #1 |
| Record a performed catalog operation in the catalog's audit trail | AUTHOR_NEW | The catalog owns its traceability, so that library auditing does not depend on another subdomain's semantics or write into a store that subdomain owns. The mechanism beneath it is reused. | ai_governance::CC_APPEND_AUDIT_EVENT_V0 was examined and rejected: it writes through ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0, and a subdomain owns its stores exclusively. Extending it was rejected as making a licensing artifact depend on library meaning. Decided by the business owner. | S3 analysis_findings #1 |
| Declare the stores the catalog owns | AUTHOR_NEW | A subdomain declares its own stores; the catalog needs a book store, a copy store and an audit trail of its own. | ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 was examined as the worked form and rejected as another subdomain's declaration. | S2 architectural_observations #1 |
| Bind the catalog's operations to the stores and mechanisms they use | AUTHOR_NEW | Bindings name one subdomain's surface and cannot be shared across subdomains. | ai_governance::RB_LICENSE_BINDINGS_V0 was examined as the worked form and rejected as another subdomain's bindings. | S2 architectural_observations #1 |
| A library staff actor whose authorization a catalog operation binds | AUTHOR_NEW | Every operation is refused unless the staff member is authorized, and nothing existing asserts that authorization. | ai_governance::AC_EMPLOYEE_V0 was examined and rejected: it names another subdomain's employee and asserts no authorization. | S3 analysis_findings #5 |
| Confirm the staff member performing an operation is authorized | AUTHOR_NEW | The catalog reads authorization on every operation; deciding who is authorized stays deferred to the staff function. | ai_governance::CC_VALIDATE_ELIGIBILITY_V0 was examined and rejected as a licensing eligibility rule, not an authorization read. | S3 analysis_findings #5 |
| Register a book together with its first physical copy | AUTHOR_NEW | No capability in the composition registers a book; the operation carries the catalog's own refusals and identity rule. | ai_governance::CC_PROVISION_LICENSE_V0 was examined as the worked form of a governed operation pipeline and rejected as licensing semantics. | S2 belief_verification #2 |
| Register a further physical copy against a registered book | AUTHOR_NEW | Nothing existing records a copy against a book, and the operation carries the barcode uniqueness and existence refusals. | ai_governance::CC_PROVISION_LICENSE_V0 was examined as the worked form and rejected as licensing semantics. | S2 belief_verification #2 |
| Update a book's bibliographic information | AUTHOR_NEW | Nothing existing updates a catalog record, and the operation carries the refusal that an update must not make one book a duplicate of another. | ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0 was examined as an in-place update of a governed record and rejected as licensing semantics. | S2 belief_verification #2 |
| Retire a book record | AUTHOR_NEW | Nothing existing retires a catalog record, and retirement must leave the book's copies untouched. | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 was examined as the worked form of withdrawing a governed record and rejected as licensing semantics. | S2 belief_verification #2 |
| Retire a physical copy | AUTHOR_NEW | Nothing existing retires a copy, and retirement must leave the book record untouched even when it was the last copy. | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 was examined as the worked form and rejected as licensing semantics. | S2 belief_verification #2 |
| Return a retired book record to the registered state | AUTHOR_NEW | Reinstatement is a business transition the composition has no counterpart for, and it must leave the book's copies untouched. | ai_governance::CC_PROVISION_LICENSE_V0 was examined as the worked form of restoring a governed record and rejected as licensing semantics. | S1 lifecycle_transitions #3 |
| Return a retired physical copy to the registered state | AUTHOR_NEW | The same transition for a copy, leaving the book record untouched. | ai_governance::CC_PROVISION_LICENSE_V0 was examined as the worked form and rejected as licensing semantics. | S1 lifecycle_transitions #6 |
| Read every book record so that a search can select among them by content | EXTEND | The records must be published before anything can select among them by content. The operation is additive, so no consumer of the mechanism is affected, and the implementation behind it already returned records — only the declaration was keys-only. | capability_side_effects::CS_MUTABLE_JSON_V0 is extended with an operation that publishes records; its LIST was examined and rejected as keys-only, and its UPDATE_WHERE as filtering only in order to update. Decided by the business owner. | S3 analysis_findings #7 |
| Search the catalog by subject or title, excluding retired books | AUTHOR_NEW | Nothing existing searches a catalog; the operation states the criteria and the exclusion, and reuses record selection beneath. | capability_transforms::CT_PURE_FILTER_RECORDS_V0 is reused as the mechanism; no composed search operation exists to reuse. | S3 analysis_findings #4 |
| Retrieve a book's complete details with the copies the library holds | AUTHOR_NEW | Nothing existing reads a book with its copies, and retrieval must serve retired books as well as registered ones. | ai_governance::CC_RESOLVE_LICENSE_TIER_V0 was examined as the worked form of a governed read and rejected as licensing semantics. | S2 belief_verification #2 |
| A governed entry point for each catalog operation | AUTHOR_NEW | Each operation is requested through its own governed entry point, and none exists for any catalog operation. | ai_governance::IN_PROVISION_AI_LICENSE_V0 was examined as the worked form and rejected as a licensing request. | S2 pps_baseline_fqdns Business entry point |
| A business moment for each of the five catalog events | AUTHOR_NEW | Five business moments are declared and none is recognised anywhere in the composition. | ai_governance::EV_LICENSE_PROVISIONED_V0 was examined as the worked form and rejected as a licensing moment. | S1 business_events Book Registered |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| NEW_SUBDOMAIN | catalog | The composition carries no artifact in the book_library_mgmt namespace and nothing that manages a library catalog, so there is no subdomain to extend. The catalog is the first of ten functions the project will govern, and the remaining nine are declared adjacent rather than touched. | S2 belief_verification #1 · S1 governance_scope #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All six CRITICAL gaps carried from Stage 2 have an authoring decision: records, operations, actor, business moments, composite uniqueness and the catalog's own audit trail. |
| No open analyst questions | SATISFIED |  |
| No dependency expansion in the last pass | SATISFIED | The dependency register closed at eleven entries — seven reused, four authored — and re-reading the composition at this stage surfaced no further dependency. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Six items re-verified against the composition, all CONFIRMED, none OVERTURNED. |
| Every INFERRED finding promoted, accepted or carried forward with a reason | SATISFIED | Stage 2 carried two INFERRED concerns — that state must be held as data, and that search and retrieval read under different rules. Both are re-grounded here as OBSERVED against the published operations of the mechanisms concerned. |

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
