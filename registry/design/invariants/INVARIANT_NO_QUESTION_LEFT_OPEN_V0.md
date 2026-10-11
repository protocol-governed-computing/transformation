# INVARIANT_NO_QUESTION_LEFT_OPEN_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_NO_QUESTION_LEFT_OPEN_V0
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

No document leaves a governed hole, a blocking question or a business question open.

## 2. Why

An unanswered question is not a value. Left in a register it reads as determined to every later phase, which is how a design whose central question was never settled reached execution admissible at every gate.

## 3. How it is checked

No cell outside the registers that hold questions hedges its value, and no clarification marked blocking or owned by the business is handed on unanswered.
