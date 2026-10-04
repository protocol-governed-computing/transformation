# Stage 3 — Analysis Loop: transformation / design
**Stage:** 3 — Analysis Loop
**CR:** rule_expressiveness
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot and the declared rule sets rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The subdomain a classification applies to belongs on the classification itself. A classification and a separately declared list of subdomains are two statements of one thing and can disagree; one row carrying both cannot. | Decides the shape of the correction, and whether the span can drift from the kinds. | OBSERVED | HIGH | CLOSED | The classification register declares three columns and none names a subdomain. |
| Q2 | The span of a change is whatever its classifications say. Nothing declares it a second time, so nothing can contradict it. | Makes the two new requirements checkable without adding a register anyone must keep in agreement. | OBSERVED | HIGH | CLOSED | Derivation has no second source to drift from. |
| Q3 | Requiring a purpose and an owner for every subdomain a change touches is possible only once the span is stated. Both requirements are consequences of the first correction rather than independent ones. | Orders the corrections: the span first, the two requirements after it. | OBSERVED | HIGH | CLOSED | No rule ties either to a touched subdomain today, because no phase knows the span. |
| Q4 | A dependency that exists and is altered is a fifth way of disposing of a dependency. The register already records dispositions; the vocabulary is short by one. | Confines the correction to a vocabulary, not a register or a phase. | OBSERVED | HIGH | CLOSED | The vocabulary admits four; the decisions register of the same phase records an extension the dependency register cannot express. |
| Q5 | Counting a register's rows is a way of judging, and none of the forty-two counts. Adding it is an addition to how rules may be written, not a rule. | Distinguishes the capability from any use of it, and keeps this change from altering a verdict by accident. | OBSERVED | HIGH | CLOSED | Three of the forty-two concern a register's shape; none counts rows. |
| Q6 | Applying a row count to any register would change a verdict. This change applies none, so the addition alters nothing until a later change chooses to use it. | Keeps the regression surface of this change to the three corrections that were asked for. | OBSERVED | HIGH | CLOSED | No register declares a row count. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| The phases judge documents against rule sets they declare, and those rule sets are governed artifacts rather than code. | S2 belief_verification #1 | CONFIRMED | Re-read from the pinned snapshot: nine phase artifacts, owned by the design subdomain. |
| A change request states a kind of change and not the subdomain it applies to. | S2 belief_verification #2 | CONFIRMED | Re-read: Classification, Rationale, Source Finding. |
| A dependency may be disposed of as existing, reused, authored new, or still under investigation, and in no other way. | S2 belief_verification #3 | CONFIRMED | Re-read: the vocabulary is closed at four. |
| No way of judging can constrain how many rows a register has. | S2 belief_verification #4 | CONFIRMED | Re-counted: forty-two ways of judging, none counting rows. |
| A subdomain touched by a change can pass every phase without its purpose being stated or its owner declared. | S2 belief_verification #5 | CONFIRMED | Re-checked against a real dossier admissible at seven phases with a modified subdomain carrying neither. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The register that carries a change's classifications | register | EXISTING | Declared by the seed phase and the change request phase alike. |
| The register that carries a change's dependencies | register | EXISTING | Declared by this phase. |
| The register that carries a statement of intent's purpose | register | EXISTING | Declared by the intent phase. |
| The register that carries ownership | register | EXISTING | Declared by the placement phase. |
| A way of judging that counts a register's rows | check kind | AUTHOR_NEW | None of the forty-two counts rows. |
| A way of judging that a purpose exists for every subdomain a change touches | check kind | INVESTIGATE | Whether this is a new way of judging or a rule written in one that exists is settled at design. |
| A way of judging that an owner is declared for every subdomain a change touches | check kind | INVESTIGATE | The same question. |
| The dossiers already judged against these phases | dossier | EXISTING | Five exist and must all be re-judged after the correction. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Declares the classification register. Gains a column. | 0 | Nothing in the composition consumes a phase artifact; the phases are read by the tool that judges. |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | Declares the classification register. Gains a column. | 0 | The same. |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0 | Declares the dependency vocabulary. Gains a fifth term. | 0 | The same. |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0 | Gains a requirement over every subdomain the change touches. | 0 | The same. |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0 | Gains a requirement over every subdomain the change touches. | 0 | The same. |
| The five dossiers already authored | Every one is re-judged. A verdict that changes for any reason other than the three corrections is a regression. | 5 | Five dossiers exist against these phases. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Stating which subdomain a classification applies to | EXTEND | The register that carries classifications gains a column naming the subdomain each applies to. The register exists; what it carries is short by one column. | A separate register listing the subdomains touched was rejected: two statements of one thing can disagree, and nothing would reconcile them. A new classification meaning "several subdomains" was rejected: it mixes the kind of a change with its span, so two rows would mean two different sorts of thing. | S2 gaps #1 |
| Deriving the span of a change from its classifications | AUTHOR_NEW | The set of subdomains a change touches is whatever its classifications name. Derived, so there is nothing second to keep in agreement. | Declaring the span separately was rejected for the reason above. | S1 known_facts #4 |
| Requiring a purpose for every subdomain a change touches | AUTHOR_NEW | A subdomain changed with nothing said about what it governs is changed blindly. Possible only once the span is stated. | Requiring it only for the subdomain a document is about was rejected: that is the rule today, and it is what let a modified subdomain through with nothing said about it. | S2 gaps #2 |
| Requiring an owner for every subdomain a change touches | AUTHOR_NEW | An unowned subdomain is answerable to nobody. | Requiring an owner per capability was rejected as insufficient: a subdomain a change touches but names no capability of has no owner at all. | S2 gaps #3 |
| Recording a dependency that exists and is altered | EXTEND | The vocabulary of ways to dispose of a dependency gains a fifth term. The register and the phase are unchanged. | A separate register for altered dependencies was rejected: the phase would then hold two records of one dependency. | S2 gaps #4 |
| Counting a register's rows | AUTHOR_NEW | A new way of judging, so that a rule constraining how many rows a register has can be written at all. | Writing the constraint into each register's own declaration was rejected: a way of judging is what rules are written in, and every register would otherwise need its own bespoke rule. | S2 gaps #5 |
| Applying a row count to any register | REUSE | None is applied. The ability is what was missing; where to use it is judged per register, in a later change. | Applying it to the classification register was rejected: a change may carry more than one classification, so constraining it to one would be wrong. | S1 known_facts #8 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | Everything corrected here belongs to the phases that judge a design, and every one of them is already owned by this subdomain. Nothing new stands on its own. | S2 belief_verification #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All five critical gaps are resolved: two by extending what a register carries, three by authoring something that does not exist. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the six questions raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Eight dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Five items re-grounded; all five CONFIRMED, none overturned. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All six findings are OBSERVED. Two dependencies remain under investigation and are recorded as such rather than promoted. |
