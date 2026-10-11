# INVARIANT_NEW_IDENTITY_UNUSED_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_NEW_IDENTITY_UNUSED_V0
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

An identity a design assigns as new names nothing the pinned composition holds.

## 2. Why

A new identity that already exists collides at compile, or silently redefines what another change delivered.

## 3. How it is checked

Every identity declared new is looked up in the pinned composition and refused when found.
