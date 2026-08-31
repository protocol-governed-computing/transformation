# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `design` — EXISTING — modified by this CR |
| Authority class | reuse existing — a correction declares, a rule set records, a person approves; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

Versions, effectivity, verdicts and dossier state all belong to the phases that judge a design, which
this subdomain owns. Nothing new stands on its own, so no subdomain is declared.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Declaring, on a correction, whether it is retroactive | design | OWNED | | S4 gap_register GAP-1 |
| Naming a state of the rule set | design | OWNED | | S4 gap_register GAP-2 |
| Pinning, on an approval, the version it was given under | design | OWNED | | S4 gap_register GAP-3 |
| Naming the dossiers a retroactive correction affects | design | OWNED | | S4 gap_register GAP-4 |
| Carrying a dossier's state on the dossier | design | OWNED | | S4 gap_register GAP-5 |
| Stating, in a verdict, the version it was rendered against | design | OWNED | | S4 gap_register GAP-6 |
| Reporting a deliberate refusal as deliberate | design | OWNED | | S4 gap_register GAP-7 |
| Refusing a run against a baseline that is not the pinned one | design | OWNED | | S4 capability_graph #8 |
| Deciding whether any particular correction is retroactive | design | DEFERRED | | S4 authoring_scope deferred #1 |
| Rule sets that differ per composition | design | DEFERRED | | S4 authoring_scope deferred #2 |
| Anything about generated artifacts | design | DEFERRED | | S4 authoring_scope deferred #3 |
| Whether a design can state an artifact it amends | design | DEFERRED | | S4 authoring_scope deferred #4 |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| NONE IDENTIFIED |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Renders a verdict naming the phase and the rule count, and no version. | EXTEND | S4 gap_register GAP-6 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-6 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-6 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-6 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-6 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-6 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-6 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-6 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | The same, and gates the approval that must pin a version. | EXTEND | S4 gap_register GAP-3 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares what the domain compiles. Unaffected by these corrections. | REVIEW | S4 dependency_graph #2 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| AN_APPROVAL_IS_A_FACT_ABOUT_A_MOMENT | An approval is valid under the rules it was given and states which those were. An approval that is only a statement about today's rules was never closed; it was provisionally closed pending every future rule. | S4 constraint_register #1 |
| A_VERSION_MEANS_ADMISSIBILITY_MOVED | A rule-set version exists only where a correction can alter a prior dossier's admissibility. A version that cannot invalidate anything is a signal that says nothing. | S4 constraint_register #2 |
| EVERY_CORRECTION_DECLARES_ITS_REACH | A correction declares whether it is retroactive, and the rule set records the declaration. Two corrections touching the same files can differ entirely in effect, so the declaration cannot be inferred from what was touched. | S4 constraint_register #3 |
| MIGRATED_IS_NOT_APPROVED | A dossier amended to satisfy a later rule set is never presented as one approved under it. It passes now and was taught to, and the two are different claims. | S4 constraint_register #4 |
| A_CLOSED_DOSSIER_IS_EVIDENCE | A closed dossier is never amended to satisfy rules written after its approval. Amending it changes the evidence of an approval that already happened. | S4 constraint_register #5 |
| RETROACTIVITY_NAMES_ITS_CASUALTIES | A retroactive correction names the dossiers it affects as part of itself. Discovered later, they are discovered by failing — unannounced and all at once. | S4 constraint_register #7 |
| A_DELIBERATE_RED_SAYS_SO | A refusal that is correct is reported differently from one that is a fault. Documenting the difference was tried and did not prevent the wrong act. | S4 design_decisions #6 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Declaring, on a correction, whether it is retroactive | design | S4 gap_register GAP-1 |
| Naming a state of the rule set | design | S4 gap_register GAP-2 |
| Pinning, on an approval, the version it was given under | design | S4 gap_register GAP-3 |
| Naming the dossiers a retroactive correction affects | design | S4 gap_register GAP-4 |
| Carrying a dossier's state on the dossier | design | S4 gap_register GAP-5 |
| Stating, in a verdict, the version it was rendered against | design | S4 gap_register GAP-6 |
| Reporting a deliberate refusal as deliberate | design | S4 gap_register GAP-7 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
