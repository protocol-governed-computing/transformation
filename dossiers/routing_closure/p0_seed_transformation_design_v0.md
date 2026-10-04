# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** routing_closure
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarification its
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
| design | MODIFY | A phase that asks the composition a question does not answer the case that nothing was found. Nothing is added to what a phase judges. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Phase | One stage a change document passes through, judged against its own rules. |
| Observation | A question a phase asks the composition about itself before it judges. |
| Nothing found | The answer an observation gives when what was asked about does not exist. |
| Judgement | A phase's verdict on a document: judged, or rejected. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A phase's judgement ends as rejected when an observation reports that nothing was found. |
| Every way an observation can answer is one the phase answers, now and when another is added. |
| Every judgement on observations that succeed is unchanged. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A phase either judges a document or rejects it. There is no third ending. | HIGH |
| A phase that cannot observe what it judges against does not judge. It rejects. | HIGH |
| A rule judging against an observation that did not arrive reports nothing, and nothing is indistinguishable from a pass. | HIGH |
| The capability a phase asks can answer in four ways: an answer, a refused question, a failure to reach the composition, and nothing found. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Every step that asks the composition a question answers three of the four ways, and not nothing found. | A step that does not answer an outcome carries on past it. | Establish which outcomes each observing step answers. |
| The phase workflows route a judgement, a refusal and a failed observation, and not nothing found. | An outcome no route answers stops the phase with no declared ending. | Establish what each phase workflow routes. |
| The observing steps and the routing are written by hand beside a generator that writes the rest of the same artifacts. | A hand-kept copy falls behind the thing it copies. | Establish what the generator writes and what it leaves. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Every judgement on observations that succeed is unchanged. | Business author |
| No phase gains an ending. | Business author — a phase judges or rejects. |
| The answers are generated, not written beside the generator. | Business author — a hand-kept copy is the gap this change closes. |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No phase judges against an observation that did not arrive. |
| Every way an observation can answer is answered. |
| Every phase ends as judged or rejected. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Document | Judged | A phase reached a verdict on it. Unchanged by this change. |
| Document | Rejected | A phase refused to judge it, or found it inadmissible. Unchanged by this change. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | This change recognises no new moment. | A phase announces nothing it did not announce before. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a phase does when an observation finds nothing | Design |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| What each phase judges | No rule changes. |
| The capability's own answers | The platform declares them; this change answers them. |
| Phases that ask the composition nothing | They have no observation to answer. |

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
| A phase whose observation reports that nothing was found ends as rejected, and judges nothing. |
| Every way the observing capability can answer is answered by every observing step and routed by every phase. |
| Adding a way of answering to the observing capability leaves no phase that does not answer it. |
| Every phase judges every document it judged before this change exactly as it did. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED | | |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| NONE IDENTIFIED | | | | |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Judging a document | An observation reports that nothing was found | A rule judging against an observation that did not arrive reports nothing. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| NONE IDENTIFIED | | |
