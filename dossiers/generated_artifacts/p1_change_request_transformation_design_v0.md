# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** generated_artifacts
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was said in.
S1 interrogates and does not author.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|-----------|----------------|-----------|--------------|
| design | MODIFY | The lifecycle carries a change to artifacts it authors and has no account of artifacts produced by a generator. A change to such an artifact is designed and then delivered by hand, outside the path that governs everything else. | CR seed §1 CR Type #1 |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|------|------------|--------------|
| Authored artifact | One a person writes. The artifact is its own source of truth. | CR seed §2 Business Vocabulary #1 |
| Generated artifact | One a tool produces from something else. The artifact carries a copy of what determines it. | CR seed §2 Business Vocabulary #2 |
| Generator | The thing an artifact is produced from, together with the mechanism that produces it. | CR seed §2 Business Vocabulary #3 |
| Provenance | The record of which generator an artifact came from. | CR seed §2 Business Vocabulary #4 |
| Agreement | Whether an artifact still matches what generated it. | CR seed §2 Business Vocabulary #5 |
| Delivery | How a change reaches the artifacts it means to change. | CR seed §2 Business Vocabulary #6 |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|---------|--------------|
| A design can name the generator an artifact is produced from. | CR seed §3 Requested Outcomes #1 |
| Construction reaches a generated artifact by invoking its generator, rather than refusing or rendering it directly. | CR seed §3 Requested Outcomes #2 |
| An artifact's agreement with its generator is checked as part of building, not by habit. | CR seed §3 Requested Outcomes #3 |
| A change to a generated artifact is delivered through the same path as any other change. | CR seed §3 Requested Outcomes #4 |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|------|-----------|--------------|
| A generator is always authoritative. A generated artifact is never corrected directly. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A generated artifact is governed as sealed output; its generator is governed as what determines it. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A design schedules the artifact and names the generator as the means. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Construction reaches a generated artifact by invoking its generator. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A template and the code that reads it are one generator, not two. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| An artifact's agreement with its generator is a build gate, not a habit. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Whether an artifact is generated is a fact about that artifact, not a decision this change makes. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| This change governs generation; it does not judge whether generating is a good idea. | HIGH | CR seed §4 Known Facts — Business Truths #8 |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|--------|----------------|-------------------|--------------|
| Some artifacts of this domain are produced by a generator rather than written. | The whole of this change. | Confirm which artifacts are generated and what produces them. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| A design has no way to say that an artifact is produced from something else. | Determines whether this adds a register or changes a rule. | Establish what a design can say today about how an artifact is reached. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Construction renders an artifact from the design alone, and would overwrite a generated one. | Says why the delivery path is unusable for these artifacts. | Confirm how construction produces an artifact. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| A generated artifact's agreement with its generator can be checked, and nothing requires the check. | Says how large the gap is: the mechanism exists and is not in force. | Establish whether an agreement check exists and whether any build requires it. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Two changes to this domain have already been designed and delivered by hand because of this. | Establishes the defect occurred rather than being foreseen. | Confirm both, and that each stopped for this reason. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|------------|-------|--------------|
| Every generated artifact in this domain has exactly one generator. | Each phase's rule set is produced from one template and one declaration. | CR seed §6 Assumptions #1 |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source | Source Finding |
|------------|--------|--------------|
| A generated artifact is never edited directly, by this change or any other. | Business author | CR seed §7 Constraints #1 |
| Construction may not become a second producer of an artifact a generator already produces. | Business author | CR seed §7 Constraints #2 |
| No verdict changes for an authored artifact. This change concerns generated ones. | Business author | CR seed §7 Constraints #3 |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|-----------|--------------|
| A generator is authoritative over the artifact it produces. | CR seed §8 Business Invariants #1 |
| An artifact and the generator that produced it agree, and the build refuses when they do not. | CR seed §8 Business Invariants #2 |
| One artifact has one generator. | CR seed §8 Business Invariants #3 |
| A change to a generated artifact is delivered by changing its generator. | CR seed §8 Business Invariants #4 |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|--------|-------|---------|--------------|
| Generated artifact | In agreement | It matches what generated it. | CR seed §9 Lifecycle States #1 |
| Generated artifact | Stale | It does not, and the build refuses. | CR seed §9 Lifecycle States #2 |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-------|----------------|--------------|--------------|
| An artifact was regenerated | When a generator is invoked and its artifact rewritten | The artifact and its generator agree again. | CR seed §10 Business Events #1 |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|-----------------|---------------------|--------------|
| A generated artifact's content | Its generator | CR seed §11 Authority Boundaries #1 |
| Which artifacts are generated | Each artifact, as a fact about itself | CR seed §11 Authority Boundaries #2 |
| How construction reaches an artifact | design | CR seed §11 Authority Boundaries #3 |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason | Source Finding |
|------|--------|--------------|
| Whether generating an artifact is a good idea | It is done today; this change governs it rather than judging it. | CR seed §12 Out of Scope #1 |
| Which artifacts are generated | A fact about each artifact, not a decision here. | CR seed §12 Out of Scope #2 |
| How rules are declared | The template and the code are what they are. | CR seed §12 Out of Scope #3 |
| How a document authored under one rule set is judged under a later one | A separate problem with its own change. | CR seed §12 Out of Scope #4 |
| Whether a design can state an artifact it amends | A separate problem with its own change. | CR seed §12 Out of Scope #5 |
| Generated artifacts outside this lifecycle | Nothing has needed it yet. | CR seed §12 Out of Scope #6 |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|------------|--------------|--------------|
| design | MODIFIED | CR seed §13 Governance Scope #1 |
| build | ADJACENT | CR seed §13 Governance Scope #2 |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|----------|------------|----------|-------|--------------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|-----------|--------------|
| A design can name the generator an artifact is produced from, and is refused if it names none for an artifact that has one. | CR seed §15 Acceptance Criteria #1 |
| Construction reaches a generated artifact by invoking its generator, and never writes one directly. | CR seed §15 Acceptance Criteria #2 |
| A build refuses when an artifact and its generator disagree. | CR seed §15 Acceptance Criteria #3 |
| A change to a phase's rule set is delivered through the pipeline rather than by hand. | CR seed §15 Acceptance Criteria #4 |
| No verdict changes for an artifact that is authored rather than generated. | CR seed §15 Acceptance Criteria #5 |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|-----------------|---------------|-----------------------|--------------|
| Generator | What it produces from, together with the mechanism that produces | They produce the same artifact from the same source. | CR seed §16 Identity and Sameness #1 |
| Generated artifact | Its own identity | They are the same artifact. | CR seed §16 Identity and Sameness #2 |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|--------|------------|----------|--------------|---------|--------------|
| Generated artifact | In agreement | Stale | Its generator changing without it being regenerated. | The build refuses. Nothing else follows. | CR seed §17 Lifecycle Transitions #1 |
| Generated artifact | Stale | In agreement | Its generator being invoked. | A moment is recorded. Nothing else follows. | CR seed §17 Lifecycle Transitions #2 |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|-----------|--------------|-----------------|--------------|
| Building | An artifact and its generator disagree | The artifact carries a copy of what determines it, and a stale copy reports confidently on the wrong thing. | CR seed §18 Operation Refusals #1 |
| Constructing an artifact | It is generated and construction would write it directly | Two producers of one artifact drift, and the generator is authoritative. | CR seed §18 Operation Refusals #2 |
| Scheduling | A design names a generated artifact and no generator | The design would not say how the artifact is reached. | CR seed §18 Operation Refusals #3 |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|-----------------|-------------|-------|--------------|
| Generated artifacts outside this lifecycle | A later change | Something outside it is generated. | CR seed §19 Authority Deferrals #1 |
| Which artifacts are generated | Each artifact | It declares what it is. | CR seed §19 Authority Deferrals #2 |

