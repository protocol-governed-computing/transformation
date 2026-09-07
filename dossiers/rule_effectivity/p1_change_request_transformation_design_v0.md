# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was said in.
S1 interrogates and does not author.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|-----------|----------------|-----------|--------------|
| design | MODIFY | Every rule applies to every document that has ever existed, and nothing records which rules a document was approved under. An approval cannot be told from a migration, and a correction cannot say whom it affects. | CR seed §1 CR Type #1 |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|------|------------|--------------|
| Rule set | What a phase judges a document against, at a moment in time. | CR seed §2 Business Vocabulary #1 |
| Rule-set version | A named state of the rule set. A new one exists only when a change can alter a prior dossier's admissibility. | CR seed §2 Business Vocabulary #2 |
| Effectivity | A correction's own declaration of whether it is retroactive or not. | CR seed §2 Business Vocabulary #3 |
| Retroactive | A correction that can alter a prior dossier's admissibility. | CR seed §2 Business Vocabulary #4 |
| Non-retroactive | One that cannot. | CR seed §2 Business Vocabulary #5 |
| Approved | Closed under a rule-set version, and still so. | CR seed §2 Business Vocabulary #6 |
| Migrated | Amended to satisfy a later rule set. It passes now and was taught to. | CR seed §2 Business Vocabulary #7 |
| Re-approved | Re-judged whole under a later rule set and re-gated by a person. | CR seed §2 Business Vocabulary #8 |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|---------|--------------|
| A correction declares whether it is retroactive, and the rule set records the declaration. | CR seed §3 Requested Outcomes #1 |
| A rule-set version exists only where a change can alter a prior dossier's admissibility. | CR seed §3 Requested Outcomes #2 |
| Every approval pins the rule-set version it was given under. | CR seed §3 Requested Outcomes #3 |
| A retroactive change names the dossiers it affects, each to be migrated or re-approved. | CR seed §3 Requested Outcomes #4 |
| A migrated dossier is distinguishable from one approved under the rules it satisfies. | CR seed §3 Requested Outcomes #5 |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|------|-----------|--------------|
| An approval remains valid under the rules it was given. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Re-evaluation under later rules is a separate act, and is recorded. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A new rule-set version exists only when a change can alter a prior dossier's admissibility. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A correction declares its own effectivity: retroactive or non-retroactive. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| The rule set records that declaration as governed history. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Each approval pins the rule-set version it was given under. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| A retroactive change creates a version and names the dossiers it affects. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A non-retroactive correction creates no version, names no dossier, and disturbs none. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| There are three states, not two: approved, migrated, re-approved. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A document is judged under the rules it was authored under and under current rules, and the two answer different questions. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| A completed change may be left at the version it was approved under. | HIGH | CR seed §4 Known Facts — Business Truths #11 |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|--------|----------------|-------------------|--------------|
| A document is judged only against the rules in force when it is judged. | The whole of this change. | Confirm what a verdict is rendered against, and whether it states which rules it used. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Nothing records which rules a document was approved under. | Without it no distinction between approved and migrated is recordable. | Establish whether any document carries a rule-set version. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| A correction cannot say whether it is retroactive. | Determines whether this adds a declaration or changes a rule. | Establish what a change can state today about its own effect on prior documents. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Dossiers have already been amended to satisfy rules written after their approval, and nothing in them says so. | Establishes the defect occurred rather than being foreseen. | Confirm which dossiers were amended and what records it. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| A rule set has no version at all. | Says how much of this is new rather than corrected. | Establish whether the rule set is versioned in any form. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|------------|-------|--------------|
| Whether a change can alter a prior dossier's admissibility is knowable by whoever makes the change. | A change knows what it added and why. | CR seed §6 Assumptions #1 |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source | Source Finding |
|------------|--------|--------------|
| A closed dossier is never amended to satisfy rules written after its approval. | Business author | CR seed §7 Constraints #1 |
| A non-retroactive correction disturbs no dossier and creates no version. | Business author | CR seed §7 Constraints #2 |
| Naming the dossiers a retroactive change affects is part of that change, not a later discovery. | Business author | CR seed §7 Constraints #3 |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|-----------|--------------|
| An approval is valid under the rules it was given, and states which those were. | CR seed §8 Business Invariants #1 |
| A rule-set version exists only where admissibility could have changed. | CR seed §8 Business Invariants #2 |
| Every correction declares its effectivity. | CR seed §8 Business Invariants #3 |
| A migrated dossier is never presented as an approved one. | CR seed §8 Business Invariants #4 |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|--------|-------|---------|--------------|
| Dossier | Approved | Closed under a rule-set version, and still so. | CR seed §9 Lifecycle States #1 |
| Dossier | Migrated | Amended to satisfy a later rule set; it passes now and was taught to. | CR seed §9 Lifecycle States #2 |
| Dossier | Re-approved | Re-judged whole under a later rule set and re-gated by a person. | CR seed §9 Lifecycle States #3 |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-------|----------------|--------------|--------------|
| A rule-set version was created | A retroactive correction is made | Documents approved before it may no longer pass. | CR seed §10 Business Events #1 |
| A dossier was migrated | A dossier is amended to satisfy a later rule set | Its verdict is no longer the one it was approved with. | CR seed §10 Business Events #2 |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|-----------------|---------------------|--------------|
| A correction's effectivity | The correction | CR seed §11 Authority Boundaries #1 |
| The record of that declaration | The rule set | CR seed §11 Authority Boundaries #2 |
| Whether a migrated dossier is re-approved | A person, at a gate | CR seed §11 Authority Boundaries #3 |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason | Source Finding |
|------|--------|--------------|
| Whether a correction should be retroactive | Some must be. This makes the question askable, not answered. | CR seed §12 Out of Scope #1 |
| Whether old dossiers must be migrated | A judgement per correction. | CR seed §12 Out of Scope #2 |
| Anything about generated artifacts | A separate problem with its own change. | CR seed §12 Out of Scope #3 |
| Whether a design can state an artifact it amends | A separate problem with its own change. | CR seed §12 Out of Scope #4 |
| Rule sets that differ per composition rather than per version | Nothing has needed it. | CR seed §12 Out of Scope #5 |

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
| A correction that declares no effectivity is refused. | CR seed §15 Acceptance Criteria #1 |
| A non-retroactive correction creates no version and names no dossier. | CR seed §15 Acceptance Criteria #2 |
| A retroactive correction creates a version and names every dossier it affects. | CR seed §15 Acceptance Criteria #3 |
| An approval states the rule-set version it was given under. | CR seed §15 Acceptance Criteria #4 |
| A migrated dossier is distinguishable from one approved under the rules it satisfies. | CR seed §15 Acceptance Criteria #5 |
| A verdict states which rule-set version it was rendered against. | CR seed §15 Acceptance Criteria #6 |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|-----------------|---------------|-----------------------|--------------|
| Rule-set version | Its own name | They name the same state of the rule set. | CR seed §16 Identity and Sameness #1 |
| Approval | The dossier and the version it was given under | They are the same closure of the same dossier. | CR seed §16 Identity and Sameness #2 |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|--------|------------|----------|--------------|---------|--------------|
| Dossier | Approved | Migrated | Being amended to satisfy a later rule set. | NONE. A migration is not an approval and triggers no gate. | CR seed §17 Lifecycle Transitions #1 |
| Dossier | Migrated | Re-approved | A person re-judging it whole and re-closing the gate. | NONE. | CR seed §17 Lifecycle Transitions #2 |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|-----------|--------------|-----------------|--------------|
| Making a correction | It declares no effectivity | A correction that cannot say whom it affects leaves every prior approval in doubt. | CR seed §18 Operation Refusals #1 |
| Creating a rule-set version | The correction is non-retroactive | A version that cannot invalidate anything makes the version meaningless as a signal. | CR seed §18 Operation Refusals #2 |
| Presenting a migrated dossier as approved | Always | It passes now and was taught to; the two are different claims. | CR seed §18 Operation Refusals #3 |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|-----------------|-------------|-------|--------------|
| Whether any particular correction is retroactive | Each correction | It is made. | CR seed §19 Authority Deferrals #1 |
| Rule sets differing per composition | A later change | Something needs it. | CR seed §19 Authority Deferrals #2 |

