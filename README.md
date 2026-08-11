# transformation

**The governed Change Request → Protocol Artifact pipeline.** A functional rehost of RI-0's
`pgs_change_mgmt` under pure PGC architecture.

A change begins as a plain-language problem statement and is driven through gated phases into an
**Authoring Mandate** — a complete, reviewable dossier — *before* any protocol artifact is written.
Only after the mandate is approved are artifacts authored, and the protocol compiler then governs
their admissibility.

```
problem statement → P0 → Gate 0 → seed → dossier P1..P7 → Gate 2 → authored artifacts
     → protocol_compiler S1..S9 → snapshot_assembler → conformance → runtime → trace
```

This pipeline is measured in **phases (P0–P7)**; `protocol_compiler` is measured in **stages
(S1–S9)**. RI-0 numbered both S1–S7/S1–S9, which made every piece of evidence ambiguous about which
pipeline produced it. A dossier has phases, a compilation has stages, and nothing uses one word for
the other.

## Build-time tool

`transformation` is **CLI only** — no TI/TE boundary contract, no Operation Identity, not
reachable over transport. A boundary contract governs a runtime surface served from a sealed
snapshot; this tool runs *before* a snapshot exists, its output is authored artifacts a human
gates, and its only reader is the person driving the change.

```bash
tc phase list                              # phases this build governs
tc phase check --phase p0 <seed.md>        # structural oracle — ADMISSIBLE / INADMISSIBLE
tc phase check --phase p1 <register.md>
tc phase check --phase p2 <register.md> --snapshot <root>   # grounds against the composition
tc phase template --phase p1               # the required section structure
tc phase rules --phase p1                  # the declared rule set
tc baseline verify <pin.json> --snapshot <root>
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
transformation           problem     → change request → authoring mandate   (this repo)
```

Every snapshot fact this pipeline needs arrives through
`inspector.api.query(operation, params, snapshot_root)`. It imports nothing from `compiler.*`.
RI-0's pipeline reached directly into `pgs_compiler.compiler.projections` to build indexes itself;
removing that coupling is why `snapshot_inspector` was completed first, and building this repo
without it is that work's acceptance test.

## Validation is pinned

Runs are validated against a **named, frozen snapshot**, never "the current snapshot" — every
register a snapshot-reading phase emits encodes facts about one specific composition. A run that
observes a different `snapshot_id` fails before any phase executes. Rebaselining is deliberate:
re-pin the id, re-approve the affected registers.

## Documents

- The composition runbook — clean-slate build and check, end to end, across every repo — is
  maintained with the release process rather than here, because it spans the whole composition.
  It carries the two loops this repo's contributors need: constructing a design into artifacts,
  and re-sealing a phase's rule set after changing it.
- `doc/TRANSFORMATION_COMPILER_PLAN_V1.md` — the rehost plan: what is being rehosted, the
  phase-by-phase validation methodology, and the settled rulings.
- `doc/TRANSFORMATION_COMPILER_PLAN_V1_ADDENDUM_A.md` — the release-4 subject: the
  `book_library_mgmt` domain, its decomposition, and the change request sequence.
- `doc/TRANSFORMATION_COMPILER_PLAN_V1_ADDENDUM_B.md` — self-hosting: why the pipeline's first
  governed change is itself, and what that settles.
- `templates/` — the phase templates. **These are the authority**: registers, columns, controlled
  vocabularies and optionality are read from them, and rule sets are derived. A shape declared
  anywhere else is not a template.
