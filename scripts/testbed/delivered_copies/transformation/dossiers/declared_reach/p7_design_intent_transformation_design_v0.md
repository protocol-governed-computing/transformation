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
    columns:
    - Decision
    - Business Fact
    - Resolution
    - Source Finding
    rows:
    - Decision: The reach is stated in a register of its own.
      Business Fact: Ownership and reach are structurally distinct, never one register with a column telling them apart.
      Resolution: A register of the design language, declared in `templates/p7_design_intent_template_v0.md` and governed by rules in `transformation/design/p7_design_intent/rules.py`. Those two files are the generator sources of the artifact this change amends, so the register and the rules that hold it are one amendment.
      Source Finding: 'S4 design_decisions #1'
    - Decision: A design names a binding; its records are derived.
      Business Fact: A design names a binding and never the records behind it.
      Resolution: The register carries the binding's identity and nothing else. Which records it covers is read from `si.store.list` at judging time, so the design states one fact and the composition answers the other. That surface counts a store's bindings today without naming them, so it is amended to publish the identities it already holds — a projection of what it computes, not a new derivation, and `si.store.show` is untouched.
      Source Finding: 'S4 design_decisions #2; S4 gap_register GAP-7'
    - Decision: The two refusals are delivered together.
      Business Fact: Every declared reach is used, and every read is declared.
      Resolution: Two rules in one amendment of `transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0`. Neither is emitted without the other, because the generator emits the phase's whole rule set at once.
      Source Finding: 'S4 design_decisions #3'
    - Decision: The store surface is declared among what the design phase observes.
      Business Fact: A rule that is not passed the facts it reasons from reports nothing and is indistinguishable from a rule that checked.
      Resolution: One declaration, in the phase's own rule module, and everything else follows from it. `transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0` already generates the map that keys an observation to the step producing it, and fails the build where a phase declares an observation no step produces. The step itself is the last hand-kept copy of that same declaration, so the emission produces it too, and the contract becomes generated in the half this change touches. Construction writes neither artifact.
      Source Finding: 'S4 design_decisions #4'
    - Decision: What a design states is what the built act carries.
      Business Fact: A reach is never added to a built artifact by hand.
      Resolution: Construction renders the declared reach into the runtime binding of the act that declared it, from the register alone.
      Source Finding: 'S4 design_decisions #5'
    - Decision: The change is delivered through the pipeline, naming the generator of the document it amends.
      Business Fact: The document that judges a design is produced by a generator rather than written.
      Resolution: '`transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0` is declared in §16 with its generator and both sources. Construction invokes the generator and writes none of it.'
      Source Finding: 'S4 design_decisions #6'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: 'Phase 7 of the change pipeline: decide whether an offered Design Intent register is admissible'
      Reason: Carries the rule set that judges a design. Gains the register that states a reach and the two rules that hold it.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Parse a phase document and its priors, observe the composition, and judge them together
      Reason: Gains the step that observes the store surface, without which every new rule reports nothing.
      Source Finding: S4 gap_register GAP-5
    - FQDN: inspection::TI_SI_STORE_LIST_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: List every store a composition declares, with the paths and the declarations behind it
      Reason: Answers every store at once with a count of each store's bindings and not their identities, which is the one hop the new rules cannot make. Gains the identities beside the count.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: inspection::TI_SI_CAPABILITY_SURFACE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: ''
      Reason: Publishes each act's steps and each operation's effect — the other half of the same derivation.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: ''
      Reason: 'States the resolution model this change lets a design declare. Unchanged: the platform already admits the reach.'
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: ''
      Reason: Declares what the domain compiles. Unchanged; named because the amended artifacts are compiled under it.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: NONE IDENTIFIED
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): ''
      Code: ''
      Summary: ''
      Owner Subdomain: ''
      Status: ''
      Source Finding: ''
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: NONE IDENTIFIED
      Binds WF: ''
      CS Bindings: ''
      Storage Structure: ''
      Source Finding: ''
  execution_topology:
    columns:
    - Workflow
    - Node
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: NONE IDENTIFIED
      Node: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): ''
      Routing: ''
      Source Finding: ''
  cc_composition:
    columns:
    - CC Code
    - Step
    - Step Name
    - Capability
    - Kind (CT, CS)
    - Operation
    - Store
    - Consumes
    - Produces
    - Routing
    - Interpreted By
    - Semantic Status
    - Interface
    rows:
    - CC Code: NONE IDENTIFIED
      Step: ''
      Step Name: ''
      Capability: ''
      Kind (CT, CS): ''
      Operation: ''
      Store: ''
      Consumes: ''
      Produces: ''
      Routing: ''
      Interpreted By: ''
      Semantic Status: ''
      Interface: ''
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: NONE IDENTIFIED
      Step: ''
      Direction (INPUT, OUTPUT): ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  interface_fields:
    columns:
    - Artifact
    - Direction (INPUT, OUTPUT, ATTRIBUTE)
    - Field
    - Type
    - Required (YES, NO)
    - Default
    - Meaning
    rows:
    - Artifact: NONE IDENTIFIED
      Direction (INPUT, OUTPUT, ATTRIBUTE): ''
      Field: ''
      Type: ''
      Required (YES, NO): ''
      Default: ''
      Meaning: ''
  implementation_bindings:
    columns:
    - CT Code
    - Module
    - Callable
    - Operation
    - Kind (atom, molecule)
    - Purity (ct_pure, ct_impure)
    - Refusal (raises, returns, never)
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Module: ''
      Callable: ''
      Operation: ''
      Kind (atom, molecule): ''
      Purity (ct_pure, ct_impure): ''
      Refusal (raises, returns, never): ''
      Source Finding: ''
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: NONE IDENTIFIED
      Extends: ''
      Value: ''
      Meaning: ''
      Source Finding: ''
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows:
    - RB Code: NONE IDENTIFIED
      Capability: ''
      Key: ''
      Value: ''
      Source Finding: ''
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Property: ''
      Value: ''
      Source Finding: ''
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: NONE IDENTIFIED
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): ''
      Proposed Path: ''
      Used By: ''
      Source Finding: ''
  transport_bindings:
    columns:
    - Artifact
    - Direction (INGRESS, EGRESS)
    - Operation
    - Handler Kind (WF_INVOCATION, SNAPSHOT_READ)
    - Handler Target
    - Field
    - Bound To
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Direction (INGRESS, EGRESS): ''
      Operation: ''
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): ''
      Handler Target: ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: design
      Count: '2'
      Artifacts: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: inspection
      Count: '1'
      Artifacts: inspection::TI_SI_STORE_LIST_V0
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: design
      Count: '0'
      Artifacts: ''
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
      Generator: transformation.design.emit:emit_rule_sets
      Generator Sources: templates/p7_design_intent_template_v0.md, transformation/design/p7_design_intent/rules.py
      Source Finding: 'S4 design_decisions #6'
    - Artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
      Generator: transformation.design.emit:emit_rule_sets
      Generator Sources: transformation/design/meta.py, transformation/design/p0_change_seed/rules.py, transformation/design/p1_change_request/rules.py, transformation/design/p2_domain_model/rules.py, transformation/design/p3_analysis_loop/rules.py, transformation/design/p4_business_model/rules.py, transformation/design/p5_business_intent/rules.py, transformation/design/p6_governance_intent/rules.py, transformation/design/p7_design_intent/rules.py, transformation/design/p8_authoring_mandate/rules.py
      Source Finding: 'S4 design_decisions #4'
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: NONE IDENTIFIED
      Consults: ''
      Source Finding: ''
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
