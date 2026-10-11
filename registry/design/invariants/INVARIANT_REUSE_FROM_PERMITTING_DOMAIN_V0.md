# INVARIANT_REUSE_FROM_PERMITTING_DOMAIN_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_REUSE_FROM_PERMITTING_DOMAIN_V0
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

Reuse is offered only from a domain that permits it.

## 2. Why

A domain's artifacts are its own to change. Reusing one that does not offer reuse couples the change to a surface its owner may change at will.

## 3. How it is checked

A reuse candidate's domain is checked against what the pinned composition says that domain permits.
