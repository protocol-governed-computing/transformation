# Stage 7 — Design Intent: transformation / design
**Stage:** 7 — Design Intent
**CR:** binding_literals
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW: the binding identities and the declarations they carry. The correction changes the Design
Intent's sealed rule set, so its workflow is replaced by a new version, redeclared whole.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| What a literal is | Every rule that judges a binding reads a literal the same way. | A literal is a single word, a qualified identity, a number, or a value opening with a quote, bracket or brace. The rooting rule keeps this definition. The step-binding form rule and the molecule form rule are widened to admit exactly it, beside the references each already admits. | S4 design_decisions #1 |
| Whether the widening is retroactive | No delivered design binds a value the narrower rules refuse. | It is not. It only admits bindings that were refused, and every admitted binding keeps its meaning. | S4 design_decisions #2 |
| How a generated value is stated | A generator determines only what the design says it does. | A binding whose source is the single word generated states that the generator of its owner determines the value. A new rule, GENERATED_SOURCE_WITHOUT_GENERATOR, refuses it unless the owner is listed in generation_provenance. It is written in the existing way of judging that resolves a cell in another register, applied only to rows whose source is generated. | S4 design_decisions #3 |
| What a design meaning the word itself writes | Reserving the word changes no admitted binding. | It writes the word quoted, which the widened form rule admits as a literal. | S4 design_decisions #4 |
| What carries the correction | The Design Intent's workflow carries its rule set as a sealed copy. | The rule declaration and the template change, and the generator seals them into a new version of the workflow. The intent that starts it names the successor. | S4 design_decisions #5 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW) | Summary | Reason | Source Finding |
|------|--------------------------------------------------|---------|--------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 | REPLACE | Decide whether an offered Design Intent register is admissible | Its sealed rule set changes, so WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 supersedes it. | S6 pps_artifacts_requiring_action #1 |
| transformation::IN_DESIGN_INTENT_SUBMITTED_V0 | REPOINT | Offer a Design Intent register for admissibility judgement | Starts the workflow this change replaces; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #2 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | REUSE |  | Applies the corrected rules by ways of judging it already has. | S6 pps_artifacts_requiring_action #3 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | REUSE |  | The contract the workflow runs. Unchanged. | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | REUSE |  | Binds read-only observation for the workflow. Unchanged. | transformation::RB_TRANSFORMATION_BINDINGS_V0 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | REVIEW |  | Declares what the domain compiles. Unchanged; named because the authored workflow is compiled under it. | S6 pps_artifacts_requiring_action #4 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|---------------------------------------------------------------|------|---------|-----------------|--------|----------------|
| Deciding whether a design intent is admissible, reading a literal one way and admitting a value its generator determines | WF | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | Decide whether an offered Design Intent register is admissible | design | NEW | S6 governance_outcome #1 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #1 |

---

## 5. Execution Topology

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::IN_DESIGN_INTENT_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #1 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #1 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #1 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #1 |

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
|-------|------|---------------------------|-------|----------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #1 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #1 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | INPUT | rule_set | generated | S7 design_resolution #3 |

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
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|
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
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | supersedes | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 | S7 existing_inventory WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| REPLACE | design | 1 | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 |
| EXTEND | design | 0 |  |
| NEW | design | 1 | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation.design.emit:emit_rule_sets | templates/p7_design_intent_template_v0.md, transformation/design/p7_design_intent/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V1.md | S7 design_resolution #5 |

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| NONE IDENTIFIED |

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| NONE IDENTIFIED |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|
| Declaring a value generated | The design does not list the artifact that holds it as generated | The rule GENERATED_SOURCE_WITHOUT_GENERATOR, which this change adds to the Design Intent's rule set | This change is delivered and the rule is sealed in the composition | S0 operation_refusals #1 |

---

## 20. Refusal — Governance-Surface Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|
| NONE IDENTIFIED |

---

## 21. Molecule Steps

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---------|------|-----------------------------|--------|------|----------|-------|----------------|
| NONE IDENTIFIED |

---

## 22. Molecule Step Bindings

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---------|------|-----------------------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 23. Test Cases

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---------|------|---------------------------------------|----------------|
| NONE IDENTIFIED |

---

## 24. Test Case Values

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---------|------|------------------------------------------|-------|-------|----------------|
| NONE IDENTIFIED |

---

## 25. Withdrawn Facts

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|----------|------|--------|----------------|

---

## Gate 1 — Design Approval

**Gate 1 closes here.** The full dossier (Stages 0–7) is presented for review as a body.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 6 — Governance Intent | Ownership, artifacts requiring action, boundary rules | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
