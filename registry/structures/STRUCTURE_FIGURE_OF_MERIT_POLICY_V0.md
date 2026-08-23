# STRUCTURE_FIGURE_OF_MERIT_POLICY_V0

## 1. Intent

What a phase document loses a star for, and how much.

**Superseded by `STRUCTURE_FIGURE_OF_MERIT_POLICY_V1`.** Four of this version's `open_hole` row
terms score values that a rule now refuses outright, which counts one defect twice. V1 removes them
and states the categories that decide what belongs in a `rows` term at all. Kept as the version the
compositions before it were rated against.

The figure of merit is **not** the verdict. Admissibility is decided by a phase's rule set and by
nothing else; this policy says how good an artifact is once judged. The two axes are independent in
both directions: an admissible document can rate poorly because it carries declared open questions,
and an inadmissible one can rate well because a single misspelled citation is fatal to
admissibility while costing little in quality. Collapsing them would make the rating a second,
softer gate, which a governed pipeline must not have.

Scoring is **deduction-based**: every artifact begins at the maximum and loses ground only against
declared evidence. Nothing has to earn its stars, so an artifact is presumed excellent until
something objective says otherwise — and every star lost names the reason it was lost.

## 2. Why this is declared rather than coded

What is deducted, and why it matters, is governance. Only *how* the arithmetic runs is
implementation. Holding the weights in Python would make the quality bar a property of a build
tool — unversioned, unreadable from the composition, and changeable without a governed act.

Changing a weight is therefore a change to this artifact, and a change to this artifact is a new
version like any other.

## 3. Deductions

| Deduction | Weight | What it catches |
|-----------|--------|-----------------|
| `identity_unresolved` | 2 | A citation that resolves to nothing really in the composition — a misspelling or a wrong namespace. Weighted double because a wrong identity propagates: every later phase reads it as established fact. |
| `register_incomplete` | 1 | A declared register that did not arrive intact. |
| `finding` | 1 | Any remaining rule finding. |
| `open_hole` | 1 | A declared governed hole. Not a defect — it is the legal alternative to guessing — so it is surfaced and scored rather than rejected. |

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation
superseded_by:
- transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1

core:
  summary: Deterministic figure of merit for a phase document — deduction-based, 0 to 5
  maximum: 5
  minimum: 0
  deductions:
  - id: identity_unresolved
    label: Identity unresolved
    weight: 2
    findings:
    - BASELINE_IDENTITY_UNRESOLVED
    - VERIFIED_BELIEF_IDENTITY_UNRESOLVED
    - CITED_ALTERNATIVE_UNRESOLVED
    - DEPENDENCY_IDENTITY_UNRESOLVED
  - id: register_incomplete
    label: Register incomplete
    weight: 1
    findings:
    - REGISTER_MISSING
    - REGISTER_EMPTY
    - REGISTER_COLUMN_MISSING
  - id: finding
    label: Findings
    weight: 1
    remaining_findings: true
  - id: open_hole
    label: Open questions
    weight: 1
    rows:
      registers:
      - open_questions
      - clarification_requests
      columns:
        Resolution Status:
        - OPEN
        Blocking:
        - 'YES'
        Status:
        - NOT_SATISFIED
        Result:
        - INSUFFICIENT_EVIDENCE
        Identity Field:
        - UNRESOLVED
        Uniqueness Rule:
        - UNRESOLVED
        Source:
        - UNRESOLVED
```

---

## 4. Not ported from RI-0

RI-0 deducted a star when an iterative worker loop ended forced, at max-iterations, or stalled.
PGC's phases are deterministic and single-shot: there is no loop, so convergence is *undefined*
rather than *failed*. RI-0's own note is explicit that undefined convergence must not be penalised,
so the deduction is absent here rather than carried across as a term nothing could ever trip.
