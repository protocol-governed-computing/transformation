# INVARIANT_DESIGN_NAMES_RESOLVE_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_DESIGN_NAMES_RESOLVE_V0
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

Every name a design uses for something it declares resolves to exactly one declaration.

## 2. Why

A design names its own parts many times: a node by its key, a step by its owner, a test case by its transform. A name that resolves to nothing, or to two things, is a part construction cannot find or cannot choose.

## 3. How it is checked

References between registers resolve, a key names one row, a binding names a field its step declares, a contract's output is produced by a step, and a code agrees with the family it is filed under.
