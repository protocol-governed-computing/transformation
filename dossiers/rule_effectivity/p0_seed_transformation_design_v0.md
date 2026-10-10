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

The Design subdomain judges each document of the transformation lifecycle against the rule set its
phase declares. A document is admissible when it satisfies every rule its phase declares. A phase
document holds two kinds of content: prose that explains the change to a person, and registers
that state the facts the rules judge. The subdomain governs what a document must say at each phase,
and the verdict it receives.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| design | MODIFY | The phases judge documents today. A document's facts are readable only through the current code, and a document names no rules that judged it. This changes the form a document carries its facts in, and makes documents, verdicts and approvals name their rule set. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Phase | One step of the transformation lifecycle, with a rule set of its own. |
| Rule set | The rules a phase declares, against which it judges a document. |
| Register | The part of a phase document that states facts the rules judge. |
| Prose | The part of a phase document that explains the change to a person. |
| Verdict | The result of judging a document against a rule set: admissible or inadmissible. |
| Finding | One reason a verdict gives for a document being inadmissible. |
| Approval | A person closing a document's gate under a rule set. |
| Rule-set identity | The name of a rule set, which changes only when the rules change. |
| Rule-set version | A rule set created by a change that can alter a prior document's admissibility. |
| Old form | Registers written as tables inside the prose. |
| New form | Registers carried as structured data in a block of their own, apart from the prose. |
| Migrated | A document amended to satisfy a later rule set, which nobody has re-confirmed. |
| Re-confirmed | A document a person judged whole under a later rule set, closing its gate again. |
| Unconfirmed | The standing of an approval under a rule set later than the one it was given under. |
| Effectivity | Whether a correction applies to documents approved before it: retroactive or not. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Every register is carried as structured data in a block of its own, apart from the prose, as an artifact carries its Machine block. |
| The prose stays prose. |
| A document names the rule set it was authored under, by an identity that changes only when the rules change. |
| A verdict names the rule set it was rendered against, by the same identity. |
| A document amended to satisfy a later rule set is recorded as migrated, apart from one authored under that rule set. |
| An approval names its rule set, and stays unconfirmed under a later rule set until a person re-confirms it. |
| Every document gives the same verdict and the same findings in its old form and its new form. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| An approval is a fact about the rule set it was given under, and it stays that fact. | HIGH |
| Under a later rule set, an approval stands unconfirmed until a person re-confirms it against that set. | HIGH |
| A document is judged against both the rules it was authored under and the current rules, because they answer different questions. | HIGH |
| The rules a document was authored under answer whether its approval was sound. The current rules answer whether it would be approved today. | HIGH |
| A document stands in one of three states: approved, migrated or re-confirmed. | HIGH |
| A completed change need not answer rules written after it closed. A document left behind stays approved under its own rule set and stands unconfirmed under the later one. | HIGH |
| Only a change that can alter a prior document's admissibility creates a new rule-set version. | HIGH |
| A correction declares its own effectivity, retroactive or not, and the rule set records the declaration as governed history. | HIGH |
| A retroactive correction creates a new rule-set version and names the documents it affects. | HIGH |
| A non-retroactive correction creates no rule-set version and disturbs no document. | HIGH |
| A phase document holds prose for a person and registers for the rules, and needs a place for facts a machine reads exactly, separate from the prose. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| A phase document carries prose and registers in one Markdown text, with each register a table inside the prose. | It is the form this change replaces. | Confirm how a phase document carries its registers today. |
| The rules read each register through conventions that only the code states. | A person cannot reproduce a verdict without the code. | Establish where each reading convention is stated, and whether any is stated outside the code. |
| Fourteen reading conventions and seven formats inside cells exist today. | It sizes what the old form depends on. | Count the reading conventions and the formats inside cells. |
| A column is found by the start of its name, a row reading NONE IDENTIFIED means an empty register, and a dash means a cell says nothing. | These are instances of the conventions only the code states. | Confirm each convention against how a register is read today. |
| Routing is written as text, an outcome and a target joined by an arrow, and the code splits it. | It is an instance of a format inside a cell. | Confirm how a routing value is written and read. |
| A verdict names no rule set. | The first of the problems with unrecorded rules. | Establish what a verdict states about the rules that rendered it. |
| An approval is silently reopened when the rules move, and nobody is told. | The second of the problems with unrecorded rules. | Establish whether anything records an approval's rule set or tells anyone when it changes. |
| A document amended to satisfy a later rule reads exactly like one written under that rule from the start. | The third of the problems with unrecorded rules. | Establish whether anything records that a document was amended to satisfy a later rule. |
| Every rule written later applies to every document ever written, the next time anyone looks. | It is why a correction can invalidate approved work. | Confirm which rules judge a document that predates them. |
| 32 of 273 delivered documents fail rules that were added after their approval. | It measures the problem. | Re-measure delivered documents against the rules in force today. |
| One added column once made every dossier inadmissible, and five delivered dossiers were amended by hand to pass again. | It is the instance that shows the problem occurred. | Confirm the instance from the record. |
| The old form leaves a document no exact place to name its rule set. | It joins the two problems into one remedy. | Establish where a document could state its rule set today. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No compatibility with v5. Dossiers approved under v5 stay as published, and this change neither converts nor reads them. | Business author |
| The old reading retires once this change shows that the old and new forms receive the same verdicts. | Business author |
| One form for every document that carries registers, from the seed to the mandate. | Business author |
| The business problem statement has no registers and stays prose. | Business author |
| The new form replaces the old form. The two never coexist. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A verdict names the rule set that rendered it. |
| An approval names the rule set it was given under. |
| No document changes verdict because its form changed. |
| A rule-set identity changes only when the rules change. |
| An approval under a later rule set stays unconfirmed until a person re-confirms it. |
| One form of phase document exists at a time. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Document | Admissible | It satisfies every rule its phase declares. |
| Document | Inadmissible | It does not, and the findings say why. |
| Document | Approved | A person closed its gate under a rule set. |
| Document | Migrated | It was amended to satisfy a later rule set, and nobody has re-confirmed it. |
| Document | Re-confirmed | A person judged it whole under a later rule set and closed its gate again. |
| Approval | Confirmed | It was given under the rule set the document is judged against. |
| Approval | Unconfirmed | A later rule set exists, and no person has re-confirmed the approval against it. |
| Rule set | Current | It is the rule set a phase judges documents against today. |
| Rule set | Superseded | A later rule-set version replaced it. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A document was judged | A document is checked against a rule set | The verdict names the rule set that rendered it. |
| A document was approved | A person closes its gate | The approval names the rule set it was given under. |
| A rule set was superseded | A retroactive correction creates a new rule-set version | The correction names the documents it affects, and their approvals stand unconfirmed. |
| A document was migrated | A document is amended to satisfy a later rule set | The record distinguishes it from a document authored under that rule set. |
| An approval was re-confirmed | A person judges a document whole under a later rule set and closes its gate again | The approval now names the later rule set. |
| A correction declared its effectivity | A correction to a rule set is made | The rule set records whether the correction is retroactive. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| An approval, and its re-confirmation | A person at the gate |
| The rule set a phase declares | design |
| Whether a correction is retroactive | The correction itself |
| Dossiers approved under v5 | The published v5 record |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| How a value inside a register is structured | Routing written as text stays text here. Giving such values a structure is the next change. |
| Where the rules are declared, and in what language | That is a later change. |
| Whether a given correction is retroactive | The correction declares that itself. |
| Governing and specifying construction on its own | That is a later change. |
| Rule sets that differ per composition rather than per version | Nothing has needed it. |
| Converting or reading dossiers approved under v5 | They stay as published, and v6 does not read them. |

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
| Every document gives the same verdict and the same findings in its old form and its new form. |
| Every verdict names the rule set that rendered it. |
| A document names the rule set it was authored under. |
| A document amended to satisfy a later rule set reads as migrated, and is distinguishable from one authored under that rule set. |
| An approval given under a superseded rule set reads as unconfirmed until a person re-confirms it. |
| A rule-set identity stays the same across every change that leaves the rules unchanged. |
| After the change, a document in the old form is not read. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Rule set | Its rule-set identity | Their rules are the same. |
| Approval | The document it closes, together with the rule set it was given under | They close the same document under the same rule set. |
| Document | The change it belongs to, together with its phase | They belong to the same change and the same phase. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Rule set | Current | Superseded | A retroactive correction creating a new rule-set version | The correction names the documents it affects. Their approvals stand unconfirmed. Nothing else follows. |
| Approval | Confirmed | Unconfirmed | The rule set it was given under being superseded | None. The approval stays a fact about its own rule set. |
| Approval | Unconfirmed | Confirmed | A person re-confirming it against the later rule set | The document becomes re-confirmed. |
| Document | Approved | Migrated | An amendment made to satisfy a later rule set | None. The approval is not carried over. |
| Document | Migrated | Re-confirmed | A person judging it whole under the later rule set and closing its gate again | None. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Judging a document | The document is in the old form, after this change | One form exists after this change, and the old reading retires. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| The structure of values inside registers | The next change | This change is delivered. |
| Where the rules are declared, and in what language | A later change | That change is made. |
| Governing and specifying construction on its own | A later change | That change is made. |
