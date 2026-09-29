# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

**Stage:** 2 — Domain Model Verification
**CR:** cr_05_catalog
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. What is
verified here is where each of the catalog's rules is read from, and what the catalog does with what
its checks find. The catalog has no transport entrance: every caller invokes its acts directly, so
each belief about behaviour was established by running the acts directly against the pinned
composition, on a scratch data root, as any caller would.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Book | What the library records about a book: its title, author, publication year, subject and state. | One keyed store, one record per book, unchanged by this change. | OBSERVED | S1 known_facts #3 |
| The Physical Copy | One copy of a book on the library's shelves, and its state. | One keyed store, one record per barcode, unchanged by this change. | OBSERVED | S1 lifecycle_states #1 |
| The Staff Credentials | What a request presents about the person performing it. | Carried by each request; the catalog stores none. | OBSERVED | S1 business_vocabulary #2 |
| The Catalog's Rules | Who may perform a catalog operation, and what a book, a work and a further edition must contain. | Held nowhere in the catalog today. Each travels with the request that is judged by it. | OBSERVED | S2 belief_verification #1 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Book | Title | Part of what identifies a book. Required. | OBSERVED | S1 known_facts #3 |
| The Book | Author | Part of what identifies a book. Required. | OBSERVED | S1 known_facts #3 |
| The Book | Publication Year | Part of what identifies a book, recorded as a number. Required. | OBSERVED | S1 known_facts #5 |
| The Book | Subject | What kind of book it is. At least one. | OBSERVED | S1 known_facts #4 |
| The Physical Copy | State | Registered or retired. | OBSERVED | S1 lifecycle_states #1 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Perform any catalog operation | Authorized staff | The operation proceeds for authorized staff; anyone else is refused. | OBSERVED | S1 requested_outcomes #1 |
| Register a book, a further edition or a copy | Authorized staff | A complete registration is recorded; an incomplete one is refused. | OBSERVED | S1 requested_outcomes #2 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Perform any catalog operation | 1 | Confirm the person performing it is authorized staff. | None. | OBSERVED | S2 belief_verification #1 |
| Register a book, a further edition or a copy | 1 | Check the registration against what it must contain. | None. | OBSERVED | S2 belief_verification #2 |
| Register a book, a further edition or a copy | 2 | Record the book, the edition or the copy, and record that it happened. | The record, and a moment on the operation trail. | OBSERVED | S2 belief_verification #3 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Every catalog operation confirms the person performing it is authorized, against rules the request supplies. | VERIFIED | All ten catalog acts in force bind `authorization_rules` from the payload into book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, whose one step judges the request's `staff_credentials` against them, and each act's gate requires the field. Run directly: staff presenting `authorized: false` are refused under the library's rules and registered a book when the request sent an empty list of rules. That book is held like any other. | S1 system_beliefs #1 |
| The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds. | VERIFIED | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 run capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and publish its violations; nothing reads them. The submission check's only refusal is a rule on the barcode and the supplied subject. Run directly: a book whose supplied details lacked everything but a title was registered. | S1 system_beliefs #2 |
| The catalog checks a copy of the book supplied beside it, not the book it records. | VERIFIED | The submission check reads `book_fields` from the payload. The act records a book built from the request's top-level title, author, year and subject. Every caller sends the subject inside `book_fields` and never at the top level, so every book registered through the library's own exercise is recorded with no subject — the defect cr_04_catalog found and set aside. | S1 system_beliefs #3 |
| The descriptions a book, a work and a further edition are checked against come from the request. | VERIFIED | book_library_mgmt::WF_REGISTER_BOOK_V0 binds `book_schema`, and book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 binds `edition_schema` and `work_schema`, from the payload; both gates require them. The register act writes its work description as a literal, but in a shape the structure check does not read, so it checks nothing. Run directly: an empty `book_schema` let an incomplete book through. | S1 system_beliefs #4 |
| A physical copy is registered in whatever state the request gives it. | VERIFIED | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 assembles the copy's `state` from the request's `copy_fields`. Run directly: a copy registered with the state RETIRED is held retired. | S1 system_beliefs #5 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Confirming staff are authorized | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Judges the request's staff credentials against a list of rules. | PARTIAL | It holds no rule of its own; the rules come from the request. |
| Checking a book submission | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | Checks supplied book and work details against descriptions, and refuses a blank barcode or an empty supplied subject. | PARTIAL | It refuses nothing its checks find, checks the supplied copy rather than the recorded book, and takes its descriptions from the request. |
| Recording a book | book_library_mgmt::CC_REGISTER_BOOK_V0 | Checks the book against a description, then records it. | PARTIAL | It ignores what its check finds and takes the description from the request. |
| Recording a further edition | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | Checks the edition against a description, then records it. | PARTIAL | It ignores what its check finds and takes the description from the request. |
| Recording a copy | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | Records a copy of a registered book. | PARTIAL | It records the copy in whatever state the request gives. |
| Correcting a record | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Refuses a correction that would change a book's identity, then writes the corrected record. | PARTIAL | It writes the state the request gives, and checks the corrected record against no description. |
| Book registration act | book_library_mgmt::WF_REGISTER_BOOK_V0 | Confirms staff, checks, claims identities and barcode, records book and copy, and records the operation. | PARTIAL | It binds the rules and the description from the request, and reads the subject where no caller sends it. |
| Edition registration act | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | Confirms staff, checks, resolves the work and records the edition. | PARTIAL | It binds the rules and both descriptions from the request. |
| Copy registration act | book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | Confirms staff, claims the barcode and records the copy. | PARTIAL | It binds the rules from the request. |
| Correction act | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | Confirms staff, resolves the book and writes the correction. | PARTIAL | It binds the rules from the request. |
| Book retirement act | book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | Confirms staff and retires a book record. | PARTIAL | It binds the rules from the request. |
| Book reinstatement act | book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | Confirms staff and reinstates a book record. | PARTIAL | It binds the rules from the request. |
| Copy retirement act | book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | Confirms staff and retires a copy. | PARTIAL | It binds the rules from the request. |
| Copy reinstatement act | book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | Confirms staff and reinstates a copy. | PARTIAL | It binds the rules from the request. |
| Retrieval act | book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | Confirms staff and returns a book's details. | PARTIAL | It binds the rules from the request. |
| Search act | book_library_mgmt::WF_SEARCH_CATALOG_V0 | Confirms staff and searches the catalog. | PARTIAL | It binds the rules from the request. |
| Rule check | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Refuses parameters that fail a given list of rules. | EXACT | Nothing; it can refuse on a check's violations, as another domain already does. |
| Structure check | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Reports every way a record fails a description. | PARTIAL | It reports and never refuses. Refusing on what it reports is the calling contract's business (ruled for v5). |
| Holding the rules in the contract | blockchain::CC_VALIDATE_REGISTRATION_V0 | Holds its description as a literal and refuses on what its check finds. | EXACT | Nothing; it is the precedent this change follows. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| The catalog holds none of its own rules; each comes with the request it judges. | CRITICAL | Anyone can perform any catalog operation by sending no rules. | OBSERVED | S2 belief_verification #1 |
| A registration the catalog finds incomplete is registered anyway. | MAJOR | A book can be held without what the library says it must contain. | OBSERVED | S2 belief_verification #2 |
| What the catalog checks is not what it records. | MAJOR | Every registered book is recorded without its subject, and a check that refused would judge the wrong thing. | OBSERVED | S2 belief_verification #3 |
| A copy is registered in the state the request gives. | MINOR | A copy can enter the catalog already retired. | OBSERVED | S2 belief_verification #5 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The catalog has no entrance that supplies its rules, so every caller states them. | No transport ingress targets a catalog act; the library's own exercise supplies the rules in every request. | OBSERVED | S2 belief_verification #1 |
| Identity closed the same hole by holding its rules in the contracts that apply them. | blockchain::CC_VALIDATE_REGISTRATION_V0 holds its description and refuses on its violations. | OBSERVED | S2 pps_baseline_fqdns #19 |
| The gates require the rule fields, so holding the rules in the catalog changes every gate. | Each of the ten gates in force requires `authorization_rules`; two also require descriptions. | OBSERVED | S2 belief_verification #4 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A correction writes the state the request gives. | Run directly: a correction set a registered book to SUSPENDED, a state the library does not have, bypassing retirement and reinstatement. Put to the business author, who answered that a correction keeps the record's state. | MAJOR | OBSERVED | S2 pps_baseline_fqdns #6 |
| A correction is not checked against what a book must contain. | Run directly: a correction left a book with no subject. Put to the business author, who answered that a corrected record meets the book description. | MAJOR | OBSERVED | S2 pps_baseline_fqdns #6 |
| The register act's work description checks nothing. | It is written as a list of required names, a shape the structure check does not read, so every work passes. Covered by the catalog holding what a work must contain. | MINOR | OBSERVED | S2 belief_verification #4 |
| The book's recorded subject is read where no caller sends it. | Put to the business author, who answered that the act records the subject where callers send it, inside the book's supplied details. | MAJOR | OBSERVED | S2 belief_verification #3 |
| The credentials a request presents are its own. | Holding the rules closes rule-widening; a caller presenting `authorized: true` is still admitted. Who a caller is lies outside this change. | MAJOR | OBSERVED | S1 out_of_scope #1 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
