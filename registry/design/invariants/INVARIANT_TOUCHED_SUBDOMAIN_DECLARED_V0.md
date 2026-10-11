# INVARIANT_TOUCHED_SUBDOMAIN_DECLARED_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_TOUCHED_SUBDOMAIN_DECLARED_V0
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

Every subdomain a change touches has its purpose stated, its owner declared, and what it authors named.

## 2. Why

A subdomain touched without a purpose, an owner or a scope is changed by nobody in particular, and the change cannot be reviewed against what that subdomain is for.

## 3. How it is checked

Each touched subdomain appears in the purpose, ownership and authoring registers, and a capability borrowed across a boundary is declared as a crossing.
