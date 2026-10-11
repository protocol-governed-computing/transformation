# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 1 — Change Request (Clarification & Fact Capture)
  CR: cr_03_catalog
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
      Rationale: The catalog exists and works. It declares six moments it announces and announces none of them, against a rule the business set when the function was established.
      Source Finding: 'CR seed §1 CR Type #1'
  business_vocabulary:
    columns:
    - Term
    - Definition
    - Source Finding
    rows:
    - Term: Work
      Definition: Something the library carries, independent of any particular edition of it.
      Source Finding: 'CR seed §2 Business Vocabulary #1'
    - Term: Book
      Definition: An edition of a work.
      Source Finding: 'CR seed §2 Business Vocabulary #2'
    - Term: Physical copy
      Definition: One copy of a book, on a shelf.
      Source Finding: 'CR seed §2 Business Vocabulary #3'
    - Term: Bibliographic information
      Definition: What the library publishes about a book.
      Source Finding: 'CR seed §2 Business Vocabulary #4'
    - Term: Retirement
      Definition: Taking a book or a copy out of service, without removing what is known about it.
      Source Finding: 'CR seed §2 Business Vocabulary #5'
    - Term: Reinstatement
      Definition: Returning a retired book or copy to service.
      Source Finding: 'CR seed §2 Business Vocabulary #6'
    - Term: Moment
      Definition: Something the catalog announces because the business declared it matters.
      Source Finding: 'CR seed §2 Business Vocabulary #7'
  requested_outcomes:
    columns:
    - Outcome
    - Source Finding
    rows:
    - Outcome: Each of the six declared moments is announced when the act it names completes.
      Source Finding: 'CR seed §3 Requested Outcomes #1'
    - Outcome: That they are announced is checked, so the silence cannot return unnoticed.
      Source Finding: 'CR seed §3 Requested Outcomes #2'
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    - Source Finding
    rows:
    - Fact: The business decided the catalog announces the moments that matter.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #1'
    - Fact: 'Six moments are declared: a work registered, a book registered, a physical copy registered, bibliographic information updated, a book retired, a physical copy retired.'
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #2'
    - Fact: A moment is announced when the act it names has completed, and not before.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #3'
    - Fact: A refusal announces nothing. Nothing happened that anyone need be told about.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #4'
    - Fact: Reinstatement is silent. The catalog performs it, records it, and announces nothing.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #5'
    - Fact: The six declared moments are the complete set. No seventh is added by this change.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #6'
    - Fact: An announcement carries which thing it concerns and when it occurred, and nothing further.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #7'
    - Fact: Nobody is expected to hear these announcements today. The moment exists for the record.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #8'
    - Fact: The catalog does not go back and announce moments that occurred before this change.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #9'
    - Fact: This is a defect, not a new requirement.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #10'
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    - Source Finding
    rows:
    - Belief: The catalog declares six moments and announces none of them.
      Why It Matters: The whole of this change.
      Verification Goal: Confirm the six are declared, and establish whether anything refers to any of them.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #1'
    - Belief: The catalog performs registration, correction, retirement and reinstatement, each as its own act.
      Why It Matters: Each declared moment must attach to the act it names.
      Verification Goal: Confirm which acts the catalog performs.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #2'
    - Belief: Nothing checks whether a declared moment is ever announced.
      Why It Matters: Explains how the silence went unnoticed and says what the check must add.
      Verification Goal: Establish whether any rule relates a declared moment to an announcement of it.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #3'
    - Belief: Reinstatement has no declared moment of its own.
      Why It Matters: The business has ruled it silent; if a moment exists, the ruling and the system disagree.
      Verification Goal: Confirm no moment is declared for reinstatement.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #4'
  assumptions:
    columns:
    - Assumption
    - Basis
    - Source Finding
    rows:
    - Assumption: Each declared moment corresponds to exactly one act the catalog performs.
      Basis: The six are named after acts the catalog is known to perform.
      Source Finding: 'CR seed §6 Assumptions #1'
  constraints:
    columns:
    - Constraint
    - Source
    - Source Finding
    rows:
    - Constraint: Nothing a caller sends or is told back changes. This is invisible from outside.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #1'
    - Constraint: No moment is added and none is removed. The six are the complete set.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #2'
    - Constraint: Nothing outside the catalog is touched.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #3'
  business_invariants:
    columns:
    - Invariant
    - Source Finding
    rows:
    - Invariant: A declared moment is announced when the act it names completes.
      Source Finding: 'CR seed §8 Business Invariants #1'
    - Invariant: A refused act announces nothing.
      Source Finding: 'CR seed §8 Business Invariants #2'
    - Invariant: An announcement carries which thing it concerns and when it occurred.
      Source Finding: 'CR seed §8 Business Invariants #3'
    - Invariant: A recorded moment is never changed or removed.
      Source Finding: 'CR seed §8 Business Invariants #4'
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    - Source Finding
    rows:
    - Object: Book
      State: In service
      Meaning: The library carries it.
      Source Finding: 'CR seed §9 Lifecycle States #1'
    - Object: Book
      State: Retired
      Meaning: Taken out of service; what is known about it is kept.
      Source Finding: 'CR seed §9 Lifecycle States #2'
    - Object: Physical copy
      State: In service
      Meaning: On the shelf.
      Source Finding: 'CR seed §9 Lifecycle States #3'
    - Object: Physical copy
      State: Retired
      Meaning: Taken out of service.
      Source Finding: 'CR seed §9 Lifecycle States #4'
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    - Source Finding
    rows:
    - Event: A work was registered
      When It Occurs: When the library first carries a work
      Significance: The library can show when it began carrying it.
      Source Finding: 'CR seed §10 Business Events #1'
    - Event: A book was registered
      When It Occurs: When an edition of a work is registered
      Significance: The library can show when the edition entered the catalog.
      Source Finding: 'CR seed §10 Business Events #2'
    - Event: A physical copy was registered
      When It Occurs: When a copy is put on a shelf
      Significance: The library can show when the copy became available.
      Source Finding: 'CR seed §10 Business Events #3'
    - Event: Bibliographic information was updated
      When It Occurs: When what the library publishes about a book is corrected
      Significance: The library can show when the record changed.
      Source Finding: 'CR seed §10 Business Events #4'
    - Event: A book was retired
      When It Occurs: When an edition is taken out of service
      Significance: The library can show when it stopped carrying it.
      Source Finding: 'CR seed §10 Business Events #5'
    - Event: A physical copy was retired
      When It Occurs: When a copy is taken out of service
      Significance: The library can show when the copy left the shelf.
      Source Finding: 'CR seed §10 Business Events #6'
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    - Source Finding
    rows:
    - Business Object: Work, book and physical copy
      Authoritative Owner: catalog
      Source Finding: 'CR seed §11 Authority Boundaries #1'
    - Business Object: Bibliographic information
      Authoritative Owner: catalog
      Source Finding: 'CR seed §11 Authority Boundaries #2'
    - Business Object: The moments the catalog announces
      Authoritative Owner: catalog
      Source Finding: 'CR seed §11 Authority Boundaries #3'
  out_of_scope:
    columns:
    - Item
    - Reason
    - Source Finding
    rows:
    - Item: What any listener does with an announcement
      Reason: The catalog announces the moment; who attends to it is a later question.
      Source Finding: 'CR seed §12 Out of Scope #1'
    - Item: Whether the six are the right six
      Reason: They are the moments the business already declared.
      Source Finding: 'CR seed §12 Out of Scope #2'
    - Item: A moment for reinstatement
      Reason: The business has ruled reinstatement silent.
      Source Finding: 'CR seed §12 Out of Scope #3'
    - Item: Anything about what the catalog holds or how it is searched
      Reason: Only the announcing is touched.
      Source Finding: 'CR seed §12 Out of Scope #4'
    - Item: Anything outside the catalog
      Reason: No other subdomain is touched.
      Source Finding: 'CR seed §12 Out of Scope #5'
    - Item: Moments that occurred before this change
      Reason: The record is added to and never rewritten.
      Source Finding: 'CR seed §12 Out of Scope #6'
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
    - Criterion: Registering a work announces that a work was registered.
      Source Finding: 'CR seed §15 Acceptance Criteria #1'
    - Criterion: Registering a book announces that a book was registered.
      Source Finding: 'CR seed §15 Acceptance Criteria #2'
    - Criterion: Registering a physical copy announces that a physical copy was registered.
      Source Finding: 'CR seed §15 Acceptance Criteria #3'
    - Criterion: Correcting bibliographic information announces that it was updated.
      Source Finding: 'CR seed §15 Acceptance Criteria #4'
    - Criterion: Retiring a book announces that a book was retired.
      Source Finding: 'CR seed §15 Acceptance Criteria #5'
    - Criterion: Retiring a physical copy announces that a physical copy was retired.
      Source Finding: 'CR seed §15 Acceptance Criteria #6'
    - Criterion: A refused act announces nothing.
      Source Finding: 'CR seed §15 Acceptance Criteria #7'
    - Criterion: Reinstating a book or a copy announces nothing.
      Source Finding: 'CR seed §15 Acceptance Criteria #8'
    - Criterion: Each announcement carries which thing it concerns and when it occurred.
      Source Finding: 'CR seed §15 Acceptance Criteria #9'
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    - Source Finding
    rows:
    - Business Object: Moment
      Identified By: The act it names
      Two Are The Same When: They name the same act of the catalog.
      Source Finding: 'CR seed §16 Identity and Sameness #1'
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    - Source Finding
    rows:
    - Object: Book
      From State: In service
      To State: Retired
      Triggered By: The library retiring it.
      Cascade: A moment is announced. Nothing else follows.
      Source Finding: 'CR seed §17 Lifecycle Transitions #1'
    - Object: Book
      From State: Retired
      To State: In service
      Triggered By: The library reinstating it.
      Cascade: NONE. Reinstatement is silent.
      Source Finding: 'CR seed §17 Lifecycle Transitions #2'
    - Object: Physical copy
      From State: In service
      To State: Retired
      Triggered By: The library retiring it.
      Cascade: A moment is announced. Nothing else follows.
      Source Finding: 'CR seed §17 Lifecycle Transitions #3'
    - Object: Physical copy
      From State: Retired
      To State: In service
      Triggered By: The library reinstating it.
      Cascade: NONE. Reinstatement is silent.
      Source Finding: 'CR seed §17 Lifecycle Transitions #4'
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    - Source Finding
    rows:
    - Operation: Announcing a moment
      Refused When: The act it names did not complete
      Business Reason: A moment names something that happened; announcing one for an act that failed would state something untrue.
      Source Finding: 'CR seed §18 Operation Refusals #1'
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Business Object: What a listener does with an announcement
      Deferred To: A later change
      Until: The business decides who is told and how.
      Source Finding: 'CR seed §19 Authority Deferrals #1'
```

Projected from the change seed. Every row is the seed's own, cited to the section it was said in.
S1 interrogates and does not author.

---

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
