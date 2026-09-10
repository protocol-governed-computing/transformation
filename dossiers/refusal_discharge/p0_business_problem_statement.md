# Business Problem Statement

**Project Name:** transformation — design

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed requirement and
> the execution path a change would take. It is not a design.

## 1. Context

A business states what it refuses before it states anything about how the work is done. Among the
first things it writes down is a register of the operations it will not perform and the reason for
each — a wallet for a person nobody accepted, a rejection that states no grounds. These are business
rules of the strongest kind: they say what must never happen, which is not a preference that can be
traded away later against effort.

The lifecycle carries that register faithfully out of the seed and into the change request, row for
row, and one rule checks that nothing was dropped on the way. From that point on, no phase asks
about it again.

---

## 2. Problem Statement

**A business can declare a refusal and the lifecycle will never ask what carries it out.**

The register is preserved and abandoned. Nothing asks which act performs the refusal, at which step,
or on which outcome. A design can therefore pass every phase, satisfy every rule, and measure as
completely determining its artifacts, while an operation the business declared it refuses is
performed on demand.

**The failure is silent by construction, and that is the whole of the problem.** A refusal that is
never carried out produces no error, no unhandled path and no missing field — the act simply
succeeds where it was supposed to stop. There is nothing for a rule set to notice, because every
rule is asking whether what the design *does* say is coherent, and this is a thing the design does
not say.

**It has already happened, once, in the only function that has exercised it.** A change request
declared four refusals for giving a person a wallet and recording a decision about one. Three became
branches of the acts that perform them. One — *the person has not been accepted, or was rejected* —
became nothing at all. Every phase read admissible, construction completeness read 100%, the build
sealed, and the act ran: an unverified person was given a wallet. The defect was found by executing
the function and checking the result against the business's own criteria, which is the latest and
most expensive place it could have been found. The refusal had been sitting in the register, in the
business's own words, since the first phase.

**Where the work is done, it still cannot be read.** That change request has since been re-authored
and all four refusals are now discharged. Three of the four are traceable only by reading the design
and recognizing the branch; their rows cite other findings, because nothing asks them to cite the
refusal. So even a correct design does not show a reviewer that the business's refusals were carried
out — it shows a reviewer a topology, and leaves them to reconstruct the mapping.

### Objectives

This change shall:

- let a design state, for each refusal the business declared, what discharges it — which act, at
  which step, on which outcome;
- refuse a design that leaves a declared refusal unaccounted for, at the phase where acts and their
  outcomes exist;
- hold a stated discharge to the design's own topology, so a refusal declared discharged by a step
  that does not exist, or on an outcome that does not lead to a refusal, is refused;
- let a refusal owned by someone else, or deliberately not carried out in this change, be stated as
  such rather than left silent — a deferral is an answer and an omission is not.

### What this change does not decide

- **Which operations a business refuses.** Each business states its own, in its own change.
- **How an act performs a refusal.** The design decides that; this change asks only that it say
  which step does and on what outcome.
- **Whether a refusal must be discharged in the same change that declared it.** It may be deferred
  to another owner. What it may not be is unmentioned.

---

## 3. What governs this today

**One rule, at the second phase, and nothing after it.** The change request must carry every refusal
the seed stated, keyed on the operation and the condition. It checks that the rows arrived. It
cannot check that anything became of them, and nothing downstream tries.

**The domain model may cite a refusal, and need not.** Where an author has traced a refusal into a
process step, they did so unprompted and cited it by hand. A later phase that reads that citation
does not exist.

**The platform already refuses at its own layer, and refuses harder.** An invariant that no
constitution rule names cannot be sealed into a composition — an obligation nothing is bound to is
not an obligation, and the build stops rather than shipping one. That check was met while delivering
the announcement capability, and its delivery record names this as the same closure one layer up:
*a declared refusal travels nine phases as prose and arrives as nothing, because no rule asks what
carries it out.* The design pipeline lacks what the composition already enforces.

---

## 4. The execution path a change would take

One repository, and the shape the lifecycle already uses:

| # | What changes |
|---|---|
| 1 | The P7 template — a register in which a design states what discharges each declared refusal. |
| 2 | The rules that judge P7 — every declared refusal is discharged or deferred, every discharge names a refusal the business declared, and every stated discharge is held to the design's own topology. |
| 3 | The check kinds those rules are built from, where an existing kind does not already express the question. |
| 4 | The generated artifacts a phase's rule set produces — reached by invoking the generator the design names, never written by hand. |

**This change authors no artifact and renders nothing.** A discharge is a claim about a design,
checked while the design is judged; it is not a fact an act carries at run time. Construction is
untouched, and the mandate will schedule no build step.

**It amends generated artifacts, and states the generator that produces them.** A phase's rule set
is produced from a template and a declaration read together, and the workflow judging P7 carries a
sealed copy. The lifecycle can state that, and one change has now been delivered that way.

---

## 5. Clarifications — answered

All six are answered by the business author. Together they settle where the statement lives, what it
must contain, what holds it to the truth, and what a design may do about a refusal it does not own.

### Answered

- **Should the discharge be stated in a register of its own, or read out of the citations the design
  already carries?**
  **Its own register.** A source finding is a citation, not a structure: it is written where an
  author found it natural and omitted where they did not, and three of the four refusals in the only
  design that discharges any cite something else. A rule resting on that convention would report a
  correct design as red and would be satisfied by anyone typing the right string. The statement is a
  claim the design makes and it belongs in a register a reviewer reads.

- **At which phase is a design refused for leaving a refusal unaccounted for?**
  **The design intent phase.** It is the first phase where acts, their steps and their outcomes
  exist, and a discharge cannot be stated before there is something to point at. Earlier phases have
  no vocabulary for it; later there is only the mandate, which would freeze the omission rather than
  catch it.

- **What must a discharge name?**
  **The act, the step and the outcome.** Naming the act alone would be satisfied by any act that
  refuses anything at all. The outcome matters because a step that returns its judgement succeeds
  whatever it found — a refusal carried by a step whose failing outcome routes onward is not a
  refusal, and that distinction was already made once, by hand, in the wallet's design.

- **Is a stated discharge checked against the design, or taken as written?**
  **Checked.** The named step must be a node of the named act's topology, and the named outcome must
  be routed from it to an ending that refuses. Both facts are already stated in the design's own
  execution topology, so nothing new needs publishing and nothing is taken on trust. A register that
  is only read for presence is a register that documents intent and enforces nothing.

- **May a design state a discharge for a refusal the business never declared?**
  **No.** The declared set and the discharged set are the same set. A discharge naming no declared
  refusal is either a refusal the business never approved or a row left behind by a rewording, and
  both are things a reviewer should be shown rather than left to find.

- **What may a design do about a refusal it does not own?**
  **Defer it, with the owner named.** A refusal may belong to another subdomain, or to a later
  change, and forcing every change to carry every refusal it inherits would make the register a
  reason to avoid declaring refusals. A deferral is an explicit disposition and must already be
  present in the change's declared scope, so it is a decision the phases already recorded rather
  than an escape written at the last phase.

### What the six settle together

Every refusal the business declared is accounted for by the design that judges itself complete —
carried out by a named step on a named outcome, or deferred to a named owner — and every discharge
the design states corresponds to a refusal the business declared and to a branch the design actually
contains.
