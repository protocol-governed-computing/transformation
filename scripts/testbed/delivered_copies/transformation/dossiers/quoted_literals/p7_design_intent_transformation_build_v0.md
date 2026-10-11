# Stage 7 — Design Intent: transformation / build

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: quoted_literals
  Status: DRAFT
  Feeds: Stage 8 — Authoring Mandate
registers:
  design_resolution:
  - decision: Where the correction lives
    business_fact: A field's default and an artifact's property were not found wrong.
    resolution: In the rendering of a binding alone. The shared reading of a value is unchanged.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: How a quoted literal renders
    business_fact: The runtime receives the value a design states.
    resolution: A binding opening and closing with the same quote mark renders as the text between them. A number with a decimal part renders as a number. Every other binding renders as today.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: What carries the correction
    business_fact: The render transform's declaration states nothing about how a literal is rendered.
    resolution: Its implementation. No artifact is replaced or extended, and construction schedules nothing.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: What proves it
    business_fact: The keyed-node probe recorded the defect as intended.
    resolution: The probe expects each recorded reason as its value; a probe renders a quoted dotted value and a decimal; every delivered artifact reproduces unchanged.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  existing_inventory:
  - fqdn: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    action: REVIEW
    summary: ''
    reason: Its implementation renders a quoted and a decimal literal as their values. Its declaration is unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    action: REUSE
    summary: ''
    reason: Runs the rendering. Unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
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
  - action: REPLACE
    subdomain: build
    count: '0'
    artifacts: ''
  - action: EXTEND
    subdomain: build
    count: '0'
    artifacts: ''
  - action: NEW
    subdomain: build
    count: '0'
    artifacts: ''
  generation_provenance: []
  declared_reach: []
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases: []
  test_case_values: []
  withdrawn_facts: null
```

HOW: the correction is the render transform's implementation. No artifact changes meaning, so none
is replaced, extended or authored.

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
