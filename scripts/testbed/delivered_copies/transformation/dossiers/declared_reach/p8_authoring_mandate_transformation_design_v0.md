# Stage 8 — Authoring Mandate: transformation / design

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: declared_reach
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
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '3'
      Description: The phase workflow that seals the rule set judging a design and the contract that observes the composition it is judged against, both reached by invoking their generator; and the store surface that answers every store at once, which gains the binding identities it already counts.
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '0'
      Description: The change authors no artifact. What it adds is a register of the design language and the rules that hold it, and both are sources of an artifact that already exists.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
      Subdomain Field: design
    - Code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
      Subdomain Field: design
    - Code: inspection::TI_SI_STORE_LIST_V0
      Subdomain Field: inspection
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

**Status: CLOSED — renewed.** Approved by the business author against the composition
`2e7815febb7e…`. A first closure of this gate was withdrawn: the design it locked declared the
inspection dependency SATISFIED, and it is a gap. The correction was made where the claim was made —
S3's third analysis finding said nothing new needs publishing — and re-judged from P3 forward rather
than carried as a deviation from a mandate that was wrong.

What is frozen is unusual and worth stating plainly: the mandate schedules **no build step**, because
the change authors no artifact. What it freezes is therefore the *amendment* set — the three artifacts
§3 counts and no others — and the way they are reached. Two are reached by invoking the generator the
design declared; the third is a projection widened to publish what it already computes. An artifact
written by hand into any of them is outside this mandate however correct it looks, and that is the
whole of what the freeze means here.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, generation provenance, artifact summary | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
