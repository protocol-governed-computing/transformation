# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** register_format
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
| design | MODIFY | The phases judge documents today, and a document's facts are readable only through the current code. This changes the form a document carries its facts in. | CR seed §1 CR Type #1 |

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
| Old form | Registers written as tables inside the prose. | CR seed §2 Business Vocabulary #7 |
| New form | Registers carried as structured data in a block of their own, apart from the prose. | CR seed §2 Business Vocabulary #8 |
| Test copy | A copy of a delivered dossier that the construction tests reproduce artifacts from. | CR seed §2 Business Vocabulary #9 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Every register is carried as structured data in a block of its own, apart from the prose, as an artifact carries its Machine block. | CR seed §3 Requested Outcomes #1 |
| The prose stays prose. | CR seed §3 Requested Outcomes #2 |
| Every document gives the same verdict and the same findings in its old form and its new form. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A phase document holds prose for a person and registers for the rules, and needs a place for facts a machine reads exactly, separate from the prose. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Dossiers approved under v5 remain the published evidence of v5, and v6 does not read them. | HIGH | CR seed §4 Known Facts — Business Truths #2 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| A phase document carries prose and registers in one Markdown text, with each register a table inside the prose. | It is the form this change replaces. | Confirm how a phase document carries its registers today. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The rules read each register through conventions that only the code states. | A person cannot reproduce a verdict without the code. | Establish where each reading convention is stated, and whether any is stated outside the code. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Fourteen reading conventions and seven formats inside cells exist today. | It sizes what the old form depends on. | Count the reading conventions and the formats inside cells. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| A column is found by the start of its name, a row reading NONE IDENTIFIED means an empty register, and a dash means a cell says nothing. | These are instances of the conventions only the code states. | Confirm each convention against how a register is read today. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Routing is written as text, an outcome and a target joined by an arrow, and the code splits it. | It is an instance of a format inside a cell, which this change leaves as text. | Confirm how a routing value is written and read. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| The construction tests reproduce artifacts from copies of delivered dossiers. | Those copies must be converted before the old reading retires. | Identify which delivered dossiers the construction tests read, and in which form. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

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
| The delivered dossiers the construction tests reproduce artifacts from are copied and converted as test fixtures before the old reading retires. | Business author | CR seed §7 Constraints #3 |
| One form for every document that carries registers, from the seed to the mandate. | Business author | CR seed §7 Constraints #4 |
| The business problem statement has no registers and stays prose. | Business author | CR seed §7 Constraints #5 |
| The new form replaces the old form. The two never coexist. | Business author | CR seed §7 Constraints #6 |
| What this change replaces is deleted, not stood down. The readers of the old form are removed from the composition with their implementation. | Business author | CR seed §7 Constraints #7 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No document changes verdict because its form changed. | CR seed §8 Business Invariants #1 |
| One form of phase document exists at a time. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Document | Admissible | It satisfies every rule its phase declares. | CR seed §9 Lifecycle States #1 |
| Document | Inadmissible | It does not, and the findings say why. | CR seed §9 Lifecycle States #2 |
| Old reading | In use | It reads documents in the old form. | CR seed §9 Lifecycle States #3 |
| Old reading | Retired | The two forms were shown to receive the same verdicts, and nothing reads the old form. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A document was judged | A document is checked against a rule set | The verdict and its findings are the same in either form. | CR seed §10 Business Events #1 |
| A document was converted | A test document or a test copy is rewritten in the new form | Its verdict and findings are compared with the old form's. | CR seed §10 Business Events #2 |
| The old reading was retired | Every converted document received the same verdict and findings in both forms | One form exists from then on. | CR seed §10 Business Events #3 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| The form of a phase document | design | CR seed §11 Authority Boundaries #1 |
| Dossiers approved under v5 | The published v5 record | CR seed §11 Authority Boundaries #2 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| How a value inside a register is structured | Routing written as text stays text here. Giving such values a structure is the next change. | CR seed §12 Out of Scope #1 |
| Where the rules are declared, and in what language | That is a later change. | CR seed §12 Out of Scope #2 |
| Which rule set judged a document | A document, a verdict and an approval naming their rule set is a later change, made once the rules are declared outside the code. | CR seed §12 Out of Scope #3 |
| Governing and specifying construction on its own | That is a later change. | CR seed §12 Out of Scope #4 |
| Converting or reading dossiers approved under v5 | They stay as published, and v6 does not read them. | CR seed §12 Out of Scope #5 |

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
| Every artifact the construction tests reproduce today, they reproduce from the converted test copies. | CR seed §15 Acceptance Criteria #2 |
| After the change, a document in the old form is not read. | CR seed §15 Acceptance Criteria #3 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Finding | The rule that raised it, the register and row it concerns, and its detail | All four agree. | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Old reading | In use | Retired | Every converted document receiving the same verdict and findings in both forms | Nothing reads the old form from then on. | CR seed §17 Lifecycle Transitions #1 |

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
| Which rule set judged a document | A later change | The rules are declared outside the code. | CR seed §19 Authority Deferrals #3 |
| Governing and specifying construction on its own | A later change | That change is made. | CR seed §19 Authority Deferrals #4 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
