# Closure — register_coverage

**Phases reached:** P0 only
**Status:** CLOSED UNBUILT, by ruling. This dossier is not carried forward
**Subject:** whether a design can state, for an artifact it amends, every fact that artifact carries
**Evidence:** `transformation/doc/REGISTER_COVERAGE_VERIFICATION.md`

---

## Why it closes

The dossier rests on observed instances of one pattern: *a fact the authoring path never had to state
because authoring supplies it, and the amending path must state and cannot.* It was closed by
checking each instance against the design language as it now stands, rather than by deciding the
pattern was uninteresting.

```
build configuration cannot be amended   still true · intentionally implicit
amended artifact cannot state its
  subdomain                             no longer true
vocabulary that extends nothing
  cannot say so                         no longer true
```

**Two of the three named instances were closed by work done since, and neither closure was recorded
against this dossier** — which is why it read as parked rather than as two-thirds delivered.

- An amended artifact states its subdomain in `p8.field_declarations`, the renderer reads it from
  there, and `AMENDED_ARTIFACT_UNPLACED` refuses an `EXTEND` artifact that is missing from it.
- A vocabulary that extends nothing says so with a declared-emptiness sentinel in `Extends`, which
  the renderer distinguishes from an unfilled cell.

**The P0 says four instances and names three.** There is no fourth paragraph. Whether one was dropped
in authoring or the count was never right cannot be established now, and the dossier does not turn on
it — the three that are named are the three that were checked.

## What does not close, and why it is not this dossier

No register holds a build configuration's fields — 56 leaf facts, and `p6.storage_governance`,
`p7.structure_stores` and `p8.build_order` between them hold none of them. That much of the P0 is
still true.

What has changed is that the facts are not lost. `render.build_manifest` derives the artifact whole
and construction acceptance compares the derived manifest against the built one on every run, with no
differences. **And the P0's own example no longer holds:** subdomain plurality is derived from the
distinct `Subdomain Field` values a mandate declares, so a change adding a second subdomain states it
exactly the way it states the first.

The residue is a different question from the one this dossier asks. It is not *"the amending path
cannot state a fact"*; it is **whether an artifact every field of which is compiler configuration
belongs in the design language at all, or belongs to the generator that derives it** — the question
`generated_artifacts` settled for artifacts whose source of truth is a generator, asked now of one
that is configuration rather than behaviour.

That question is raised when a change forces it. **No change has yet amended a build configuration**,
so there is no evidence to rule on and no design to judge. Holding a dossier open against a question
its P0 does not ask, for evidence that does not exist, is how a fork becomes something nobody can
close.

## What must not happen

This closure is not a finding that the design language is complete for amendment. It is a finding
that the three instances that were named are two closed and one differently framed. **A fourth
instance found by carrying a real change to construction is a new dossier, not a reopening of this
one** — a closed dossier is evidence and is never amended.
