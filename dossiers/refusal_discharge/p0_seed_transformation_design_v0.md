# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** refusal_discharge
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the six clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Design subdomain governs how a proposed change is judged before anything is built. It holds the
phases a change passes through, the rule set each phase declares, and the verdict a document
receives against them. Its authority is to refuse: a document that does not say what its phase
requires does not proceed, and a phase that reaches for language belonging to a later phase is out
of bounds. It governs what may be said at each stage of a change and in what order, and it decides
nothing about what any particular change should do.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| design | MODIFY | A business declares the operations it refuses at the first phase, and no phase after the second asks what carries any of them out. A design can be judged complete while a declared refusal is performed on demand. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Refusal | An operation the business states it will not perform, and the condition under which it will not. |
| Act | Something the business does as one unit, which completes or is refused. |
| Step | One part of an act, which returns an outcome the act routes on. |
| Outcome | What a step reports, which decides where the act goes next. |
| Ending | Where an act stops. An ending either completes the act or refuses it. |
| Discharge | The act, step and outcome that carry a declared refusal out. |
| Deferral | A declared refusal this change does not carry out, with the owner who will. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A design states, for each refusal the business declared, what discharges it — which act, at which step, on which outcome. |
| A design that leaves a declared refusal unaccounted for is refused. |
| A stated discharge is held to the design's own topology, so a step that does not exist or an outcome that does not refuse is refused. |
| A refusal this change does not own is stated as deferred, with its owner, rather than left silent. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A discharge is stated in a register of its own, not read out of the citations a design already carries. | HIGH |
| A citation is written where an author found it natural and omitted where they did not, so it cannot be what a rule rests on. | HIGH |
| A design is refused for an unaccounted refusal at the design intent phase, the first where acts, steps and outcomes exist. | HIGH |
| A discharge names the act, the step and the outcome; naming the act alone would be satisfied by any act that refuses anything. | HIGH |
| A step that returns its judgement succeeds whatever it found, so a refusal carried on an outcome that routes onward is not carried at all. | HIGH |
| A stated discharge is checked against the design's own execution topology rather than taken as written. | HIGH |
| The declared set and the discharged set are the same set: no discharge names a refusal the business never declared. | HIGH |
| A refusal owned by someone else may be deferred, and the deferral must already be present in the change's declared scope. | HIGH |
| A refusal that is never carried out produces no error and no missing field — the act simply succeeds where it was to stop. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The refusals a business declares are carried from the seed into the change request and checked for arrival, and no phase after that reads them. | The whole of this change. | Establish every rule that reads the refusal register, and at which phase each sits. |
| A design can be judged admissible at every phase while a declared refusal is carried out by nothing. | Says the gap is real rather than theoretical. | Confirm that no phase after the second poses the question, by any rule under any name. |
| A change request declared four refusals and one became nothing at all, and the act ran and did the thing the business refused. | Establishes the failure occurred rather than being foreseen. | Confirm the change, the refusal, and how the defect was eventually found. |
| That change has since been re-authored and all four refusals are now discharged, and three of the four cite something other than the refusal. | Says a correct design still does not show a reviewer that the refusals were carried out. | Confirm each refusal's discharge in the current design and what each row cites. |
| A design states its acts, their steps and each step's outcomes, and which ending each outcome routes to. | Decides whether a stated discharge can be checked without publishing anything new. | Establish what the design language already states about topology and endings. |
| A phase's declared scope records what the change defers and to whom. | Decides whether a deferral can be grounded rather than written freely at the last phase. | Establish where a deferral is recorded today and what it carries. |
| The composition refuses to seal an obligation nothing is bound to, and the build stops rather than shipping one. | Says the closure this change asks for is one the system already enforces one layer down. | Confirm the check, and confirm it was met by a real change rather than declared. |
| The document that judges a design is produced by a generator rather than written. | Says how this change is delivered, and that the path has been used once. | Confirm the artifact is generated, and which change was delivered through that path. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| A business declares few refusals per change, written when the problem is stated rather than discovered as the design proceeds. | The register belongs to the seed, which is authored before any design exists. |
| One refusal is carried out by one act at one step, rather than by several acts jointly. | A refusal names an operation, and an operation is one act. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| A discharge is stated in a register, never inferred from a citation. | Business author |
| A discharge names the act, the step and the outcome. | Business author |
| A stated discharge is checked against the design's own topology. | Business author |
| No discharge names a refusal the business did not declare. | Business author |
| A deferral names its owner and is already present in the change's declared scope. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every refusal the business declared is accounted for by the design, as discharged or as deferred. |
| A discharge names an act, a step of that act, and an outcome of that step. |
| The outcome a discharge names routes to an ending that refuses. |
| Every discharge a design states corresponds to a refusal the business declared. |
| A deferred refusal names the owner who will carry it out. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Refusal | Declared | The business has stated the operation and the condition, and nothing has been designed. |
| Refusal | Unaccounted | The design says nothing about it, which is the state this change ends. |
| Refusal | Discharged | The design names the act, step and outcome that carry it out. |
| Refusal | Deferred | The design states that another owner carries it out, and which. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A design accounted for a refusal | A design states what discharges a declared refusal | What the business refuses is visible as designed behaviour before anything is built. |
| A design was refused for an unaccounted refusal | A design reaches the design intent phase with a declared refusal it says nothing about | The omission is caught where a reviewer sees it rather than when the act runs. |
| A design was refused for a discharge that does not hold | A design names a step its act does not have, or an outcome that does not refuse | A stated discharge that would not stop the operation is not a discharge. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a design may state | design |
| Which operations are refused, and when | The business raising the change |
| How an act carries a refusal out | The design raising the change |
| Whether a refusal may be deferred, and to whom | The business raising the change |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Which operations a business refuses | Each business states its own, in its own change. |
| How an act performs a refusal | The design decides that; this change asks only which step does and on what outcome. |
| Whether a refusal must be discharged by the change that declared it | It may be deferred to another owner; what it may not be is unmentioned. |
| Whether the built act actually refuses when it runs | The platform decides that, and proving it is a matter of exercising the act. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| design | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A design can state what discharges each refusal the business declared, and a reviewer reads it in the design. |
| A design carrying a declared refusal it says nothing about is refused, naming the refusal. |
| A design naming a step its act does not have, or an outcome that does not lead to a refusal, is refused. |
| A design stating a discharge for a refusal the business never declared is refused. |
| A design that declares no refusals is judged exactly as it is today. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Refusal | The operation and the condition it is refused under | One operation refuses under several conditions, and each is its own refusal. |
| Discharge | The refusal it accounts for | One refusal is accounted for once, however many outcomes could be said to stop the act. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Refusal | Declared | Unaccounted | The design reaching the design intent phase saying nothing about it. | The design is refused. Nothing proceeds to the mandate. |
| Refusal | Declared | Discharged | The design stating the act, step and outcome that carry it out. | The stated discharge is checked against the design's own topology. |
| Refusal | Declared | Deferred | The design stating another owner carries it out. | The deferral is checked against what the change already declared out of its scope. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Judging a design | A refusal the business declared is neither discharged nor deferred | An operation the business refuses would be performed on demand, and nothing would report it. |
| Judging a design | A discharge names a step the act does not have | A discharge that points at nothing stops nothing. |
| Judging a design | A discharge names an outcome that does not route to a refusing ending | A step whose failing outcome routes onward does not refuse the operation, however plainly the register says it does. |
| Judging a design | A discharge names a refusal the business did not declare | It is a refusal nobody approved, or a row left behind by a rewording. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Which operations are refused, and when | Each business | That business raises a change that refuses something. |
| Whether the built act refuses when it runs | The platform | The act is exercised against the business's own criteria. |
