# Business Problem Statement

**Project Name:** transformation

## 1. Context

A change of meaning is a new identity. When an artifact is replaced, its successor names it, it is
stood down, and whatever named it is re-pointed at the successor. A released composition is sealed
with every identity it holds, archived at its tag and cited by its DOI.

The standard bounds what must be kept. A superseded thing is retained only while a retention
condition holds. Once none holds, a person may delete it, and the deletion is a governed act whose
record names the deleted identity, the person who decided, and the determination that no retention
condition held.

The platform is in development. No release is a stable baseline yet, and no consumer depends on the
live tree: a consumer of a release uses the release, at its tag.

---

## 2. Problem Statement

**Every replaced version is carried forever, though nothing runs it.**

Thirty-three artifacts in the live tree are stood down today, across eight domains. Nothing executes
them. They are carried because the checks assume that a replaced version stays:

- the check that a published identity still means what it meant treats an identity the live tree no
  longer holds as a finding, so a published version can never leave;
- the check that each supersession is stated the same way on both sides needs both sides present;
- the check that every transform's implementation exists keeps the code of a stood-down transform
  alive;
- a stood-down artifact that names another keeps that one alive too, so one replacement holds a chain.

The cost is real. A change that retires a piece of code cannot delete it while a stood-down artifact
still names it. The format change is waiting on exactly this: the readers it replaces are
implemented by the reading it retires, and two stood-down judging contracts, bound by seven
stood-down phase workflows, still name them.

Nothing records a deletion, and nothing states when retention applies. Whether to keep a version is
assumed in code, not declared.

### This change shall

- declare when a replaced version is retained, once, where every check reads it: during
  development, nothing in the live tree is retained for its own sake;
- let a replaced version be deleted by a recorded human act, the record naming what the standard
  requires;
- make every check accept a deletion so recorded, and refuse one that is not recorded;
- ensure a deleted name is never used again;
- delete the stood-down versions of this domain that nothing needs, each with its record.

### What a caller sees

The live tree holds what runs. A replaced version is gone from it, its deletion is on record, and
its name stays retired. A released composition still holds every identity it was sealed with.

### Constraints decided by the business

- **The standard does not change.** It already bounds retention and defines deletion. This change
  realizes it.
- **Identity and succession stay mandatory.** A change of meaning is still a new identity, and a
  replaced version still names its successor before it goes.
- **A deleted name is never reused.** Releases are cited by the identities they hold.
- **Releases are untouched.** A sealed release keeps every identity it holds, at its tag.
- **Development ends at a declared point.** When a stable baseline is declared, retention conditions
  begin to bind, by changing the declaration rather than the code.

### What this change does not decide

- **What retention conditions apply after development.** That is decided when a stable baseline is
  declared.
- **The form a phase document carries its facts in.** That is the format change, which waits for
  this one.

### Left for later changes

- **Declaring the first stable baseline.**
- **Deleting other domains' stood-down versions.** Each domain deletes its own, in its own change,
  under the declaration this change makes. A change made here acts only on what this domain owns.
