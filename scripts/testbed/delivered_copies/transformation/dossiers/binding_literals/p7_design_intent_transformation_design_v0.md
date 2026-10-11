# Stage 7 — Design Intent: transformation / design

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: binding_literals
  Status: DRAFT
  Feeds: Stage 8 — Authoring Mandate
registers:
  design_resolution:
  - decision: What a literal is
    business_fact: Every rule that judges a binding reads a literal the same way.
    resolution: A literal is a single word, a qualified identity, a number, or a value opening with a quote, bracket or brace. The rooting rule keeps this definition. The step-binding form rule and the molecule form rule are widened to admit exactly it, beside the references each already admits.
    source_finding: 'S4 design_decisions #1'
  - decision: Whether the widening is retroactive
    business_fact: No delivered design binds a value the narrower rules refuse.
    resolution: It is not. It only admits bindings that were refused, and every admitted binding keeps its meaning.
    source_finding: 'S4 design_decisions #2'
  - decision: How a generated value is stated
    business_fact: A generator determines only what the design says it does.
    resolution: A binding whose source is the single word generated states that the generator of its owner determines the value. A new rule, GENERATED_SOURCE_WITHOUT_GENERATOR, refuses it unless the owner is listed in generation_provenance. It is written in the existing way of judging that resolves a cell in another register, applied only to rows whose source is generated.
    source_finding: 'S4 design_decisions #3'
  - decision: What a design meaning the word itself writes
    business_fact: Reserving the word changes no admitted binding.
    resolution: It writes the word quoted, which the widened form rule admits as a literal.
    source_finding: 'S4 design_decisions #4'
  - decision: What carries the correction
    business_fact: The Design Intent's workflow carries its rule set as a sealed copy.
    resolution: The rule declaration and the template change, and the generator seals them into a new version of the workflow. The intent that starts it names the successor.
    source_finding: 'S4 design_decisions #5'
  existing_inventory:
  - fqdn: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
    action: REPLACE
    summary: Decide whether an offered Design Intent register is admissible
    reason: Its sealed rule set changes, so WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 supersedes it.
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  - fqdn: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    action: REPOINT
    summary: Offer a Design Intent register for admissibility judgement
    reason: Starts the workflow this change replaces; it names the successor and keeps its identity.
    source_finding: 'S6 pps_artifacts_requiring_action #2'
  - fqdn: transformation::CT_PURE_EVALUATE_RULES_V0
    action: REUSE
    summary: ''
    reason: Applies the corrected rules by ways of judging it already has.
    source_finding: 'S6 pps_artifacts_requiring_action #3'
  - fqdn: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    action: REUSE
    summary: ''
    reason: The contract the workflow runs. Unchanged.
    source_finding: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
  - fqdn: transformation::RB_TRANSFORMATION_BINDINGS_V0
    action: REUSE
    summary: ''
    reason: Binds read-only observation for the workflow. Unchanged.
    source_finding: transformation::RB_TRANSFORMATION_BINDINGS_V0
  - fqdn: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
    action: REVIEW
    summary: ''
    reason: Declares what the domain compiles. Unchanged; named because the authored workflow is compiled under it.
    source_finding: 'S6 pps_artifacts_requiring_action #4'
  new_artifacts:
  - capability: Deciding whether a design intent is admissible, reading a literal one way and admitting a value its generator determines
    family: WF
    code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    summary: Decide whether an offered Design Intent register is admissible
    owner_subdomain: design
    status: NEW
    source_finding: 'S6 governance_outcome #1'
  rb_declarations:
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  execution_topology:
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    node: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    runs: ''
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    node: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  cc_composition: []
  step_bindings:
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding: 'S6 pps_artifacts_requiring_action #1'
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding: 'S7 design_resolution #3'
  interface_fields: []
  implementation_bindings: []
  vocabulary_extensions: []
  runtime_policies: []
  artifact_properties:
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    property: supersedes
    value:
    - transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
    source_finding: S7 existing_inventory WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: REPLACE
    subdomain: design
    count: '1'
    artifacts: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
  - action: EXTEND
    subdomain: design
    count: '0'
    artifacts: ''
  - action: NEW
    subdomain: design
    count: '1'
    artifacts: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
  generation_provenance:
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - templates/p7_design_intent_template_v0.md
    - transformation/design/p7_design_intent/rules.py
    - registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V1.md
    source_finding: 'S7 design_resolution #5'
  declared_reach: []
  refusal_discharge: []
  refusal_deferrals:
  - operation: Declaring a value generated
    refused_when: The design does not list the artifact that holds it as generated
    deferred_to: The rule GENERATED_SOURCE_WITHOUT_GENERATOR, which this change adds to the Design Intent's rule set
    until: This change is delivered and the rule is sealed in the composition
    source_finding: 'S0 operation_refusals #1'
  refusal_governance_discharge: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases: []
  test_case_values: []
  withdrawn_facts: null
```

HOW: the binding identities and the declarations they carry. The correction changes the Design
Intent's sealed rule set, so its workflow is replaced by a new version, redeclared whole.

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

---

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

---

## 18. Refusal Discharge

---

## 19. Refusal Deferrals

---

## 20. Refusal — Governance-Surface Discharge

---

## 21. Molecule Steps

---

## 22. Molecule Step Bindings

---

## 23. Test Cases

---

## 24. Test Case Values

---

## 25. Withdrawn Facts

---

## Gate 1 — Design Approval

**Gate 1 closes here.** The full dossier (Stages 0–7) is presented for review as a body.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 6 — Governance Intent | Ownership, artifacts requiring action, boundary rules | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
