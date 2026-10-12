# Stage 8 — Authoring Mandate: transformation / design

## Machine

```yaml
document:
  phase: p8
  domain: transformation
  subdomain: design
  cr: binding_literals
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    action: NEW
    subdomain: design
    depends_on: null
  critical_path:
  - position: '1'
    code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
  mandate_artifact_summary:
  - action: REPLACE
    count: '1'
    description: The Design Intent's workflow, stood down by its successor naming it; not scheduled, because nothing is authored for it.
  - action: EXTEND
    count: '0'
    description: Nothing is extended.
  - action: NEW
    count: '1'
    description: The Design Intent's successor workflow, reached by invoking the generator §16 of the design declares, and never written.
  field_declarations:
  - code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
    subdomain_field: design
  - code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1
    subdomain_field: design
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

What is frozen is one workflow replaced by its successor, which the generator emits, and the intent
that starts it named again. What reaches the successor is the Design Intent's rule declaration and
its template:

- the step-binding form rule and the molecule form rule admit a literal exactly as the rooting rule
  defines one: a single word, a qualified identity, a number, or a value opening with a quote,
  bracket or brace;
- one rule, `GENERATED_SOURCE_WITHOUT_GENERATOR`, refuses a binding whose source is `generated`
  unless its owner is listed in `generation_provenance`, written in the existing way of judging that
  resolves a cell in another register;
- the template states the definition of a literal and the reserved source.

A rule written by hand into the sealed rule set is outside this mandate however correct it looks,
and so is a new way of judging.

**The probes are inside the freeze.** One test document per newly admitted form — a quoted dotted
value, a number, a qualified identity, each in a step binding and in a molecule binding — and one
built to fail the new rule, are part of what this mandate schedules. Every Design Intent document in
the test corpus keeps its verdict and its findings; a verdict that moves is a finding, not a cost.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, replacement, generation provenance | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
