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
  - wave: '1'
    step: '1'
    code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    action: NEW
    subdomain: conformance
    depends_on: null
  critical_path:
  - position: '1'
    code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
  mandate_artifact_summary:
  - action: NEW
    count: '1'
    description: 'The vocabulary of places an obligation may be enforced: the five in use today, plus a place meaning carried elsewhere with the destination named, and a place meaning declared and not yet enforced. It is the one artifact this change renders.'
  - action: EXTEND
    count: '0'
    description: The governance surface is authored rather than rendered, so the four amendments Stage 7 assigned are written by hand and carry no build step. Two constitutions gain a requirement; two obligations of this subdomain are restated with the place that matches what their checks do.
  - action: REPLACE
    count: '0'
    description: Nothing is replaced by construction. The check module belonging to the parity obligation is withdrawn by hand, with the exclusion that named it.
  field_declarations:
  - code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    subdomain_field: conformance
  new_capabilities: []
  new_intents: []
  cross_subdomain_notes:
  - code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    note: Governs a field every obligation declares, so it is read by six subdomains beyond this one. It is admitted before any obligation may declare a place it carries.
  - code: capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0
    note: Withdrawn by `capability_contracts`, not here. The only artifact of this change outside the conformance subdomain, and it is named rather than scheduled.
  - code: authority::INVARIANT_NO_AMBIENT_AUTHORITY_V0
    note: One of fourteen obligations across six subdomains whose declared response to a violation their checks cannot produce. Each owner restates its own; none is scheduled here.
  - code: surface_contract::INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0
    note: The one delegation naming a practice rather than a mechanism. Its owner restates it as declared and not yet enforced, since code review is not a destination that can be confirmed.
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
