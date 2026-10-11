# INVARIANT_RESTATEMENT_MATCHES_SOURCE_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_RESTATEMENT_MATCHES_SOURCE_V0
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

A row citing an upstream row says what that row said.

## 2. Why

A citation carried forward over a changed claim is worse than a dropped row. The citation lends the substitution a provenance it does not have.

## 3. How it is checked

A restated row is compared with the row it cites, on the columns that carry the claim.
