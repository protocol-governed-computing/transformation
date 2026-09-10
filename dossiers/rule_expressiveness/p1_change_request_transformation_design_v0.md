# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** rule_expressiveness
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was said in.
S1 interrogates and does not author.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|-----------|----------------|-----------|--------------|
| design | MODIFY | The phases exist and judge documents today. Three things they rely on cannot be stated in the language their rules are written in, so three classes of defect pass unnoticed. This changes what the rule language can express. | CR seed §1 CR Type #1 |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|------|------------|--------------|
| Phase | One step a change passes through, with a rule set of its own and a verdict. | CR seed §2 Business Vocabulary #1 |
| Rule | A single thing a phase requires of a document, judged mechanically. | CR seed §2 Business Vocabulary #2 |
| Check kind | A way of judging that rules are written in. A rule can only say what some check kind can express. | CR seed §2 Business Vocabulary #3 |
| Register | A table in a document, carrying rows of one sort. | CR seed §2 Business Vocabulary #4 |
| Classification | What kind of change a change request is — new, extension, modification, retirement. | CR seed §2 Business Vocabulary #5 |
| Subdomain | The part of a system a change is a change to. | CR seed §2 Business Vocabulary #6 |
| Span | The set of subdomains one change touches. | CR seed §2 Business Vocabulary #7 |
| Disposition | What a change does about something it depends on. | CR seed §2 Business Vocabulary #8 |
| Purpose | The statement of what a subdomain governs and why it exists. | CR seed §2 Business Vocabulary #9 |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|---------|--------------|
| A change request states which subdomains it touches and what kind of change each receives. | CR seed §3 Requested Outcomes #1 |
| Every subdomain a change touches has its purpose stated and its owner declared. | CR seed §3 Requested Outcomes #2 |
| A dependency can be recorded as existing and altered by this change. | CR seed §3 Requested Outcomes #3 |
| A rule can constrain how many rows a register has. | CR seed §3 Requested Outcomes #4 |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|------|-----------|--------------|
| One change may touch more than one subdomain. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A change request may carry more than one classification. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| The subdomain a classification applies to is stated on the classification itself, not declared separately. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The span of a change is derived from what its classifications say, never declared a second time. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Every subdomain a change touches has its purpose stated and its owner declared. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A dependency that exists and is altered is a way of disposing of a dependency, not a new register. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The ability to constrain a register's row count is what is missing; where to apply it is judged per register. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| This change applies a row-count constraint to no register. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| Each of the three is a correction, not a new requirement — the lifecycle already relies on all three. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A rule can only be written if some way of judging can express it. | HIGH | CR seed §4 Known Facts — Business Truths #10 |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|--------|----------------|-------------------|--------------|
| The phases judge documents against rule sets they declare, and those rule sets are governed artifacts rather than code. | Determines whether this change is authored or written. | Confirm the rule sets are declared artifacts of this subdomain. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| A change request states a kind of change and not the subdomain it applies to. | The first of the three gaps. | Confirm what the classification register carries today. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| A dependency may be disposed of as existing, reused, authored new, or still under investigation, and in no other way. | The second gap. | Confirm the set of dispositions the register admits. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| No way of judging can constrain how many rows a register has. | The third gap. | Confirm that none of the declared ways of judging counts rows. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| A subdomain touched by a change can pass every phase without its purpose being stated or its owner declared. | This is the defect the first gap causes, and the reason it matters. | Establish whether any rule requires either for a subdomain a change touches. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|------------|-------|--------------|
| The three gaps are independent and may be corrected in one change. | Each is a separate thing the language cannot say; none depends on another. | CR seed §6 Assumptions #1 |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source | Source Finding |
|------------|--------|--------------|
| No existing verdict may change except where one of the three gaps caused it. A document admissible today for good reasons stays admissible. | Business author | CR seed §7 Constraints #1 |
| Applying a row-count constraint to any register is a separate judgement and none is made here. | Business author | CR seed §7 Constraints #2 |
| Only the phases that judge a design are touched. The construction half is not. | Business author | CR seed §7 Constraints #3 |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|-----------|--------------|
| A rule can only be written if some way of judging can express it. | CR seed §8 Business Invariants #1 |
| Every subdomain a change touches has its purpose stated and its owner declared. | CR seed §8 Business Invariants #2 |
| The span of a change is derived from what its classifications say, and stated nowhere else. | CR seed §8 Business Invariants #3 |
| A phase judges documents only against rules it declares. | CR seed §8 Business Invariants #4 |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|--------|-------|---------|--------------|
| Document | Admissible | It says what its phase requires. | CR seed §9 Lifecycle States #1 |
| Document | Inadmissible | It does not, and the findings say where. | CR seed §9 Lifecycle States #2 |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-------|----------------|--------------|--------------|
| A document was judged | A document is checked against a phase's rule set | The verdict and its findings are what the lifecycle produces. | CR seed §10 Business Events #1 |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|-----------------|---------------------|--------------|
| The rule set a phase declares | design | CR seed §11 Authority Boundaries #1 |
| The ways of judging that rules are written in | design | CR seed §11 Authority Boundaries #2 |
| What any particular change should do | The change itself, never this subdomain | CR seed §11 Authority Boundaries #3 |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason | Source Finding |
|------|--------|--------------|
| Changes that span two domains rather than two subdomains | Nothing has needed it; a span that has never occurred cannot be specified honestly. | CR seed §12 Out of Scope #1 |
| Applying a row-count constraint to any register | Each is its own judgement about what that register means. | CR seed §12 Out of Scope #2 |
| The construction half of the lifecycle | Only the phases that judge a design are touched. | CR seed §12 Out of Scope #3 |
| Whether one change may touch several subdomains | It already may. This makes it stateable, not permissible. | CR seed §12 Out of Scope #4 |

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
| A change request that touches two subdomains states both, and states what kind of change each receives. | CR seed §15 Acceptance Criteria #1 |
| A change that touches a subdomain without stating its purpose is refused, and the finding names the subdomain. | CR seed §15 Acceptance Criteria #2 |
| A change that touches a subdomain without declaring its owner is refused, and the finding names the subdomain. | CR seed §15 Acceptance Criteria #3 |
| A dependency that exists and is altered by the change can be recorded as such, and is distinguishable from one merely reused. | CR seed §15 Acceptance Criteria #4 |
| A rule can be written that constrains how many rows a register has, and it refuses a register carrying more. | CR seed §15 Acceptance Criteria #5 |
| Every document admissible before this change, for reasons other than the three gaps, is admissible after it. | CR seed §15 Acceptance Criteria #6 |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|-----------------|---------------|-----------------------|--------------|
| Phase | Its own name | They are the same phase of the same lifecycle. | CR seed §16 Identity and Sameness #1 |
| Rule | The phase that declares it, together with what it requires | They are declared by the same phase and require the same thing. | CR seed §16 Identity and Sameness #2 |
| Check kind | Its own name | They are the same way of judging. | CR seed §16 Identity and Sameness #3 |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|--------|------------|----------|--------------|---------|--------------|
| Document | Inadmissible | Admissible | Every rule its phase declares being satisfied. | None. A verdict is a verdict; nothing follows from it automatically. | CR seed §17 Lifecycle Transitions #1 |
| Document | Admissible | Inadmissible | A phase's rule set gaining a rule the document does not satisfy. | None. | CR seed §17 Lifecycle Transitions #2 |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|-----------|--------------|-----------------|--------------|
| Judging a change request | A classification names no subdomain | A kind of change with no subject cannot be checked against anything. | CR seed §18 Operation Refusals #1 |
| Judging a statement of intent | A subdomain the change touches has no purpose stated | A subdomain changed without a statement of what it governs is changed blindly. | CR seed §18 Operation Refusals #2 |
| Judging a statement of placement | A subdomain the change touches has no owner declared | An unowned subdomain is answerable to nobody. | CR seed §18 Operation Refusals #3 |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|-----------------|-------------|-------|--------------|
| Changes spanning two domains | A later change | A change that genuinely spans two domains exists. | CR seed §19 Authority Deferrals #1 |
| Row-count constraints on particular registers | A later change | Each register's own meaning is judged. | CR seed §19 Authority Deferrals #2 |

