# Business Problem Statement

**Project Name:** transformation

## 1. Context

Each phase of the transformation lifecycle judges a document against a rule set. A document is
admissible when it satisfies every rule its phase declares. The rule sets change: a correction
adds a rule, widens a vocabulary, or requires a column that was not required before.

A phase document carries its registers as structured data in a block of its own, apart from its
prose. Each phase declares its registers in a register schema, and the schema's identity is the
identity of the rules it declares.

---

## 2. Problem Statement

**The document names no rules that judged it.**

### The rules that judged a document are unrecorded

A document does not change when the rules do. Every rule written later applies to every document
ever written, the next time anyone looks.

- **A verdict has no rule set.** "This document is admissible" describes the rules of today, not the
  rules it was approved under. A re-run after a correction may differ. Nothing says whether the
  document changed, the rules changed, or both.
- **An approval is silently reopened.** A gate closes on a document judged against the rules of that
  day. When the rules move, nobody is told, and the document does not know.
- **A migration looks like an authoring.** A document amended to satisfy a later rule reads exactly
  like one written under that rule from the start. The second is a stronger claim than the first.

This has happened and has been measured. One added column made every dossier inadmissible at once,
and five delivered dossiers were amended by hand to pass again. Today, 32 of 273 delivered
documents fail rules that were added after their approval.

### This change shall

- let a document name the rule set it was authored under, by an identity that changes only when
  the rules change;
- let a verdict name the rule set it was rendered against, by the same identity;
- record a document amended to satisfy a later rule set as migrated, apart from one authored under
  that rule set;
- make an approval name its rule set, and leave it unconfirmed under a later rule set until a person
  re-confirms it.

### What a caller sees

Every verdict names the rule set that rendered it.

### What this change does not decide

- **Whether a given correction is retroactive.** The correction declares that itself (§3).

### Left for later changes

- **Rule sets that differ per composition** rather than per version. Nothing has needed it.

---

## 3. Clarifications — answered and outstanding

The business author answered six questions. None remain open.

### Answered

- **When the rules change, is an existing approval still an approval?** **An approval is a fact about
  the rule set it was given under, and it stays that fact.** Under a later rule set, the approval
  stands unconfirmed until a person re-confirms it against that set. An approval that the next rule
  silently erased would mean no gate was ever closed. An approval that silently carried over would
  claim a judgement nobody made.

- **Should a document be judged against the rules it was authored under, the current rules, or both?**
  Both, because they answer different questions. The rules it was authored under answer whether its
  approval was sound. The current rules answer whether it would be approved today. A verdict that
  does not name its rule set answers neither.

- **Is a document that passes today's rules only because it was amended making the same claim as one
  that passed them when written?** No. A document stands in one of three states:
  - **approved**: a person closed its gate under a rule set;
  - **migrated**: it was amended to satisfy a later rule set, and nobody has re-confirmed it;
  - **re-confirmed**: a person judged it whole under the later rule set and closed its gate again.

- **Must every document move to each new rule set?** No. A completed change need not answer rules
  written after it closed. A document left behind stays approved under its own rule set and stands
  unconfirmed under the later one.

- **What gives a rule set a new version: every change, or only one that can invalidate a document?**
  **Only a change that can alter a prior document's admissibility.** If every change created a
  version, documents would fall behind for corrections that could never affect them. "Migrated"
  would then distinguish nothing. A new version means that documents approved before it may no
  longer pass.

- **Who decides that a correction is retroactive: the correction, or the rule set?** **The correction
  declares its own effectivity, retroactive or not, and the rule set records the declaration as
  governed history.** Only the change knows whether it can invalidate a document, because it knows
  what it added and why. A retroactive correction creates a new version and names the documents it
  affects. A non-retroactive correction creates no version and disturbs no document.
