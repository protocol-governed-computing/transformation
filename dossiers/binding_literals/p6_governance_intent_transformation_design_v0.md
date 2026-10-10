# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** binding_literals
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE: ownership, storage, dependencies, and the existing artifacts this change acts on.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `design` — EXISTING — modified by this CR |
| Authority class | reuse existing — an author proposes, a phase decides; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

The rules that judge a binding belong to the Design Intent phase, which this subdomain owns. Its
workflow carries them as a sealed copy, so correcting them replaces the workflow with a new version.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Giving a literal one meaning across every rule that judges a binding | design | OWNED | | S4 gap_register GAP-1 |
| Stating that a generator determines a value | design | OWNED | | S4 gap_register GAP-2 |
| Judging a document against declared rules | design | SATISFIED | transformation::CT_PURE_EVALUATE_RULES_V0 | S4 capability_graph #3 |
| The rule-effectivity change | design | DEFERRED | | S4 authoring_scope deferred #1 |

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
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 | Carries two rules that disagree about what a literal is, and no statement for a generated value. | REPLACE | S4 gap_register GAP-1 |
| transformation::IN_DESIGN_INTENT_SUBMITTED_V0 | Starts the workflow this change replaces. | REVIEW | S4 design_decisions #5 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | Applies whatever rules it is handed, including the new one, by a way of judging it already has. | REUSE | S4 capability_graph #3 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares what the domain compiles. Named because the authored workflow is compiled under it. | REVIEW | S4 dependency_graph #1 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| ONE_MEANING_OF_A_LITERAL | Every rule that judges a binding admits the same literals: a single word, a qualified identity, a number, or a value opening with a quote, bracket or brace. | S4 constraint_register #1 |
| GENERATED_ONLY_WHERE_NAMED | A binding whose source is generated is admitted only when its owner is listed as generated. | S4 constraint_register #2 |
| NOTHING_ADMITTED_IS_REFUSED | Every design admissible before this change is admissible after it, with every binding meaning what it meant. | S4 constraint_register #3 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Giving a literal one meaning across every rule that judges a binding | design | S4 gap_register GAP-1 |
| Stating that a generator determines a value | design | S4 gap_register GAP-2 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
