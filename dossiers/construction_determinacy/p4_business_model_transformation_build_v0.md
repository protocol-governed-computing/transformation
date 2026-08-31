# Stage 4 — Business Model: transformation / build
**Stage:** 4 — Business Model
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The design | States what is to be built. | Declaring — it is the only authority construction may take a fact from. | S1 authority_boundaries #3 |
| The renderer | Produces each artifact from what the design states. | Producing — and today also supplying facts the design does not state. | S1 business_vocabulary #3 |
| The measure | Decides whether a design determines its artifacts, and refuses it if not. | Deciding — nothing is written unless it admits the design. | S1 authority_boundaries #2 |
| The mandate | States what is to be built and in what order. | Declaring — it freezes scope, and something written outside it was approved by nobody. | S1 business_vocabulary #2 |
| A constitution | Fixes a fact no design should have to restate. | Governing — the reason one invented fact is worth keeping. | S3 analysis_findings #4 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Design | The approved statement of what is to be built. | The seventh phase document, with twenty registers. | S2 entities #1 |
| Mandate | The approved statement of what is to be built in what order. | The eighth phase document, scheduling only what does not yet exist. | S2 entities #2 |
| Determined fact | Something about an artifact that the design states. | Not held. Judged today by whether the rendered value came out empty. | S2 entities #4 |
| Invented fact | Something the renderer supplies from anywhere but the design. | Not held, not counted, indistinguishable from a determined one. | S2 entities #5 |
| The measure | The count of how much of an artifact the design determines. | Computed per attempt; refuses below complete. | S2 entities #6 |
| Provenance | Where a rendered value came from. | Held nowhere. The one fact the measure needs and cannot derive. | S3 analysis_findings #3 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The two literals | A vocabulary's group name and spelling rule, written for every vocabulary the renderer will ever produce. | S2 belief_verification #2 |
| The three defaults | A structure's layer, a transform's kind and its purity — each read from the design and falling back when absent. | S3 analysis_findings #2 |
| The one declared exception | An event's moment-of-occurrence field, supplied because the event constitution fixes it, with its ground in prose beside code. | S3 analysis_findings #4 |
| The build manifest | An artifact no mandate schedules, whose every field is compiler configuration. | S3 analysis_findings #1 |
| The derived requirement list | Seven hundred and ten facts, against a hundred and seventy in the declared list it replaced. | S3 analysis_findings #3 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A design was measured | Before anything is written | The design determines its artifacts, or nothing is written. | S1 business_events #1 |
| An artifact was written | A design measuring complete | What the design states becomes the artifact. | S1 business_events #2 |
| An artifact was written carrying a fact nobody designed | Whenever the renderer sources a fact from its own text | The artifact has an author the approval never named. This is the state this change ends. | S1 business_events #3 |
| An artifact was written that no mandate scheduled | A build manifest being founded | Something outside a frozen scope was approved by nobody. | S3 analysis_findings #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Renderer | reports | Provenance | Reporting where each rendered value came from. | S3 authoring_decisions #1 |
| Measure | tests | Provenance | Measuring a design. | S3 authoring_decisions #2 |
| Design | states | Determined fact | Stating a vocabulary's group and spelling. | S3 authoring_decisions #3 |
| Constitution | governs | Determined fact | Declaring that something else governs a fact. | S3 authoring_decisions #4 |
| Renderer | stops writing | Build manifest | Writing a build manifest. | S3 authoring_decisions #5 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Reporting where each rendered value came from | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The one fact the measure needs and cannot derive. Without it the rest is a correction to two builders. |
| Measuring a design | S3 authoring_decisions #2 | CRITICAL | GAP-2 | The population stays derived; only the test per leaf changes, from emptiness to provenance. |
| Stating a vocabulary's group and spelling | S3 authoring_decisions #3 | MAJOR | GAP-3 | The register carrying a vocabulary's values has the rows and lacks the columns. |
| Declaring that something else governs a fact | S3 authoring_decisions #4 | MAJOR | GAP-4 | Without it the change would refuse an event's moment field, which a constitution rightly fixes. |
| Writing a build manifest | S3 authoring_decisions #5 | MAJOR | GAP-5 | Removed from construction. Every field of it is compiler configuration and no business fact determines any. |
| Admitting a design for construction | S3 dependency_discoveries #6 | SATISFIED | | What is offered is correct; what is done with it is not. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| build | build | capability call | SATISFIED | S3 dependency_discoveries #1 — the renderer produces every family and is where provenance is known. |
| build | design | data read | SATISFIED | S3 dependency_discoveries #5 — the registers a design states belong to that subdomain and are named for it, not written here. |
| build | build | data read | SATISFIED | S3 dependency_discoveries #2 — the measure already walks what the renderer emits. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | The measure keeps its threshold; a design below complete still writes nothing. | S1 constraints #1 | governance rule |
| 2 | A fact is added to what the measure counts, never removed to make a design pass. | S1 constraints #2 | governance rule |
| 3 | Nothing is written that the mandate did not schedule. | S1 constraints #3 | governance rule |
| 4 | A renderer supplies no fact from a path, a directory or a dossier's location. | S1 constraints #4 | governance rule |
| 5 | An artifact that is rendered is admissible to the platform, or the rendering is wrong. | S1 constraints #5 | governance rule |
| 6 | The measure's population stays derived from the renderer, because deriving it is what stops it drifting. | S3 analysis_findings #3 | domain knowledge |
| 7 | A fact a constitution fixes may be supplied, and the ground must be declared rather than left in prose. | S3 analysis_findings #4 | domain knowledge |
| 8 | A default is an invention; overridability is not the test. | S3 analysis_findings #2 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Reporting where each rendered value came from | build | AUTHOR_NEW |
| GAP-2 | S3 authoring_decisions #2 | Measuring a design | build | EXTEND |
| GAP-3 | S3 authoring_decisions #3 | Stating a vocabulary's group and spelling | design | EXTEND |
| GAP-4 | S3 authoring_decisions #4 | Declaring that something else governs a fact | build | AUTHOR_NEW |
| GAP-5 | S3 authoring_decisions #5 | Writing a build manifest | build | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The renderer reports, per leaf, where the value came from. | S3 analysis_findings #3 | Only the renderer knows. Inferring provenance by re-reading the design would be a second opinion about the renderer, which is the drift the derived list ended. | Rules out deriving provenance anywhere but at the point of rendering, and makes every builder answerable for each value it writes. |
| 2 | The measure's population stays derived; only its test changes. | S3 analysis_findings #3 | Deriving the population is what stops it drifting — the declared list it replaced read complete while the renderer could reproduce one artifact in twenty-five. | Rules out restoring a declared requirement list, and confines the change to the test applied per leaf. |
| 3 | A default counts as an invention. | S3 analysis_findings #2 | A design that omits a default measures complete, which is what the two literals did. Overridability is not the difference; where the value came from is. | Widens the change from two facts to five, and rules out exempting a fallback because it can be overridden. |
| 4 | A fact a constitution fixes may be supplied, and the ground is declared. | S3 analysis_findings #4 | An event's moment field is supplied because the event constitution fixes it. A refusal that could not tell that from an invention would refuse it. | Rules out refusing every fact the renderer supplies, and rules out leaving the justification in prose nothing reads. |
| 5 | Construction stops writing a build manifest. | S3 analysis_findings #1 | Every field of it is compiler configuration and no business fact determines any of them. It was written by the renderer because hand-copying drifted, which argues for one producer, not for that producer. | Rules out giving the manifest a design, and leaves how a domain is founded to a ruling this change does not make. |
| 6 | A vocabulary's group and spelling are stated in the register that carries its values. | S3 authoring_decisions #3 | That register has the rows and lacks the columns. One vocabulary's facts stated in two places is the disagreement this change is about. | Rules out a separate register for vocabulary shape. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Reporting where each rendered value came from | GAP-1 |
| Measuring a design | GAP-2 |
| Stating a vocabulary's group and spelling | GAP-3 |
| Declaring that something else governs a fact | GAP-4 |
| Writing a build manifest | GAP-5 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Founding a domain the compiler can discover | Construction stops writing the manifest; who produces it instead is a ruling this change does not make. |
| Re-measuring every design already written | Each dossier's own act, once the stricter test is in force. |
| The nine families never yet emitted | Two emits are a thin basis; each family's first emission is where a further invention would surface. |
