# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** declared_reach
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the four clarifications its
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
| design | MODIFY | The platform admits an act that reads records another part of the business owns, and a design cannot state one. A change needing it has no way to say so, and the ways available are all wrong. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Act | Something the business does as one unit, which completes or is refused. |
| Reach | An act reading records another part of the business owns. |
| Binding | What connects an act, when it runs, to the descriptions of the records it works against. |
| Owned | The records an act writes, described by the part of the business answerable for them. |
| Consulted | The records an act reads and never writes. |
| Declaration | What a design states, which a reviewer reads and construction renders. |
| Derivation | A fact read from the composition rather than restated in a design. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A design can state the bindings an act consults, alongside the one it owns. |
| Construction renders what the design states, so the built act declares the reach the design declared. |
| A design whose act reads records it never declared a reach to is refused. |
| A design that declares a reach nothing uses is refused. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A reach is stated in a register of its own, kept structurally distinct from the records an act owns. | HIGH |
| A design names the binding it consults and never the records behind it; those are derived from the composition. | HIGH |
| Restating another part's records in the reaching act's design would be a second copy maintained by someone other than their owner. | HIGH |
| A design whose act reads records it declared no reach to is refused, and the reading is derived from what the composition publishes rather than guessed. | HIGH |
| Every declared reach is used by at least one read the act performs; a reach is a scoped permission, not a reserve. | HIGH |
| The declared set and the used set are the same set: an act reaches nothing it did not declare and declares nothing it does not reach. | HIGH |
| A reach added to a built artifact by hand works, passes every check, and is a reach no reviewer saw. | HIGH |
| A rule resting on a name or on what an implementation does is a convention anybody can break by naming something well. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| A design states one binding per act and has no register for a second. | The whole of this change. | Establish what a design states today about where an act's records live. |
| The platform admits an act that declares the bindings it consults, and refuses a write through one. | Says the capability exists and this change states it rather than inventing it. | Confirm what the platform admits, and what it does when an act writes through a reach. |
| A change exists that needs a reach, is raised and pinned, and stops where it would state one. | Establishes the requirement occurred rather than being foreseen. | Confirm the change, and confirm what stops it. |
| The composition publishes which records a binding covers, and which records a composed capability reads. | Decides whether the rules can derive what a design must not restate. | Establish what is published about stores, bindings and the operations that address them. |
| The rules that judge a design already refuse a reach in one direction, and have no counterpart for storage. | Says the shape exists and what is missing beside it. | Confirm the existing rule and what it reasons from. |
| The document that judges a design is produced by a generator rather than written. | Says how this change is delivered, and that the path has never been used. | Confirm the artifact is generated, and whether any change has been delivered through that path. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| An act reaches few bindings, named when it is designed, rather than a set discovered as it runs. | The platform resolves them when the composition is sealed, so they are known before anything runs. |
| A capability's reading is fixed by its declaration and does not vary per call. | A capability contract is a fixed sequence with no branching over which records it addresses. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Ownership and reach are structurally distinct, never one register with a column telling them apart. | Business author |
| A design names a binding and never the records behind it. | Business author |
| What a rule checks is derived from the composition, never inferred from a name or an implementation. | Business author |
| Every declared reach is used, and every read is declared. | Business author |
| A reach is never added to a built artifact by hand. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| An act declares the bindings it consults, in a register kept apart from the one it owns. |
| A design names a binding; the records it covers are derived from the composition. |
| An act reads nothing it did not declare a reach to. |
| Every reach an act declares is used by a read that act performs. |
| What a design states about reach is what the built act carries. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Reach | Undeclarable | The design language has no register for it, which is the state this change ends. |
| Reach | Declared | A design states the binding an act consults, and a reviewer reads it there. |
| Reach | Rendered | Construction has emitted the declaration into the built act. |
| Reach | Unused | Declared and consumed by no read, which is refused. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A design declared a reach | A design states a binding its act consults | The act's whole storage surface is visible before anything is built. |
| A design was refused for an undeclared read | A design's act reads records it declared no reach to | The defect is caught where a reviewer sees it rather than when the act runs. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a design may state | design |
| Which records a binding covers | The part of the business that owns them |
| Whether a reach is permitted at all | The platform |
| Which acts reach which records | The domain raising the change |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Which acts reach which records | Each domain's business, stated in its own change. |
| How the composition resolves a reach | The platform decided that; the design language states it. |
| Whether a reach may cross a domain | Settled by the platform: it may not. |
| Whether an act may write through a reach | Settled by the platform: it may not, and the refusal already runs. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| design | MODIFIED |
| build | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A design can state the bindings its act consults, and a reviewer reads them in the design. |
| The built act carries the reach the design declared, without anyone editing it. |
| A design whose act reads records it declared no reach to is refused, naming the records and the act. |
| A design declaring a reach that no read uses is refused. |
| A design that declares no reach is judged exactly as it is today. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Reach | The act that reaches and the binding it consults | One act names one binding, however many records it reads there. |
| Binding | Its own identity | They are the same binding. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Reach | Undeclarable | Declared | A design stating the binding its act consults. | Nothing else follows. The act does what it would have done, and now says so. |
| Reach | Declared | Rendered | Construction emitting the declaration into the built act. | The act resolves the records it consults when it runs, and a write through them is refused by the platform. |
| Reach | Declared | Unused | Every read that used it being removed from the act. | The design is refused. Nothing is silently dropped. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Judging a design | Its act reads records it declared no reach to | The reach would be invisible until the act ran, which is the defect this change removes. |
| Judging a design | It declares a reach no read uses | A permission granted for nothing is a permission nobody reviewed the purpose of. |
| Delivering a reach | It is added to a built artifact by hand | A reach no reviewer saw defeats the reason for declaring one. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Which acts reach which records | Each domain | That domain raises the change that needs a reach. |
| Whether a reach may cross a domain | The platform | Something needs one, which nothing does. |
