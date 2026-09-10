# Business Problem Statement

**Project Name:** transformation — design

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed requirement and
> the execution path a change would take. It is not a design.

## 1. Context

A design states what an act must become, and construction renders it. Everything an act needs to run
is stated once, in a register, where a reviewer reads it before anything is built — which capability
it composes, what each step consumes and produces, and where its records live.

The platform recently gained something a design cannot state. An act may now declare that it reads
records another part of the business owns: it names the description it owns and the ones it merely
consults, the composition resolves all of them, and a write to anything consulted is refused when the
act runs. The reach is a first-class thing the platform carries.

---

## 2. Problem Statement

**The platform admits a declared reach and the design language cannot state one.**

A design says where an act's own records live. There is no register for the records it reads and does
not own, so a design that needs a reach has three options and all of them are wrong: leave it
unstated and have the act stop when it runs, restate another part's records as its own, or add the
declaration to the built artifact by hand — which works, passes every check, and is the ungoverned
act the reach was introduced to remove.

**The third is the dangerous one**, because it is the easy one and it looks like delivery. A reach
added by hand is a reach no reviewer saw, which is precisely the property the platform change was
made to gain.

**The requirement is confirmed rather than anticipated, and one composition is where it surfaced.**
The instance belongs to a business domain this lifecycle does not require and a later composition may
not contain; it is evidence that the shape occurs. In that composition, an act creating a wallet
reads the records an identity subdomain owns. The platform capability it needs exists and is proven.
Its change request is raised, pinned, and stopped at the point where it would state the reach.

This change shall:

- let a design state the bindings an act consults, alongside the one it owns;
- have construction render what the design states, so the built act declares the reach the design
  declared;
- make a reach a design states but does not own visible to the rules that judge a design, so an act
  reaching across a boundary is something a reviewer sees rather than something a run discovers.

### What this change does not decide

- **Which acts reach which records.** Each domain's business, stated in its own change.
- **How the composition resolves a reach.** The platform decided that; the design language states it
  and construction emits it.
- **Whether a reach may cross a domain.** Settled by the platform: it may not.

---

## 3. What governs this today

**The register that states where an act's records live.** A design declares one binding per act, and
construction renders exactly that. Nothing in the design language names a second, and no rule asks
whether an act reads records it did not declare — the question could not be posed, because the
platform had no answer for it until now.

**The rules that judge a design already reason about reach in one direction.** A rule refuses an act
that reaches a *writing* capability across a boundary, and it works from what the composition
publishes. It has no counterpart for storage, because storage reach did not exist.

---

## 4. The execution path a change would take

One repository, and the shape is the one the lifecycle already uses:

| # | What changes |
|---|---|
| 1 | The P7 register that declares an act's storage — a design states the bindings it consults. |
| 2 | The rules that judge P7 — a declared reach is held to what the platform admits, and a design that reaches records it never declared is refused. |
| 3 | The renderer — construction emits the declaration into the built act, so what runs is what was designed. |
| 4 | The P8 mandate, if the reach changes what construction must schedule. |

**This change amends a generated artifact.** A phase's rule set is produced from a template and a
declaration read together, and the workflow that judges P7 carries a sealed copy. The lifecycle can
now say that: a design names the generator an artifact is produced from, and construction invokes it
rather than writing the artifact directly. **That capability was delivered and has never been used.**
This change would be the first to use it, and it is therefore also the first change to a phase's rule
set delivered through the pipeline rather than by hand.

---

## 5. Clarifications — answered

All four are answered by the business author, and together they close the model: an act declares
exactly the foreign bindings it consults, the composition derives their record surface, every actual
read is declared, and every declaration is used.

### Answered

- **Does the reach belong in the register that already declares an act's binding, or in a register of
  its own?**
  **Its own register.** Ownership and read-only reach stay structurally distinct — not one register
  with a column saying which is which, where the two would be a typo apart and a rule reading the
  column would be the only thing between them. It also mirrors what the artifact does: the act
  declares the binding it owns in one field and the ones it consults in another, so the design states
  the change in the same shape construction renders it.

- **Must a design state the records it expects to read through a reach, or only the binding it
  consults?**
  **Only the binding.** The binding is the owning subdomain's declaration of its own records;
  restating those records in the reaching act's design is the second copy this whole line of work
  exists to remove — it would be maintained by someone other than their owner, one layer further out
  than the case that started it. The reachable records are derived from the pinned composition.

  **Derivable today, checked rather than assumed:** the composition publishes every store with the
  structure that declares it and the bindings that reach it, so a rule can resolve a declared binding
  to the records it covers without a new fact being published.

- **Should a rule refuse a design whose act composes a capability that reads records the act has not
  declared a reach to?**
  **Yes — P7 refuses it.** That is the defect the wallet hit, caught where a reviewer sees it rather
  than when the act runs. **Derived, never guessed:** the read surface of a composed capability comes
  from its declared contract and its capability's declared operations — the steps a contract performs,
  the store each addresses, and whether the operation reads or writes. All three are published. A
  rule resting on an operation's name or on what an implementation happens to do would be a
  convention anybody could break by naming something well.

- **May an act declare a reach it never uses?**
  **No.** Every declared consulted binding is consumed by at least one composed read. A reach is a
  scoped permission for a stated purpose, not a reserve held against future need — and an unused one
  is a permission granted for nothing that nothing would notice.

### What the four settle together

The declared set and the used set are the same set. An act reaches nothing it did not declare, and
declares nothing it does not reach. Neither half is checkable without the other: the first alone
permits a reserve, the second alone permits a silent reach.
