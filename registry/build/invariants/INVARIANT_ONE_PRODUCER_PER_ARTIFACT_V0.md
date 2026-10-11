# INVARIANT_ONE_PRODUCER_PER_ARTIFACT_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_ONE_PRODUCER_PER_ARTIFACT_V0
artifact_kind: INVARIANT
version: V0
governed_by: transformation::CONSTITUTION_BUILD_V0
authority: pgc.platform
concern: build
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the construction compiler, when `tc construction check` measures a design
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

An artifact a generator writes is never also rendered.

## 2. Why

Two producers for one artifact are two designs of record. The one written last wins, and nothing says which that was.

## 3. How it is checked

Enforced by the construction compiler when `tc construction check` measures a design.
