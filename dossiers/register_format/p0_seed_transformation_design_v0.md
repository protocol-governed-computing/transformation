# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** register_format
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarification its
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
| design | MODIFY | The phases judge documents today, and a document's facts are readable only through the current code. This changes the form a document carries its facts in. |

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
| Old form | Registers written as tables inside the prose. |
| New form | Registers carried as structured data in a block of their own, apart from the prose. |
| Test copy | A copy of a delivered dossier that the construction tests reproduce artifacts from. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Every register is carried as structured data in a block of its own, apart from the prose, as an artifact carries its Machine block. |
| The prose stays prose. |
| Every document gives the same verdict and the same findings in its old form and its new form. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A phase document holds prose for a person and registers for the rules, and needs a place for facts a machine reads exactly, separate from the prose. | HIGH |
| Dossiers approved under v5 remain the published evidence of v5, and v6 does not read them. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| A phase document carries prose and registers in one Markdown text, with each register a table inside the prose. | It is the form this change replaces. | Confirm how a phase document carries its registers today. |
| The rules read each register through conventions that only the code states. | A person cannot reproduce a verdict without the code. | Establish where each reading convention is stated, and whether any is stated outside the code. |
| Fourteen reading conventions and seven formats inside cells exist today. | It sizes what the old form depends on. | Count the reading conventions and the formats inside cells. |
| A column is found by the start of its name, a row reading NONE IDENTIFIED means an empty register, and a dash means a cell says nothing. | These are instances of the conventions only the code states. | Confirm each convention against how a register is read today. |
| Routing is written as text, an outcome and a target joined by an arrow, and the code splits it. | It is an instance of a format inside a cell, which this change leaves as text. | Confirm how a routing value is written and read. |
| The construction tests reproduce artifacts from copies of delivered dossiers. | Those copies must be converted before the old reading retires. | Identify which delivered dossiers the construction tests read, and in which form. |

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
| The delivered dossiers the construction tests reproduce artifacts from are copied and converted as test fixtures before the old reading retires. | Business author |
| One form for every document that carries registers, from the seed to the mandate. | Business author |
| The business problem statement has no registers and stays prose. | Business author |
| The new form replaces the old form. The two never coexist. | Business author |
| What this change replaces is deleted, not stood down. The readers of the old form are removed from the composition with their implementation. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No document changes verdict because its form changed. |
| One form of phase document exists at a time. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Document | Admissible | It satisfies every rule its phase declares. |
| Document | Inadmissible | It does not, and the findings say why. |
| Old reading | In use | It reads documents in the old form. |
| Old reading | Retired | The two forms were shown to receive the same verdicts, and nothing reads the old form. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A document was judged | A document is checked against a rule set | The verdict and its findings are the same in either form. |
| A document was converted | A test document or a test copy is rewritten in the new form | Its verdict and findings are compared with the old form's. |
| The old reading was retired | Every converted document received the same verdict and findings in both forms | One form exists from then on. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| The form of a phase document | design |
| Dossiers approved under v5 | The published v5 record |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| How a value inside a register is structured | Routing written as text stays text here. Giving such values a structure is the next change. |
| Where the rules are declared, and in what language | That is a later change. |
| Which rule set judged a document | A document, a verdict and an approval naming their rule set is a later change, made once the rules are declared outside the code. |
| Governing and specifying construction on its own | That is a later change. |
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
| Every artifact the construction tests reproduce today, they reproduce from the converted test copies. |
| After the change, a document in the old form is not read. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Finding | The rule that raised it, the register and row it concerns, and its detail | All four agree. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Old reading | In use | Retired | Every converted document receiving the same verdict and findings in both forms | Nothing reads the old form from then on. |

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
| Which rule set judged a document | A later change | The rules are declared outside the code. |
| Governing and specifying construction on its own | A later change | That change is made. |
