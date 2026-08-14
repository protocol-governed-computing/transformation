# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** declared_reach
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
| design | MODIFY | The platform admits an act that reads records another part of the business owns, and a design cannot state one. A change needing it has no way to say so, and the ways available are all wrong. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Act | Something the business does as one unit, which completes or is refused. | CR seed §2 Business Vocabulary #1 |
| Reach | An act reading records another part of the business owns. | CR seed §2 Business Vocabulary #2 |
| Binding | What connects an act, when it runs, to the descriptions of the records it works against. | CR seed §2 Business Vocabulary #3 |
| Owned | The records an act writes, described by the part of the business answerable for them. | CR seed §2 Business Vocabulary #4 |
| Consulted | The records an act reads and never writes. | CR seed §2 Business Vocabulary #5 |
| Declaration | What a design states, which a reviewer reads and construction renders. | CR seed §2 Business Vocabulary #6 |
| Derivation | A fact read from the composition rather than restated in a design. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A design can state the bindings an act consults, alongside the one it owns. | CR seed §3 Requested Outcomes #1 |
| Construction renders what the design states, so the built act declares the reach the design declared. | CR seed §3 Requested Outcomes #2 |
| A design whose act reads records it never declared a reach to is refused. | CR seed §3 Requested Outcomes #3 |
| A design that declares a reach nothing uses is refused. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A reach is stated in a register of its own, kept structurally distinct from the records an act owns. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A design names the binding it consults and never the records behind it; those are derived from the composition. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Restating another part's records in the reaching act's design would be a second copy maintained by someone other than their owner. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A design whose act reads records it declared no reach to is refused, and the reading is derived from what the composition publishes rather than guessed. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Every declared reach is used by at least one read the act performs; a reach is a scoped permission, not a reserve. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| The declared set and the used set are the same set: an act reaches nothing it did not declare and declares nothing it does not reach. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| A reach added to a built artifact by hand works, passes every check, and is a reach no reviewer saw. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A rule resting on a name or on what an implementation does is a convention anybody can break by naming something well. | HIGH | CR seed §4 Known Facts — Business Truths #8 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| A design states one binding per act and has no register for a second. | The whole of this change. | Establish what a design states today about where an act's records live. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The platform admits an act that declares the bindings it consults, and refuses a write through one. | Says the capability exists and this change states it rather than inventing it. | Confirm what the platform admits, and what it does when an act writes through a reach. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| A change exists that needs a reach, is raised and pinned, and stops where it would state one. | Establishes the requirement occurred rather than being foreseen. | Confirm the change, and confirm what stops it. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The composition publishes which records a binding covers, and which records a composed capability reads. | Decides whether the rules can derive what a design must not restate. | Establish what is published about stores, bindings and the operations that address them. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The rules that judge a design already refuse a reach in one direction, and have no counterpart for storage. | Says the shape exists and what is missing beside it. | Confirm the existing rule and what it reasons from. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| The document that judges a design is produced by a generator rather than written. | Says how this change is delivered, and that the path has never been used. | Confirm the artifact is generated, and whether any change has been delivered through that path. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| An act reaches few bindings, named when it is designed, rather than a set discovered as it runs. | The platform resolves them when the composition is sealed, so they are known before anything runs. | CR seed §6 Assumptions #1 |
| A capability's reading is fixed by its declaration and does not vary per call. | A capability contract is a fixed sequence with no branching over which records it addresses. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Ownership and reach are structurally distinct, never one register with a column telling them apart. | Business author | CR seed §7 Constraints #1 |
| A design names a binding and never the records behind it. | Business author | CR seed §7 Constraints #2 |
| What a rule checks is derived from the composition, never inferred from a name or an implementation. | Business author | CR seed §7 Constraints #3 |
| Every declared reach is used, and every read is declared. | Business author | CR seed §7 Constraints #4 |
| A reach is never added to a built artifact by hand. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| An act declares the bindings it consults, in a register kept apart from the one it owns. | CR seed §8 Business Invariants #1 |
| A design names a binding; the records it covers are derived from the composition. | CR seed §8 Business Invariants #2 |
| An act reads nothing it did not declare a reach to. | CR seed §8 Business Invariants #3 |
| Every reach an act declares is used by a read that act performs. | CR seed §8 Business Invariants #4 |
| What a design states about reach is what the built act carries. | CR seed §8 Business Invariants #5 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Reach | Undeclarable | The design language has no register for it, which is the state this change ends. | CR seed §9 Lifecycle States #1 |
| Reach | Declared | A design states the binding an act consults, and a reviewer reads it there. | CR seed §9 Lifecycle States #2 |
| Reach | Rendered | Construction has emitted the declaration into the built act. | CR seed §9 Lifecycle States #3 |
| Reach | Unused | Declared and consumed by no read, which is refused. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A design declared a reach | A design states a binding its act consults | The act's whole storage surface is visible before anything is built. | CR seed §10 Business Events #1 |
| A design was refused for an undeclared read | A design's act reads records it declared no reach to | The defect is caught where a reviewer sees it rather than when the act runs. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a design may state | design | CR seed §11 Authority Boundaries #1 |
| Which records a binding covers | The part of the business that owns them | CR seed §11 Authority Boundaries #2 |
| Whether a reach is permitted at all | The platform | CR seed §11 Authority Boundaries #3 |
| Which acts reach which records | The domain raising the change | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Which acts reach which records | Each domain's business, stated in its own change. | CR seed §12 Out of Scope #1 |
| How the composition resolves a reach | The platform decided that; the design language states it. | CR seed §12 Out of Scope #2 |
| Whether a reach may cross a domain | Settled by the platform: it may not. | CR seed §12 Out of Scope #3 |
| Whether an act may write through a reach | Settled by the platform: it may not, and the refusal already runs. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| design | MODIFIED | CR seed §13 Governance Scope #1 |
| build | MODIFIED | CR seed §13 Governance Scope #2 |

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
| A design can state the bindings its act consults, and a reviewer reads them in the design. | CR seed §15 Acceptance Criteria #1 |
| The built act carries the reach the design declared, without anyone editing it. | CR seed §15 Acceptance Criteria #2 |
| A design whose act reads records it declared no reach to is refused, naming the records and the act. | CR seed §15 Acceptance Criteria #3 |
| A design declaring a reach that no read uses is refused. | CR seed §15 Acceptance Criteria #4 |
| A design that declares no reach is judged exactly as it is today. | CR seed §15 Acceptance Criteria #5 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Reach | The act that reaches and the binding it consults | One act names one binding, however many records it reads there. | CR seed §16 Identity and Sameness #1 |
| Binding | Its own identity | They are the same binding. | CR seed §16 Identity and Sameness #2 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Reach | Undeclarable | Declared | A design stating the binding its act consults. | Nothing else follows. The act does what it would have done, and now says so. | CR seed §17 Lifecycle Transitions #1 |
| Reach | Declared | Rendered | Construction emitting the declaration into the built act. | The act resolves the records it consults when it runs, and a write through them is refused by the platform. | CR seed §17 Lifecycle Transitions #2 |
| Reach | Declared | Unused | Every read that used it being removed from the act. | The design is refused. Nothing is silently dropped. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Judging a design | Its act reads records it declared no reach to | The reach would be invisible until the act ran, which is the defect this change removes. | CR seed §18 Operation Refusals #1 |
| Judging a design | It declares a reach no read uses | A permission granted for nothing is a permission nobody reviewed the purpose of. | CR seed §18 Operation Refusals #2 |
| Delivering a reach | It is added to a built artifact by hand | A reach no reviewer saw defeats the reason for declaring one. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Which acts reach which records | Each domain | That domain raises the change that needs a reach. | CR seed §19 Authority Deferrals #1 |
| Whether a reach may cross a domain | The platform | Something needs one, which nothing does. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
