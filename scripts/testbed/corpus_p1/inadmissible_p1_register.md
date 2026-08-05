# Change Request — transformation / phases

The P1 register. Every row restates content from the accepted seed and cites the finding it came
from; P1 classifies and traces, it does not add. Business language only — nothing here gets a code.

**Stage:** 1 — Change Request
**CR:** cr_00_new_subdomain
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|----------------|-----------|----------------|
| INVENTED_SUBDOMAIN | The pipeline that decides which changes are admissible is a distinct concern from the capabilities it admits, and needs its own governance boundary. It extends nothing that exists. | CR seed §1 CR Type |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|------|------------|----------------|
| Phase | One governed step of the change pipeline, with declared inputs, outputs and rules. |  |
| Seed | The business problem statement reorganized into fixed registers, and the only input later phases accept. | I remembered it |
| Seed Phase | The first phase: it turns a person's problem statement into a seed. | CR seed §2 Business Vocabulary |
| Rule Set | The declared set of conditions that decide whether a seed is admissible. Governance, not implementation. | CR seed §2 Business Vocabulary |
| Check Mechanism | A means of performing one kind of condition test. Implementation; carries no judgement about what should be tested. | CR seed §2 Business Vocabulary |
| Verdict | The outcome of applying the rule set to a seed: admissible or inadmissible. There is no partial pass. | CR seed §2 Business Vocabulary |
| Finding | One recorded failure of one rule, naming the rule, where it failed, and why that matters. | CR seed §2 Business Vocabulary |
| Gate | A point where a person accepts responsibility before the pipeline continues. | CR seed §2 Business Vocabulary |
| Author of Record | The person accountable for a seed's content. | CR seed §2 Business Vocabulary |
| Business Truth | Something the business authoritatively decides or requires. | CR seed §2 Business Vocabulary |
| System Belief | Something believed about what already exists, which must be verified rather than assumed. | CR seed §2 Business Vocabulary |
| Clarification | An open question that must be asked and never guessed. | CR seed §2 Business Vocabulary |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|---------|----------------|
| Establish the seed phase as a governed capability of the platform, with its rules readable from the composition rather than from a build tool. | CR seed §3 Requested Outcomes #1 |
| Produce a verdict for any offered seed, reporting every rule the seed failed rather than stopping at the first failure. | CR seed §3 Requested Outcomes #2 |
| Record accountability: a person is the author of record for a seed, and a person confirms at the gate that it says what they meant. | CR seed §3 Requested Outcomes #3 |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|------|-----------|----------------|
| The change pipeline must be governed the same way the capabilities it admits are governed. | MAYBE | CR seed §4 Known Facts #1 |
| The seed phase reorganizes a problem statement; it never decides business content. | HIGH | CR seed §4 Known Facts #2 |
| A seed is either admissible or inadmissible; there is no partial pass and no warning tier. | HIGH | CR seed §4 Known Facts #3 |
| Every rule is applied to every seed; evaluation does not stop at the first failure. | HIGH | CR seed §4 Known Facts #4 |
| The rule set is governance and must be readable from the composition and versioned as declared behaviour. | HIGH | CR seed §4 Known Facts #5 |
| A check mechanism is implementation and may live in code, provided it carries no judgement about what should be tested. | HIGH | CR seed §4 Known Facts #6 |
| A person is the author of record for a seed, and a person confirms it at the gate. | HIGH | CR seed §4 Known Facts #7 |
| The seed phase may not add business content the problem statement does not contain. | HIGH | CR seed §4 Known Facts #8 |
| The seed phase may not resolve an open question by guessing. | HIGH | CR seed §4 Known Facts #9 |
| The seed phase may not assign any design. | HIGH | CR seed §4 Known Facts #10 |
| The seed phase may not promote a System Belief into a Business Truth. | HIGH | CR seed §4 Known Facts #11 |
| Changing the rule set requires the same governed change process as any other declared behaviour. | HIGH | CR seed §4 Known Facts #12 |
| This change establishes the seed phase and its rule set only. | HIGH | CR seed §4 Known Facts #13 |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|--------|----------------|-------------------|----------------|
| No capability in the current composition decides seed admissibility. | This CR exists to fill that gap; if such a capability exists, the CR scope changes. | Confirm no existing capability produces a seed verdict. | CR seed §5 Beliefs #1 |
| A capability for declaring pure, deterministic transforms already exists. | The check mechanisms are pure transforms and should reuse it rather than author a new form. | Identify the governing declaration for pure capability transforms and its purity obligations. | CR seed §5 Beliefs #2 |
| A capability for declaring governed calls already exists, and forbids orchestration logic inside them. | Determines whether a rule can be a governed call or must be data the phase evaluates. | Identify the governing declaration for capability contracts and what it forbids. | CR seed §5 Beliefs #3 |
| A workflow form already exists that composes governed calls as a fixed graph without iteration. | Determines how the phase applies many rules to many registers. | Identify the workflow declaration and confirm whether iteration is available to it. | CR seed §5 Beliefs #4 |
| An actor form already exists for recording accountability. | The author of record and the gate reviewer are actors. | Identify the actor declaration and how a workflow binds one. | CR seed §5 Beliefs #5 |
| A form for declaring rules as data, separate from the mechanism that enforces them, already exists. | If so, the rule set should reuse it rather than invent a carrier. | Identify how existing rules are declared apart from their enforcement, and whether that form fits a rule set applied to a document. | CR seed §5 Beliefs #6 |
| Vocabulary extension is restricted to specific declared categories. | Determines whether the controlled vocabularies of the seed may be declared as vocabulary. | Identify what may be extended as vocabulary and what may not. | CR seed §5 Beliefs #7 |
| The platform's existing content is largely infrastructure rather than business capability. | Establishes what this subdomain can legitimately reuse. | Identify which existing capabilities are reuse candidates for a pipeline subdomain. | CR seed §5 Beliefs #8 |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|------------|-------|----------------|
| The seed template's section structure is stable and will not change while this CR is in flight. | It is fixed by the reference elicitation already in use. | CR seed §6 Assumptions |
| A person can supply every register by hand, so the pipeline never depends on an automated drafter. | Stated release constraint. | CR seed §6 Assumptions |

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|------------|--------|----------------|
| What is checked, and why, must be readable from the composition; only how a check runs may live in code. | Business policy | CR seed §7 Constraints |
| The pipeline is reachable only from a local command line, not over any network boundary. | Business policy | CR seed §7 Constraints |
| Dossiers are evidence about a composition and must never become part of one. | Business policy | CR seed §7 Constraints |
| A verdict must be reproducible: the same seed and the same rule set always give the same verdict. | Business policy | CR seed §7 Constraints |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|-----------|----------------|
| A seed has exactly one verdict, enforced by CT_PURE_EVALUATE_RULES_V0. | CR seed §8 Invariants #1 |
| Every rule in the rule set is applied to every seed offered to the phase. | CR seed §8 Invariants #2 |
| An inadmissible seed carries at least one finding, and an admissible seed carries none. | CR seed §8 Invariants #3 |
| Every finding names the rule that produced it. | CR seed §8 Invariants #4 |
| Every seed has exactly one author of record. | CR seed §8 Invariants #5 |
| The same seed and rule set always produce the same verdict. | CR seed §8 Invariants #6 |
| A seed that has not passed the gate is never consumed by a later phase. | CR seed §8 Invariants #7 |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|--------|-------|---------|----------------|
| Seed | Drafted | Reorganized from a problem statement; not yet judged. | CR seed §9 Lifecycle States |
| Seed | Admissible | The rule set found no findings. | CR seed §9 Lifecycle States |
| Seed | Inadmissible | At least one finding was recorded; the seed cannot proceed. | CR seed §9 Lifecycle States |
| Seed | Accepted | A person confirmed at the gate that it says what they meant. | CR seed §9 Lifecycle States |
| Rule Set | Active | The declared rules currently deciding admissibility. | CR seed §9 Lifecycle States |
| Rule Set | Superseded | Replaced by a later version through a governed change. | CR seed §9 Lifecycle States |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-------|----------------|--------------|----------------|
| Seed Offered | When a seed is submitted to the phase for judgement. | The phase has something to decide about. | CR seed §10 Business Events |
| Verdict Reached | When the rule set has been applied in full. | The seed's admissibility is established and recorded. | CR seed §10 Business Events |
| Seed Accepted | When a person confirms the seed at the gate. | Accountability is recorded and later phases may consume it. | CR seed §10 Business Events |
| Seed Rejected | When a verdict is inadmissible, or a person declines at the gate. | The change does not proceed, and the cause is recorded. | CR seed §10 Business Events |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|-----------------|---------------------|----------------|
| Problem Statement | The person who wrote it | CR seed §11 Authority Boundaries |
| Seed content | The author of record | CR seed §11 Authority Boundaries |
| Rule Set | Phases | CR seed §11 Authority Boundaries |
| Verdict | Phases | CR seed §11 Authority Boundaries |
| Finding | Phases | CR seed §11 Authority Boundaries |
| Gate acceptance | The gate reviewer | CR seed §11 Authority Boundaries |

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|------|--------|----------------|
| The remaining phases of the pipeline. | This change establishes the seed phase only; the rest arrive as later change requests. | CR seed §12 Out of Scope |
| Automated drafting of a seed. | The pipeline must not depend on it; it may be added later behind the same rules. | CR seed §12 Out of Scope |
| Reachability over any network boundary. | The pipeline is build-time and local only. | CR seed §12 Out of Scope |
| Rules that require reading an existing composition. | The seed phase judges a document alone; composition-aware rules belong to later phases. | CR seed §12 Out of Scope |
| Deciding which parts of a composition may be reused by a later change. | A property of the analysis phase, not the seed phase. | CR seed §12 Out of Scope |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, ADJACENT) | Source Finding |
|------------|--------------|----------------|
| phases | INVENTED | CR seed §13 Governance Scope |
| capability_transforms | ADJACENT | CR seed §13 Governance Scope |
| capability_contracts | ADJACENT | CR seed §13 Governance Scope |
| workflow | ADJACENT | CR seed §13 Governance Scope |
| intent | ADJACENT | CR seed §13 Governance Scope |
| runtime_binding | ADJACENT | CR seed §13 Governance Scope |
| governance | ADJACENT | CR seed §13 Governance Scope |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|----------|------------|----------|-------|----------------|
| How is the rule set carried as declared data? | The seed requires it readable from the composition and versioned as declared behaviour, but does not say in what form. | NO | HUMAN | CR seed §14 Clarification Requests #1 |
| Does the phase receive the seed as text, or as a location it must read? | Reproducibility of a verdict depends on the answer. | NO | HUMAN | CR seed §14 Clarification Requests #2 |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|-----------|----------------|
| A person can offer a seed to the phase and receive a verdict of admissible or inadmissible. | CR seed §15 Acceptance Criteria #1 |
| An inadmissible seed reports every rule it failed, not only the first. | CR seed §15 Acceptance Criteria #2 |
| The rules deciding admissibility can be read from the composition without reading any code. | CR seed §15 Acceptance Criteria #3 |
| Offering the same seed twice produces the same verdict. | CR seed §15 Acceptance Criteria #4 |
| A seed records exactly one author of record, and a gate acceptance records the person who gave it. | CR seed §15 Acceptance Criteria #5 |
| A seed that fails the gate is not consumed by any later phase. | CR seed §15 Acceptance Criteria #6 |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|-----------------|---------------|-----------------------|----------------|

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|--------|------------|----------|--------------|---------|----------------|

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|-----------|--------------|-----------------|----------------|

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|-----------------|-------------|-------|----------------|

---
