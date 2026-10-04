# Stage 3 — Analysis Loop: book_library_mgmt / catalog

**Stage:** 3 — Analysis Loop

**CR:** cr_05_catalog

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: where each of the catalog's rules is held, and what the
catalog checks against what it records. Every act and every gate was read, not only those the change
request names, because the catalog's rules reach every one of them.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | Every act confirms its staff against rules the request hands it, and the rules every caller sends are the library's: the credentials name a staff member, and they are authorized. Written in the confirming contract, the rules hold for every act that composes it, and no request can widen them. | The confirming contract holds the rules as a literal. The ten acts stop binding them, and the ten gates stop requiring them. | OBSERVED | HIGH | CLOSED | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 is composed by all ten acts in force; every caller in the library's exercise sends `staff_id not_null` and `authorized eq true`; run directly with no rules, unauthorized staff registered a book |
| Q2 | Four checks report and nothing acts on the report. A rule step requiring the violations to be empty, following each check, turns each report into a refusal, as identity and another domain already do. | The submission check, the book record, the edition record and the correction each refuse on what their check finds. The platform check stays a reporter, as ruled for v5. | OBSERVED | HIGH | CLOSED | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 publish violations nothing reads; blockchain::CC_VALIDATE_REGISTRATION_V0 follows the same check with a rule requiring none |
| Q3 | The descriptions a book, a work and a further edition are checked against are fixed values of the library's, and can be written where they are used. The book description is its title, author and year as text, text and a number, and its subject as a list; a further edition is described as a book is; a work names its title and author. | The contracts that check hold their descriptions as literals; the two registration acts stop binding them and their gates stop requiring them. The malformed work description the register act wrote is replaced by the contract's own. | OBSERVED | HIGH | CLOSED | Every caller in the library's exercise sends the same book description; book_library_mgmt::WF_REGISTER_BOOK_V0 writes `work_schema` as `required: [title, author]`, which capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 reads as no requirement at all |
| Q4 | The submission check reads the book details the request supplies beside the book; the registration records a book the act builds from the request's own fields. Checking the book the act builds — the one it records — makes what is checked what is recorded. | Each registration act hands its submission check the record it will write, not the supplied copy. | OBSERVED | HIGH | CLOSED | book_library_mgmt::WF_REGISTER_BOOK_V0 binds the check's `book_fields` from the payload and the record's from the request's top-level fields; book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 does the same with `edition_fields` and `work_fields` |
| Q5 | The book the register act records reads its subject where no caller sends it, so every book registered through the library's exercise is recorded without one. Callers send the subject inside the book details they supply. | The register act records the subject from the supplied book details, as the author answered. Checked as recorded, every present registration passes. | OBSERVED | HIGH | CLOSED | book_library_mgmt::WF_REGISTER_BOOK_V0 binds `subject` from `$.payload.subject`; the library's exercise sends it only in `book_fields.subject`; cr_04_catalog P3 Q1 recorded the same and set it aside |
| Q6 | A copy is recorded in the state the request gives it, in both acts that register copies, because the copy contract assembles its state from the request. | The copy contract writes the state REGISTERED as its own value. | OBSERVED | HIGH | CLOSED | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 is composed by book_library_mgmt::WF_REGISTER_BOOK_V0 and book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0; run directly, a copy registered RETIRED is held retired |
| Q7 | A correction writes the state the request gives it and is checked against no description, so it can set a state the library does not have or leave a book with no subject. | The correction writes the state the record already has, and checks the corrected record against the book description, refusing a record without a subject. | OBSERVED | HIGH | CLOSED | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 assembles `state` from `updated_fields.state`; run directly, a correction set SUSPENDED and an empty subject; the author answered both |
| Q8 | Every gate in force requires the authorization rules, and two require descriptions and supplied copies no act will read. A gate that requires what no act reads refuses a request for lacking something nobody uses. | The ten gates stop requiring the rules; the book gate stops requiring the description; the edition gate stops requiring its descriptions and its supplied edition and work details. What every act does read stays required. | OBSERVED | HIGH | CLOSED | The ten intents in force each require `authorization_rules`; book_library_mgmt::IN_REGISTER_BOOK_V0 requires `book_schema`; book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 requires `edition_schema`, `work_schema`, `edition_fields` and `work_fields` |
| Q9 | The credentials a request presents are its own. Holding the rules stops a request from widening them; a request presenting credentials that say it is authorized is still admitted. | Recorded and carried; who a caller is lies outside this change. | OBSERVED | HIGH | CLOSED | S1 out_of_scope #1 |
| Q10 | Records made under a request's own rules stay as they were made, including every book recorded without a subject. | No repair, no backfill. | OBSERVED | HIGH | CLOSED | S1 constraints #2 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| Every catalog operation confirms the person performing it is authorized, against rules the request supplies. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 and Q8 |
| The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds. | S2 belief_verification #2 | CONFIRMED | Resolved in Q2 |
| The catalog checks a copy of the book supplied beside it, not the book it records. | S2 belief_verification #3 | CONFIRMED | Resolved in Q4 and Q5 |
| The descriptions a book, a work and a further edition are checked against come from the request. | S2 belief_verification #4 | CONFIRMED | Resolved in Q3 and Q8 |
| A physical copy is registered in whatever state the request gives it. | S2 belief_verification #5 | CONFIRMED | Resolved in Q6 |
| The catalog holds none of its own rules; each comes with the request it judges. | S2 gaps #1 | CONFIRMED | Resolved in Q1 through Q3 |
| A registration the catalog finds incomplete is registered anyway. | S2 gaps #2 | CONFIRMED | Resolved in Q2 |
| What the catalog checks is not what it records. | S2 gaps #3 | CONFIRMED | Resolved in Q4 and Q5 |
| A copy is registered in the state the request gives. | S2 gaps #4 | CONFIRMED | Resolved in Q6 |
| A correction writes the state the request gives. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q7, per the author's answer |
| A correction is not checked against what a book must contain. | S2 discovery_concerns #2 | CONFIRMED | Resolved in Q7, per the author's answer |
| The register act's work description checks nothing. | S2 discovery_concerns #3 | CONFIRMED | Resolved in Q3 |
| The book's recorded subject is read where no caller sends it. | S2 discovery_concerns #4 | CONFIRMED | Resolved in Q5, per the author's answer |
| The credentials a request presents are its own. | S2 discovery_concerns #5 | CONFIRMED | Carried in Q9; outside this change |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| Checking a record's structure | Platform transform | REUSE | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, unchanged |
| Refusing on a list of rules | Platform transform | REUSE | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, unchanged |
| Assembling a record from fields | Platform transform | REUSE | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, unchanged |
| Confirming staff | Capability contract | EXTEND | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 holds its rules |
| Checking a submission | Capability contract | EXTEND | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 holds its descriptions and refuses on violations |
| Recording a book | Capability contract | EXTEND | book_library_mgmt::CC_REGISTER_BOOK_V0 holds its description and refuses on violations |
| Recording an edition | Capability contract | EXTEND | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 holds its description and refuses on violations |
| Recording a copy | Capability contract | EXTEND | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 writes its state itself |
| Correcting a record | Capability contract | EXTEND | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 keeps the state and checks the corrected record |
| The ten acts | Workflows | EXTEND | Every act in force stops binding the rules; the two registration acts check what they record and the register act records the supplied subject |
| The ten gates | Intents | EXTEND | Every gate in force stops requiring the rules, and the two registration gates what no act reads |
| The superseded correction | Workflow and intent | EXISTING | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 and its intent are superseded and not in force; unchanged |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Amended — holds its rules | 22 | si.topology.impact impacted_count 22 |
| book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | Amended — holds its descriptions, refuses on violations | 23 | si.topology.impact impacted_count 23 |
| book_library_mgmt::CC_REGISTER_BOOK_V0 | Amended — holds its description, refuses on violations | 28 | si.topology.impact impacted_count 28 |
| book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | Amended — holds its description, refuses on violations | 27 | si.topology.impact impacted_count 27 |
| book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | Amended — writes the state itself | 29 | si.topology.impact impacted_count 29 |
| book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Amended — keeps the state, checks the corrected record | 24 | si.topology.impact impacted_count 24 |
| book_library_mgmt::WF_REGISTER_BOOK_V0 | Amended — stops binding rules, checks and records the supplied subject | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | Amended — stops binding rules, checks what it records | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | Amended — stops binding rules | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | Amended — stops binding rules | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | Amended — stops binding rules | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 | Amended — stops binding rules | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | Amended — stops binding rules | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0 | Amended — stops binding rules | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0 | Amended — stops binding rules | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::WF_SEARCH_CATALOG_V0 | Amended — stops binding rules | 0 | si.topology.impact impacted_count 0 |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | Amended — stops requiring rules and description | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | Amended — stops requiring rules, descriptions and supplied details | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0 | Amended — stops requiring rules | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | Amended — stops requiring rules | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0 | Amended — stops requiring rules | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 | Amended — stops requiring rules | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0 | Amended — stops requiring rules | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 | Amended — stops requiring rules | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0 | Amended — stops requiring rules | 1 | si.topology.impact impacted_count 1 |
| book_library_mgmt::IN_SEARCH_CATALOG_V0 | Amended — stops requiring rules | 1 | si.topology.impact impacted_count 1 |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Refuse anyone the library has not authorized | EXTEND | The confirming step holds the library's rules, so every act that composes it holds them. | Holding the rules in each act was checked and rejected: ten acts would carry ten copies of one rule. | S3 analysis_findings Q1 |
| Refuse a registration the catalog finds incomplete | EXTEND | A rule following each check refuses when it found anything, as identity does. | Making the platform check refuse was rejected by ruling: a check that decides can no longer be used only to report. | S3 analysis_findings Q2 |
| Hold what a book, a work and a further edition must contain | EXTEND | The checking contracts hold their descriptions as literals. | Holding them in the acts was checked and rejected: the descriptions belong to the checks, and both registration acts compose the same submission check. | S3 analysis_findings Q3 |
| Check what the catalog records | EXTEND | Each registration act hands its check the record it writes. | Checking the supplied copy as well was checked and rejected: a second check of the wrong thing adds nothing. | S3 analysis_findings Q4 |
| Record the subject callers supply | EXTEND | The register act reads the subject where callers send it. | Requiring it at the top level was rejected by the author: every present caller would change. | S3 analysis_findings Q5 |
| Register a copy as registered | EXTEND | The copy contract writes the state itself, for both acts that register copies. | Checking the requested state was rejected: there is one state a copy is registered in, so there is nothing to check, only something to write. | S3 analysis_findings Q6 |
| Keep a corrected record's state, and check it against the book description | EXTEND | The correction writes the state the record has, and refuses a corrected record that fails the book description or has no subject. | Refusing a correction that names a state was checked and rejected: a request's extra words are ignored, not refused. | S3 analysis_findings Q7 |
| Admit a request without the rules the catalog holds | EXTEND | Every gate stops requiring the rules, and the registration gates what no act reads. | Leaving the gates as they are was checked and rejected: a gate requiring what nothing reads refuses a correct request for its absence. | S3 analysis_findings Q8 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | catalog | Every rule held here is the catalog's own, and every step that changes belongs to the catalog. Nothing moves and no other subdomain changes. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The one CRITICAL gap resolves to a committed decision: the confirming step holds the library's rules |
| No open analyst questions | SATISFIED | All ten findings are CLOSED. The three questions Stage 2 raised were answered by the business author |
| No dependency expansion in the last pass | SATISFIED | A second pass read every act and every gate in force, not only those the change request names, and added the gates' unread requirements; a third pass over what each act writes found nothing further |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All fourteen items re-grounded and CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED; five were established by running the acts against the pinned composition |
