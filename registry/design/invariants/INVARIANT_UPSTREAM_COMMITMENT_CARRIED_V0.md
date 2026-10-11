# INVARIANT_UPSTREAM_COMMITMENT_CARRIED_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_UPSTREAM_COMMITMENT_CARRIED_V0
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

A commitment an earlier phase made is carried forward. None is silently dropped.

## 2. Why

A dropped commitment leaves a well-formed document. A change request missing an acceptance criterion reads as complete, and that criterion is what the finished composition is later validated against.

## 3. How it is checked

Rows of an upstream register reappear here, matched by citation, by key or by identity: beliefs, decisions, in-scope capabilities, designed artifacts, bindings and purpose.
