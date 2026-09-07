# Stage 2 — Domain Model Discovery: book_library_mgmt / catalog
**Stage:** 2 — Domain Model Discovery
**CR:** cr_03_catalog
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot through the inspection
interface. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Work | Something the library carries, independent of any edition. | Held by the catalog. | VERIFIED | S1 business_vocabulary #1 |
| Book | An edition of a work. | Held by the catalog. | VERIFIED | S1 business_vocabulary #2 |
| Physical copy | One copy of a book, on a shelf. | Held by the catalog. | VERIFIED | S1 business_vocabulary #3 |
| Moment | Something the catalog announces because the business declared it matters. | Declared, and referred to by nothing. | VERIFIED | S1 business_vocabulary #7 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Moment | What it names | The act whose completion it announces. | VERIFIED | S1 business_events #1 |
| Moment | Whether it is announced | Whether anything in the composition refers to it. | VERIFIED | S1 system_beliefs #1 |
| Book | State | Whether it is in service or retired. | VERIFIED | S1 lifecycle_states #1 |
| Physical copy | State | Whether it is in service or retired. | VERIFIED | S1 lifecycle_states #3 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Registering a work, a book or a physical copy | The library | The thing is held by the catalog. | VERIFIED | S1 system_beliefs #2 |
| Correcting bibliographic information | The library | What the library publishes is changed. | VERIFIED | S1 system_beliefs #2 |
| Retiring a book or a physical copy | The library | The thing is out of service; what is known about it is kept. | VERIFIED | S1 system_beliefs #2 |
| Reinstating a book or a physical copy | The library | The thing is back in service. | VERIFIED | S1 system_beliefs #4 |
| Announcing a moment | The completion of the act it names | Nothing. No act announces anything today. | NOT_FOUND | S1 system_beliefs #1 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Announcing a moment | 1 | Complete the act the moment names. | The act's own record. | VERIFIED | S1 known_facts #3 |
| Announcing a moment | 2 | Announce the moment, carrying which thing it concerns and when. | The announcement. | NOT_FOUND | S1 known_facts #7 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The catalog declares six moments and announces none of them. | VERIFIED | Six are declared — `book_library_mgmt::EV_WORK_REGISTERED_V0`, `EV_BOOK_REGISTERED_V0`, `EV_PHYSICAL_COPY_REGISTERED_V0`, `EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0`, `EV_BOOK_RETIRED_V0`, `EV_PHYSICAL_COPY_RETIRED_V0`. Each reports a reference count of zero, and no workflow in the domain announces anything at all. | S1 system_beliefs #1 |
| The catalog performs registration, correction, retirement and reinstatement, each as its own act. | VERIFIED | Ten workflows are held for this subdomain, including registration of a book, an additional edition and a physical copy; correction of bibliographic information; retirement and reinstatement of both a book record and a physical copy. | S1 system_beliefs #2 |
| Nothing checks whether a declared moment is ever announced. | VERIFIED | No rule relates a declared moment to a reference to it. The six have been declared and silent since the subdomain was built, and nothing has reported a fault. | S1 system_beliefs #3 |
| Reinstatement has no declared moment of its own. | VERIFIED | Two workflows reinstate, and neither a book reinstated nor a copy reinstated appears among the six declared moments. The business's ruling that reinstatement is silent and the composition agree. | S1 system_beliefs #4 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Registers a book | book_library_mgmt::WF_REGISTER_BOOK_V0 | Registers an edition of a work. | PARTIAL | Announces nothing. |
| Registers an additional edition | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | Registers a further edition of a work already carried. | PARTIAL | Announces nothing. |
| Registers a physical copy | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | Puts a copy on a shelf. | PARTIAL | Announces nothing. |
| Corrects bibliographic information | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Changes what the library publishes about a book. | PARTIAL | Announces nothing. |
| Retires a book | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | Takes an edition out of service. | PARTIAL | Announces nothing. |
| Retires a physical copy | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | Takes a copy out of service. | PARTIAL | Announces nothing. |
| Reinstates a book | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | Returns an edition to service. | EXACT | Nothing; the business has ruled reinstatement silent. |
| Reinstates a physical copy | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | Returns a copy to service. | EXACT | Nothing; the business has ruled reinstatement silent. |
| Declares that a work was registered | book_library_mgmt::EV_WORK_REGISTERED_V0 | Names the moment. | PARTIAL | Is referred to by nothing and is therefore never announced. |
| Declares that a book was registered | book_library_mgmt::EV_BOOK_REGISTERED_V0 | Names the moment. | PARTIAL | The same. |
| Declares that a physical copy was registered | book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0 | Names the moment. | PARTIAL | The same. |
| Declares that bibliographic information was updated | book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | Names the moment. | PARTIAL | The same. |
| Declares that a book was retired | book_library_mgmt::EV_BOOK_RETIRED_V0 | Names the moment. | PARTIAL | The same. |
| Declares that a physical copy was retired | book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0 | Names the moment. | PARTIAL | The same. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| No act announces any moment. | CRITICAL | The whole of this change. Six declared moments are silent. | VERIFIED | S1 system_beliefs #1 |
| Nothing checks that a declared moment is announced. | CRITICAL | The silence returned unnoticed once and would again. | VERIFIED | S1 system_beliefs #3 |
| The moment naming a registered work has no single act that plainly produces it. | OPEN QUESTION | Registration of a book and of an additional edition both concern works; which announces a work registered is not evident from the composition. | VERIFIED | S1 assumptions #1 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A declared moment that nothing refers to is indistinguishable, from the outside, from a moment the business never declared. | Reference count of zero on all six. | VERIFIED | S1 system_beliefs #1 |
| This is the same defect a different domain was found to have, in the same shape and for the same reason. | Six moments here; three in the identity function of another domain, all silent, none checked. | VERIFIED | S1 system_beliefs #3 |
| Every act this change touches already exists and needs no new capability. Only where each act ends is changed. | Ten workflows held for this subdomain, all performing their acts today. | VERIFIED | S1 system_beliefs #2 |
| The business's ruling and the composition agree that reinstatement is silent, so this change removes a question rather than answering one. | Two reinstatement workflows, no declared moment for either. | VERIFIED | S1 system_beliefs #4 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The business believed the catalog announced six moments and it announced none. Nothing reported a fault, because nothing checks. | Reference count of zero on all six, and no announcement anywhere in the domain. | CRITICAL | VERIFIED | S1 system_beliefs #1 |
| Two acts register something that concerns a work, and only one moment names a work registered. Attaching it to the wrong act would announce something untrue. | Registration of a book and of an additional edition both exist. | MAJOR | VERIFIED | S1 assumptions #1 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Which act announces that a work was registered — registering a book, or registering an additional edition? | business | A moment attached to the wrong act announces something untrue. | S1 assumptions #1 |
