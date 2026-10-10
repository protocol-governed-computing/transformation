# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** binding_literals
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Design subdomain judges each document of the transformation lifecycle against the rule set its
phase declares. A document is admissible when it satisfies every rule its phase declares. The
Design Intent phase holds every statement of where a step's input comes from to a form the runtime
resolves. The subdomain governs what a document must say at each phase, and the verdict it receives.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| design | MODIFY | The Design Intent phase judges where each input's value comes from. Two of its rules disagree about what a literal is, and it has no way to say that a generator determines a value. This corrects both. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Binding | A design's statement of where a step's input comes from. |
| Reference | A binding to a value the runtime offers: the starting intent, the contract's own inputs, or an earlier step's result. |
| Literal | A binding to a value the design fixes. |
| Generator | What produces an artifact in place of construction writing it. |
| Generated value | An input whose value the generator of the artifact that holds it determines. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A literal has one meaning across every rule that judges a binding, so a quoted value is a literal wherever it appears. |
| A design can say that an input's value is determined by the generator of the artifact that holds it, and only where the design names that generator. |
| Every binding that is admissible today stays admissible, with the same meaning. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A value comes from the starting intent, from the contract's own inputs or from an earlier step, or it is a literal the design fixes. | HIGH |
| An operation name such as si.artifact.list is a literal, and so is a dotted identity such as a schema's identity. | HIGH |
| A design names the generator of an artifact it does not write, and construction invokes the generator instead of writing the artifact. | HIGH |
| Bound to an invented literal, a generated value passes and says something false. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Two rules of the Design Intent phase judge the same binding: one asks whether it is a reference the runtime offers, the other whether it is written in a form the runtime resolves. | It is where the disagreement lives. | Identify the rules that judge a binding, and what each asks. |
| Written plain, a dotted literal is refused as a reference to a source the runtime does not offer. | It is half of the disagreement. | Confirm how a plain dotted value is judged. |
| Written in quotes, a dotted literal is accepted as a literal by one rule and refused by the other, which admits a literal only as a single word or an inline list or mapping. | It is the other half. | Confirm how a quoted dotted value is judged by each rule. |
| No spelling of a dotted literal satisfies both rules. | It is the defect. | Establish whether any spelling is admitted by both. |
| Every contract that observes the composition binds a dotted literal, so no design can redeclare one. | It is what the defect blocks. | Identify the contracts that bind a dotted literal today. |
| A phase workflow hands its judging contract the rule set the generator seals into it. | It is the generated value that has no statement. | Confirm how a phase workflow's rule set reaches its contract. |
| A generated value left unbound is refused as missing, and bound to a description is refused as malformed. | It shows the design has no way to state it. | Confirm how each is judged. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No admissible design becomes inadmissible. This correction only admits statements that were refused. It is not retroactive. | Business author |
| Saying a value is generated is admissible only for an artifact the design lists as generated. | Business author |
| The rule-effectivity change is parked at its governance intent and resumes against the composition this change produces. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A literal has one meaning across every rule that judges a binding. |
| A generator determines only what the design says it does. |
| No admissible design becomes inadmissible. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Binding | Admissible | Every rule that judges it admits it. |
| Binding | Refused | A rule that judges it refuses it, and the finding says why. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A binding was judged | A design intent is checked | Every rule that judges a binding reads a literal the same way. |
| A value was declared generated | A design states that the generator determines an input | It is admitted only where the design names that generator. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| The rules that judge a binding | design |
| A generated value | The generator the design names |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| The rule-effectivity change | It is parked and resumes against the composition this change produces. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| design | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A design can redeclare a contract that observes the composition, with every literal it binds stated. |
| A design can redeclare a workflow whose rule set a generator seals, stating that the generator determines it. |
| A value declared generated for an artifact the design does not list as generated is refused. |
| Every design admissible before this change is admissible after it. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| NONE IDENTIFIED |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Declaring a value generated | The design does not list the artifact that holds it as generated | A generator determines only what the design says it does. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| The rule-effectivity change | Its own dossier | This change is delivered. |
