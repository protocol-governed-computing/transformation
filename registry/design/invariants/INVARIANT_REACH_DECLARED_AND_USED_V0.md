# INVARIANT_REACH_DECLARED_AND_USED_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_REACH_DECLARED_AND_USED_V0
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

An act reads only what it declared a reach to, and uses every reach it declared.

## 2. Why

A read nobody declared couples an act to data it was never reviewed as depending on. A reach declared and never used is a dependency on paper only.

## 3. How it is checked

The reads a design's steps perform are compared with the reach it declares, in both directions.
