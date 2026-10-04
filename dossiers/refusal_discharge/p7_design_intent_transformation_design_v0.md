# Stage 7 — Design Intent: transformation / design
**Stage:** 7 — Design Intent
**CR:** refusal_discharge
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW. Binding FQDNs are assigned here; business facts and placement decisions are not repeated.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The refusals are read from the seed rather than carried forward. | The rules that judge a design must read the refusals the business declared. | The design intent phase declares `p0` among its priors, alongside `p5` and `p6`. Business intent and governance intent already declare it, so the mechanism exists and this change uses it rather than adding one. The alternative was three registers and three carry rules across the intermediate phases, restating what the seed says and able to drift from it. | S4 design_decisions #1 |
| A discharge is stated in one register and a deferral in another. | A discharge names an act, a step and an outcome; a deferral names an owner and a condition. | Two registers of the design language, `refusal_discharge` and `refusal_deferrals`, declared in `templates/p7_design_intent_template_v0.md` and governed by rules in `transformation/design/p7_design_intent/rules.py`. One table holding both would leave several cells empty on every row, and a blank meaning *not applicable* is indistinguishable from one meaning *unanswered*. | S4 design_decisions #2 |
| Coverage is asked of both registers at once. | Every refusal the business declared is accounted for, as discharged or as deferred. | One rule, reading the seed's refusals against both registers. The kind that checks a prior's rows arrived reads a single register; it gains an optional list of registers defaulting to the one it reads today, exactly as the kind that resolves a cell against another register already does. Every existing rule using it is unchanged. | S4 design_decisions #6 |
| A discharge is held to the design's own topology. | A register read only for presence documents intent and enforces nothing. | Two rules and two check kinds. The first resolves the act and step against `execution_topology` and requires the outcome to be one that step reports. The second reads the node that outcome routes to and requires it to be an ending that refuses. Both read the design alone; no composition fact is observed. | S4 design_decisions #5 |
| A refusing ending is one typed as a plain exit. | An outcome that routes onward does not refuse, however plainly the register says it does. | The topology types every node, and the corpus types a completing ending as a success exit and every refusing one as a plain exit. The rule reads that type; it does not read the node's name, which would be a convention anybody could break by naming an exit well. | S4 design_decisions #3 |
| A deferral is held to the seed and to naming an owner. | A deferral names its owner, and no deferral names a refusal the business did not declare. | The register's rows are confined to the seed's refusals by the same kind that confines the discharge register, and the owner column is required. Neither the authoring scope nor the seed's authority deferrals is keyed to a refusal, so there is nothing else to resolve into. | S4 design_decisions #4 |
| Each new rule is proved by a probe built to fail it. | No document in the corpus states a discharge, so every new rule would report clean while checking nothing. | Five probes, one per rule, in the phase testbed alongside the existing inadmissible fixtures. A rule whose probe passes has been shown to fire; a rule that only reports clean has been shown nothing. | S4 design_decisions #7 |
| The change is delivered through the pipeline, naming the generator of the documents it amends. | The judging artifacts are re-emitted by their generator, never written by hand. | The three amended artifacts are declared in §16 with their generator and its sources. Construction invokes the generator and writes none of them. | S4 constraint_register #7 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | EXTEND | Phase 7 of the change pipeline: decide whether an offered Design Intent register is admissible | Carries the rule set that judges a design. Gains two registers, five rules, and the seed among its declared priors. | S6 pps_artifacts_requiring_action #1 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | EXTEND | Parse a phase document and its priors, observe the composition, and judge them together | Generated from every phase's rule module read together, so it is re-emitted when any of them changes. This change declares no observation, so what it passes is unchanged. | S6 pps_artifacts_requiring_action #2 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | EXTEND | Apply a declared rule set to a parsed design and report every rule that failed | Carries the check kinds the rules are built from. Gains two kinds, and one existing kind gains an optional parameter. | S6 pps_artifacts_requiring_action #3 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | REVIEW | | Declares the register the business states its refusals in. Unchanged: what the business may say is not what this change touches. | S4 constraint_register #4 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | REVIEW | | Holds the change request's restatement to the seed in both directions. Unchanged, and the reason a rule may read the seed instead of the restatement. | S4 design_decisions #1 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | REVIEW | | Declares what the domain compiles. Unchanged; named because the amended artifacts are compiled under it. | S6 pps_artifacts_requiring_action #1 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| NONE IDENTIFIED |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| NONE IDENTIFIED |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| NONE IDENTIFIED |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|
| NONE IDENTIFIED |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|
| NONE IDENTIFIED |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| NONE IDENTIFIED |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| NONE IDENTIFIED |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|-----------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | design | 3 | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0, transformation::CT_PURE_EVALUATE_RULES_V0 |
| NEW | design | 0 | |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p7_design_intent_template_v0.md, transformation/design/p7_design_intent/rules.py | S4 constraint_register #7 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | transformation.design.emit:emit_rule_sets | transformation/design/meta.py, transformation/design/p0_change_seed/rules.py, transformation/design/p1_change_request/rules.py, transformation/design/p2_domain_model/rules.py, transformation/design/p3_analysis_loop/rules.py, transformation/design/p4_business_model/rules.py, transformation/design/p5_business_intent/rules.py, transformation/design/p6_governance_intent/rules.py, transformation/design/p7_design_intent/rules.py, transformation/design/p8_authoring_mandate/rules.py | S4 constraint_register #7 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | transformation.design.emit:emit_rule_sets | transformation/design/checks.py | S4 constraint_register #7 |

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| NONE IDENTIFIED |

---

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`6e1e571dbbb8…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the amendment of the three artifacts §2 marks EXTEND, each
re-emitted by the generator §16 declares, and nothing else. No register of this design names an
artifact to author, and §15 states that plainly: three EXTEND, zero NEW.

**This is the last design that will not have to account for its own refusals.** The seed of this
change declares four, and under the rule set in the pinned composition nothing asks what carries any
of them out — which is the defect, stated by the dossier that removes it. Each of the four is
discharged by a rule this change authors, and where they are stated is §1, because the register that
would hold them does not exist until this change delivers it.

**What this approval does not have that the last one had.** cr_03 was gated after Construction
Completeness read 100%, and that figure is the evidence a design uniquely determines its artifacts.
There is no such figure here: nothing in this change is rendered from a design register, so
Construction Completeness has nothing to read. The equivalent evidence arrives later and from
elsewhere — `emit_rule_sets --check` agreeing after the rules are written, and five probes each
built to fail. Approving this design is approving that substitution.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | Ownership, dependencies, artifacts requiring action | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
