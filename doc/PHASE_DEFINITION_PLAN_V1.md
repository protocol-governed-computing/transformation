# Phase Definition — implementation plan

## Verdict

Worth doing, in stages, and the valuable part is **not** generalizing the engine — that is already
done. The engine is `CC_JUDGE_AGAINST_SNAPSHOT_V0`: one contract that parses a document, applies a
rule set handed to it, and returns a verdict. Every phase workflow already invokes it. There is no
per-phase evaluation code to unify.

What is worth doing is promoting the **phase's own definition** out of Python. Today a phase is
described in four places, and the pipeline's own thesis is that behaviour is declared rather than
coded.

## What already exists

| Fact about a phase | Lives in | Form |
|---|---|---|
| purpose, question, key rule, rung, template, gate | `design/catalog.py` | Python dataclass |
| rule set | `design/p<n>_*/rules.py` | Python, sealed into the workflow |
| priors | `design/p<n>_*/rules.py` — `PRIORS` | Python tuple |
| observations | `design/p<n>_*/rules.py` — `OBSERVATIONS` | Python dict |
| transition | `catalog.next_phase()` | derived from tuple order |
| the phase list itself | `cli.py` — `RULE_SETS` | Python dict |
| merit policy | one governed artifact, all phases | already declared |

`catalog.Phase` already carries seven of the proposed fields, including `gate`. So this is
consolidation and promotion, not design.

## What the refactor is actually about

Three things, in decreasing value and increasing cost. Each stands alone and can ship alone.

### Stage 1 — gate and transition become checkable

**The gap this closes is real and already recorded.** A gate exists today only as prose in a
template; nothing states where acceptance is required, and nothing distinguishes *admissible* from
*accepted*. The transition between phases is implicit in a tuple's order.

- Give `catalog.Phase` a declared `transition` rather than deriving it from position, and make
  `gate` mandatory where a gate exists.
- Add a check that a dossier's declared lifecycle state is consistent with the gates its phases have
  passed — a document may be admissible and unaccepted, and nothing currently says so.

Smallest change, highest value, no artifact work.

### Stage 2 — one declaration per phase

Fold `PRIORS`, `OBSERVATIONS` and the `rule_set()` entry point into the phase's `catalog` entry, so
that a phase is described once. Adding a phase should touch the phase's own definition, its rule
module, and its template — not also `cli.py`, `catalog.py`, `emit_rule_sets.py` and the testbed
case table.

This is a mechanical refactor with a real test: **adding a tenth phase should require editing one
declaration.** If it does not, the stage is not finished.

### Stage 3 — PhaseDefinition as a governed artifact

Promote the consolidated declaration into a compiled artifact per phase — producer, input document,
output document, template, rule set reference, gate, transition — and have the phase workflow
reference it rather than carry a sealed copy of the rule set.

**Do this last, and only with eyes open.** No consumer outside the tool needs it: the runtime already
gets what it needs from the sealed rule set in each workflow. The argument for it is doctrinal, and
it is a good argument — "which phases exist and in what order" is currently code in a project whose
thesis is that behaviour is declared — but it buys principle, not function.

If it is done, `emit_rule_sets.py --check` generalizes from "the sealed rule set matches the declared
one" to "the sealed phase definition matches the declared one", which is the same drift protection
over a wider surface.

## What not to do

- **Do not collapse the nine workflows into one.** A phase is exactly where governance may diverge —
  a phase that needs a different capability, an extra observation, a second gate. One workflow per
  phase is the seam that makes divergence possible without a refactor. Keeping it costs nothing: the
  workflows are generated, not hand-maintained.
- **Do not make the merit policy per-phase yet.** One policy is what makes a score comparable across
  phases. Per-phase scoring is a governance change with its own justification needed, not a
  by-product of a refactor. Add the field when a phase needs to differ, not before.
- **Do not do this while the two missing preservation rules are outstanding.** They caused defects
  this release; this causes none. Sequence accordingly.

## Cost and risk

Stage 1 is hours and touches no artifact. Stage 2 is a day and is mechanical, with the ten-phase test
as its acceptance. Stage 3 adds a compiled artifact kind and a seal check, and should not be started
until Stages 1 and 2 are in and the pipeline has run a change request through them.

The standing risk is the same for all three: the rule sets are sealed into compiled workflows, so any
change to how a phase is declared must keep `emit_rule_sets.py --check` clean and be followed by a
recompile. A drifted seal means the tool and the composition judge different documents.

## Relationship to the specification

Fragment `standards/doc/spec/05_transformation.md` requires that gates be declared and that
acceptance not be inferred from admissibility (§10, §15.11), and that phases hand off explicitly
(§4). Stage 1 is the implementation catching up to the specification it was reverse-engineered into.
Stage 3 is optional against that specification: it requires rules to be declared data, which they
already are, and says nothing about where a phase's own definition lives.
