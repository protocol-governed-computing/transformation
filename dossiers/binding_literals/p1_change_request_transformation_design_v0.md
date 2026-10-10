# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** binding_literals
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
| design | MODIFY | The Design Intent phase judges where each input's value comes from. Two of its rules disagree about what a literal is, and it has no way to say that a generator determines a value. This corrects both. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Binding | A design's statement of where a step's input comes from. | CR seed §2 Business Vocabulary #1 |
| Reference | A binding to a value the runtime offers: the starting intent, the contract's own inputs, or an earlier step's result. | CR seed §2 Business Vocabulary #2 |
| Literal | A binding to a value the design fixes. | CR seed §2 Business Vocabulary #3 |
| Generator | What produces an artifact in place of construction writing it. | CR seed §2 Business Vocabulary #4 |
| Generated value | An input whose value the generator of the artifact that holds it determines. | CR seed §2 Business Vocabulary #5 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A literal has one meaning across every rule that judges a binding, so a quoted value is a literal wherever it appears. | CR seed §3 Requested Outcomes #1 |
| A design can say that an input's value is determined by the generator of the artifact that holds it, and only where the design names that generator. | CR seed §3 Requested Outcomes #2 |
| Every binding that is admissible today stays admissible, with the same meaning. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A value comes from the starting intent, from the contract's own inputs or from an earlier step, or it is a literal the design fixes. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| An operation name such as si.artifact.list is a literal, and so is a dotted identity such as a schema's identity. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A design names the generator of an artifact it does not write, and construction invokes the generator instead of writing the artifact. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Bound to an invented literal, a generated value passes and says something false. | HIGH | CR seed §4 Known Facts — Business Truths #4 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Two rules of the Design Intent phase judge the same binding: one asks whether it is a reference the runtime offers, the other whether it is written in a form the runtime resolves. | It is where the disagreement lives. | Identify the rules that judge a binding, and what each asks. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Written plain, a dotted literal is refused as a reference to a source the runtime does not offer. | It is half of the disagreement. | Confirm how a plain dotted value is judged. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Written in quotes, a dotted literal is accepted as a literal by one rule and refused by the other, which admits a literal only as a single word or an inline list or mapping. | It is the other half. | Confirm how a quoted dotted value is judged by each rule. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| No spelling of a dotted literal satisfies both rules. | It is the defect. | Establish whether any spelling is admitted by both. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Every contract that observes the composition binds a dotted literal, so no design can redeclare one. | It is what the defect blocks. | Identify the contracts that bind a dotted literal today. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| A phase workflow hands its judging contract the rule set the generator seals into it. | It is the generated value that has no statement. | Confirm how a phase workflow's rule set reaches its contract. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |
| A generated value left unbound is refused as missing, and bound to a description is refused as malformed. | It shows the design has no way to state it. | Confirm how each is judged. | CR seed §5 Existing-System Beliefs — Requiring Verification #7 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| NONE IDENTIFIED |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| No admissible design becomes inadmissible. This correction only admits statements that were refused. It is not retroactive. | Business author | CR seed §7 Constraints #1 |
| Saying a value is generated is admissible only for an artifact the design lists as generated. | Business author | CR seed §7 Constraints #2 |
| The rule-effectivity change is parked at its governance intent and resumes against the composition this change produces. | Business author | CR seed §7 Constraints #3 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A literal has one meaning across every rule that judges a binding. | CR seed §8 Business Invariants #1 |
| A generator determines only what the design says it does. | CR seed §8 Business Invariants #2 |
| No admissible design becomes inadmissible. | CR seed §8 Business Invariants #3 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Binding | Admissible | Every rule that judges it admits it. | CR seed §9 Lifecycle States #1 |
| Binding | Refused | A rule that judges it refuses it, and the finding says why. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A binding was judged | A design intent is checked | Every rule that judges a binding reads a literal the same way. | CR seed §10 Business Events #1 |
| A value was declared generated | A design states that the generator determines an input | It is admitted only where the design names that generator. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| The rules that judge a binding | design | CR seed §11 Authority Boundaries #1 |
| A generated value | The generator the design names | CR seed §11 Authority Boundaries #2 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| The rule-effectivity change | It is parked and resumes against the composition this change produces. | CR seed §12 Out of Scope #1 |

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
| A design can redeclare a contract that observes the composition, with every literal it binds stated. | CR seed §15 Acceptance Criteria #1 |
| A design can redeclare a workflow whose rule set a generator seals, stating that the generator determines it. | CR seed §15 Acceptance Criteria #2 |
| A value declared generated for an artifact the design does not list as generated is refused. | CR seed §15 Acceptance Criteria #3 |
| Every design admissible before this change is admissible after it. | CR seed §15 Acceptance Criteria #4 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| NONE IDENTIFIED |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| NONE IDENTIFIED |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Declaring a value generated | The design does not list the artifact that holds it as generated | A generator determines only what the design says it does. | CR seed §18 Operation Refusals #1 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| The rule-effectivity change | Its own dossier | This change is delivered. | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
