# Change Seed — transformation / design and build

**Stage:** 0 — Change Seed
**CR:** semantic_change
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
| design | MODIFY | A design cannot say that it re-points a reference without restating the artifact that holds it. |
| build | MODIFY | Construction builds an amendment that changes meaning, and does not ask what a replaced artifact reaches. |
| artifact | MODIFY | The platform does not declare which parts of a declaration name another artifact, nor that explanation is exempt only where it is text. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Amendment | A change that restates an artifact under the identity it has. |
| Replacement | A change that gives an artifact a new identity standing in for the old one. |
| Meaning | What a declaration commits the artifact to, which is everything the platform does not declare explanation or unordered. |
| Referrer | An artifact that names another. |
| Re-point | Changing which artifact a referrer names, and nothing else about it. |
| Reference part | A part of a declaration whose value names another artifact. |
| Caller | Something outside the composition that names an artifact, such as a request sent to it. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The platform declares which parts of a declaration name another artifact, and that a reference now naming the declared successor of what it named is not a change of meaning. |
| The platform declares that a part declared explanation is exempt only where its value is text. |
| An amendment that changes what an artifact means is refused when it is built. |
| A design can re-point a reference to a replaced artifact without restating the artifact that holds it. |
| A design that leaves a reference to an artifact it replaces unaccounted for is refused when it is built. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A change of meaning is a new identity; a change of how it is written is not. | HIGH |
| What carries no meaning is what the platform declares, and nothing else. | HIGH |
| A reference to a replaced artifact is re-pointed or retired. | HIGH |
| Re-pointing keeps the referring artifact's identity. | HIGH |
| A caller outside the composition moves itself, and a change lists the callers it knows of. | HIGH |
| A part declared explanation is exempt only where its value is text. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Construction compares an amendment with the artifact it restates only for what the amendment would lose. | A change of meaning that adds or alters something is built. | Establish what construction compares. |
| A design can name a referrer only by restating it. | A referrer the design language cannot express cannot be re-pointed. | Establish which actions a design may take on an artifact it holds. |
| The platform's declaration does not say which parts name another artifact. | Without it, a re-point reads as a change of meaning, and every replacement ripples upward. | Establish what the declaration holds and what consults it. |
| Nothing in the design checks what a replaced artifact reaches. | The compiler refuses late, after the design is approved. | Establish where references to a replaced artifact are first refused. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| A re-point changes the one reference and nothing else in the referring artifact. | Business author |
| Every change that is built today and keeps its meaning is built exactly as it is today. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No change of meaning is built under an old identity. |
| No reference to a replaced artifact survives a change unaccounted for. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Artifact | In force | Reachable and referable. Unchanged by this change. |
| Artifact | Replaced | Stood down by a successor and out of reach. Unchanged by this change. |
| Declaration of what carries no meaning | In force | Consulted when two declarations are compared. |
| Declaration of what carries no meaning | Replaced | Stood down by the version this change adds. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | | |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Which parts of a declaration carry no meaning | The platform's artifact subdomain |
| Which parts of a declaration name another artifact | The platform's artifact subdomain |
| Whether a design may be built | Build |
| What a design may say | Design |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Deciding which past changes altered meaning | The next change. |
| Comparing a whole composition with the one last cited | The release process. |
| Moving callers outside the composition | Each caller moves itself. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| design | MODIFIED |
| build | MODIFIED |
| artifact | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| The platform's declaration names every part of a declaration that names another artifact, and states that explanation is exempt only where it is text. |
| The new declaration replaces the old one, which stays retained and out of reach. |
| An amendment that adds, removes or alters anything that carries meaning is refused when it is built, and the refusal names what changed. |
| An amendment that changes only explanation, or only the order of an unordered list, is built. |
| An amendment that changes a part declared explanation from text to anything else is refused. |
| A re-point that names the declared successor of what it named is built, and the referrer keeps its identity. |
| A design re-points a reference without restating the referrer, and only that reference changes. |
| A design that replaces an artifact and leaves one of its referrers unaccounted for is refused when it is built, and the refusal names the referrer. |
| Every delivered design that keeps meaning builds exactly as it does today. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Artifact meaning | The artifact's declaration | Everything not declared explanation is equal, unordered lists hold the same members, and each reference names the same artifact or its declared successor |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Declaration of what carries no meaning | In force | Replaced | This change adds its successor | Every reference to it is re-pointed to the successor |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building a design | An amendment changes what an artifact means | A change of meaning is a new identity. |
| Building a design | A reference to an artifact it replaces is left unaccounted for | A reference to a replaced artifact is re-pointed or retired. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| NONE IDENTIFIED | | |
