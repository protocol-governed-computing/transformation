# INVARIANT_MEANING_CHANGE_IS_NEW_IDENTITY_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_MEANING_CHANGE_IS_NEW_IDENTITY_V0
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

An amendment that changes an artifact's meaning gives it a new identity.

## 2. Why

A pin names identities. An identity whose meaning changes in place silently changes what every pin naming it meant.

## 3. How it is checked

Enforced by the construction compiler when `tc construction check` measures a design.
