# Stage 3 — Analysis Loop: transformation / design
**Stage:** 3 — Analysis Loop
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot and the recorded history rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The five gaps are one chain, not five problems. A correction declaring its effectivity is what produces a version; a version is what an approval pins; a pinned approval is what makes migrated distinguishable from approved. Correcting the first in isolation would leave the rest unreachable, and correcting any later one first is impossible. | Fixes the order of the work and rules out partial delivery. | OBSERVED | HIGH | CLOSED | Each gap's evidence names the one before it as its cause. |
| Q2 | A version is a name for a state of the rule set, created only where admissibility could have changed. It is not a count and not a date; a count says how many rules exist and a date says when, and neither says whether a prior document may still pass. | Decides what a version is, and keeps it meaningful as a signal. | OBSERVED | HIGH | CLOSED | The rule set reports its count and consistency today; neither distinguishes one state from another. |
| Q3 | The correction declares its effectivity because only the correction knows what it added and why. The rule set records the declaration because a claim held only by its author is what exists today and is why five dossiers were migrated with the reasoning in one commit message. | Places the declaration and its record with different owners, deliberately. | OBSERVED | HIGH | CLOSED | The amendment, its reason and its reversal survive in git and in no dossier. |
| Q4 | Naming the dossiers a retroactive correction affects is part of that correction. Discovered later, it is discovered by them failing — which is how it was discovered this session, after the fact and by surprise. | Makes the affected set a declared output rather than an emergent one. | OBSERVED | HIGH | CLOSED | Three completed dossiers failed at once, unannounced, and were amended in response. |
| Q5 | Approved, migrated and re-approved are three states of a dossier and must be carried by the dossier. Held anywhere else they are a second statement about a document that the document itself contradicts. | Decides where a dossier's state lives. | OBSERVED | HIGH | CLOSED | The distinction exists today only where someone wrote it in prose, outside the dossiers entirely. |
| Q6 | A deliberate refusal and a defect look identical, and the tool offers no way to tell them apart. Three dossiers read inadmissible correctly, and nothing says so. Making a deliberate red legible is part of this change, because without it the easy act remains the wrong one. | Prevents the correction from being undone by the next person who runs the suite. | OBSERVED | HIGH | CLOSED | Three dossiers currently read inadmissible by design; the tool reports them exactly as it reports a fault. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| A document is judged only against the rules in force when it is judged. | S2 belief_verification #1 | CONFIRMED | Re-read: a verdict names the phase and the rule count, and no version. |
| Nothing records which rules a document was approved under. | S2 belief_verification #2 | CONFIRMED | Re-searched: no dossier in either domain carries a version. |
| A correction cannot say whether it is retroactive. | S2 belief_verification #3 | CONFIRMED | Re-read: neither a template nor a declaration carries a statement of effect, and no rule asks. |
| Dossiers have already been amended to satisfy rules written after their approval, and nothing in them says so. | S2 belief_verification #4 | CONFIRMED | Re-read from the recorded history: amended, then restored, both recorded outside the dossiers. |
| A rule set has no version at all. | S2 belief_verification #5 | CONFIRMED | Re-read: a count and a consistency report, and nothing that names a state. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| A statement, on a correction, of whether it is retroactive | declaration | AUTHOR_NEW | Nothing carries one. |
| A name for a state of the rule set | declaration | AUTHOR_NEW | The rule set has no version in any form. |
| A statement, on an approval, of the version it was given under | declaration | AUTHOR_NEW | No dossier carries one. |
| The list of dossiers a retroactive correction affects | declaration | AUTHOR_NEW | Discovered by failure today, declared nowhere. |
| A dossier's state — approved, migrated or re-approved | declaration | AUTHOR_NEW | Exists only in prose outside the dossiers. |
| The verdict a phase renders | mechanism | EXTEND | It states the phase and the rule count; it must also state the version. |
| The mechanism that refuses a run against an unpinned baseline | mechanism | REUSE | The same principle, one axis over, already enforced and refusing before any phase runs. |
| The reporting of a deliberate refusal | mechanism | EXTEND | A deliberate red and a defect are reported identically. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| The nine phase workflows | Each renders a verdict that must name the version it used. | 0 | Nothing in the composition consumes a phase. |
| Every existing dossier | Each gains a state and, where approved, a pinned version. Three are approved under a version that predates versioning and must be named retrospectively as the first. | 8 | Eight dossiers exist across two domains and this one. |
| The corrections made this session | Two, one of each effectivity, neither declared. They are the first test of the declaration and should be recorded retrospectively. | 2 | One changed no verdict; one invalidated every dossier that existed. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Declaring, on a correction, whether it is retroactive | AUTHOR_NEW | Only the correction knows what it added and why. | Inferring it from what the correction touched was rejected: a change to a diagnostic message and a change to a required column touch the same files and differ entirely in effect. | S2 gaps #1 |
| Naming a state of the rule set | AUTHOR_NEW | An approval must pin something, and a count is not a state. | Using the rule count was rejected — it says how many rules exist, not which state. Using a date was rejected — it says when, not whether a prior document may still pass. | S2 gaps #2 |
| Pinning, on an approval, the version it was given under | AUTHOR_NEW | Without it an approval that still stands cannot be told from one whose rules have moved. | Recording it centrally was rejected: a claim about a document, held away from it, can disagree with it. | S2 gaps #3 |
| Naming the dossiers a retroactive correction affects | AUTHOR_NEW | Discovered later, it is discovered by failure — which is how it was discovered this session. | Leaving it to be found by re-running everything was rejected: that is the current behaviour and it produced an unannounced mass failure. | S2 gaps #4 |
| Carrying a dossier's state on the dossier | AUTHOR_NEW | Three states exist and the corpus cannot express any of them. | Holding state in a register outside the dossiers was rejected for the reason above. | S2 gaps #5 |
| Stating, in a verdict, the version it was rendered against | EXTEND | A verdict already states the phase and the rule count; the version is one more thing said about the same judgement. | A separate report was rejected: a verdict and a claim about that verdict, held apart, can disagree. | S2 belief_verification #1 |
| Reporting a deliberate refusal as deliberate | EXTEND | A red that is correct and a red that is a fault are reported identically, and the easy response to either is to make it pass. | Documenting the distinction was rejected: it is documented, in a handoff, and the migration happened anyway. | S2 discovery_concerns #2 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | Versions, effectivity and verdicts all belong to the phases that judge a design, which this subdomain owns. | S2 belief_verification #5 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All five are resolved: five by authoring what does not exist, and the chain among them is established. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the six raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Eight dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Five items re-grounded; all five CONFIRMED. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All six findings are OBSERVED. None rests on inference. |
