# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** refusal_discharge
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|---------|-------------------------------------------------------------------|---------|--------------|
| design | MODIFY | A business declares the operations it refuses at the first phase, and no phase after the second asks what carries any of them out. A design can be judged complete while a declared refusal is performed on demand. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Refusal | An operation the business states it will not perform, and the condition under which it will not. | CR seed §2 Business Vocabulary #1 |
| Act | Something the business does as one unit, which completes or is refused. | CR seed §2 Business Vocabulary #2 |
| Step | One part of an act, which returns an outcome the act routes on. | CR seed §2 Business Vocabulary #3 |
| Outcome | What a step reports, which decides where the act goes next. | CR seed §2 Business Vocabulary #4 |
| Ending | Where an act stops. An ending either completes the act or refuses it. | CR seed §2 Business Vocabulary #5 |
| Discharge | The act, step and outcome that carry a declared refusal out. | CR seed §2 Business Vocabulary #6 |
| Deferral | A declared refusal this change does not carry out, with the owner who will. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A design states, for each refusal the business declared, what discharges it — which act, at which step, on which outcome. | CR seed §3 Requested Outcomes #1 |
| A design that leaves a declared refusal unaccounted for is refused. | CR seed §3 Requested Outcomes #2 |
| A stated discharge is held to the design's own topology, so a step that does not exist or an outcome that does not refuse is refused. | CR seed §3 Requested Outcomes #3 |
| A refusal this change does not own is stated as deferred, with its owner, rather than left silent. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A discharge is stated in a register of its own, not read out of the citations a design already carries. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A citation is written where an author found it natural and omitted where they did not, so it cannot be what a rule rests on. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A design is refused for an unaccounted refusal at the design intent phase, the first where acts, steps and outcomes exist. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A discharge names the act, the step and the outcome; naming the act alone would be satisfied by any act that refuses anything. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A step that returns its judgement succeeds whatever it found, so a refusal carried on an outcome that routes onward is not carried at all. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A stated discharge is checked against the design's own execution topology rather than taken as written. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The declared set and the discharged set are the same set: no discharge names a refusal the business never declared. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A refusal owned by someone else may be deferred, and the deferral must already be present in the change's declared scope. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A refusal that is never carried out produces no error and no missing field — the act simply succeeds where it was to stop. | HIGH | CR seed §4 Known Facts — Business Truths #9 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The refusals a business declares are carried from the seed into the change request and checked for arrival, and no phase after that reads them. | The whole of this change. | Establish every rule that reads the refusal register, and at which phase each sits. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| A design can be judged admissible at every phase while a declared refusal is carried out by nothing. | Says the gap is real rather than theoretical. | Confirm that no phase after the second poses the question, by any rule under any name. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| A change request declared four refusals and one became nothing at all, and the act ran and did the thing the business refused. | Establishes the failure occurred rather than being foreseen. | Confirm the change, the refusal, and how the defect was eventually found. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| That change has since been re-authored and all four refusals are now discharged, and three of the four cite something other than the refusal. | Says a correct design still does not show a reviewer that the refusals were carried out. | Confirm each refusal's discharge in the current design and what each row cites. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| A design states its acts, their steps and each step's outcomes, and which ending each outcome routes to. | Decides whether a stated discharge can be checked without publishing anything new. | Establish what the design language already states about topology and endings. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| A phase's declared scope records what the change defers and to whom. | Decides whether a deferral can be grounded rather than written freely at the last phase. | Establish where a deferral is recorded today and what it carries. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |
| The composition refuses to seal an obligation nothing is bound to, and the build stops rather than shipping one. | Says the closure this change asks for is one the system already enforces one layer down. | Confirm the check, and confirm it was met by a real change rather than declared. | CR seed §5 Existing-System Beliefs — Requiring Verification #7 |
| The document that judges a design is produced by a generator rather than written. | Says how this change is delivered, and that the path has been used once. | Confirm the artifact is generated, and which change was delivered through that path. | CR seed §5 Existing-System Beliefs — Requiring Verification #8 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| A business declares few refusals per change, written when the problem is stated rather than discovered as the design proceeds. | The register belongs to the seed, which is authored before any design exists. | CR seed §6 Assumptions #1 |
| One refusal is carried out by one act at one step, rather than by several acts jointly. | A refusal names an operation, and an operation is one act. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| A discharge is stated in a register, never inferred from a citation. | Business author | CR seed §7 Constraints #1 |
| A discharge names the act, the step and the outcome. | Business author | CR seed §7 Constraints #2 |
| A stated discharge is checked against the design's own topology. | Business author | CR seed §7 Constraints #3 |
| No discharge names a refusal the business did not declare. | Business author | CR seed §7 Constraints #4 |
| A deferral names its owner and is already present in the change's declared scope. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every refusal the business declared is accounted for by the design, as discharged or as deferred. | CR seed §8 Business Invariants #1 |
| A discharge names an act, a step of that act, and an outcome of that step. | CR seed §8 Business Invariants #2 |
| The outcome a discharge names routes to an ending that refuses. | CR seed §8 Business Invariants #3 |
| Every discharge a design states corresponds to a refusal the business declared. | CR seed §8 Business Invariants #4 |
| A deferred refusal names the owner who will carry it out. | CR seed §8 Business Invariants #5 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Refusal | Declared | The business has stated the operation and the condition, and nothing has been designed. | CR seed §9 Lifecycle States #1 |
| Refusal | Unaccounted | The design says nothing about it, which is the state this change ends. | CR seed §9 Lifecycle States #2 |
| Refusal | Discharged | The design names the act, step and outcome that carry it out. | CR seed §9 Lifecycle States #3 |
| Refusal | Deferred | The design states that another owner carries it out, and which. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A design accounted for a refusal | A design states what discharges a declared refusal | What the business refuses is visible as designed behaviour before anything is built. | CR seed §10 Business Events #1 |
| A design was refused for an unaccounted refusal | A design reaches the design intent phase with a declared refusal it says nothing about | The omission is caught where a reviewer sees it rather than when the act runs. | CR seed §10 Business Events #2 |
| A design was refused for a discharge that does not hold | A design names a step its act does not have, or an outcome that does not refuse | A stated discharge that would not stop the operation is not a discharge. | CR seed §10 Business Events #3 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a design may state | design | CR seed §11 Authority Boundaries #1 |
| Which operations are refused, and when | The business raising the change | CR seed §11 Authority Boundaries #2 |
| How an act carries a refusal out | The design raising the change | CR seed §11 Authority Boundaries #3 |
| Whether a refusal may be deferred, and to whom | The business raising the change | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Which operations a business refuses | Each business states its own, in its own change. | CR seed §12 Out of Scope #1 |
| How an act performs a refusal | The design decides that; this change asks only which step does and on what outcome. | CR seed §12 Out of Scope #2 |
| Whether a refusal must be discharged by the change that declared it | It may be deferred to another owner; what it may not be is unmentioned. | CR seed §12 Out of Scope #3 |
| Whether the built act actually refuses when it runs | The platform decides that, and proving it is a matter of exercising the act. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| design | MODIFIED | CR seed §13 Governance Scope #1 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| NONE IDENTIFIED |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| A design can state what discharges each refusal the business declared, and a reviewer reads it in the design. | CR seed §15 Acceptance Criteria #1 |
| A design carrying a declared refusal it says nothing about is refused, naming the refusal. | CR seed §15 Acceptance Criteria #2 |
| A design naming a step its act does not have, or an outcome that does not lead to a refusal, is refused. | CR seed §15 Acceptance Criteria #3 |
| A design stating a discharge for a refusal the business never declared is refused. | CR seed §15 Acceptance Criteria #4 |
| A design that declares no refusals is judged exactly as it is today. | CR seed §15 Acceptance Criteria #5 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Refusal | The operation and the condition it is refused under | One operation refuses under several conditions, and each is its own refusal. | CR seed §16 Identity and Sameness #1 |
| Discharge | The refusal it accounts for | One refusal is accounted for once, however many outcomes could be said to stop the act. | CR seed §16 Identity and Sameness #2 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Refusal | Declared | Unaccounted | The design reaching the design intent phase saying nothing about it. | The design is refused. Nothing proceeds to the mandate. | CR seed §17 Lifecycle Transitions #1 |
| Refusal | Declared | Discharged | The design stating the act, step and outcome that carry it out. | The stated discharge is checked against the design's own topology. | CR seed §17 Lifecycle Transitions #2 |
| Refusal | Declared | Deferred | The design stating another owner carries it out. | The deferral is checked against what the change already declared out of its scope. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Judging a design | A refusal the business declared is neither discharged nor deferred | An operation the business refuses would be performed on demand, and nothing would report it. | CR seed §18 Operation Refusals #1 |
| Judging a design | A discharge names a step the act does not have | A discharge that points at nothing stops nothing. | CR seed §18 Operation Refusals #2 |
| Judging a design | A discharge names an outcome that does not route to a refusing ending | A step whose failing outcome routes onward does not refuse the operation, however plainly the register says it does. | CR seed §18 Operation Refusals #3 |
| Judging a design | A discharge names a refusal the business did not declare | It is a refusal nobody approved, or a row left behind by a rewording. | CR seed §18 Operation Refusals #4 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Which operations are refused, and when | Each business | That business raises a change that refuses something. | CR seed §19 Authority Deferrals #1 |
| Whether the built act refuses when it runs | The platform | The act is exercised against the business's own criteria. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
