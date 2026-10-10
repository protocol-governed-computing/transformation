# Stage 3 — Analysis Loop: transformation / design
**Stage:** 3 — Analysis Loop
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot, the declared rule sets and the history, rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The instance is in the history. One commit added a column to the classification register. Another amended three delivered identity dossiers to satisfy it. A third restored them to their approved text and left them inadmissible until a document can name the rule set it was approved under. | Closes the one belief Stage 2 could not confirm. It also shows the change has been awaited. | OBSERVED | HIGH | CLOSED | Transformation commit a018b88 added the column. Business-domain commit c4868f6 amended identity dossiers cr_01 to cr_03, and commit 5aab784 restored them. Three of the five amended dossiers were located. |
| Q2 | Every consumer of a register receives it as data from one reading step. Changing the form changes that reading and the writers of documents, and leaves the judging unchanged. | Confines the change to the reading, the writers and the test documents. It makes identical verdicts across the two forms testable. | OBSERVED | HIGH | CLOSED | The register reading feeds four contracts in force: three that judge and one that constructs. Each receives registers as data. |
| Q3 | Construction meets this change only through the shared reading. It splits values inside cells itself, and those values keep their text form here. | Construction stays adjacent. Its reading of values inside cells changes in the next change, which gives those values a structure. | OBSERVED | HIGH | CLOSED | The constructing contract binds the same register reading the judging binds. |
| Q4 | A phase's workflow version cannot be the rule-set identity. It changes whenever the workflow changes, whether or not a rule did. The identity has to follow the rules themselves. | Decides what a document, a verdict and an approval name. | OBSERVED | HIGH | CLOSED | Seven phases hold a second workflow version. |
| Q5 | The composition keeps superseded workflow versions beside current ones. A rule set that is superseded stays available, so a document naming its rule set can be judged under it without rebuilding its pinned composition. | Lets "judged under the rules it was authored under" work without reproducing old compositions. | OBSERVED | HIGH | CLOSED | The pinned snapshot holds both versions of seven phase workflows. |
| Q6 | The three restored identity dossiers are v5 dossiers. With no compatibility with v5, they stay as published and are not re-judged. | Their wait ends here: they remain the published v5 record. | OBSERVED | HIGH | CLOSED | The business author's constraint against v5 compatibility. |
| Q7 | The history records three delivered dossiers amended by hand to satisfy the added column, not five. The instance stands; its count is three. | Corrects the count the seed carried. The case for the change is unchanged. | OBSERVED | HIGH | CLOSED | Commit c4868f6 amended three identity dossiers; no other commit amends a delivered dossier for that column. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| A phase document carries prose and registers in one Markdown text, with each register a table inside the prose. | S2 belief_verification #1 | CONFIRMED | Re-read: each register is a table opened under a marker comment in the document's text. |
| The rules read each register through conventions that only the code states. | S2 belief_verification #2 | CONFIRMED | Re-searched the pinned snapshot: no artifact states a reading convention. |
| Fourteen reading conventions and seven formats inside cells exist today. | S2 belief_verification #3 | CONFIRMED | Re-counted from the reading and judging code. |
| A column is found by the start of its name, a row reading NONE IDENTIFIED means an empty register, and a dash means a cell says nothing. | S2 belief_verification #4 | CONFIRMED | Re-read each convention where the reading applies it. |
| Routing is written as text, an outcome and a target joined by an arrow, and the code splits it. | S2 belief_verification #5 | CONFIRMED | Re-read: both the judging and the construction split routing values themselves. |
| A verdict names no rule set. | S2 belief_verification #6 | CONFIRMED | Re-read the verdict the judging returns: verdict, findings and the number of rules evaluated. |
| An approval is silently reopened when the rules move, and nobody is told. | S2 belief_verification #7 | CONFIRMED | Re-read the header fields; none records a rule set, and nothing reports a change of rules. |
| A document amended to satisfy a later rule reads exactly like one written under that rule from the start. | S2 belief_verification #8 | CONFIRMED | The amended identity dossiers carried no mark of their amendment until they were restored. |
| Every rule written later applies to every document ever written, the next time anyone looks. | S2 belief_verification #9 | CONFIRMED | Confirmed in practice: no pin names the working composition, so documents meet today's rules. |
| 32 of 273 delivered documents fail rules that were added after their approval. | S2 belief_verification #10 | CONFIRMED | Re-measured against the rules in force and the working composition. |
| One added column once made every dossier inadmissible, and five delivered dossiers were amended by hand to pass again. | S2 belief_verification #11 | OVERTURNED | The history shows three, not five: commit a018b88 added the column; commit c4868f6 amended three delivered identity dossiers; commit 5aab784 restored them. Resolved by finding Q7. |
| The old form leaves a document no exact place to name its rule set. | S2 belief_verification #12 | CONFIRMED | Re-read the header and the registers; neither has a place for it. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The reading of a document's registers | capability | EXTEND | It reads the old form only. It must read the new form instead. |
| The reading of a phase's prior documents | capability | EXTEND | The same. |
| The judging of a document against declared rules | capability | EXTEND | Its verdict names no rule set. |
| The phase templates | template | EXTEND | They lay out registers as tables inside prose. |
| The projection that writes a change request from its seed | capability | EXTEND | It writes registers as tables. |
| The test documents that exercise the judging | test documents | EXTEND | They are in the old form and must be converted once. |
| A rule-set identity that changes only when the rules change | concept | AUTHOR_NEW | Nothing holds one today. |
| A record that a document was migrated | concept | AUTHOR_NEW | Nothing records it today. |
| An approval's rule set and its confirmation | concept | AUTHOR_NEW | Nothing records either today. |
| A correction's declared effectivity | concept | AUTHOR_NEW | Nothing records it today. |
| Construction's reading of registers | capability | EXISTING | It receives registers from the shared reading and is unchanged here. |
| Dossiers approved under v5 | dossier | EXISTING | They stay as published, and v6 does not read them. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::CT_PURE_PARSE_REGISTERS_V0 | Reads the new form instead of the old. | 4 | Bound by three judging contracts and one constructing contract in force. |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | Reads prior documents in the new form. | 3 | Bound by the three judging contracts in force. |
| transformation::CT_PURE_EVALUATE_RULES_V0 | Names the rule set in the verdict it returns. | 3 | Bound by the three judging contracts in force. |
| transformation::CC_JUDGE_DOCUMENT_V0 | Carries the rule-set identity into the verdict. | 3 | Bound by the seed, change request and first domain-model workflows. |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | Carries the rule-set identity into the verdict. | 6 | Bound by the six later phase workflows in force. |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | Carries the rule-set identity into the verdict. | 1 | Bound by the analysis-loop workflow in force. |
| The test documents | Every one is converted once, and judged in both forms. A verdict that differs between the forms is a regression. | 0 | They are read by the test harnesses, not by the composition. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Carrying registers as structured data apart from the prose | EXTEND | The reading exists. What it reads changes. Every consumer already receives registers as data. | Keeping tables and stating their conventions was rejected: the business author chose one structured form. Carrying both forms was rejected: the two never coexist. | S2 gaps #1 |
| A rule-set identity that changes only when the rules change | AUTHOR_NEW | A document, a verdict and an approval need something to name. The identity follows the rules themselves. | Naming the phase's workflow version was rejected: it changes for reasons other than the rules. | S2 gaps #6 |
| Naming the rule set in a document | AUTHOR_NEW | A document states the rule set it was authored under, in its structured data. | A field in the old header was rejected: it would be read through the same conventions this change retires. | S2 gaps #2 |
| Naming the rule set in a verdict | EXTEND | The judging already returns a verdict. It gains the identity of the rule set it applied. | Reporting where the rules were read from was rejected: a location on disk is not an identity. | S2 gaps #3 |
| Naming an approval's rule set, and confirming it again | AUTHOR_NEW | An approval names its rule set. Under a later rule set it stays unconfirmed until a person re-confirms it. | Letting an approval lapse when its rules move, or survive unchanged, were both rejected by the business author. | S2 gaps #4 |
| Recording that a document was migrated | AUTHOR_NEW | A document amended to satisfy a later rule set says so, apart from one authored under that set. | Inferring a migration from history was rejected: the record must say it, not a reader of commits. | S2 gaps #5 |
| Declaring a correction's effectivity | AUTHOR_NEW | A correction states whether it is retroactive, and the rule set records it as governed history. | Recording it only in a commit message was rejected: that is the record today, and it was lost. | S2 gaps #7 |
| Proving identical verdicts across the two forms | AUTHOR_NEW | Each test document is converted mechanically and judged in both forms, and the findings are compared. | Comparing verdict counts only was rejected: different findings can produce the same count. | S2 architectural_observations #2 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | The reading, the judging, the templates and the phase rule sets all belong to the subdomain that judges a design. Construction consumes the shared reading and stays adjacent. | S2 architectural_observations #2 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All four critical gaps are resolved: one by extending the reading, three by authoring what does not exist. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the seven questions raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Twelve dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Twelve items re-grounded; eleven CONFIRMED, one OVERTURNED and resolved by Q7. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All seven findings are OBSERVED. The belief Stage 2 left unconfirmed is confirmed from the history. |
