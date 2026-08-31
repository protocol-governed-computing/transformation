# Business Problem Statement

**Project Name:** transformation

## 1. Context

A change reaches its artifacts through the design phase. The design states, register by register,
what each artifact must become: its nodes, its steps, the fields it accepts and returns, the stores
it reaches, the bindings it resolves through.

A change may author an artifact or amend one. When it amends, the rule is that the design states the
artifact **whole** — construction renders the amendment from the design alone and the result replaces
what was there, so a design stating only what it adds renders an artifact with the rest deleted, and
reports itself complete while doing it. A separate check compares each amendment with what it
replaces and refuses one that narrows it.

That check works. What it reveals is that the design sometimes cannot state the artifact whole no
matter how it is written.

---

## 2. Problem Statement

**The design language can express an artifact a change authors, and cannot express one it amends.**

The registers were shaped for authoring. Where the authoring path supplies a fact implicitly — because
a new artifact declares it in the same breath as being declared at all — the amending path has
nowhere to say it. The fact is not optional and not derivable; it simply has no register.

Four instances, all found by carrying one real change to the point of construction:

**A build configuration cannot be amended at all.** Adding a second subdomain to a domain's build
declaration loses fifty-one facts — the artifact kinds it discovers, where its outputs are written,
where its bootstrap search begins, the phases it builds in. No register in the design holds any of
them, at any shape. The change is refused, correctly, and cannot be expressed correctly either.

**An amended artifact cannot state its subdomain.** The design states which subdomain owns an
artifact only for artifacts the change authors. An artifact being amended already has one, and the
design has no way to restate it, so the fact is lost by the amendment that was supposed to preserve
it.

**A vocabulary that extends nothing cannot say so.** The register carries what a vocabulary extends.
A vocabulary that is the base has nothing to name there, and no way to state that this is deliberate
rather than omitted.

The pattern in all of them is one thing: **a fact the authoring path never had to state, because
authoring supplies it, and the amending path must state and cannot.**

This change shall:

- let a design state, for an artifact it amends, every fact that artifact carries;
- make it impossible for an amendment to be admissible and incomplete at the same time.

### What this change does not decide

- **Anything about generated artifacts.** Where an artifact's source of truth is a generator, the
  question is which of them is authoritative, and that is a different problem with its own change.
  This one concerns artifacts that are authored — where the artifact *is* the source of truth — and
  the design language's coverage of them.
- **Anything about rule-set versioning or which rules apply to a document.** A separate problem with
  its own change.
- **Whether an amendment should have to state an artifact whole.** It should. That rule is what
  surfaced this, and it is not in question.
- **How many registers there should be.** Whether this is closed by widening registers that exist,
  adding registers, or letting an amendment cite what it does not change is a design question, not a
  business one.

### Left for later changes

- **Artifact kinds nothing has yet amended.** Four kinds are known to be affected. The rest are
  unexamined, and a kind nobody has tried to amend cannot honestly be specified.

---

## 3. Clarifications — answered and outstanding

One was answered by the business author, and it settles the shape of the change. Five remain open and
no phase may proceed on a guess about them.

### Answered

- **Must an amendment restate every fact an artifact carries, or may it state what it changes and
  declare the rest untouched?** **It restates every fact. A register per fact.** An amendment renders
  the artifact that replaces its predecessor, so a design that states less than the artifact is a
  design that renders less than the artifact — and the alternative, declaring the rest untouched,
  makes the design something that must be read together with the thing it replaces in order to mean
  anything. A design that cannot be read whole cannot be reviewed whole.

**What follows from that, accepted deliberately:**

- **The design language needs a register for every fact of every amendable artifact kind.** Where a
  register is missing today, one is added. The known gaps are a build configuration's discovery,
  output, bootstrap and phase declarations; an amended artifact's subdomain; and a base vocabulary's
  absence of a base.
- **An amendment's design grows with the artifact, not with the change.** Adding one subdomain to a
  build configuration will state that configuration whole. This is the cost of a design that reads as
  the artifact rather than as a diff against it, and it is accepted.
- **A design therefore transcribes existing state.** That is not duplication to be optimised away:
  what the design states is what construction renders, and a fact absent from the design is a fact
  absent from the artifact.

### Outstanding

- **Is a fact the authoring path supplies implicitly a fact the design should have been stating all
  along**, even when authoring?
- **When a design cannot express an artifact it must amend, is the change refused, or is the
  amendment carried some other way and recorded?**
- **Should an artifact kind that no design can fully express be admissible as an amendment target at
  all?**
- **Who decides that a register is missing — the change that trips over it, or a review of the
  artifact kinds against the registers?**
- **Is "the design states the artifact whole" a rule about the design, or about what construction
  renders?** The two come apart exactly where a register is missing.
