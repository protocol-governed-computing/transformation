# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE: ownership, storage, dependencies, and the existing artifacts this change acts on.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `design` — EXISTING — modified by this CR |
| Authority class | reuse existing — an author proposes, a phase decides, a gate reviewer approves and re-confirms; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

The reading, the judging, the phase rule sets and the templates already belong to the subdomain
that judges a design. Construction receives registers through the shared reading and is not
changed, so no subdomain is declared.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Carrying registers as structured data apart from the prose | design | OWNED | | S4 gap_register GAP-1 |
| A rule-set identity that changes only when the rules change | design | OWNED | | S4 gap_register GAP-2 |
| Naming the rule set in a document | design | OWNED | | S4 gap_register GAP-3 |
| Naming the rule set in a verdict | design | OWNED | | S4 gap_register GAP-4 |
| Naming an approval's rule set, and confirming it again | design | OWNED | | S4 gap_register GAP-5 |
| Recording that a document was migrated | design | OWNED | | S4 gap_register GAP-6 |
| Declaring a correction's effectivity | design | OWNED | | S4 gap_register GAP-7 |
| Proving identical verdicts across the two forms | design | OWNED | | S4 gap_register GAP-8 |
| A person closing a gate and re-confirming an approval | design | SATISFIED | transformation::AC_GATE_REVIEWER_V0 | S4 actors #2 |
| How a value inside a register is structured | design | DEFERRED | | S4 authoring_scope deferred #1 |
| Where the rules are declared, and in what language | design | DEFERRED | | S4 authoring_scope deferred #2 |
| Governing and specifying construction on its own | build | DEFERRED | | S4 authoring_scope deferred #3 |
| Rule sets that differ per composition rather than per version | design | DEFERRED | | S4 authoring_scope deferred #4 |

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
| transformation::CT_PURE_PARSE_REGISTERS_V0 | Reads registers as tables inside the prose, through conventions only the code states. | REPLACE | S4 gap_register GAP-1 |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | Reads prior documents in the old form. | REPLACE | S4 gap_register GAP-1 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | Returns a verdict that names no rule set. | REPLACE | S4 gap_register GAP-4 |
| transformation::CC_JUDGE_DOCUMENT_V0 | Judges the seed and the change request; its verdict names no rule set. | REPLACE | S4 gap_register GAP-4 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | Judges the six later phases; its verdict names no rule set. | REPLACE | S4 gap_register GAP-4 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | Judges the analysis loop; its verdict names no rule set. | REPLACE | S4 gap_register GAP-4 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Carries a rule set with no identity, judging the old form. | REPLACE | S4 gap_register GAP-2 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | The same. | REPLACE | S4 gap_register GAP-2 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V1 | The same. | REPLACE | S4 gap_register GAP-2 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V1 | The same. | REPLACE | S4 gap_register GAP-2 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V1 | The same. | REPLACE | S4 gap_register GAP-2 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V1 | The same. | REPLACE | S4 gap_register GAP-2 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V1 | The same. | REPLACE | S4 gap_register GAP-2 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | The same. | REPLACE | S4 gap_register GAP-2 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V1 | The same. | REPLACE | S4 gap_register GAP-2 |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Receives registers from the shared reading and splits values inside cells itself. Unchanged here. | REVIEW | S4 dependency_graph #2 |
| transformation::AC_GATE_REVIEWER_V0 | The person who closes a gate. Also the one who re-confirms an approval. | REUSE | S4 actors #2 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares what the domain compiles. Named because the extended artifacts are compiled under it. | REVIEW | S4 dependency_graph #1 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| VERDICT_NAMES_ITS_RULE_SET | Every verdict carries the identity of the rule set that rendered it. A verdict without one is not a verdict. | S4 constraint_register #1 |
| APPROVAL_NAMES_ITS_RULE_SET | An approval carries the identity of the rule set it was given under, and keeps it. | S4 constraint_register #2 |
| FORM_NEVER_MOVES_A_VERDICT | Every test document receives the same findings in both forms before the old reading retires. A difference is a regression. | S4 constraint_register #3 |
| IDENTITY_FOLLOWS_THE_RULES | A rule-set identity changes when, and only when, a change can alter a prior document's admissibility. A workflow version is not a rule-set identity. | S4 constraint_register #4 |
| ONLY_A_PERSON_RECONFIRMS | Under a later rule set an approval stands unconfirmed. Only a person at the gate re-confirms it; no judging does. | S4 constraint_register #5 |
| ONE_FORM_AT_A_TIME | The new form replaces the old one. No reading of the old form survives the change. | S4 constraint_register #6 |
| CORRECTION_DECLARES_ITS_EFFECTIVITY | A correction states whether it is retroactive, and the rule set records the statement as governed history. | S4 constraint_register #12 |
| DESIGN_OWNS_ONLY_THE_JUDGING | This change acts on the reading, the judging and the phase rule sets. Construction is reviewed, not changed. | S4 design_decisions #2 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Carrying registers as structured data apart from the prose | design | S4 gap_register GAP-1 |
| A rule-set identity that changes only when the rules change | design | S4 gap_register GAP-2 |
| Naming the rule set in a document | design | S4 gap_register GAP-3 |
| Naming the rule set in a verdict | design | S4 gap_register GAP-4 |
| Naming an approval's rule set, and confirming it again | design | S4 gap_register GAP-5 |
| Recording that a document was migrated | design | S4 gap_register GAP-6 |
| Declaring a correction's effectivity | design | S4 gap_register GAP-7 |
| Proving identical verdicts across the two forms | design | S4 gap_register GAP-8 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
