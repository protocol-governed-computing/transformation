# Closure — founding_design_bootstrap

**CR:** the founding change that established `transformation / design`
**Phases reached:** P0 – P2
**Outcome:** IMPLEMENTED OUTSIDE THE GOVERNED CONSTRUCTION PATH — a bootstrap exception
**Superseded for lifecycle purposes by:** `generated_artifacts`
**Status of this dossier:** read-only historical evidence. Do not resume, amend or re-judge it.

---

## What this dossier is

The founding change request for the `design` subdomain — the pipeline that decides which changes are
admissible. Its classification reads `design | NEW_SUBDOMAIN`, and its purpose paragraph states the
boundary it established: *the pipeline that decides which changes are admissible is a distinct
concern from the capabilities it admits, and needs its own governance boundary.*

It was previously named `new_subdomain`, which read as a category of change — a template for adding
any subdomain — and it is not that. It is one specific CR, about one specific subdomain, and the
name invited exactly that misreading.

## What happened, stated exactly

**The change was delivered. The dossier's pipeline path was not.**

The design subdomain exists, compiles, and judges every change made since. What stopped at P2 was the
governed route to it, not the work. To carry this dossier further, someone would have had to author a
phase's rule sets — and those are a template plus code, from which the workflow artifacts are
generated. No design register has a shape that carries a nested rule set, and an artifact rendered
from such a design would be overwritten by the next emission.

So the founding change was implemented by hand, correctly, while the dossier described the intent and
stopped. That is a **bootstrap exception**: a lifecycle cannot govern its own creation, because the
thing that would govern it is what is being created.

## Why this is not abandoned

**Abandoned** is a real terminal state and is reserved for it: work that stops, delivers nothing, and
has no successor. It preserves history and prevents a change vanishing silently from the record.

This is none of those. It delivered its intended system, and it has a successor that owns the gap
which stopped it. Calling it abandoned would blur a state that must stay sharp, and would also assert
something false — that nothing came of it.

## What the successor owns

`generated_artifacts` owns the reason this dossier could not proceed: the lifecycle governs authored
artifacts and has no account of generated ones. That is the gap which must close before any change to
a phase's rule sets can be delivered through the pipeline rather than beside it.

`rule_expressiveness` hit the same wall later, from the other direction, and closed at Gate 1 for the
same reason. Two dossiers, one cause, recorded once — in the successor.

## The missing baseline pin

This dossier carries no `baseline.json`, and none is to be added.

A pin names the composition a change is validated against. At the time this change was made there was
no pinned-baseline discipline to observe, because the pipeline that enforces it is what this change
created. The absence is a **historical limitation of the bootstrap**, not a defect to retrofit.
Adding one now would assert a validation that never happened, against a composition this dossier
never saw — the same error as amending a closed CR to satisfy later rules.

## Reading it

The three documents are evidence of what was intended and how the boundary was reasoned, at the
moment the pipeline came into being. They are not a specification of the design subdomain as it now
stands; the artifacts are that. Read them for the argument, not for the inventory.
