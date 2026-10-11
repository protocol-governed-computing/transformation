# INVARIANT_RENDER_INVENTS_NOTHING_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_RENDER_INVENTS_NOTHING_V0
artifact_kind: INVARIANT
version: V0
governed_by: transformation::CONSTITUTION_BUILD_V0
authority: pgc.platform
concern: build
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the construction compiler, measuring each design it renders (CT_PURE_ATTRIBUTE_PROVENANCE_V0)
assert_projection:
  applies_to_kinds:
  - AC
  - CC
  - CT
  - EV
  - IN
  - RB
  - STRUCTURE
  - TEST_DATA
  - VOCAB
  - WF
```

---

## 1. Claim

Every rendered value is read from a register or is a default a constitution fixes.

## 2. Why

A value with no source in the design or in a constitution was invented by the renderer, and no gate saw it.

## 3. How it is checked

Enforced by the construction compiler: `CT_PURE_ATTRIBUTE_PROVENANCE_V0` runs on every design construction renders.
