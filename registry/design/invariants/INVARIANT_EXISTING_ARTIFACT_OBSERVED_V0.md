# INVARIANT_EXISTING_ARTIFACT_OBSERVED_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_EXISTING_ARTIFACT_OBSERVED_V0
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

A claim about an existing artifact resolves in the pinned composition.

## 2. Why

An artifact named from memory may not exist, or may exist in another domain. Citing the baseline is observation, and an observation that cannot be repeated is not one.

## 3. How it is checked

Every identity a register claims exists is looked up in the composition the dossier is pinned to.
