# Stage 2 — Domain Model Discovery: book_library_mgmt / catalog
**Stage:** 2 — Domain Model Discovery
**CR:** cr_04_catalog
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot through the inspection
interface, and against the compiled dispatch the runtime actually reads. What was searched is
recorded, not only what was found. Where a belief came back narrower or wider than Stage 1 stated
it, the correction is recorded against the belief.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Operation | Something a librarian asks the catalog to do. | Ten are declared for this subdomain, each with a boundary and a workflow. | VERIFIED | S1 business_vocabulary #1 |
| Request | One asking, with what the librarian supplied. | Not held; it is what arrives at the boundary. | VERIFIED | S1 business_vocabulary #2 |
| Requirement | Something an operation states a request must supply. | Declared at the operation's boundary, as a name and the form the value takes. | VERIFIED | S1 business_vocabulary #4 |
| Use | A step of the operation reading something the request supplied. | Declared in the operation's own steps, as a reference to the supplied value. | VERIFIED | S1 known_facts #7 |
| Publication year | The year an edition was published. | Held in the catalog's book store. Its form is not declared anywhere the catalog owns; it is stated at each boundary and in the description supplied with each request, which say number in every case but one. | VERIFIED | S1 business_vocabulary #7 |
| Correction | Changing some details of a record the catalog already holds. | The record named, and the changed details supplied together. | VERIFIED | S1 business_vocabulary #5 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Requirement | Its name | What the request must supply. | VERIFIED | S1 business_vocabulary #4 |
| Requirement | The form it takes | Whether the value is a number, a word, a list or a record. | VERIFIED | S1 known_facts #1 |
| Requirement | Whether it must be supplied | All fifty-nine requirements across the subdomain's ten operations must be supplied; none is optional. | VERIFIED | S1 business_invariants #4 |
| Publication year | Its form at the boundary | A number in two of the three operations that name it, and a word in the third. | VERIFIED | S1 known_facts #2 |
| Publication year | Its form in the record | Not declared by the catalog. It is whatever the description supplied with the request says, which is a number in every request the library makes. | VERIFIED | S1 known_facts #1 |
| Correction | The record it names | The identity the catalog holds the record under. Read by the operation's steps. | VERIFIED | S1 known_facts #4 |
| Correction | The details it changes | Supplied together. Read by the operation's steps. | VERIFIED | S1 known_facts #4 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Admitting a request | The catalog boundary | The request proceeds, or it is turned away before anything happened. | VERIFIED | S1 business_vocabulary #3 |
| Registering a further edition | A librarian | A further edition of a held work is registered. | VERIFIED | S1 requested_outcomes #1 |
| Correcting bibliographic information | A librarian | What the library publishes about a record is changed. | VERIFIED | S1 requested_outcomes #2 |
| Registering a work for the first time | A librarian | The work, its first edition and a copy are registered. | VERIFIED | S1 known_facts #2 |
| Comparing what an operation requires against what it uses | Nobody, until now | Nothing performed this while the boundary admitted everything. | VERIFIED | S1 known_facts #12 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Admitting a request | 1 | Read what the operation states a request must supply. | Nothing. | VERIFIED | S1 known_facts #8 |
| Admitting a request | 2 | Turn the request away if anything stated is missing or in the wrong form. | The refusal, given to the librarian before anything happened. | VERIFIED | S1 lifecycle_states #2 |
| Registering a further edition | 3 | Read the eleven things the request supplied, including the publication year. | The edition and the work it belongs to. | VERIFIED | S1 known_facts #7 |
| Correcting bibliographic information | 4 | Read the record named and the details being changed. | The corrected record. | VERIFIED | S1 known_facts #4 |
| Correcting bibliographic information | 5 | Read the title, the author and the publication year the request also supplied. | Nothing. No step performs this. | NOT_FOUND | S1 known_facts #7 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number. | VERIFIED | `book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0` declares the publication year as a word. `book_library_mgmt::IN_REGISTER_BOOK_V0` declares it as a number, as does `book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0`. The description of a book that the library supplies with each request declares it a number, and every year in the library's own exercise of the catalog is a number. Two of three boundaries, the supplied description and the data agree; the third does not. | S1 system_beliefs #1 |
| Correcting bibliographic information asks for three details it does not use. | VERIFIED | `book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0` requires eight things. Its workflow has four steps, and across all four it reads five: the record named, the details being changed, and the three the boundary uses to decide who may perform the operation. The title, the author and the publication year are read by no step. | S1 system_beliefs #2 |
| No other catalog operation asks for something it does not use. | NOT_FOUND | All ten operations of the subdomain were compared, requirement by requirement, against the steps that carry them. **The belief holds in the direction Stage 1 meant it and fails in the other.** No operation but the correction requires something no step uses. But `book_library_mgmt::IN_REGISTER_BOOK_V0` has the opposite defect: its workflow reads the subject of the book and its boundary does not require it. The boundary therefore admits a request with no subject that the operation cannot then carry out. Whether any caller supplies the subject where the act reads it was not established at this stage. | S1 system_beliefs #3 |
| Who may perform each operation is stated separately from what the operation needs. | VERIFIED | Three of the eight things the correction requires — the credentials, the authorisation rules and the identity of the staff member — are consumed by the boundary's own decision about who may perform the operation, not by any step. They are present in every one of the subdomain's ten operations and are unaffected by what the operation does. Restating what an operation needs cannot reach them. | S1 system_beliefs #4 |
| The details a correction changes are supplied together, as the changed fields. | VERIFIED | The correction's steps read the changed details as one supplied thing, and read the record they belong to by its identity. Removing the title, the author and the publication year removes nothing a step reads. | S1 system_beliefs #5 |
| Both failures break the library's own end-to-end exercise of the catalog. | VERIFIED | Run against the pinned composition, the exercise stops at the second edition: the 1984 edition of the work being registered is absent from the catalog when the exercise looks for it. The first defect refuses it at the boundary, so the correction is never reached. | S1 known_facts #10 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Admits a request to register a further edition | book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | States the eleven things such a request must supply, and turns away a request that does not supply them. | MISMATCH | States the publication year as a word. Turns away every request that supplies it the way the catalog holds it. |
| Registers a further edition | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | Registers a further edition of a work already carried, reading all eleven things supplied. | EXACT | Nothing. It uses everything its boundary requires; only the form of one requirement is wrong. |
| Admits a request to correct bibliographic information | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | States the eight things such a request must supply. | MISMATCH | Requires the title, the author and the publication year, which no step of the correction reads. Turns away a correction that does not resupply them. |
| Corrects bibliographic information | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Changes the details of a held record, reading the record named and the details being changed. | EXACT | Nothing. It is the boundary above it that is wrong. |
| Admits a request to register a work | book_library_mgmt::IN_REGISTER_BOOK_V0 | States the ten things such a request must supply. | PARTIAL | Does not require the subject, which its workflow reads. Admits a request the operation cannot then carry out. |
| Registers a work | book_library_mgmt::WF_REGISTER_BOOK_V0 | Registers a work, its first edition and a copy, reading eleven things supplied. | EXACT | Nothing; it reads one thing its boundary does not require. |
| Holds what the catalog knows | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | Declares the six stores the catalog owns and the paths they occupy. | MISMATCH | Declares no form for any detail it holds, so it cannot settle whether a publication year is a number. The description of a book is supplied with each request rather than declared once. |

---

## 5. Gaps

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Registering a further edition states the publication year in a form the catalog does not hold it in. | HIGH | Every correct request is turned away. The library's own exercise of the catalog stops here and never reaches the second defect. | VERIFIED | S1 requested_outcomes #1 |
| Correcting bibliographic information requires three details no step reads. | HIGH | A correction that does not restate the fields it leaves alone is turned away, which is every correction. | VERIFIED | S1 requested_outcomes #2 |
| Registering a work reads a detail its boundary does not require. | MEDIUM | The boundary admits a request with no subject that the operation then cannot carry out, so a declaration gap surfaces as a failure part-way through rather than as a refusal before anything happened. Whether any caller supplies the detail where the operation reads it was not established here. | VERIFIED | S1 system_beliefs #3 |
| Nothing compares what an operation requires against what it uses. | MEDIUM | All three defects were introduced without anything objecting, and stood undetected for as long as the boundary admitted everything. | VERIFIED | S1 known_facts #12 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The subdomain's operations are otherwise exact. | Seven of the ten operations require precisely what their steps read, name for name. The defects are three, not a pattern across the subdomain. | VERIFIED | S1 system_beliefs #3 |
| The two defects are opposite in shape and were invisible for the same reason. | One boundary requires more than its operation reads; another requires less. Both are a disagreement between two statements of one fact, and neither is visible from either statement alone. | VERIFIED | S1 known_facts #8 |
| Who may perform an operation is declared uniformly and is untouched by this. | The same three things appear in all ten operations and are consumed by the boundary rather than by any step. They are constant across operations that read nothing else in common. | VERIFIED | S1 out_of_scope #1 |
| A form mismatch and a name mismatch are not found by the same means. | Comparing names against what the steps read finds two of the three defects and cannot see the third. The publication year's form is wrong while its name is required and read, which no name-level comparison distinguishes. | VERIFIED | S1 known_facts #1 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The defect discovered in registering a work is outside what Stage 1 scoped. | Stage 1 named two operations and stated that no other asks for something it does not use. Discovery confirmed that and found a third operation with the opposite defect. It is in the same subdomain, of the same kind, and the change would be incomplete without it. | MEDIUM | VERIFIED | S1 system_beliefs #3 |
| The form of a detail the catalog holds is declared nowhere the catalog owns. | The store declares paths and no forms. The publication year's form is stated at three boundaries and in a description supplied with each request, and those four statements are the only ones there are. Three say number and one says word, and nothing compares them. The same disagreement could arise for any other detail. | MEDIUM | VERIFIED | S1 known_facts #1 |
| Whether the defects are confined to this domain is not established. | Ten operations of this subdomain were compared. The same comparison across the whole composition reports findings in other domains, which are those domains' business and were not examined here. | LOW | INSUFFICIENT_EVIDENCE | S1 out_of_scope #3 |

---

## 8. Open Questions

<!-- register:open_questions business_language -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Does registering a work belong in this change, or in its own? | SCOPE | Discovery found a third defect in the same subdomain, of the opposite shape, that Stage 1 did not name. It is one requirement added rather than removed, which Stage 1 explicitly ruled out: no operation gains a requirement in this change. Either the constraint is relaxed for this one, or the defect is raised separately. | S1 constraints #5 |
