# Halt — generated_artifacts

**Phases reached:** P0 – P6, every one admissible
**Status:** HALTED at P7, and this is the expected outcome
**Resolved by:** its own GAP-5 — delivery by hand, once, recorded
**Do not:** author a partial P7, or amend the nine phase artifacts directly

> **Delivered.** The by-hand delivery this document anticipated has been carried out and is recorded
> in `delivery.md`. P7 is authorable from here on — the register that was missing exists — but not
> for this change, which is complete at P6 by design. `THE_LAST_EXCEPTION` is spent.

---

## Why it stops, and why that is not a failure

**P7 cannot be authored for this change — not authored-and-incomplete, but unauthorable.**

The change amends nine artifacts: the phase workflows carrying each phase's sealed rule set. Under
this change's own rules, a generated artifact is never edited directly — it is reached by amending
its generator and invoking it. So the design must say *"this artifact is reached by invoking that
generator."*

**P7 has no register in which to say it.** Its fifteen registers describe what an artifact must
become — its inventory, topology, compositions, bindings, interfaces, stores. **None names how an
artifact is reached.** That register is `GAP-2`, added by this change.

So the design cannot be expressed under the language it exists to extend. This is the bootstrap
`GAP-5` anticipated and made a decision rather than a circumstance:

> The path this change creates does not exist until it is delivered.

## How this halt differs from cr_04's

The two look alike and are not the same defect. Keeping them apart is why they are separate dossiers.

| | `cr_04_wallet` | this dossier |
|---|---|---|
| P7 | authorable, admissible, **99.4%** determined | **not authorable** |
| what is missing | a register for facts a build STRUCTURE carries | a register for how an artifact is reached |
| the artifact | authored — it is its own source of truth | generated — its source of truth is elsewhere |
| owned by | `register_coverage` | this dossier |

`cr_04` could state everything about its artifacts except 51 facts of one kind. This change cannot
state the one thing it most needs to say about any of its nine.

## The alternative, and why it is refused

The nine artifacts could be edited directly. Every one is a plain file; the smallest is 333 lines and
the largest 1,710.

That is refused by this change's own governance rules — `GENERATOR_IS_AUTHORITATIVE` and
`ONE_ARTIFACT_ONE_PRODUCER`. An edit would last until whoever next runs the emission, and a change
that violates its own boundary rules to deliver itself has established nothing.

## Delivery

By hand, once, per `GAP-5` and the boundary rule `THE_LAST_EXCEPTION`. The design that governs it was
judged through six phases and is recorded here. The generator — a template and the declaration read
with it — is amended, the emission is invoked, and the agreement check becomes a build gate.

**After this delivery the exemption is spent.** `THE_LAST_EXCEPTION` states it: no later change to
this subdomain may claim it, because the path will exist. Two changes before this one were delivered
by hand — `founding_design_bootstrap`, which established the subdomain, and `rule_expressiveness`,
which closed at Gate 1. This is the third and last.

## Resuming

Nothing to resume. This dossier is complete at P6 by design, not blocked. What follows is delivery,
and then `register_coverage` becomes deliverable *through* the pipeline rather than beside it — the
first change in this subdomain's history that will be.
