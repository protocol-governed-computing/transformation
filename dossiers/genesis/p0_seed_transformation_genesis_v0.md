# Change Seed — transformation / design, build

## Machine

```yaml
document:
  phase: p0
  domain: transformation
  subdomain:
  - design
  - build
  cr: genesis
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The transformation domain governs how a composition is allowed to change. Its design subdomain
    carries a proposed change from a person's problem statement, through nine phases each judged by
    declared rules, to a mandate that schedules what to build. Its build subdomain turns an approved
    mandate into the artifacts it schedules, and reports how much of each the design determined. The
    domain owns the pipeline itself: what each phase consumes and produces, which rules decide
    admissibility, and who is accountable at each gate. It governs no business capability of its own.
  cr_type:
  - subdomain: design
    classification: NEW_SUBDOMAIN
    rationale: The change describes the phase pipeline as a governed part of the composition, judged by its own declared rules.
  - subdomain: build
    classification: NEW_SUBDOMAIN
    rationale: The change describes construction as a governed part of the composition, separate from the phases because it fails differently.
  business_vocabulary:
  - term: Composition
    definition: The sealed set of everything the platform declares, which a change is designed against.
  - term: Change
    definition: A proposal to alter a composition, carried from a problem statement to a mandate.
  - term: Phase
    definition: One step of the pipeline, which takes one document and judges it against the rules declared for that step.
  - term: Problem Statement
    definition: The account of what the business wants, written by a person in their own words.
  - term: Seed
    definition: The problem statement reorganized into fixed registers, adding and deciding nothing.
  - term: Register
    definition: A named part of a document that later phases read by name.
  - term: Rule
    definition: A declared condition a document must meet to be admissible, with the reason it exists.
  - term: Verdict
    definition: Admissible or inadmissible, with every rule the document failed.
  - term: Finding
    definition: One failed rule, saying where in the document it failed and why the rule exists.
  - term: Gate
    definition: A point at which a person approves a document before the pipeline continues.
  - term: Design
    definition: The phase document that states, for every artifact a change introduces, what it is and how it connects.
  - term: Mandate
    definition: The approved schedule of the artifacts to build, in the order they can be built.
  - term: Construction
    definition: Turning an approved mandate into the artifacts it schedules.
  - term: Determination
    definition: How much of a built artifact the design stated, rather than something construction would have had to supply.
  - term: Author of Record
    definition: The person accountable for a document's content.
  - term: Reviewer
    definition: The person who approves a document at a gate.
  requested_outcomes:
  - outcome: Every phase of a change is judged by rules readable from the composition, without reading code.
  - outcome: A verdict reports every failed rule, where it failed and why the rule exists.
  - outcome: The same document judged by the same rules always gets the same verdict.
  - outcome: An approved mandate is built into exactly the artifacts it schedules, and nothing the design did not determine is written.
  - outcome: A person is accountable for every document and approves it at each gate.
  known_facts:
  - fact: A change is carried in nine phases, from a problem statement to a mandate.
    certainty: HIGH
  - fact: Each phase takes one document and judges it against the rules declared for that phase.
    certainty: HIGH
  - fact: A verdict is admissible or inadmissible; there is no partial pass.
    certainty: HIGH
  - fact: A verdict reports every rule the document failed, never only the first.
    certainty: HIGH
  - fact: A finding says where the document failed and why the rule exists.
    certainty: HIGH
  - fact: The same document judged by the same rules always gets the same verdict.
    certainty: HIGH
  - fact: The first phase reorganizes a problem statement into a seed and decides nothing.
    certainty: HIGH
  - fact: Later phases verify beliefs about the existing system against the composition the change is designed against.
    certainty: HIGH
  - fact: The last phase orders the build.
    certainty: HIGH
  - fact: The rules that decide admissibility are declared once, versioned, and changed only through a governed change.
    certainty: HIGH
  - fact: A mechanism that knows how to perform a kind of check may live in code; what is checked and why may not.
    certainty: HIGH
  - fact: Construction writes only what the design states or what a governing artifact fixes.
    certainty: HIGH
  - fact: Construction reports how much of each artifact the design determined.
    certainty: HIGH
  - fact: A value construction would have to invent is a defect in the design.
    certainty: HIGH
  - fact: The person who writes a problem statement is its author of record.
    certainty: HIGH
  - fact: A person confirms the seed, approves the design, and approves the mandate.
    certainty: HIGH
  - fact: Nothing is built that a person did not approve.
    certainty: HIGH
  - fact: Nothing a person approved is changed without a new approval.
    certainty: HIGH
  - fact: The pipeline runs before a composition exists and is not reachable from outside.
    certainty: HIGH
  - fact: The pipeline reads the composition only through the platform's inspection capability.
    certainty: HIGH
  system_beliefs:
  - belief: The composition the change is designed against holds no part of the transformation domain.
    why_it_matters: The change is classified NEW_SUBDOMAIN for both subdomains on that basis.
    verification_goal: Confirm no artifact in the pinned composition carries the transformation namespace.
  - belief: The platform offers an inspection capability that answers questions about a composition.
    why_it_matters: The pipeline reads the composition only through it; without it no belief can be verified.
    verification_goal: Confirm the pinned composition publishes inspection operations a phase can call.
  - belief: The platform governs how a capability, a workflow, a binding and a structure are declared.
    why_it_matters: The pipeline is described in those terms and is governed by the platform's rules for them.
    verification_goal: Confirm the pinned composition holds the constitutions that govern each kind the pipeline declares.
  assumptions:
  - assumption: The pipeline is driven from a local command line by the people making a change.
    basis: The statement excludes any reachability beyond a local command line.
  constraints:
  - constraint: What is checked, and why it matters, must not live in code.
    source: Business policy
  - constraint: The first phase must not add business content, resolve an open question, assign design, or treat a belief as a fact.
    source: Business policy
  - constraint: Construction must not write a value the design did not determine.
    source: Business policy
  - constraint: The pipeline must read the composition only through the platform's inspection capability.
    source: Business policy
  - constraint: Workers that draft documents, reachability beyond a local command line, and a governed generation step must not be designed into this change.
    source: Business policy
  business_invariants:
  - invariant: Every phase is judged only by rules declared for it.
  - invariant: A verdict reports every failed rule.
  - invariant: The same document and the same rules give the same verdict.
  - invariant: Every rule states why it exists.
  - invariant: Nothing is built that a person did not approve.
  - invariant: A built artifact holds only what the design or a governing artifact determined.
  - invariant: Every document has a person accountable for it.
  lifecycle_states:
  - object: Phase Document
    state: Drafted
    meaning: The document is written and has not been judged.
  - object: Phase Document
    state: Admissible
    meaning: The document passed every rule declared for its phase.
  - object: Phase Document
    state: Inadmissible
    meaning: The document failed at least one rule, and the verdict names each.
  - object: Phase Document
    state: Approved
    meaning: A person approved the admissible document at its gate.
  - object: Mandate
    state: Built
    meaning: Construction built the artifacts the approved mandate schedules.
  business_events:
  - event: Document Judged
    when_it_occurs: When a phase judges a document against its rules.
    significance: The document receives its verdict and every finding.
  - event: Document Approved
    when_it_occurs: When a person approves an admissible document at its gate.
    significance: The pipeline may continue past the gate.
  - event: Mandate Built
    when_it_occurs: When construction builds the artifacts an approved mandate schedules.
    significance: The change's artifacts exist and their determination is reported.
  authority_boundaries:
  - business_object: The rules that decide admissibility
    authoritative_owner: Transformation, through governed change
  - business_object: A document's content
    authoritative_owner: Its author of record
  - business_object: Approval at a gate
    authoritative_owner: The reviewer
  - business_object: The composition a change is designed against
    authoritative_owner: The platform
  out_of_scope:
  - item: Workers that draft documents
    reason: Excluded by the statement; expected through a later governed change.
  - item: Reachability beyond a local command line
    reason: Excluded by the statement; the pipeline is a build-time tool.
  - item: A governed step that generates documents
    reason: Excluded by the statement; expected through a later governed change.
  governance_scope:
  - scope_item: design
    relationship: CREATED
  - scope_item: build
    relationship: CREATED
  clarification_requests: null
  acceptance_criteria:
  - criterion: Each of the nine phases judges a document against the rules declared for it and returns admissible or inadmissible.
  - criterion: An inadmissible verdict names every rule the document failed, where it failed, and why the rule exists.
  - criterion: Judging the same document twice against the same rules gives the same verdict.
  - criterion: A seed that adds business content, resolves an open question, assigns design, or states a belief as a fact is inadmissible.
  - criterion: A belief about the existing system is verified against the composition the change is designed against.
  - criterion: The rules each phase applies can be read from the composition without reading code.
  - criterion: Construction builds exactly the artifacts an approved mandate schedules.
  - criterion: Construction reports how much of each artifact the design determined, and a value it would have to invent is reported as a defect.
  - criterion: Nothing is built from a mandate a person has not approved.
  identity_and_sameness:
  - business_object: Phase Document
    identified_by: Its phase, its domain and subdomain, and its change.
    two_are_the_same_when: All four match.
  - business_object: Rule
    identified_by: Where it is declared.
    two_are_the_same_when: They are declared in the same place.
  lifecycle_transitions:
  - object: Phase Document
    from_state: null
    to_state: Drafted
    triggered_by: Its author writes it.
    cascade: None.
  - object: Phase Document
    from_state: Drafted
    to_state: Admissible
    triggered_by: The phase judges it and no rule fails.
    cascade: None.
  - object: Phase Document
    from_state: Drafted
    to_state: Inadmissible
    triggered_by: The phase judges it and at least one rule fails.
    cascade: None.
  - object: Phase Document
    from_state: Inadmissible
    to_state: Drafted
    triggered_by: Its author revises it.
    cascade: None.
  - object: Phase Document
    from_state: Admissible
    to_state: Approved
    triggered_by: The reviewer approves it at its gate.
    cascade: None.
  - object: Mandate
    from_state: null
    to_state: Built
    triggered_by: Construction builds an approved mandate.
    cascade: None.
  operation_refusals:
  - operation: Continue past a gate
    refused_when: The document is inadmissible or not approved.
    business_reason: Nothing proceeds that a person did not approve.
  - operation: Build a mandate
    refused_when: The mandate has not been approved.
    business_reason: Nothing is built that a person did not approve.
  - operation: Judge a document
    refused_when: The composition it is designed against is not the one it names.
    business_reason: A verdict against another composition is evidence of nothing.
  authority_deferrals: null
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

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
