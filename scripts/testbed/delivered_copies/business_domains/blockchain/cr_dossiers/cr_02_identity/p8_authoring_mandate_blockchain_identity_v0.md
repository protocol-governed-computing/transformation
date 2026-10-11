# Stage 8 — Authoring Mandate: blockchain / identity

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_02_identity
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
      Code: blockchain::TI_REGISTER_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '1'
      Step: '2'
      Code: blockchain::TI_ACCEPT_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '1'
      Step: '3'
      Code: blockchain::TI_REJECT_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: —
    - Wave: '2'
      Step: '4'
      Code: blockchain::TE_REGISTER_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::TI_REGISTER_ACTOR_V0
    - Wave: '2'
      Step: '5'
      Code: blockchain::TE_ACCEPT_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::TI_ACCEPT_ACTOR_V0
    - Wave: '2'
      Step: '6'
      Code: blockchain::TE_REJECT_ACTOR_V0
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: identity
      Depends On: blockchain::TI_REJECT_ACTOR_V0
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: blockchain::TI_REGISTER_ACTOR_V0
    - Position: '2'
      Code: blockchain::TE_REGISTER_ACTOR_V0
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '6'
      Description: Three ingress declarations, each naming an act the business offers and holding what the act requires and a caller must not send; and three egress declarations, each stating which kind of answer an ending takes and what of the result the caller is told.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: blockchain::TI_REGISTER_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TI_ACCEPT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TI_REJECT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TE_REGISTER_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TE_ACCEPT_ACTOR_V0
      Subdomain Field: identity
    - Code: blockchain::TE_REJECT_ACTOR_V0
      Subdomain Field: identity
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows: []
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows: []
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
      Note: Amended, not authored, and therefore not scheduled as a build step. It already admits both boundary kinds among its artifact types; what is added is the source layer they are found in and the identity rule that puts them in this namespace. The amendment must be in place before any of the six is compiled, because a declaration in a layer the manifest does not search is a declaration the compiler never sees.
    - Code: blockchain::WF_REGISTER_ACTOR_V0
      Note: Reached unchanged. The ingress declaration names it as the act it dispatches to; nothing about the act, its topology or its bindings is amended.
    - Code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Note: Reached unchanged by two declarations, one holding the constants of an acceptance and one those of a rejection. That one act serves two offered names is invisible to a caller, and is what allows the business's public names to follow what it records rather than what it executes.
    - Code: blockchain::CC_VALIDATE_REGISTRATION_V0
      Note: Reached unchanged, but the declaration it validates against now arrives from a sealed artifact rather than from whoever calls. What the ingress declares a caller may send and what this contract is given to validate against must name the same fields; a change to either without the other is a change to the readability test the business refused to have stated twice.
```

Mechanically derived from the design. Every artifact the design declares appears here exactly once,
scheduled after everything it depends on. Nothing is decided at this stage; the order is read off the
design's own dependencies.

Six artifacts, three independent pairs. Each ingress declaration names an act that already exists and
is scheduled before its egress, so that a request can be admitted before there is anything to say
about how it ended. The pairs do not depend on one another and could be built in any order among
themselves; they are scheduled register first, then acceptance, then rejection, following the order
in which the business performs them.

---

## 1. Build Dependency Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes

---

## Gate 2 — Dossier Lock

**Gate 2 closes here.** The dossier is locked before artifact authoring begins.

---

## gov_projection — Governed Handoff to Artifact Authoring

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 7 | design_resolution · existing_inventory · new_artifacts · interface_fields · artifact_properties · transport_bindings · artifact_summary |
| **Emits** → Authoring | build_order · critical_path · mandate_artifact_summary · field_declarations · new_capabilities · new_intents · cross_subdomain_notes |
