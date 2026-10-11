# Change Seed — book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 0 — Change Seed
  CR: cr_05_catalog
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
      Rationale: The catalog is built. It applies its rules as each request states them rather than holding them itself, registers what its own check found incomplete, and checks a copy of the book rather than the book it records. Nothing is added to what the catalog does; its own rules are made to hold however it is reached.
  business_vocabulary:
    columns:
    - Term
    - Definition
    rows:
    - Term: Authorized staff
      Definition: A library staff member permitted to perform catalog operations.
    - Term: Staff credentials
      Definition: What a request presents about the person performing it.
    - Term: Description
      Definition: What the library says a book, a work or a further edition must contain.
    - Term: Business rule
      Definition: 'Something the library decided about the catalog: who may perform an operation, and what a book, a work or a further edition must contain.'
  requested_outcomes:
    columns:
    - Outcome
    rows:
    - Outcome: The catalog holds the rules that decide who is authorized to perform a catalog operation, and refuses anyone they do not admit, whatever the request says.
    - Outcome: The catalog holds what a book, a work and a further edition must contain, and refuses a registration that does not meet it.
    - Outcome: The catalog checks the book, work or edition it records, not a copy supplied beside it.
    - Outcome: The catalog registers a physical copy as registered, whatever state the request gives it.
    - Outcome: Every correct request from authorized staff is admitted, with the same outcome as today.
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    rows:
    - Fact: Only authorized staff perform catalog operations.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The catalog does not decide who is authorized; it requires that they are.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A book's bibliographic information is its title, author, publication year and subject.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A book carries at least one subject.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The catalog records a publication year as a number.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A work names its title and author.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A further edition is described as a book is.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A registration that does not meet the library's description is refused.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: What a request says about the catalog's rules is ignored, not refused; it is not part of the request.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A physical copy's registration leads to registered, whatever the request carries.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Every rule of the catalog's own is held by the catalog.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The library adds to its record and does not rewrite it.
      Certainty (HIGH, MEDIUM, LOW): HIGH
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    rows:
    - Belief: Every catalog operation confirms the person performing it is authorized, against rules the request supplies.
      Why It Matters: 'This is the hole the library most needs closed: a request supplying no rules is confirmed whoever sends it.'
      Verification Goal: Establish where each operation reads its authorization rules from.
    - Belief: The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds.
      Why It Matters: A check nothing acts on refuses nothing.
      Verification Goal: Establish what each registration does with what its check finds.
    - Belief: The catalog checks a copy of the book supplied beside it, not the book it records.
      Why It Matters: A check of the wrong thing would judge something other than what is written, even if it refused.
      Verification Goal: Establish what each check reads, and what each registration writes.
    - Belief: The descriptions a book, a work and a further edition are checked against come from the request.
      Why It Matters: A request supplying an empty description has nothing checked against it.
      Verification Goal: Establish where each description is read from.
    - Belief: A physical copy is registered in whatever state the request gives it.
      Why It Matters: A copy was registered already retired.
      Verification Goal: Establish where a copy's registered state comes from.
  assumptions:
    columns:
    - Assumption
    - Basis
    rows:
    - Assumption: NONE IDENTIFIED
      Basis: ''
  constraints:
    columns:
    - Constraint
    - Source
    rows:
    - Constraint: Every correct request from authorized staff is admitted, with the same outcome as today.
      Source: Business author
    - Constraint: Records made under a request's own rules stay as they were made.
      Source: Business author — the record is added to, never rewritten.
  business_invariants:
    columns:
    - Invariant
    rows:
    - Invariant: No catalog operation is performed by anyone the library has not authorized.
    - Invariant: No book, work or further edition is registered without what the library says it must contain.
    - Invariant: What the catalog checks is what it records.
    - Invariant: No physical copy is registered in any state but registered.
    - Invariant: A business rule of the catalog's is held by the catalog, and no request changes it.
    - Invariant: A refusal changes no record.
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    rows:
    - Object: Physical copy
      State: Registered
      Meaning: On the shelf and in service. The only state a copy is registered in.
    - Object: Physical copy
      State: Retired
      Meaning: Taken out of service; unchanged by this change.
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    rows:
    - Event: A work was registered
      When It Occurs: When authorized staff register a complete book
      Significance: Unchanged by this change.
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    rows:
    - Business Object: The rules a catalog operation's staff credentials are judged by
      Authoritative Owner: Catalog
    - Business Object: What a book, a work and a further edition must contain
      Authoritative Owner: Catalog
    - Business Object: Which staff are authorized
      Authoritative Owner: The staff function
  out_of_scope:
    columns:
    - Item
    - Reason
    rows:
    - Item: Who a caller is, and whether the credentials a request presents are genuine
      Reason: The catalog holds the rules credentials are judged by; it does not authenticate them.
    - Item: Which staff are authorized
      Reason: That belongs to the staff function.
    - Item: Loans, members and every function other than the catalog
      Reason: Not this change.
    - Item: Records already in the catalog
      Reason: The library adds to its record and does not rewrite it.
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
    - Criterion: A catalog operation requested by anyone the library has not authorized is refused, whatever rules the request states, and no record changes.
    - Criterion: A book, a work or a further edition missing what the library says it must contain is refused, whatever description the request states, and nothing is registered by it.
    - Criterion: What the catalog checks for a registration is what it records.
    - Criterion: A physical copy is registered as registered, whatever state the request gives it.
    - Criterion: A request stating rules of its own is judged by the catalog's rules, and is not refused for stating them.
    - Criterion: Every correct request from authorized staff is admitted, with the same outcome as before this change.
    - Criterion: Records made before this change are unchanged by it.
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    rows:
    - Business Object: NONE IDENTIFIED
      Identified By: ''
      Two Are The Same When: ''
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    rows:
    - Object: Physical copy
      From State: Does not exist
      To State: Registered
      Triggered By: Authorized staff registering it
      Cascade: Unchanged by this change.
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    rows:
    - Operation: Any catalog operation
      Refused When: The person performing it is not authorized staff
      Business Reason: Only authorized staff perform catalog operations.
    - Operation: Registering a book
      Refused When: It lacks what the library says a book must contain
      Business Reason: The library said the parts are required.
    - Operation: Registering a further edition
      Refused When: It lacks what the library says an edition must contain
      Business Reason: The library said the parts are required.
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    rows:
    - Business Object: Which staff are authorized
      Deferred To: The staff function
      Until: Always; it is not the catalog's to decide.
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

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

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
