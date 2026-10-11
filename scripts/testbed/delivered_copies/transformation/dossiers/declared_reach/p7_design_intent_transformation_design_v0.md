# Stage 7 — Design Intent: transformation / design

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: declared_reach
  Status: DRAFT
  Feeds: Stage 8 — Authoring Mandate
registers:
  design_resolution:
  - decision: The reach is stated in a register of its own.
    business_fact: Ownership and reach are structurally distinct, never one register with a column telling them apart.
    resolution: A register of the design language, declared in `templates/p7_design_intent_template_v0.md` and governed by rules in `transformation/design/p7_design_intent/rules.py`. Those two files are the generator sources of the artifact this change amends, so the register and the rules that hold it are one amendment.
    source_finding: 'S4 design_decisions #1'
  - decision: A design names a binding; its records are derived.
    business_fact: A design names a binding and never the records behind it.
    resolution: The register carries the binding's identity and nothing else. Which records it covers is read from `si.store.list` at judging time, so the design states one fact and the composition answers the other. That surface counts a store's bindings today without naming them, so it is amended to publish the identities it already holds — a projection of what it computes, not a new derivation, and `si.store.show` is untouched.
    source_finding: 'S4 design_decisions #2; S4 gap_register GAP-7'
  - decision: The two refusals are delivered together.
    business_fact: Every declared reach is used, and every read is declared.
    resolution: Two rules in one amendment of `transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0`. Neither is emitted without the other, because the generator emits the phase's whole rule set at once.
    source_finding: 'S4 design_decisions #3'
  - decision: The store surface is declared among what the design phase observes.
    business_fact: A rule that is not passed the facts it reasons from reports nothing and is indistinguishable from a rule that checked.
    resolution: One declaration, in the phase's own rule module, and everything else follows from it. `transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0` already generates the map that keys an observation to the step producing it, and fails the build where a phase declares an observation no step produces. The step itself is the last hand-kept copy of that same declaration, so the emission produces it too, and the contract becomes generated in the half this change touches. Construction writes neither artifact.
    source_finding: 'S4 design_decisions #4'
  - decision: What a design states is what the built act carries.
    business_fact: A reach is never added to a built artifact by hand.
    resolution: Construction renders the declared reach into the runtime binding of the act that declared it, from the register alone.
    source_finding: 'S4 design_decisions #5'
  - decision: The change is delivered through the pipeline, naming the generator of the document it amends.
    business_fact: The document that judges a design is produced by a generator rather than written.
    resolution: '`transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0` is declared in §16 with its generator and both sources. Construction invokes the generator and writes none of it.'
    source_finding: 'S4 design_decisions #6'
  existing_inventory:
  - fqdn: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    action: EXTEND
    summary: 'Phase 7 of the change pipeline: decide whether an offered Design Intent register is admissible'
    reason: Carries the rule set that judges a design. Gains the register that states a reach and the two rules that hold it.
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  - fqdn: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
    action: EXTEND
    summary: Parse a phase document and its priors, observe the composition, and judge them together
    reason: Gains the step that observes the store surface, without which every new rule reports nothing.
    source_finding: S4 gap_register GAP-5
  - fqdn: inspection::TI_SI_STORE_LIST_V0
    action: EXTEND
    summary: List every store a composition declares, with the paths and the declarations behind it
    reason: Answers every store at once with a count of each store's bindings and not their identities, which is the one hop the new rules cannot make. Gains the identities beside the count.
    source_finding: 'S6 pps_artifacts_requiring_action #3'
  - fqdn: inspection::TI_SI_CAPABILITY_SURFACE_V0
    action: REUSE
    summary: ''
    reason: Publishes each act's steps and each operation's effect — the other half of the same derivation.
    source_finding: 'S6 pps_artifacts_requiring_action #4'
  - fqdn: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
    action: REVIEW
    summary: ''
    reason: 'States the resolution model this change lets a design declare. Unchanged: the platform already admits the reach.'
    source_finding: 'S6 pps_artifacts_requiring_action #5'
  - fqdn: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
    action: REVIEW
    summary: ''
    reason: Declares what the domain compiles. Unchanged; named because the amended artifacts are compiled under it.
    source_finding: 'S6 pps_artifacts_requiring_action #2'
  new_artifacts: []
  rb_declarations: []
  execution_topology: []
  cc_composition: []
  step_bindings: []
  interface_fields: []
  implementation_bindings: []
  vocabulary_extensions: []
  runtime_policies: []
  artifact_properties: []
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: EXTEND
    subdomain: design
    count: '2'
    artifacts: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
  - action: EXTEND
    subdomain: inspection
    count: '1'
    artifacts: inspection::TI_SI_STORE_LIST_V0
  - action: NEW
    subdomain: design
    count: '0'
    artifacts: ''
  generation_provenance:
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - templates/p7_design_intent_template_v0.md
    - transformation/design/p7_design_intent/rules.py
    source_finding: 'S4 design_decisions #6'
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - transformation/design/meta.py
    - transformation/design/p0_change_seed/rules.py
    - transformation/design/p1_change_request/rules.py
    - transformation/design/p2_domain_model/rules.py
    - transformation/design/p3_analysis_loop/rules.py
    - transformation/design/p4_business_model/rules.py
    - transformation/design/p5_business_intent/rules.py
    - transformation/design/p6_governance_intent/rules.py
    - transformation/design/p7_design_intent/rules.py
    - transformation/design/p8_authoring_mandate/rules.py
    source_finding: 'S4 design_decisions #4'
  declared_reach: []
```

HOW. Binding FQDNs are assigned here; business facts and placement decisions are not repeated.

---

## 1. Design Decisions Resolution

---

## 2. Artifact Inventory — Existing Artifacts

---

## 3. Artifact Family Mapping — New Artifacts

---

## 4. Runtime Binding (RB) Declarations

---

## 5. Execution Topology

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Implementation Bindings

---

## 10. Vocabulary Extensions

---

## 11. Runtime Policies

---

## 12. Artifact Properties

---

## 13. STRUCTURE Stores

---

## 14. Transport Bindings

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

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
