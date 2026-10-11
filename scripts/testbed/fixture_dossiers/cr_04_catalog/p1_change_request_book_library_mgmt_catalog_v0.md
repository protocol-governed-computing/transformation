# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 1 — Change Request (Clarification & Fact Capture)
  CR: cr_04_catalog
  Status: DRAFT
  Feeds: Stage 2 — Domain Model Discovery
registers:
  cr_type:
    columns:
    - Subdomain
    - Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE)
    - Rationale
    - Source Finding
    rows:
    - Subdomain: catalog
      Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE): MODIFY
      Rationale: Two operations state that they need things they do not use, and one states a publication year in a form the catalog does not hold it in. Correct requests are turned away. What each operation needs is restated to match what it does.
      Source Finding: 'CR seed §1 CR Type #1'
  business_vocabulary:
    columns:
    - Term
    - Definition
    - Source Finding
    rows:
    - Term: Operation
      Definition: Something a librarian asks the catalog to do.
      Source Finding: 'CR seed §2 Business Vocabulary #1'
    - Term: Request
      Definition: One asking, with what the librarian supplied.
      Source Finding: 'CR seed §2 Business Vocabulary #2'
    - Term: Admission
      Definition: The catalog deciding whether a request may proceed.
      Source Finding: 'CR seed §2 Business Vocabulary #3'
    - Term: Requirement
      Definition: Something an operation states a request must supply.
      Source Finding: 'CR seed §2 Business Vocabulary #4'
    - Term: Correction
      Definition: Changing some details of a record the catalog already holds.
      Source Finding: 'CR seed §2 Business Vocabulary #5'
    - Term: Further edition
      Definition: Another edition of a work the library already carries.
      Source Finding: 'CR seed §2 Business Vocabulary #6'
    - Term: Publication year
      Definition: The year an edition was published, which the catalog holds as a number.
      Source Finding: 'CR seed §2 Business Vocabulary #7'
  requested_outcomes:
    columns:
    - Outcome
    - Source Finding
    rows:
    - Outcome: Registering a further edition asks for the publication year in the form the catalog holds it.
      Source Finding: 'CR seed §3 Requested Outcomes #1'
    - Outcome: Correcting bibliographic information asks for the record and the changes, and nothing it does not use.
      Source Finding: 'CR seed §3 Requested Outcomes #2'
    - Outcome: A correct request for either operation is admitted.
      Source Finding: 'CR seed §3 Requested Outcomes #3'
    - Outcome: Every requirement an operation states is something that operation uses.
      Source Finding: 'CR seed §3 Requested Outcomes #4'
    - Outcome: Who may perform each operation, and what they must be authorised to do, is unchanged.
      Source Finding: 'CR seed §3 Requested Outcomes #5'
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    - Source Finding
    rows:
    - Fact: The catalog holds a publication year as a number, wherever it holds one.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #1'
    - Fact: Registering a work for the first time asks for the publication year as a number.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #2'
    - Fact: Registering a further edition of that same work asks for it as text.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #3'
    - Fact: A correction names the record it corrects and supplies the fields it changes.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #4'
    - Fact: A correction does not restate the fields it leaves alone; that is what makes it a correction.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #5'
    - Fact: Correcting bibliographic information asks for the title, author and publication year of the record.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #6'
    - Fact: The steps that carry out a correction read the record named and the changed fields, and read none of those three.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #7'
    - Fact: A requirement an operation does not use turns away correct requests and admits nothing extra.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #8'
    - Fact: A librarian correcting the subject headings of a record is turned away for not resupplying its title.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #9'
    - Fact: The library's end-to-end exercise of the catalog fails at both operations today.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #10'
    - Fact: Both failures are the boundary behaving correctly on a wrong statement.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #11'
    - Fact: Nothing compared what an operation asks for against what it uses, for as long as the boundary admitted everything.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #12'
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    - Source Finding
    rows:
    - Belief: Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number.
      Why It Matters: One half of the change.
      Verification Goal: Confirm both statements, and confirm which form the catalog records.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #1'
    - Belief: Correcting bibliographic information asks for three details it does not use.
      Why It Matters: The other half.
      Verification Goal: Confirm the three, and confirm no step of the correction reads them.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #2'
    - Belief: No other catalog operation asks for something it does not use.
      Why It Matters: Says whether this is two instances or a pattern across the subdomain.
      Verification Goal: Establish, for every catalog operation, what it asks for and what it uses.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #3'
    - Belief: Who may perform each operation is stated separately from what the operation needs.
      Why It Matters: Decides whether restating requirements can affect authorisation.
      Verification Goal: Confirm the two are separate statements.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #4'
    - Belief: The details a correction changes are supplied together, as the changed fields.
      Why It Matters: Decides whether removing three requirements loses anything.
      Verification Goal: Confirm the changed fields carry the details being corrected.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #5'
  assumptions:
    columns:
    - Assumption
    - Basis
    - Source Finding
    rows:
    - Assumption: A librarian supplies a publication year the way the catalog displays it.
      Basis: The catalog holds and shows it as a number.
      Source Finding: 'CR seed §6 Assumptions #1'
    - Assumption: The two operations were written from a third, and the requirements were carried across without being reconsidered.
      Basis: Registering a work needs the title, author and year; correcting a record does not, and asks for all three.
      Source Finding: 'CR seed §6 Assumptions #2'
  constraints:
    columns:
    - Constraint
    - Source
    - Source Finding
    rows:
    - Constraint: Every requirement an operation keeps is one that operation uses.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #1'
    - Constraint: Nothing about who may perform an operation changes.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #2'
    - Constraint: The records the catalog already holds are not migrated, rewritten or revalidated.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #3'
    - Constraint: A publication year is a number, in every operation that names one.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #4'
    - Constraint: No operation gains a requirement in this change.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #5'
  business_invariants:
    columns:
    - Invariant
    - Source Finding
    rows:
    - Invariant: An operation requires only what it uses.
      Source Finding: 'CR seed §8 Business Invariants #1'
    - Invariant: A publication year is stated as a number wherever an operation asks for one.
      Source Finding: 'CR seed §8 Business Invariants #2'
    - Invariant: A correction requires the record it corrects and the changes it makes.
      Source Finding: 'CR seed §8 Business Invariants #3'
    - Invariant: A correct request is admitted.
      Source Finding: 'CR seed §8 Business Invariants #4'
    - Invariant: What an operation requires is stated separately from who may perform it.
      Source Finding: 'CR seed §8 Business Invariants #5'
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    - Source Finding
    rows:
    - Object: Request
      State: Admitted
      Meaning: The catalog accepted it and the operation proceeds.
      Source Finding: 'CR seed §9 Lifecycle States #1'
    - Object: Request
      State: Turned away
      Meaning: The catalog refused it before anything happened.
      Source Finding: 'CR seed §9 Lifecycle States #2'
    - Object: Request
      State: Correct and turned away
      Meaning: Everything the operation needs was supplied and it was refused anyway. This is the state this change ends.
      Source Finding: 'CR seed §9 Lifecycle States #3'
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    - Source Finding
    rows:
    - Event: A request was admitted
      When It Occurs: When a librarian supplied what the operation needs
      Significance: The operation proceeds and the catalog changes.
      Source Finding: 'CR seed §10 Business Events #1'
    - Event: A request was turned away
      When It Occurs: When something the operation needs was missing or in the wrong form
      Significance: The librarian is told before anything happened, and the catalog is unchanged.
      Source Finding: 'CR seed §10 Business Events #2'
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    - Source Finding
    rows:
    - Business Object: What each catalog operation requires
      Authoritative Owner: The catalog subdomain
      Source Finding: 'CR seed §11 Authority Boundaries #1'
    - Business Object: The form a publication year takes
      Authoritative Owner: The catalog subdomain
      Source Finding: 'CR seed §11 Authority Boundaries #2'
    - Business Object: Who may perform a catalog operation
      Authoritative Owner: The library's authorisation rules
      Source Finding: 'CR seed §11 Authority Boundaries #3'
    - Business Object: Whether a request is admitted
      Authoritative Owner: The catalog boundary
      Source Finding: 'CR seed §11 Authority Boundaries #4'
  out_of_scope:
    columns:
    - Item
    - Reason
    - Source Finding
    rows:
    - Item: Who may perform any catalog operation
      Reason: A separate statement, unchanged by this.
      Source Finding: 'CR seed §12 Out of Scope #1'
    - Item: The records the catalog already holds
      Reason: No held record changes; only what a new request must supply.
      Source Finding: 'CR seed §12 Out of Scope #2'
    - Item: Operations of subdomains other than the catalog
      Reason: Each subdomain's own change.
      Source Finding: 'CR seed §12 Out of Scope #3'
    - Item: Whether the boundary should determine admission at all
      Reason: Settled; the boundary does what it always declared.
      Source Finding: 'CR seed §12 Out of Scope #4'
  governance_scope:
    columns:
    - Scope Item
    - Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT)
    - Source Finding
    rows:
    - Scope Item: catalog
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): MODIFIED
      Source Finding: 'CR seed §13 Governance Scope #1'
  clarification_requests:
    columns:
    - Question
    - Why Needed
    - Blocking (YES, NO)
    - Owner (HUMAN, SNAPSHOT, GOVERNANCE)
    - Source Finding
    rows:
    - Question: NONE IDENTIFIED
      Why Needed: ''
      Blocking (YES, NO): ''
      Owner (HUMAN, SNAPSHOT, GOVERNANCE): ''
      Source Finding: ''
  acceptance_criteria:
    columns:
    - Criterion
    - Source Finding
    rows:
    - Criterion: Registering a further edition of a held work, with the publication year as a number, is admitted and the edition is registered.
      Source Finding: 'CR seed §15 Acceptance Criteria #1'
    - Criterion: Correcting the subject headings of a held record, naming the record and the changes only, is admitted and the record is corrected.
      Source Finding: 'CR seed §15 Acceptance Criteria #2'
    - Criterion: The library's end-to-end exercise of the catalog completes, with every criterion holding.
      Source Finding: 'CR seed §15 Acceptance Criteria #3'
    - Criterion: A request omitting something either operation still needs is turned away.
      Source Finding: 'CR seed §15 Acceptance Criteria #4'
    - Criterion: A librarian not authorised for either operation is refused exactly as today.
      Source Finding: 'CR seed §15 Acceptance Criteria #5'
    - Criterion: No catalog operation requires anything it does not use.
      Source Finding: 'CR seed §15 Acceptance Criteria #6'
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    - Source Finding
    rows:
    - Business Object: Record
      Identified By: The identity the catalog holds it under
      Two Are The Same When: Two requests name the same identity.
      Source Finding: 'CR seed §16 Identity and Sameness #1'
    - Business Object: Requirement
      Identified By: The operation that states it and the thing it asks for
      Two Are The Same When: One operation asks for one thing once.
      Source Finding: 'CR seed §16 Identity and Sameness #2'
    - Business Object: Publication year
      Identified By: The year itself
      Two Are The Same When: Two are the same year, however either was supplied.
      Source Finding: 'CR seed §16 Identity and Sameness #3'
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    - Source Finding
    rows:
    - Object: Request
      From State: Correct and turned away
      To State: Admitted
      Triggered By: The operation stating only what it uses.
      Cascade: The operation proceeds as it always would have. Nothing about the catalog's records changes.
      Source Finding: 'CR seed §17 Lifecycle Transitions #1'
    - Object: Request
      From State: Admitted
      To State: Turned away
      Triggered By: Something the operation needs being absent.
      Cascade: The catalog is unchanged and the librarian is told.
      Source Finding: 'CR seed §17 Lifecycle Transitions #2'
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    - Source Finding
    rows:
    - Operation: Registering a further edition
      Refused When: The publication year is not supplied
      Business Reason: The catalog holds an edition by the work it belongs to and the year it was published, so an edition without a year cannot be placed.
      Source Finding: 'CR seed §18 Operation Refusals #1'
    - Operation: Correcting bibliographic information
      Refused When: The record to correct is not named
      Business Reason: A correction with no subject changes nothing, and the catalog would not know what to change.
      Source Finding: 'CR seed §18 Operation Refusals #2'
    - Operation: Correcting bibliographic information
      Refused When: No changed fields are supplied
      Business Reason: A correction that changes nothing is not a correction.
      Source Finding: 'CR seed §18 Operation Refusals #3'
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Business Object: What operations of other subdomains require
      Deferred To: Each subdomain
      Until: That subdomain raises the change that needs it.
      Source Finding: 'CR seed §19 Authority Deferrals #1'
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
