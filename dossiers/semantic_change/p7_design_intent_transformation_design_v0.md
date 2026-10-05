# Stage 7 — Design Intent: transformation / design

**Stage:** 7 — Design Intent
**CR:** semantic_change
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Read against the pinned baseline
`2c5eac6de01d8a3717ded2726e318c7e4523dc42c39980153e2a216435126e49`.

The rules that judge a design change, so the workflow carrying them is replaced by its next version.
The new version admits a re-point and no withdrawal. No phase workflow is determined by a design, so
the new version is named here and not scheduled: its rules, routing and provenance are generated, and
its places, inputs and binding are carried by hand from the version it replaces. The old version is
stood down by hand, and the intent that starts the design phase is re-pointed by hand. Everything else this change does is construction's and
inspection's, and is armed by the refusals deferred below.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Amendments are compared by the declaration | A change of meaning is a new identity | Construction compares each EXTEND row's artifact, rendered or generated, with the composition by artifact::VOCAB_DECLARATION_REPRESENTATION_V1, and refuses any difference the declaration does not excuse | S4 design_decisions #1 |
| No uncompared amendment | No amendment is built uncompared | Construction refuses a design with an EXTEND, REPLACE or REPOINT row when no composition is given | S4 design_decisions #2 |
| No withdrawal | A withdrawal is a change of meaning | The design phase's template and rules drop the withdrawal register | S4 design_decisions #3 |
| A re-point | A referrer follows a replacement without restatement | The design phase admits REPOINT as an inventory action; construction rewrites only references to what the design replaces | S4 design_decisions #4 |
| Reach is accounted for | Every live referrer is replaced, amended or re-pointed | Construction asks si.artifact.refs for each REPLACE row's referrers, and inspection answers from the record of references | S4 design_decisions #5; S4 design_decisions #6 |
| A new version of the design workflow | This change follows the rule it builds | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 supersedes transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0. No phase workflow is determined by a design, so it is named here and not scheduled: its places, inputs and binding are carried by hand from transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, and the generator, mapped to it for the design phase, writes its rules, routing and provenance. transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 is marked stood down by hand, and transformation::IN_DESIGN_INTENT_SUBMITTED_V0 re-pointed by hand | S4 design_decisions #7 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | REVIEW |  | Its rules admit a withdrawal and no re-point. Stood down by hand, superseded by transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1: no phase workflow is determined by a design, so neither its successor nor its supersession can be scheduled for construction. | S6 pps_artifacts_requiring_action #1 |
| transformation::IN_DESIGN_INTENT_SUBMITTED_V0 | REVIEW |  | Re-pointed by hand to start the new version: a design can re-point only once this change's rules are sealed. Only its workflow changes. | S6 pps_artifacts_requiring_action #2 |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | REUSE |  | Read by construction, unchanged. | S6 pps_artifacts_requiring_action #3 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Execution Topology

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|

---

## 9. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|

---

## 10. Structure Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|------|------|------|----------------|

---

## 11. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| NEW | design | 0 | |

---

## 12. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 13. Unchanged Registers

No act, transform, policy or entrance is touched. The generator's map of phases to workflows names the new version, and the new workflow's rules, routing and provenance are its output; it is named in the design resolution, not here, because it is not scheduled.

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|---|---|---|---|---|---|---|

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---|---|---|---|---|

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|---|---|---|---|

---

## 14. Refusal Discharge

The business declared four refusals, all made when a design is built. Construction is not a phase, so no phase rule governs them; each is deferred to the construction check this change arms.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|
| Building a design | An amendment changes what an artifact means | `tc construction check` and `emit`, comparing each amendment with the composition by artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | Armed by this change. | S0 operation_refusals #1 |
| Building a design | An amendment cannot be compared with the composition | `tc construction check` and `emit`, refusing a design that amends, replaces or re-points without `--snapshot` | Armed by this change. | S0 operation_refusals #2 |
| Building a design | A design withdraws a fact from an artifact it amends | The design phase's rules, in the workflow this change adds, which no longer admit the withdrawal register | Armed when the new workflow is sealed. | S0 operation_refusals #3 |
| Building a design | A reference to an artifact it replaces is left unaccounted for | `tc construction check` and `emit`, reading each replaced artifact's referrers from si.artifact.refs | Armed by this change. | S0 operation_refusals #4 |

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|---|---|---|---|---|

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn.

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---|---|---|---|---|---|

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---|---|---|---|

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---|---|---|---|---|---|

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|---|---|---|---|

