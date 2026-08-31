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
| Correction | Declares whether it can alter a prior dossier's admissibility. | Declaring — only it knows what it added and why. | S1 business_vocabulary #3 |
| Rule set | Records the declaration as governed history. | Recording — it holds what corrections declare. | S1 business_vocabulary #1 |
| Person at a gate | Closes an approval, and re-closes one after migration. | Deciding — the only actor that approves. | S1 authority_boundaries #3 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Rule-set version | A named state of the rule set, created only where admissibility could have changed. | Nothing holds one. | S2 entities #2 |
| Effectivity | A correction's declaration of whether it is retroactive. | Nothing holds one. | S2 entities #3 |
| Approval | A gate closed on a dossier, under a stated version. | Recorded in the dossier, without saying under what. | S2 entities #4 |
| Migration | A dossier amended to satisfy a later rule set. | Recorded in one commit message and nowhere else. | S2 entities #5 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The eight existing dossiers | Each gains a state, and where approved a pinned version. Three predate versioning and are named retrospectively as the first. | S3 impact_analysis #2 |
| The two corrections made this session | One non-retroactive, one retroactive, neither declared. The first test of the declaration. | S3 impact_analysis #3 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A rule-set version was created | A retroactive correction is made | Documents approved before it may no longer pass. | S1 business_events #1 |
| A dossier was migrated | A dossier is amended to satisfy a later rule set | Its verdict is no longer the one it was approved with. | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Correction | declares | Effectivity | Declaring, on a correction, whether it is retroactive. | S3 authoring_decisions #1 |
| Rule set | is named by | Rule-set version | Naming a state of the rule set. | S3 authoring_decisions #2 |
| Approval | pins | Rule-set version | Pinning, on an approval, the version it was given under. | S3 authoring_decisions #3 |
| Correction | names | Affected dossiers | Naming the dossiers a retroactive correction affects. | S3 authoring_decisions #4 |
| Dossier | carries | Its state | Carrying a dossier's state on the dossier. | S3 authoring_decisions #5 |
| Verdict | states | Rule-set version | Stating, in a verdict, the version it was rendered against. | S3 authoring_decisions #6 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Declaring, on a correction, whether it is retroactive | S3 authoring_decisions #1 | CRITICAL | GAP-1 | First in the chain; nothing else is reachable without it. |
| Naming a state of the rule set | S3 authoring_decisions #2 | CRITICAL | GAP-2 | A count is not a state and a date is not a state. |
| Pinning, on an approval, the version it was given under | S3 authoring_decisions #3 | CRITICAL | GAP-3 | What makes an approval that stands distinguishable from one whose rules moved. |
| Naming the dossiers a retroactive correction affects | S3 authoring_decisions #4 | CRITICAL | GAP-4 | Declared output, not emergent discovery. |
| Carrying a dossier's state on the dossier | S3 authoring_decisions #5 | CRITICAL | GAP-5 | Approved, migrated, re-approved. |
| Stating, in a verdict, the version it was rendered against | S3 authoring_decisions #6 | CRITICAL | GAP-6 | One more thing said about a judgement already described. |
| Reporting a deliberate refusal as deliberate | S3 authoring_decisions #7 | CRITICAL | GAP-7 | Without it the easy act stays the wrong one. |
| Refusing a run against a baseline that is not the pinned one | S3 dependency_discoveries #7 | SATISFIED | | The same principle, one axis over, already enforced. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| design | design | capability call | GAP | S3 analysis_findings Q1 — the five gaps are one chain and each depends on the one before it. |
| design | build | data read | SATISFIED | S1 governance_scope #2 — the construction half is adjacent and untouched. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | An approval is valid under the rules it was given, and states which those were. | S1 business_invariants #1 | invariant |
| 2 | A rule-set version exists only where admissibility could have changed. | S1 business_invariants #2 | invariant |
| 3 | Every correction declares its effectivity. | S1 business_invariants #3 | invariant |
| 4 | A migrated dossier is never presented as an approved one. | S1 business_invariants #4 | invariant |
| 5 | A closed dossier is never amended to satisfy rules written after its approval. | S1 constraints #1 | governance rule |
| 6 | A non-retroactive correction disturbs no dossier and creates no version. | S1 constraints #2 | governance rule |
| 7 | Naming the dossiers a retroactive change affects is part of that change. | S1 constraints #3 | governance rule |
| 8 | A completed change may be left at the version it was approved under. | S1 known_facts #11 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Declaring, on a correction, whether it is retroactive | design | NEW |
| GAP-2 | S3 authoring_decisions #2 | Naming a state of the rule set | design | NEW |
| GAP-3 | S3 authoring_decisions #3 | Pinning, on an approval, the version it was given under | design | NEW |
| GAP-4 | S3 authoring_decisions #4 | Naming the dossiers a retroactive correction affects | design | NEW |
| GAP-5 | S3 authoring_decisions #5 | Carrying a dossier's state on the dossier | design | NEW |
| GAP-6 | S3 authoring_decisions #6 | Stating, in a verdict, the version it was rendered against | design | EXTEND |
| GAP-7 | S3 authoring_decisions #7 | Reporting a deliberate refusal as deliberate | design | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The five gaps are delivered as one chain, in order. | S3 analysis_findings Q1 | Each depends on the one before it; correcting the first in isolation leaves the rest unreachable. | Rules out partial delivery, and fixes the order of the work. |
| 2 | A version names a state of the rule set, not a count and not a date. | S3 analysis_findings Q2 | A count says how many rules exist and a date says when; neither says whether a prior document may still pass. | Rules out reusing the rule count or a timestamp as the pin. |
| 3 | The correction declares its effectivity; the rule set records it. | S3 analysis_findings Q3 | Only the correction knows what it added and why; a claim held only by its author is what exists today. | Rules out inferring effectivity from what a correction touched. |
| 4 | The affected dossiers are named by the correction that affects them. | S3 analysis_findings Q4 | Discovered later, they are discovered by failing — which is how they were discovered this session. | Rules out finding them by re-running everything, which is the current behaviour. |
| 5 | A dossier's state is carried by the dossier. | S3 analysis_findings Q5 | Held elsewhere it is a second statement about a document that the document itself contradicts. | Rules out a central register of dossier states. |
| 6 | A deliberate refusal is reported as deliberate. | S3 analysis_findings Q6 | A correct red and a faulty red are reported identically, and the easy response to either is to make it pass. | Rules out documenting the distinction, which was done and did not prevent the migration. |
| 7 | The two corrections made this session are recorded retrospectively, one of each effectivity. | S3 impact_analysis #3 | They are the first instances the declaration must describe, and the only ones whose effect is already known. | The change is validated against the history that motivated it. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Declaring, on a correction, whether it is retroactive | GAP-1 |
| Naming a state of the rule set | GAP-2 |
| Pinning, on an approval, the version it was given under | GAP-3 |
| Naming the dossiers a retroactive correction affects | GAP-4 |
| Carrying a dossier's state on the dossier | GAP-5 |
| Stating, in a verdict, the version it was rendered against | GAP-6 |
| Reporting a deliberate refusal as deliberate | GAP-7 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Deciding whether any particular correction is retroactive | Each correction decides, when it is made. |
| Rule sets that differ per composition rather than per version | Nothing has needed it. |
| Anything about generated artifacts | A separate problem with its own change. |
| Whether a design can state an artifact it amends | A separate problem with its own change. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
