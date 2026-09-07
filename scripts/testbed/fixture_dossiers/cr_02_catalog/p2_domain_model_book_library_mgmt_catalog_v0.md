# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

**Stage:** 2 — Domain Model Verification
**CR:** cr_02_catalog
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition, and every other
register projects from those resolutions. This is the first change request whose baseline contains a
subdomain the pipeline itself built: what already exists here is the previous catalog change's own
output.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Work | A published work, recognizable as one thing across the editions in which it is published. | None — the composition holds no store for a work, and nothing groups records that describe one. | OBSERVED | S2 belief_verification #3 |
| Edition | A publication of a work, identified by title, author and publication year. The record the previous change calls a book is an edition. | A durable record store keyed by the identifying attributes, holding one record per edition. | OBSERVED | S2 belief_verification #2 |
| Physical Copy | An individual copy the library owns, belonging to exactly one edition. | A durable record store keyed by barcode, holding one record per copy. | OBSERVED | S2 belief_verification #4 |
| Bibliographic Information | An edition's descriptive content. | Held within the edition's own record. | OBSERVED | S2 belief_verification #2 |
| Edition Summary | Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean. | None — search results carry one edition's bibliographic information and nothing about a work. | OBSERVED | S2 belief_verification #5 |
| Work Summary | A short description of the work an edition belongs to, carried in that edition's retrieval. | None — retrieval carries the edition and its copies and nothing about a work. | OBSERVED | S2 belief_verification #5 |
| Existing Catalog Record | A catalog record written under the previous governed change, before this one. | The same store the edition occupies; the composition declares the store, not its contents. | INFERRED | S2 belief_verification #7 |
| Authorized Staff | A library staff member permitted to perform catalog operations. | None — the catalog requires authorization and does not decide it. | OBSERVED | S2 belief_verification #5 |
| Business Operation | An action performed against the catalog that must be traceable and auditable. | An append-only trail holding one entry per performed operation. | OBSERVED | S2 belief_verification #5 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Work | Title | The work's title, shared by every edition of it. | INFERRED | S1 identity_and_sameness #1 |
| Work | Author | The work's author, shared by every edition of it. | INFERRED | S1 identity_and_sameness #1 |
| Edition | Title | The edition's title, one of the three attributes that identify it. | OBSERVED | S2 belief_verification #3 |
| Edition | Author | The edition's author, one of the three attributes that identify it. | OBSERVED | S2 belief_verification #3 |
| Edition | Publication Year | The year of publication, the attribute that distinguishes one edition of a work from another. | OBSERVED | S2 belief_verification #3 |
| Edition | Subject | What kind of material it is, stated as free text, and what staff search on. | OBSERVED | S2 belief_verification #5 |
| Edition | State | Whether the edition's record is registered or retired. | OBSERVED | S2 belief_verification #6 |
| Edition | Identifying Key | The single value formed from title, author and publication year, claimed so that no two editions share it. | OBSERVED | S2 belief_verification #3 |
| Physical Copy | Barcode | The identifier the library assigns to a copy, which distinguishes it from every other copy. | OBSERVED | S2 belief_verification #4 |
| Physical Copy | Edition Identity | The edition the copy belongs to, recorded on the copy. | OBSERVED | S2 belief_verification #4 |
| Physical Copy | State | Whether the copy's record is registered or retired. | OBSERVED | S2 belief_verification #6 |
| Business Operation | Operation Record | What was performed, by whom, against which record. | OBSERVED | S2 belief_verification #5 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Register an edition of a work the catalog does not yet hold | Authorized staff | The work enters the catalog with its first edition and that edition's first copy. | INFERRED | S1 requested_outcomes #1 |
| Register an additional edition of an existing work | Authorized staff | A further edition is recorded against a work the catalog already holds. | INFERRED | S1 requested_outcomes #2 |
| Search the catalog | Authorized staff | One result per matching work, carrying enough of a summary of that work's editions to choose one. | OBSERVED | S2 belief_verification #5 |
| Retrieve an edition's complete details | Authorized staff | The edition's bibliographic information, the physical copies of it, and a summary of the work it belongs to. | OBSERVED | S2 belief_verification #5 |
| Register a physical copy | Authorized staff | A copy is recorded against exactly one edition. | OBSERVED | S2 belief_verification #4 |
| Update bibliographic information | Authorized staff | A registered edition's descriptive content changes. | OBSERVED | S2 belief_verification #5 |
| Retire a record | Authorized staff | An edition or a copy is judged obsolete and is no longer to be used. | OBSERVED | S2 belief_verification #5 |
| Reinstate a record | Authorized staff | A retired edition or copy returns to the registered state. | OBSERVED | S2 belief_verification #6 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Register an edition of a work the catalog does not yet hold | 1 | Confirm the staff member is authorized. | None | OBSERVED | S2 belief_verification #5 |
| Register an edition of a work the catalog does not yet hold | 2 | Validate the submission carries what an edition requires. | None | OBSERVED | S2 belief_verification #5 |
| Register an edition of a work the catalog does not yet hold | 3 | Claim the work, identified by title and author. | A work record | INFERRED | S1 identity_and_sameness #1 |
| Register an edition of a work the catalog does not yet hold | 4 | Claim the edition's identity, so no two editions share title, author and publication year. | An identity claim | OBSERVED | S2 belief_verification #3 |
| Register an edition of a work the catalog does not yet hold | 5 | Claim the first copy's barcode. | A barcode claim | OBSERVED | S2 belief_verification #4 |
| Register an edition of a work the catalog does not yet hold | 6 | Write the edition record and its first copy record. | An edition record and a copy record | OBSERVED | S2 belief_verification #2 |
| Register an edition of a work the catalog does not yet hold | 7 | Record the operation in the audit trail. | An operation entry | OBSERVED | S2 belief_verification #5 |
| Register an additional edition of an existing work | 1 | Confirm the staff member is authorized. | None | OBSERVED | S2 belief_verification #5 |
| Register an additional edition of an existing work | 2 | Resolve the work the edition belongs to, by title and author. | None | INFERRED | S1 identity_and_sameness #1 |
| Register an additional edition of an existing work | 3 | Claim the edition's identity, so no two editions of the work share a publication year. | An identity claim | OBSERVED | S2 belief_verification #3 |
| Register an additional edition of an existing work | 4 | Write the edition record against the resolved work. | An edition record | INFERRED | S1 requested_outcomes #2 |
| Register an additional edition of an existing work | 5 | Record the operation in the audit trail. | An operation entry | OBSERVED | S2 belief_verification #5 |
| Search the catalog | 1 | Confirm the staff member is authorized. | None | OBSERVED | S2 belief_verification #5 |
| Search the catalog | 2 | Select the registered editions matching the stated subject or title, excluding retired ones. | None | OBSERVED | S2 belief_verification #5 |
| Search the catalog | 3 | Group the matching editions by the work they belong to. | None | INFERRED | S1 requested_outcomes #3 |
| Search the catalog | 4 | Return one result per work, carrying a summary of its matching editions. | A search result | INFERRED | S1 requested_outcomes #3 |
| Retrieve an edition's complete details | 1 | Confirm the staff member is authorized. | None | OBSERVED | S2 belief_verification #5 |
| Retrieve an edition's complete details | 2 | Read the named edition and the physical copies of it. | None | OBSERVED | S2 belief_verification #5 |
| Retrieve an edition's complete details | 3 | Read a summary of the work the edition belongs to. | None | INFERRED | S1 requested_outcomes #4 |
| Retrieve an edition's complete details | 4 | Return the edition, its copies and the work summary. | A retrieval result | INFERRED | S1 requested_outcomes #4 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change. | VERIFIED | The pinned composition declares six domains and carries forty-three artifacts in the book_library_mgmt namespace, among them book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 and book_library_mgmt::RB_CATALOG_BINDINGS_V0, which declare the subdomain's stores and bind its workflows to them. | S1 system_beliefs #1 |
| The catalog is believed to hold bibliographic records and physical copies of library materials. | VERIFIED | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 declares five stores: one for book records, one for physical copies, an append-only operations trail, and two uniqueness registries. book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 write the first two. | S1 system_beliefs #2 |
| A book is believed to be identified by title, author and publication year. | VERIFIED | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 forms one key from exactly those three attributes, and book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 claims that key so a second record carrying the same three is refused. book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 resolves a record by the same key. | S1 system_beliefs #3 |
| A physical copy is believed to belong to exactly one book. | VERIFIED | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 records a copy against one book record, and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 claims its barcode so no two copies share one. | S1 system_beliefs #4 |
| The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details. | VERIFIED | Nine workflows serve them: book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0. Every one admits only an authorized staff member, through book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0. | S1 system_beliefs #5 |
| A retired record is believed to be reinstatable. | VERIFIED | book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 return a retired record to the registered state, reached through book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0. | S1 system_beliefs #6 |
| Records written under the previous change are believed to exist and to be readable. | INSUFFICIENT_EVIDENCE | The composition declares the stores and the paths they occupy; it does not carry their contents. Whether any record was ever written is runtime state, and no inspection of a sealed snapshot can answer it. The belief is resolvable only by reading a store the previous change wrote. | S1 system_beliefs #7 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Catalog storage declaration | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | Declares the five stores the catalog owns and the paths they occupy. | PARTIAL | It declares no store for a work, and no store in which the grouping of editions under a work could be held. |
| Edition identity key | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | Forms one key from title, author and publication year. | EXACT | It forms an edition's key; the work's key of title and author alone is not a key it forms. |
| Edition identity claim | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | Claims the identifying key so that no two records share title, author and publication year. | EXACT | It claims one edition; it neither claims a work nor relates two editions that share a title and an author. |
| Edition identity resolution | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 | Resolves a registered record by its identifying key. | EXACT | It resolves one edition by its own key and cannot answer which work an edition belongs to. |
| Register an edition | book_library_mgmt::CC_REGISTER_BOOK_V0 | Confirms authorization, validates the submission, claims identity and barcode, writes the record and its first copy, and records the operation. | PARTIAL | It registers an edition standing alone; nothing in it claims or resolves the work the edition belongs to. |
| Validate a submission | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | Confirms a registration carries what a record requires before anything is claimed or written. | PARTIAL | It validates an edition's own attributes and knows nothing a work would require. |
| Register a physical copy | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | Records a copy against one existing record and claims its barcode. | EXACT | Nothing — a copy already belongs to exactly one edition, which is what this change requires of it. |
| Barcode claim | book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | Claims a copy's barcode so no two copies share one. | EXACT | It is unaffected by the work abstraction. |
| Search the catalog | book_library_mgmt::CC_SEARCH_CATALOG_V0 | Selects registered records matching a stated subject or title and excludes retired ones. | PARTIAL | It returns one result per matching edition. It cannot group editions under the work they belong to, and returns three near-identical results where the library wants one. |
| Retrieve complete details | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Assembles one record's bibliographic information together with the physical copies of it. | PARTIAL | It carries no summary of the work the record belongs to, so the work's title cannot be shown without a second lookup. |
| Update bibliographic information | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Changes a registered record's descriptive content and refuses a change that would duplicate another record. | EXACT | It refuses duplication at the edition level, which is where this change leaves it. |
| Retire a record | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 | Retires one record and cascades to nothing. | EXACT | It retires an edition, which is what this change requires; a work is not retired. |
| Retire a physical copy | book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0 | Retires one copy and leaves its record unaffected. | EXACT | It is unaffected by the work abstraction. |
| Reinstate a record | book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | Returns a retired record to the registered state. | EXACT | It is unaffected by the work abstraction. |
| Reinstate a physical copy | book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 | Returns a retired copy to the registered state. | EXACT | It is unaffected by the work abstraction. |
| Audit the operation | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | Appends one performed operation to the catalog's own append-only trail. | EXACT | It records whatever operation it is handed, including ones this change adds. |
| Staff authorization check | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Confirms the staff member performing an operation is authorized. | EXACT | It requires authorization and does not decide it, which this change leaves unchanged. |
| Catalog entry points | book_library_mgmt::IN_REGISTER_BOOK_V0 | Admits a registration request and declares what a caller must supply. | PARTIAL | It admits an edition's attributes and names no work. |
| Search entry point | book_library_mgmt::IN_SEARCH_CATALOG_V0 | Admits a search request stating a subject or a title. | EXACT | It admits the search terms this change keeps; what changes is the shape of the answer. |
| Retrieval entry point | book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | Admits a request for one record's complete details. | PARTIAL | It names the record to retrieve and carries nothing that would ask for the work. |
| Runtime binding declaration | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | Binds the catalog's workflows to the stores and policies they use. | PARTIAL | It binds the five stores that exist; a store for works would have to be bound here too. |
| Business moments | book_library_mgmt::EV_BOOK_REGISTERED_V0 | Declares the moment a record enters the catalog. | PARTIAL | It names the registration of an edition; the moment a work enters the catalog has no declaration. |
| Durable record store | capability_side_effects::CS_MUTABLE_JSON_V0 | Writes, reads, selects, lists, updates in place and deletes durable records. | EXACT | It holds whatever it is given; it enforces no identity and no grouping. |
| Uniqueness registry | capability_side_effects::CS_REGISTRY_V0 | Registers a key, resolves it, and reports whether it exists. | EXACT | It enforces uniqueness on one key; grouping editions under a work is not something it expresses. |
| Record selection | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | Selects the records matching stated criteria. | PARTIAL | It selects records; it does not group the selected records by an attribute they share. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| The catalog has no work — nothing in the composition represents the thing that several editions are editions of. | CRITICAL | Every outcome this change requests rests on it: an additional edition has nothing to be registered against, a search cannot group by it, and a retrieval cannot summarise it. | OBSERVED | S2 belief_verification #3 |
| No store holds a work, and the storage declaration has no place to put one. | CRITICAL | A work that is derived at read time and never recorded cannot be claimed, cannot be resolved, and cannot be shown to have exactly one authoritative record. | OBSERVED | S2 belief_verification #1 |
| Nothing claims a work's identity of title and author, as the edition's identity of title, author and publication year is claimed. | CRITICAL | Without a claim, two registrations describing the same work would produce two works, and the invariant that no two works share a title and an author is unenforceable. | OBSERVED | S2 belief_verification #3 |
| Search returns one result per matching edition and cannot group its results by work. | CRITICAL | The requested outcome is one result per work carrying a summary of its editions; the existing search answers a different question. | OBSERVED | S2 belief_verification #5 |
| Retrieval carries no summary of the work a record belongs to. | CRITICAL | Staff selecting an edition from a search result would have to look the work up separately, which is what carrying the summary exists to avoid. | OBSERVED | S2 belief_verification #5 |
| Registering an edition neither resolves nor creates the work it belongs to. | CRITICAL | Registering an additional edition of an existing work is the change's central operation and has no path through the existing registration. | OBSERVED | S2 belief_verification #5 |
| Records written under the previous change carry no work membership, and whether any such record exists cannot be established from the composition. | OPEN QUESTION | The promise that existing records remain valid without recreation is about data. It is not testable against a snapshot, only against a store the previous change wrote. | INFERRED | S2 belief_verification #7 |
| No business moment is declared for a work entering the catalog. | MINOR | The moments this change adds would go unrecognised while the edition's own moments continue to be declared. | OBSERVED | S2 belief_verification #1 |
| Deciding which staff are authorized still belongs to a function that does not exist. | MINOR | Unchanged by this change, and deferred by the business to the staff function. | OBSERVED | S2 belief_verification #5 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The record the previous change calls a book is identified by exactly the three attributes that identify an edition, and two records differing only in publication year are already two records. The existing catalog therefore already distinguishes editions, and what it has never had is the work above them. | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 · book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | OBSERVED | S2 belief_verification #3 |
| A physical copy is recorded against one record and claims its own barcode, so a copy already belongs to exactly one edition and needs no change at all. | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 · book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 | OBSERVED | S2 belief_verification #4 |
| Uniqueness in this composition is claimed through a registry keyed on one value, and the existing edition key is formed by a pure transform before it is claimed. A work's key of title and author could be formed and claimed the same way. | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 · capability_side_effects::CS_REGISTRY_V0 | OBSERVED | S2 belief_verification #3 |
| Every catalog operation is composed as an ordered pipeline that confirms authorization first and records the operation last, so an operation this change adds has a worked shape to follow. | book_library_mgmt::CC_REGISTER_BOOK_V0 · book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 · book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | OBSERVED | S2 belief_verification #5 |
| Selecting records by stated criteria is available as a pure transform, and grouping the selected records by an attribute they share is not. | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | OBSERVED | S2 belief_verification #5 |
| The subdomain owns its five stores and binds its own workflows to them, so a store for works would be declared and bound in the subdomain's own declarations. | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 · book_library_mgmt::RB_CATALOG_BINDINGS_V0 | OBSERVED | S2 belief_verification #1 |
| Retirement is declared on the record the previous change calls a book and cascades to nothing, which is exactly what retiring an edition independently of a work's other editions requires. | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 · book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 | OBSERVED | S2 belief_verification #6 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The promise that existing records remain valid without recreation cannot be verified at this stage at all. The composition declares stores and paths; it does not carry what is in them, and a snapshot has no way to say whether the previous change ever wrote a record. The promise is a claim about data, and only execution against a store the previous change wrote can settle it. | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | CRITICAL | OBSERVED | S2 belief_verification #7 |
| The existing search is the one existing capability whose answer this change alters, and it is also the one every existing acceptance criterion about search was written against. Grouping its results by work changes the shape of what staff already receive, and the business has accepted that as an extension rather than a regression. | book_library_mgmt::CC_SEARCH_CATALOG_V0 | MAJOR | OBSERVED | S2 belief_verification #5 |
| The work an existing record belongs to is derivable from the record's own title and author, but deriving it at read time and recording it are different things. If a work is claimed, every record written before this change needs a claim it never made; if it is not, the work has no authoritative record. | book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 | MAJOR | INFERRED | S2 belief_verification #3 |
| The registration this change extends already claims two identities and writes two records before it audits, and it was reordered during the previous change so that every claim precedes every write. Adding a work claim to it touches the sequence that ordering was established to protect. | book_library_mgmt::CC_REGISTER_BOOK_V0 · book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | MAJOR | OBSERVED | S2 belief_verification #5 |

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
