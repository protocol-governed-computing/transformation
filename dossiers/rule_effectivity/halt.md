# Halt — rule_effectivity

**Phases reached:** P0 – P6, every one admissible
**Status:** HALTED at P7, for a cause this dossier does not own
**Blocked by:** `transformation/dossiers/generated_artifacts`
**Do not:** author a partial P7, or amend the nine phase artifacts directly

---

## Why it stops

This change amends nine artifacts: the phase workflows that render verdicts, each of which must name
the rule-set version it judged against, and one of which gates the approval that must pin a version.

Those nine are **generated**. Each carries a sealed copy of a rule set produced from a template and a
declaration read together. A design cannot say *"this artifact is reached by invoking that
generator"*, because no register in P7 names how an artifact is reached.

The design is complete and sound. The language to express its delivery does not exist yet.

## This is the second dossier to stop here, and that is the point

| dossier | phases | why it stopped |
|---|---|---|
| `generated_artifacts` | P0–P6 | P7 cannot name a generator — the gap it exists to close |
| `rule_effectivity` | P0–P6 | the same, for the same nine artifacts |

Two independent changes, designed separately, stopped at one wall for one documented cause. Neither
was bent to fit. That is the evidence for the delivery order recorded in the handoff:
`generated_artifacts` is delivered first, by hand and once, and every lifecycle change after it is
deliverable through the pipeline.

## What must not happen

The nine artifacts could be edited directly. This dossier's own boundary rules do not forbid it —
that prohibition belongs to `generated_artifacts` — but doing so would deliver this change by
violating the change that is meant to precede it, and would make the second delivery indistinguishable
from the first.

Equally, this dossier must not be delivered *before* `generated_artifacts`. The chain in its own P3
holds within this change; the chain between changes holds too, and this one is second.

## Resuming

When `generated_artifacts` is delivered, this dossier resumes at P7 with no design decision
reopened. Its seven gaps are settled, its seven boundary rules are stated, and Gate 1 is approvable
on the record as it stands.

One thing to carry forward when it resumes: **the two corrections made during this session are the
first instances the declaration must describe** — one non-retroactive (a diagnostic message that
changed no verdict) and one retroactive (a required column that invalidated every dossier then in
existence). Design decision #7 commits to recording both retrospectively. They are the only cases
whose effect is already known, and they are the change's own first test.
