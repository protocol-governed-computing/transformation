# Domain Model — book_library_mgmt / catalog (deliberately inadmissible fixture)

**Stage:** 2 — Domain Model Verification
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

> P2 verifies the semantic model inherited from P1 against the compiled snapshot. It discovers
> facts; it does not decide. Every belief P1 recorded gets a result, and `NOT_FOUND` is a final
> answer — absence is a finding, not a reason to keep searching.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Catalog | The library's authoritative description of the materials it holds. | Not separately held; the catalog is the whole of the work and copy records. | OPEN | S1 business_vocabulary Catalog |
| Bibliographic Work | The subject of a single authoritative record describing a published title the library holds. | One durable record per work, addressable by identity and updatable in place. | INFERRED | S1 business_vocabulary Bibliographic Work |
| Book | One kind of bibliographic work: a published material the library registers in the catalog. | Not held separately; a book is recorded as the bibliographic work it is a kind of. | INFERRED | S1 business_vocabulary Book |
| Physical Copy | An individual copy owned by the library, belonging to exactly one bibliographic work. | One durable record per copy, each naming the single work it belongs to. | INFERRED | S1 business_vocabulary Physical Copy |
| Catalog Record | The single authoritative record for one bibliographic work or one physical copy. | Durable, addressable state that can be updated in place and marked retired. | INFERRED | S1 business_vocabulary Catalog Record |
| Bibliographic Information | The descriptive content of a bibliographic work's catalog record. | Held within the work's record, not separately. | OPEN | S1 business_vocabulary Bibliographic Information |
| Book Details | The complete description of a registered book, as retrieved by staff. | Not held; assembled on retrieval from a work's record and the copies belonging to it. | OPEN | S1 business_vocabulary Book Details |
| Obsolete Record | A catalog record the library has determined is no longer to be used. | Not held separately; a state a catalog record reaches. | OPEN | S1 business_vocabulary Obsolete Record |
| Authorized Staff | A library staff member permitted to perform catalog operations. | Not held by the catalog; the actor whose identity an operation binds. | INFERRED | S1 business_vocabulary Authorized Staff |
| Business Operation | An action performed against the catalog that must be traceable and auditable. | Not catalog state; appended to a durable record that is never rewritten. | INFERRED | S1 business_vocabulary Business Operation |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Bibliographic Work | identity | What distinguishes one cataloged work from another, so registering the same book twice does not produce two records. | OPEN | S1 acceptance_criteria #8 |
| Bibliographic Work | bibliographic information | The descriptive content staff may update. | OPEN | S1 business_events Bibliographic Information Updated |
| Bibliographic Work | record state | Whether the work's record is current or retired. | OPEN | S1 lifecycle_states Bibliographic Work |
| Physical Copy | identity | What distinguishes one owned copy from another. | OPEN | S1 business_invariants #3 |
| Physical Copy | owning work | The one bibliographic work the copy belongs to. | OPEN | S1 business_invariants #1 |
| Physical Copy | record state | Whether the copy's record is current. | OPEN | S1 lifecycle_states Physical Copy |
| Business Operation | performing staff member | Which authorized staff member performed the operation. | INFERRED | S1 business_invariants #5 |
| Business Operation | what was performed | The action taken and the record it touched, so the operation can be audited afterwards. | INFERRED | S1 business_invariants #4 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Register a book | Authorized staff | The work has exactly one authoritative record in the catalog. | OPEN | S1 business_events Book Registered |
| Register a physical copy | Authorized staff | The copy is recorded against exactly one bibliographic work. | OPEN | S1 business_events Physical Copy Registered |
| Update bibliographic information | Authorized staff | The authoritative description of a registered work is changed. | OPEN | S1 business_events Bibliographic Information Updated |
| Retire an obsolete record | Authorized staff | The record is no longer offered as current. | OPEN | S1 business_events Record Retired |
| Search the catalog | Authorized staff | The materials matching the staff member's terms are located. | OPEN | S1 business_events Catalog Searched |
| Retrieve complete book details | Authorized staff | The complete description of a registered book is returned. | OPEN | S1 business_events Book Details Retrieved |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Register a book | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | OPEN | S1 business_invariants #5 |
| Register a book | 2 | Confirm no authoritative record already exists for the work | A duplication check result | OPEN | S1 acceptance_criteria #8 |
| Register a book | 3 | Record the work's bibliographic information as its authoritative record | The bibliographic work record | OPEN | S1 business_invariants #2 |
| Register a book | 4 | Record that the work was registered | A durable, auditable record of the operation | INFERRED | S1 business_invariants #4 |
| Register a physical copy | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | OPEN | S1 business_invariants #5 |
| Register a physical copy | 2 | Confirm the bibliographic work the copy belongs to is registered | A work-exists check result | OPEN | S1 business_invariants #1 |
| Register a physical copy | 3 | Record the copy against that one work | The physical copy record | OPEN | S1 business_invariants #3 |
| Register a physical copy | 4 | Record that the copy was registered | A durable, auditable record of the operation | INFERRED | S1 business_invariants #4 |
| Update bibliographic information | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | OPEN | S1 business_invariants #5 |
| Update bibliographic information | 2 | Confirm the work has a current authoritative record | A record-exists check result | OPEN | S1 lifecycle_states Bibliographic Work |
| Update bibliographic information | 3 | Replace the descriptive content of that record | The updated bibliographic work record | OPEN | S1 requested_outcomes #3 |
| Update bibliographic information | 4 | Record that the information was updated | A durable, auditable record of the operation | INFERRED | S1 business_invariants #4 |
| Retire an obsolete record | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | OPEN | S1 business_invariants #5 |
| Retire an obsolete record | 2 | Confirm the record is current | A record-state check result | OPEN | S1 lifecycle_states Bibliographic Work |
| Retire an obsolete record | 3 | Mark the record retired so it is no longer offered as current | The retired catalog record | OPEN | S1 acceptance_criteria #4 |
| Retire an obsolete record | 4 | Record that the record was retired | A durable, auditable record of the operation | INFERRED | S1 business_invariants #4 |
| Search the catalog | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | OPEN | S1 business_invariants #5 |
| Search the catalog | 2 | Select the current records matching the staff member's terms | The matching records | OPEN | S1 acceptance_criteria #5 |
| Search the catalog | 3 | Record that the catalog was searched | A durable, auditable record of the operation | INFERRED | S1 business_invariants #4 |
| Retrieve complete book details | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | OPEN | S1 business_invariants #5 |
| Retrieve complete book details | 2 | Assemble the work's record together with the copies belonging to it | The complete book details | OPEN | S1 acceptance_criteria #6 |
| Retrieve complete book details | 3 | Record that the details were retrieved | A durable, auditable record of the operation | INFERRED | S1 business_invariants #4 |

## 3. Belief Verification

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------|----------|----------------|
| No capability in the current composition manages a library catalog. | NOT_FOUND | Semantic vocabulary search over the composition returns no identity for book, library, bibliographic or copy. The only identities matching catalog are inspection::TI_SI_CATALOG_V0 and inspection::TE_SI_CATALOG_V0, which publish the list of inspection operations and carry no library meaning. | S1 system_beliefs #1 |
| The platform offers a governed form in which a business capability of this kind can be declared. | VERIFIED | A business subdomain declares its operations as governed entry points, ordered pipelines, owned stores, bound actors and emitted moments: ai_governance::IN_PROVISION_AI_LICENSE_V0, ai_governance::CC_PROVISION_LICENSE_V0, ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0, ai_governance::RB_LICENSE_BINDINGS_V0, ai_governance::AC_EMPLOYEE_V0, ai_governance::EV_EMPLOYEE_REGISTERED_V0. | S1 system_beliefs #2 |
| The platform already records business operations in a way that can be audited afterwards. | VERIFIED | ai_governance::CC_APPEND_AUDIT_EVENT_V0 and ai_governance::CC_RECORD_GOVERNED_ACTION_V0 append a performed action to an append-only store declared by ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0, realized by capability_side_effects::CS_APPENDONLY_JSONL_V0. | S1 system_beliefs #3 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|------------|------|--------------|-----|-----------|
| Business entry point | ai_governance::IN_PROVISION_AI_LICENSE_V0 | Declares the entry point through which a business operation is requested. | EXACT | It admits a licensing request, not a catalog operation. |
| Governed operation pipeline | ai_governance::CC_PROVISION_LICENSE_V0 | Composes one business operation as an ordered pipeline of governed steps. | EXACT | It carries licensing semantics; the catalog's own operations must be authored. |
| Domain storage declaration | ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 | Declares the stores a business subdomain owns and the paths they occupy. | EXACT | It declares another subdomain's stores; a subdomain owns its stores exclusively. |
| Runtime binding declaration | ai_governance::RB_LICENSE_BINDINGS_V0 | Binds a subdomain's workflows to the stores and policies they use. | EXACT | It binds another subdomain's surface. |
| Business actor | ai_governance::AC_EMPLOYEE_V0 | Declares a business actor whose identity an operation binds. | PARTIAL | It names an employee, not library staff, and asserts no authorization. |
| Business moment | ai_governance::EV_EMPLOYEE_REGISTERED_V0 | Declares a business moment the domain recognizes and emits. | PARTIAL | It declares a licensing moment, not a catalog one. |
| Audit append | ai_governance::CC_APPEND_AUDT_EVENT_V0 | Appends one performed action to a durable audit record. | PARTIAL | It appends another subdomain's audit shape into another subdomain's store. |
| Governed action record | ai_governance::CC_RECORD_GOVERNED_ACTION_V0 | Records that a governed action was performed, with its outcome. | PARTIAL | It records an agent action, not a catalog operation. |
| Append-only record | workload::CS_APPENDONLY_JSONL_V0 | Appends an entry to a durable record that is never rewritten. | EXACT | It records what happened; it decides nothing about what may happen. |
| Keyed mutable state | capability_side_effects::CS_MUTABLE_JSON_V0 | Key-addressable state that can be read and updated in place. | EXACT | It holds state; it enforces no business rule over it. |
| Registry state | capability_side_effects::CS_REGISTRY_V0 | Holds a keyed registry of declared entries. | PARTIAL | It is a registry mechanism, not a bibliographic record. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| No authoritative record exists for a bibliographic work or for a physical copy. | CRITICAL | Every requested outcome rests on that record, and nothing in the composition holds one. | OPEN | S2 belief_verification No capability manages a library catalog |
| No operation registers, describes, searches or retires a library material. | CRITICAL | All six required operations must be authored; none can be reused unchanged. | OPEN | S2 belief_verification No capability manages a library catalog |
| No rule enforces that a copy belongs to exactly one work. | CRITICAL | Nothing enforces it; capability_side_effects::CS_MUTABLE_JSON_V0 would have to carry the rule. | OPEN | S1 business_invariants #1 |
| No audit record is shaped for catalog operations. | OPEN QUESTION | A durable record of performed actions exists but carries another subdomain's shape and store; whether the catalog reuses that shape or declares its own is a Stage-3 decision. | INFERRED | S2 belief_verification The platform already records business operations |
| No authority decides which staff are authorized. | OPEN QUESTION | Every operation is restricted to authorized staff, and the granting authority is unresolved while patron management is deferred. | OPEN | S1 clarification_requests #3 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A business subdomain already declares its operations as governed entry points over ordered pipelines, with the stores it owns declared alongside them. | ai_governance::IN_PROVISION_AI_LICENSE_V0, ai_governance::CC_PROVISION_LICENSE_V0, ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 | OBSERVED | S2 belief_verification The platform offers a governed form |
| A subdomain owns its stores exclusively and declares them itself, so a new subdomain declares its own rather than reaching into another's. | ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0, ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0 | OBSERVED | S2 belief_verification The platform offers a governed form |
| Durable state and the durable record of an action are separate mechanisms: one is updated in place, the other is only appended to. | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | OBSERVED | S2 belief_verification The platform already records business operations |
| Auditability is realized as an ordinary step inside a business pipeline, not as a property the platform supplies underneath one. | ai_governance::CC_APPEND_AUDIT_EVENT_V0, ai_governance::CC_RECORD_GOVERNED_ACTION_V0 | OBSERVED | S2 belief_verification The platform already records business operations |
| The word used for the library's description of its holdings is already in the composition with an unrelated meaning — the list of inspection operations. | inspection::TI_SI_CATALOG_V0, inspection::TE_SI_CATALOG_V0 | OBSERVED | S2 belief_verification No capability manages a library catalog |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The only business subdomain available as precedent governs licensing and agent actions, so the forms observed may carry that subject's shape rather than a general one. | ai_governance::CC_PROVISION_LICENSE_V0, ai_governance::CC_RECORD_GOVERNED_ACTION_V0 | MINOR | OBSERVED | S2 belief_verification The platform offers a governed form |
| Two of the six required operations only read, yet every business operation is required to leave a durable record; if reads are excluded the audit requirement is narrower than the business stated it. | ai_governance::CC_APPEND_AUDIT_EVENT_V0 | MAJOR | INFERRED | S1 clarification_requests #2 |
| The term the business uses for its holdings already denotes something else in the composition, so an identity chosen carelessly would collide in meaning without colliding in name. | inspection::TE_SI_CATALOG_V0 | MINOR | OBSERVED | S2 belief_verification No capability manages a library catalog |

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Does retirement apply to physical copy records as well as to bibliographic work records? | business | The lifecycle a design must support differs, and the composition holds nothing that answers it. | S1 clarification_requests #1 |
