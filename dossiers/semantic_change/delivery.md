# Delivery — semantic_change

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `2c5eac6de01d…`
**Delivered:** a change of meaning can no longer be built under an old identity. Construction
compares every amendment with the composition by the platform's declaration, refuses an amendment
it cannot compare, and refuses a replacement whose referrers the design leaves unaccounted for. A
design may re-point a reference and may not withdraw a fact. Inspection reports every referrer the
composition records.
**Validated:** `semantic_change_design_test` 17/17; `test_inspector` 152/152; full regression
`--all` 65/65 as expected

---

## What this change closed

- **M1, a change of meaning.** Construction compared an amendment only for the facts it would lose.
  It now compares the whole declaration with what the composition holds, through
  `artifact::VOCAB_DECLARATION_REPRESENTATION_V1`: explanation is ignored where it is text, a list
  declared unordered is a set, and a reference may stay as it was or name its declared successor.
  Any other difference is refused, by place. A generated amendment is compared too, from the
  generator's preview, before anything is written. Construction refuses to compare when the
  declaration names a rule it does not apply.
- **An uncompared amendment.** `check` printed a note without `--snapshot` and admitted the design,
  and `emit` never compared at all. Both now refuse a design that amends, replaces or re-points
  without the composition, and both compare before writing.
- **A withdrawal.** P7 refuses any row in `withdrawn_facts`. The register stays declared, so the
  registers every phase may cite are unchanged.
- **M2, a re-point.** P7 admits `REPOINT`. Construction rewrites, in the artifact's Machine block,
  each name of what the design replaces to its one declared successor, and refuses a re-point that
  moves anything but references.
- **M3, reach.** For each `REPLACE` row, every live referrer must be replaced, amended or
  re-pointed by the design, or construction refuses and names it.
- **Inspection.** `si.artifact.refs` walked the evidence graph only, which keeps addressed nodes and
  edges within a domain. Of the 1,008 references the composition records it missed 342, all into 17
  artifacts — `CONSTITUTION_CAPABILITY_CONTRACT_V0` was reported referred to by 1 of 73. The
  inspector's graph now adds the record of references, so `refs` and `si.topology.impact` see them.

---

## What it took

**The change follows the rule it builds.** Its rules for judging a design changed, so
`transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0` is stood down for `_V1`. No phase workflow
is determined by a design, so V1 was named in the design and not scheduled: its places, inputs and
binding were carried by hand from V0, and `emit_rule_sets`, now mapping P7 to V1, wrote its rules,
routing and provenance. V0 was marked stood down by hand, and
`transformation::IN_DESIGN_INTENT_SUBMITTED_V0` re-pointed by hand, because a design can re-point
only once this change's rules are sealed. Construction measured 0 of 0 facts, a count over nothing.

**Removing the withdrawal register would have changed six other phases.** P1 to P6 each seal the
registers a citation may resolve to. Retiring `withdrawn_facts` changed all six rule sets, so the
register stays and P7 refuses a row in it.

**The figures behind the inspection finding were corrected.** The first count read how often a
part holds any full name as how often one artifact is named. The record was measured directly, per
artifact, and P2 was corrected before Gate 1.

**The code it touched:**

- `transformation`: `build/sameness.py` (new); `cli.py` (the meaning gate in `check` and `emit`,
  re-points, reach); `build/completeness.py` (the narrowing comparison removed); `build/generators.py`
  (a preview per generator); `design/emit.py` (preview, P7 mapped to V1); the P7 template and rules.
- `snapshot_inspector`: `inspector/graph.py`.
- `withdrawal_design_test` retired; `semantic_change_design_test` added; `e2e_phases_test` and
  `differential` name V1.

---

## What is carried

- **External callers of the design workflow.** `design/emit.py`'s phase map, `e2e_phases_test` and
  `differential` name `WF_P7_…_V1`. Construction reads
  `artifact::VOCAB_DECLARATION_REPRESENTATION_V1` by exact identity in `build/sameness.py`.
- **Short-code references are not in the record.** A replaced artifact named only by short code is
  not found by the reach check. The compiler's reach check still refuses it when the composition is
  built.
- **Designs that withdrew facts.** Blockchain `cr_05`, book_library_mgmt `cr_05` and CLM `cr_02`
  would now be refused if rebuilt. They are the re-cut's.
- **A partly re-pointed set.** A set naming several replaced artifacts, re-pointed for only some of
  them, reads as a change of meaning.
