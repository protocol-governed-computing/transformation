# Stage 8 — Authoring Mandate: book_library_mgmt / catalog
**Stage:** 8 — Authoring Mandate
**CR:** cr_03_catalog
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
| EXTEND | 6 | The six acts that complete a declared moment, each re-rendered whole so that it announces what it completed. One of them announces three. |
| NEW | 0 | The change authors no artifact. All six moments were declared long ago and referenced by nothing; what was missing was the acts saying they had completed them. |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| book_library_mgmt::WF_REGISTER_BOOK_V0 | catalog |
| book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | catalog |
| book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0 | catalog |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | catalog |
| book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0 | catalog |
| book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0 | catalog |

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

**Status: CLOSED.** Approved by the business author against the composition `9c2c693d882e…`, the one
`baseline.json` pins, after Construction Completeness read 100% on all six acts.

What is frozen is six acts and what each announces. The acts are re-rendered whole from the design,
which is what an EXTEND means, so nothing about them is edited in place and the announcements arrive
with the rendering. **A moment announced by editing a built artifact is outside this mandate** — and
so is a moment the business never declared, which is why neither reinstatement act is here.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, topology, bindings, announcements | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
