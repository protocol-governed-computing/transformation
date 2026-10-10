# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** version_retirement
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE: ownership, storage, dependencies, and the existing artifacts this change acts on.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `design` — EXISTING — modified by this CR |
| Authority class | reuse existing — a person decides a deletion; the checks refuse what is not recorded |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

The deleted versions belong to the subdomain that judges a design. The retention declaration, the
ledger and the checks are workspace process, which every domain reads. This change authors no
artifact and re-points none: every live artifact that names a deleted version is its successor, or
names it only as a node's place.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Declaring when a replaced version is retained | design | OWNED |  | S4 gap_register GAP-1 |
| Recording a deletion | design | OWNED |  | S4 gap_register GAP-2 |
| Accepting a recorded deletion in every check that assumed retention | design | OWNED |  | S4 gap_register GAP-3 |
| Refusing a deleted name used again | design | OWNED |  | S4 gap_register GAP-4 |
| Deleting this domain's stood-down versions | design | OWNED |  | S4 gap_register GAP-5 |
| What retention conditions apply after development | design | DEFERRED |  | S4 authoring_scope deferred #1 |
| Declaring the first stable baseline | design | DEFERRED |  | S4 authoring_scope deferred #2 |
| Deleting other domains' stood-down versions | design | DEFERRED |  | S4 authoring_scope deferred #3 |
| The form a phase document carries its facts in | design | DEFERRED |  | S4 authoring_scope deferred #4 |

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
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V0 | Stood down; nothing reads it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 | Stood down; nothing runs it; never released. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | Stood down; nothing runs it. Deleted at delivery, with its record. | REVIEW | S4 gap_register GAP-5 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| DELETION_IS_RECORDED | A replaced version leaves the live tree only with a ledger entry naming the identity, the deciding person, the determination that no retention condition held, and the change that deleted it. | S4 constraint_register #1 |
| RETIRED_NAME_NEVER_REUSED | An identity the ledger records never appears in the live tree again. | S4 constraint_register #2 |
| NOTHING_LIVE_NAMES_THE_DELETED | A live artifact never names a deleted identity, except a successor naming its predecessor. A node's name is a place, not a reference. | S4 design_decisions #5 |
| RETENTION_DECLARED_ONCE | Every check reads when retention applies from the one declaration, and no check decides it in code. | S4 constraint_register #4 |
| RELEASES_UNTOUCHED | A sealed release keeps every identity it holds, at its tag. No deletion touches it. | S4 constraint_register #7 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| NONE IDENTIFIED |

---

## Gate 1 — Design Approval, where a change ends here

This change schedules no artifact, so the dossier is terminal at this stage. Its capabilities are
realized in the workspace process and by recorded deletions, not by authored or constructed
artifacts. The full dossier (Stages 0–6) is presented for review as a body. Approval authorizes the
retention declaration, the ledger, the two checks that read it, and the eleven deletions it argues
for. Gate 2 has no mandate to lock and does not apply.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
