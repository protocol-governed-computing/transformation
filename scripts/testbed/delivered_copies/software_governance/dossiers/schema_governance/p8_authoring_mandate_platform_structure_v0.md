# Stage 8 — Authoring Mandate: platform / structure

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: schema_governance
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
      Code: structure::VOCAB_SCHEMA_DISPOSITION_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: structure
      Depends On: —
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: structure::VOCAB_SCHEMA_DISPOSITION_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '1'
      Description: The two dispositions a kind may have toward description. It is admitted first because the dispatch table's new column draws every value from it.
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '0'
      Description: 'Two amendments are written by hand, because the governance surface is authored rather than rendered: the dispatch table gains a disposition per kind, and the constitution gains what a description must state to count as one. Neither carries a build step.'
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Count: '0'
      Description: Nothing is stood down. Three descriptions are corrected by the subdomains that own their kinds, and two are written by the subdomain that owns theirs; none of that is scheduled here.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: structure::VOCAB_SCHEMA_DISPOSITION_V0
      Subdomain Field: structure
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
    - Code: actor::CONSTITUTION_ACTOR_V0
      Note: Corrected by `actor`, not here. Its description expects a role and forbids the attributes every actor carries. What a declaration admits is its owner's to state; this mandate states only that the kind is described.
    - Code: event::CONSTITUTION_EVENT_V0
      Note: Corrected by `event`, not here. Its description forbids content twenty declarations carry.
    - Code: intent::CONSTITUTION_INTENT_V0
      Note: Corrected by `intent`, not here. Its description rejects a whole number as a type across thirty-one declarations.
    - Code: transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0
      Note: Described by `transport`, not here. Its two kinds carry forty-four artifacts and have no description at all.
    - Code: structure::STRUCTURE_SCHEMA_DISPATCH_V0
      Note: Amended by hand. Every value of its new column is drawn from the vocabulary this mandate schedules, so the vocabulary is admitted first.
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

**Status: CLOSED.** Approved by the business author against the composition `8f82acb652c8…`, the one
`baseline.json` pins, after Construction Completeness read 100% on the single artifact this mandate
renders.

What is frozen is one vocabulary of two dispositions, and two hand-authored amendments: a disposition
per kind, and a statement of what a description must contain to be one. **A description of any
artifact kind is outside this mandate** — three are corrected and two are written by the subdomains
that own those kinds, because what a declaration may contain is theirs to state and this change
decides only that it is stated.

The refusals this change writes are recorded in §19 as deferrals rather than discharges. The kind
disposition refusal arms once every kind carries one; arming it first would refuse every build on
kinds this dossier does not describe.
