# Stage 8 — Authoring Mandate: blockchain / identity

## Machine

```yaml
document:
  phase: p8
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: blockchain::TI_REGISTER_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '2'
    code: blockchain::TI_ACCEPT_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '3'
    code: blockchain::TI_REJECT_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '2'
    step: '4'
    code: blockchain::TE_REGISTER_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::TI_REGISTER_ACTOR_V0
  - wave: '2'
    step: '5'
    code: blockchain::TE_ACCEPT_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::TI_ACCEPT_ACTOR_V0
  - wave: '2'
    step: '6'
    code: blockchain::TE_REJECT_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::TI_REJECT_ACTOR_V0
  critical_path:
  - position: '1'
    code: blockchain::TI_REGISTER_ACTOR_V0
  - position: '2'
    code: blockchain::TE_REGISTER_ACTOR_V0
  mandate_artifact_summary:
  - action: NEW
    count: '6'
    description: Three ingress declarations, each naming an act the business offers and holding what the act requires and a caller must not send; and three egress declarations, each stating which kind of answer an ending takes and what of the result the caller is told.
  field_declarations:
  - code: blockchain::TI_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_REJECT_ACTOR_V0
    subdomain_field: identity
  new_capabilities: null
  new_intents: null
  cross_subdomain_notes:
  - code: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
    note: Amended, not authored, and therefore not scheduled as a build step. It already admits both boundary kinds among its artifact types; what is added is the source layer they are found in and the identity rule that puts them in this namespace. The amendment must be in place before any of the six is compiled, because a declaration in a layer the manifest does not search is a declaration the compiler never sees.
  - code: blockchain::WF_REGISTER_ACTOR_V0
    note: Reached unchanged. The ingress declaration names it as the act it dispatches to; nothing about the act, its topology or its bindings is amended.
  - code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    note: Reached unchanged by two declarations, one holding the constants of an acceptance and one those of a rejection. That one act serves two offered names is invisible to a caller, and is what allows the business's public names to follow what it records rather than what it executes.
  - code: blockchain::CC_VALIDATE_REGISTRATION_V0
    note: Reached unchanged, but the declaration it validates against now arrives from a sealed artifact rather than from whoever calls. What the ingress declares a caller may send and what this contract is given to validate against must name the same fields; a change to either without the other is a change to the readability test the business refused to have stated twice.
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
