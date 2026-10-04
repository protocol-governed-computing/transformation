# Stage 8 — Authoring Mandate: transformation / design
**Stage:** 8 — Authoring Mandate
**CR:** refusal_discharge
**Status:** DRAFT
**Feeds:** Artifact Authoring

Mechanical. Stage 7's assignments re-ordered into a build sequence; nothing added, nothing dropped.

---

## 1. Build Dependency Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| NONE IDENTIFIED |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| NONE IDENTIFIED |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| EXTEND | 3 | The phase workflow that seals the rule set judging a design, the contract that observes the composition a design is judged against, and the transform carrying the check kinds the rules are built from — all three reached by invoking the generator §16 declares, and none of them written. |
| NEW | 0 | The change authors no artifact. What it adds is two registers of the design language, five rules and two check kinds, and every one of those is a source of an artifact that already exists. |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | design |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | design |
| transformation::CT_PURE_EVALUATE_RULES_V0 | design |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| NONE IDENTIFIED |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| NONE IDENTIFIED |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| NONE IDENTIFIED |

---

## Gate 2 — Mandate Approval

**Gate 2 closes here**, and it freezes scope before authoring begins. After it, any departure is an
Approved Deviation recorded in the authoring manifest — never a silent change.

**Status: CLOSED.** Approved by the business author against the composition `6e1e571dbbb8…`, the one
`baseline.json` pins. Construction Completeness is not cited because it does not apply: §3 records
zero NEW, and the three EXTEND artifacts are re-emitted by their generator rather than rendered from
a register.

What is frozen is the amendment set and the way it is reached: three artifacts, none authored, all
three re-emitted by the generator §16 declares. What reaches them is two registers appended to the
design intent template, five rules in that phase's rule module, two check kinds, one existing check
kind gaining an optional parameter, and the seed added to the phase's declared priors. A rule written
by hand into the sealed rule set is outside this mandate however correct it looks, and so is a check
kind added without a rule that uses it.

**The probes are inside the freeze, not beside it.** Five rules are authored and no document in the
corpus states a discharge, so each would report clean on its first run while checking nothing. One
probe per rule, each built to fail, is part of what this mandate schedules — not a follow-up someone
may decide the green has made unnecessary.

**Declaring a prior is not free, and what it costs is frozen here too.** The six existing P7 payloads
in the phase testbed carry `p5` and `p6`. Adding the seed to the phase's declared priors makes every
one of them a run missing a prior it declares, which the phase reports as an unchecked handoff rather
than passing quietly. Supplying `p0` to those six is inside this mandate: it authors nothing, changes
no rule and alters no verdict that was correct before. **A payload whose verdict changes is not
covered by this paragraph** — that is a rule firing on an existing document, and it is a finding.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, amendments, generation provenance | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
