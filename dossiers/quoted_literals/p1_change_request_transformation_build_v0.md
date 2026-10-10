# Stage 1 — Change Request: Clarification & Fact Capture: transformation / build
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** quoted_literals
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
| build | MODIFY | Construction renders each binding a design states into the artifact the runtime executes. A quoted literal keeps its quotes and a decimal number becomes text, so the runtime receives a value the design never stated. This renders every literal as the value it states. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Binding | A design's statement of where a step's input comes from. | CR seed §2 Business Vocabulary #1 |
| Literal | A binding to a value the design fixes. | CR seed §2 Business Vocabulary #2 |
| Quoted literal | A literal written inside quote marks, as a value with a dot in it must be. | CR seed §2 Business Vocabulary #3 |
| Rendering | Producing an artifact from what the design states. | CR seed §2 Business Vocabulary #4 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A quoted literal renders as the value inside its quotes. | CR seed §3 Requested Outcomes #1 |
| A number renders as a number, whole or decimal. | CR seed §3 Requested Outcomes #2 |
| Every other binding renders exactly as it does today. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A literal is a single word, a qualified identity, a number, or a value opening with a quote, bracket or brace. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A value with a dot in it is written quoted, or it reads as a reference. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Until now no design could state a quoted literal admissibly. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The rule-effectivity change redeclares the contracts that observe the composition, and states their operation names as quoted literals. | HIGH | CR seed §4 Known Facts — Business Truths #4 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Construction hands the runtime a quoted literal with its quote marks. | It is the defect. | Confirm how a quoted binding is rendered. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Construction reads a whole number as a number and any other number as text. | It is the second defect. | Confirm how a numeric binding is rendered. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| No delivered artifact carries a quoted or decimal literal. | It is why the correction changes nothing delivered. | Establish whether any delivered design binds one. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The design is admissible and construction reports the artifact determined, while the runtime receives the wrong value. | It is why nothing catches it. | Confirm what the measure of a design reports for a quoted binding. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

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
| No delivered artifact changes. Every artifact construction reproduces today, it reproduces unchanged. | Business author | CR seed §7 Constraints #1 |
| The rule-effectivity change waits for this one, and resumes once it is delivered. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| The runtime receives the value a design states. | CR seed §8 Business Invariants #1 |
| No delivered artifact changes. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Binding | Stated | The design states where the value comes from. | CR seed §9 Lifecycle States #1 |
| Binding | Rendered | The artifact carries the value the design states. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A binding was rendered | Construction produces an artifact from a design | The artifact carries the value the design states. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| The rendering of a binding | build | CR seed §11 Authority Boundaries #1 |
| What a literal is | design | CR seed §11 Authority Boundaries #2 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| The rule-effectivity change | It waits for this one, and resumes once it is delivered. | CR seed §12 Out of Scope #1 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| build | MODIFIED | CR seed §13 Governance Scope #1 |
| design | ADJACENT | CR seed §13 Governance Scope #2 |

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
| A design binding a quoted literal renders an artifact carrying the value inside the quotes. | CR seed §15 Acceptance Criteria #1 |
| A design binding a decimal number renders an artifact carrying a number. | CR seed §15 Acceptance Criteria #2 |
| Every artifact construction reproduces today, it reproduces unchanged. | CR seed §15 Acceptance Criteria #3 |

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
| Binding | Stated | Rendered | Construction producing the artifact | None. | CR seed §17 Lifecycle Transitions #1 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| NONE IDENTIFIED |

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
