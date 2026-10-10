# Stage 6 — Governance Intent: transformation / build
**Stage:** 6 — Governance Intent
**CR:** quoted_literals
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE: ownership, storage, dependencies, and the existing artifacts this change acts on.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `build` — EXISTING — modified by this CR |
| Authority class | reuse existing — construction renders, a design declares; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

Rendering an artifact from a design belongs to the subdomain that constructs it. The render
transform's declaration states nothing about how a literal is rendered, so its implementation is
corrected and no artifact changes.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Rendering a quoted literal as the value inside its quotes | build | OWNED | | S4 gap_register GAP-1 |
| Rendering a decimal number as a number | build | OWNED | | S4 gap_register GAP-2 |
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
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | Its implementation renders a quoted literal with its quotes and a decimal number as text. Its declaration states nothing about either. | REVIEW | S4 design_decisions #3 |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Runs the rendering. Unchanged. | REUSE | S4 dependency_graph #1 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| RENDER_THE_STATED_VALUE | A literal a design states renders as that value: a quoted literal as the text between its quotes, a number as a number. | S4 constraint_register #1 |
| NOTHING_DELIVERED_MOVES | Every artifact construction reproduces today, it reproduces unchanged. | S4 constraint_register #3 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Rendering a quoted literal as the value inside its quotes | build | S4 gap_register GAP-1 |
| Rendering a decimal number as a number | build | S4 gap_register GAP-2 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
