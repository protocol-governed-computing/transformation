# Stage 8 — Authoring Mandate: platform / conformance

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: enforcement_capability
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
    - Wave: '1'
      Step: '1'
      Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: conformance
      Depends On: —
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '1'
      Description: 'The vocabulary of places an obligation may be enforced: the five in use today, plus a place meaning carried elsewhere with the destination named, and a place meaning declared and not yet enforced. It is the one artifact this change renders.'
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '0'
      Description: The governance surface is authored rather than rendered, so the four amendments Stage 7 assigned are written by hand and carry no build step. Two constitutions gain a requirement; two obligations of this subdomain are restated with the place that matches what their checks do.
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Count: '0'
      Description: Nothing is replaced by construction. The check module belonging to the parity obligation is withdrawn by hand, with the exclusion that named it.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Subdomain Field: conformance
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
    - Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Note: Governs a field every obligation declares, so it is read by six subdomains beyond this one. It is admitted before any obligation may declare a place it carries.
    - Code: capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0
      Note: Withdrawn by `capability_contracts`, not here. The only artifact of this change outside the conformance subdomain, and it is named rather than scheduled.
    - Code: authority::INVARIANT_NO_AMBIENT_AUTHORITY_V0
      Note: One of fourteen obligations across six subdomains whose declared response to a violation their checks cannot produce. Each owner restates its own; none is scheduled here.
    - Code: surface_contract::INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0
      Note: The one delegation naming a practice rather than a mechanism. Its owner restates it as declared and not yet enforced, since code review is not a destination that can be confirmed.
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

**Status: CLOSED.** Approved by the business author against the composition `10aa26e1582f…`, the one
`baseline.json` pins, after Construction Completeness read 100% on the single artifact this mandate
renders.

What is frozen is one vocabulary and the seven places it admits. The four governance amendments are
frozen as hand-authored work, not as build steps, because the governance surface is authored rather
than constructed. **An obligation restated by any subdomain other than conformance is outside this
mandate** — §7 names seventeen such obligations across six subdomains, and naming them is not
scheduling them.
