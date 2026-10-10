# Business Problem Statement

**Project Name:** transformation

## 1. Context

A design states, for every input of every step, where its value comes from: a reference to a value
the runtime offers, or a literal the design fixes. The Design Intent phase reads a literal one way:
a single word, a qualified identity, a number, or a value opening with a quote, bracket or brace. A
value with a dot in it is written quoted, or it reads as a reference.

Construction renders each statement into the artifact the runtime executes.

---

## 2. Problem Statement

**Construction does not render every literal as the value the design states.**

### A quoted literal keeps its quotes

A design writes `"si.artifact.list"` to state the operation name si.artifact.list. Construction
hands the runtime the text with its quote marks, a value the design never stated. The design is
admissible, construction reports the artifact determined, and the runtime receives the wrong value.

No delivered artifact carries such a value today, because until now no design could state a quoted
literal admissibly. The first design that does — the rule-effectivity change, redeclaring the
contracts that observe the composition — would be built wrong.

### A decimal number becomes text

Construction reads a whole number as a number and any other number as text. A design stating 1.5
hands the runtime the text 1.5.

### This change shall

- render a quoted literal as the value inside its quotes;
- render a number as a number, whole or decimal;
- leave every other binding rendered exactly as it is today.

### What a caller sees

A design states a value, and the runtime receives that value.

### Constraints decided by the business

- **No delivered artifact changes.** Every artifact construction reproduces today, it reproduces
  unchanged.
- **The rule-effectivity change waits for this one**, and resumes once it is delivered.
