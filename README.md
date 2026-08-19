# transformation

**The governed Change Request → Protocol Artifact pipeline**, and it holds **two compilers**.

| Compiler | Transforms | Code | Registry |
|---|---|---|---|
| **Design** | problem → design | `transformation/design/` | `registry/design/` |
| **Construction** | design → protocol artifacts | `transformation/build/` | `registry/build/` |

They are two because they fail differently. A *design* failure is a mandate that is incomplete or
contradictory, and a phase's rule set catches it. A *construction* failure is a mandate that was
valid and did not uniquely determine an artifact — only the thing that renders can expose that, and
the repair amends the design language rather than one register. Merging them would blur two failure
classes that different layers repair.

The repository is named for the lifecycle, not for either compiler. **`transformation` is not a
third compiler.** A functional rehost of RI-0's `pgs_change_mgmt`, extended well past where RI-0
stopped.

A change begins as a plain-language problem statement and is driven through gated phases into an
**Authoring Mandate** — a complete, reviewable dossier — *before* any protocol artifact is written.
Only after the mandate is approved are artifacts authored, and the protocol compiler then governs
their admissibility.

```
problem statement → P0 → Gate 0 → seed → dossier P1..P7 → Gate 1 → P8 → Gate 2
     → construction → authored artifacts
     → protocol_compiler S1..S9 → snapshot_assembler → conformance → runtime → trace
```

This pipeline is measured in **phases (P0–P8)**; `protocol_compiler` is measured in **stages
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
tc phase project <prior.md> --phase p1 --out <doc.md>       # phases that decide nothing

tc phase meta                              # do the rule sets themselves hold?
tc phase emit --check                      # are the sealed workflows current?

tc baseline show --snapshot <root>                 # the composition present, as a pin
tc baseline verify <pin.json> --snapshot <root>
tc baseline approve <pin.json> --phase p2 --by <who>

tc construction check <dossier> --snapshot <root>   # does the design determine its artifacts?
tc construction emit  <dossier> --root <domain>     # render them, at 100% or not at all
```

Two of these judge the pipeline rather than a dossier. `tc phase meta` asserts that every declared
rule can run and every implemented mechanism is declared — if that correspondence breaks, a verdict
over a document is meaningless, because a rule that cannot run reports green over a subject it never
evaluated. `tc phase emit --check` asserts the sealed copy of a rule set still agrees with the
generator that produces it; a rule added after a workflow was emitted once left 52 rules sealed
against 55 declared, and every run reported confidently on the smaller set. Both belong in a build.

`tc construction check` measures **determinacy** before anything is written: the fraction of the
facts the artifacts require that the design determines. Below 100% nothing is emitted, because a
generator choosing a value it was not given is a generator inventing one.

## The two loops

`$W` is the workspace root holding the sibling repos.

**After editing a dossier's P7 or P8** — skipping a step leaves the snapshot describing a design that
no longer exists:

```bash
D=$W/business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog

tc construction check $D --snapshot $W/snapshot
tc construction emit  $D --root $W/business_domains/book_library_mgmt

python $W/transformation/scripts/testbed/construction_acceptance.py
$W/protocol_compiler/compile_domain.sh $W/business_domains/book_library_mgmt
$W/snapshot_assembler/assemble.sh
```

`--snapshot` on the check is not optional in practice. Completeness never looks at what already
exists, so an artifact inventoried `EXTEND` is rendered whole and replaces its predecessor — a design
stating only the delta deletes the rest, at 100% completeness. The flag is what runs the narrowing
check; without it that check does not run, and says so.

Construction writes into `data/`, never into the domain. **Promotion is a separate, deliberate act.**
A `tc construction build` CLI existed once and was removed, because it duplicated a governed path
with an ungoverned one.

A new capability transform is a protocol artifact *and* a Python implementation. Construction renders
the first; the second is hand-authored at
`business_domains/<domain>/implementation/capability_transforms/atoms/<code_lower>.py` with a
callable `execute(inputs, context)` raising `CTExecutionError`. A CT whose module is missing returns
nothing and its contract yields `VIOLATION` — while every check above still passes.

**After changing a phase's rule set** — the rules are declared in
`transformation/design/<phase>/rules.py` and *sealed* into that phase's workflow artifact. Editing
the declaration alone leaves `tc phase check` and the governed workflow evaluating different rule
sets:

```bash
tc phase emit --check                                  # names the drifted phase
python $W/transformation/scripts/emit_rule_sets.py     # re-seal
$W/protocol_compiler/compile_domain.sh $W/transformation
$W/snapshot_assembler/assemble.sh
python $W/transformation/scripts/testbed/build_fixtures.py
python $W/transformation/scripts/testbed/build_payloads.py
```

Fixtures and payloads are **derived from the live dossier** — never hand-edit one; change the dossier
or the mutator in `build_fixtures.py`. A derived fixture cannot go stale silently, because the
derivation raises rather than producing a wrong one.

The fast inner loop is `python scripts/testbed/differential.py`, which drives the capability
transforms directly. It proves the rule sets and the check logic and nothing about workflow wiring;
`scripts/testbed/e2e_phases_test.py` boots the assembled snapshot and proves the wiring. Neither
substitutes for the other — a workflow that bound `$.capability_result.header` across nodes passed
the differential and failed immediately under the runtime.

From P2 a phase also needs its **priors**, or the handoff between phases goes unchecked:
P1←p0 · P2←p1 · P3←p2 · P4←p3 · **P5←p0** · P6←p5 · P7←p5+p6 · P8←p7. P5 reads the seed, not P4: the
subdomain purpose is authored once at P0, has no register to travel in through P1–P4, and reappears
at P5.

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
observes a different `snapshot_id` fails before any phase executes.

Rebaselining is deliberate and has two halves. `tc baseline verify` proves the composition is the
one named; `tc baseline approve` records that someone re-read the registers asserting facts about
it. Which registers a phase owes is derived from its rule set — a register rests on a snapshot fact
exactly when a rule governing it consults an observation. The approval lives in the pin, so re-pinning
drops it: an approval is against one composition and survives no other.

## Documents

- `doc/THE_SHAPE_OF_A_CHANGE_V0.md` — when a subject is a new change request and when it is the
  same one re-authored, and which artifacts a governance change may amend.
- `doc/TRANSFORMATION_COMPILER_PLAN_V1_ADDENDUM_A.md` — the `book_library_mgmt` domain, its
  decomposition, and the change request sequence it is worked through.
- `doc/TRANSFORMATION_COMPILER_PLAN_V1_ADDENDUM_B.md` — self-hosting: why the pipeline's first
  governed change is itself, and what that settles. Plan V1 itself has been removed; the addenda are
  what survives, and a settled ruling is restated where it is needed rather than by restoring the
  plan.
- `doc/REGISTER_COVERAGE_VERIFICATION.md` — whether a design can state, for an artifact it amends,
  every fact that artifact carries. Four observed instances of one pattern: a fact the authoring
  path never had to state because authoring supplies it, and the amending path must state and
  cannot.
- `templates/` — the phase templates. **These are the authority**: registers, columns, controlled
  vocabularies and optionality are read from them, and rule sets are derived. A shape declared
  anywhere else is not a template.
