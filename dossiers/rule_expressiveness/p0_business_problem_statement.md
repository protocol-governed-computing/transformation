# Business Problem Statement

**Project Name:** transformation

## 1. Context

The transformation lifecycle governs how a protocol-governed system changes. A change is carried
through nine phases, and each phase is judged against a rule set the phase itself declares — at
present 751 rules resolving against 42 kinds of check. The rule sets are governed artifacts, so the
lifecycle that governs change is itself declared in the same artifact language as the businesses it
governs.

A rule can only be written if the rule language can say it. Three things it cannot say were found by
carrying a real change — a blockchain wallet — through the phases and watching what the pipeline
failed to notice.

---

## 2. Problem Statement

**The rule language cannot express three things the lifecycle depends on, so three classes of defect
pass unnoticed.**

**A change cannot say which subdomains it touches.** A change request states what kind of change it
is — new, extension, modification, retirement — but not what it is a change *to*. When one change
touches two subdomains it states two kinds, and nothing says which kind applies to which subdomain.
The consequence is not cosmetic: a subdomain can be changed by a CR that never states its purpose
and never declares who owns it, and every phase passes. That is exactly what happened. A wallet
change also modified the identity function, and identity received no statement of what must be true
of it afterwards and no declared owner — while the dossier was admissible at every phase.

**A dependency on something that exists and must change cannot be expressed.** A change records what
it depends on and how each dependency is disposed of: it exists, it is reused, it is authored new, or
it is still being investigated. There is no way to say *it exists and this change alters it*. The
same phase decides exactly that, one register later, and records it — so the pipeline holds both
statements and cannot reconcile them. Recording such a dependency as merely existing is true and
loses the entire point.

**No rule can say how many rows a register may have.** A register can be required to be present, to
have columns, and to be non-empty. Nothing can say it has exactly one row, or at most one. So a
register meant to carry a single answer can carry three contradictory ones and no rule anyone could
write today would catch it.

This change shall:

- let a change request state which subdomains it touches and what kind of change each receives;
- require that every subdomain a change touches has its purpose stated and its owner declared;
- let a dependency be recorded as existing and altered by this change;
- let a rule constrain how many rows a register has.

### What a caller sees

Nothing runs here, so nothing is served differently. What changes is what the pipeline refuses.
Documents that were admissible and incomplete become inadmissible and say why.

### What this change does not decide

- **Whether one change may touch several subdomains.** It may. This change makes it stateable, not
  permissible — it was already happening.
- **Whether a change request may carry more than one classification.** It may, and it did before this
  change. What is added is which subdomain each classification applies to.
- **How many rows any particular register should have.** This change makes the constraint
  expressible. Where to apply it is a separate judgement, made per register.
- **Anything about the construction half of the lifecycle.** Only the phases that judge a design.

### Left for later changes

- **Changes that span two domains**, rather than two subdomains of one domain. Nothing has needed it
  yet, and a span that has never occurred is a span nobody can specify honestly.
- **Applying a row-count constraint to registers other than the one this change names.** Each is its
  own judgement about what that register means.

---

## 3. Clarifications answered by the business author

These questions were put to the business author and answered by them. The design process did not
assume them.

- **May one change touch more than one subdomain?** Yes. It already does, and the pipeline should
  state it rather than absorb it silently.
- **May a change request carry more than one classification?** Yes. A change that creates one
  subdomain and modifies another is two kinds of change, honestly stated.
- **Should the subdomain a classification applies to be stated on the classification itself, or
  declared separately?** On the classification itself. A separately declared list of subdomains and
  a separately declared list of kinds can drift apart; one row carrying both cannot.
- **Should the span of a change be derived or declared?** Derived. If each classification names its
  subdomain, the set of subdomains touched is whatever those rows say, and there is nothing second
  to keep in agreement.
- **What follows for a subdomain a change touches?** Its purpose is stated and its owner is declared,
  the same as for any other subdomain the change touches. A subdomain changed without either is the
  defect this change exists to catch.
- **Is a dependency that exists and is altered a new kind of disposition, or a different register?**
  A new disposition. The register already records what a change depends on; what was missing is one
  of the ways a dependency can be disposed of.
- **Where should a row-count constraint be used first?** Nowhere by default. The ability to state it
  is what was missing. Applying it is judged per register, and this change applies it to none.
- **Is this a change the business is adding, or a correction?** A correction. Each of the three is
  something the lifecycle already relies on and cannot state.
