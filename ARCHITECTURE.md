# Architecture — `transformation`

**Release 5.** This document is frozen for this release. It describes what this repository is, what
it owns, and what it must never do. It is written to be read before any code, and assumes no prior
familiarity with Protocol-Governed Computing.

For the big picture — what PGC is and how the repositories compose — see
**https://github.com/protocol-governed-computing**.

---

## 1. What this repo is

This is how the system **changes**. Everything else in the composition governs what the system does;
this governs how it becomes something else.

> A change begins as a sentence someone in the business says, and ends as artefacts that compile.
> This repository is the graded path between those two things, and it refuses to let a step be
> skipped.

It holds two compilers. The first drives a problem statement through gated phases until it becomes
an **authoring mandate** — a design complete enough to build from. The second measures whether that
mandate actually determines the artefacts it schedules, and then writes them.

**What this repo is not.** It is not a project-management tool, not a document generator, and not
part of the running system. It executes before a snapshot exists, its output is authored artefacts a
human approves, and its only reader is the person driving the change.

## 2. Where it sits

```
                    ┌──────────────────────────────────────────┐
                    │  transformation      ← YOU ARE HERE      │
   a business       │                                          │     artefacts
   problem  ───────▶│   design/   problem  → mandate           │───▶  in a domain
   in prose         │   build/    mandate  → artefacts         │      repository
                    └──────────────────┬───────────────────────┘             │
                                       │ reads facts about                   │
                                       │ the current system                  ▼
                              snapshot_inspector              compiler → assembler
                                       ▲                                     │
                                       └──────── sealed snapshot ◀───────────┘
```

Note the loop. The mandate is judged against the snapshot the system currently *is*; the artefacts it
produces are compiled into the snapshot the system will *become*. **Evolution is never greenfield**
— even a brand-new domain compiles against a normative closure that already exists.

That is not a philosophical point. The pipeline's distinguishing logic — whether to reuse or extend,
where something belongs, who owns it, whether meaning was preserved — is only meaningful against a
baseline. A greenfield run leaves all of it unevaluated *while reporting success*.

## 3. The central idea: the language widens as you descend

The distinction that explains every design choice in this repository:

```
   PHASE                     VOCABULARY ADMITTED               so that…

   p0  change seed      ┐
   p1  change request   │
   p2  domain model     ├──▶  business language only     the business can read and
   p3  analysis loop    │                                correct its own problem
   p4  business model   ┘
   ─────────────────────────────────────────────────────────────────────────────
   p5  business intent  ────▶  + provisional names       WHAT must be true
   p6  governance intent ───▶  + placement               WHERE it belongs
   p7  design intent    ────▶  + bindings, paths, FQDNs  HOW it is realised
   p8  authoring mandate ───▶  + build order             IN WHAT ORDER
```

Each phase admits a strictly wider vocabulary than the one before, and **nothing may be said early
that belongs late**. A problem statement containing a module path has already decided the design
before anyone examined the problem — and the phase's rule set refuses it. Nine phases, 751 declared
rules, all of them checkable.

Two gates are human, and only two: **Design Approval** after p7, and **Mandate Approval** after p8,
at which point the dossier is locked.

### Why two compilers rather than one

They are separate **because they fail differently**:

| | failure reads as | fixed by |
|---|---|---|
| **Design Compiler** | *the mandate is incomplete or contradictory* | re-authoring a register |
| **Construction Compiler** | *the mandate was valid and did not determine an artefact* | amending the design language |

Different people fix those, and merging the compilers would blur the two into "it didn't work".

## 4. What it owns, and what it must never do

**It owns:**

- **the phase rule sets** — what each phase's document must contain and what it may not say yet;
- **the structural oracle** — the deterministic judge that renders a verdict on a document;
- **the pinned baseline** — the named, frozen snapshot every claim is verified against;
- **construction completeness** — the measurement of whether a design determines its artefacts;
- **emission** — writing the artefacts a mandate schedules into the domain that owns them.

**It must never:**

- **reach into the compiler.** Every fact about a snapshot arrives through the inspector's query
  interface. If a phase needs a fact the inspector does not publish, the answer is a **new inspection
  operation** — never a private index built from compiler internals. Building this repository without
  a compiler import is the acceptance test for that whole separation.
- **be reachable over transport.** No boundary contract, no operation identity, CLI only. An
  operation identity would assert this tool is part of the executable composition, which is exactly
  what "dossiers are evidence, not artefacts" exists to prevent.
- **put a dossier in a snapshot.** A dossier describes a change to a composition; it is not part of
  one.
- **own the dossiers it judges.** A dossier lives with the domain it changes, in that domain's
  repository. The pipeline judges; it does not collect.
- **let a decision be non-deterministic.** A worker may *draft* prose into a register. The schema,
  the oracle, the gates and the mandate *decide*, and they are deterministic. No phase may depend on
  a worker existing.

## 5. Try it — watch a document be judged

Two commands, no prior knowledge. First, see the pipeline itself:

```bash
cd transformation
python -m transformation phase list
```

Every phase prints what it is for, how many rules it declares, what vocabulary it admits, and its
one governing rule. Now judge a real document against phase 1's 189 rules:

```bash
python -m transformation phase check --phase p1 \
    dossiers/new_subdomain/p1_change_request_transformation_phases_v0.md \
    --snapshot ../snapshot
```

```
Status            INADMISSIBLE
  34 finding(s) over 189 declared rules
  [ROW_NOT_IN_SEED] identity_and_sameness: p0 was not supplied — this handoff is
  unchecked, and an unchecked handoff looks identical to a preserved one
```

The document is fine. **The check is incomplete**, and it says so rather than passing. Supply the
phase it descends from and run it again:

```bash
python -m transformation phase check --phase p1 <same document> \
    --snapshot ../snapshot --prior p0=dossiers/new_subdomain/p0_seed_transformation_phases_v0.md
```

```
ADMISSIBLE  [p1]
  0 finding(s) over 189 declared rules
  Figure of Merit   ★★★★☆ 4/5   (-1 open questions)
  Ready for P2      YES
```

### What just happened, and why it is the whole idea

The 34 findings were not complaints about content. They were **refusals to certify a handoff nobody
could see** — every row that claims to carry something forward from p0 was unverifiable without p0.
A pipeline that had shrugged and passed would have produced exactly the same verdict for a document
that quietly dropped half its problem statement.

Notice too that the verdict is not a boolean. `ADMISSIBLE` is the gate; the **figure of merit** is a
separate judgement of quality, and this document is admissible while still carrying an open question.
Admissibility and excellence are different questions, and conflating them makes one of them useless.

### Then look at the other end

```bash
python -m transformation baseline show --snapshot ../snapshot
python -m transformation construction check <a dossier with a p7>
```

`baseline show` prints the composition as a pin — an identity hash, an artefact count, the domains
present. `construction check` measures whether a design determines its artefacts, and the default
threshold is **100**:

> A fact the design does not state is a fact the generator would have to invent, and a generator that
> invents design is a second, ungoverned design authority.

Anything below 100 is a refusal, not a warning.

## 6. The baseline is pinned, and stays pinned

Validation never runs against "the current snapshot". It runs against a **named, frozen** one, and a
run that observes a different identity **fails before executing a phase**.

**The pin lives with the change, not with this repository** — each dossier carries its own, and each
change pins the composition its predecessor produced. A completed change is never re-pinned forward:
approving a register against a composition that arrived later asserts a re-reading of facts the build
already settled. An in-flight change is different and may legitimately re-pin.

Rebaselining is a deliberate, reviewed act — re-pin the identity, re-approve the affected registers.
Never a silent drift, because otherwise **a regression is indistinguishable from a rebuild**.

## 7. Phases, never stages

A dossier has **phases** (p0–p8). A compilation has **stages** (S1–S9). No document, path, register
field or identifier uses one word for the other.

This looks like pedantry and is not. The earlier implementation numbered its dossier phases S1–S7,
colliding with the compiler's own S1–S9, and every piece of evidence became ambiguous about which
pipeline produced it. A word that names two things names neither.

## 8. Layout

```
transformation/
    cli.py                the command surface: phase · construction · baseline
    baseline.py           the pin, and verification against it
    design/               the Design Compiler
        p0_change_seed/ … p8_authoring_mandate/    one package per phase
        rules.py  oracle.py  checks.py             the deterministic judge
        derive.py project.py evaluate.py merit.py  projection and figure of merit
    build/                the Construction Compiler
        completeness.py   does this design determine its artefacts?
        render.py         write them

templates/                the required section structure, one per phase
registry/                 this repo's own governance artefacts — design/ and build/
                          are compiled subdomains, like any domain's
dossiers/                 this repo's own authored dossiers
doc/                      the phase definitions and the compiler plan
```

`registry/` deserves a second look: **this repository is itself a compiled domain.** The lifecycle
that governs change is declared in the same artefact language as the businesses it governs.

## 9. Rules this repo enforces

1. **Each phase admits a strictly wider vocabulary than the last**, and nothing may be said early
   that belongs late.
2. **A run fails before executing a phase** if the snapshot on disk is not the pinned baseline.
3. **Every snapshot fact arrives through the inspection interface.** No compiler import, ever.
4. **Dossiers are evidence, not artefacts** — they never enter a snapshot.
5. **A dossier lives with the domain it changes**, never centralised here.
6. **Decisions are deterministic**; only drafting may be assistive, and no phase depends on a worker.
7. **Construction completeness below 100 is a refusal**, because the gap would be filled by
   invention.
8. **Phases are never called stages.**
9. **The tool has no transport surface.** CLI only.

## 10. How to know it works

```bash
python -m transformation phase meta          # the rule sets checked against themselves
python -m transformation phase list          # every phase, with its declared rule count
```

`phase meta` is the one to trust. It verifies the **rules themselves** rather than any document —
that every declared rule resolves to a check that exists, and that every check is declared. A good
result reads:

```
CONSISTENT — 751 rules across 9 phases resolve against 42 check kinds
```

A pipeline whose rules are not themselves checkable is a pipeline that can quietly stop enforcing
something. Beyond that, the test suite drives complete dossiers through every phase and compares the
result against a fixture that pins **the register rows and the oracle's verdict — never authored
prose.** Prose from a drafter is not byte-reproducible, and a fixture that diffs it is deleted within
a week.

## 11. Where the architecture is explained

This document describes *this repository*. The architecture it realizes is developed in the papers
indexed at **https://github.com/protocol-governed-computing**:

- **An Architecture for Closed-Loop Governed Transformation** — the closest companion to this
  repository: why evolution must itself be governed, and what closes the loop.
- **Realizing the Normative Platform and Its Governed Transformation** — construction completeness,
  the baseline as a party to its own transformation, and what realization surfaced.
- **A Conceptual Model** — the artefact language a mandate ultimately schedules.
