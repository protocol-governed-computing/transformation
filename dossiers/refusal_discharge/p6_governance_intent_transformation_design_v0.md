# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** refusal_discharge
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE it lives and who owns it. No new artifact codes; nothing crosses a subdomain boundary.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Stating what discharges a declared refusal | design | OWNED | | S5 scope_boundary Stating what discharges a declared refusal |
| Refusing a design that leaves a declared refusal unaccounted for | design | OWNED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | S5 scope_boundary Refusing a design that leaves a declared refusal unaccounted for |
| Stating that a refusal is deferred, and to whom | design | OWNED | | S5 scope_boundary Stating that a refusal is deferred, and to whom |
| Holding a discharge to the act and step it names | design | OWNED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | S5 scope_boundary Holding a discharge to the act and step it names |
| Holding a discharge's outcome to an ending that refuses | design | OWNED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | S5 scope_boundary Holding a discharge's outcome to an ending that refuses |
| Refusing a discharge or deferral naming a refusal the business never declared | design | OWNED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | S5 scope_boundary Refusing a discharge or deferral naming a refusal the business never declared |
| Giving the design intent phase the seed | design | OWNED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | S5 scope_boundary Giving the design intent phase the seed |
| Reading a prior's rows across several registers | design | OWNED | transformation::CT_PURE_EVALUATE_RULES_V0 | S5 scope_boundary Reading a prior's rows across several registers |
| Which operations a business refuses, and when | design | DEFERRED | | S5 scope_boundary Which operations a business refuses, and when |
| How an act performs a refusal | design | DEFERRED | | S5 scope_boundary How an act performs a refusal |
| Whether the built act refuses when it runs | design | DEFERRED | | S5 scope_boundary Whether the built act refuses when it runs |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|--------------------------|----------------|
| NONE IDENTIFIED |

---

## 4. Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Declares the rule set a design is judged against, and asks nothing about what carries a declared refusal out. Reads the business intent and governance intent documents, and not the seed. | EXTEND | S4 gap_register GAP-2 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Passes the composition's published facts to the rules that need them. This change declares no observation, so what it passes does not change; it is re-emitted because it is generated from the same declaration. | EXTEND | S4 gap_register GAP-7 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | Applies a declared rule set to a parsed design. Carries the check kinds the rules are built from; two are added and one is widened. | EXTEND | S4 gap_register GAP-8 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| THE_REFUSAL_IS_THE_BUSINESS_ALONE | The design states what discharges a refusal and never what is refused. A rule that admitted a discharge for a condition the seed does not carry would let the design author business rules. | S4 constraint_register #4 |
| THE_SEED_IS_THE_SOURCE | Where a rule needs the refusals, it reads the seed, not the change request that restates them. The restatement is already proved identical in both directions, so reading the copy would add a dependency and no assurance. | S4 design_decisions #1 |
| NO_HAND_WRITTEN_RULE_SET | The judging artifacts are re-emitted by the generator the design names. A rule written by hand beside its declaration is the drift the generator removes. | S4 constraint_register #7 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Stating what discharges a declared refusal | design | S4 gap_register GAP-1 |
| Refusing a design that leaves a declared refusal unaccounted for | design | S4 gap_register GAP-2 |
| Stating that a refusal is deferred, and to whom | design | S4 gap_register GAP-3 |
| Holding a discharge to the act and step it names | design | S4 gap_register GAP-4 |
| Holding a discharge's outcome to an ending that refuses | design | S4 gap_register GAP-5 |
| Refusing a discharge or deferral naming a refusal the business never declared | design | S4 gap_register GAP-6 |
| Giving the design intent phase the seed | design | S4 gap_register GAP-7 |
| Reading a prior's rows across several registers | design | S4 gap_register GAP-8 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
