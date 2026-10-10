# Change Seed — transformation / build

**Stage:** 0 — Change Seed
**CR:** quoted_literals
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Build subdomain governs the passage from an approved design to the artifacts it determines: the
measure that decides whether a design determines them, the rendering of each artifact from what the
design states, and the writing of the result where its binding says it belongs. Its authority is to
refuse a design that does not determine what it schedules. It decides nothing about what a design
should contain.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| build | MODIFY | Construction renders each binding a design states into the artifact the runtime executes. A quoted literal keeps its quotes and a decimal number becomes text, so the runtime receives a value the design never stated. This renders every literal as the value it states. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Binding | A design's statement of where a step's input comes from. |
| Literal | A binding to a value the design fixes. |
| Quoted literal | A literal written inside quote marks, as a value with a dot in it must be. |
| Rendering | Producing an artifact from what the design states. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A quoted literal renders as the value inside its quotes. |
| A number renders as a number, whole or decimal. |
| Every other binding renders exactly as it does today. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A literal is a single word, a qualified identity, a number, or a value opening with a quote, bracket or brace. | HIGH |
| A value with a dot in it is written quoted, or it reads as a reference. | HIGH |
| Until now no design could state a quoted literal admissibly. | HIGH |
| The rule-effectivity change redeclares the contracts that observe the composition, and states their operation names as quoted literals. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Construction hands the runtime a quoted literal with its quote marks. | It is the defect. | Confirm how a quoted binding is rendered. |
| Construction reads a whole number as a number and any other number as text. | It is the second defect. | Confirm how a numeric binding is rendered. |
| No delivered artifact carries a quoted or decimal literal. | It is why the correction changes nothing delivered. | Establish whether any delivered design binds one. |
| The design is admissible and construction reports the artifact determined, while the runtime receives the wrong value. | It is why nothing catches it. | Confirm what the measure of a design reports for a quoted binding. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No delivered artifact changes. Every artifact construction reproduces today, it reproduces unchanged. | Business author |
| The rule-effectivity change waits for this one, and resumes once it is delivered. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| The runtime receives the value a design states. |
| No delivered artifact changes. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Binding | Stated | The design states where the value comes from. |
| Binding | Rendered | The artifact carries the value the design states. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A binding was rendered | Construction produces an artifact from a design | The artifact carries the value the design states. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| The rendering of a binding | build |
| What a literal is | design |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| The rule-effectivity change | It waits for this one, and resumes once it is delivered. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| build | MODIFIED |
| design | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A design binding a quoted literal renders an artifact carrying the value inside the quotes. |
| A design binding a decimal number renders an artifact carrying a number. |
| Every artifact construction reproduces today, it reproduces unchanged. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Binding | Stated | Rendered | Construction producing the artifact | None. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| NONE IDENTIFIED |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| The rule-effectivity change | Its own dossier | This change is delivered. |
