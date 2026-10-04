# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** generated_artifacts
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
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
| design | MODIFY | The lifecycle carries a change to artifacts it authors and has no account of artifacts produced by a generator. A change to such an artifact is designed and then delivered by hand, outside the path that governs everything else. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Authored artifact | One a person writes. The artifact is its own source of truth. |
| Generated artifact | One a tool produces from something else. The artifact carries a copy of what determines it. |
| Generator | The thing an artifact is produced from, together with the mechanism that produces it. |
| Provenance | The record of which generator an artifact came from. |
| Agreement | Whether an artifact still matches what generated it. |
| Delivery | How a change reaches the artifacts it means to change. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A design can name the generator an artifact is produced from. |
| Construction reaches a generated artifact by invoking its generator, rather than refusing or rendering it directly. |
| An artifact's agreement with its generator is checked as part of building, not by habit. |
| A change to a generated artifact is delivered through the same path as any other change. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A generator is always authoritative. A generated artifact is never corrected directly. | HIGH |
| A generated artifact is governed as sealed output; its generator is governed as what determines it. | HIGH |
| A design schedules the artifact and names the generator as the means. | HIGH |
| Construction reaches a generated artifact by invoking its generator. | HIGH |
| A template and the code that reads it are one generator, not two. | HIGH |
| An artifact's agreement with its generator is a build gate, not a habit. | HIGH |
| Whether an artifact is generated is a fact about that artifact, not a decision this change makes. | HIGH |
| This change governs generation; it does not judge whether generating is a good idea. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Some artifacts of this domain are produced by a generator rather than written. | The whole of this change. | Confirm which artifacts are generated and what produces them. |
| A design has no way to say that an artifact is produced from something else. | Determines whether this adds a register or changes a rule. | Establish what a design can say today about how an artifact is reached. |
| Construction renders an artifact from the design alone, and would overwrite a generated one. | Says why the delivery path is unusable for these artifacts. | Confirm how construction produces an artifact. |
| A generated artifact's agreement with its generator can be checked, and nothing requires the check. | Says how large the gap is: the mechanism exists and is not in force. | Establish whether an agreement check exists and whether any build requires it. |
| Two changes to this domain have already been designed and delivered by hand because of this. | Establishes the defect occurred rather than being foreseen. | Confirm both, and that each stopped for this reason. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| Every generated artifact in this domain has exactly one generator. | Each phase's rule set is produced from one template and one declaration. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| A generated artifact is never edited directly, by this change or any other. | Business author |
| Construction may not become a second producer of an artifact a generator already produces. | Business author |
| No verdict changes for an authored artifact. This change concerns generated ones. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A generator is authoritative over the artifact it produces. |
| An artifact and the generator that produced it agree, and the build refuses when they do not. |
| One artifact has one generator. |
| A change to a generated artifact is delivered by changing its generator. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Generated artifact | In agreement | It matches what generated it. |
| Generated artifact | Stale | It does not, and the build refuses. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| An artifact was regenerated | When a generator is invoked and its artifact rewritten | The artifact and its generator agree again. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| A generated artifact's content | Its generator |
| Which artifacts are generated | Each artifact, as a fact about itself |
| How construction reaches an artifact | design |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Whether generating an artifact is a good idea | It is done today; this change governs it rather than judging it. |
| Which artifacts are generated | A fact about each artifact, not a decision here. |
| How rules are declared | The template and the code are what they are. |
| How a document authored under one rule set is judged under a later one | A separate problem with its own change. |
| Whether a design can state an artifact it amends | A separate problem with its own change. |
| Generated artifacts outside this lifecycle | Nothing has needed it yet. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| design | MODIFIED |
| build | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A design can name the generator an artifact is produced from, and is refused if it names none for an artifact that has one. |
| Construction reaches a generated artifact by invoking its generator, and never writes one directly. |
| A build refuses when an artifact and its generator disagree. |
| A change to a phase's rule set is delivered through the pipeline rather than by hand. |
| No verdict changes for an artifact that is authored rather than generated. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Generator | What it produces from, together with the mechanism that produces | They produce the same artifact from the same source. |
| Generated artifact | Its own identity | They are the same artifact. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Generated artifact | In agreement | Stale | Its generator changing without it being regenerated. | The build refuses. Nothing else follows. |
| Generated artifact | Stale | In agreement | Its generator being invoked. | A moment is recorded. Nothing else follows. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building | An artifact and its generator disagree | The artifact carries a copy of what determines it, and a stale copy reports confidently on the wrong thing. |
| Constructing an artifact | It is generated and construction would write it directly | Two producers of one artifact drift, and the generator is authoritative. |
| Scheduling | A design names a generated artifact and no generator | The design would not say how the artifact is reached. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Generated artifacts outside this lifecycle | A later change | Something outside it is generated. |
| Which artifacts are generated | Each artifact | It declares what it is. |
