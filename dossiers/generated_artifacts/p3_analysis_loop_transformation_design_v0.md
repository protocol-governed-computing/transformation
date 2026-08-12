# Stage 3 — Analysis Loop: transformation / design
**Stage:** 3 — Analysis Loop
**CR:** generated_artifacts
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot and the record rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | Whether an artifact is generated is a fact about that artifact, so the artifact declares it. Nothing else can know it without being told, and a list held elsewhere is a second statement of one truth. | Decides where provenance lives. | OBSERVED | HIGH | CLOSED | Nine artifacts carry a sealed copy; nothing in any of them says so, and the pairing is known only to the tool that writes them. |
| Q2 | A design names the generator as the means by which the artifact it schedules is reached. The artifact stays the thing scheduled, because the artifact is what enters a composition. | Keeps the mandate scheduling artifacts and not tools. | OBSERVED | HIGH | CLOSED | A mandate schedules what enters the composition; a generator never does. |
| Q3 | Construction invoking the generator is the only arrangement with one producer. Refusing outright leaves delivery ungoverned; rendering directly makes construction a second producer of the same artifact. | Decides the shape of the construction change. | OBSERVED | HIGH | CLOSED | Two producers of one truth drift, and the drift is silent until something reads the stale one. |
| Q4 | Agreement is already computable and already reported. What is missing is that nothing refuses on it. The correction is to require the existing check, not to build one. | Makes the largest-sounding gap the smallest change. | OBSERVED | HIGH | CLOSED | The emission reports every artifact's agreement and returns non-zero; it is named in a runbook and a plan, and in no build. |
| Q5 | This change cannot be delivered through the path it creates. It is the last change requiring delivery by hand, and that must be stated as a decision rather than left as a circumstance. | Determines how this dossier itself closes. | OBSERVED | HIGH | CLOSED | Two prior dossiers stopped for this cause; this one alters the same artifacts. |
| Q6 | A template and the declaration it is read with determine the artifact only together, so they are one generator. Naming either alone would let a change amend one and regenerate from a stale pairing. | Decides what a generator is, and therefore what is named. | OBSERVED | HIGH | CLOSED | The emission reads both to produce one artifact. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| Some artifacts of this domain are produced by a generator rather than written. | S2 belief_verification #1 | CONFIRMED | Re-read: nine phase workflows, each named by the emission that writes it. |
| A design has no way to say that an artifact is produced from something else. | S2 belief_verification #2 | CONFIRMED | Re-read: no register names a generator and no rule asks for one. |
| Construction renders an artifact from the design alone, and would overwrite a generated one. | S2 belief_verification #3 | CONFIRMED | Re-read: an amendment renders the artifact that replaces its predecessor. |
| A generated artifact's agreement with its generator can be checked, and nothing requires the check. | S2 belief_verification #4 | CONFIRMED | Re-checked: present in a runbook and a plan document, absent from every build. |
| Two changes to this domain have already been designed and delivered by hand because of this. | S2 belief_verification #5 | CONFIRMED | Both closures re-read; each records the same cause. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The register in which a design states what an artifact must become | register | EXTEND | It states what the artifact is, and must also state how it is reached. |
| The mechanism that reports whether an artifact agrees with its generator | mechanism | REUSE | It exists, reports per artifact, and returns non-zero. |
| The build that must refuse on disagreement | mechanism | EXTEND | The check exists; no build requires it. |
| The construction step that produces an artifact | mechanism | EXTEND | It renders; it must also be able to invoke. |
| A statement, on an artifact, that it is generated and by what | declaration | AUTHOR_NEW | Nothing records it anywhere. |
| The nine phase workflows | artifact | EXISTING | Each gains a statement of its own provenance. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Gains a rule requiring a generated artifact to name its generator. | 0 | Nothing in the composition consumes a phase; phases are read by the tool that judges. |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | Unchanged in what it schedules; a scheduled artifact may now be reached by invocation. | 0 | The same. |
| The nine phase workflows | Each gains a statement that it is generated and by what. Their sealed rule sets are untouched. | 0 | The same. |
| The build | Gains a refusal it does not have. Every existing build that passes today must still pass, unless something is already stale. | — | The check reports agreement across all nine today. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Stating, on an artifact, that it is generated and by what | AUTHOR_NEW | Whether an artifact is generated is a fact about that artifact. Held anywhere else it is a second statement of one truth, able to disagree with the artifact it describes. | A list of generated artifacts held by the tool was rejected for that reason; it is what exists today and is why nothing else can know. | S2 gaps #4 |
| Naming, in a design, the generator an artifact is reached by | EXTEND | The design already states what an artifact must become. Stating how it is reached is one more thing said about the same artifact. | A separate register for generated artifacts was rejected: a design would then describe one artifact in two places. | S2 gaps #1 |
| Reaching a generated artifact by invoking its generator | EXTEND | The only arrangement with a single producer. | Refusing outright was rejected — it leaves delivery ungoverned permanently. Rendering directly was rejected — construction becomes a second producer and the two drift silently. | S2 gaps #2 |
| Refusing a build when an artifact and its generator disagree | EXTEND | The check exists and reports correctly. What is missing is that nothing acts on it. | Writing a new check was rejected: a second checker of one property is the defect this change exists to prevent, committed by the change itself. | S2 gaps #3 |
| Delivering this change by hand, once, and recording it | AUTHOR_NEW | The path this change creates does not exist until it is delivered. Stating it as a decision makes it the last such exception rather than an unexplained irregularity. | Waiting for the capability was rejected as circular. Delivering silently was rejected: two earlier changes were delivered by hand and only one recorded why. | S2 discovery_concerns #1 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | Everything corrected here belongs to the phases that judge a design and to how construction reaches an artifact. Both are owned by this subdomain. | S2 belief_verification #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All four are resolved: one by authoring a statement of provenance, three by extending what already exists. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the six raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Six dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Five items re-grounded; all five CONFIRMED. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All six findings are OBSERVED. None rests on inference. |
