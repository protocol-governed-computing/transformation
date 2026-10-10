# Stage 8 — Authoring Mandate: transformation / design
**Stage:** 8 — Authoring Mandate
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Artifact Authoring

Mechanical. Stage 7's assignments re-ordered into a build sequence; nothing added, nothing dropped.

---

## 1. Build Dependency Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | transformation::VOCAB_DOCUMENT_STANDING_V0 | NEW | design | — |
| 1 | 2 | transformation::VOCAB_APPROVAL_STANDING_V0 | NEW | design | — |
| 1 | 3 | transformation::VOCAB_CORRECTION_EFFECTIVITY_V0 | NEW | design | — |
| 1 | 4 | transformation::CT_PURE_PARSE_REGISTERS_V1 | NEW | design | — |
| 1 | 5 | transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | NEW | design | — |
| 1 | 6 | transformation::CT_PURE_EVALUATE_RULES_V1 | NEW | design | — |
| 2 | 7 | transformation::CC_JUDGE_DOCUMENT_V1 | NEW | design | transformation::CT_PURE_PARSE_REGISTERS_V1, transformation::CT_PURE_PARSE_PRIOR_PHASES_V1, transformation::CT_PURE_EVALUATE_RULES_V1 |
| 2 | 8 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | NEW | design | transformation::CT_PURE_PARSE_REGISTERS_V1, transformation::CT_PURE_PARSE_PRIOR_PHASES_V1, transformation::CT_PURE_EVALUATE_RULES_V1 |
| 2 | 9 | transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | NEW | design | transformation::CT_PURE_PARSE_REGISTERS_V1, transformation::CT_PURE_PARSE_PRIOR_PHASES_V1, transformation::CT_PURE_EVALUATE_RULES_V1 |
| 3 | 10 | transformation::WF_P0_SEED_ADMISSIBILITY_V1 | NEW | design | transformation::CC_JUDGE_DOCUMENT_V1 |
| 3 | 11 | transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | NEW | design | transformation::CC_JUDGE_DOCUMENT_V1 |
| 3 | 12 | transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | NEW | design | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |
| 3 | 13 | transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | NEW | design | transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 |
| 3 | 14 | transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | NEW | design | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |
| 3 | 15 | transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | NEW | design | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |
| 3 | 16 | transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | NEW | design | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |
| 3 | 17 | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3 | NEW | design | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |
| 3 | 18 | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | NEW | design | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | transformation::CT_PURE_PARSE_REGISTERS_V1 |
| 2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |
| 3 | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| REPLACE | 15 | Three transforms, three judging contracts and nine phase workflows, each stood down by its successor naming it; not scheduled, because nothing is authored for them. |
| EXTEND | 0 | Nothing is extended. Ten artifacts are re-pointed at a successor and keep their identity: the nine phase intents and the construction contract. |
| NEW | 18 | The successors: three transforms and one judging contract rendered from the design; two observing contracts and nine phase workflows reached by invoking the generator §16 of the design declares; and three vocabularies. |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| transformation::VOCAB_DOCUMENT_STANDING_V0 | design |
| transformation::VOCAB_APPROVAL_STANDING_V0 | design |
| transformation::VOCAB_CORRECTION_EFFECTIVITY_V0 | design |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | design |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | design |
| transformation::CT_PURE_EVALUATE_RULES_V1 | design |
| transformation::CC_JUDGE_DOCUMENT_V1 | design |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | design |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | design |
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | design |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | design |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | design |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | design |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | design |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | design |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | design |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3 | design |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | design |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | Read a phase document's header and registers from its Machine block, and its sections from its prose | document_text:string | header:object, sections:array, registers:array |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | Read the upstream phase documents a phase is judged against, each from its Machine block | prior_texts:object | priors:object |
| transformation::CT_PURE_EVALUATE_RULES_V1 | Evaluate a declared rule set against a parsed document, naming the rule set and whether the document's approval holds under it | header:object, sections:array, registers:array, document_text:string, rule_set:array, observed:object, priors:object, rule_set_id:string | verdict:string, findings:array, rules_evaluated:integer, rule_set:string, approval_standing:string |
| transformation::CC_JUDGE_DOCUMENT_V1 | Parse a phase document and judge it against a declared rule set, naming that rule set in the verdict | document_text:string, prior_texts:object, rule_set:array, rule_set_id:string | verdict:string, findings:array, rules_evaluated:integer, rule_set:string, approval_standing:string |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | Parse a phase document and its priors, observe the composition, and judge them together under a named rule set | document_text:string, prior_texts:object, rule_set:array, rule_set_id:string | verdict:string, findings:array, rules_evaluated:integer, rule_set:string, approval_standing:string |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | Parse an analysis loop and its priors, observe the composition's declarations, and judge them together under a named rule set | document_text:string, prior_texts:object, rule_set:array, rule_set_id:string | verdict:string, findings:array, rules_evaluated:integer, rule_set:string, approval_standing:string |

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
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | A build contract re-pointed at the new register reading. It keeps its identity and its own splitting of values inside cells. |

---

## Gate 2 — Mandate Approval

**Gate 2 closes here**, and it freezes scope before authoring begins. After it, any departure is an
Approved Deviation recorded in the authoring manifest — never a silent change.

What is frozen is eighteen artifacts, fifteen stood down and ten re-pointed, and what reaches them:

- **The form.** A phase document carries its header and registers in one YAML Machine block,
  registers as lists of rows keyed by column, values as strings. The reader returns the header,
  sections and registers the table reader returned. Templates and the seed-to-request projection
  write the new form. No reader of tables survives the change.
- **The identity.** One register schema per phase, `registry/schema/SCHEMA_REGISTERS_P<n>_<NAME>_V0.json`,
  holding its `$id`, the digest of the rule set its workflow seals, and its revision history. Its
  shape constraints admit any block until the design unravel fills them under the same `$id`.
  Emission seals the `$id` beside the rule set and refuses a sealed rule set whose digest the
  schema does not record.
- **The verdict.** The judging names the rule set that rendered it, and reports whether the
  document's approval holds under it. The check selects the workflow sealing the rule set a
  document names, and the current one, and reports both verdicts.
- **The standing.** The header names `rule_set`, `approved_under`, `standing` and, for a migrated
  document, `migrated_from`; the vocabularies close their values.

**The proof is inside the freeze, not beside it.** Every test document — the phase corpora, the
end-to-end payloads and the fixture dossiers — is converted once by the table reader and judged in
both forms by the same rule set. The findings are compared by rule, register, row and detail; any
difference is a regression, and the table reader is deleted only when there is none. Each new
transform carries the cases the design declares. A rule-set change without a recorded revision is
refused by emission, and a probe built to do that is part of this mandate.

Outside it: values inside cells keep their text form, the rules stay in their modules, construction
keeps its own splitting of values, and no dossier approved under v5 is read.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, replacements, generation provenance | COMPLETE — GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
