# INVARIANT_ANNOUNCEMENT_FROM_COMPLETING_ENDING_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_ANNOUNCEMENT_FROM_COMPLETING_ENDING_V0
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

A moment is announced only from an ending that completes the act.

## 2. Why

An announcement from a refusing ending tells listeners that something happened when it did not.

## 3. How it is checked

Every emission names an ending the act's topology completes on, and an event the design declares.
