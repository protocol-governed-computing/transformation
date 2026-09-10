# Business Problem Statement

**Project Name:** transformation

## 1. Context

The transformation lifecycle carries a change from a problem statement to artifacts that compile. A
design says which artifacts a change touches and what each must become; construction renders them and
measures whether the design determined them.

That works because an artifact is authored. Some are not. A phase's rule set is generated: the phase
declares its registers in a template and its remaining rules in code, and a tool writes the artifact
that carries a sealed copy. The largest is over seventeen hundred lines and nobody types it.

---

## 2. Problem Statement

**The lifecycle governs authored artifacts and has no account of generated ones.**

A design that touches a generated artifact cannot be built from, and the reasons compound.

**An amendment must redeclare the artifact whole.** Construction renders the amended artifact from
the design alone and the result replaces what was there, so a design stating only what it adds
renders an artifact with the rest deleted — and reports complete while doing it. For a generated
artifact this is not merely laborious, it is wrong twice over: no design register has a shape that
carries a nested rule set, and an artifact rendered from such a design would be overwritten by the
next generation anyway.

**The thing that determines the artifact is not the artifact.** The rules live in a template and in
code; the artifact carries a copy so it can be sealed, versioned and inspected. A change that means
to alter the rules must alter what generates them. The lifecycle has no way to say that — it knows
how to schedule an artifact and not how to schedule the thing an artifact is generated from.

**So the delivery of such a change is ungoverned.** It was carried out by hand, correctly, and
nothing in the dossier records how the artifacts were reached. A change whose delivery cannot be
stated is a change whose delivery nobody checked.

This was not hypothetical. A change to the phases themselves was designed through six phases,
approved, and stopped at the seventh because there was no admissible way to state how it reached the
artifacts.

This change shall:

- let a design name the thing an artifact is generated from, and schedule that;
- let construction tell a generated artifact from an authored one, and refuse to render one it does
  not own;
- record, for a generated artifact, the provenance from generator to artifact, so the sealed copy
  can be checked against what generated it.

### What this change does not decide

- **Whether generating an artifact is a good idea.** It is done today and this change governs it, it
  does not judge it.
- **Which artifacts are generated.** That is a fact about each artifact, not a decision here.
- **Anything about how rules are declared.** The template and the code are what they are; this change
  is about stating and checking the path from them to the artifact.
- **How a document authored under one rule set is judged under a later one.** That is a separate
  problem with its own change.

### Left for later changes

- **Generated artifacts outside this lifecycle.** The governance surface may one day emit rather than
  carry an artifact, and the same question will arise there. Nothing has needed it yet.

---

## 3. Clarifications — answered and outstanding

Three were answered by the business author. Three remain open and no phase may proceed on a guess
about them.

### Answered

- **When a generator and its generated artifact disagree, which is wrong?** The artifact. **The
  generator is always authoritative and the generated artifact is never corrected directly.** A
  disagreement is not a difference of opinion; it is proof the copy is stale. Correcting the artifact
  leaves the generator still producing the old value, so the next emission reverts the correction
  silently — the fix lasts until whoever next runs the tool. This has already happened in the
  direction that hurts: a rule added after a workflow was emitted left fifty-two rules sealed against
  fifty-five declared, and every run reported confidently on the smaller set.

- **Is a generated artifact governed, or is its generator governed, or both?** Both, and not equally.
  The artifact is governed as sealed output — read-only, with the standing the snapshot has. Editing
  one is the same class of error as editing the snapshot by hand. The generator is governed as the
  thing that determines it, and is where a change is made.

- **What evidence should a change carry that a sealed copy matches what generated it?** The
  agreement itself, checked mechanically. A generator that can report whether every artifact already
  matches must do so as a **build gate rather than a habit** — otherwise "the generator is
  authoritative" describes a truth nobody is holding. `emit_rule_sets --check` exists and returns
  non-zero; it is not yet required by any build.

- **May a design schedule a generator, or must it schedule the artifact and name the generator as
  the means?** It schedules the **artifact** and names the generator as the means. The artifact is
  what enters the composition and what conformance judges; a mandate scheduling a generator schedules
  something that never appears in a snapshot.

- **Should construction refuse to render a generated artifact outright, or render it by invoking the
  generator?** It **invokes the generator**. Refusing outright leaves delivery ungoverned forever,
  which is the hole. Rendering it directly would make construction a second producer of the same
  artifact, and two producers of one truth drift. Invoking is the only route where one producer stays
  authoritative.

- **Is the template a generator, the code a generator, or both together?** **Both together, as one
  generator.** Neither determines the artifact alone: the template declares the registers and their
  columns, the code declares what remains, and the emission reads both. Treating them as two would
  let a change amend one and regenerate from a stale pairing.

**The consequence, accepted deliberately:** construction gains the ability to invoke a generator, and
a generated artifact's agreement with its generator becomes a build gate rather than a habit.
