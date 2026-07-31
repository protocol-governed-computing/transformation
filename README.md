# transformation_compiler

**The governed Change Request → Protocol Artifact pipeline.** A functional rehost of RI-0's
`pgs_change_mgmt` under pure PGC architecture.

A change begins as a plain-language problem statement and is driven through gated stages into an
**Authoring Mandate** — a complete, reviewable dossier — *before* any protocol artifact is written.
Only after the mandate is approved are artifacts authored, and the protocol compiler then governs
their admissibility.

```
seed → dossier Stage 1..7 → Gate 2 → authored artifacts
     → protocol_compiler S1..S9 → snapshot_assembler → conformance → runtime → trace
```

## Why "transformation", not "change management"

**PGC evolution is never greenfield.** Every change is a transformation of an existing composition:
a new domain still compiles against the platform's normative closure and composes into a snapshot
that already exists. The name states what the tool does; `change_mgmt` named the process around it.

That property is also what makes the tool testable. Its distinguishing logic — REUSE / EXTEND
decisions, placement, ownership, semantic preservation, roundtrip equivalence — is meaningful only
against a baseline. A greenfield run exercises none of it.

## Relationship to the rest of the toolchain

```
protocol_compiler       source      → compiled projections
snapshot_assembler      projections → assembled snapshot
protocol_runtime        snapshot    → execution
snapshot_inspector      snapshot    → inspection
transformation_compiler problem     → change request → authoring mandate   (this repo)
```

Every snapshot fact this pipeline needs arrives through
`inspector.api.query(operation, params, snapshot_root)` across a governed Operation Identity
boundary. It imports nothing from `compiler.*`. RI-0's pipeline reached directly into
`pgs_compiler.compiler.projections` to build indexes itself; removing that coupling is why
`snapshot_inspector` was completed first, and building this repo without it is that work's
acceptance test.

## Documents

- `doc/TRANSFORMATION_COMPILER_PLAN_V1.md` — the rehost plan: what is being rehosted, the
  stage-by-stage validation methodology, the domain choice, and the rulings needed before code.
