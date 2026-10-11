# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 2 — Domain Model Verification
  CR: cr_05_catalog
  Status: DRAFT
  Feeds: Stage 3 — Analysis Loop
registers:
  entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Evidence Status
    - Source Finding
    rows:
    - Entity: The Book
      Description: 'What the library records about a book: its title, author, publication year, subject and state.'
      Store Model: One keyed store, one record per book, unchanged by this change.
      Evidence Status: OBSERVED
      Source Finding: 'S1 known_facts #3'
    - Entity: The Physical Copy
      Description: One copy of a book on the library's shelves, and its state.
      Store Model: One keyed store, one record per barcode, unchanged by this change.
      Evidence Status: OBSERVED
      Source Finding: 'S1 lifecycle_states #1'
    - Entity: The Staff Credentials
      Description: What a request presents about the person performing it.
      Store Model: Carried by each request; the catalog stores none.
      Evidence Status: OBSERVED
      Source Finding: 'S1 business_vocabulary #2'
    - Entity: The Catalog's Rules
      Description: Who may perform a catalog operation, and what a book, a work and a further edition must contain.
      Store Model: Held nowhere in the catalog today. Each travels with the request that is judged by it.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #1'
  entity_attributes:
    columns:
    - Entity
    - Attribute
    - Meaning
    - Evidence Status
    - Source Finding
    rows:
    - Entity: The Book
      Attribute: Title
      Meaning: Part of what identifies a book. Required.
      Evidence Status: OBSERVED
      Source Finding: 'S1 known_facts #3'
    - Entity: The Book
      Attribute: Author
      Meaning: Part of what identifies a book. Required.
      Evidence Status: OBSERVED
      Source Finding: 'S1 known_facts #3'
    - Entity: The Book
      Attribute: Publication Year
      Meaning: Part of what identifies a book, recorded as a number. Required.
      Evidence Status: OBSERVED
      Source Finding: 'S1 known_facts #5'
    - Entity: The Book
      Attribute: Subject
      Meaning: What kind of book it is. At least one.
      Evidence Status: OBSERVED
      Source Finding: 'S1 known_facts #4'
    - Entity: The Physical Copy
      Attribute: State
      Meaning: Registered or retired.
      Evidence Status: OBSERVED
      Source Finding: 'S1 lifecycle_states #1'
  business_processes:
    columns:
    - Process
    - Initiator
    - Outcome
    - Evidence Status
    - Source Finding
    rows:
    - Process: Perform any catalog operation
      Initiator: Authorized staff
      Outcome: The operation proceeds for authorized staff; anyone else is refused.
      Evidence Status: OBSERVED
      Source Finding: 'S1 requested_outcomes #1'
    - Process: Register a book, a further edition or a copy
      Initiator: Authorized staff
      Outcome: A complete registration is recorded; an incomplete one is refused.
      Evidence Status: OBSERVED
      Source Finding: 'S1 requested_outcomes #2'
  process_steps:
    columns:
    - Process
    - 'Step #'
    - Action
    - Record Produced
    - Evidence Status
    - Source Finding
    rows:
    - Process: Perform any catalog operation
      'Step #': '1'
      Action: Confirm the person performing it is authorized staff.
      Record Produced: None.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #1'
    - Process: Register a book, a further edition or a copy
      'Step #': '1'
      Action: Check the registration against what it must contain.
      Record Produced: None.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Process: Register a book, a further edition or a copy
      'Step #': '2'
      Action: Record the book, the edition or the copy, and record that it happened.
      Record Produced: The record, and a moment on the operation trail.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
  belief_verification:
    columns:
    - Belief
    - Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE)
    - Evidence
    - Source Finding
    rows:
    - Belief: Every catalog operation confirms the person performing it is authorized, against rules the request supplies.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: 'All ten catalog acts in force bind `authorization_rules` from the payload into book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, whose one step judges the request''s `staff_credentials` against them, and each act''s gate requires the field. Run directly: staff presenting `authorized: false` are refused under the library''s rules and registered a book when the request sent an empty list of rules. That book is held like any other.'
      Source Finding: 'S1 system_beliefs #1'
    - Belief: The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: 'book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 run capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and publish its violations; nothing reads them. The submission check''s only refusal is a rule on the barcode and the supplied subject. Run directly: a book whose supplied details lacked everything but a title was registered.'
      Source Finding: 'S1 system_beliefs #2'
    - Belief: The catalog checks a copy of the book supplied beside it, not the book it records.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: The submission check reads `book_fields` from the payload. The act records a book built from the request's top-level title, author, year and subject. Every caller sends the subject inside `book_fields` and never at the top level, so every book registered through the library's own exercise is recorded with no subject — the defect cr_04_catalog found and set aside.
      Source Finding: 'S1 system_beliefs #3'
    - Belief: The descriptions a book, a work and a further edition are checked against come from the request.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: 'book_library_mgmt::WF_REGISTER_BOOK_V0 binds `book_schema`, and book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 binds `edition_schema` and `work_schema`, from the payload; both gates require them. The register act writes its work description as a literal, but in a shape the structure check does not read, so it checks nothing. Run directly: an empty `book_schema` let an incomplete book through.'
      Source Finding: 'S1 system_beliefs #4'
    - Belief: A physical copy is registered in whatever state the request gives it.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: 'book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 assembles the copy''s `state` from the request''s `copy_fields`. Run directly: a copy registered with the state RETIRED is held retired.'
      Source Finding: 'S1 system_beliefs #5'
  pps_baseline_fqdns:
    columns:
    - Capability
    - FQDN
    - What It Does
    - Fit (EXACT, PARTIAL, MISMATCH)
    - Cannot Do
    rows:
    - Capability: Confirming staff are authorized
      FQDN: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      What It Does: Judges the request's staff credentials against a list of rules.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It holds no rule of its own; the rules come from the request.
    - Capability: Checking a book submission
      FQDN: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      What It Does: Checks supplied book and work details against descriptions, and refuses a blank barcode or an empty supplied subject.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It refuses nothing its checks find, checks the supplied copy rather than the recorded book, and takes its descriptions from the request.
    - Capability: Recording a book
      FQDN: book_library_mgmt::CC_REGISTER_BOOK_V0
      What It Does: Checks the book against a description, then records it.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It ignores what its check finds and takes the description from the request.
    - Capability: Recording a further edition
      FQDN: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      What It Does: Checks the edition against a description, then records it.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It ignores what its check finds and takes the description from the request.
    - Capability: Recording a copy
      FQDN: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      What It Does: Records a copy of a registered book.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It records the copy in whatever state the request gives.
    - Capability: Correcting a record
      FQDN: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      What It Does: Refuses a correction that would change a book's identity, then writes the corrected record.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It writes the state the request gives, and checks the corrected record against no description.
    - Capability: Book registration act
      FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      What It Does: Confirms staff, checks, claims identities and barcode, records book and copy, and records the operation.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules and the description from the request, and reads the subject where no caller sends it.
    - Capability: Edition registration act
      FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      What It Does: Confirms staff, checks, resolves the work and records the edition.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules and both descriptions from the request.
    - Capability: Copy registration act
      FQDN: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      What It Does: Confirms staff, claims the barcode and records the copy.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules from the request.
    - Capability: Correction act
      FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      What It Does: Confirms staff, resolves the book and writes the correction.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules from the request.
    - Capability: Book retirement act
      FQDN: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      What It Does: Confirms staff and retires a book record.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules from the request.
    - Capability: Book reinstatement act
      FQDN: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      What It Does: Confirms staff and reinstates a book record.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules from the request.
    - Capability: Copy retirement act
      FQDN: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      What It Does: Confirms staff and retires a copy.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules from the request.
    - Capability: Copy reinstatement act
      FQDN: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      What It Does: Confirms staff and reinstates a copy.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules from the request.
    - Capability: Retrieval act
      FQDN: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      What It Does: Confirms staff and returns a book's details.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules from the request.
    - Capability: Search act
      FQDN: book_library_mgmt::WF_SEARCH_CATALOG_V0
      What It Does: Confirms staff and searches the catalog.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It binds the rules from the request.
    - Capability: Rule check
      FQDN: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
      What It Does: Refuses parameters that fail a given list of rules.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing; it can refuse on a check's violations, as another domain already does.
    - Capability: Structure check
      FQDN: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
      What It Does: Reports every way a record fails a description.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It reports and never refuses. Refusing on what it reports is the calling contract's business (ruled for v5).
    - Capability: Holding the rules in the contract
      FQDN: blockchain::CC_VALIDATE_REGISTRATION_V0
      What It Does: Holds its description as a literal and refuses on what its check finds.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing; it is the precedent this change follows.
  gaps:
    columns:
    - Gap
    - Severity
    - Impact
    - Evidence Status
    - Source Finding
    rows:
    - Gap: The catalog holds none of its own rules; each comes with the request it judges.
      Severity: CRITICAL
      Impact: Anyone can perform any catalog operation by sending no rules.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #1'
    - Gap: A registration the catalog finds incomplete is registered anyway.
      Severity: MAJOR
      Impact: A book can be held without what the library says it must contain.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #2'
    - Gap: What the catalog checks is not what it records.
      Severity: MAJOR
      Impact: Every registered book is recorded without its subject, and a check that refused would judge the wrong thing.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Gap: A copy is registered in the state the request gives.
      Severity: MINOR
      Impact: A copy can enter the catalog already retired.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #5'
  architectural_observations:
    columns:
    - Observation
    - Evidence
    - Evidence Status
    - Source Finding
    rows:
    - Observation: The catalog has no entrance that supplies its rules, so every caller states them.
      Evidence: No transport ingress targets a catalog act; the library's own exercise supplies the rules in every request.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #1'
    - Observation: Identity closed the same hole by holding its rules in the contracts that apply them.
      Evidence: blockchain::CC_VALIDATE_REGISTRATION_V0 holds its description and refuses on its violations.
      Evidence Status: OBSERVED
      Source Finding: 'S2 pps_baseline_fqdns #19'
    - Observation: The gates require the rule fields, so holding the rules in the catalog changes every gate.
      Evidence: Each of the ten gates in force requires `authorization_rules`; two also require descriptions.
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #4'
  discovery_concerns:
    columns:
    - Concern
    - Evidence
    - Severity
    - Evidence Status
    - Source Finding
    rows:
    - Concern: A correction writes the state the request gives.
      Evidence: 'Run directly: a correction set a registered book to SUSPENDED, a state the library does not have, bypassing retirement and reinstatement. Put to the business author, who answered that a correction keeps the record''s state.'
      Severity: MAJOR
      Evidence Status: OBSERVED
      Source Finding: 'S2 pps_baseline_fqdns #6'
    - Concern: A correction is not checked against what a book must contain.
      Evidence: 'Run directly: a correction left a book with no subject. Put to the business author, who answered that a corrected record meets the book description.'
      Severity: MAJOR
      Evidence Status: OBSERVED
      Source Finding: 'S2 pps_baseline_fqdns #6'
    - Concern: The register act's work description checks nothing.
      Evidence: It is written as a list of required names, a shape the structure check does not read, so every work passes. Covered by the catalog holding what a work must contain.
      Severity: MINOR
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #4'
    - Concern: The book's recorded subject is read where no caller sends it.
      Evidence: Put to the business author, who answered that the act records the subject where callers send it, inside the book's supplied details.
      Severity: MAJOR
      Evidence Status: OBSERVED
      Source Finding: 'S2 belief_verification #3'
    - Concern: The credentials a request presents are its own.
      Evidence: 'Holding the rules closes rule-widening; a caller presenting `authorized: true` is still admitted. Who a caller is lies outside this change.'
      Severity: MAJOR
      Evidence Status: OBSERVED
      Source Finding: 'S1 out_of_scope #1'
  open_questions:
    columns:
    - Question
    - Category
    - Why It Matters
    - Source Finding
    rows: []
```

Every belief the change request declared is resolved against the pinned composition. What is
verified here is where each of the catalog's rules is read from, and what the catalog does with what
its checks find. The catalog has no transport entrance: every caller invokes its acts directly, so
each belief about behaviour was established by running the acts directly against the pinned
composition, on a scratch data root, as any caller would.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
