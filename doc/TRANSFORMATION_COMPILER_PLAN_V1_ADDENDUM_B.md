# Plan V1 — Addendum B: Self-Hosting

The transformation compiler's phases are authored as protocol artifacts, and the change request
that authors them is driven by the transformation compiler. Its first governed change is itself.

---

## 1. The inconsistency this closes

PGC's claim is that governed behavior is **declared, compiled, sealed, and executed** — never
hand-coded. A tool that decides which evolutions of a composition are admissible, while its own
admissibility rules live in Python, is the one component of the platform exempt from the platform's
central rule.

Moving the rule set from Python control flow into Python *data* is a real improvement and not
sufficient. Data inside an interpreter is still implementation: it is not compiled, not sealed, not
in the snapshot, and not inspectable through `si.*`. The rules cannot be quoted as evidence from
the composition they govern.

So each phase becomes a governed workflow.

## 2. The artifact set per phase

Kind meanings, as the platform actually defines them:

| Kind | What it is | Canonical path |
|---|---|---|
| `IN_` | Intent — the entry point | `canonical/<domain>/intents/` |
| `WF_` | Workflow — the executable graph | `canonical/<domain>/workflows/` |
| `CC_` | Capability contract — a node's governed call | `canonical/<domain>/capability_contracts/` |
| `CT_` | Capability transform — pure implementation | `canonical/<domain>/capability_transforms/` |
| `RB_` | **Runtime bindings** | `canonical/<domain>/runtime_bindings/` |
| `AC_` | **Actor** | `canonical/<domain>/actors/` |

Per phase, in domain `transformation`:

```
IN_SEED_SUBMITTED_V0            entry: a seed document is offered to P0
WF_P0_SEED_ADMISSIBILITY_V0     the graph: parse → evaluate → verdict
CC_PARSE_SEED_V0                governed call, bound to the parse transform
CC_EVALUATE_SEED_RULES_V0       governed call, bound to the evaluator transform
CT_PURE_PARSE_SEED_V0           raw seed text → structured registers
CT_PURE_EVALUATE_SEED_RULES_V0  rule set × registers → findings
VOCAB_*                         the controlled vocabularies (CR types, certainty, relationships)
RB_TRANSFORMATION_BINDINGS_V0   runtime bindings
AC_SEED_AUTHOR_V0               the human author of record
AC_GATE_REVIEWER_V0             the human at Gate 0 / Gate 2
```

### The rule set is data, the evaluator is the only mechanism

**A rule is not a `CC_` node.** The compiler forbids it: `assert_cc_no_implicit_chaining_v0`
constitutionally bans `loop`, `conditional`, `flow`, `next` and `transitions` from CC artifacts,
and a `WF_` graph is a static DAG with no iteration. Iteration exists at exactly one place — inside
a `CT_` machine, as a `loop` step with `over` / `iterator` / `accumulator`
(`compiler/stages/s5_construct.py`).

So a rule set of N rules evaluated over a document of M rows cannot be N workflow nodes. The shape
is:

| Element | Kind | Holds |
|---|---|---|
| the rule set | governed data artifact | **behavior** — what makes a seed admissible |
| the evaluator | `CT_PURE_EVALUATE_SEED_RULES_V0` | **implementation** — how a check is performed |
| the graph | `WF_P0_SEED_ADMISSIBILITY_V0` | composition only — parse, evaluate, verdict |

This is still a genuine behavior/implementation split, and a stronger one than Python data: the
rule set is compiled, sealed, immutable, versioned, and readable through `si.*` from the
composition it governs. The evaluator is a generic mechanism carrying no policy — it cannot be read
to discover what is governed, only how a check runs.

The `rules.py` / `checks.py` decomposition already built maps onto this almost one to one: `rules.py`
becomes the governed rule-set artifact, `checks.py` becomes the evaluator's check kinds. The
decomposition was right; the medium was wrong.

**`AC_` is the sharpest gain.** The plan says P0's output is human-authored and that Gate 0 is a
human confirming the seed says what they meant. Today that is convention — nothing enforces it. As
an actor artifact it becomes governed: the gate has a declared actor, and "a human is the author of
record" stops being a sentence in a document and becomes a property of the composition.

## 3. CR-0 — the compiler authors itself

The transformation domain is not hand-authored. It is the subject of a change request driven by the
transformation compiler:

```
CR-0   NEW_SUBDOMAIN   transformation::phases
```

The Python P0 built during scaffolding is **not the product**. It is the **genesis oracle**: the
hand-built implementation that drives exactly one change request — the one that authors the
compiled phases — after which the compiled artifacts take over.

This is how the platform itself bootstrapped, and it produces evidence nothing else can: the first
governed evolution the transformation compiler performs is the evolution that makes it governed.

### What the genesis oracle must and must not be

"The genesis oracle drives CR-0" is easy to over-read. Driving a change request through P1–P7
requires P1–P7 to exist, and building them in Python so that CR-0 can rehost them into artifacts
implements the entire pipeline twice.

That is not the intent, and the plan already licenses the alternative: **no phase depends on a
worker existing, and a human can fill any register by hand.** For CR-0 the human authors the
dossier registers directly; the genesis oracle's job is to *validate* them, not to produce them.

The genesis oracle is therefore only what has already been built — the seed template, the rule set,
the check kinds, the evaluator and the CLI. Nothing further is written in Python in order to reach
CR-0.

**The genesis oracle is retained, not deleted.** After CR-0 compiles, both oracles exist: the
Python implementation and the compiled `WF_P0_SEED_ADMISSIBILITY_V0`. Running both over the same
seed and requiring identical verdicts is a **differential conformance test** — the strongest
available proof that the rehost preserved behavior, and exactly the semantic-preservation claim
§4 of the plan says a transformation must support. Divergence is a defect in one of them, and the
test says which seeds expose it.

## 4. Bootstrap — why the circularity is bounded

Circularity exists only for changes **to the transformation domain itself**: evolving the phases
requires the phases. It does not touch anything else — for `book_library_mgmt` the sealed snapshot
already contains the phase workflows, and CR-1 through CR-6 simply run them.

Genesis is hand-driven once, by the Python oracle, and never again. Subsequent changes to the
transformation domain are ordinary CRs against the composition that contains it — which is the
`EXTEND_SUBDOMAIN` / `MODIFY` path the plan already requires, applied to the tool's own domain.

## 5. What this does not change

**CLI-only stands, with its meaning sharpened.** A compiled `WF_` executed through
`protocol_runtime` behind a local CLI driver is *not* a transport surface. The §5 ruling means **no
TI/TE boundary contract and no Operation Identity** — it never meant "the logic is Python." The
tool remains build-time and unreachable over transport.

**Snapshot access is unchanged.** Phases that read the composition still do so through
`inspector.api.query`. A compiled phase reads the snapshot the way any workflow does.

**Dossiers remain evidence, not artifacts.** The *phases* enter the snapshot; the dossiers they
produce never do.

## 6. Why this belongs in the baseline

The strategic case is not packaging convenience. Read the composition as it stands:

```
CONSTITUTION 31   INVARIANT 83   TI/TE 34   STRUCTURE 25   SURFACE 8
CT 17   CC 15   EV 10   AC 6   IN 5   WF 5   VOCAB 4   CS 3   RB 3
```

That is overwhelmingly **infrastructure**. There is very little business-shaped material in the
baseline for an adopter's first change request to reuse — which quietly weakens the plan's own §4
claim that "even CR-1 is not greenfield." The claim is true in letter (a new domain does compose
against 249 artifacts) and thin in substance (almost none of them are candidates a business CR
would legitimately reuse).

`transformation::` changes that. P0 alone contributes on the order of thirty artifacts across
`IN`, `WF`, `CC`, `CT`, `VOCAB`, `RB` and `AC`; the full phase set plausibly doubles the baseline
with a real, working, business-shaped domain. An adopter then starts from a platform that already
contains a governed pipeline doing real work, rather than a platform that contains only the means
to build one.

This is why CR-0 comes before the `book_library_mgmt` sequence rather than after it: the domain the
adopter inherits should be in the baseline before the baseline is used to demonstrate anything.

## 7. Versioning — the cost, and what it buys

Freezing the rule set as `_V0` artifacts before CR-1…CR-6 have exercised it guarantees churn. The
rule set will move as real change requests expose gaps, and under the immutable-version rule every
movement is a new `_V1`, `_V2`, `_V3`. Shipping a moving target as baseline is a genuine cost and
should not be discovered later as a surprise.

Two things make it acceptable:

- **The churn is evidence.** Revising a rule is a `MODIFY` against a real subdomain with real
  consumers; retiring one is a `DEPRECATE`. These are precisely the transformations the plan needs
  demonstrated, and `transformation::` supplies them from actual use rather than constructed test
  cases.
- **Scope CR-0 to the stable core.** CR-0 authors the structural rules — section presence,
  numbering, table shape, controlled vocabularies — which are fixed by the template and will not
  move. Semantic rules (belief discipline, design leakage, clarification completeness) accrete
  through later CRs, which is the governed path anyway.

## 8. Reuse eligibility — a requirement this creates

Placing `transformation::` in the composition means P3's REUSE search will find it. A library
catalog CR must not be offered `CT_PURE_EVALUATE_SEED_RULES_V0` as a reuse candidate: it is
tooling, not business capability, and a REUSE decision that reaches into the pipeline governing the
change would be a genuine defect rather than noise.

So reuse eligibility must become explicit. Either a domain declares whether it is a reuse target,
or the transformation domain is excluded from the P3 search by rule. **Neither exists today**, and
whichever is chosen must be settled before P3 is authored — it is a property of the analysis loop,
not a filter bolted on afterwards.

The general form of the question outlives this addendum: a composition will accumulate domains that
are infrastructure for other domains, and P3 needs a principled answer for all of them, not a
special case for this one.

## 9. The open design question

P0 consumes a markdown document that is not yet an artifact. The reader must therefore live
somewhere:

```
CT_PURE_PARSE_SEED_V0   raw seed text → structured registers (header, sections, tables)
```

A pure text→structure transform is legitimate and has no side effects, so this is admissible in
principle. What must be settled before authoring: whether the transform receives the document
**text** (file reading stays outside the graph, in the driver) or a **path** (which would put I/O
inside a transform, and must not). The former is correct and should be stated as a ruling.

The second open question is **how the rule set is carried**. It is data the evaluator consumes, but
it must be a governed artifact rather than a literal embedded in the transform — an opaque rule
table inside a `CT_` would be less inspectable than the Python it replaced, which would defeat the
purpose of this addendum entirely. Whether that artifact is `VOCAB`, a store, or a new kind is
open; that it must be independently readable through `si.*` is not.

## 10. Sequence

CR-0 precedes everything in Addendum A:

1. Genesis oracle in Python — **built**: template, rule set, check kinds, evaluator, CLI. Nothing
   further is written in Python to reach CR-0.
2. **Settle the two open questions** (§9) and reuse eligibility (§8).
3. **CR-0** — author `transformation::phases`, registers filled by hand and validated by the
   genesis oracle: `IN_`, `WF_`, `CC_`, `CT_`, `VOCAB_`, `RB_`, `AC_`, scoped to P0 and the
   structural rule core.
4. Compile CR-0 through `protocol_compiler` S1–S9, assemble, run. The phases are now in the
   composition.
5. **Differential conformance** — the Python oracle and the compiled P0 must agree on every fixture
   seed.
6. **CR-1 … CR-6** (Addendum A) — driven by the compiled pipeline, not the Python one, with the
   semantic rule set accreting through them.

Step 5 is the acceptance test for this addendum, and step 6 is where the release-4 claim is
actually evidenced.
