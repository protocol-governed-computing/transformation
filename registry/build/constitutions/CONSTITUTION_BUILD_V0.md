# CONSTITUTION_BUILD_V0

## Machine

```yaml
fqdn: transformation::CONSTITUTION_BUILD_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: build
core:
  enforcement_model: compiler_enforced
  governs:
  - INVARIANT
rules:
- applies_to: DESIGN
  enforced_by: transformation::INVARIANT_DESIGN_UNIQUELY_DETERMINES_ARTIFACT_V0
- applies_to: DESIGN
  enforced_by: transformation::INVARIANT_RENDER_INVENTS_NOTHING_V0
- applies_to: DESIGN
  enforced_by: transformation::INVARIANT_ONE_PRODUCER_PER_ARTIFACT_V0
- applies_to: DESIGN
  enforced_by: transformation::INVARIANT_MEANING_CHANGE_IS_NEW_IDENTITY_V0
```

---

## 1. Construction determinacy

Construction renders the artifacts an admissible design schedules. It may render only what the design determines, and it stops rather than supply a fact the design does not state.
