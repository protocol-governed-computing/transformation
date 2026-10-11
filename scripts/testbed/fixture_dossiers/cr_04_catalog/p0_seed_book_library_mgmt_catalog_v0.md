# Change Seed — book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 0 — Change Seed
  CR: cr_04_catalog
  Status: DRAFT
  Feeds: Stage 1 — Change Request
registers:
  subdomain_purpose: |2

    The Catalog subdomain governs what the library knows about its books: the works it carries, the
    editions of those works, and the physical copies on its shelves. It holds one record for each, the
    state that says whether each is in service or retired, and the details the library publishes about
    them. It records each thing being registered, its details being corrected, and its being retired or
    reinstated, and it announces the moments the business declared matter. It does not govern who borrows
    a book, what a borrower may do, or what the library charges.
  cr_type:
    columns:
    - Subdomain
    - Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE)
    - Rationale
    rows:
    - Subdomain: catalog
      Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE): MODIFY
      Rationale: Two operations state that they need things they do not use, and one states a publication year in a form the catalog does not hold it in. Correct requests are turned away. What each operation needs is restated to match what it does.
  business_vocabulary:
    columns:
    - Term
    - Definition
    rows:
    - Term: Operation
      Definition: Something a librarian asks the catalog to do.
    - Term: Request
      Definition: One asking, with what the librarian supplied.
    - Term: Admission
      Definition: The catalog deciding whether a request may proceed.
    - Term: Requirement
      Definition: Something an operation states a request must supply.
    - Term: Correction
      Definition: Changing some details of a record the catalog already holds.
    - Term: Further edition
      Definition: Another edition of a work the library already carries.
    - Term: Publication year
      Definition: The year an edition was published, which the catalog holds as a number.
  requested_outcomes:
    columns:
    - Outcome
    rows:
    - Outcome: Registering a further edition asks for the publication year in the form the catalog holds it.
    - Outcome: Correcting bibliographic information asks for the record and the changes, and nothing it does not use.
    - Outcome: A correct request for either operation is admitted.
    - Outcome: Every requirement an operation states is something that operation uses.
    - Outcome: Who may perform each operation, and what they must be authorised to do, is unchanged.
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    rows:
    - Fact: The catalog holds a publication year as a number, wherever it holds one.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Registering a work for the first time asks for the publication year as a number.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Registering a further edition of that same work asks for it as text.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A correction names the record it corrects and supplies the fields it changes.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A correction does not restate the fields it leaves alone; that is what makes it a correction.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Correcting bibliographic information asks for the title, author and publication year of the record.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The steps that carry out a correction read the record named and the changed fields, and read none of those three.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A requirement an operation does not use turns away correct requests and admits nothing extra.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A librarian correcting the subject headings of a record is turned away for not resupplying its title.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The library's end-to-end exercise of the catalog fails at both operations today.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Both failures are the boundary behaving correctly on a wrong statement.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Nothing compared what an operation asks for against what it uses, for as long as the boundary admitted everything.
      Certainty (HIGH, MEDIUM, LOW): HIGH
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    rows:
    - Belief: Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number.
      Why It Matters: One half of the change.
      Verification Goal: Confirm both statements, and confirm which form the catalog records.
    - Belief: Correcting bibliographic information asks for three details it does not use.
      Why It Matters: The other half.
      Verification Goal: Confirm the three, and confirm no step of the correction reads them.
    - Belief: No other catalog operation asks for something it does not use.
      Why It Matters: Says whether this is two instances or a pattern across the subdomain.
      Verification Goal: Establish, for every catalog operation, what it asks for and what it uses.
    - Belief: Who may perform each operation is stated separately from what the operation needs.
      Why It Matters: Decides whether restating requirements can affect authorisation.
      Verification Goal: Confirm the two are separate statements.
    - Belief: The details a correction changes are supplied together, as the changed fields.
      Why It Matters: Decides whether removing three requirements loses anything.
      Verification Goal: Confirm the changed fields carry the details being corrected.
  assumptions:
    columns:
    - Assumption
    - Basis
    rows:
    - Assumption: A librarian supplies a publication year the way the catalog displays it.
      Basis: The catalog holds and shows it as a number.
    - Assumption: The two operations were written from a third, and the requirements were carried across without being reconsidered.
      Basis: Registering a work needs the title, author and year; correcting a record does not, and asks for all three.
  constraints:
    columns:
    - Constraint
    - Source
    rows:
    - Constraint: Every requirement an operation keeps is one that operation uses.
      Source: Business author
    - Constraint: Nothing about who may perform an operation changes.
      Source: Business author
    - Constraint: The records the catalog already holds are not migrated, rewritten or revalidated.
      Source: Business author
    - Constraint: A publication year is a number, in every operation that names one.
      Source: Business author
    - Constraint: No operation gains a requirement in this change.
      Source: Business author
  business_invariants:
    columns:
    - Invariant
    rows:
    - Invariant: An operation requires only what it uses.
    - Invariant: A publication year is stated as a number wherever an operation asks for one.
    - Invariant: A correction requires the record it corrects and the changes it makes.
    - Invariant: A correct request is admitted.
    - Invariant: What an operation requires is stated separately from who may perform it.
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    rows:
    - Object: Request
      State: Admitted
      Meaning: The catalog accepted it and the operation proceeds.
    - Object: Request
      State: Turned away
      Meaning: The catalog refused it before anything happened.
    - Object: Request
      State: Correct and turned away
      Meaning: Everything the operation needs was supplied and it was refused anyway. This is the state this change ends.
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    rows:
    - Event: A request was admitted
      When It Occurs: When a librarian supplied what the operation needs
      Significance: The operation proceeds and the catalog changes.
    - Event: A request was turned away
      When It Occurs: When something the operation needs was missing or in the wrong form
      Significance: The librarian is told before anything happened, and the catalog is unchanged.
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    rows:
    - Business Object: What each catalog operation requires
      Authoritative Owner: The catalog subdomain
    - Business Object: The form a publication year takes
      Authoritative Owner: The catalog subdomain
    - Business Object: Who may perform a catalog operation
      Authoritative Owner: The library's authorisation rules
    - Business Object: Whether a request is admitted
      Authoritative Owner: The catalog boundary
  out_of_scope:
    columns:
    - Item
    - Reason
    rows:
    - Item: Who may perform any catalog operation
      Reason: A separate statement, unchanged by this.
    - Item: The records the catalog already holds
      Reason: No held record changes; only what a new request must supply.
    - Item: Operations of subdomains other than the catalog
      Reason: Each subdomain's own change.
    - Item: Whether the boundary should determine admission at all
      Reason: Settled; the boundary does what it always declared.
  governance_scope:
    columns:
    - Scope Item
    - Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT)
    rows:
    - Scope Item: catalog
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): MODIFIED
  clarification_requests:
    columns:
    - Question
    - Why Needed
    - Blocking (YES, NO)
    - Owner (HUMAN, SNAPSHOT, GOVERNANCE)
    rows:
    - Question: NONE IDENTIFIED
      Why Needed: ''
      Blocking (YES, NO): ''
      Owner (HUMAN, SNAPSHOT, GOVERNANCE): ''
  acceptance_criteria:
    columns:
    - Criterion
    rows:
    - Criterion: Registering a further edition of a held work, with the publication year as a number, is admitted and the edition is registered.
    - Criterion: Correcting the subject headings of a held record, naming the record and the changes only, is admitted and the record is corrected.
    - Criterion: The library's end-to-end exercise of the catalog completes, with every criterion holding.
    - Criterion: A request omitting something either operation still needs is turned away.
    - Criterion: A librarian not authorised for either operation is refused exactly as today.
    - Criterion: No catalog operation requires anything it does not use.
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    rows:
    - Business Object: Record
      Identified By: The identity the catalog holds it under
      Two Are The Same When: Two requests name the same identity.
    - Business Object: Requirement
      Identified By: The operation that states it and the thing it asks for
      Two Are The Same When: One operation asks for one thing once.
    - Business Object: Publication year
      Identified By: The year itself
      Two Are The Same When: Two are the same year, however either was supplied.
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    rows:
    - Object: Request
      From State: Correct and turned away
      To State: Admitted
      Triggered By: The operation stating only what it uses.
      Cascade: The operation proceeds as it always would have. Nothing about the catalog's records changes.
    - Object: Request
      From State: Admitted
      To State: Turned away
      Triggered By: Something the operation needs being absent.
      Cascade: The catalog is unchanged and the librarian is told.
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    rows:
    - Operation: Registering a further edition
      Refused When: The publication year is not supplied
      Business Reason: The catalog holds an edition by the work it belongs to and the year it was published, so an edition without a year cannot be placed.
    - Operation: Correcting bibliographic information
      Refused When: The record to correct is not named
      Business Reason: A correction with no subject changes nothing, and the catalog would not know what to change.
    - Operation: Correcting bibliographic information
      Refused When: No changed fields are supplied
      Business Reason: A correction that changes nothing is not a correction.
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    rows:
    - Business Object: What operations of other subdomains require
      Deferred To: Each subdomain
      Until: That subdomain raises the change that needs it.
```

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals
