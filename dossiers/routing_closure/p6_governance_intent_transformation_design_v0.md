# Stage 6 — Governance Intent: transformation / design

**Stage:** 6 — Governance Intent

**CR:** routing_closure

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. Nothing moves and nothing is added: every artifact that changes, and the
generator, already belongs to design.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Answer every way an observation can answer | design | OWNED |  | S5 scope_boundary Answer every way an observation can answer |
| Reject a judgement whose observation found nothing | design | OWNED |  | S5 scope_boundary Reject a judgement whose observation found nothing |
| Generate the answers and the routing | design | OWNED |  | S5 scope_boundary Generate the answers and the routing |
| Reading the capability's outcomes from its declaration | platform, in a later change | DEFERRED |  | S5 scope_boundary Reading the capability's outcomes from its declaration |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED | | | |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Observing the composition | design -> platform | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_SNAPSHOT_QUERY_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Present; six observing steps do not answer nothing found | EXTEND | S4 dependency_graph transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 | Present; two observing steps do not answer nothing found | EXTEND | S4 dependency_graph transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Present; routing generated, unchanged; provenance names its judging contract | EXTEND | S4 design_decisions #3 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | Present; routing generated, unchanged; provenance names its judging contract | EXTEND | S4 design_decisions #3 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0 | Present; does not route nothing found | EXTEND | S4 design_decisions #3 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0 | Present; does not route nothing found | EXTEND | S4 design_decisions #3 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0 | Present; does not route nothing found | EXTEND | S4 design_decisions #3 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0 | Present; does not route nothing found | EXTEND | S4 design_decisions #3 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0 | Present; does not route nothing found | EXTEND | S4 design_decisions #3 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Present; does not route nothing found | EXTEND | S4 design_decisions #3 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | Present; does not route nothing found | EXTEND | S4 design_decisions #3 |
| transformation::CC_JUDGE_DOCUMENT_V0 | Present; observes nothing, reused unchanged | REUSE | S4 dependency_graph transformation::CC_JUDGE_DOCUMENT_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| AN_OBSERVATION_IS_ANSWERED_IN_FULL | Each observing step answers every outcome its capability declares, and ends its contract on any but success. | S4 design_decisions #1 |
| A_CONTRACT_DECLARES_HOW_IT_ENDS | A judging contract declares every outcome its steps can end it with. | S4 design_decisions #2 |
| A_PHASE_JUDGES_OR_REJECTS | A phase routes every outcome its judging contract declares; success is judged and every other outcome is rejected. | S4 design_decisions #3 |
| WHAT_IS_DERIVED_IS_GENERATED | The answers, the declared outcomes and the routing are written by the generator, never beside it. | S4 design_decisions #4 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Answer every way an observation can answer | design | S6 ownership Answer every way an observation can answer |
| Reject a judgement whose observation found nothing | design | S6 ownership Reject a judgement whose observation found nothing |
| Generate the answers and the routing | design | S6 ownership Generate the answers and the routing |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
