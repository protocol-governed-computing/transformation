# Stage 8 — Authoring Mandate: transformation / design

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: refusal_discharge
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
      Description: The phase workflow that seals the rule set judging a design, the contract that observes the composition a design is judged against, and the transform carrying the check kinds the rules are built from — all three reached by invoking the generator §16 declares, and none of them written.
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '0'
      Description: The change authors no artifact. What it adds is two registers of the design language, five rules and two check kinds, and every one of those is a source of an artifact that already exists.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
      Subdomain Field: design
    - Code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
      Subdomain Field: design
    - Code: transformation::CT_PURE_EVALUATE_RULES_V0
      Subdomain Field: design
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

**Status: CLOSED.** Approved by the business author against the composition `6e1e571dbbb8…`, the one
`baseline.json` pins. Construction Completeness is not cited because it does not apply: §3 records
zero NEW, and the three EXTEND artifacts are re-emitted by their generator rather than rendered from
a register.

What is frozen is the amendment set and the way it is reached: three artifacts, none authored, all
three re-emitted by the generator §16 declares. What reaches them is two registers appended to the
design intent template, five rules in that phase's rule module, two check kinds, one existing check
kind gaining an optional parameter, and the seed added to the phase's declared priors. A rule written
by hand into the sealed rule set is outside this mandate however correct it looks, and so is a check
kind added without a rule that uses it.

**The probes are inside the freeze, not beside it.** Five rules are authored and no document in the
corpus states a discharge, so each would report clean on its first run while checking nothing. One
probe per rule, each built to fail, is part of what this mandate schedules — not a follow-up someone
may decide the green has made unnecessary.

**Declaring a prior is not free, and what it costs is frozen here too.** The six existing P7 payloads
in the phase testbed carry `p5` and `p6`. Adding the seed to the phase's declared priors makes every
one of them a run missing a prior it declares, which the phase reports as an unchecked handoff rather
than passing quietly. Supplying `p0` to those six is inside this mandate: it authors nothing, changes
no rule and alters no verdict that was correct before. **A payload whose verdict changes is not
covered by this paragraph** — that is a rule firing on an existing document, and it is a finding.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, amendments, generation provenance | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
