# Business Problem Statement

**Project Name:** transformation

## 1. Context

A design states, for every input of every step, where its value comes from. The Design Intent phase
holds each statement to a form the runtime resolves. A value comes from the starting intent, from the
contract's own inputs or from an earlier step, or it is a literal the design fixes.

Two rules of that phase judge the same statement. One asks whether it is a reference the runtime
offers. The other asks whether it is written in a form the runtime resolves.

Some artifacts are produced by a generator rather than written. A design names the generator, and
construction invokes it instead of writing the artifact.

---

## 2. Problem Statement

**A design cannot state some values its artifacts hold today.**

### A literal with a dot in it has no admissible spelling

An operation name such as `si.artifact.list` is a literal. So is a dotted identity, such as a
schema's `$id`. Written plain, the first rule reads it as a reference to a source the runtime does not
offer, and refuses it. Written in quotes, the first rule accepts it as a literal, and the second
refuses it, because it admits a literal only as a single word or an inline list or mapping.

The two rules disagree about what a literal is. No spelling satisfies both. Every contract that
observes the composition binds such a literal, so no design can redeclare one.

### A value a generator writes has no statement at all

A phase workflow hands its judging contract the rule set the generator seals into it. The design
names the generator, but it has no way to say that the generator determines that input. Left
unbound, the input is refused as missing. Bound to a description, it is refused as malformed. Bound
to an invented literal, it passes and says something false.

### This change shall

- give a literal one meaning across every rule that judges a binding, so a quoted value is a
  literal wherever it appears;
- let a design say that an input's value is determined by the generator of the artifact that holds
  it, and only where the design names that generator;
- leave every binding that is admissible today admissible, and give it the same meaning.

### What a caller sees

A design can redeclare a contract that observes the composition, and a workflow whose rule set a
generator seals, without inventing a value or leaving one unstated.

### Constraints decided by the business

- **No admissible design becomes inadmissible.** This correction only admits statements that were
  refused. It is not retroactive.
- **A generator determines only what the design says it does.** Saying a value is generated is
  admissible only for an artifact the design lists as generated.
- **The work that found this waits for it.** The rule-effectivity change is parked at its governance
  intent and resumes against the composition this change produces.
