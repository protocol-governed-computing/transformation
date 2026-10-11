# INVARIANT_PHASE_SPEAKS_ITS_RUNG_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_PHASE_SPEAKS_ITS_RUNG_V0
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

A phase uses only the vocabulary its rung admits.

## 2. Why

Each phase answers one question. A phase that names artifacts, bindings or paths before its rung admits them answers the next phase's question early, and nothing reviews that answer where it belongs.

## 3. How it is checked

Business-language columns name no compiled artifact, an intent states no binding, and a placement names no provisional or storage code.
