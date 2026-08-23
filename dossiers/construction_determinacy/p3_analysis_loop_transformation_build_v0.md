# Stage 3 — Analysis Loop: transformation / build
**Stage:** 3 — Analysis Loop
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

The two questions Stage 2 left open, closed against the pinned composition; every belief it verified,
re-grounded rather than carried.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | **A build manifest is not an artifact a design determines, and construction should not write one.** Every field of it is configuration for the compiler that discovers a domain: which layer to search, which module holds the registry, which namespace an identity resolves to, which families to admit. None of that is a business fact any phase states, and the manifest's own account says as much. It is written by construction only because a domain that the compiler cannot discover is a domain that does not build, and hand-copying it had drifted — which is an argument for one producer, not for that producer being the renderer. | Removes a whole artifact from what construction may write, and with it the only fact construction ever derived from an identity. | OBSERVED | HIGH | CLOSED | The manifest declares a search layer, a registry module, an implementation namespace, a layer category, an identity rule and an artifact-type list. No register of any phase carries any of them. Its own text calls every field compiler configuration and says no phase designs it. |
| Q2 | **A default is a fact the renderer determines, and counting it as one the design determined is the same defect in a milder form.** Three are in use — a structure's layer, a transform's kind and its purity — and each is read from the design and falls back when absent. None is wrong today. But a design that omits one measures complete, which is exactly what the vocabulary's two literals did, and the only difference is that a default can be overridden and the literals cannot. | Fixes that the change reaches five facts rather than two, and settles that the test is where a value came from, not whether it can be overridden. | INFERRED | HIGH | CLOSED | A structure's layer falls back to a domain layer, a transform's kind to an atom, its purity to pure. Each sits beside a design lookup and is used only when the lookup returns nothing. The measure records the fallback as determined. |
| Q3 | **The measure cannot be fixed by changing what it counts, only by changing what the renderer reports.** Its population is the renderer's own output, walked leaf by leaf, and that is deliberate: a hand-maintained list drifted, reading complete while the renderer could reproduce one artifact in twenty-five. Restoring a declared list would restore that drift. What the measure lacks is not a better population but a second fact per leaf — where the value came from — which only the renderer knows. | Fixes the shape of the change: the renderer reports provenance per leaf, and the measure counts a leaf determined only when the design supplied it. | OBSERVED | HIGH | CLOSED | The requirement list is the emitted shape walked leaf by leaf; the declared list it replaced held a hundred and seventy facts against seven hundred and ten derived. The test applied to each leaf is emptiness alone. |
| Q4 | **One invention is worth keeping and the renderer already says why.** An event's moment-of-occurrence field is supplied by the renderer because the event constitution fixes it, and a design that states its own keeps it. That is a fact the design need not state because something else already governs it — which is a different case from a fact nobody governs and nobody states. | Establishes that the change refuses an invented fact rather than every fact the renderer supplies, and that the distinction must be declarable rather than left in prose. | OBSERVED | HIGH | CLOSED | The field is added with its ground stated in the builder's own text, and a design declaring the same field overrides it. No mechanism reads that ground; it is prose beside code. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| The population the measure counts is derived from the renderer rather than from the artifact. | S2 belief_verification #1 | CONFIRMED | The requirement list is the emitted shape walked leaf by leaf, and a leaf is determined when it is not empty. |
| A vocabulary's group name and spelling rule are literals in the renderer. | S2 belief_verification #2 | CONFIRMED | One line writes both as constants for every vocabulary; no register carries either. |
| A build manifest is written when the renderer judges the domain to have none. | S2 belief_verification #3 | CONFIRMED | Written when the mandate schedules anything, the file does not exist beneath the root, and no generator was named. |
| No design register carries a group name, a spelling rule or a domain name. | S2 belief_verification #4 | CONFIRMED | Re-read across all twenty registers of the seventh phase. |
| Every family the renderer writes may carry invented facts, not only these two. | S2 belief_verification #5 | CONFIRMED | Confirmed as Stage 2 narrowed it: one defect, one declared exception, three defaults. The wider belief Stage 1 held is not what was found. |
| Nothing else was written that the mandate did not schedule. | S2 belief_verification #6 | CONFIRMED | Two emits; the manifest is the only artifact ever written outside a mandate. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The rendering of each artifact | capability | EXTEND | Renders every family from the design. The change has it report, per leaf, where the value came from. |
| The measure of a design | capability | EXTEND | Counts a leaf determined when it is not empty. The change has it count a leaf determined when the design supplied it. |
| The writing of a construction | capability | EXTEND | Writes what the mandate schedules, plus a manifest. The change removes the manifest. |
| The declaration of a fact something else governs | governance | AUTHOR_NEW | Exists once, in prose beside code, for an event's moment field. Nothing reads it and nothing else may state it. |
| The registers of the seventh phase | governance | EXTEND | Twenty exist. A vocabulary's group and spelling have no column, and the change adds them. |
| The compiler's discovery of a domain | governance | INVESTIGATE | The manifest configures it. Who produces the manifest once construction stops is not this change's to settle alone. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | Every artifact construction renders, in every family. It gains the obligation to report where each value came from. | 1 | Reported by the composition. |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | Every design measured. Its test changes from emptiness to provenance. | 1 | Reported by the composition. |
| transformation::CC_PERSIST_ARTIFACTS_V0 | What may be written. It loses the manifest. | 1 | Reported by the composition. |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Names the three steps; unchanged in shape. | 1 | Reported by the composition. |
| transformation::WF_CONSTRUCT_ARTIFACTS_V0 | The act as a whole; unchanged in shape. | 0 | Reported by the composition. |
| transformation::IN_CONSTRUCTION_REQUESTED_V0 | Unchanged. What is offered for construction is correct. | 1 | Reported by the composition. |
| Every design already written | Each is re-measured under a stricter test, and any that relied on a default or a literal reads short. | 22 | Twenty-two dossiers carry a pin; each would be re-measured before its next construction. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|-----------|----------|-----------|---------------------|----------------|
| Reporting where each rendered value came from | AUTHOR_NEW | Only the renderer knows, and nothing records it today. It is the one fact the measure needs and cannot derive. | Inferring provenance by re-reading the design was considered and rejected: it would be a second opinion about the renderer, which is the drift the derived list ended. | analysis_findings #3 |
| Measuring a design | EXTEND | The population stays the renderer's own output, because deriving it is what stops it drifting. Only the test per leaf changes. | Restoring a declared requirement list was checked and rejected: it read complete while the renderer could reproduce one artifact in twenty-five. | analysis_findings #3 |
| Stating a vocabulary's group and spelling | EXTEND | The register that carries a vocabulary's values is where its group and spelling belong; it has the rows and lacks the columns. | A separate register for vocabulary shape was considered and rejected: one vocabulary's facts stated in two places is the disagreement this change is about. | analysis_findings #3 |
| Declaring that something else governs a fact | AUTHOR_NEW | One such fact exists and its ground is prose beside code. A refusal that cannot be told from a justified supply would refuse the event's moment field. | Removing the event's moment field was considered and rejected: the event constitution fixes it and no design should restate what a constitution already settles. | analysis_findings #4 |
| Writing a build manifest | REUSE | Construction stops writing it. Nothing replaces it inside this change; how a domain is founded is named for a ruling. | Giving the manifest a design was considered and rejected: every field of it is compiler configuration and no business fact determines any of them. | analysis_findings #1 |

---

## 6. Placement Decision

<!-- register:placement_decision -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | build | Measuring a design, rendering its artifacts and writing them is what this subdomain governs, and all three change. The registers the seventh phase declares belong to the design subdomain and are named for it, not written here. | S1 governance_scope #1 |

---

## 7. Discovery Saturation

<!-- register:saturation -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| Every question Stage 2 left open is closed. | SATISFIED | The manifest leaves construction; a default counts as an invention, which widens the change from two facts to five. |
| Every belief Stage 2 verified was re-grounded. | SATISFIED | All six confirmed, including the one Stage 2 narrowed against Stage 1; none overturned. |
| The count of the defect is established. | SATISFIED | Two literals no design may state, three defaults a design may state and need not, one artifact no mandate schedules. Six facts across three of eleven families. |
| The one justified invention is distinguished from the rest. | SATISFIED | An event's moment field is supplied because a constitution fixes it, and a design stating its own overrides it. That ground exists in prose and the change makes it declarable. |
| The shape of the fix is determined without designing it. | SATISFIED | The renderer reports provenance per leaf; the measure tests provenance rather than emptiness; the population stays derived. Nothing further is needed to state what the change does. |
