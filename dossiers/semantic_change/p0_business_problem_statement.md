# Business Problem Statement

**Project Name:** transformation — semantic change

## 1. Context

A change to the composition either restates an artifact under the identity it has, or gives it a new
identity that stands in for the old one. The open standard decides which: a change to what an
artifact means is a new identity, and a change to how it is written keeps the one it has. The
platform now declares which parts of a declaration carry no meaning, so the two can be told apart.

Nothing in how a change is designed or built uses that. A design may restate an artifact with a
different meaning under its old identity, and construction builds it. Every change of the last cycle
did exactly that.

The platform's declaration says less than the standard. It does not say which parts of a
declaration name another artifact. So re-pointing a reference reads as a change of meaning, and every
replacement would ripple through every artifact above it. It also does not say that a part declared
explanation is exempt only where it holds text.

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

- have the platform declare which parts of a declaration name another artifact, and that a reference
  now naming the declared successor of what it named is not a change of meaning;
- have the platform declare that a part declared explanation is exempt only where its value is text;
- refuse to build an amendment that changes what an artifact means;
- let a design re-point a reference to a replaced artifact without restating the artifact that holds
  it;
- refuse to build a design that leaves a reference to an artifact it replaces unaccounted for.

### What the business already decided

These are settled and are not reopened by this change:

- **A change of meaning is a new identity; a change of how it is written is not.**
- **What carries no meaning is what the platform declares, and nothing else.**
- **A reference to a replaced artifact is re-pointed or retired.** Re-pointing keeps the referring
  artifact's identity.
- **A caller outside the composition moves itself.** A change lists the callers it knows of.

---

## 3. Clarifications answered by the business author

- **Is a part the platform declares explanation exempt when it holds data?** No. It is exempt only
  where its value is text.
- **Is the platform's declaration amended in place?** No. Adding to what it says changes what it
  means, so it is replaced by a new version, under the rule this change builds.
- **Does this change decide which past changes altered meaning?** No. That is the next change, and it
  uses what this one builds.
- **Does this change compare a whole composition with the one last cited?** No. That comparison
  belongs to the release process.
