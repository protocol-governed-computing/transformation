# Stage 6 — Governance Intent: transformation / design

**Stage:** 6 — Governance Intent

**CR:** semantic_change

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. What a design may say is the design subdomain's; whether it may be built is
build's. Both read the platform's declaration of how two declarations compare.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Judge a design | design | OWNED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | S5 scope_boundary Judge a design |
| Build a design | build | OWNED | | S5 subdomain_purposes build |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| How two declarations compare | build -> artifact | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | SATISFIED | S4 dependency_graph artifact::VOCAB_DECLARATION_REPRESENTATION_V1 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Present; its rules admit a withdrawal and no re-point | REPLACE | S4 design_decisions #7 |
| transformation::IN_DESIGN_INTENT_SUBMITTED_V0 | Present; starts the workflow being replaced | REVIEW | S4 design_decisions #7 |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | Present and read unchanged | REUSE | S4 dependency_graph artifact::VOCAB_DECLARATION_REPRESENTATION_V1 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| COMPARED_BY_THE_DECLARATION | Construction compares two declarations only by the rules the platform declares, and refuses to compare when the platform declares one it does not apply. | S4 design_decisions #1 |
| NO_UNCOMPARED_AMENDMENT | A design that amends, replaces or re-points is built only against the composition. | S4 design_decisions #2 |
| A_REPOINT_CHANGES_ONE_REFERENCE | A re-point rewrites only references to what the design replaces, in declared reference parts. | S4 design_decisions #4 |
| REACH_ACCOUNTED_BEFORE_BUILD | Every live referrer of a replaced artifact is replaced, amended or re-pointed by the design. | S4 design_decisions #5 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Judge a design | design | S6 ownership Judge a design |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
