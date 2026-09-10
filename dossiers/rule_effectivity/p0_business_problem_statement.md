# Business Problem Statement

**Project Name:** transformation

## 1. Context

Each phase of the transformation lifecycle declares a rule set, and a document is admissible when it
satisfies every rule its phase declares. The rule sets change: a correction adds a rule, widens a
vocabulary, or requires a column that was not required before.

Documents do not change when rules do. A dossier authored last month sits on disk exactly as it was
approved, and every rule written since is applied to it the next time anyone looks.

---

## 2. Problem Statement

**Every rule is retroactive to every document that has ever existed, and nothing records which rules a
document was authored under.**

A correction that requires a new column invalidates every dossier that predates it. That happened:
one column was added and every dossier ever authored became inadmissible at once — including three
that were complete, approved, and delivered months earlier. Each was amended by hand and passed again.

Three things are wrong, and they are separable.

**A verdict has no date.** "This dossier is admissible" is a statement about now, not about when it
was approved. Re-run it after any correction and the answer may differ, with nothing to say whether
the document changed, the rules changed, or both.

**An approval does not survive the rules it was given under.** A gate closed on a design judged
complete against the rules of that day. When the rules move, the approval is silently reopened —
nobody is told, and the dossier does not know.

**A migration is indistinguishable from an authoring.** A dossier amended to satisfy a rule written
after it was approved looks exactly like one authored under that rule from the start. The record
cannot tell a document that always said this from one taught to say it afterwards, and the second is
a weaker claim.

This change shall:

- give a rule set a version, so a document can say which one it was authored under;
- let a verdict state the rule set it was rendered against;
- distinguish a dossier migrated to a later rule set from one authored under it;
- say what happens to an approval when the rules it was given under change.

### What this change does not decide

- **Whether a correction should be retroactive.** Some must be. This change makes the question
  askable, not answered.
- **Whether old dossiers must be migrated.** That is a judgement per correction.
- **Anything about generated artifacts.** A separate problem with its own change.

### Left for later changes

- **Rule sets that differ per composition** rather than per version. Nothing has needed it.

---

## 3. Clarifications — answered and outstanding

Four were answered by the business author. Two remain open and no phase may proceed on a guess about
them.

### Answered

- **When the rules change, is an existing approval still an approval?** Yes. **An approval remains
  valid under the rules it was given, and re-evaluation under current rules is a separate act that is
  recorded.** Anything else destroys the meaning of a gate: if an approval is only ever a statement
  about today's rules, then no gate was ever closed — it was provisionally closed pending every
  future rule, and "approved" means "not yet invalidated". A closed gate is a fact about a moment.

- **Should a document be judged against the rules it was authored under, the current rules, or both?**
  Both, because they answer different questions. Judged under the rules it was authored under, the
  question is whether the approval was sound. Judged under current rules, the question is whether the
  document would be approved today. Neither answer substitutes for the other, and a verdict that does
  not say which rules it was rendered against answers neither.

- **Is a dossier that satisfies today's rules only because it was amended making the same claim as
  one that satisfied them when written?** No. There are three states, not two: **approved** — closed
  under a rule set and still so; **migrated** — amended to satisfy a later rule set, passing now and
  taught to; **re-approved** — re-judged whole under the later rule set and re-gated by a human. Five
  dossiers were migrated and none re-approved, because no human re-closed a gate on them.

- **Must every dossier be migrated when a rule set moves, or may one be left at the version it was
  approved under?** It may be left. A completed change is not obliged to answer rules written after
  it closed, for the same reason its baseline is never re-pinned forward: approving a document
  against a rule set that arrived later asserts a re-reading of facts already settled.

**The consequence, accepted deliberately:** a document must carry the rule-set version it was
approved under, or none of the above is recordable and the distinction between approved and migrated
cannot be made at all.

- **What versions a rule set: every change, or only one that can invalidate a document?** **Only one
  that can alter a prior dossier's admissibility.** Versioning every change makes the version
  meaningless as a signal: a document would fall behind constantly for corrections that could never
  have affected it, and "migrated" would stop distinguishing anything. A version means *documents
  approved before this may no longer pass*.

- **Who decides that a correction is retroactive — the correction, or the rule set?** **The
  correction declares its own effectivity — non-retroactive or retroactive — and the rule set records
  that declaration as governed history.** Only the change knows whether it can invalidate, because it
  knows what it added and why. But a claim held only in a commit message is what exists today, and it
  is why five dossiers were migrated with the reasoning surviving in one commit body.

**What follows, and it is more than the two answers:**

- **Each approval pins the rule-set version it was given under.** Without that pin nothing can
  distinguish an approval that still stands from one whose rules have moved.
- **A retroactive change creates a new version and identifies the dossiers it affects**, each to be
  migrated or re-approved. Naming them is part of the change, not a later discovery.
- **A non-retroactive correction does neither.** No version, no migration, no dossier disturbed —
  and the declaration is what makes that claim checkable rather than assumed.

Applied to this session: the diagnostic-message improvement changed no verdict and should have
declared itself non-retroactive. The Subdomain column invalidated every dossier that existed and
should have declared itself retroactive, created a version, and named all five.
