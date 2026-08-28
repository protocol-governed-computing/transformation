# Stage 8 — Authoring Mandate: transformation / build
**Stage:** 8 — Authoring Mandate
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Artifact Authoring

Mechanical. Stage 7's assignments re-ordered into a build sequence; nothing added, nothing dropped.

---

## 1. Build Dependency Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | transformation::VOCAB_FACT_PROVENANCE_V0 | NEW | build | — |
| 2 | 2 | transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | NEW | build | transformation::VOCAB_FACT_PROVENANCE_V0 |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | transformation::VOCAB_FACT_PROVENANCE_V0 |
| 2 | transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 2 | The vocabulary of origins a rendered fact may have, and the transform that reports one origin per leaf. The vocabulary is admitted first because the transform's every answer is drawn from it. |
| EXTEND | 2 | The renderer, which becomes answerable for each value it writes and gains an output carrying one source per leaf; and the measure, whose population is unchanged and whose test becomes provenance rather than presence. |
| REPLACE | 0 | Nothing is stood down. The build manifest already written for a domain that does not exist was removed by hand before this change was raised, and no artifact is superseded by it. |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| transformation::VOCAB_FACT_PROVENANCE_V0 | build |
| transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | build |
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | build |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | build |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0 | Report, for each leaf of a rendered artifact, whether the design stated it, a constitution governs it, or the renderer supplied it | rendered, sources | provenance, governed_by |

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
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Extended by `design`, not here. A phase's registers and the rule set that judges them are that subdomain's. Until its vocabulary register gains a column for the group and one for the spelling, every design scheduling a vocabulary reads short — which is this change refusing correctly, not failing. |
| vocabulary::CONSTITUTION_VOCABULARY_V0 | Unchanged, and named as the authority the new vocabulary is governed by. It carries the rule the first rendered vocabulary was refused against. |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Unchanged. Named because both authored artifacts and all three amendments are compiled under it. |

---

## Gate 2 — Mandate Approval

**Gate 2 closes here**, and it freezes scope before authoring begins. After it, any departure is an
Approved Deviation recorded in the authoring manifest — never a silent change.

**Status: CLOSED.** Approved by the business author against the composition `47dd8edc2123…`, the one
`baseline.json` pins, after Construction Completeness read 100% on all four artifacts.

What is frozen is the vocabulary of origins a rendered fact may have, the transform that reports one
origin per leaf, and the two amendments that make the renderer answerable and the measure test
provenance rather than presence. **The register in which a vocabulary's group and spelling are
stated is outside this mandate** — a phase's registers belong to the design subdomain — and so is
whatever founds a domain the compiler can discover, once construction stops writing manifests.

The mandate is complete and the change cannot yet be emitted, for the reason the change is about.
Amending either transform re-renders it whole, and both carry prose descriptions on themselves and
on each of their fields that no design register may state — the interface register's meaning column
is documentation and is deliberately not rendered, so an amendment necessarily loses them. **This
dossier's own construction is refused by the defect it exists to remove**, which is the sharpest
available statement of why it is worth removing.


---

## Approved Deviation — a fourth origin

**Recorded rather than silent, as Gate 2 requires.**

The design named three origins. Authoring found a fourth it could not do without: a value the artifact
already carried that **no register of the design can express**. Prose descriptions are the case —
`typed_fields` deliberately does not render a field's `Meaning`, because the built corpus carries a
description on some fields and not others, which marks it documentation rather than governed content.
That reasoning holds, and its consequence was that amending any artifact carrying descriptions dropped
every one of them, so the amendment could not state the artifact whole and was refused.

`carried_from_predecessor` closes it. **Preserving is not authoring**: the renderer invents nothing,
it declines to delete what the design has no way to speak about. The origin is recorded per leaf, so
the measure counts it as accounted for rather than as a fact somebody stated, and it is confined to
descriptions — every other omitted leaf is one the design could have stated, and inheriting those
would be the drift this change exists to end, one level down.

This deviation is what made the dossier's own construction admissible. Before it, **the change was
refused by the defect it exists to remove.**
