# RB_TRANSFORMATION_BINDINGS_V0

## Header (Mandatory)

- **Artifact Code:** RB_TRANSFORMATION_BINDINGS_V0
- **Artifact Kind:** runtime_binding
- **Governed By:** CONSTITUTION_RUNTIME_BINDING_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Runtime bindings for the transformation phase pipeline.

The seed phase has **no side effects and no storage**: it reads a document supplied as text and
returns a verdict. Nothing is persisted, so no capability side effect is bound. That emptiness is
declared rather than assumed — a phase that later needs to record a gate acceptance will bind its
host here, through a governed change.

---

## Machine

```yaml
fqdn: transformation::RB_TRANSFORMATION_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
core:
  summary: Runtime bindings for the transformation phase pipeline
  description: The seed phase is pure — it binds no side effect and persists nothing.
  bindings: {}

extensions:
  notes:
    - This artifact performs no discovery and no inference.
    - The seed phase reaches no host — it consumes supplied text and returns a verdict.
```
