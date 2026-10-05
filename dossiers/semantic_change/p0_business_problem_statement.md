# Business Problem Statement

**Project Name:** transformation — semantic change

## 1. Context

A change to the composition either restates an artifact under the identity it has, or gives it a new
identity that stands in for the old one. The open standard decides which: a change to what an
artifact means is a new identity, and a change to how it is written keeps the one it has. The
platform declares which parts of a declaration carry no meaning, which parts name another artifact,
and the rules a comparison applies. So the two can be told apart.

Nothing in how a change is designed or built uses that. A design may restate an artifact with a
different meaning under its old identity, and construction builds it. Every change of the last cycle
did exactly that.

Construction does compare an amendment with what it amends, but only for what the amendment would
lose. It does not look for what it adds or alters. It lets a design withdraw a fact, which is itself a
change of meaning. And it skips the comparison entirely when it is not handed the composition.

When a change does give an artifact a new identity, everything that refers to the old one must be
pointed at the new one, or retired with it. A design can do that today only by restating each
referrer whole, and some referrers cannot be restated in the design language. Nothing in the design
says what the change reaches. The build finds out late, when the compiler refuses a reference to an
artifact that has been stood down.

---

## 2. Problem Statement

**A change of meaning can be built under an old identity, and a change that does give a new identity
cannot say, or carry out, what it reaches.**

This change shall:

- refuse to build an amendment that changes what an artifact means, by the platform's declaration;
- refuse to build an amendment it cannot compare with the composition;
- stop letting a design withdraw a fact from an artifact it amends;
- let a design re-point a reference to a replaced artifact without restating the artifact that holds
  it;
- refuse to build a design that leaves a reference to an artifact it replaces unaccounted for.

### What the business already decided

These are settled and are not reopened by this change:

- **A change of meaning is a new identity; a change of how it is written is not.**
- **What carries no meaning, what names another artifact, and how two declarations are compared are
  the platform's declaration, and nothing else.**
- **A reference to a replaced artifact is re-pointed or retired.** Re-pointing keeps the referring
  artifact's identity.
- **A caller outside the composition moves itself.** A change lists the callers it knows of.

---

## 3. Clarifications answered by the business author

- **Does this change decide which past changes altered meaning?** No. That is the next change, and it
  uses what this one builds.
- **What happens to the designs that withdrew facts?** They changed meaning. The next change re-cuts
  them.
- **Does this change compare a whole composition with the one last published?** No.
