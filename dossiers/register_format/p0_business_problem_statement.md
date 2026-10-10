# Business Problem Statement

**Project Name:** transformation

## 1. Context

Each phase of the transformation lifecycle judges a document against a rule set. A document is
admissible when it satisfies every rule its phase declares.

A phase document holds two kinds of content. Its prose explains the change to a person. Its
registers state the facts the rules judge. Today both live in one Markdown text, and each register
is a table inside the prose.

---

## 2. Problem Statement

**Only the current code can read a phase document's facts.**

A document needs a place for facts that a machine reads exactly, separate from the prose a person
reads.

### The facts are readable only through code

The rules read each register through conventions that only the code states:

- a column is found by the start of its name;
- a row reading `NONE IDENTIFIED` means the register is empty;
- a dash means the cell says nothing;
- routing is written as text, `OUTCOME -> target`, and the code splits it.

Fourteen such reading conventions and seven formats inside cells exist today. A person who wants to
reproduce a verdict without this code cannot, because the conventions are written nowhere else.

### This change shall

- carry every register as structured data in a block of its own, apart from the prose, as an
  artifact carries its Machine block;
- keep the prose as prose;
- give every document the same verdict and the same findings in its old form and its new form.

### What a caller sees

Authors write registers as structured data, beside their prose. No document changes verdict because
its form changed.

### Constraints decided by the business

- **No compatibility with v5.** Dossiers approved under v5 stay as published. This change neither
  converts nor reads them. The old reading retires once this change shows that the old and new forms
  receive the same verdicts.
- **The construction tests keep their coverage.** The delivered dossiers they reproduce artifacts
  from are copied and converted as test fixtures before the old reading retires.
- **One form for every document that carries registers**, from the seed to the mandate. The business
  problem statement has no registers and stays prose.
- **One form after this change.** The new form replaces the old form. The two never coexist.
- **What this change replaces is deleted, not stood down.** The readers of the old form are removed
  from the composition with their implementation; a version nothing can run is not carried.

### What this change does not decide

- **How a value inside a register is structured.** Routing written as text stays text here. Giving
  such values a structure is the next change.
- **Where the rules are declared, and in what language.** That is a later change.
- **Which rule set judged a document.** A document, a verdict and an approval naming their rule set
  is a later change, made once the rules are declared outside the code.

### Left for later changes

- **The structure of values inside registers.**
- **Declaring the design compiler's rules outside its code.**
- **Recording the rule set that judged a document, its approval and its migration.**
- **Governing and specifying construction on its own.**

---

## 3. Clarifications — answered and outstanding

The business author answered one question. None remain open.

### Answered

- **Must dossiers approved before this change move to the new form?** No. v6 does not read v5
  dossiers. They remain the published evidence of v5.
