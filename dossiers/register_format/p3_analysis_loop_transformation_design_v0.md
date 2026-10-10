# Stage 3 — Analysis Loop: transformation / design
**Stage:** 3 — Analysis Loop
**CR:** register_format
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot, the readers of a phase document, and the tests that read delivered dossiers.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | Every consumer of a register receives it as data from one reading step, in one shape: a header, sections, and registers each with columns and rows. A reader of the new form that returns that shape changes nothing downstream. | Confines the change to the reading, the writers of documents and the test documents. Makes identical findings across the two forms testable. | OBSERVED | HIGH | CLOSED | The reading feeds three judging contracts and one constructing contract, and the judging code reads only the shape it returns. |
| Q2 | Values inside cells keep their text form, and an empty register keeps its sentinel row, so the new reader can return exactly what the old one returns. Giving them structure is the next change. | The two forms can be compared finding for finding. | OBSERVED | HIGH | CLOSED | Construction and the judging both split values inside cells themselves. |
| Q3 | The readers change meaning: they read a different form, and a document in the old form no longer parses. Each is replaced by a new version. The four contracts that bind them keep their meaning and are re-pointed. | Two replacements and four repoints; no phase workflow changes. | OBSERVED | HIGH | CLOSED | A change of meaning is a new identity; a contract that names a replaced reader names its successor and keeps its own identity. |
| Q4 | The replaced readers are deleted, not stood down. Their implementation is the old reading, which this change retires, and nothing names them once the contracts are re-pointed. The design language has no deletion action and needs none: a deletion is a recorded human act, carried out at delivery. | The first realization of deleting a superseded artifact by a recorded act. | OBSERVED | HIGH | CLOSED | No live artifact names the readers but the four contracts. The only sealed snapshot containing them is an archived release, which retains them itself. |
| Q5 | The converter is the old reading serialising what it reads into the new form. It is a tool, not an artifact, and it is deleted with the old reading. | Conversion is mechanical and the same for every document. | OBSERVED | HIGH | CLOSED | The old reading already returns registers as data; writing that data out is the new form. |
| Q6 | The construction tests read only a dossier's design and mandate. A test copy is those two documents, converted, beside the catalog's fixtures. | 32 documents from 16 dossiers are copied and converted. The delivered originals are not edited. | OBSERVED | HIGH | CLOSED | Each dossier contributes its design and its mandate and nothing else. |
| Q7 | A finding's register and row live only in its location text. Comparing findings as text is exact for one evaluator judging two forms. Holding the location apart is needed only when two evaluators are compared. | No change to findings here. | OBSERVED | HIGH | CLOSED | The same evaluator writes the same text for the same register and row. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| A phase document carries prose and registers in one Markdown text, with each register a table inside the prose. | S2 belief_verification #1 | CONFIRMED | Re-read: each register is a table opened under a marker comment in the document's text. |
| The rules read each register through conventions that only the code states. | S2 belief_verification #2 | CONFIRMED | Re-searched the pinned snapshot: no artifact states a reading convention. |
| Fourteen reading conventions and seven formats inside cells exist today. | S2 belief_verification #3 | CONFIRMED | Re-counted from the reading and judging code. |
| A column is found by the start of its name, a row reading NONE IDENTIFIED means an empty register, and a dash means a cell says nothing. | S2 belief_verification #4 | CONFIRMED | Re-read each convention where the reading applies it. |
| Routing is written as text, an outcome and a target joined by an arrow, and the code splits it. | S2 belief_verification #5 | CONFIRMED | Re-read: both the judging and construction split routing values themselves. |
| The construction tests reproduce artifacts from copies of delivered dossiers. | S2 belief_verification #6 | CONFIRMED | Re-counted: 42 documents from 21 dossiers in seven roots; 16 dossiers read where delivered. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The reading of a document's registers | capability | EXTEND | It reads the old form only, and must read the new form instead. |
| The reading of a phase's prior documents | capability | EXTEND | The same. |
| The judging of a document against declared rules | capability | EXISTING | It receives the same shape from either reader and is unchanged. |
| The phase templates | template | EXTEND | They lay out registers as tables inside prose. |
| The projection that writes a change request from its seed | capability | EXTEND | It writes registers as tables. |
| The builders of test documents and the design tests | test documents | EXTEND | They write designs as tables. |
| The test documents and test copies | test documents | EXTEND | They are in the old form and are converted once. |
| A converter from the old form to the new | capability | AUTHOR_NEW | Nothing converts a document today. |
| Construction's reading of registers | capability | EXISTING | It receives registers from the shared reading, and splits values inside cells itself. |
| Dossiers delivered before this change | dossier | EXISTING | They stay as delivered; their test copies are what the tests read. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::CT_PURE_PARSE_REGISTERS_V0 | Replaced by a reader of the new form, and deleted. | 4 | Bound by three judging contracts and one constructing contract in force. |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | Replaced by a reader of the new form, and deleted. | 3 | Bound by the three judging contracts in force. |
| transformation::CC_JUDGE_DOCUMENT_V0 | Re-pointed at the new readers. | 3 | Bound by the seed, change request and first domain-model workflows. |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | Re-pointed at the new readers. | 6 | Bound by the six later phase workflows in force. |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | Re-pointed at the new readers. | 1 | Bound by the analysis-loop workflow in force. |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Re-pointed at the new register reader. | 1 | Bound by the construction workflow. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Carrying registers as structured data apart from the prose | EXTEND | The reading exists; what it reads changes. Every consumer already receives registers as data. | Keeping tables and writing down their conventions was rejected: the business author chose one structured form. Carrying both forms was rejected: the two never coexist. | S2 gaps #1 |
| A block for structured facts in every document that carries registers | EXTEND | The templates and the projection write it; the prose stays around it. | A separate file beside the document was rejected: the prose and its facts would be two things to keep together. | S2 gaps #2 |
| Converting a document from the old form to the new | AUTHOR_NEW | The old reading writes out what it reads. It runs once over the test documents and test copies, and goes with the old reading. | Re-authoring the test documents by hand was rejected: a conversion that is not mechanical cannot show the two forms agree. | S2 gaps #3 |
| Keeping the construction tests' coverage | EXTEND | Each delivered dossier the tests read gets a test copy of its design and mandate, converted, as the catalog's already has. | Accepting the lost coverage was rejected by the business author. | S2 gaps #4 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | The reading, the templates and the phase documents belong to the subdomain that judges a design. Construction consumes the shared reading and stays adjacent. | S2 architectural_observations #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | Both critical gaps are resolved by extending the reading and the writers. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the seven questions raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Ten dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Six items re-grounded; all six CONFIRMED. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All seven findings are OBSERVED. |
