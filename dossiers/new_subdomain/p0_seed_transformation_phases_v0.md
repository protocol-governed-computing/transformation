# Change Seed — transformation / phases

**Stage:** 0 — Change Seed
**CR:** new_subdomain
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Phases subdomain governs how a proposed change to a composition is carried from a person's
problem statement to a decision about whether it may proceed. It owns the pipeline itself: what each
phase consumes and produces, which rules decide admissibility, and who is accountable at each gate.
Other parts of the platform govern what a composition contains; this subdomain governs how a
composition is allowed to change.

## 1. CR Type

<!-- register:cr_type business_language -->
| Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|----------------|-----------|
| NEW_SUBDOMAIN | The pipeline that decides which changes are admissible is a distinct concern from the capabilities it admits, and needs its own governance boundary. It extends nothing that exists. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Phase | One governed step of the change pipeline, with declared inputs, outputs and rules. |
| Seed | The business problem statement reorganized into fixed registers, and the only input later phases accept. |
| Seed Phase | The first phase: it turns a person's problem statement into a seed. |
| Rule Set | The declared set of conditions that decide whether a seed is admissible. Governance, not implementation. |
| Check Mechanism | A means of performing one kind of condition test. Implementation; carries no judgement about what should be tested. |
| Verdict | The outcome of applying the rule set to a seed: admissible or inadmissible. There is no partial pass. |
| Finding | One recorded failure of one rule, naming the rule, where it failed, and why that matters. |
| Gate | A point where a person accepts responsibility before the pipeline continues. |
| Author of Record | The person accountable for a seed's content. |
| Business Truth | Something the business authoritatively decides or requires. |
| System Belief | Something believed about what already exists, which must be verified rather than assumed. |
| Clarification | An open question that must be asked and never guessed. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Establish the seed phase as a governed capability of the platform, with its rules readable from the composition rather than from a build tool. |
| Produce a verdict for any offered seed, reporting every rule the seed failed rather than stopping at the first failure. |
| Record accountability: a person is the author of record for a seed, and a person confirms at the gate that it says what they meant. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The change pipeline must be governed the same way the capabilities it admits are governed. | HIGH |
| The seed phase reorganizes a problem statement; it never decides business content. | HIGH |
| A seed is either admissible or inadmissible; there is no partial pass and no warning tier. | HIGH |
| Every rule is applied to every seed; evaluation does not stop at the first failure. | HIGH |
| The rule set is governance and must be readable from the composition and versioned as declared behaviour. | HIGH |
| A check mechanism is implementation and may live in code, provided it carries no judgement about what should be tested. | HIGH |
| A person is the author of record for a seed, and a person confirms it at the gate. | HIGH |
| The seed phase may not add business content the problem statement does not contain. | HIGH |
| The seed phase may not resolve an open question by guessing. | HIGH |
| The seed phase may not assign any design. | HIGH |
| The seed phase may not promote a System Belief into a Business Truth. | HIGH |
| Changing the rule set requires the same governed change process as any other declared behaviour. | HIGH |
| This change establishes the seed phase and its rule set only. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| No capability in the current composition decides seed admissibility. | This CR exists to fill that gap; if such a capability exists, the CR scope changes. | Confirm no existing capability produces a seed verdict. |
| A capability for declaring pure, deterministic transforms already exists. | The check mechanisms are pure transforms and should reuse it rather than author a new form. | Identify the governing declaration for pure capability transforms and its purity obligations. |
| A capability for declaring governed calls already exists, and forbids orchestration logic inside them. | Determines whether a rule can be a governed call or must be data the phase evaluates. | Identify the governing declaration for capability contracts and what it forbids. |
| A workflow form already exists that composes governed calls as a fixed graph without iteration. | Determines how the phase applies many rules to many registers. | Identify the workflow declaration and confirm whether iteration is available to it. |
| An actor form already exists for recording accountability. | The author of record and the gate reviewer are actors. | Identify the actor declaration and how a workflow binds one. |
| A form for declaring rules as data, separate from the mechanism that enforces them, already exists. | If so, the rule set should reuse it rather than invent a carrier. | Identify how existing rules are declared apart from their enforcement, and whether that form fits a rule set applied to a document. |
| Vocabulary extension is restricted to specific declared categories. | Determines whether the controlled vocabularies of the seed may be declared as vocabulary. | Identify what may be extended as vocabulary and what may not. |
| The platform's existing content is largely infrastructure rather than business capability. | Establishes what this subdomain can legitimately reuse. | Identify which existing capabilities are reuse candidates for a pipeline subdomain. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| The seed template's register structure is stable and will not change while this CR is in flight. | It is fixed by the reference elicitation already in use. |
| A person can supply every register by hand, so the pipeline never depends on an automated drafter. | Stated release constraint. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| What is checked, and why, must be readable from the composition; only how a check runs may live in code. | Business policy |
| The pipeline is reachable only from a local command line, not over any network boundary. | Business policy |
| Dossiers are evidence about a composition and must never become part of one. | Business policy |
| A verdict must be reproducible: the same seed and the same rule set always give the same verdict. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A seed has exactly one verdict. |
| Every rule in the rule set is applied to every seed offered to the phase. |
| An inadmissible seed carries at least one finding, and an admissible seed carries none. |
| Every finding names the rule that produced it. |
| Every seed has exactly one author of record. |
| The same seed and rule set always produce the same verdict. |
| A seed that has not passed the gate is never consumed by a later phase. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Seed | Drafted | Reorganized from a problem statement; not yet judged. |
| Seed | Admissible | The rule set found no findings. |
| Seed | Inadmissible | At least one finding was recorded; the seed cannot proceed. |
| Seed | Accepted | A person confirmed at the gate that it says what they meant. |
| Rule Set | Active | The declared rules currently deciding admissibility. |
| Rule Set | Superseded | Replaced by a later version through a governed change. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| Seed Offered | When a seed is submitted to the phase for judgement. | The phase has something to decide about. |
| Verdict Reached | When the rule set has been applied in full. | The seed's admissibility is established and recorded. |
| Seed Accepted | When a person confirms the seed at the gate. | Accountability is recorded and later phases may consume it. |
| Seed Rejected | When a verdict is inadmissible, or a person declines at the gate. | The change does not proceed, and the cause is recorded. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Problem Statement | The person who wrote it |
| Seed content | The author of record |
| Rule Set | Phases |
| Verdict | Phases |
| Finding | Phases |
| Gate acceptance | The gate reviewer |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| The remaining phases of the pipeline. | This change establishes the seed phase only; the rest arrive as later change requests. |
| Automated drafting of a seed. | The pipeline must not depend on it; it may be added later behind the same rules. |
| Reachability over any network boundary. | The pipeline is build-time and local only. |
| Rules that require reading an existing composition. | The seed phase judges a document alone; composition-aware rules belong to later phases. |
| Deciding which parts of a composition may be reused by a later change. | A property of the analysis phase, not the seed phase. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| phases | CREATED |
| capability_transforms | ADJACENT |
| capability_contracts | ADJACENT |
| workflow | ADJACENT |
| intent | ADJACENT |
| runtime_binding | ADJACENT |
| governance | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| How is the rule set carried as declared data? | The problem statement requires it readable from the composition and versioned as declared behaviour, but does not say in what form. | NO | HUMAN |
| Does the phase receive the seed as text, or as a location it must read? | Reproducibility of a verdict depends on the answer. | NO | HUMAN |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A person can offer a seed to the phase and receive a verdict of admissible or inadmissible. |
| An inadmissible seed reports every rule it failed, not only the first. |
| The rules deciding admissibility can be read from the composition without reading any code. |
| Offering the same seed twice produces the same verdict. |
| A seed records exactly one author of record, and a gate acceptance records the person who gave it. |
| A seed that fails the gate is not consumed by any later phase. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
