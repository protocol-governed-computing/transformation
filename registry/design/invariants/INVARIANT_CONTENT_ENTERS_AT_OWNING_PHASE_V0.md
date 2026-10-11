# INVARIANT_CONTENT_ENTERS_AT_OWNING_PHASE_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_CONTENT_ENTERS_AT_OWNING_PHASE_V0
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

Content enters at the phase that owns it. A later phase restates and refines; it does not invent.

## 2. Why

Content invented downstream has no business statement behind it. It is design presented as requirement, and no gate before it was asked to approve it.

## 3. How it is checked

A row here that no upstream row states is refused where the phase only restates: a seed row in the change request, a refusal the business never declared, an artifact scheduled that no phase designed.
