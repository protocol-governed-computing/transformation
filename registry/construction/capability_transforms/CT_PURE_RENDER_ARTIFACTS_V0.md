# CT_PURE_RENDER_ARTIFACTS_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_RENDER_ARTIFACTS_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Render every protocol artifact a mandate schedules, from the design that determines it.

This is the Construction lifecycle's one generative step. P0–P8 judge documents and emit verdicts;
this consumes `DesignIntent(P7) + AuthoringMandate(P8)` and emits artifacts.

---

## 2. The whole mandate in one call

A capability contract is a fixed pipeline with no iteration, so a step that rendered one artifact
could never render twenty-five. The iteration lives inside a pure transform, where it observes
nothing and decides nothing.

---

## 3. What is rendered, and what is not

**The Machine block.** It is what the compiler reads, the snapshot seals and the runtime executes.
An artifact's prose is human narrative that no register determines or should, and a generator that
authored prose would be writing documentation nobody committed to.

**Nothing is invented.** Every value comes from a register or a constitution-fixed default — an
intent's ACK/NACK, a family's `governed_by`, a workflow's structure. The completeness gate ahead of
this step is what guarantees there is nothing left to invent by the time it runs.

---

## Machine

```yaml
fqdn: transformation::CT_PURE_RENDER_ARTIFACTS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
core:
  summary: Render every artifact a mandate schedules from the design that determines it
  description: |
    Emits one entry per scheduled artifact, each carrying the path it belongs at and the Machine
    block that governs it. Raises when the mandate schedules nothing this design declares, because a
    construction that emits nothing is a reconciliation failure rather than an empty build.
  inputs:
    design_registers:
      type: array
      required: true
      description: Parsed P7 registers — the design semantics
    mandate_registers:
      type: array
      required: true
      description: Parsed P8 registers — the build order
  outputs:
    artifacts:
      type: array
      required: true
      description: One entry per artifact — path, domain, and the Machine block
    artifact_count:
      type: integer
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_RENDER_ARTIFACTS
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_render_artifacts_v0
    callable: execute
```
