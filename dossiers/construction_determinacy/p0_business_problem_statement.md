# Business Problem Statement

**Project Name:** transformation — build

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed business
> requirement and the execution path a change would take. It is not a design.

## 1. Context

Construction renders artifacts from an approved design. Before it writes anything it measures the
design: a fact the design does not state is a fact the renderer would have to invent, and a renderer
that invents design is a second design authority nobody approved. The measure refuses anything below
complete, so the design determines the artifact and the renderer only writes it down.

## 2. Problem Statement

**The measure counts what the renderer asks the design for, not what the artifact needs — so a
renderer that never asks can invent freely and still measure complete.**

**A vocabulary was rendered with a name and a rule the design never stated.** A change designed a
vocabulary of seven values. The renderer wrote them under a group name and a spelling rule taken from
two literals in its own text, identical for every vocabulary it will ever write. The values are
lowercase and the rule it applied says they must be upper case, so the platform refused the artifact
when it was next built. The measure had read the design complete, because the group name and the
spelling rule are not among the facts it counts.

**A build manifest was written for a domain that does not exist.** The same construction wrote a
second artifact nobody designed: a manifest declaring the subdomain of the change to be a business
domain in its own right, importing the platform. The subdomain is part of the platform. The manifest
was inferred from where the change happened to sit, and the measure did not count it because nothing
in the design named it.

**Both are the same act.** The renderer supplied a fact the design did not state, and the measure
that exists to prevent exactly that reported complete. What the measure counts is derived from the
shape the renderer emits, so a fact the renderer sources from a literal or from a path is invisible
to it by construction.

## 3. Why This Surfaced Now

**Construction had never written to disk before.** The renderer produced a shape the acceptance
harness compared against artifacts written by hand, and a hand-written artifact carried the group
name, the spelling rule and the manifest without anyone noticing they were absent from the design.
Emitting made the renderer the author, and the invented facts became the artifact.

**Both instances came from one change, on its first emit.** They are what one design of one new
vocabulary in one subdomain was enough to surface.

## 4. What This Is Not

**It is not a case against the measure.** Refusing an under-determined design is right, and the
threshold is right at complete. What is wrong is that the measure's population is derived from the
renderer rather than from the artifact, so the two can only ever agree.

**It is not a defect in the change that found it.** The design stated everything it was asked for and
measured complete. Nothing it could have said would have supplied a fact the measure does not count.
