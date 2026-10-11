# Stage 3 — Analysis Loop: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 3 — Analysis Loop
  CR: cr_05_catalog
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
    - Question Id: Q1
      Finding: 'Every act confirms its staff against rules the request hands it, and the rules every caller sends are the library''s: the credentials name a staff member, and they are authorized. Written in the confirming contract, the rules hold for every act that composes it, and no request can widen them.'
      Impact: The confirming contract holds the rules as a literal. The ten acts stop binding them, and the ten gates stop requiring them.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 is composed by all ten acts in force; every caller in the library's exercise sends `staff_id not_null` and `authorized eq true`; run directly with no rules, unauthorized staff registered a book
    - Question Id: Q2
      Finding: Four checks report and nothing acts on the report. A rule step requiring the violations to be empty, following each check, turns each report into a refusal, as identity and another domain already do.
      Impact: The submission check, the book record, the edition record and the correction each refuse on what their check finds. The platform check stays a reporter, as ruled for v5.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 publish violations nothing reads; blockchain::CC_VALIDATE_REGISTRATION_V0 follows the same check with a rule requiring none
    - Question Id: Q3
      Finding: The descriptions a book, a work and a further edition are checked against are fixed values of the library's, and can be written where they are used. The book description is its title, author and year as text, text and a number, and its subject as a list; a further edition is described as a book is; a work names its title and author.
      Impact: The contracts that check hold their descriptions as literals; the two registration acts stop binding them and their gates stop requiring them. The malformed work description the register act wrote is replaced by the contract's own.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: 'Every caller in the library''s exercise sends the same book description; book_library_mgmt::WF_REGISTER_BOOK_V0 writes `work_schema` as `required: [title, author]`, which capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 reads as no requirement at all'
    - Question Id: Q4
      Finding: The submission check reads the book details the request supplies beside the book; the registration records a book the act builds from the request's own fields. Checking the book the act builds — the one it records — makes what is checked what is recorded.
      Impact: Each registration act hands its submission check the record it will write, not the supplied copy.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::WF_REGISTER_BOOK_V0 binds the check's `book_fields` from the payload and the record's from the request's top-level fields; book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 does the same with `edition_fields` and `work_fields`
    - Question Id: Q5
      Finding: The book the register act records reads its subject where no caller sends it, so every book registered through the library's exercise is recorded without one. Callers send the subject inside the book details they supply.
      Impact: The register act records the subject from the supplied book details, as the author answered. Checked as recorded, every present registration passes.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::WF_REGISTER_BOOK_V0 binds `subject` from `$.payload.subject`; the library's exercise sends it only in `book_fields.subject`; cr_04_catalog P3 Q1 recorded the same and set it aside
    - Question Id: Q6
      Finding: A copy is recorded in the state the request gives it, in both acts that register copies, because the copy contract assembles its state from the request.
      Impact: The copy contract writes the state REGISTERED as its own value.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 is composed by book_library_mgmt::WF_REGISTER_BOOK_V0 and book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0; run directly, a copy registered RETIRED is held retired
    - Question Id: Q7
      Finding: A correction writes the state the request gives it and is checked against no description, so it can set a state the library does not have or leave a book with no subject.
      Impact: The correction writes the state the record already has, and checks the corrected record against the book description, refusing a record without a subject.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 assembles `state` from `updated_fields.state`; run directly, a correction set SUSPENDED and an empty subject; the author answered both
    - Question Id: Q8
      Finding: Every gate in force requires the authorization rules, and two require descriptions and supplied copies no act will read. A gate that requires what no act reads refuses a request for lacking something nobody uses.
      Impact: The ten gates stop requiring the rules; the book gate stops requiring the description; the edition gate stops requiring its descriptions and its supplied edition and work details. What every act does read stays required.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: The ten intents in force each require `authorization_rules`; book_library_mgmt::IN_REGISTER_BOOK_V0 requires `book_schema`; book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 requires `edition_schema`, `work_schema`, `edition_fields` and `work_fields`
    - Question Id: Q9
      Finding: The credentials a request presents are its own. Holding the rules stops a request from widening them; a request presenting credentials that say it is authorized is still admitted.
      Impact: Recorded and carried; who a caller is lies outside this change.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: 'S1 out_of_scope #1'
    - Question Id: Q10
      Finding: Records made under a request's own rules stay as they were made, including every book recorded without a subject.
      Impact: No repair, no backfill.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: 'S1 constraints #2'
  verification_results:
    columns:
    - Item
    - Origin
    - Result (CONFIRMED, OVERTURNED)
    - Evidence
    rows:
    - Item: Every catalog operation confirms the person performing it is authorized, against rules the request supplies.
      Origin: 'S2 belief_verification #1'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q1 and Q8
    - Item: The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds.
      Origin: 'S2 belief_verification #2'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q2
    - Item: The catalog checks a copy of the book supplied beside it, not the book it records.
      Origin: 'S2 belief_verification #3'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q4 and Q5
    - Item: The descriptions a book, a work and a further edition are checked against come from the request.
      Origin: 'S2 belief_verification #4'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q3 and Q8
    - Item: A physical copy is registered in whatever state the request gives it.
      Origin: 'S2 belief_verification #5'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q6
    - Item: The catalog holds none of its own rules; each comes with the request it judges.
      Origin: 'S2 gaps #1'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q1 through Q3
    - Item: A registration the catalog finds incomplete is registered anyway.
      Origin: 'S2 gaps #2'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q2
    - Item: What the catalog checks is not what it records.
      Origin: 'S2 gaps #3'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q4 and Q5
    - Item: A copy is registered in the state the request gives.
      Origin: 'S2 gaps #4'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q6
    - Item: A correction writes the state the request gives.
      Origin: 'S2 discovery_concerns #1'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q7, per the author's answer
    - Item: A correction is not checked against what a book must contain.
      Origin: 'S2 discovery_concerns #2'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q7, per the author's answer
    - Item: The register act's work description checks nothing.
      Origin: 'S2 discovery_concerns #3'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q3
    - Item: The book's recorded subject is read where no caller sends it.
      Origin: 'S2 discovery_concerns #4'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Resolved in Q5, per the author's answer
    - Item: The credentials a request presents are its own.
      Origin: 'S2 discovery_concerns #5'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Carried in Q9; outside this change
  dependency_discoveries:
    columns:
    - Dependency
    - Type
    - Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE)
    - Evidence
    rows:
    - Dependency: Checking a record's structure
      Type: Platform transform
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, unchanged
    - Dependency: Refusing on a list of rules
      Type: Platform transform
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, unchanged
    - Dependency: Assembling a record from fields
      Type: Platform transform
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, unchanged
    - Dependency: Confirming staff
      Type: Capability contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXTEND
      Evidence: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 holds its rules
    - Dependency: Checking a submission
      Type: Capability contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXTEND
      Evidence: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 holds its descriptions and refuses on violations
    - Dependency: Recording a book
      Type: Capability contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXTEND
      Evidence: book_library_mgmt::CC_REGISTER_BOOK_V0 holds its description and refuses on violations
    - Dependency: Recording an edition
      Type: Capability contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXTEND
      Evidence: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 holds its description and refuses on violations
    - Dependency: Recording a copy
      Type: Capability contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXTEND
      Evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 writes its state itself
    - Dependency: Correcting a record
      Type: Capability contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXTEND
      Evidence: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 keeps the state and checks the corrected record
    - Dependency: The ten acts
      Type: Workflows
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXTEND
      Evidence: Every act in force stops binding the rules; the two registration acts check what they record and the register act records the supplied subject
    - Dependency: The ten gates
      Type: Intents
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXTEND
      Evidence: Every gate in force stops requiring the rules, and the two registration gates what no act reads
    - Dependency: The superseded correction
      Type: Workflow and intent
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 and its intent are superseded and not in force; unchanged
  impact_analysis:
    columns:
    - Artifact
    - Impact Scope
    - Consumer Count
    - Evidence
    rows:
    - Artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      Impact Scope: Amended — holds its rules
      Consumer Count: '22'
      Evidence: si.topology.impact impacted_count 22
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Impact Scope: Amended — holds its descriptions, refuses on violations
      Consumer Count: '23'
      Evidence: si.topology.impact impacted_count 23
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Impact Scope: Amended — holds its description, refuses on violations
      Consumer Count: '28'
      Evidence: si.topology.impact impacted_count 28
    - Artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      Impact Scope: Amended — holds its description, refuses on violations
      Consumer Count: '27'
      Evidence: si.topology.impact impacted_count 27
    - Artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      Impact Scope: Amended — writes the state itself
      Consumer Count: '29'
      Evidence: si.topology.impact impacted_count 29
    - Artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Impact Scope: Amended — keeps the state, checks the corrected record
      Consumer Count: '24'
      Evidence: si.topology.impact impacted_count 24
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Impact Scope: Amended — stops binding rules, checks and records the supplied subject
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Impact Scope: Amended — stops binding rules, checks what it records
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      Impact Scope: Amended — stops binding rules
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Impact Scope: Amended — stops binding rules
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      Impact Scope: Amended — stops binding rules
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      Impact Scope: Amended — stops binding rules
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      Impact Scope: Amended — stops binding rules
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      Impact Scope: Amended — stops binding rules
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Impact Scope: Amended — stops binding rules
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Impact Scope: Amended — stops binding rules
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Impact Scope: Amended — stops requiring rules and description
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Impact Scope: Amended — stops requiring rules, descriptions and supplied details
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
      Impact Scope: Amended — stops requiring rules
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Impact Scope: Amended — stops requiring rules
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
      Impact Scope: Amended — stops requiring rules
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
      Impact Scope: Amended — stops requiring rules
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
      Impact Scope: Amended — stops requiring rules
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
      Impact Scope: Amended — stops requiring rules
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Impact Scope: Amended — stops requiring rules
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Impact Scope: Amended — stops requiring rules
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1
  authoring_decisions:
    columns:
    - Capability
    - Decision (REUSE, EXTEND, AUTHOR_NEW)
    - Rationale
    - Alternatives Checked
    - Source Finding
    rows:
    - Capability: Refuse anyone the library has not authorized
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The confirming step holds the library's rules, so every act that composes it holds them.
      Alternatives Checked: 'Holding the rules in each act was checked and rejected: ten acts would carry ten copies of one rule.'
      Source Finding: S3 analysis_findings Q1
    - Capability: Refuse a registration the catalog finds incomplete
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: A rule following each check refuses when it found anything, as identity does.
      Alternatives Checked: 'Making the platform check refuse was rejected by ruling: a check that decides can no longer be used only to report.'
      Source Finding: S3 analysis_findings Q2
    - Capability: Hold what a book, a work and a further edition must contain
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The checking contracts hold their descriptions as literals.
      Alternatives Checked: 'Holding them in the acts was checked and rejected: the descriptions belong to the checks, and both registration acts compose the same submission check.'
      Source Finding: S3 analysis_findings Q3
    - Capability: Check what the catalog records
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: Each registration act hands its check the record it writes.
      Alternatives Checked: 'Checking the supplied copy as well was checked and rejected: a second check of the wrong thing adds nothing.'
      Source Finding: S3 analysis_findings Q4
    - Capability: Record the subject callers supply
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The register act reads the subject where callers send it.
      Alternatives Checked: 'Requiring it at the top level was rejected by the author: every present caller would change.'
      Source Finding: S3 analysis_findings Q5
    - Capability: Register a copy as registered
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The copy contract writes the state itself, for both acts that register copies.
      Alternatives Checked: 'Checking the requested state was rejected: there is one state a copy is registered in, so there is nothing to check, only something to write.'
      Source Finding: S3 analysis_findings Q6
    - Capability: Keep a corrected record's state, and check it against the book description
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The correction writes the state the record has, and refuses a corrected record that fails the book description or has no subject.
      Alternatives Checked: 'Refusing a correction that names a state was checked and rejected: a request''s extra words are ignored, not refused.'
      Source Finding: S3 analysis_findings Q7
    - Capability: Admit a request without the rules the catalog holds
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: Every gate stops requiring the rules, and the registration gates what no act reads.
      Alternatives Checked: 'Leaving the gates as they are was checked and rejected: a gate requiring what nothing reads refuses a correct request for its absence.'
      Source Finding: S3 analysis_findings Q8
  placement_decision:
    columns:
    - Decision (NEW_SUBDOMAIN, EXTEND)
    - Subdomain
    - Rationale
    - Source Finding
    rows:
    - Decision (NEW_SUBDOMAIN, EXTEND): EXTEND
      Subdomain: catalog
      Rationale: Every rule held here is the catalog's own, and every step that changes belongs to the catalog. Nothing moves and no other subdomain changes.
      Source Finding: S3 analysis_findings Q1
  saturation:
    columns:
    - Criterion
    - Status (SATISFIED, NOT_SATISFIED)
    - Evidence
    rows:
    - Criterion: No unresolved CRITICAL gaps
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: 'The one CRITICAL gap resolves to a committed decision: the confirming step holds the library''s rules'
    - Criterion: No open analyst questions
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: All ten findings are CLOSED. The three questions Stage 2 raised were answered by the business author
    - Criterion: No dependency expansion in the last pass
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: A second pass read every act and every gate in force, not only those the change request names, and added the gates' unread requirements; a third pass over what each act writes found nothing further
    - Criterion: Verification pass complete, no OVERTURNED item unresolved
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: All fourteen items re-grounded and CONFIRMED
    - Criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: Every finding is OBSERVED; five were established by running the acts against the pinned composition
```

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: where each of the catalog's rules is held, and what the
catalog checks against what it records. Every act and every gate was read, not only those the change
request names, because the catalog's rules reach every one of them.

---

## 1. Analysis Findings

## 2. Verification Results

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Placement Decision

## 7. Saturation Assessment
