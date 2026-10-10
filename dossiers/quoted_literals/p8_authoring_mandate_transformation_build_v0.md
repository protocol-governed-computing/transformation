# Stage 8 — Authoring Mandate: transformation / build
**Stage:** 8 — Authoring Mandate
**CR:** quoted_literals
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
| REPLACE | 0 | Nothing is replaced. |
| EXTEND | 0 | Nothing is extended. The render transform's declaration states nothing about how a literal is rendered, and is unchanged. |
| NEW | 0 | The change authors no artifact. It corrects the render transform's implementation. |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | build |

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

What is frozen is one correction to the rendering of a binding: a value opening and closing with
the same quote mark renders as the text between them, and a number with a decimal part renders as a
number. The shared reading of a value, which renders a field's default and an artifact's property,
is outside this mandate, and so is any artifact's declaration.

**The probes are inside the freeze.** The keyed-node probe expects each recorded reason as its value,
and one probe renders a quoted dotted value and a decimal. Every artifact construction reproduces
today must reproduce unchanged; one that moves is a finding, not a cost.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, design resolution | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
