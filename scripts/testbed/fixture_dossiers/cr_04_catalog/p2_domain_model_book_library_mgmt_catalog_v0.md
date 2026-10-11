# Stage 2 — Domain Model Discovery: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 2 — Domain Model Discovery
  CR: cr_04_catalog
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
    - Entity: Operation
      Description: Something a librarian asks the catalog to do.
      Store Model: Ten are declared for this subdomain, each with a boundary and a workflow.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #1'
    - Entity: Request
      Description: One asking, with what the librarian supplied.
      Store Model: Not held; it is what arrives at the boundary.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #2'
    - Entity: Requirement
      Description: Something an operation states a request must supply.
      Store Model: Declared at the operation's boundary, as a name and the form the value takes.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #4'
    - Entity: Use
      Description: A step of the operation reading something the request supplied.
      Store Model: Declared in the operation's own steps, as a reference to the supplied value.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #7'
    - Entity: Publication year
      Description: The year an edition was published.
      Store Model: Held in the catalog's book store. Its form is not declared anywhere the catalog owns; it is stated at each boundary and in the description supplied with each request, which say number in every case but one.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #7'
    - Entity: Correction
      Description: Changing some details of a record the catalog already holds.
      Store Model: The record named, and the changed details supplied together.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #5'
  entity_attributes:
    columns:
    - Entity
    - Attribute
    - Meaning
    - Evidence Status
    - Source Finding
    rows:
    - Entity: Requirement
      Attribute: Its name
      Meaning: What the request must supply.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #4'
    - Entity: Requirement
      Attribute: The form it takes
      Meaning: Whether the value is a number, a word, a list or a record.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #1'
    - Entity: Requirement
      Attribute: Whether it must be supplied
      Meaning: All fifty-nine requirements across the subdomain's ten operations must be supplied; none is optional.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_invariants #4'
    - Entity: Publication year
      Attribute: Its form at the boundary
      Meaning: A number in two of the three operations that name it, and a word in the third.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #2'
    - Entity: Publication year
      Attribute: Its form in the record
      Meaning: Not declared by the catalog. It is whatever the description supplied with the request says, which is a number in every request the library makes.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #1'
    - Entity: Correction
      Attribute: The record it names
      Meaning: The identity the catalog holds the record under. Read by the operation's steps.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #4'
    - Entity: Correction
      Attribute: The details it changes
      Meaning: Supplied together. Read by the operation's steps.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #4'
  business_processes:
    columns:
    - Process
    - Initiator
    - Outcome
    - Evidence Status
    - Source Finding
    rows:
    - Process: Admitting a request
      Initiator: The catalog boundary
      Outcome: The request proceeds, or it is turned away before anything happened.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #3'
    - Process: Registering a further edition
      Initiator: A librarian
      Outcome: A further edition of a held work is registered.
      Evidence Status: VERIFIED
      Source Finding: 'S1 requested_outcomes #1'
    - Process: Correcting bibliographic information
      Initiator: A librarian
      Outcome: What the library publishes about a record is changed.
      Evidence Status: VERIFIED
      Source Finding: 'S1 requested_outcomes #2'
    - Process: Registering a work for the first time
      Initiator: A librarian
      Outcome: The work, its first edition and a copy are registered.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #2'
    - Process: Comparing what an operation requires against what it uses
      Initiator: Nobody, until now
      Outcome: Nothing performed this while the boundary admitted everything.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #12'
  process_steps:
    columns:
    - Process
    - 'Step #'
    - Action
    - Record Produced
    - Evidence Status
    - Source Finding
    rows:
    - Process: Admitting a request
      'Step #': '1'
      Action: Read what the operation states a request must supply.
      Record Produced: Nothing.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #8'
    - Process: Admitting a request
      'Step #': '2'
      Action: Turn the request away if anything stated is missing or in the wrong form.
      Record Produced: The refusal, given to the librarian before anything happened.
      Evidence Status: VERIFIED
      Source Finding: 'S1 lifecycle_states #2'
    - Process: Registering a further edition
      'Step #': '3'
      Action: Read the eleven things the request supplied, including the publication year.
      Record Produced: The edition and the work it belongs to.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #7'
    - Process: Correcting bibliographic information
      'Step #': '4'
      Action: Read the record named and the details being changed.
      Record Produced: The corrected record.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #4'
    - Process: Correcting bibliographic information
      'Step #': '5'
      Action: Read the title, the author and the publication year the request also supplied.
      Record Produced: Nothing. No step performs this.
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 known_facts #7'
  belief_verification:
    columns:
    - Belief
    - Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE)
    - Evidence
    - Source Finding
    rows:
    - Belief: Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: '`book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0` declares the publication year as a word. `book_library_mgmt::IN_REGISTER_BOOK_V0` declares it as a number, as does `book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0`. The description of a book that the library supplies with each request declares it a number, and every year in the library''s own exercise of the catalog is a number. Two of three boundaries, the supplied description and the data agree; the third does not.'
      Source Finding: 'S1 system_beliefs #1'
    - Belief: Correcting bibliographic information asks for three details it does not use.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: '`book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0` requires eight things. Its workflow has four steps, and across all four it reads five: the record named, the details being changed, and the three the boundary uses to decide who may perform the operation. The title, the author and the publication year are read by no step.'
      Source Finding: 'S1 system_beliefs #2'
    - Belief: No other catalog operation asks for something it does not use.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): NOT_FOUND
      Evidence: 'All ten operations of the subdomain were compared, requirement by requirement, against the steps that carry them. **The belief holds in the direction Stage 1 meant it and fails in the other.** No operation but the correction requires something no step uses. But `book_library_mgmt::IN_REGISTER_BOOK_V0` has the opposite defect: its workflow reads the subject of the book and its boundary does not require it. The boundary therefore admits a request with no subject that the operation cannot then carry out. Whether any caller supplies the subject where the act reads it was not established at this stage.'
      Source Finding: 'S1 system_beliefs #3'
    - Belief: Who may perform each operation is stated separately from what the operation needs.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: Three of the eight things the correction requires — the credentials, the authorisation rules and the identity of the staff member — are consumed by the boundary's own decision about who may perform the operation, not by any step. They are present in every one of the subdomain's ten operations and are unaffected by what the operation does. Restating what an operation needs cannot reach them.
      Source Finding: 'S1 system_beliefs #4'
    - Belief: The details a correction changes are supplied together, as the changed fields.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: The correction's steps read the changed details as one supplied thing, and read the record they belong to by its identity. Removing the title, the author and the publication year removes nothing a step reads.
      Source Finding: 'S1 system_beliefs #5'
    - Belief: Both failures break the library's own end-to-end exercise of the catalog.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: 'Run against the pinned composition, the exercise stops at the second edition: the 1984 edition of the work being registered is absent from the catalog when the exercise looks for it. The first defect refuses it at the boundary, so the correction is never reached.'
      Source Finding: 'S1 known_facts #10'
  pps_baseline_fqdns:
    columns:
    - Capability
    - FQDN
    - What It Does
    - Fit (EXACT, PARTIAL, MISMATCH)
    - Cannot Do
    rows:
    - Capability: Admits a request to register a further edition
      FQDN: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      What It Does: States the eleven things such a request must supply, and turns away a request that does not supply them.
      Fit (EXACT, PARTIAL, MISMATCH): MISMATCH
      Cannot Do: States the publication year as a word. Turns away every request that supplies it the way the catalog holds it.
    - Capability: Registers a further edition
      FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      What It Does: Registers a further edition of a work already carried, reading all eleven things supplied.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing. It uses everything its boundary requires; only the form of one requirement is wrong.
    - Capability: Admits a request to correct bibliographic information
      FQDN: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      What It Does: States the eight things such a request must supply.
      Fit (EXACT, PARTIAL, MISMATCH): MISMATCH
      Cannot Do: Requires the title, the author and the publication year, which no step of the correction reads. Turns away a correction that does not resupply them.
    - Capability: Corrects bibliographic information
      FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      What It Does: Changes the details of a held record, reading the record named and the details being changed.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing. It is the boundary above it that is wrong.
    - Capability: Admits a request to register a work
      FQDN: book_library_mgmt::IN_REGISTER_BOOK_V0
      What It Does: States the ten things such a request must supply.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: Does not require the subject, which its workflow reads. Admits a request the operation cannot then carry out.
    - Capability: Registers a work
      FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      What It Does: Registers a work, its first edition and a copy, reading eleven things supplied.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing; it reads one thing its boundary does not require.
    - Capability: Holds what the catalog knows
      FQDN: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      What It Does: Declares the six stores the catalog owns and the paths they occupy.
      Fit (EXACT, PARTIAL, MISMATCH): MISMATCH
      Cannot Do: Declares no form for any detail it holds, so it cannot settle whether a publication year is a number. The description of a book is supplied with each request rather than declared once.
  gaps:
    columns:
    - Gap
    - Severity
    - Impact
    - Evidence Status
    - Source Finding
    rows:
    - Gap: Registering a further edition states the publication year in a form the catalog does not hold it in.
      Severity: HIGH
      Impact: Every correct request is turned away. The library's own exercise of the catalog stops here and never reaches the second defect.
      Evidence Status: VERIFIED
      Source Finding: 'S1 requested_outcomes #1'
    - Gap: Correcting bibliographic information requires three details no step reads.
      Severity: HIGH
      Impact: A correction that does not restate the fields it leaves alone is turned away, which is every correction.
      Evidence Status: VERIFIED
      Source Finding: 'S1 requested_outcomes #2'
    - Gap: Registering a work reads a detail its boundary does not require.
      Severity: MEDIUM
      Impact: The boundary admits a request with no subject that the operation then cannot carry out, so a declaration gap surfaces as a failure part-way through rather than as a refusal before anything happened. Whether any caller supplies the detail where the operation reads it was not established here.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #3'
    - Gap: Nothing compares what an operation requires against what it uses.
      Severity: MEDIUM
      Impact: All three defects were introduced without anything objecting, and stood undetected for as long as the boundary admitted everything.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #12'
  architectural_observations:
    columns:
    - Observation
    - Evidence
    - Evidence Status
    - Source Finding
    rows:
    - Observation: The subdomain's operations are otherwise exact.
      Evidence: Seven of the ten operations require precisely what their steps read, name for name. The defects are three, not a pattern across the subdomain.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #3'
    - Observation: The two defects are opposite in shape and were invisible for the same reason.
      Evidence: One boundary requires more than its operation reads; another requires less. Both are a disagreement between two statements of one fact, and neither is visible from either statement alone.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #8'
    - Observation: Who may perform an operation is declared uniformly and is untouched by this.
      Evidence: The same three things appear in all ten operations and are consumed by the boundary rather than by any step. They are constant across operations that read nothing else in common.
      Evidence Status: VERIFIED
      Source Finding: 'S1 out_of_scope #1'
    - Observation: A form mismatch and a name mismatch are not found by the same means.
      Evidence: Comparing names against what the steps read finds two of the three defects and cannot see the third. The publication year's form is wrong while its name is required and read, which no name-level comparison distinguishes.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #1'
  discovery_concerns:
    columns:
    - Concern
    - Evidence
    - Severity
    - Evidence Status
    - Source Finding
    rows:
    - Concern: The defect discovered in registering a work is outside what Stage 1 scoped.
      Evidence: Stage 1 named two operations and stated that no other asks for something it does not use. Discovery confirmed that and found a third operation with the opposite defect. It is in the same subdomain, of the same kind, and the change would be incomplete without it.
      Severity: MEDIUM
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #3'
    - Concern: The form of a detail the catalog holds is declared nowhere the catalog owns.
      Evidence: The store declares paths and no forms. The publication year's form is stated at three boundaries and in a description supplied with each request, and those four statements are the only ones there are. Three say number and one says word, and nothing compares them. The same disagreement could arise for any other detail.
      Severity: MEDIUM
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #1'
    - Concern: Whether the defects are confined to this domain is not established.
      Evidence: Ten operations of this subdomain were compared. The same comparison across the whole composition reports findings in other domains, which are those domains' business and were not examined here.
      Severity: LOW
      Evidence Status: INSUFFICIENT_EVIDENCE
      Source Finding: 'S1 out_of_scope #3'
  open_questions:
    columns:
    - Question
    - Category
    - Why It Matters
    - Source Finding
    rows:
    - Question: Does registering a work belong in this change, or in its own?
      Category: SCOPE
      Why It Matters: 'Discovery found a third defect in the same subdomain, of the opposite shape, that Stage 1 did not name. It is one requirement added rather than removed, which Stage 1 explicitly ruled out: no operation gains a requirement in this change. Either the constraint is relaxed for this one, or the defect is raised separately.'
      Source Finding: 'S1 constraints #5'
```

Every belief carried from Stage 1 was grounded against the pinned snapshot through the inspection
interface, and against the compiled dispatch the runtime actually reads. What was searched is
recorded, not only what was found. Where a belief came back narrower or wider than Stage 1 stated
it, the correction is recorded against the belief.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gaps

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions
