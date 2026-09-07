# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

**Stage:** 2 — Domain Model Verification
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every claim about what exists is grounded in the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d` — 292 artifacts across
ai_governance, inspection, platform, transformation, workload — read through the inspection interface.
The semantic model is inherited from Stage 1 and confirmed here, never re-derived.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Book | A published material the library catalogs — the general term for anything it catalogs, including materials that are not books. | One durable record per book, addressed by its title, author and publication year together, updatable in place, and markable retired and registered again. | INFERRED | S1 business_vocabulary Book · S1 identity_and_sameness #1 |
| Physical Copy | An individual copy the library owns, belonging to exactly one book. | One durable record per copy, addressed by its barcode, naming the single book it belongs to, and markable retired and registered again. | INFERRED | S1 business_vocabulary Physical Copy · S1 identity_and_sameness #2 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Book | Title | The title the book is published under; part of what identifies it. | INFERRED | S1 known_facts — a book's bibliographic information is title, author, publication year and subject |
| Book | Author | The author the book is published under; part of what identifies it. | INFERRED | S1 known_facts — bibliographic information |
| Book | Publication Year | The year this edition was published; part of what identifies it, and what distinguishes one edition from another. | INFERRED | S1 identity_and_sameness #1 |
| Book | Subject | What kind of book it is. A book carries at least one and may carry several. | INFERRED | S1 known_facts — a book carries at least one subject and may carry several |
| Book | State | Whether the book is registered or retired. | INFERRED | S1 lifecycle_states Book |
| Physical Copy | Barcode | The identifier the library assigns to this copy; what identifies it among all copies the library owns. | INFERRED | S1 identity_and_sameness #2 |
| Physical Copy | Book | The single book this copy belongs to. | INFERRED | S1 business_invariants — each physical copy belongs to exactly one book |
| Physical Copy | State | Whether the copy is registered or retired. | INFERRED | S1 lifecycle_states Physical Copy |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Register a book | Authorized staff | The catalog holds one authoritative record for the book, and one for the physical copy registered with it. | INFERRED | S1 business_events Book Registered |
| Register a physical copy | Authorized staff | The catalog holds one authoritative record for a further copy of a registered book. | INFERRED | S1 business_events Physical Copy Registered |
| Update bibliographic information | Authorized staff | The book's authoritative description reflects the change, or the update is refused for making the book a duplicate of another. | INFERRED | S1 business_events Bibliographic Information Updated |
| Retire a book record | Authorized staff | The book record is retired, excluded from search, still retrievable, and its copies unaffected. | INFERRED | S1 business_events Book Retired |
| Retire a physical copy | Authorized staff | The copy record is retired and the book record is unaffected, including when it was the last copy. | INFERRED | S1 business_events Physical Copy Retired |
| Reinstate a book record | Authorized staff | The retired book record is registered again and appears in search. | INFERRED | S1 lifecycle_transitions #3 |
| Reinstate a physical copy | Authorized staff | The retired copy record is registered again. | INFERRED | S1 lifecycle_transitions #6 |
| Search the catalog | Authorized staff | The bibliographic information of each registered book matching the subject or title searched for. | INFERRED | S1 known_facts — staff search the catalog by subject or by title |
| Retrieve complete book details | Authorized staff | The book's bibliographic information and the physical copies the library holds of it. | INFERRED | S1 known_facts — retrieving complete book details returns the bibliographic information and the copies |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Register a book | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Register a book | 2 | Confirm at least one physical copy is offered with the book | A completeness decision | INFERRED | S1 operation_refusals #2 |
| Register a book | 3 | Confirm the book carries at least one subject | A completeness decision | INFERRED | S1 operation_refusals #3 |
| Register a book | 4 | Confirm no registered book already carries this title, author and publication year | A sameness decision | INFERRED | S1 operation_refusals #1 |
| Register a book | 5 | Record the book's bibliographic information as its authoritative record, registered | The book record | INFERRED | S1 business_invariants — each book has exactly one authoritative record |
| Register a book | 6 | Record the offered copy against the book, registered | The physical copy record | INFERRED | S1 known_facts — registering a book requires at least one physical copy |
| Register a book | 7 | Record that the book was registered | A durable, auditable record of the operation | INFERRED | S1 business_invariants — every business operation is traceable and auditable |
| Register a physical copy | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Register a physical copy | 2 | Confirm the book the copy names is registered in the catalog | An existence decision | INFERRED | S1 operation_refusals #4 |
| Register a physical copy | 3 | Confirm no copy the library owns already carries this barcode | A sameness decision | INFERRED | S1 operation_refusals #5 |
| Register a physical copy | 4 | Record the copy against that book, registered | The physical copy record | INFERRED | S1 business_invariants — each copy has exactly one authoritative record |
| Register a physical copy | 5 | Record that the copy was registered | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Update bibliographic information | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Update bibliographic information | 2 | Confirm the changed title, author and publication year would not match another registered book | A sameness decision | INFERRED | S1 operation_refusals #6 |
| Update bibliographic information | 3 | Record the changed bibliographic information as the book's authoritative description | The updated book record | INFERRED | S1 business_events Bibliographic Information Updated |
| Update bibliographic information | 4 | Record that the book's information was updated | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Retire a book record | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Retire a book record | 2 | Record the book record as retired, leaving its copies as they are | The retired book record | INFERRED | S1 lifecycle_transitions #2 |
| Retire a book record | 3 | Record that the book was retired | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Retire a physical copy | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Retire a physical copy | 2 | Record the copy as retired, leaving the book record as it is | The retired copy record | INFERRED | S1 lifecycle_transitions #5 |
| Retire a physical copy | 3 | Record that the copy was retired | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Reinstate a book record | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Reinstate a book record | 2 | Record the retired book record as registered again | The registered book record | INFERRED | S1 lifecycle_transitions #3 |
| Reinstate a book record | 3 | Record that the book was returned to the registered state | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Reinstate a physical copy | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Reinstate a physical copy | 2 | Record the retired copy as registered again | The registered copy record | INFERRED | S1 lifecycle_transitions #6 |
| Reinstate a physical copy | 3 | Record that the copy was returned to the registered state | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Search the catalog | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Search the catalog | 2 | Select the registered books whose subject or title matches what was searched for, excluding retired books | The matching set | INFERRED | S1 known_facts — a retired book is excluded from search results |
| Search the catalog | 3 | Return the bibliographic information of each matching book, and nothing about its copies | The search result | INFERRED | S1 known_facts — a search returns the bibliographic information of each matching book |
| Search the catalog | 4 | Record that the catalog was searched | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Retrieve complete book details | 1 | Confirm the staff member is authorized to perform catalog operations | An authorization decision | INFERRED | S1 operation_refusals #7 |
| Retrieve complete book details | 2 | Read the book's authoritative record, whether registered or retired | The book record | INFERRED | S1 known_facts — a retired book's details remain retrievable |
| Retrieve complete book details | 3 | Read the physical copies recorded against that book | The copies held | INFERRED | S1 known_facts — complete details return the copies the library holds |
| Retrieve complete book details | 4 | Record that the book's details were retrieved | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The book_library_mgmt project is absent from the current baseline. | VERIFIED | catalog::CS_MUTABLE_JSON_V0 carries no identity in the book_library_mgmt namespace. | S1 system_beliefs #1 |
| No capability in the current composition manages a library catalog. | NOT_FOUND |  | S1 system_beliefs #2 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Uniqueness registry | capability_side_effects::CS_REGISTRY_V0 | Registers a key, resolves it, reports whether it exists, counts and deregisters. | PARTIAL | It enforces uniqueness on one key; a book is identified by title, author and publication year together, and the composite is not a key it forms. |
| Durable record store | capability_side_effects::CS_MUTABLE_JSON_V0 | Writes, reads, lists, updates in place and deletes durable records. | EXACT | It holds whatever it is given; it enforces no identity, no state and no authorization. |
| Append-only trail | capability_side_effects::CS_APPENDONLY_JSONL_V0 | Appends an entry and returns the whole trail. | EXACT | It appends what it is handed; it does not decide which operations must be recorded. |
| Audit composition | ai_governance::CC_APPEND_AUDIT_EVENT_V0 | Composes the recording of a performed action into an append-only store. | PARTIAL | It carries agent-governance semantics and appends to another subdomain's store; a subdomain owns its stores exclusively. |
| Record shape validation | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Confirms a record carries the fields its contract declares. | EXACT | It does not know which fields a book or a copy requires. |
| Record assembly | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Assembles a durable record from supplied values. | EXACT | It applies no identity rule and decides no sameness. |
| Record selection | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | Selects the records matching stated criteria. | EXACT | It knows nothing of registered and retired, so exclusion of retired books must be stated as criteria. |
| Parameter rule validation | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Confirms supplied parameters satisfy declared rules. | EXACT | It carries no catalog rule of its own. |
| Business actor | ai_governance::AC_EMPLOYEE_V0 | Declares a business actor whose identity an operation binds. | PARTIAL | It names an employee of another subdomain and asserts no authorization to perform catalog operations. |
| Business entry point | ai_governance::IN_PROVISION_AI_LICENSE_V0 | Declares the governed entry point through which a business operation is requested. | EXACT | It admits a licensing request, not a catalog operation. |
| Governed operation pipeline | ai_governance::CC_PROVISION_LICENSE_V0 | Composes one business operation as an ordered pipeline of governed steps. | EXACT | It carries licensing semantics; the catalog's operations must be authored. |
| Subdomain storage declaration | ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 | Declares the stores a business subdomain owns and the paths they occupy. | EXACT | It declares another subdomain's stores. |
| Runtime binding declaration | ai_governance::RB_LICENSE_BINDINGS_V0 | Binds a subdomain's workflows to the stores and policies they use. | EXACT | It binds another subdomain's surface. |
| Business moment | ai_governance::EV_LICENSE_PROVISIONED_V0 | Declares a business moment the domain recognises when an operation completes. | EXACT | It names a licensing moment, not a catalog one. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Nothing in the composition holds a book record or a copy record. | CRITICAL | Every requested outcome depends on a durable authoritative record per book and per copy; the store mechanisms exist, the catalog's own stores do not. | OBSERVED | S2 belief_verification #2 |
| No capability registers a book, registers a copy, updates bibliographic information, retires a record, reinstates a record, searches, or retrieves book details. | CRITICAL | The nine business processes have no counterpart in the composition and must all be authored. | OBSERVED | S2 belief_verification #2 |
| No actor exists for library staff, and none asserts authorization to perform catalog operations. | CRITICAL | Every operation is refused unless the staff member is authorized, and there is nothing to bind that decision to. | OBSERVED | S1 operation_refusals #7 |
| No business moment exists for a book or copy being registered, updated, retired or reinstated. | CRITICAL | Five business events are declared and none is recognised anywhere in the composition. | OBSERVED | S1 business_events Book Registered |
| Uniqueness on a composite of title, author and publication year has no counterpart in the composition. | CRITICAL | Duplicate prevention is the business problem this change exists to solve, and the registry available enforces uniqueness on a single key. | OBSERVED | S1 identity_and_sameness #1 |
| No audit trail belongs to the catalog; the only audit composition belongs to another subdomain. | CRITICAL | Every operation must be traceable, and a subdomain owns its stores exclusively. | OBSERVED | S1 business_invariants — every business operation is traceable and auditable |
| Subject is free text, so searching by kind of book is only as consistent as what staff type into it. | MINOR | Noted, not modelled: the business has chosen free text, and no value-set validation applies. | OBSERVED | S1 known_facts — a book's subject is free text |
| Deciding which staff are authorized is deferred to the staff function, which does not exist. | MINOR | Noted, not modelled: the catalog reads authorization and never grants it. | OBSERVED | S1 authority_deferrals #1 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A business subdomain in this composition declares its own stores and binds its own workflows to them, so a new subdomain has a worked precedent for owning its records. | catalog::STRUCTURE_AI_LICENSING_STORAGE_V0 · ai_governance::RB_LICENSE_BINDINGS_V0 | OBSERVED | S2 belief_verification #1 |
| Durable records that are written, read, listed and updated in place are available as a declared side effect, as is an append-only trail. | capability_side_effects::CS_MUTABLE_JSON_V0 · capability_side_effects::CS_APPENDONLY_JSONL_V0 | OBSERVED | S1 system_beliefs #99 |
| An append-only trail exists as a declared side effect and is reused rather than authored. | capability_side_effects::CS_APPENDONLY_JSONL_V0 | OBSERVED |  |
| Uniqueness is available as a declared side effect, keyed on a single value. | capability_side_effects::CS_REGISTRY_V0 | OBSERVED | S1 belief_register #4 |
| Pure transforms already exist for assembling a record, validating its shape, and selecting records by criteria. | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 · capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 · capability_transforms::CT_PURE_FILTER_RECORDS_V0 | OBSERVED | S2 belief_verification #2 |
| Recording a performed action into an append-only trail is already composed as a governed step, within another subdomain. | ai_governance::CC_APPEND_AUDIT_EVENT_V0 | OBSERVED | S1 business_invariants — traceable and auditable |
| The composition carries no business vocabulary for a library: no identity claims book, library, copy, subject, title or barcode. | inspection::TI_SI_CATALOG_V0 | OBSERVED | S2 belief_verification #2 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The only composed audit step belongs to another subdomain, so satisfying traceability by reusing it would cross a subdomain's ownership of its own stores. | ai_governance::CC_APPEND_AUDIT_EVENT_V0 · ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 | MAJOR | OBSERVED | S1 business_invariants — traceable and auditable |
| The available uniqueness mechanism is keyed on one value while a book is identified by three attributes together, so duplicate prevention needs a stated key rather than a direct reuse. | capability_side_effects::CS_REGISTRY_V0 | MAJOR | OBSERVED | S1 identity_and_sameness #1 |
| Reinstatement means a record's state moves both ways, so state must be held as data on the record rather than implied by which store it is in. | capability_side_effects::CS_MUTABLE_JSON_V0 | MAJOR | INFERRED | S1 lifecycle_transitions #3 |
| Search must exclude retired books while retrieval must not, so the same records are read under two different rules. | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | MINOR | INFERRED | S1 known_facts — a retired book is excluded from search results |
| The one business actor available names an employee of another subdomain and asserts no authorization, so authorization has nothing to bind to until the staff function exists. | ai_governance::AC_EMPLOYEE_V0 | MINOR | OBSERVED | S1 authority_deferrals #1 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
