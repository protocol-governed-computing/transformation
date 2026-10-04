# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** rule_effectivity
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
| design | MODIFY | Every rule applies to every document that has ever existed, and nothing records which rules a document was approved under. An approval cannot be told from a migration, and a correction cannot say whom it affects. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Rule set | What a phase judges a document against, at a moment in time. |
| Rule-set version | A named state of the rule set. A new one exists only when a change can alter a prior dossier's admissibility. |
| Effectivity | A correction's own declaration of whether it is retroactive or not. |
| Retroactive | A correction that can alter a prior dossier's admissibility. |
| Non-retroactive | One that cannot. |
| Approved | Closed under a rule-set version, and still so. |
| Migrated | Amended to satisfy a later rule set. It passes now and was taught to. |
| Re-approved | Re-judged whole under a later rule set and re-gated by a person. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A correction declares whether it is retroactive, and the rule set records the declaration. |
| A rule-set version exists only where a change can alter a prior dossier's admissibility. |
| Every approval pins the rule-set version it was given under. |
| A retroactive change names the dossiers it affects, each to be migrated or re-approved. |
| A migrated dossier is distinguishable from one approved under the rules it satisfies. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| An approval remains valid under the rules it was given. | HIGH |
| Re-evaluation under later rules is a separate act, and is recorded. | HIGH |
| A new rule-set version exists only when a change can alter a prior dossier's admissibility. | HIGH |
| A correction declares its own effectivity: retroactive or non-retroactive. | HIGH |
| The rule set records that declaration as governed history. | HIGH |
| Each approval pins the rule-set version it was given under. | HIGH |
| A retroactive change creates a version and names the dossiers it affects. | HIGH |
| A non-retroactive correction creates no version, names no dossier, and disturbs none. | HIGH |
| There are three states, not two: approved, migrated, re-approved. | HIGH |
| A document is judged under the rules it was authored under and under current rules, and the two answer different questions. | HIGH |
| A completed change may be left at the version it was approved under. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| A document is judged only against the rules in force when it is judged. | The whole of this change. | Confirm what a verdict is rendered against, and whether it states which rules it used. |
| Nothing records which rules a document was approved under. | Without it no distinction between approved and migrated is recordable. | Establish whether any document carries a rule-set version. |
| A correction cannot say whether it is retroactive. | Determines whether this adds a declaration or changes a rule. | Establish what a change can state today about its own effect on prior documents. |
| Dossiers have already been amended to satisfy rules written after their approval, and nothing in them says so. | Establishes the defect occurred rather than being foreseen. | Confirm which dossiers were amended and what records it. |
| A rule set has no version at all. | Says how much of this is new rather than corrected. | Establish whether the rule set is versioned in any form. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| Whether a change can alter a prior dossier's admissibility is knowable by whoever makes the change. | A change knows what it added and why. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| A closed dossier is never amended to satisfy rules written after its approval. | Business author |
| A non-retroactive correction disturbs no dossier and creates no version. | Business author |
| Naming the dossiers a retroactive change affects is part of that change, not a later discovery. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| An approval is valid under the rules it was given, and states which those were. |
| A rule-set version exists only where admissibility could have changed. |
| Every correction declares its effectivity. |
| A migrated dossier is never presented as an approved one. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Dossier | Approved | Closed under a rule-set version, and still so. |
| Dossier | Migrated | Amended to satisfy a later rule set; it passes now and was taught to. |
| Dossier | Re-approved | Re-judged whole under a later rule set and re-gated by a person. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A rule-set version was created | A retroactive correction is made | Documents approved before it may no longer pass. |
| A dossier was migrated | A dossier is amended to satisfy a later rule set | Its verdict is no longer the one it was approved with. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| A correction's effectivity | The correction |
| The record of that declaration | The rule set |
| Whether a migrated dossier is re-approved | A person, at a gate |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Whether a correction should be retroactive | Some must be. This makes the question askable, not answered. |
| Whether old dossiers must be migrated | A judgement per correction. |
| Anything about generated artifacts | A separate problem with its own change. |
| Whether a design can state an artifact it amends | A separate problem with its own change. |
| Rule sets that differ per composition rather than per version | Nothing has needed it. |

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
| A correction that declares no effectivity is refused. |
| A non-retroactive correction creates no version and names no dossier. |
| A retroactive correction creates a version and names every dossier it affects. |
| An approval states the rule-set version it was given under. |
| A migrated dossier is distinguishable from one approved under the rules it satisfies. |
| A verdict states which rule-set version it was rendered against. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Rule-set version | Its own name | They name the same state of the rule set. |
| Approval | The dossier and the version it was given under | They are the same closure of the same dossier. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Dossier | Approved | Migrated | Being amended to satisfy a later rule set. | NONE. A migration is not an approval and triggers no gate. |
| Dossier | Migrated | Re-approved | A person re-judging it whole and re-closing the gate. | NONE. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Making a correction | It declares no effectivity | A correction that cannot say whom it affects leaves every prior approval in doubt. |
| Creating a rule-set version | The correction is non-retroactive | A version that cannot invalidate anything makes the version meaningless as a signal. |
| Presenting a migrated dossier as approved | Always | It passes now and was taught to; the two are different claims. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Whether any particular correction is retroactive | Each correction | It is made. |
| Rule sets differing per composition | A later change | Something needs it. |
