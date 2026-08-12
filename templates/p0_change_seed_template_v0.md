# P0 — Change Seed

**Stage:** 0 — Change Seed
**CR:** <cr-id>
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

---

## Document Contract

**Input:** `0_business_problem_statement.md` — free-form business prose, written by a person.
**Output:** this document — the same content, reorganized into governed registers.

P0 **reorganizes; it does not decide.** Everything a register asserts must be traceable to a
sentence in the problem statement. Everything the problem statement leaves unsaid becomes a
Clarification Request — never a filled-in guess.

INVALID OUTPUT:
- business content the problem statement does not contain
- any artifact code, FQDN or capability name (no design at this rung)
- a Clarification answered by the author rather than asked
- a System Belief promoted into a Known Fact

A required register with no rows MUST render as a single `| NONE IDENTIFIED |` row. Emptiness is
declared, never inferred from a blank register.

**Gate 0** — a person confirms the seed says what they meant, before any governed phase consumes it.

---

### The three-way split (the heart of P0)

P0 exists to keep three kinds of statement from contaminating one another, because every later
phase treats them differently:

| Register | Nature | Authoritative | What P2 does with it |
|----------|--------|---------------|----------------------|
| §4 Known Facts | business truths | the human | takes as given |
| §5 System Beliefs | suspicions about what exists | nobody yet | verifies against the snapshot |
| §14 Clarification Requests | open questions | unanswered | must ask, never guess |

A belief recorded as a fact is never verified. A question recorded as a fact is answered by
invention. Both failures are silent, and both originate here.

---

### Elicitation — questions for the human, and what each answer is used for

| Question | Declared intent |
|----------|-----------------|
| What does this subdomain govern, and why does it exist? | §0 Subdomain Purpose — the one narrative no compiled artifact can derive; consumed downstream, never rediscovered |
| Is this new, an extension, a modification, or a retirement? | §1 CR Type — P1 records the classification and its rationale |
| Which business terms carry governed meaning here? | §2 Business Vocabulary — every later phase reads meaning from this register |
| What must be true at close for this change to have succeeded? | §3 Requested Outcomes — P4 consolidates, P5 turns them into declared behaviour |
| What does the business authoritatively decide or require? | §4 Known Facts — taken as given; never re-litigated |
| What do you believe already exists? | §5 System Beliefs — P2 verification targets, each needing a Verification Goal |
| What are you assuming without having established it? | §6 Assumptions — surfaced so a later phase can overturn them explicitly |
| What is non-negotiable? | §7 Constraints — bound the design space at P5 and P6 |
| What must always be true, regardless of state? | §8 Business Invariants — P5 turns these into declared invariants |
| What states does each core object move through? | §9 Lifecycle States — P2 confirms them against the model |
| Which moments must the domain recognise? | §10 Business Events — P5 derives events from these |
| Who is authoritative for each business object? | §11 Authority Boundaries — P6 turns ownership into placement |
| What is deliberately *not* in this change? | §12 Out of Scope — what makes later CRs governed evolution rather than retrofitted scope |
| Which subdomains does this touch, and how? | §13 Governance Scope — P6 reads placement from this |
| What could you not answer? | §14 Clarification Requests — asked, never guessed |
| How will you know it worked, without looking inside? | §15 Acceptance Criteria — business-observable, testable without runtime internals |
| What identifies each object, and when are two of them the same thing? | §16 Identity and Sameness — P2 grounds identity in the model, P5 turns sameness into a declared rule |
| What moves an object between states, and what does *not* follow from it? | §17 Lifecycle Transitions — P5 declares the transitions; a cascade nobody asked for is invented behaviour |
| When must an operation refuse? | §18 Operation Refusals — P5 turns a refusal into declared behaviour rather than an unhandled path |
| Which authority is deliberately left to a later change? | §19 Authority Deferrals — P6 must not place what this change does not own |

An unanswered question is an open gap, never licence to assume.

---

## 0. Subdomain Purpose

*The one irreducible business narrative no compiled artifact can derive: what this subdomain
governs and why it exists. Stated once here, at the source; consumed downstream, never
rediscovered.*

<!-- register:subdomain_purpose business_language -->

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|

## 16. Identity and Sameness

*What identifies each business object, and the business rule that decides when two of them are the
same thing. A domain that cannot say when two records describe one object cannot prevent a duplicate,
and "a single authoritative record" is unverifiable.*

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|

## 17. Lifecycle Transitions

*What moves an object from one state to another, and what does **not** follow from it. The Cascade
column is the register's reason for existing: a transition that triggers nothing must say so, because
otherwise a later phase is free to invent the cascade the business never asked for.*

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|

## 18. Operation Refusals

*When an operation must refuse, and the business reason. A refusal the business requires and the seed
omits becomes, downstream, an unhandled path that silently succeeds.*

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|

## 19. Authority Deferrals

*Authority this change deliberately does not take, and where it is expected to land. Distinct from
§11: an owner named there is owned **now**, and a deferral recorded as an owner is placement P6 will
perform against a function that does not exist.*

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|

---

## gov_projection — Governed Handoff to Stage 1

*Governed, lossless, identity-preserving. Every register is forwarded — Stage 1 never re-discovers
what the seed established. Emit keys match the register ids above exactly.*

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
