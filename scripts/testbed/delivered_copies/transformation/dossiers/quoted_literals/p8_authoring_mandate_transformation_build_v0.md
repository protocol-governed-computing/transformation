# Stage 8 — Authoring Mandate: transformation / build

## Machine

```yaml
document:
  phase: p8
  domain: transformation
  subdomain: build
  cr: quoted_literals
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order: []
  critical_path: []
  mandate_artifact_summary:
  - action: REPLACE
    count: '0'
    description: Nothing is replaced.
  - action: EXTEND
    count: '0'
    description: Nothing is extended. The render transform's declaration states nothing about how a literal is rendered, and is unchanged.
  - action: NEW
    count: '0'
    description: The change authors no artifact. It corrects the render transform's implementation.
  field_declarations:
  - code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    subdomain_field: build
  new_capabilities: []
  new_intents: []
  cross_subdomain_notes: []
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
