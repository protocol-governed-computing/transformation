# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** rule_effectivity
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
| design | MODIFY | The phases judge documents today. A document's facts are readable only through the current code, and a document names no rules that judged it. This changes the form a document carries its facts in, and makes documents, verdicts and approvals name their rule set. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Phase | One step of the transformation lifecycle, with a rule set of its own. | CR seed §2 Business Vocabulary #1 |
| Rule set | The rules a phase declares, against which it judges a document. | CR seed §2 Business Vocabulary #2 |
| Register | The part of a phase document that states facts the rules judge. | CR seed §2 Business Vocabulary #3 |
| Prose | The part of a phase document that explains the change to a person. | CR seed §2 Business Vocabulary #4 |
| Verdict | The result of judging a document against a rule set: admissible or inadmissible. | CR seed §2 Business Vocabulary #5 |
| Finding | One reason a verdict gives for a document being inadmissible. | CR seed §2 Business Vocabulary #6 |
| Approval | A person closing a document's gate under a rule set. | CR seed §2 Business Vocabulary #7 |
| Rule-set identity | The name of a rule set, which changes only when the rules change. | CR seed §2 Business Vocabulary #8 |
| Rule-set version | A rule set created by a change that can alter a prior document's admissibility. | CR seed §2 Business Vocabulary #9 |
| Old form | Registers written as tables inside the prose. | CR seed §2 Business Vocabulary #10 |
| New form | Registers carried as structured data in a block of their own, apart from the prose. | CR seed §2 Business Vocabulary #11 |
| Migrated | A document amended to satisfy a later rule set, which nobody has re-confirmed. | CR seed §2 Business Vocabulary #12 |
| Re-confirmed | A document a person judged whole under a later rule set, closing its gate again. | CR seed §2 Business Vocabulary #13 |
| Unconfirmed | The standing of an approval under a rule set later than the one it was given under. | CR seed §2 Business Vocabulary #14 |
| Effectivity | Whether a correction applies to documents approved before it: retroactive or not. | CR seed §2 Business Vocabulary #15 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Every register is carried as structured data in a block of its own, apart from the prose, as an artifact carries its Machine block. | CR seed §3 Requested Outcomes #1 |
| The prose stays prose. | CR seed §3 Requested Outcomes #2 |
| A document names the rule set it was authored under, by an identity that changes only when the rules change. | CR seed §3 Requested Outcomes #3 |
| A verdict names the rule set it was rendered against, by the same identity. | CR seed §3 Requested Outcomes #4 |
| A document amended to satisfy a later rule set is recorded as migrated, apart from one authored under that rule set. | CR seed §3 Requested Outcomes #5 |
| An approval names its rule set, and stays unconfirmed under a later rule set until a person re-confirms it. | CR seed §3 Requested Outcomes #6 |
| Every document gives the same verdict and the same findings in its old form and its new form. | CR seed §3 Requested Outcomes #7 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| An approval is a fact about the rule set it was given under, and it stays that fact. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Under a later rule set, an approval stands unconfirmed until a person re-confirms it against that set. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A document is judged against both the rules it was authored under and the current rules, because they answer different questions. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The rules a document was authored under answer whether its approval was sound. The current rules answer whether it would be approved today. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A document stands in one of three states: approved, migrated or re-confirmed. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A completed change need not answer rules written after it closed. A document left behind stays approved under its own rule set and stands unconfirmed under the later one. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Only a change that can alter a prior document's admissibility creates a new rule-set version. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A correction declares its own effectivity, retroactive or not, and the rule set records the declaration as governed history. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A retroactive correction creates a new rule-set version and names the documents it affects. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A non-retroactive correction creates no rule-set version and disturbs no document. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| A phase document holds prose for a person and registers for the rules, and needs a place for facts a machine reads exactly, separate from the prose. | HIGH | CR seed §4 Known Facts — Business Truths #11 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| A phase document carries prose and registers in one Markdown text, with each register a table inside the prose. | It is the form this change replaces. | Confirm how a phase document carries its registers today. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The rules read each register through conventions that only the code states. | A person cannot reproduce a verdict without the code. | Establish where each reading convention is stated, and whether any is stated outside the code. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Fourteen reading conventions and seven formats inside cells exist today. | It sizes what the old form depends on. | Count the reading conventions and the formats inside cells. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| A column is found by the start of its name, a row reading NONE IDENTIFIED means an empty register, and a dash means a cell says nothing. | These are instances of the conventions only the code states. | Confirm each convention against how a register is read today. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Routing is written as text, an outcome and a target joined by an arrow, and the code splits it. | It is an instance of a format inside a cell. | Confirm how a routing value is written and read. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| A verdict names no rule set. | The first of the problems with unrecorded rules. | Establish what a verdict states about the rules that rendered it. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |
| An approval is silently reopened when the rules move, and nobody is told. | The second of the problems with unrecorded rules. | Establish whether anything records an approval's rule set or tells anyone when it changes. | CR seed §5 Existing-System Beliefs — Requiring Verification #7 |
| A document amended to satisfy a later rule reads exactly like one written under that rule from the start. | The third of the problems with unrecorded rules. | Establish whether anything records that a document was amended to satisfy a later rule. | CR seed §5 Existing-System Beliefs — Requiring Verification #8 |
| Every rule written later applies to every document ever written, the next time anyone looks. | It is why a correction can invalidate approved work. | Confirm which rules judge a document that predates them. | CR seed §5 Existing-System Beliefs — Requiring Verification #9 |
| 32 of 273 delivered documents fail rules that were added after their approval. | It measures the problem. | Re-measure delivered documents against the rules in force today. | CR seed §5 Existing-System Beliefs — Requiring Verification #10 |
| One added column once made every dossier inadmissible, and five delivered dossiers were amended by hand to pass again. | It is the instance that shows the problem occurred. | Confirm the instance from the record. | CR seed §5 Existing-System Beliefs — Requiring Verification #11 |
| The old form leaves a document no exact place to name its rule set. | It joins the two problems into one remedy. | Establish where a document could state its rule set today. | CR seed §5 Existing-System Beliefs — Requiring Verification #12 |

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
| No compatibility with v5. Dossiers approved under v5 stay as published, and this change neither converts nor reads them. | Business author | CR seed §7 Constraints #1 |
| The old reading retires once this change shows that the old and new forms receive the same verdicts. | Business author | CR seed §7 Constraints #2 |
| One form for every document that carries registers, from the seed to the mandate. | Business author | CR seed §7 Constraints #3 |
| The business problem statement has no registers and stays prose. | Business author | CR seed §7 Constraints #4 |
| The new form replaces the old form. The two never coexist. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A verdict names the rule set that rendered it. | CR seed §8 Business Invariants #1 |
| An approval names the rule set it was given under. | CR seed §8 Business Invariants #2 |
| No document changes verdict because its form changed. | CR seed §8 Business Invariants #3 |
| A rule-set identity changes only when the rules change. | CR seed §8 Business Invariants #4 |
| An approval under a later rule set stays unconfirmed until a person re-confirms it. | CR seed §8 Business Invariants #5 |
| One form of phase document exists at a time. | CR seed §8 Business Invariants #6 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Document | Admissible | It satisfies every rule its phase declares. | CR seed §9 Lifecycle States #1 |
| Document | Inadmissible | It does not, and the findings say why. | CR seed §9 Lifecycle States #2 |
| Document | Approved | A person closed its gate under a rule set. | CR seed §9 Lifecycle States #3 |
| Document | Migrated | It was amended to satisfy a later rule set, and nobody has re-confirmed it. | CR seed §9 Lifecycle States #4 |
| Document | Re-confirmed | A person judged it whole under a later rule set and closed its gate again. | CR seed §9 Lifecycle States #5 |
| Approval | Confirmed | It was given under the rule set the document is judged against. | CR seed §9 Lifecycle States #6 |
| Approval | Unconfirmed | A later rule set exists, and no person has re-confirmed the approval against it. | CR seed §9 Lifecycle States #7 |
| Rule set | Current | It is the rule set a phase judges documents against today. | CR seed §9 Lifecycle States #8 |
| Rule set | Superseded | A later rule-set version replaced it. | CR seed §9 Lifecycle States #9 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A document was judged | A document is checked against a rule set | The verdict names the rule set that rendered it. | CR seed §10 Business Events #1 |
| A document was approved | A person closes its gate | The approval names the rule set it was given under. | CR seed §10 Business Events #2 |
| A rule set was superseded | A retroactive correction creates a new rule-set version | The correction names the documents it affects, and their approvals stand unconfirmed. | CR seed §10 Business Events #3 |
| A document was migrated | A document is amended to satisfy a later rule set | The record distinguishes it from a document authored under that rule set. | CR seed §10 Business Events #4 |
| An approval was re-confirmed | A person judges a document whole under a later rule set and closes its gate again | The approval now names the later rule set. | CR seed §10 Business Events #5 |
| A correction declared its effectivity | A correction to a rule set is made | The rule set records whether the correction is retroactive. | CR seed §10 Business Events #6 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| An approval, and its re-confirmation | A person at the gate | CR seed §11 Authority Boundaries #1 |
| The rule set a phase declares | design | CR seed §11 Authority Boundaries #2 |
| Whether a correction is retroactive | The correction itself | CR seed §11 Authority Boundaries #3 |
| Dossiers approved under v5 | The published v5 record | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| How a value inside a register is structured | Routing written as text stays text here. Giving such values a structure is the next change. | CR seed §12 Out of Scope #1 |
| Where the rules are declared, and in what language | That is a later change. | CR seed §12 Out of Scope #2 |
| Whether a given correction is retroactive | The correction declares that itself. | CR seed §12 Out of Scope #3 |
| Governing and specifying construction on its own | That is a later change. | CR seed §12 Out of Scope #4 |
| Rule sets that differ per composition rather than per version | Nothing has needed it. | CR seed §12 Out of Scope #5 |
| Converting or reading dossiers approved under v5 | They stay as published, and v6 does not read them. | CR seed §12 Out of Scope #6 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| design | MODIFIED | CR seed §13 Governance Scope #1 |
| build | ADJACENT | CR seed §13 Governance Scope #2 |

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
| Every document gives the same verdict and the same findings in its old form and its new form. | CR seed §15 Acceptance Criteria #1 |
| Every verdict names the rule set that rendered it. | CR seed §15 Acceptance Criteria #2 |
| A document names the rule set it was authored under. | CR seed §15 Acceptance Criteria #3 |
| A document amended to satisfy a later rule set reads as migrated, and is distinguishable from one authored under that rule set. | CR seed §15 Acceptance Criteria #4 |
| An approval given under a superseded rule set reads as unconfirmed until a person re-confirms it. | CR seed §15 Acceptance Criteria #5 |
| A rule-set identity stays the same across every change that leaves the rules unchanged. | CR seed §15 Acceptance Criteria #6 |
| After the change, a document in the old form is not read. | CR seed §15 Acceptance Criteria #7 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Rule set | Its rule-set identity | Their rules are the same. | CR seed §16 Identity and Sameness #1 |
| Approval | The document it closes, together with the rule set it was given under | They close the same document under the same rule set. | CR seed §16 Identity and Sameness #2 |
| Document | The change it belongs to, together with its phase | They belong to the same change and the same phase. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Rule set | Current | Superseded | A retroactive correction creating a new rule-set version | The correction names the documents it affects. Their approvals stand unconfirmed. Nothing else follows. | CR seed §17 Lifecycle Transitions #1 |
| Approval | Confirmed | Unconfirmed | The rule set it was given under being superseded | None. The approval stays a fact about its own rule set. | CR seed §17 Lifecycle Transitions #2 |
| Approval | Unconfirmed | Confirmed | A person re-confirming it against the later rule set | The document becomes re-confirmed. | CR seed §17 Lifecycle Transitions #3 |
| Document | Approved | Migrated | An amendment made to satisfy a later rule set | None. The approval is not carried over. | CR seed §17 Lifecycle Transitions #4 |
| Document | Migrated | Re-confirmed | A person judging it whole under the later rule set and closing its gate again | None. | CR seed §17 Lifecycle Transitions #5 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Judging a document | The document is in the old form, after this change | One form exists after this change, and the old reading retires. | CR seed §18 Operation Refusals #1 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| The structure of values inside registers | The next change | This change is delivered. | CR seed §19 Authority Deferrals #1 |
| Where the rules are declared, and in what language | A later change | That change is made. | CR seed §19 Authority Deferrals #2 |
| Governing and specifying construction on its own | A later change | That change is made. | CR seed §19 Authority Deferrals #3 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
