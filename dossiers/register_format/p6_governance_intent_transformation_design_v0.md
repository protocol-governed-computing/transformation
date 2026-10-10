# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** register_format
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

The reading and the templates belong to the subdomain that judges a design. Construction binds the
shared reading and is re-pointed, keeping its identity, so no subdomain is declared.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Carrying registers as structured data apart from the prose | design | OWNED |  | S4 gap_register GAP-1 |
| A block for structured facts in every document that carries registers | design | OWNED |  | S4 gap_register GAP-2 |
| Converting a document from the old form to the new | design | OWNED |  | S4 gap_register GAP-3 |
| Keeping the construction tests' coverage | design | OWNED |  | S4 gap_register GAP-4 |
| Judging a document against declared rules | design | SATISFIED | transformation::CT_PURE_EVALUATE_RULES_V0 | S4 capability_graph #5 |
| How a value inside a register is structured | design | DEFERRED |  | S4 authoring_scope deferred #1 |
| Where the rules are declared, and in what language | design | DEFERRED |  | S4 authoring_scope deferred #2 |
| Which rule set judged a document | design | DEFERRED |  | S4 authoring_scope deferred #3 |
| Governing and specifying construction on its own | build | DEFERRED |  | S4 authoring_scope deferred #4 |
| Converting or reading dossiers approved under v5 | design | DEFERRED |  | S4 authoring_scope deferred #5 |

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
|------|----------------|-----------------------------------------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V0 | Reads registers as tables inside the prose, through conventions only the code states. | REPLACE | S4 gap_register GAP-1 |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | Reads prior documents in the old form. | REPLACE | S4 gap_register GAP-1 |
| transformation::CC_JUDGE_DOCUMENT_V0 | Binds the readers this change replaces. | REVIEW | S4 design_decisions #3 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | Binds the readers this change replaces. | REVIEW | S4 design_decisions #3 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | Binds the readers this change replaces. | REVIEW | S4 design_decisions #3 |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Binds the register reader this change replaces. | REVIEW | S4 dependency_graph #1 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | Judges the same shape from either reader. Unchanged. | REUSE | S4 capability_graph #5 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares what the domain compiles. Named because the authored readers are compiled under it. | REVIEW | S4 dependency_graph #1 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| FORM_NEVER_MOVES_A_FINDING | Every test document and test copy receives the same verdict and the same findings in both forms before the old reading retires. A difference is a regression. | S4 constraint_register #1 |
| ONE_FORM_AT_A_TIME | The new form replaces the old one. No reading of the old form survives the change. | S4 constraint_register #2 |
| REPLACED_IS_DELETED | What this change replaces is deleted at delivery by a recorded human act, naming the deleted identity, who decided, and that no retention condition held. It is not stood down. | S4 constraint_register #9 |
| DELIVERED_DOSSIERS_UNTOUCHED | A delivered dossier is never edited. The construction tests read its converted test copy. | S4 constraint_register #5 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Carrying registers as structured data apart from the prose | design | S4 gap_register GAP-1 |
| A block for structured facts in every document that carries registers | design | S4 gap_register GAP-2 |
| Converting a document from the old form to the new | design | S4 gap_register GAP-3 |
| Keeping the construction tests' coverage | design | S4 gap_register GAP-4 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
