# INVARIANT_BUILD_ORDER_TOPOLOGICAL_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_BUILD_ORDER_TOPOLOGICAL_V0
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

The mandate builds every dependency before its dependant, in contiguous steps.

## 2. Why

A build order that schedules a prerequisite later is a list, not a sequence anyone can execute, and the defect is invisible in either row alone.

## 3. How it is checked

Steps and the critical path are numbered without gaps, every dependency scheduled in the mandate comes earlier, and the critical path runs through scheduled steps.
