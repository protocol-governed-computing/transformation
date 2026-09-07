# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** rule_expressiveness
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
| design | MODIFY | The phases exist and judge documents today. Three things they rely on cannot be stated in the language their rules are written in, so three classes of defect pass unnoticed. This changes what the rule language can express. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Phase | One step a change passes through, with a rule set of its own and a verdict. |
| Rule | A single thing a phase requires of a document, judged mechanically. |
| Check kind | A way of judging that rules are written in. A rule can only say what some check kind can express. |
| Register | A table in a document, carrying rows of one sort. |
| Classification | What kind of change a change request is — new, extension, modification, retirement. |
| Subdomain | The part of a system a change is a change to. |
| Span | The set of subdomains one change touches. |
| Disposition | What a change does about something it depends on. |
| Purpose | The statement of what a subdomain governs and why it exists. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A change request states which subdomains it touches and what kind of change each receives. |
| Every subdomain a change touches has its purpose stated and its owner declared. |
| A dependency can be recorded as existing and altered by this change. |
| A rule can constrain how many rows a register has. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| One change may touch more than one subdomain. | HIGH |
| A change request may carry more than one classification. | HIGH |
| The subdomain a classification applies to is stated on the classification itself, not declared separately. | HIGH |
| The span of a change is derived from what its classifications say, never declared a second time. | HIGH |
| Every subdomain a change touches has its purpose stated and its owner declared. | HIGH |
| A dependency that exists and is altered is a way of disposing of a dependency, not a new register. | HIGH |
| The ability to constrain a register's row count is what is missing; where to apply it is judged per register. | HIGH |
| This change applies a row-count constraint to no register. | HIGH |
| Each of the three is a correction, not a new requirement — the lifecycle already relies on all three. | HIGH |
| A rule can only be written if some way of judging can express it. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The phases judge documents against rule sets they declare, and those rule sets are governed artifacts rather than code. | Determines whether this change is authored or written. | Confirm the rule sets are declared artifacts of this subdomain. |
| A change request states a kind of change and not the subdomain it applies to. | The first of the three gaps. | Confirm what the classification register carries today. |
| A dependency may be disposed of as existing, reused, authored new, or still under investigation, and in no other way. | The second gap. | Confirm the set of dispositions the register admits. |
| No way of judging can constrain how many rows a register has. | The third gap. | Confirm that none of the declared ways of judging counts rows. |
| A subdomain touched by a change can pass every phase without its purpose being stated or its owner declared. | This is the defect the first gap causes, and the reason it matters. | Establish whether any rule requires either for a subdomain a change touches. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| The three gaps are independent and may be corrected in one change. | Each is a separate thing the language cannot say; none depends on another. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No existing verdict may change except where one of the three gaps caused it. A document admissible today for good reasons stays admissible. | Business author |
| Applying a row-count constraint to any register is a separate judgement and none is made here. | Business author |
| Only the phases that judge a design are touched. The construction half is not. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A rule can only be written if some way of judging can express it. |
| Every subdomain a change touches has its purpose stated and its owner declared. |
| The span of a change is derived from what its classifications say, and stated nowhere else. |
| A phase judges documents only against rules it declares. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Document | Admissible | It says what its phase requires. |
| Document | Inadmissible | It does not, and the findings say where. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A document was judged | A document is checked against a phase's rule set | The verdict and its findings are what the lifecycle produces. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| The rule set a phase declares | design |
| The ways of judging that rules are written in | design |
| What any particular change should do | The change itself, never this subdomain |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Changes that span two domains rather than two subdomains | Nothing has needed it; a span that has never occurred cannot be specified honestly. |
| Applying a row-count constraint to any register | Each is its own judgement about what that register means. |
| The construction half of the lifecycle | Only the phases that judge a design are touched. |
| Whether one change may touch several subdomains | It already may. This makes it stateable, not permissible. |

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
| A change request that touches two subdomains states both, and states what kind of change each receives. |
| A change that touches a subdomain without stating its purpose is refused, and the finding names the subdomain. |
| A change that touches a subdomain without declaring its owner is refused, and the finding names the subdomain. |
| A dependency that exists and is altered by the change can be recorded as such, and is distinguishable from one merely reused. |
| A rule can be written that constrains how many rows a register has, and it refuses a register carrying more. |
| Every document admissible before this change, for reasons other than the three gaps, is admissible after it. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Phase | Its own name | They are the same phase of the same lifecycle. |
| Rule | The phase that declares it, together with what it requires | They are declared by the same phase and require the same thing. |
| Check kind | Its own name | They are the same way of judging. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Document | Inadmissible | Admissible | Every rule its phase declares being satisfied. | None. A verdict is a verdict; nothing follows from it automatically. |
| Document | Admissible | Inadmissible | A phase's rule set gaining a rule the document does not satisfy. | None. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Judging a change request | A classification names no subdomain | A kind of change with no subject cannot be checked against anything. |
| Judging a statement of intent | A subdomain the change touches has no purpose stated | A subdomain changed without a statement of what it governs is changed blindly. |
| Judging a statement of placement | A subdomain the change touches has no owner declared | An unowned subdomain is answerable to nobody. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Changes spanning two domains | A later change | A change that genuinely spans two domains exists. |
| Row-count constraints on particular registers | A later change | Each register's own meaning is judged. |
