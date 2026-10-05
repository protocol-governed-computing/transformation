# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design and build
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** semantic_change
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
| design | MODIFY | A design cannot re-point a reference without restating the artifact that holds it, and may withdraw a fact from an artifact it amends. | CR seed §1 CR Type #1 |
| build | MODIFY | Construction builds an amendment that changes meaning, skips the comparison without the composition, and does not ask what a replaced artifact reaches. | CR seed §1 CR Type #2 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Amendment | A change that restates an artifact under the identity it has. | CR seed §2 Business Vocabulary #1 |
| Replacement | A change that gives an artifact a new identity standing in for the old one. | CR seed §2 Business Vocabulary #2 |
| Meaning | What a declaration commits the artifact to, read by the rules the platform declares. | CR seed §2 Business Vocabulary #3 |
| Referrer | An artifact that names another. | CR seed §2 Business Vocabulary #4 |
| Re-point | Changing which artifact a referrer names, and nothing else about it. | CR seed §2 Business Vocabulary #5 |
| Reference part | A part of a declaration the platform declares names another artifact. | CR seed §2 Business Vocabulary #6 |
| Caller | Something outside the composition that names an artifact, such as a request sent to it. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| An amendment that changes what an artifact means is refused when it is built. | CR seed §3 Requested Outcomes #1 |
| An amendment that cannot be compared with the composition is refused when it is built. | CR seed §3 Requested Outcomes #2 |
| A design can no longer withdraw a fact from an artifact it amends. | CR seed §3 Requested Outcomes #3 |
| A design can re-point a reference to a replaced artifact without restating the artifact that holds it. | CR seed §3 Requested Outcomes #4 |
| A design that leaves a reference to an artifact it replaces unaccounted for is refused when it is built. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A change of meaning is a new identity; a change of how it is written is not. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| What carries no meaning is what the platform declares, and nothing else. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A reference to a replaced artifact is re-pointed or retired. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Re-pointing keeps the referring artifact's identity. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A caller outside the composition moves itself, and a change lists the callers it knows of. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| What carries no meaning, what names another artifact, and how two declarations are compared are the platform's declaration. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| A withdrawal from an amended artifact is a change of meaning. | HIGH | CR seed §4 Known Facts — Business Truths #7 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Construction compares an amendment with the artifact it restates only for what the amendment would lose, and only when handed the composition. | A change of meaning that adds or alters something is built, and so is any amendment built without the composition. | Establish what construction compares, and when. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| A design can name a referrer only by restating it. | A referrer the design language cannot express cannot be re-pointed. | Establish which actions a design may take on an artifact it holds. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The composition's record of references names every artifact that names another. | A replacement learns what it reaches from that record. | Establish that inspection reports every referrer. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Nothing in the design checks what a replaced artifact reaches. | The compiler refuses late, after the design is approved. | Establish where references to a replaced artifact are first refused. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

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
| A re-point changes the one reference and nothing else in the referring artifact. | Business author | CR seed §7 Constraints #1 |
| Every change that is built today and keeps its meaning is built exactly as it is today. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No change of meaning is built under an old identity. | CR seed §8 Business Invariants #1 |
| No reference to a replaced artifact survives a change unaccounted for. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Artifact | In force | Reachable and referable. Unchanged by this change. | CR seed §9 Lifecycle States #1 |
| Artifact | Replaced | Stood down by a successor and out of reach. Unchanged by this change. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| NONE IDENTIFIED |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Which parts of a declaration carry no meaning | The platform's artifact subdomain | CR seed §11 Authority Boundaries #1 |
| Which parts of a declaration name another artifact | The platform's artifact subdomain | CR seed §11 Authority Boundaries #2 |
| How two declarations are compared | The platform's artifact subdomain | CR seed §11 Authority Boundaries #3 |
| Whether a design may be built | Build | CR seed §11 Authority Boundaries #4 |
| What a design may say | Design | CR seed §11 Authority Boundaries #5 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Deciding which past changes altered meaning | The next change. | CR seed §12 Out of Scope #1 |
| Comparing a whole composition with the one last published | Not part of this change. | CR seed §12 Out of Scope #2 |
| Moving callers outside the composition | Each caller moves itself. | CR seed §12 Out of Scope #3 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| design | MODIFIED | CR seed §13 Governance Scope #1 |
| build | MODIFIED | CR seed §13 Governance Scope #2 |
| artifact | ADJACENT | CR seed §13 Governance Scope #3 |

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
| An amendment that adds, removes or alters anything that carries meaning is refused when it is built, and the refusal names what changed. | CR seed §15 Acceptance Criteria #1 |
| An amendment that changes only explanation, or only the order of an unordered list, is built. | CR seed §15 Acceptance Criteria #2 |
| An amendment that changes a part declared explanation from text to anything else is refused. | CR seed §15 Acceptance Criteria #3 |
| A re-point that names the declared successor of what it named is built, and the referrer keeps its identity. | CR seed §15 Acceptance Criteria #4 |
| A design re-points a reference without restating the referrer, and only that reference changes. | CR seed §15 Acceptance Criteria #5 |
| A design that replaces an artifact and leaves one of its referrers unaccounted for is refused when it is built, and the refusal names the referrer. | CR seed §15 Acceptance Criteria #6 |
| An amendment built without the composition is refused, and the refusal says why. | CR seed §15 Acceptance Criteria #7 |
| A design that withdraws a fact is refused. | CR seed §15 Acceptance Criteria #8 |
| A comparison is refused when the platform declares a rule it does not apply. | CR seed §15 Acceptance Criteria #9 |
| Every delivered design that keeps meaning builds exactly as it does today. | CR seed §15 Acceptance Criteria #10 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Artifact meaning | The artifact's declaration | Everything not declared explanation is equal, unordered lists hold the same members, and each reference names the same artifact or its declared successor | CR seed §16 Identity and Sameness #1 |

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
| Building a design | An amendment changes what an artifact means | A change of meaning is a new identity. | CR seed §18 Operation Refusals #1 |
| Building a design | An amendment cannot be compared with the composition | An uncompared amendment could change meaning unseen. | CR seed §18 Operation Refusals #2 |
| Building a design | A design withdraws a fact from an artifact it amends | A withdrawal is a change of meaning. | CR seed §18 Operation Refusals #3 |
| Building a design | A reference to an artifact it replaces is left unaccounted for | A reference to a replaced artifact is re-pointed or retired. | CR seed §18 Operation Refusals #4 |

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
