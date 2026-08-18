# CT_PURE_MEASURE_COMPLETENESS_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_MEASURE_COMPLETENESS_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Measure whether a design uniquely determines the artifacts it specifies, and **refuse when it does
not**.

`UNIQUELY_DETERMINED_OR_STOP` is a rule, not a report. A fact the design does not state is a fact
construction would have to invent, and a generator that invents design is a second design authority
that no gate approved. So this transform raises rather than returning a low score, and the runtime
maps the raise to VIOLATION.

---

## 2. The requirement list is derived

What construction requires is the shape the renderer emits, walked leaf by leaf. It is not a
declared list, because a declared list is a second opinion about construction and drifts from it:
the hand-written version read 100% while the generator could reproduce one artifact in twenty-five,
having asked whether a contract declared a pipeline and never whether each step declared its store.

Derived, the same corpus requires **710** facts rather than 170.

---

## Machine

```yaml
fqdn: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
core:
  summary: Measure Construction Completeness and refuse a design that does not determine its artifacts
  refusal: raises
  description: |
    Derives the requirement list from the renderer, compares the design against it, and raises when
    completeness is below the declared threshold. A verdict of "complete" is an ordinary return; a
    refusal is an exception, because the CT status surface has exactly two outcomes and a refusal
    must not be indistinguishable from a low-but-passing score.
  inputs:
    design_registers:
      type: array
      required: true
      description: Parsed P7 registers — the design semantics
    mandate_registers:
      type: array
      required: true
      description: Parsed P8 registers — the build order
    threshold:
      type: number
      required: true
      description: Minimum Construction Completeness; 100 unless a caller deliberately relaxes it
  outputs:
    completeness:
      type: number
      required: true
    determined:
      type: integer
      required: true
    required:
      type: integer
      required: true
    undetermined:
      type: array
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_MEASURE_COMPLETENESS
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_measure_completeness_v0
    callable: execute
```
