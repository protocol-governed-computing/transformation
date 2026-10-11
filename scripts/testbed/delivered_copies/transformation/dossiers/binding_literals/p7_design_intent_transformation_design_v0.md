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
    columns:
    - Decision
    - Business Fact
    - Resolution
    - Source Finding
    rows:
    - Decision: What a literal is
      Business Fact: Every rule that judges a binding reads a literal the same way.
      Resolution: A literal is a single word, a qualified identity, a number, or a value opening with a quote, bracket or brace. The rooting rule keeps this definition. The step-binding form rule and the molecule form rule are widened to admit exactly it, beside the references each already admits.
      Source Finding: 'S4 design_decisions #1'
    - Decision: Whether the widening is retroactive
      Business Fact: No delivered design binds a value the narrower rules refuse.
      Resolution: It is not. It only admits bindings that were refused, and every admitted binding keeps its meaning.
      Source Finding: 'S4 design_decisions #2'
    - Decision: How a generated value is stated
      Business Fact: A generator determines only what the design says it does.
      Resolution: A binding whose source is the single word generated states that the generator of its owner determines the value. A new rule, GENERATED_SOURCE_WITHOUT_GENERATOR, refuses it unless the owner is listed in generation_provenance. It is written in the existing way of judging that resolves a cell in another register, applied only to rows whose source is generated.
      Source Finding: 'S4 design_decisions #3'
    - Decision: What a design meaning the word itself writes
      Business Fact: Reserving the word changes no admitted binding.
      Resolution: It writes the word quoted, which the widened form rule admits as a literal.
      Source Finding: 'S4 design_decisions #4'
    - Decision: What carries the correction
      Business Fact: The Design Intent's workflow carries its rule set as a sealed copy.
      Resolution: The rule declaration and the template change, and the generator seals them into a new version of the workflow. The intent that starts it names the successor.
      Source Finding: 'S4 design_decisions #5'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPLACE
      Summary: Decide whether an offered Design Intent register is admissible
      Reason: Its sealed rule set changes, so WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 supersedes it.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REPOINT
      Summary: Offer a Design Intent register for admissibility judgement
      Reason: Starts the workflow this change replaces; it names the successor and keeps its identity.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: transformation::CT_PURE_EVALUATE_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Applies the corrected rules by ways of judging it already has.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: The contract the workflow runs. Unchanged.
      Source Finding: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    - FQDN: transformation::RB_TRANSFORMATION_BINDINGS_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REUSE
      Summary: ''
      Reason: Binds read-only observation for the workflow. Unchanged.
      Source Finding: transformation::RB_TRANSFORMATION_BINDINGS_V0
    - FQDN: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
      Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW): REVIEW
      Summary: ''
      Reason: Declares what the domain compiles. Unchanged; named because the authored workflow is compiled under it.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
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
    - Capability: Deciding whether a design intent is admissible, reading a literal one way and admitting a value its generator determines
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): WF
      Code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Summary: Decide whether an offered Design Intent register is admissible
      Owner Subdomain: design
      Status: NEW
      Source Finding: 'S6 governance_outcome #1'
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: transformation::RB_TRANSFORMATION_BINDINGS_V0
      Binds WF: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      CS Bindings: capability_side_effects::CS_SNAPSHOT_QUERY_V0
      Storage Structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
  execution_topology:
    columns:
    - Workflow
    - Node
    - Runs
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Node: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): IN
      Routing: ACK -> transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1; NACK -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Node: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): CC
      Routing: SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Node: EXIT_JUDGED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT_SUCCESS
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Node: EXIT_REJECTED
      Runs: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): EXIT
      Routing: —
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
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
    - Owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      Direction (INPUT, OUTPUT): INPUT
      Field: document_text
      Bound To: payload.register_text
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      Direction (INPUT, OUTPUT): INPUT
      Field: prior_texts
      Bound To: payload.prior_texts
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - Owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      Direction (INPUT, OUTPUT): INPUT
      Field: rule_set
      Bound To: generated
      Source Finding: 'S7 design_resolution #3'
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
    - Group
    - Casing
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: NONE IDENTIFIED
      Extends: ''
      Group: ''
      Casing: ''
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
    - Artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Property: supersedes
      Value: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
      Source Finding: S7 existing_inventory WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
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
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Subdomain: design
      Count: '1'
      Artifacts: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: design
      Count: '0'
      Artifacts: ''
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: design
      Count: '1'
      Artifacts: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
      Generator: transformation.design.emit:emit_rule_sets
      Generator Sources: templates/p7_design_intent_template_v0.md, transformation/design/p7_design_intent/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V1.md
      Source Finding: 'S7 design_resolution #5'
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: NONE IDENTIFIED
      Consults: ''
      Source Finding: ''
  refusal_discharge:
    columns:
    - Operation
    - Refused When
    - Act
    - Step
    - Outcome
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Act: ''
      Step: ''
      Outcome: ''
      Source Finding: ''
  refusal_deferrals:
    columns:
    - Operation
    - Refused When
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Operation: Declaring a value generated
      Refused When: The design does not list the artifact that holds it as generated
      Deferred To: The rule GENERATED_SOURCE_WITHOUT_GENERATOR, which this change adds to the Design Intent's rule set
      Until: This change is delivered and the rule is sealed in the composition
      Source Finding: 'S0 operation_refusals #1'
  refusal_governance_discharge:
    columns:
    - Operation
    - Refused When
    - Phase
    - Governing Rule
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Phase: ''
      Governing Rule: ''
      Source Finding: ''
  molecule_steps:
    columns:
    - CT Code
    - Step
    - Kind (atom, molecule, loop)
    - Target
    - Over
    - Iterator
    - Emits
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Step: ''
      Kind (atom, molecule, loop): ''
      Target: ''
      Over: ''
      Iterator: ''
      Emits: ''
      Source Finding: ''
  molecule_step_bindings:
    columns:
    - CT Code
    - Step
    - Role (INPUT, CARRY, UPDATE)
    - Field
    - Bound To
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Step: ''
      Role (INPUT, CARRY, UPDATE): ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  test_cases:
    columns:
    - CT Code
    - Case
    - Expected Outcome (SUCCESS, VIOLATION)
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Case: ''
      Expected Outcome (SUCCESS, VIOLATION): ''
      Source Finding: ''
  test_case_values:
    columns:
    - CT Code
    - Case
    - Role (INPUT, EXPECTED, ASSERT, RECORDED)
    - Field
    - Value
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Case: ''
      Role (INPUT, EXPECTED, ASSERT, RECORDED): ''
      Field: ''
      Value: ''
      Source Finding: ''
  withdrawn_facts:
    columns:
    - Artifact
    - Fact
    - Reason
    - Source Finding
    rows: []
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
