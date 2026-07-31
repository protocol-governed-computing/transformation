# Transformation Compiler — Plan V1

The functional rehost of `pgs_change_mgmt` as `transformation_compiler`, under pure PGC
architecture.

---

## 1. What is being rehosted

`pgs_change_mgmt` is a **governed SDLC change pipeline**: a plain-language problem statement is
driven through gated stages into an Authoring Mandate, and only then are protocol artifacts
written. Two tiers, two gates:

```
DOSSIER TIER
  Stage 1   Change Request         classification + problem / outcome / known facts
  Stage 2   Domain Model           confirm the semantic model AGAINST THE SNAPSHOT
  Stage 3   Analysis Loop          REUSE / EXTEND / AUTHOR_NEW decisions, by evidence
  Stage 4   Business Model         canonical hub, consolidating 1–3
  Stage 5   Business Intent        WHAT — scope, invariants, actions, provisional codes
  Stage 6   Governance Intent      WHERE — ownership, storage, cross-subdomain dependencies
  Stage 6b  Design Intent          HOW — binding FQDNs assigned to every new artifact
  Stage 7   Authoring Mandate      the build sequence (topological sort of the design)
            ══ Gate 2 ══
AUTHORING TIER
  author .md artifacts → compiler governs admissibility → runtime tests → manifest → closure
```

The name change is not cosmetic. **PGC evolution is never greenfield**: every change is a
transformation of an existing composition. `transformation_compiler` names what the tool does;
`change_mgmt` named the process it supports.

## 2. The validation methodology — endorsed

Executing a real use case and validating one stage at a time is the right approach, and should be
the release's governing method rather than a testing afterthought. Two refinements:

**Do not conflate two stage numberings.** The transformation compiler has dossier Stages 1–7; the
protocol compiler has S1–S9. They are different axes and a rehost that blurs them will produce
confusing evidence. The full chain is:

```
seed → dossier Stage 1..7 → Gate 2 → authored artifacts → protocol_compiler S1..S9
     → snapshot_assembler → composition conformance → runtime → trace
```

Validation is per **dossier stage** for the transformation compiler, and the *authored artifacts*
are then validated by the existing compiler pipeline, which already has its own gates.

**Golden fixtures must target the oracle, not the prose.** `pgs_change_mgmt` drives its stages with
LLM workers (`worker/claude.py`, `gemini.py`, `ollama_worker.py`). Worker output is not
byte-reproducible, so `stage_N_expected/` cannot be a byte diff of authored prose. What *is*
deterministic, and therefore what fixtures must pin, is the **structured register** each stage
emits and the **structural oracle** that validates it — well-formed FQDNs, controlled vocabularies,
traceability, cross-stage consistency. Pin the register rows and the oracle verdict; treat the
prose as evidence for a human gate, never as a test assertion.

## 3. Domain choice — where this plan differs

A small, real business domain (library management: Book, Borrower, Loan, Reservation) is the right
subject, and blockchain is correctly deferred: it would leave every failure ambiguous between "the
transformation compiler is wrong" and "blockchain is complicated."

But **one greenfield domain cannot validate a transformation compiler**, and the reason is
structural rather than a matter of taste. Read the pipeline's own stage definitions:

| Stage | Depends on an existing surface |
|---|---|
| Stage 2 — Domain Model | *"confirm the semantic model **against the snapshot**"* |
| Stage 3 — Analysis Loop | **REUSE / EXTEND** / AUTHOR_NEW, *by evidence* |
| Stage 6 — Governance Intent | ownership, storage, **cross-subdomain dependencies** |
| Stage 7 — Authoring Mandate | topological sort **over the composed graph** |

Against a blank slate every Stage-3 decision is `AUTHOR_NEW`; the REUSE and EXTEND branches never
execute. Of the four declared CR types — `NEW_SUBDOMAIN`, `EXTEND_SUBDOMAIN`, `MODIFY`,
`DEPRECATE` — only the first is reachable. The pipeline would run green while its distinguishing
logic sat unevaluated.

That is precisely the vacuity pattern this codebase has hit repeatedly: four profile invariants
unevaluated across two migrations, vocabulary rules silently skipped, `kind_index` cross-references
empty for a release. **A green result over an empty subject set is not evidence.** A greenfield
validation of a change compiler is that failure mode by construction — and it contradicts the
concept the rename exists to encode.

### The unit of validation is a CR sequence, not a domain

The minimum that exercises the tool is **four change requests against the release-3 composition**:

| CR | Type | What it forces |
|---|---|---|
| CR-1 | `NEW_SUBDOMAIN` | placement and ownership against 240 existing artifacts; Stage-3 **REUSE** of platform capabilities (`CS_MUTABLE_JSON_V0`, `CT_PURE_LOOKUP_V0`, …) rather than authoring new ones |
| CR-2 | `EXTEND_SUBDOMAIN` | Stage-3 **EXTEND**; semantic preservation and roundtrip equivalence now have a real baseline — CR-1's own output |
| CR-3 | `MODIFY` | changing declared behaviour: the immutable-version rule (`_V0 → _V1`) becomes load-bearing |
| CR-4 | `DEPRECATE` | retirement, supersession, and what happens to consumers of the retired artifact |

Note that **even CR-1 is not greenfield in PGC**. A new domain compiles against the platform's
normative closure (69 members) and composes into a snapshot of 240 artifacts, so Stage 2 and
Stage 3 have real content from the first CR. That is the "never greenfield" property in practice,
and it is why the library domain is a legitimate subject rather than a toy.

**One CR must be refused.** A fifth case — a change that violates a governance rule, e.g. a second
active `fb.security_domain` contract or an unauthorized vocabulary extension — proves the gates
bite. A pipeline that has never rejected anything has not demonstrated governance; it has
demonstrated transport.

## 4. The design question the rehost must answer first

`pgs_change_mgmt` drives its stages with LLM workers. PGC is deterministic and fail-hard. These
are not obviously compatible, and the rehost cannot proceed on an unstated answer.

The reconciliation the legacy design implies, and which the rehost should make explicit: **the
worker is assistive, the governance is structural.** What is governed is the register schema, the
structural oracle, the two gates and the mandate — all deterministic. What is assistive is the
prose a worker drafts to populate a register. A non-deterministic drafter behind a deterministic
oracle and a human gate is coherent; a non-deterministic *decision* inside a governed pipeline is
not.

Consequences to settle before building:

- Is a worker required at all, or is it one admissible way to populate a register that a human
  could equally fill by hand? (The seed mechanism suggests the latter — it exists precisely to
  stand in for the interactive elicitation.)
- Does the transformation compiler need a boundary contract (TI/TE) and an Operation Identity, as
  the inspector now has — or is it a build-time tool with a CLI only?
- Where do dossiers live? They are evidence about a composition, not part of it. They must not
  enter the snapshot as artifacts.

## 5. What the rehost must not replicate

`pgs_change_mgmt/engine/compilation_unit.py:382-383` imports `build_artifact_index` and
`build_store_index` directly from `pgs_compiler.compiler.projections` and builds the indexes
itself. That coupling is exactly what `snapshot_inspector` was built to remove, and the whole
reason inspection was completed before this rehost.

**Every snapshot fact the transformation compiler needs must come through
`inspector.api.query(operation, params, snapshot_root)`.** The legacy `PiClient` (345 lines, ~73
call sites) enumerates what is needed; all seven of its methods are now core operations. If a
stage needs a fact the inspector does not publish, the answer is a new `si.` operation — not a
reach into compiler internals.

This is also the acceptance test for the inspection work: if the rehost can be built without
importing `compiler.*`, the boundary was drawn correctly.

## 6. Sequence

1. **Settle §4** — the worker/governance split, the boundary question, dossier residency. These
   are rulings, not code.
2. **Stand up `transformation_compiler`** with the dossier register model, the structural oracle
   and the two gates. No worker yet — drive it from hand-authored seeds and registers, so the
   deterministic core is proven before anything non-deterministic is attached.
3. **CR-1 (`NEW_SUBDOMAIN`)** — the library domain, validated stage by stage against the release-3
   snapshot, then through `protocol_compiler` S1–S9, assembly, composition conformance and runtime.
4. **CR-2, CR-3, CR-4** — EXTEND, MODIFY, DEPRECATE, each against the composition the previous CR
   produced. This is where semantic preservation and roundtrip equivalence acquire meaning.
5. **CR-5 — the refusal.** A change that must be rejected, with the rejection recorded as evidence.
6. **Re-attach the worker** as an assistive drafter behind the now-proven oracle.
7. **Then blockchain**, as the scale test — a rich existing domain rehosted with no architectural
   change.

Steps 1–5 are the release-4 target. Step 7 is a later cycle, and it tests a different claim:
correctness first, scalability second, never both at once.

## 7. Fixtures

```
examples/
  01_library/
    seed.md                       the frozen elicitation
    cr_01_new_subdomain/
      stage_1..7_expected/        register rows + oracle verdict (NOT prose)
      mandate_expected.md
      authored_artifacts/
      compiled_expected/          S1–S9 evidence
      trace_expected/
    cr_02_extend_subdomain/
    cr_03_modify/
    cr_04_deprecate/
    cr_05_refused/                the rejection and its recorded cause
```

Every future change to the transformation compiler is then a regression run against a known-good
*evolution*, not a known-good snapshot. That distinction matters: a snapshot fixture proves the
tool can produce an output; an evolution fixture proves it can produce the right *change*.
