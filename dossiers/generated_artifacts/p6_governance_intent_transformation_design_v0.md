# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** generated_artifacts
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `design` — EXISTING — modified by this CR |
| Authority class | reuse existing — an author proposes, a phase decides, a build refuses; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

Everything corrected here belongs to the phases that judge a design and to how construction reaches
an artifact. Both are owned by this subdomain, so nothing new stands on its own and no subdomain is
declared.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Stating, on an artifact, that it is generated and by what | design | OWNED | | S4 gap_register GAP-1 |
| Naming, in a design, the generator an artifact is reached by | design | OWNED | | S4 gap_register GAP-2 |
| Reaching a generated artifact by invoking its generator | design | OWNED | | S4 gap_register GAP-3 |
| Refusing a build when an artifact and its generator disagree | design | OWNED | | S4 gap_register GAP-4 |
| Delivering this change by hand, once, and recording it | design | OWNED | | S4 gap_register GAP-5 |
| Reporting whether an artifact agrees with its generator | design | OWNED | | S4 capability_graph #6 |
| Generated artifacts outside this lifecycle | design | DEFERRED | | S4 authoring_scope deferred #1 |
| Whether a design can state an artifact it amends | design | DEFERRED | | S4 authoring_scope deferred #2 |
| How a document authored under one rule set is judged under a later one | design | DEFERRED | | S4 authoring_scope deferred #3 |

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
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Declares what a design must state about an artifact. Nothing about how the artifact is reached. | EXTEND | S4 gap_register GAP-2 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Carries a sealed rule set produced from elsewhere, and says nothing about where. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | The same, and schedules artifacts without knowing any are generated. | EXTEND | S4 gap_register GAP-1 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares what the domain compiles. Unaffected by these corrections. | REVIEW | S4 dependency_graph #2 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| GENERATOR_IS_AUTHORITATIVE | Where an artifact is produced from something else, that something else is authoritative over it. The artifact is sealed output and is never corrected directly. A disagreement is not a difference of opinion; it is proof the copy is stale. | S4 constraint_register #1 |
| ONE_ARTIFACT_ONE_PRODUCER | An artifact has exactly one producer. Construction reaches a generated artifact by invoking its generator and never by writing it, because two producers of one truth drift and the drift is silent until something reads the stale one. | S4 constraint_register #6 |
| PROVENANCE_BELONGS_TO_THE_ARTIFACT | Whether an artifact is generated, and by what, is stated by that artifact. It is not held in a list beside it, because a second statement of one truth can disagree with the thing it describes. | S4 design_decisions #1 |
| AGREEMENT_IS_ENFORCED_NOT_OBSERVED | The build refuses when an artifact and its generator disagree. A check that exists and is required by nothing is a habit, and a written obligation nobody must meet is indistinguishable from none. | S4 constraint_register #2 |
| A_GENERATOR_IS_ITS_SOURCES_TOGETHER | A template and the declaration it is read with are one generator. Naming either alone would permit regenerating from a stale pairing. | S4 constraint_register #8 |
| THE_LAST_EXCEPTION | This change is delivered outside the path it creates, once, and recorded. No later change to this subdomain may claim the same exemption, because the path will exist. | S4 design_decisions #6 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Stating, on an artifact, that it is generated and by what | design | S4 gap_register GAP-1 |
| Naming, in a design, the generator an artifact is reached by | design | S4 gap_register GAP-2 |
| Reaching a generated artifact by invoking its generator | design | S4 gap_register GAP-3 |
| Refusing a build when an artifact and its generator disagree | design | S4 gap_register GAP-4 |
| Delivering this change by hand, once, and recording it | design | S4 gap_register GAP-5 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
