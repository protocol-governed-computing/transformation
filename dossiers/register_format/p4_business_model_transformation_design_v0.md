# Stage 4 — Business Model: transformation / design
**Stage:** 4 — Business Model
**CR:** register_format
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Author | Writes phase documents, their prose and their registers. | Proposing — never decides admissibility. | S1 business_events #1 |
| Phase | Judges a document against the rule set it declares and renders a verdict. | Deciding — the sole arbiter of whether a document is admissible. | S1 authority_boundaries #1 |
| Construction tests | Reproduce artifacts from the designs and mandates of delivered dossiers. | Checking — decide nothing about admissibility. | S1 business_events #2 |

<!-- register:bm_entities business_language -->
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Phase | One step of the transformation lifecycle, with a rule set of its own. | One declared workflow per phase, owned by this subdomain. | S2 entities #1 |
| Rule set | The rules a phase declares, against which it judges a document. | A copy held inside the phase's workflow, produced from the phase's template and its declaration together. | S2 entities #2 |
| Register | The part of a phase document that states facts the rules judge. | A table inside the document's prose, marked by a comment above it. | S2 entities #3 |
| Prose | The part of a phase document that explains the change to a person. | The rest of the same text. | S2 entities #4 |
| Verdict | The result of judging a document against a rule set: admissible or inadmissible. | Returned by the judging, and held by nobody. | S2 entities #5 |
| Finding | One reason a verdict gives for a document being inadmissible. | Part of the verdict: the rule that raised it, where it was found, and a detail. | S2 entities #6 |
| Old form | Registers written as tables inside the prose. | Every phase document and test document today. | S2 entities #7 |
| New form | Registers carried as structured data in a block of their own, apart from the prose. | Nothing holds it. | S2 entities #8 |
| Test copy | A copy of a delivered dossier that the construction tests reproduce artifacts from. | Exists for one domain only, as maintained fixtures; every other domain is read from its delivered dossiers. | S2 entities #9 |

<!-- register:resources optional business_language -->
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The test documents | They exercise the judging, are in the old form, and are converted once to prove the two forms receive the same findings. | S3 dependency_discoveries #7 |
| The test copies | The designs and mandates of the delivered dossiers the construction tests read, converted beside the catalog's fixtures. | S3 analysis_findings Q6 |

<!-- register:events business_language -->
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A document was judged | A document is checked against a rule set | The verdict and its findings are the same in either form. | S1 business_events #1 |
| A document was converted | A test document or a test copy is rewritten in the new form | Its verdict and findings are compared with the old form's. | S1 business_events #2 |
| The old reading was retired | Every converted document received the same verdict and findings in both forms | One form exists from then on. | S1 business_events #3 |

<!-- register:relationships optional business_language -->
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Document | carries | Register | Carrying registers as structured data apart from the prose. | S3 authoring_decisions #1 |
| Document | holds | Block | A block for structured facts in every document that carries registers. | S3 authoring_decisions #2 |
| Converter | rewrites | Document | Converting a document from the old form to the new. | S3 authoring_decisions #3 |
| Construction tests | read | Test copy | Keeping the construction tests' coverage. | S3 authoring_decisions #4 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|------------|----------------|--------|--------------------|-------|
| Carrying registers as structured data apart from the prose | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The reading exists; what it reads changes. |
| A block for structured facts in every document that carries registers | S3 authoring_decisions #2 | CRITICAL | GAP-2 | The templates and the projection write it. |
| Converting a document from the old form to the new | S3 authoring_decisions #3 | CRITICAL | GAP-3 | Mechanical, once, and gone with the old reading. |
| Keeping the construction tests' coverage | S3 authoring_decisions #4 | CRITICAL | GAP-4 | A test copy is a design and a mandate. |
| Judging a document against declared rules | S3 dependency_discoveries #3 | SATISFIED |  | Receives the same shape from either reader; unchanged. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| build | design | data read | SATISFIED | S3 analysis_findings Q3 — construction binds the shared reading and is re-pointed, keeping its identity. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | No document changes verdict because its form changed. | S1 business_invariants #1 | invariant |
| 2 | One form of phase document exists at a time. | S1 business_invariants #2 | invariant |
| 3 | No compatibility with v5. Dossiers approved under v5 stay as published, and this change neither converts nor reads them. | S1 constraints #1 | governance rule |
| 4 | The old reading retires once this change shows that the old and new forms receive the same verdicts. | S1 constraints #2 | governance rule |
| 5 | The delivered dossiers the construction tests reproduce artifacts from are copied and converted as test fixtures before the old reading retires. | S1 constraints #3 | governance rule |
| 6 | One form for every document that carries registers, from the seed to the mandate. | S1 constraints #4 | governance rule |
| 7 | The business problem statement has no registers and stays prose. | S1 constraints #5 | governance rule |
| 8 | The new form replaces the old form. The two never coexist. | S1 constraints #6 | governance rule |
| 9 | What this change replaces is deleted, not stood down. The readers of the old form are removed from the composition with their implementation. | S1 constraints #7 | governance rule |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|------------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Carrying registers as structured data apart from the prose | design | EXTEND |
| GAP-2 | S3 authoring_decisions #2 | A block for structured facts in every document that carries registers | design | EXTEND |
| GAP-3 | S3 authoring_decisions #3 | Converting a document from the old form to the new | design | NEW |
| GAP-4 | S3 authoring_decisions #4 | Keeping the construction tests' coverage | design | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Only the reading changes; the new reader returns the old reader's shape. | S3 analysis_findings Q1 | Every consumer receives registers as data from one reading step. | Rules out changing what any rule judges. A finding that moves is a regression. |
| 2 | Values inside cells stay text, and an empty register keeps its sentinel row. | S3 analysis_findings Q2 | The two forms must be comparable finding for finding. | Rules out giving values structure here. |
| 3 | The two readers are replaced by new versions; the four contracts that bind them are re-pointed. | S3 analysis_findings Q3 | The readers change meaning; the contracts do not. | Rules out changing any phase workflow. |
| 4 | The replaced readers are deleted at delivery, by a recorded human act. | S3 analysis_findings Q4 | Their implementation is the old reading, and nothing names them after the repoints. | Rules out standing them down and carrying them. |
| 5 | The converter is the old reading writing out what it reads, and goes with it. | S3 analysis_findings Q5 | Conversion must be mechanical to show the forms agree. | Rules out converting any document by hand. |
| 6 | A test copy is a dossier's design and mandate, converted, beside the catalog's fixtures. | S3 analysis_findings Q6 | The construction tests read nothing else. | Rules out editing a delivered dossier. |
| 7 | Findings are compared as text: rule, location and detail. | S3 analysis_findings Q7 | One evaluator judges both forms. | Rules out changing the shape of a finding here. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|------------|------------------|
| Carrying registers as structured data apart from the prose | GAP-1 |
| A block for structured facts in every document that carries registers | GAP-2 |
| Converting a document from the old form to the new | GAP-3 |
| Keeping the construction tests' coverage | GAP-4 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| How a value inside a register is structured | Routing written as text stays text here. Giving such values a structure is the next change. |
| Where the rules are declared, and in what language | That is a later change. |
| Which rule set judged a document | A document, a verdict and an approval naming their rule set is a later change, made once the rules are declared outside the code. |
| Governing and specifying construction on its own | That is a later change. |
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
