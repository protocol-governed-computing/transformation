# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** rule_expressiveness
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `design` — EXISTING — extended by this CR |
| Authority class | reuse existing — an author proposes, a phase decides; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

Everything corrected here belongs to the phases that judge a design, and every one of those phases
is already owned by this subdomain. Nothing new stands on its own, so no subdomain is declared.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Stating which subdomain a classification applies to | design | OWNED | | S4 gap_register GAP-1 |
| Deriving the span of a change from its classifications | design | OWNED | | S4 gap_register GAP-2 |
| Requiring a purpose for every subdomain a change touches | design | OWNED | | S4 gap_register GAP-3 |
| Requiring an owner for every subdomain a change touches | design | OWNED | | S4 gap_register GAP-4 |
| Recording a dependency that exists and is altered | design | OWNED | | S4 gap_register GAP-5 |
| Counting a register's rows | design | OWNED | | S4 gap_register GAP-6 |
| Applying a row count to any register | design | DEFERRED | | S4 authoring_scope deferred #2 |
| Changes that span two domains | design | DEFERRED | | S4 authoring_scope deferred #1 |
| Anything in the construction half of the lifecycle | build | DEFERRED | | S4 authoring_scope deferred #3 |

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
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Declares the classification register with three columns, none naming a subdomain. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | The same. | EXTEND | S4 gap_register GAP-1 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0 | Declares the ways a dependency may be disposed of, closed at four. | EXTEND | S4 gap_register GAP-5 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0 | Requires a purpose for the subdomain the document is about, and for no other. | EXTEND | S4 gap_register GAP-3 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0 | Requires an owner per capability, and for no subdomain as such. | EXTEND | S4 gap_register GAP-4 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares what the domain compiles. Unaffected by the corrections. | REVIEW | S4 dependency_graph #2 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_PHASE_JUDGES_ONLY_BY_WHAT_IT_DECLARES | A phase judges a document against the rule set it declares and against nothing else. A correction is made by changing what a phase declares, never by changing how a verdict is reached behind it. | S4 constraint_register #4 |
| SPAN_IS_DERIVED_NEVER_DECLARED | Nothing declares which subdomains a change touches. The span is whatever the classifications name, and no rule may read a span from anywhere else. | S4 constraint_register #3 |
| EXPRESSIBILITY_BEFORE_ENFORCEMENT | Adding a way of judging and using it are separate acts. This change adds one and applies it to no register, so no verdict moves because of it. | S4 design_decisions #6 |
| NO_UNRELATED_VERDICT_MOVES | Every dossier already judged is re-judged. A verdict that changes for any reason other than the three corrections is a regression and is treated as one. | S4 design_decisions #7 |
| DESIGN_OWNS_ONLY_THE_JUDGING | This subdomain owns the phases and the ways of judging. It owns nothing about what any particular change should do, and the construction half is untouched. | S4 constraint_register #7 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Stating which subdomain a classification applies to | design | S4 gap_register GAP-1 |
| Deriving the span of a change from its classifications | design | S4 gap_register GAP-2 |
| Requiring a purpose for every subdomain a change touches | design | S4 gap_register GAP-3 |
| Requiring an owner for every subdomain a change touches | design | S4 gap_register GAP-4 |
| Recording a dependency that exists and is altered | design | S4 gap_register GAP-5 |
| Counting a register's rows | design | S4 gap_register GAP-6 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
