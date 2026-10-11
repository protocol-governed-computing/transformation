# INVARIANT_DECLARED_ARTIFACT_FULLY_STATED_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_DECLARED_ARTIFACT_FULLY_STATED_V0
artifact_kind: INVARIANT
version: V0
governed_by: transformation::CONSTITUTION_DESIGN_V0
authority: pgc.platform
concern: design
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the design compiler, evaluating each phase's sealed rule set over a phase document
assert_projection:
  applies_to_kinds:
  - WF
```

---

## 1. Claim

Every artifact a design declares carries every part its kind needs.

## 2. Why

A workflow without a topology, a transform without an implementation or a vector, or a contract without a composition is declared and cannot be built. The gap surfaces at construction, far from the register that left it.

## 3. How it is checked

For each declared artifact, the registers its kind needs hold a row for it.
