# Stage 8 — Authoring Mandate: platform / structure

## Machine

```yaml
document:
  phase: p8
  domain: platform
  subdomain: structure
  cr: schema_governance
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: structure::VOCAB_SCHEMA_DISPOSITION_V0
    action: NEW
    subdomain: structure
    depends_on: null
  critical_path:
  - position: '1'
    code: structure::VOCAB_SCHEMA_DISPOSITION_V0
  mandate_artifact_summary:
  - action: NEW
    count: '1'
    description: The two dispositions a kind may have toward description. It is admitted first because the dispatch table's new column draws every value from it.
  - action: EXTEND
    count: '0'
    description: 'Two amendments are written by hand, because the governance surface is authored rather than rendered: the dispatch table gains a disposition per kind, and the constitution gains what a description must state to count as one. Neither carries a build step.'
  - action: REPLACE
    count: '0'
    description: Nothing is stood down. Three descriptions are corrected by the subdomains that own their kinds, and two are written by the subdomain that owns theirs; none of that is scheduled here.
  field_declarations:
  - code: structure::VOCAB_SCHEMA_DISPOSITION_V0
    subdomain_field: structure
  new_capabilities: []
  new_intents: []
  cross_subdomain_notes:
  - code: actor::CONSTITUTION_ACTOR_V0
    note: Corrected by `actor`, not here. Its description expects a role and forbids the attributes every actor carries. What a declaration admits is its owner's to state; this mandate states only that the kind is described.
  - code: event::CONSTITUTION_EVENT_V0
    note: Corrected by `event`, not here. Its description forbids content twenty declarations carry.
  - code: intent::CONSTITUTION_INTENT_V0
    note: Corrected by `intent`, not here. Its description rejects a whole number as a type across thirty-one declarations.
  - code: transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0
    note: Described by `transport`, not here. Its two kinds carry forty-four artifacts and have no description at all.
  - code: structure::STRUCTURE_SCHEMA_DISPATCH_V0
    note: Amended by hand. Every value of its new column is drawn from the vocabulary this mandate schedules, so the vocabulary is admitted first.
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
