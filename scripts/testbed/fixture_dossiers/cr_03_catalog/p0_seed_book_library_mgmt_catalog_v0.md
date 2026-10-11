# Change Seed — book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 0 — Change Seed
  CR: cr_03_catalog
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
      Rationale: The catalog exists and works. It declares six moments it announces and announces none of them, against a rule the business set when the function was established.
  business_vocabulary:
    columns:
    - Term
    - Definition
    rows:
    - Term: Work
      Definition: Something the library carries, independent of any particular edition of it.
    - Term: Book
      Definition: An edition of a work.
    - Term: Physical copy
      Definition: One copy of a book, on a shelf.
    - Term: Bibliographic information
      Definition: What the library publishes about a book.
    - Term: Retirement
      Definition: Taking a book or a copy out of service, without removing what is known about it.
    - Term: Reinstatement
      Definition: Returning a retired book or copy to service.
    - Term: Moment
      Definition: Something the catalog announces because the business declared it matters.
  requested_outcomes:
    columns:
    - Outcome
    rows:
    - Outcome: Each of the six declared moments is announced when the act it names completes.
    - Outcome: That they are announced is checked, so the silence cannot return unnoticed.
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    rows:
    - Fact: The business decided the catalog announces the moments that matter.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: 'Six moments are declared: a work registered, a book registered, a physical copy registered, bibliographic information updated, a book retired, a physical copy retired.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A moment is announced when the act it names has completed, and not before.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A refusal announces nothing. Nothing happened that anyone need be told about.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Reinstatement is silent. The catalog performs it, records it, and announces nothing.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The six declared moments are the complete set. No seventh is added by this change.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: An announcement carries which thing it concerns and when it occurred, and nothing further.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Nobody is expected to hear these announcements today. The moment exists for the record.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The catalog does not go back and announce moments that occurred before this change.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: This is a defect, not a new requirement.
      Certainty (HIGH, MEDIUM, LOW): HIGH
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    rows:
    - Belief: The catalog declares six moments and announces none of them.
      Why It Matters: The whole of this change.
      Verification Goal: Confirm the six are declared, and establish whether anything refers to any of them.
    - Belief: The catalog performs registration, correction, retirement and reinstatement, each as its own act.
      Why It Matters: Each declared moment must attach to the act it names.
      Verification Goal: Confirm which acts the catalog performs.
    - Belief: Nothing checks whether a declared moment is ever announced.
      Why It Matters: Explains how the silence went unnoticed and says what the check must add.
      Verification Goal: Establish whether any rule relates a declared moment to an announcement of it.
    - Belief: Reinstatement has no declared moment of its own.
      Why It Matters: The business has ruled it silent; if a moment exists, the ruling and the system disagree.
      Verification Goal: Confirm no moment is declared for reinstatement.
  assumptions:
    columns:
    - Assumption
    - Basis
    rows:
    - Assumption: Each declared moment corresponds to exactly one act the catalog performs.
      Basis: The six are named after acts the catalog is known to perform.
  constraints:
    columns:
    - Constraint
    - Source
    rows:
    - Constraint: Nothing a caller sends or is told back changes. This is invisible from outside.
      Source: Business author
    - Constraint: No moment is added and none is removed. The six are the complete set.
      Source: Business author
    - Constraint: Nothing outside the catalog is touched.
      Source: Business author
  business_invariants:
    columns:
    - Invariant
    rows:
    - Invariant: A declared moment is announced when the act it names completes.
    - Invariant: A refused act announces nothing.
    - Invariant: An announcement carries which thing it concerns and when it occurred.
    - Invariant: A recorded moment is never changed or removed.
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    rows:
    - Object: Book
      State: In service
      Meaning: The library carries it.
    - Object: Book
      State: Retired
      Meaning: Taken out of service; what is known about it is kept.
    - Object: Physical copy
      State: In service
      Meaning: On the shelf.
    - Object: Physical copy
      State: Retired
      Meaning: Taken out of service.
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    rows:
    - Event: A work was registered
      When It Occurs: When the library first carries a work
      Significance: The library can show when it began carrying it.
    - Event: A book was registered
      When It Occurs: When an edition of a work is registered
      Significance: The library can show when the edition entered the catalog.
    - Event: A physical copy was registered
      When It Occurs: When a copy is put on a shelf
      Significance: The library can show when the copy became available.
    - Event: Bibliographic information was updated
      When It Occurs: When what the library publishes about a book is corrected
      Significance: The library can show when the record changed.
    - Event: A book was retired
      When It Occurs: When an edition is taken out of service
      Significance: The library can show when it stopped carrying it.
    - Event: A physical copy was retired
      When It Occurs: When a copy is taken out of service
      Significance: The library can show when the copy left the shelf.
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    rows:
    - Business Object: Work, book and physical copy
      Authoritative Owner: catalog
    - Business Object: Bibliographic information
      Authoritative Owner: catalog
    - Business Object: The moments the catalog announces
      Authoritative Owner: catalog
  out_of_scope:
    columns:
    - Item
    - Reason
    rows:
    - Item: What any listener does with an announcement
      Reason: The catalog announces the moment; who attends to it is a later question.
    - Item: Whether the six are the right six
      Reason: They are the moments the business already declared.
    - Item: A moment for reinstatement
      Reason: The business has ruled reinstatement silent.
    - Item: Anything about what the catalog holds or how it is searched
      Reason: Only the announcing is touched.
    - Item: Anything outside the catalog
      Reason: No other subdomain is touched.
    - Item: Moments that occurred before this change
      Reason: The record is added to and never rewritten.
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
    - Criterion: Registering a work announces that a work was registered.
    - Criterion: Registering a book announces that a book was registered.
    - Criterion: Registering a physical copy announces that a physical copy was registered.
    - Criterion: Correcting bibliographic information announces that it was updated.
    - Criterion: Retiring a book announces that a book was retired.
    - Criterion: Retiring a physical copy announces that a physical copy was retired.
    - Criterion: A refused act announces nothing.
    - Criterion: Reinstating a book or a copy announces nothing.
    - Criterion: Each announcement carries which thing it concerns and when it occurred.
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    rows:
    - Business Object: Moment
      Identified By: The act it names
      Two Are The Same When: They name the same act of the catalog.
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    rows:
    - Object: Book
      From State: In service
      To State: Retired
      Triggered By: The library retiring it.
      Cascade: A moment is announced. Nothing else follows.
    - Object: Book
      From State: Retired
      To State: In service
      Triggered By: The library reinstating it.
      Cascade: NONE. Reinstatement is silent.
    - Object: Physical copy
      From State: In service
      To State: Retired
      Triggered By: The library retiring it.
      Cascade: A moment is announced. Nothing else follows.
    - Object: Physical copy
      From State: Retired
      To State: In service
      Triggered By: The library reinstating it.
      Cascade: NONE. Reinstatement is silent.
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    rows:
    - Operation: Announcing a moment
      Refused When: The act it names did not complete
      Business Reason: A moment names something that happened; announcing one for an act that failed would state something untrue.
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    rows:
    - Business Object: What a listener does with an announcement
      Deferred To: A later change
      Until: The business decides who is told and how.
```

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

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
