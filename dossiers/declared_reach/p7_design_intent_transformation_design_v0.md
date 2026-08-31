# Stage 7 — Design Intent: transformation / design
**Stage:** 7 — Design Intent
**CR:** declared_reach
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW. Binding FQDNs are assigned here; business facts and placement decisions are not repeated.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The reach is stated in a register of its own. | Ownership and reach are structurally distinct, never one register with a column telling them apart. | A register of the design language, declared in `templates/p7_design_intent_template_v0.md` and governed by rules in `transformation/design/p7_design_intent/rules.py`. Those two files are the generator sources of the artifact this change amends, so the register and the rules that hold it are one amendment. | S4 design_decisions #1 |
| A design names a binding; its records are derived. | A design names a binding and never the records behind it. | The register carries the binding's identity and nothing else. Which records it covers is read from `si.store.list` at judging time, so the design states one fact and the composition answers the other. That surface counts a store's bindings today without naming them, so it is amended to publish the identities it already holds — a projection of what it computes, not a new derivation, and `si.store.show` is untouched. | S4 design_decisions #2; S4 gap_register GAP-7 |
| The two refusals are delivered together. | Every declared reach is used, and every read is declared. | Two rules in one amendment of `transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0`. Neither is emitted without the other, because the generator emits the phase's whole rule set at once. | S4 design_decisions #3 |
| The store surface is declared among what the design phase observes. | A rule that is not passed the facts it reasons from reports nothing and is indistinguishable from a rule that checked. | One declaration, in the phase's own rule module, and everything else follows from it. `transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0` already generates the map that keys an observation to the step producing it, and fails the build where a phase declares an observation no step produces. The step itself is the last hand-kept copy of that same declaration, so the emission produces it too, and the contract becomes generated in the half this change touches. Construction writes neither artifact. | S4 design_decisions #4 |
| What a design states is what the built act carries. | A reach is never added to a built artifact by hand. | Construction renders the declared reach into the runtime binding of the act that declared it, from the register alone. | S4 design_decisions #5 |
| The change is delivered through the pipeline, naming the generator of the document it amends. | The document that judges a design is produced by a generator rather than written. | `transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0` is declared in §16 with its generator and both sources. Construction invokes the generator and writes none of it. | S4 design_decisions #6 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | EXTEND | Phase 7 of the change pipeline: decide whether an offered Design Intent register is admissible | Carries the rule set that judges a design. Gains the register that states a reach and the two rules that hold it. | S6 pps_artifacts_requiring_action #1 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | EXTEND | Parse a phase document and its priors, observe the composition, and judge them together | Gains the step that observes the store surface, without which every new rule reports nothing. | S4 gap_register GAP-5 |
| inspection::TI_SI_STORE_LIST_V0 | EXTEND | List every store a composition declares, with the paths and the declarations behind it | Answers every store at once with a count of each store's bindings and not their identities, which is the one hop the new rules cannot make. Gains the identities beside the count. | S6 pps_artifacts_requiring_action #3 |
| inspection::TI_SI_CAPABILITY_SURFACE_V0 | REUSE | | Publishes each act's steps and each operation's effect — the other half of the same derivation. | S6 pps_artifacts_requiring_action #4 |
| runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0 | REVIEW | | States the resolution model this change lets a design declare. Unchanged: the platform already admits the reach. | S6 pps_artifacts_requiring_action #5 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | REVIEW | | Declares what the domain compiles. Unchanged; named because the amended artifacts are compiled under it. | S6 pps_artifacts_requiring_action #2 |

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
| EXTEND | design | 2 | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 |
| EXTEND | inspection | 1 | inspection::TI_SI_STORE_LIST_V0 |
| NEW | design | 0 | |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p7_design_intent_template_v0.md, transformation/design/p7_design_intent/rules.py | S4 design_decisions #6 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | transformation.design.emit:emit_rule_sets | transformation/design/meta.py, transformation/design/p0_change_seed/rules.py, transformation/design/p1_change_request/rules.py, transformation/design/p2_domain_model/rules.py, transformation/design/p3_analysis_loop/rules.py, transformation/design/p4_business_model/rules.py, transformation/design/p5_business_intent/rules.py, transformation/design/p6_governance_intent/rules.py, transformation/design/p7_design_intent/rules.py, transformation/design/p8_authoring_mandate/rules.py | S4 design_decisions #4 |

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

**Status: CLOSED — renewed.** A first closure was withdrawn when the design's claim that the
inspection surface was sufficient turned out to be false; the correction was made at S3, where the
claim was made, and every phase re-judged. Approved by the business author, as a body, against the composition
`2e7815febb7e…` — the same composition every grounded register of this dossier was re-read against
and attested to in `baseline.json`, and the one `rebaseline.md` records the replacement of. What the
approval authorizes is the amendment of the three artifacts §2 marks EXTEND, reached by invoking the generator
§16 declares, and nothing else.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | Ownership, dependencies, artifacts requiring action | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
