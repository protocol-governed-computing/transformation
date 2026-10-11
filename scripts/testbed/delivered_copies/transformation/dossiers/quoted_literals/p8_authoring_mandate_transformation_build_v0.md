# Stage 8 — Authoring Mandate: transformation / build

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: quoted_literals
  Status: DRAFT
  Feeds: Artifact Authoring
registers:
  build_order:
    columns:
    - Wave
    - Step
    - Code
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Depends On
    rows:
    - Wave: NONE IDENTIFIED
      Step: ''
      Code: ''
      Action (REPLACE, EXTEND, NEW): ''
      Subdomain: ''
      Depends On: ''
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: NONE IDENTIFIED
      Code: ''
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Count: '0'
      Description: Nothing is replaced.
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '0'
      Description: Nothing is extended. The render transform's declaration states nothing about how a literal is rendered, and is unchanged.
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '0'
      Description: The change authors no artifact. It corrects the render transform's implementation.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
      Subdomain Field: build
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: NONE IDENTIFIED
      Purpose: ''
      Inputs: ''
      Outputs: ''
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: NONE IDENTIFIED
      Purpose: ''
      Workflow: ''
      Inputs: ''
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: NONE IDENTIFIED
      Note: ''
```

Mechanical. Stage 7's assignments re-ordered into a build sequence; nothing added, nothing dropped.

---

## 1. Build Dependency Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Subdomain Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes

---

## Gate 2 — Mandate Approval

**Gate 2 closes here**, and it freezes scope before authoring begins. After it, any departure is an
Approved Deviation recorded in the authoring manifest — never a silent change.

What is frozen is one correction to the rendering of a binding: a value opening and closing with
the same quote mark renders as the text between them, and a number with a decimal part renders as a
number. The shared reading of a value, which renders a field's default and an artifact's property,
is outside this mandate, and so is any artifact's declaration.

**The probes are inside the freeze.** The keyed-node probe expects each recorded reason as its value,
and one probe renders a quoted dotted value and a decimal. Every artifact construction reproduces
today must reproduce unchanged; one that moves is a finding, not a cost.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, design resolution | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
