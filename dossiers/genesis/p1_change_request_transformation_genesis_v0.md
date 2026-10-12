# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design, build

## Machine

```yaml
document:
  phase: p1
  domain: transformation
  subdomain:
  - design
  - build
  cr: genesis
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: design
    classification: NEW_SUBDOMAIN
    rationale: The change describes the phase pipeline as a governed part of the composition, judged by its own declared rules.
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: build
    classification: NEW_SUBDOMAIN
    rationale: The change describes construction as a governed part of the composition, separate from the phases because it fails differently.
    source_finding: {phase: p0, register: cr_type, row: 2}
  business_vocabulary:
  - term: Composition
    definition: The sealed set of everything the platform declares, which a change is designed against.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Change
    definition: A proposal to alter a composition, carried from a problem statement to a mandate.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Phase
    definition: One step of the pipeline, which takes one document and judges it against the rules declared for that step.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Problem Statement
    definition: The account of what the business wants, written by a person in their own words.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Seed
    definition: The problem statement reorganized into fixed registers, adding and deciding nothing.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Register
    definition: A named part of a document that later phases read by name.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Rule
    definition: A declared condition a document must meet to be admissible, with the reason it exists.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Verdict
    definition: Admissible or inadmissible, with every rule the document failed.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Finding
    definition: One failed rule, saying where in the document it failed and why the rule exists.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - term: Gate
    definition: A point at which a person approves a document before the pipeline continues.
    source_finding: {phase: p0, register: business_vocabulary, row: 10}
  - term: Design
    definition: The phase document that states, for every artifact a change introduces, what it is and how it connects.
    source_finding: {phase: p0, register: business_vocabulary, row: 11}
  - term: Mandate
    definition: The approved schedule of the artifacts to build, in the order they can be built.
    source_finding: {phase: p0, register: business_vocabulary, row: 12}
  - term: Construction
    definition: Turning an approved mandate into the artifacts it schedules.
    source_finding: {phase: p0, register: business_vocabulary, row: 13}
  - term: Determination
    definition: How much of a built artifact the design stated, rather than something construction would have had to supply.
    source_finding: {phase: p0, register: business_vocabulary, row: 14}
  - term: Author of Record
    definition: The person accountable for a document's content.
    source_finding: {phase: p0, register: business_vocabulary, row: 15}
  - term: Reviewer
    definition: The person who approves a document at a gate.
    source_finding: {phase: p0, register: business_vocabulary, row: 16}
  requested_outcomes:
  - outcome: Every phase of a change is judged by rules readable from the composition, without reading code.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: A verdict reports every failed rule, where it failed and why the rule exists.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: The same document judged by the same rules always gets the same verdict.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: An approved mandate is built into exactly the artifacts it schedules, and nothing the design did not determine is written.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: A person is accountable for every document and approves it at each gate.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  known_facts:
  - fact: A change is carried in nine phases, from a problem statement to a mandate.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: Each phase takes one document and judges it against the rules declared for that phase.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A verdict is admissible or inadmissible; there is no partial pass.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A verdict reports every rule the document failed, never only the first.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: A finding says where the document failed and why the rule exists.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: The same document judged by the same rules always gets the same verdict.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: The first phase reorganizes a problem statement into a seed and decides nothing.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: Later phases verify beliefs about the existing system against the composition the change is designed against.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: The last phase orders the build.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: The rules that decide admissibility are declared once, versioned, and changed only through a governed change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: A mechanism that knows how to perform a kind of check may live in code; what is checked and why may not.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: Construction writes only what the design states or what a governing artifact fixes.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: Construction reports how much of each artifact the design determined.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: A value construction would have to invent is a defect in the design.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: The person who writes a problem statement is its author of record.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: A person confirms the seed, approves the design, and approves the mandate.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: Nothing is built that a person did not approve.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: Nothing a person approved is changed without a new approval.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: The pipeline runs before a composition exists and is not reachable from outside.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: The pipeline reads the composition only through the platform's inspection capability.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  system_beliefs:
  - belief: The composition the change is designed against holds no part of the transformation domain.
    why_it_matters: The change is classified NEW_SUBDOMAIN for both subdomains on that basis.
    verification_goal: Confirm no artifact in the pinned composition carries the transformation namespace.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The platform offers an inspection capability that answers questions about a composition.
    why_it_matters: The pipeline reads the composition only through it; without it no belief can be verified.
    verification_goal: Confirm the pinned composition publishes inspection operations a phase can call.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: The platform governs how a capability, a workflow, a binding and a structure are declared.
    why_it_matters: The pipeline is described in those terms and is governed by the platform's rules for them.
    verification_goal: Confirm the pinned composition holds the constitutions that govern each kind the pipeline declares.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  assumptions:
  - assumption: The pipeline is driven from a local command line by the people making a change.
    basis: The statement excludes any reachability beyond a local command line.
    source_finding: {phase: p0, register: assumptions, row: 1}
  constraints:
  - constraint: What is checked, and why it matters, must not live in code.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: The first phase must not add business content, resolve an open question, assign design, or treat a belief as a fact.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: Construction must not write a value the design did not determine.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: The pipeline must read the composition only through the platform's inspection capability.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: Workers that draft documents, reachability beyond a local command line, and a governed generation step must not be designed into this change.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 5}
  business_invariants:
  - invariant: Every phase is judged only by rules declared for it.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: A verdict reports every failed rule.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: The same document and the same rules give the same verdict.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: Every rule states why it exists.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Nothing is built that a person did not approve.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: A built artifact holds only what the design or a governing artifact determined.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: Every document has a person accountable for it.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  lifecycle_states:
  - object: Phase Document
    state: Drafted
    meaning: The document is written and has not been judged.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Phase Document
    state: Admissible
    meaning: The document passed every rule declared for its phase.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Phase Document
    state: Inadmissible
    meaning: The document failed at least one rule, and the verdict names each.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: Phase Document
    state: Approved
    meaning: A person approved the admissible document at its gate.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  - object: Mandate
    state: Built
    meaning: Construction built the artifacts the approved mandate schedules.
    source_finding: {phase: p0, register: lifecycle_states, row: 5}
  business_events:
  - event: Document Judged
    when_it_occurs: When a phase judges a document against its rules.
    significance: The document receives its verdict and every finding.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: Document Approved
    when_it_occurs: When a person approves an admissible document at its gate.
    significance: The pipeline may continue past the gate.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: Mandate Built
    when_it_occurs: When construction builds the artifacts an approved mandate schedules.
    significance: The change's artifacts exist and their determination is reported.
    source_finding: {phase: p0, register: business_events, row: 3}
  authority_boundaries:
  - business_object: The rules that decide admissibility
    authoritative_owner: Transformation, through governed change
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: A document's content
    authoritative_owner: Its author of record
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Approval at a gate
    authoritative_owner: The reviewer
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: The composition a change is designed against
    authoritative_owner: The platform
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  out_of_scope:
  - item: Workers that draft documents
    reason: Excluded by the statement; expected through a later governed change.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Reachability beyond a local command line
    reason: Excluded by the statement; the pipeline is a build-time tool.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: A governed step that generates documents
    reason: Excluded by the statement; expected through a later governed change.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  governance_scope:
  - scope_item: design
    relationship: CREATED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: build
    relationship: CREATED
    source_finding: {phase: p0, register: governance_scope, row: 2}
  clarification_requests: null
  acceptance_criteria:
  - criterion: Each of the nine phases judges a document against the rules declared for it and returns admissible or inadmissible.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: An inadmissible verdict names every rule the document failed, where it failed, and why the rule exists.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: Judging the same document twice against the same rules gives the same verdict.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A seed that adds business content, resolves an open question, assigns design, or states a belief as a fact is inadmissible.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A belief about the existing system is verified against the composition the change is designed against.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: The rules each phase applies can be read from the composition without reading code.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Construction builds exactly the artifacts an approved mandate schedules.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: Construction reports how much of each artifact the design determined, and a value it would have to invent is reported as a defect.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: Nothing is built from a mandate a person has not approved.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  identity_and_sameness:
  - business_object: Phase Document
    identified_by: Its phase, its domain and subdomain, and its change.
    two_are_the_same_when: All four match.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: Rule
    identified_by: Where it is declared.
    two_are_the_same_when: They are declared in the same place.
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  lifecycle_transitions:
  - object: Phase Document
    from_state: null
    to_state: Drafted
    triggered_by: Its author writes it.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Phase Document
    from_state: Drafted
    to_state: Admissible
    triggered_by: The phase judges it and no rule fails.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: Phase Document
    from_state: Drafted
    to_state: Inadmissible
    triggered_by: The phase judges it and at least one rule fails.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  - object: Phase Document
    from_state: Inadmissible
    to_state: Drafted
    triggered_by: Its author revises it.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 4}
  - object: Phase Document
    from_state: Admissible
    to_state: Approved
    triggered_by: The reviewer approves it at its gate.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 5}
  - object: Mandate
    from_state: null
    to_state: Built
    triggered_by: Construction builds an approved mandate.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 6}
  operation_refusals:
  - operation: Continue past a gate
    refused_when: The document is inadmissible or not approved.
    business_reason: Nothing proceeds that a person did not approve.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Build a mandate
    refused_when: The mandate has not been approved.
    business_reason: Nothing is built that a person did not approve.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Judge a document
    refused_when: The composition it is designed against is not the one it names.
    business_reason: A verdict against another composition is evidence of nothing.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  authority_deferrals: null
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
