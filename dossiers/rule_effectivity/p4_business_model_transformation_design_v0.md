# Stage 4 — Business Model: transformation / design
**Stage:** 4 — Business Model
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Author | Drives a change through the phases and writes the documents each requires. | Proposing — never decides admissibility. | S1 business_events #1 |
| Person at the gate | Approves a document under a rule set, and re-confirms it under a later one. | Deciding — the sole authority over an approval and its re-confirmation. | S1 authority_boundaries #1 |
| Phase | Judges a document against the rule set it declares and renders a verdict. | Deciding — the sole arbiter of whether a document is admissible. | S1 authority_boundaries #2 |
| Correction | Changes a rule set and declares whether it applies to documents approved before it. | Declaring — the sole authority over its own effectivity. | S1 authority_boundaries #3 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Phase | One step of the lifecycle, with a rule set of its own. | One declared workflow per phase, owned by this subdomain. Seven phases hold a second version beside the first. | S2 entities #1 |
| Rule set | The rules a phase declares, against which it judges a document. | A copy held inside the phase's workflow, produced from the phase's template and its declaration together. | S2 entities #2 |
| Register | The part of a phase document that states facts the rules judge. | A table inside the document's prose, marked by a comment above it. | S2 entities #3 |
| Prose | The part of a phase document that explains the change to a person. | The rest of the same text. | S2 entities #4 |
| Verdict | The result of judging a document against a rule set. | Returned by the judging, and held by nobody. | S2 entities #5 |
| Finding | One reason a verdict gives for a document being inadmissible. | Part of the verdict. | S2 entities #6 |
| Approval | A person closing a document's gate under a rule set. | A lifecycle state in the document's header. Nothing records the rule set. | S2 entities #7 |
| Rule-set identity | The name of a rule set, which changes only when the rules change. | Nothing holds it. | S2 entities #8 |
| Rule-set version | A rule set created by a change that can alter a prior document's admissibility. | A new version of a phase's workflow. It is created whenever the workflow changes, whether or not a rule did. | S2 entities #9 |
| Effectivity | Whether a correction applies to documents approved before it. | Nothing holds it. | S2 entities #10 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The test documents | They exercise the judging, are in the old form, and are converted once to prove the two forms receive the same verdicts. | S3 dependency_discoveries #6 |
| Dossiers approved under v5 | They stay as published, and v6 does not read them. | S3 dependency_discoveries #12 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A document was judged | A document is checked against a rule set | The verdict names the rule set that rendered it. | S1 business_events #1 |
| A document was approved | A person closes its gate | The approval names the rule set it was given under. | S1 business_events #2 |
| A rule set was superseded | A retroactive correction creates a new rule-set version | The correction names the documents it affects, and their approvals stand unconfirmed. | S1 business_events #3 |
| A document was migrated | A document is amended to satisfy a later rule set | The record distinguishes it from a document authored under that rule set. | S1 business_events #4 |
| An approval was re-confirmed | A person judges a document whole under a later rule set and closes its gate again | The approval now names the later rule set. | S1 business_events #5 |
| A correction declared its effectivity | A correction to a rule set is made | The rule set records whether the correction is retroactive. | S1 business_events #6 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Document | carries | Register | Carrying registers as structured data apart from the prose. | S3 authoring_decisions #1 |
| Rule set | has | Rule-set identity | A rule-set identity that changes only when the rules change. | S3 authoring_decisions #2 |
| Document | names | Rule set | Naming the rule set in a document. | S3 authoring_decisions #3 |
| Verdict | names | Rule set | Naming the rule set in a verdict. | S3 authoring_decisions #4 |
| Approval | names | Rule set | Naming an approval's rule set, and confirming it again. | S3 authoring_decisions #5 |
| Document | records | Migration | Recording that a document was migrated. | S3 authoring_decisions #6 |
| Correction | declares | Effectivity | Declaring a correction's effectivity. | S3 authoring_decisions #7 |
| Test document | proves | Verdict | Proving identical verdicts across the two forms. | S3 authoring_decisions #8 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Carrying registers as structured data apart from the prose | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The reading exists; what it reads changes. |
| A rule-set identity that changes only when the rules change | S3 authoring_decisions #2 | CRITICAL | GAP-2 | What a document, a verdict and an approval name. |
| Naming the rule set in a document | S3 authoring_decisions #3 | CRITICAL | GAP-3 | Possible only once the identity exists. |
| Naming the rule set in a verdict | S3 authoring_decisions #4 | CRITICAL | GAP-4 | The same. |
| Naming an approval's rule set, and confirming it again | S3 authoring_decisions #5 | CRITICAL | GAP-5 | The same. |
| Recording that a document was migrated | S3 authoring_decisions #6 | CRITICAL | GAP-6 | Separates a migrated document from one authored under the later rule set. |
| Declaring a correction's effectivity | S3 authoring_decisions #7 | CRITICAL | GAP-7 | Decides whether a correction supersedes a rule set. |
| Proving identical verdicts across the two forms | S3 authoring_decisions #8 | CRITICAL | GAP-8 | The condition on which the old reading retires. |
| Construction's reading of registers | S3 dependency_discoveries #11 | SATISFIED | | Receives registers from the shared reading and is unchanged here. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| design | design | capability call | GAP | S3 analysis_findings Q4 — naming a rule set anywhere depends on the identity existing first. |
| build | design | data read | SATISFIED | S3 analysis_findings Q3 — construction receives registers from the shared reading and is adjacent. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | A verdict names the rule set that rendered it. | S1 business_invariants #1 | invariant |
| 2 | An approval names the rule set it was given under. | S1 business_invariants #2 | invariant |
| 3 | No document changes verdict because its form changed. | S1 business_invariants #3 | invariant |
| 4 | A rule-set identity changes only when the rules change. | S1 business_invariants #4 | invariant |
| 5 | An approval under a later rule set stays unconfirmed until a person re-confirms it. | S1 business_invariants #5 | invariant |
| 6 | One form of phase document exists at a time. | S1 business_invariants #6 | invariant |
| 7 | No compatibility with v5. Dossiers approved under v5 stay as published, and this change neither converts nor reads them. | S1 constraints #1 | governance rule |
| 8 | The old reading retires once this change shows that the old and new forms receive the same verdicts. | S1 constraints #2 | governance rule |
| 9 | One form for every document that carries registers, from the seed to the mandate. | S1 constraints #3 | governance rule |
| 10 | The business problem statement has no registers and stays prose. | S1 constraints #4 | governance rule |
| 11 | The new form replaces the old form. The two never coexist. | S1 constraints #5 | governance rule |
| 12 | A correction declares its own effectivity, retroactive or not, and the rule set records the declaration as governed history. | S1 known_facts #8 | domain knowledge |
| 13 | Only a change that can alter a prior document's admissibility creates a new rule-set version. | S1 known_facts #7 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Carrying registers as structured data apart from the prose | design | EXTEND |
| GAP-2 | S3 authoring_decisions #2 | A rule-set identity that changes only when the rules change | design | NEW |
| GAP-3 | S3 authoring_decisions #3 | Naming the rule set in a document | design | NEW |
| GAP-4 | S3 authoring_decisions #4 | Naming the rule set in a verdict | design | EXTEND |
| GAP-5 | S3 authoring_decisions #5 | Naming an approval's rule set, and confirming it again | design | NEW |
| GAP-6 | S3 authoring_decisions #6 | Recording that a document was migrated | design | NEW |
| GAP-7 | S3 authoring_decisions #7 | Declaring a correction's effectivity | design | NEW |
| GAP-8 | S3 authoring_decisions #8 | Proving identical verdicts across the two forms | design | NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The change is confined to the reading, the writers of documents and the test documents. The judging receives the same data in either form. | S3 analysis_findings Q2 | Every consumer of a register receives it as data from one reading step. | Rules out changing what any rule judges. A verdict that moves is a regression. |
| 2 | Construction stays adjacent. Values written inside cells keep their text form until the next change. | S3 analysis_findings Q3 | Construction meets this change only through the shared reading. | Rules out giving values inside cells a structure here. |
| 3 | The rule-set identity follows the rules themselves, not the phase's workflow version. | S3 analysis_findings Q4 | A workflow version changes whether or not a rule did. | Rules out naming a workflow version as a document's, a verdict's or an approval's rule set. |
| 4 | A superseded rule set stays available in the composition, so a document is judged under the rule set it names without rebuilding its pinned composition. | S3 analysis_findings Q5 | The composition already keeps superseded workflow versions beside current ones. | Rules out depending on old compositions being reproducible. |
| 5 | Dossiers approved under v5 stay as published and are not re-judged. | S3 analysis_findings Q6 | v6 is not compatible with v5. | Rules out converting or reading any v5 dossier. |
| 6 | A document is judged against both the rules it was authored under and the current rules. | S1 known_facts #3 | The two answer different questions: whether its approval was sound, and whether it would be approved today. | Rules out a verdict that names no rule set. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Carrying registers as structured data apart from the prose | GAP-1 |
| A rule-set identity that changes only when the rules change | GAP-2 |
| Naming the rule set in a document | GAP-3 |
| Naming the rule set in a verdict | GAP-4 |
| Naming an approval's rule set, and confirming it again | GAP-5 |
| Recording that a document was migrated | GAP-6 |
| Declaring a correction's effectivity | GAP-7 |
| Proving identical verdicts across the two forms | GAP-8 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| How a value inside a register is structured | Routing written as text stays text here. Giving such values a structure is the next change. |
| Where the rules are declared, and in what language | That is a later change. |
| Governing and specifying construction on its own | That is a later change. |
| Rule sets that differ per composition rather than per version | Nothing has needed it. |
| Converting or reading dossiers approved under v5 | They stay as published, and v6 does not read them. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
