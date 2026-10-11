# Stage 8 — Authoring Mandate: blockchain / identity

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_03_identity
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
    rows: []
  critical_path:
    columns:
    - Position
    - Code
    rows: []
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '1'
      Description: One capability contract, rendered whole under its own code. Four of its five steps are unchanged; the fifth calls a keyed update in place of a keyed write, taking the record the fourth step assembles as the fields to set.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
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
    - Code: capability_side_effects::CS_MUTABLE_JSON_V0
      Note: 'The keyed update this correction calls was added to the capability before this change was designed, on the neutral surface and not by this domain. A business domain may not author a capability, and the operation it needed did not exist: the store offered a keyed write and a filtered update, and nothing that changed part of one record addressed by its key. Identity depends on it exactly as the change that established this function depended on a clock.'
    - Code: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
      Note: Composes the amended contract and is not amended. Its routing reads the contract's result statuses, which the correction preserves, so re-rendering the contract changes nothing the workflow observes.
    - Code: blockchain::CC_RESOLVE_ACTOR_V0
      Note: Reached unchanged, and the only reader of the store. From this change forward it will read records still carrying the name and preferences a decision had been stripping. It reads the record whole and asserts nothing about its shape, so more fields reach it and nothing about it needs to change.
    - Code: blockchain::TI_ACCEPT_ACTOR_V0
      Note: Unchanged, with blockchain::TI_REJECT_ACTOR_V0 and both egress declarations. They name a workflow rather than a contract, which is why a correction inside a contract is invisible to every caller.
```

Mechanically derived from the design. Every artifact the design declares appears here exactly once,
scheduled after everything it depends on. Nothing is decided at this stage; the order is read off the
design's own dependencies.

**Nothing is scheduled.** This change authors no artifact, and an amended artifact is never a build
step — a mandate may not schedule authoring an identity the composition already holds. The one
artifact this change touches is realized because the design amends it, which construction reads from
the design rather than from this mandate. A build order with no rows is the correct shape for a
correction, and it is stated here rather than left to be inferred from an absence.

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
| **Consumes** ← Stage 7 | design_resolution · existing_inventory · new_artifacts · cc_composition · step_bindings · interface_fields · artifact_properties · artifact_summary |
| **Emits** → Authoring | build_order · critical_path · mandate_artifact_summary · field_declarations · new_capabilities · new_intents · cross_subdomain_notes |
