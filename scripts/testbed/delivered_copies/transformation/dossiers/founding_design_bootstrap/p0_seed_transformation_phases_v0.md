# Change Seed — transformation / phases

## Machine

```yaml
header:
  Stage: 0 — Change Seed
  CR: new_subdomain
  Status: DRAFT
  Feeds: Stage 1 — Change Request
registers:
  subdomain_purpose: |2

    The Phases subdomain governs how a proposed change to a composition is carried from a person's
    problem statement to a decision about whether it may proceed. It owns the pipeline itself: what each
    phase consumes and produces, which rules decide admissibility, and who is accountable at each gate.
    Other parts of the platform govern what a composition contains; this subdomain governs how a
    composition is allowed to change.
  cr_type:
    columns:
    - Subdomain
    - Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE)
    - Rationale
    rows:
    - Subdomain: design
      Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE): NEW_SUBDOMAIN
      Rationale: The pipeline that decides which changes are admissible is a distinct concern from the capabilities it admits, and needs its own governance boundary. It extends nothing that exists.
  business_vocabulary:
    columns:
    - Term
    - Definition
    rows:
    - Term: Phase
      Definition: One governed step of the change pipeline, with declared inputs, outputs and rules.
    - Term: Seed
      Definition: The business problem statement reorganized into fixed registers, and the only input later phases accept.
    - Term: Seed Phase
      Definition: 'The first phase: it turns a person''s problem statement into a seed.'
    - Term: Rule Set
      Definition: The declared set of conditions that decide whether a seed is admissible. Governance, not implementation.
    - Term: Check Mechanism
      Definition: A means of performing one kind of condition test. Implementation; carries no judgement about what should be tested.
    - Term: Verdict
      Definition: 'The outcome of applying the rule set to a seed: admissible or inadmissible. There is no partial pass.'
    - Term: Finding
      Definition: One recorded failure of one rule, naming the rule, where it failed, and why that matters.
    - Term: Gate
      Definition: A point where a person accepts responsibility before the pipeline continues.
    - Term: Author of Record
      Definition: The person accountable for a seed's content.
    - Term: Business Truth
      Definition: Something the business authoritatively decides or requires.
    - Term: System Belief
      Definition: Something believed about what already exists, which must be verified rather than assumed.
    - Term: Clarification
      Definition: An open question that must be asked and never guessed.
  requested_outcomes:
    columns:
    - Outcome
    rows:
    - Outcome: Establish the seed phase as a governed capability of the platform, with its rules readable from the composition rather than from a build tool.
    - Outcome: Produce a verdict for any offered seed, reporting every rule the seed failed rather than stopping at the first failure.
    - Outcome: 'Record accountability: a person is the author of record for a seed, and a person confirms at the gate that it says what they meant.'
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    rows:
    - Fact: The change pipeline must be governed the same way the capabilities it admits are governed.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The seed phase reorganizes a problem statement; it never decides business content.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A seed is either admissible or inadmissible; there is no partial pass and no warning tier.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Every rule is applied to every seed; evaluation does not stop at the first failure.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The rule set is governance and must be readable from the composition and versioned as declared behaviour.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A check mechanism is implementation and may live in code, provided it carries no judgement about what should be tested.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A person is the author of record for a seed, and a person confirms it at the gate.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The seed phase may not add business content the problem statement does not contain.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The seed phase may not resolve an open question by guessing.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The seed phase may not assign any design.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The seed phase may not promote a System Belief into a Business Truth.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Changing the rule set requires the same governed change process as any other declared behaviour.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: This change establishes the seed phase and its rule set only.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The rule set is carried sealed inside the phase's own compiled artifact, alongside the workflow that applies it.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The sealed rule set is generated from the declaration rather than typed, and the two are compared on every run.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A phase receives the seed as text, the whole document travelling with the request.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: A verdict must be reproducible from what was judged, so a phase is never handed a location to read.
      Certainty (HIGH, MEDIUM, LOW): HIGH
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    rows:
    - Belief: No capability in the current composition decides seed admissibility.
      Why It Matters: This CR exists to fill that gap; if such a capability exists, the CR scope changes.
      Verification Goal: Confirm no existing capability produces a seed verdict.
    - Belief: A capability for declaring pure, deterministic transforms already exists.
      Why It Matters: The check mechanisms are pure transforms and should reuse it rather than author a new form.
      Verification Goal: Identify the governing declaration for pure capability transforms and its purity obligations.
    - Belief: A capability for declaring governed calls already exists, and forbids orchestration logic inside them.
      Why It Matters: Determines whether a rule can be a governed call or must be data the phase evaluates.
      Verification Goal: Identify the governing declaration for capability contracts and what it forbids.
    - Belief: A workflow form already exists that composes governed calls as a fixed graph without iteration.
      Why It Matters: Determines how the phase applies many rules to many registers.
      Verification Goal: Identify the workflow declaration and confirm whether iteration is available to it.
    - Belief: An actor form already exists for recording accountability.
      Why It Matters: The author of record and the gate reviewer are actors.
      Verification Goal: Identify the actor declaration and how a workflow binds one.
    - Belief: A form for declaring rules as data, separate from the mechanism that enforces them, already exists.
      Why It Matters: If so, the rule set should reuse it rather than invent a carrier.
      Verification Goal: Identify how existing rules are declared apart from their enforcement, and whether that form fits a rule set applied to a document.
    - Belief: Vocabulary extension is restricted to specific declared categories.
      Why It Matters: Determines whether the controlled vocabularies of the seed may be declared as vocabulary.
      Verification Goal: Identify what may be extended as vocabulary and what may not.
    - Belief: The platform's existing content is largely infrastructure rather than business capability.
      Why It Matters: Establishes what this subdomain can legitimately reuse.
      Verification Goal: Identify which existing capabilities are reuse candidates for a pipeline subdomain.
  assumptions:
    columns:
    - Assumption
    - Basis
    rows:
    - Assumption: The seed template's register structure is stable and will not change while this CR is in flight.
      Basis: It is fixed by the reference elicitation already in use.
    - Assumption: A person can supply every register by hand, so the pipeline never depends on an automated drafter.
      Basis: Stated release constraint.
  constraints:
    columns:
    - Constraint
    - Source
    rows:
    - Constraint: What is checked, and why, must be readable from the composition; only how a check runs may live in code.
      Source: Business policy
    - Constraint: The pipeline is reachable only from a local command line, not over any network boundary.
      Source: Business policy
    - Constraint: Dossiers are evidence about a composition and must never become part of one.
      Source: Business policy
    - Constraint: 'A verdict must be reproducible: the same seed and the same rule set always give the same verdict.'
      Source: Business policy
  business_invariants:
    columns:
    - Invariant
    rows:
    - Invariant: A seed has exactly one verdict.
    - Invariant: Every rule in the rule set is applied to every seed offered to the phase.
    - Invariant: An inadmissible seed carries at least one finding, and an admissible seed carries none.
    - Invariant: Every finding names the rule that produced it.
    - Invariant: Every seed has exactly one author of record.
    - Invariant: The same seed and rule set always produce the same verdict.
    - Invariant: A seed that has not passed the gate is never consumed by a later phase.
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    rows:
    - Object: Seed
      State: Drafted
      Meaning: Reorganized from a problem statement; not yet judged.
    - Object: Seed
      State: Admissible
      Meaning: The rule set found no findings.
    - Object: Seed
      State: Inadmissible
      Meaning: At least one finding was recorded; the seed cannot proceed.
    - Object: Seed
      State: Accepted
      Meaning: A person confirmed at the gate that it says what they meant.
    - Object: Rule Set
      State: Active
      Meaning: The declared rules currently deciding admissibility.
    - Object: Rule Set
      State: Superseded
      Meaning: Replaced by a later version through a governed change.
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    rows:
    - Event: Seed Offered
      When It Occurs: When a seed is submitted to the phase for judgement.
      Significance: The phase has something to decide about.
    - Event: Verdict Reached
      When It Occurs: When the rule set has been applied in full.
      Significance: The seed's admissibility is established and recorded.
    - Event: Seed Accepted
      When It Occurs: When a person confirms the seed at the gate.
      Significance: Accountability is recorded and later phases may consume it.
    - Event: Seed Rejected
      When It Occurs: When a verdict is inadmissible, or a person declines at the gate.
      Significance: The change does not proceed, and the cause is recorded.
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    rows:
    - Business Object: Problem Statement
      Authoritative Owner: The person who wrote it
    - Business Object: Seed content
      Authoritative Owner: The author of record
    - Business Object: Rule Set
      Authoritative Owner: Phases
    - Business Object: Verdict
      Authoritative Owner: Phases
    - Business Object: Finding
      Authoritative Owner: Phases
    - Business Object: Gate acceptance
      Authoritative Owner: The gate reviewer
  out_of_scope:
    columns:
    - Item
    - Reason
    rows:
    - Item: The remaining phases of the pipeline.
      Reason: This change establishes the seed phase only; the rest arrive as later change requests.
    - Item: Automated drafting of a seed.
      Reason: The pipeline must not depend on it; it may be added later behind the same rules.
    - Item: Reachability over any network boundary.
      Reason: The pipeline is build-time and local only.
    - Item: Rules that require reading an existing composition.
      Reason: The seed phase judges a document alone; composition-aware rules belong to later phases.
    - Item: Deciding which parts of a composition may be reused by a later change.
      Reason: A property of the analysis phase, not the seed phase.
  governance_scope:
    columns:
    - Scope Item
    - Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT)
    rows:
    - Scope Item: phases
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): CREATED
    - Scope Item: capability_transforms
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: capability_contracts
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: workflow
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: intent
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: runtime_binding
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: governance
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
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
    - Criterion: A person can offer a seed to the phase and receive a verdict of admissible or inadmissible.
    - Criterion: An inadmissible seed reports every rule it failed, not only the first.
    - Criterion: The rules deciding admissibility can be read from the composition without reading any code.
    - Criterion: Offering the same seed twice produces the same verdict.
    - Criterion: A seed records exactly one author of record, and a gate acceptance records the person who gave it.
    - Criterion: A seed that fails the gate is not consumed by any later phase.
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    rows: []
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    rows: []
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    rows: []
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    rows: []
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
