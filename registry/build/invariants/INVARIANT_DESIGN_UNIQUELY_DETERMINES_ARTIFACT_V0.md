# INVARIANT_DESIGN_UNIQUELY_DETERMINES_ARTIFACT_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_DESIGN_UNIQUELY_DETERMINES_ARTIFACT_V0
artifact_kind: INVARIANT
version: V0
governed_by: transformation::CONSTITUTION_BUILD_V0
authority: pgc.platform
concern: build
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the construction compiler, measuring each design it renders (CT_PURE_MEASURE_COMPLETENESS_V0)
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

A design states every fact construction renders, or construction stops.

## 2. Why

A fact construction supplies on its own is a decision nobody reviewed. Construction completeness must be total, or the artifact says something the design did not.

## 3. How it is checked

Enforced by the construction compiler: `CT_PURE_MEASURE_COMPLETENESS_V0` runs on every design construction renders.
