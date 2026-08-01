# Transformation Compiler — Plan V1

The functional rehost of `pgs_change_mgmt` as `transformation_compiler`, under pure PGC
architecture.

---

## 0. The claim

The release is not "change management, rehosted." It is the first demonstration of
**protocol-governed evolution**:

```
existing composition → transformation compiler → candidate evolution → governance → new composition
```

Ordinary SDLC tooling manages the *process* around a change. A transformation compiler takes a
composition as input and emits a governed successor composition, or refuses. That is the claim
release 4 must evidence — acceptance *and* refusal — and it is why the validation subject is a
change sequence rather than a domain.

## 1. What is being rehosted

`pgs_change_mgmt` is a **governed SDLC change pipeline**: a plain-language problem statement is
driven through gated phases into an Authoring Mandate, and only then are protocol artifacts
written. Three tiers, three gates:

```
SEED TIER
  P0    Business Problem Statement   human-authored prose → conformant seed
        ══ Gate 0 ══
DOSSIER TIER
  P1    Change Request        classification + problem / outcome / known facts
  P2    Domain Model          confirm the semantic model AGAINST THE SNAPSHOT
  P3    Analysis Loop         REUSE / EXTEND / AUTHOR_NEW decisions, by evidence
  P4    Business Model        canonical hub, consolidating P1–P3
  P5    Business Intent       WHAT — scope, invariants, actions, provisional codes
  P6    Governance Intent     WHERE — ownership, storage, cross-subdomain dependencies
  P7    Design Intent        HOW — binding FQDNs assigned to every new artifact
  P8    Authoring Mandate    the build sequence (topological sort of the design)
        ══ Gate 2 ══
AUTHORING TIER
  author .md artifacts → compiler governs admissibility → runtime tests → manifest → closure
```

**Phases, not stages.** The legacy pipeline numbered these S1–S7, colliding with the protocol
compiler's own S1–S9 — two different axes wearing the same labels, which makes every piece of
evidence ambiguous about which pipeline produced it. This rehost renames them **phases (P0–P8)**
and leaves **stages (S1–S9)** to `protocol_compiler`. The rule is mechanical: a dossier is measured
in phases, a compilation is measured in stages, and no document uses one word for the other.

The repo name change is not cosmetic either. **PGC evolution is never greenfield**: every change is
a transformation of an existing composition. `transformation_compiler` names what the tool does;
`change_mgmt` named the process it supports.

## 2. Phase 0 — the seed

The legacy pipeline began at S1 and consumed a hand-built elicitation document
(`1_input_elicitation_<domain>_<subdomain>_v0.md`). That document is already highly structured —
fourteen registers, a three-way split between Business Truths, System Beliefs and Clarifications —
and nothing in the pipeline says where it came from. In practice a human wrote it *and* silently
performed the classification the pipeline is supposed to govern.

P0 makes that step explicit and separates the two things it was conflating:

| | Input | Output | Nature |
|---|---|---|---|
| **P0** | `0_business_problem_statement.md` — free-form business prose, human-authored, assistance permitted | `0_seed_business_problem_statement.md` — template-conformant seed | faithful rewrite |
| **P1** | the seed | Change Request register | classification |

**P0's only obligation is faithfulness.** It reorganizes prose into the seed template; it must not
add business content, invent design, resolve a Clarification, or promote a System Belief to a
Business Truth. Everything the seed asserts must be traceable to a sentence in the problem
statement. Anything the problem statement leaves unsaid becomes a §14 Clarification Request, never
a filled-in guess. That is Gate 0: a human confirms the seed says what they meant, before any
governed phase consumes it.

The seed template is fixed by the legacy elicitation's section structure — Subdomain Purpose, CR
Type, Business Vocabulary, Requested Outcomes, Known Facts (Business Truths), Existing-System
Beliefs, Assumptions, Constraints, Business Invariants, Lifecycle States, Business Events,
Authority Boundaries, Out of Scope, Governance Scope, Clarification Requests, Acceptance Criteria.
`pgs_change_mgmt/.../blockchain/chain/1_input_elicitation_blockchain_chain_v0.md` is the reference
*instance* of that shape, not the subject: the release-4 seeds instantiate the template for
`book_library_mgmt` (Addendum A).

Two properties follow, both of which the plan needs:

- The **structural oracle applies at P0**, not from P1. A seed is admissible or it is not —
  required sections present, CR Type in the controlled vocabulary, every Belief carrying a
  Verification Goal, no Belief stated as a Fact. This is the deterministic core's first test, and
  it needs no snapshot access at all.
- P0 settles part of §5 by construction. The seed is *defined* as human-authored, so the worker
  question narrows: a worker may draft the seed, but Gate 0 makes a human its author of record. The
  pipeline never depends on a worker existing.

## 3. The validation methodology — endorsed

Executing a real use case and validating one phase at a time is the right approach, and should be
the release's governing method rather than a testing afterthought. Two refinements:

**Keep the two axes separate.** With the phase/stage rename (§1) the naming collision is gone; what
remains is to keep the *evidence* separate. The full chain is:

```
problem statement → P0 → Gate 0 → seed → dossier P1..P8 → Gate 2
     → authored artifacts → protocol_compiler S1..S9
     → snapshot_assembler → composition conformance → runtime → trace
```

Validation is per **dossier phase** for the transformation compiler, and the *authored artifacts*
are then validated by the existing compiler pipeline, which already has its own gates.

**Golden fixtures must target the oracle, not the prose.** `pgs_change_mgmt` drives its phases with
LLM workers (`worker/claude.py`, `gemini.py`, `ollama_worker.py`). Worker output is not
byte-reproducible, so `p<N>_expected/` cannot be a byte diff of authored prose. What *is*
deterministic, and therefore what fixtures must pin, is the **structured register** each phase
emits and the **structural oracle** that validates it — well-formed FQDNs, controlled vocabularies,
traceability, cross-phase consistency. Pin the register rows and the oracle verdict; treat the
prose as evidence for a human gate, never as a test assertion.

## 4. Domain choice — where this plan differs

A small, real business domain (library management — fixed as `book_library_mgmt` in Addendum A) is
the right subject, and blockchain is correctly deferred: it would leave every failure ambiguous between "the
transformation compiler is wrong" and "blockchain is complicated."

But **one greenfield domain cannot validate a transformation compiler**, and the reason is
structural rather than a matter of taste. Read the pipeline's own phase definitions:

| Phase | Depends on an existing surface |
|---|---|
| P2 — Domain Model | *"confirm the semantic model **against the snapshot**"* |
| P3 — Analysis Loop | **REUSE / EXTEND** / AUTHOR_NEW, *by evidence* |
| P6 — Governance Intent | ownership, storage, **cross-subdomain dependencies** |
| P8 — Authoring Mandate | topological sort **over the composed graph** |

Against a blank slate every P3 decision is `AUTHOR_NEW`; the REUSE and EXTEND branches never
execute. Of the four declared CR types — `NEW_SUBDOMAIN`, `EXTEND_SUBDOMAIN`, `MODIFY`,
`DEPRECATE` — only the first is reachable. The pipeline would run green while its distinguishing
logic sat unevaluated.

That is precisely the vacuity pattern this codebase has hit repeatedly: four profile invariants
unevaluated across two migrations, vocabulary rules silently skipped, `kind_index` cross-references
empty for a release. **A green result over an empty subject set is not evidence.** A greenfield
validation of a change compiler is that failure mode by construction — and it contradicts the
concept the rename exists to encode.

### The unit of validation is a CR sequence, not a domain

The minimum that exercises the tool is a **sequence of change requests against the release-3
composition**, each one taking as its baseline the composition the previous CR produced:

| CR | Type | What it forces |
|---|---|---|
| CR-1 | `NEW_SUBDOMAIN` | placement and ownership against 249 existing artifacts; P3 **REUSE** of platform capabilities (`CS_MUTABLE_JSON_V0`, `CT_PURE_LOOKUP_V0`, …) rather than authoring new ones |
| CR-2 | `EXTEND_SUBDOMAIN` | P3 **EXTEND vs AUTHOR_NEW**; semantic preservation and roundtrip equivalence now have a real baseline — CR-1's own output |
| CR-3 | `NEW_SUBDOMAIN` | REUSE of **business entities across subdomains**, not just platform capabilities; P6's first real cross-subdomain dependency; a P8 sort spanning subdomains |
| CR-4 | `MODIFY` | changing declared behaviour: the immutable-version rule (`_V0 → _V1`) becomes load-bearing |
| CR-5 | `DEPRECATE` | retirement, supersession, and consumer migration — against consumers an earlier CR actually built |
| CR-6 | *refused* | the gates bite; the rejection and its cause recorded as evidence |

`NEW_SUBDOMAIN` appears twice on purpose: CR-1 exercises reuse of the platform surface, CR-3
exercises reuse of business entities authored by a previous CR. They are different paths, and the
second is the stronger claim.

The subject that instantiates this sequence — the `book_library_mgmt` domain, its decomposition,
and the CR-1 problem statement — is fixed in **Addendum A**.

Note that **even CR-1 is not greenfield in PGC**. A new domain compiles against the platform's
normative closure (69 members) and composes into a snapshot of 249 artifacts, so P2 and P3 have
real content from the first CR. That is the "never greenfield" property in practice, and it is why
the library domain is a legitimate subject rather than a toy.

**One CR must be refused.** CR-6 — a change that violates a governance rule, e.g. a duplicate
active authority or an unauthorized vocabulary extension — proves the gates bite. A pipeline that
has never rejected anything has not demonstrated governance; it has demonstrated transport.

### The CR taxonomy is not closed

The four types above are what release 4 must reach. They are not the whole space. The
`ai_governance` migration already performed an operation none of them names: two subdomains
consolidated into one namespace with a fork deleted — a **MERGE_SUBDOMAIN**, with
**SPLIT_SUBDOMAIN** as its inverse (and the `platform` → `software_governance` +
`conformance_workloads` split as its precedent). Both are transformations ordinary SDLC tooling has
no concept of, and both are natural extensions of this taxonomy.

They are **out of scope for release 4** — deliberately. But the register model and the CR-type
vocabulary should be authored so that adding a type is a vocabulary extension, not a redesign.

## 5. The design questions, settled

`pgs_change_mgmt` drives its phases with LLM workers. PGC is deterministic and fail-hard. These
are not obviously compatible, and the rehost cannot proceed on an unstated answer.

The reconciliation the legacy design implies, and which the rehost makes explicit: **the worker is
assistive, the governance is structural.** What is governed is the register schema, the structural
oracle, the gates and the mandate — all deterministic. What is assistive is the prose a worker
drafts to populate a register. A non-deterministic drafter behind a deterministic oracle and a
human gate is coherent; a non-deterministic *decision* inside a governed pipeline is not.

The three consequences, ruled:

**Is a worker required?** No. **P0 settles it**: the problem statement is human-authored by
definition and Gate 0 makes a human the seed's author of record, so no phase may depend on a worker
existing.

**Boundary contract or CLI?** **CLI only.** The transformation compiler is a build-time tool. It
gets no TI/TE boundary contract and no Operation Identity, and it is not reachable over transport.

The reason is not convenience. A boundary contract governs a *runtime* surface — something a
sealed snapshot serves to a caller it does not control. The transformation compiler is the opposite
end of the lifecycle: it runs before a snapshot exists, its output is authored artifacts a human
gates, and its only reader is the person driving the change. Giving it an Operation Identity would
assert it is part of the executable composition, which is exactly the confusion "dossiers are
evidence, not artifacts" exists to prevent. Transport stays reserved for `si.*` inspection and
runtime execution.

**Where do dossiers live?** Outside the snapshot, always. They are evidence *about* a composition,
never part of one. Generated dossiers are gitignored; authored dossiers live in `cr_dossiers/`
in the repo of the domain they change, and are tracked there.

### The baseline is pinned

Every CR **SHALL** identify the baseline composition it is validated against — a named, frozen
snapshot, never "the current snapshot".

Every register a snapshot-reading phase emits encodes facts about one specific composition: which
artifacts exist, what the normative closure contains, what a REUSE decision found. Against a moving
snapshot those fixtures fail for reasons unrelated to the transformation compiler, and a regression
becomes indistinguishable from a rebuild.

A run that observes a snapshot other than the one its CR pins **fails before executing a phase**.
Rebaselining is a deliberate, reviewed act that re-pins the identity and re-approves the affected
registers — never a silent drift. Each CR after the first pins the composition its predecessor
produced, by the same rule.

**The pin's value lives in `baseline.json`, in the CR's own dossier — and nowhere else.** This
document states the rule; it does not carry the value. Three layers, and each does exactly one job:

```
this plan          states the rule       every CR pins a baseline
baseline.json      holds the values      snapshot_id, artifact count, domain list
compiler/runtime   enforces the values   a mismatched snapshot halts the run
```

A value restated in prose is a value nothing verifies. Once it drifts, the document that is
supposed to govern the work is the thing misleading it — which is the failure mode this section
exists to prevent, applied to itself.

    tc baseline verify <dossier>/baseline.json --snapshot <snapshot-root>

## 6. What the rehost must not replicate

`pgs_change_mgmt/engine/compilation_unit.py:382-383` imports `build_artifact_index` and
`build_store_index` directly from `pgs_compiler.compiler.projections` and builds the indexes
itself. That coupling is exactly what `snapshot_inspector` was built to remove, and the whole
reason inspection was completed before this rehost.

**Every snapshot fact the transformation compiler needs must come through
`inspector.api.query(operation, params, snapshot_root)`.** The legacy `PiClient` (345 lines, ~73
call sites) enumerates what is needed; all seven of its methods are now core operations. If a phase
needs a fact the inspector does not publish, the answer is a new `si.` operation — not a reach into
compiler internals.

This is also the acceptance test for the inspection work: if the rehost can be built without
importing `compiler.*`, the boundary was drawn correctly.

## 7. Sequence

1. **§5 is settled** — worker assistive not required, CLI only, dossiers outside the snapshot,
   baseline pinned. Rulings, not code; recorded so the build does not reopen them.
2. **Fix the P0 seed template and its genesis oracle.** No snapshot access, no registers
   downstream — the smallest deterministic surface in the tool, and the one every later phase reads
   from.
3. **CR-0 — the compiler authors itself.** The phases are governed artifacts (`IN_`, `WF_`, `CC_`,
   `CT_`, `RB_`, `AC_`), authored by a change request the genesis oracle drives, then compiled and
   run. The Python implementation is retained as a differential conformance check, not as the
   product. **Addendum B.**
4. **Stand up the remaining phases** with the dossier register model and the gates. No worker yet —
   drive them from hand-authored problem statements and registers, so the deterministic core is
   proven before anything non-deterministic is attached.
5. **CR-1 (`NEW_SUBDOMAIN`)** — `book_library_mgmt/catalog`, validated phase by phase against the
   release-3 snapshot, then through `protocol_compiler` S1–S9, assembly, composition conformance
   and runtime.
6. **CR-2 … CR-5** — EXTEND, the second NEW_SUBDOMAIN, MODIFY, DEPRECATE, each against the
   composition the previous CR produced. This is where semantic preservation and roundtrip
   equivalence acquire meaning.
7. **CR-6 — the refusal.** A change that must be rejected, with the rejection recorded as evidence.
8. **Re-attach the worker** as an assistive drafter behind the now-proven oracle.
9. **Then blockchain**, as the scale test — a rich existing domain rehosted with no architectural
   change.

Steps 1–7 are the release-4 target. Step 9 is a later cycle, and it tests a different claim:
correctness first, scalability second, never both at once.

## 8. Fixtures

```
<domain repo>/cr_dossiers/
  cr_NN_<subject>/
    baseline.json                             pinned snapshot_id — checked before any phase runs
    p0_business_problem_statement.md          human-authored prose — the P0 input
    p0_seed_<domain>_<subdomain>_v0.md        the frozen seed — P0 output, P1 input
    p1..p7_<domain>_<subdomain>_v0.md         the register documents each phase emits
    p0_expected/                              seed oracle verdict + faithfulness trace
    p1..p7_expected/                          register rows + oracle verdict (NOT prose)
    mandate_expected.md
    authored_artifacts/
    compiled_expected/                        S1–S9 evidence
    trace_expected/
  cr_02_extend_subdomain_catalog/
  cr_03_new_subdomain_circulation/
  cr_04_modify/
  cr_05_deprecate/
  cr_06_refused/                              the rejection and its recorded cause
```

Each CR carries its own problem statement and seed: a CR sequence is a sequence of *changes*, and
CR-2's seed is written against the composition CR-1 produced, not against the original one.

Every future change to the transformation compiler is then a regression run against a known-good
*evolution*, not a known-good snapshot. That distinction matters: a snapshot fixture proves the
tool can produce an output; an evolution fixture proves it can produce the right *change*.
