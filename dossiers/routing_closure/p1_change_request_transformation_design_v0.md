# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** routing_closure
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
| design | MODIFY | A phase that asks the composition a question does not answer the case that nothing was found. Nothing is added to what a phase judges. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Phase | One stage a change document passes through, judged against its own rules. | CR seed §2 Business Vocabulary #1 |
| Observation | A question a phase asks the composition about itself before it judges. | CR seed §2 Business Vocabulary #2 |
| Nothing found | The answer an observation gives when what was asked about does not exist. | CR seed §2 Business Vocabulary #3 |
| Judgement | A phase's verdict on a document: judged, or rejected. | CR seed §2 Business Vocabulary #4 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A phase's judgement ends as rejected when an observation reports that nothing was found. | CR seed §3 Requested Outcomes #1 |
| Every way an observation can answer is one the phase answers, now and when another is added. | CR seed §3 Requested Outcomes #2 |
| Every judgement on observations that succeed is unchanged. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A phase either judges a document or rejects it. There is no third ending. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A phase that cannot observe what it judges against does not judge. It rejects. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A rule judging against an observation that did not arrive reports nothing, and nothing is indistinguishable from a pass. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The capability a phase asks can answer in four ways: an answer, a refused question, a failure to reach the composition, and nothing found. | HIGH | CR seed §4 Known Facts — Business Truths #4 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Every step that asks the composition a question answers three of the four ways, and not nothing found. | A step that does not answer an outcome carries on past it. | Establish which outcomes each observing step answers. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The phase workflows route a judgement, a refusal and a failed observation, and not nothing found. | An outcome no route answers stops the phase with no declared ending. | Establish what each phase workflow routes. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The observing steps and the routing are written by hand beside a generator that writes the rest of the same artifacts. | A hand-kept copy falls behind the thing it copies. | Establish what the generator writes and what it leaves. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |

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
| Every judgement on observations that succeed is unchanged. | Business author | CR seed §7 Constraints #1 |
| No phase gains an ending. | Business author — a phase judges or rejects. | CR seed §7 Constraints #2 |
| The answers are generated, not written beside the generator. | Business author — a hand-kept copy is the gap this change closes. | CR seed §7 Constraints #3 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No phase judges against an observation that did not arrive. | CR seed §8 Business Invariants #1 |
| Every way an observation can answer is answered. | CR seed §8 Business Invariants #2 |
| Every phase ends as judged or rejected. | CR seed §8 Business Invariants #3 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Document | Judged | A phase reached a verdict on it. Unchanged by this change. | CR seed §9 Lifecycle States #1 |
| Document | Rejected | A phase refused to judge it, or found it inadmissible. Unchanged by this change. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| NONE IDENTIFIED | This change recognises no new moment. | A phase announces nothing it did not announce before. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a phase does when an observation finds nothing | Design | CR seed §11 Authority Boundaries #1 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| What each phase judges | No rule changes. | CR seed §12 Out of Scope #1 |
| The capability's own answers | The platform declares them; this change answers them. | CR seed §12 Out of Scope #2 |
| Phases that ask the composition nothing | They have no observation to answer. | CR seed §12 Out of Scope #3 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| design | MODIFIED | CR seed §13 Governance Scope #1 |
| build | ADJACENT | CR seed §13 Governance Scope #2 |

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
| A phase whose observation reports that nothing was found ends as rejected, and judges nothing. | CR seed §15 Acceptance Criteria #1 |
| Every way the observing capability can answer is answered by every observing step and routed by every phase. | CR seed §15 Acceptance Criteria #2 |
| Adding a way of answering to the observing capability leaves no phase that does not answer it. | CR seed §15 Acceptance Criteria #3 |
| Every phase judges every document it judged before this change exactly as it did. | CR seed §15 Acceptance Criteria #4 |

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
| Judging a document | An observation reports that nothing was found | A rule judging against an observation that did not arrive reports nothing. | CR seed §18 Operation Refusals #1 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| NONE IDENTIFIED |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
