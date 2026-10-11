# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 1 — Change Request (Clarification & Fact Capture)
  CR: cr_05_catalog
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
      Rationale: The catalog is built. It applies its rules as each request states them rather than holding them itself, registers what its own check found incomplete, and checks a copy of the book rather than the book it records. Nothing is added to what the catalog does; its own rules are made to hold however it is reached.
      Source Finding: 'CR seed §1 CR Type #1'
  business_vocabulary:
    columns:
    - Term
    - Definition
    - Source Finding
    rows:
    - Term: Authorized staff
      Definition: A library staff member permitted to perform catalog operations.
      Source Finding: 'CR seed §2 Business Vocabulary #1'
    - Term: Staff credentials
      Definition: What a request presents about the person performing it.
      Source Finding: 'CR seed §2 Business Vocabulary #2'
    - Term: Description
      Definition: What the library says a book, a work or a further edition must contain.
      Source Finding: 'CR seed §2 Business Vocabulary #3'
    - Term: Business rule
      Definition: 'Something the library decided about the catalog: who may perform an operation, and what a book, a work or a further edition must contain.'
      Source Finding: 'CR seed §2 Business Vocabulary #4'
  requested_outcomes:
    columns:
    - Outcome
    - Source Finding
    rows:
    - Outcome: The catalog holds the rules that decide who is authorized to perform a catalog operation, and refuses anyone they do not admit, whatever the request says.
      Source Finding: 'CR seed §3 Requested Outcomes #1'
    - Outcome: The catalog holds what a book, a work and a further edition must contain, and refuses a registration that does not meet it.
      Source Finding: 'CR seed §3 Requested Outcomes #2'
    - Outcome: The catalog checks the book, work or edition it records, not a copy supplied beside it.
      Source Finding: 'CR seed §3 Requested Outcomes #3'
    - Outcome: The catalog registers a physical copy as registered, whatever state the request gives it.
      Source Finding: 'CR seed §3 Requested Outcomes #4'
    - Outcome: Every correct request from authorized staff is admitted, with the same outcome as today.
      Source Finding: 'CR seed §3 Requested Outcomes #5'
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    - Source Finding
    rows:
    - Fact: Only authorized staff perform catalog operations.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #1'
    - Fact: The catalog does not decide who is authorized; it requires that they are.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #2'
    - Fact: A book's bibliographic information is its title, author, publication year and subject.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #3'
    - Fact: A book carries at least one subject.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #4'
    - Fact: The catalog records a publication year as a number.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #5'
    - Fact: A work names its title and author.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #6'
    - Fact: A further edition is described as a book is.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #7'
    - Fact: A registration that does not meet the library's description is refused.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #8'
    - Fact: What a request says about the catalog's rules is ignored, not refused; it is not part of the request.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #9'
    - Fact: A physical copy's registration leads to registered, whatever the request carries.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #10'
    - Fact: Every rule of the catalog's own is held by the catalog.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #11'
    - Fact: The library adds to its record and does not rewrite it.
      Certainty (HIGH, MEDIUM, LOW): HIGH
      Source Finding: 'CR seed §4 Known Facts — Business Truths #12'
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    - Source Finding
    rows:
    - Belief: Every catalog operation confirms the person performing it is authorized, against rules the request supplies.
      Why It Matters: 'This is the hole the library most needs closed: a request supplying no rules is confirmed whoever sends it.'
      Verification Goal: Establish where each operation reads its authorization rules from.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #1'
    - Belief: The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds.
      Why It Matters: A check nothing acts on refuses nothing.
      Verification Goal: Establish what each registration does with what its check finds.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #2'
    - Belief: The catalog checks a copy of the book supplied beside it, not the book it records.
      Why It Matters: A check of the wrong thing would judge something other than what is written, even if it refused.
      Verification Goal: Establish what each check reads, and what each registration writes.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #3'
    - Belief: The descriptions a book, a work and a further edition are checked against come from the request.
      Why It Matters: A request supplying an empty description has nothing checked against it.
      Verification Goal: Establish where each description is read from.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #4'
    - Belief: A physical copy is registered in whatever state the request gives it.
      Why It Matters: A copy was registered already retired.
      Verification Goal: Establish where a copy's registered state comes from.
      Source Finding: 'CR seed §5 Existing-System Beliefs — Requiring Verification #5'
  assumptions:
    columns:
    - Assumption
    - Basis
    - Source Finding
    rows:
    - Assumption: NONE IDENTIFIED
      Basis: ''
      Source Finding: ''
  constraints:
    columns:
    - Constraint
    - Source
    - Source Finding
    rows:
    - Constraint: Every correct request from authorized staff is admitted, with the same outcome as today.
      Source: Business author
      Source Finding: 'CR seed §7 Constraints #1'
    - Constraint: Records made under a request's own rules stay as they were made.
      Source: Business author — the record is added to, never rewritten.
      Source Finding: 'CR seed §7 Constraints #2'
  business_invariants:
    columns:
    - Invariant
    - Source Finding
    rows:
    - Invariant: No catalog operation is performed by anyone the library has not authorized.
      Source Finding: 'CR seed §8 Business Invariants #1'
    - Invariant: No book, work or further edition is registered without what the library says it must contain.
      Source Finding: 'CR seed §8 Business Invariants #2'
    - Invariant: What the catalog checks is what it records.
      Source Finding: 'CR seed §8 Business Invariants #3'
    - Invariant: No physical copy is registered in any state but registered.
      Source Finding: 'CR seed §8 Business Invariants #4'
    - Invariant: A business rule of the catalog's is held by the catalog, and no request changes it.
      Source Finding: 'CR seed §8 Business Invariants #5'
    - Invariant: A refusal changes no record.
      Source Finding: 'CR seed §8 Business Invariants #6'
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    - Source Finding
    rows:
    - Object: Physical copy
      State: Registered
      Meaning: On the shelf and in service. The only state a copy is registered in.
      Source Finding: 'CR seed §9 Lifecycle States #1'
    - Object: Physical copy
      State: Retired
      Meaning: Taken out of service; unchanged by this change.
      Source Finding: 'CR seed §9 Lifecycle States #2'
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    - Source Finding
    rows:
    - Event: A work was registered
      When It Occurs: When authorized staff register a complete book
      Significance: Unchanged by this change.
      Source Finding: 'CR seed §10 Business Events #1'
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    - Source Finding
    rows:
    - Business Object: The rules a catalog operation's staff credentials are judged by
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #1'
    - Business Object: What a book, a work and a further edition must contain
      Authoritative Owner: Catalog
      Source Finding: 'CR seed §11 Authority Boundaries #2'
    - Business Object: Which staff are authorized
      Authoritative Owner: The staff function
      Source Finding: 'CR seed §11 Authority Boundaries #3'
  out_of_scope:
    columns:
    - Item
    - Reason
    - Source Finding
    rows:
    - Item: Who a caller is, and whether the credentials a request presents are genuine
      Reason: The catalog holds the rules credentials are judged by; it does not authenticate them.
      Source Finding: 'CR seed §12 Out of Scope #1'
    - Item: Which staff are authorized
      Reason: That belongs to the staff function.
      Source Finding: 'CR seed §12 Out of Scope #2'
    - Item: Loans, members and every function other than the catalog
      Reason: Not this change.
      Source Finding: 'CR seed §12 Out of Scope #3'
    - Item: Records already in the catalog
      Reason: The library adds to its record and does not rewrite it.
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
    - Criterion: A catalog operation requested by anyone the library has not authorized is refused, whatever rules the request states, and no record changes.
      Source Finding: 'CR seed §15 Acceptance Criteria #1'
    - Criterion: A book, a work or a further edition missing what the library says it must contain is refused, whatever description the request states, and nothing is registered by it.
      Source Finding: 'CR seed §15 Acceptance Criteria #2'
    - Criterion: What the catalog checks for a registration is what it records.
      Source Finding: 'CR seed §15 Acceptance Criteria #3'
    - Criterion: A physical copy is registered as registered, whatever state the request gives it.
      Source Finding: 'CR seed §15 Acceptance Criteria #4'
    - Criterion: A request stating rules of its own is judged by the catalog's rules, and is not refused for stating them.
      Source Finding: 'CR seed §15 Acceptance Criteria #5'
    - Criterion: Every correct request from authorized staff is admitted, with the same outcome as before this change.
      Source Finding: 'CR seed §15 Acceptance Criteria #6'
    - Criterion: Records made before this change are unchanged by it.
      Source Finding: 'CR seed §15 Acceptance Criteria #7'
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    - Source Finding
    rows:
    - Business Object: NONE IDENTIFIED
      Identified By: ''
      Two Are The Same When: ''
      Source Finding: ''
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    - Source Finding
    rows:
    - Object: Physical copy
      From State: Does not exist
      To State: Registered
      Triggered By: Authorized staff registering it
      Cascade: Unchanged by this change.
      Source Finding: 'CR seed §17 Lifecycle Transitions #1'
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    - Source Finding
    rows:
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Business Reason: Only authorized staff perform catalog operations.
      Source Finding: 'CR seed §18 Operation Refusals #1'
    - Operation: Registering a book
      Refused When: It lacks what the library says a book must contain
      Business Reason: The library said the parts are required.
      Source Finding: 'CR seed §18 Operation Refusals #2'
    - Operation: Registering a further edition
      Refused When: It lacks what the library says an edition must contain
      Business Reason: The library said the parts are required.
      Source Finding: 'CR seed §18 Operation Refusals #3'
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Business Object: Which staff are authorized
      Deferred To: The staff function
      Until: Always; it is not the catalog's to decide.
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
