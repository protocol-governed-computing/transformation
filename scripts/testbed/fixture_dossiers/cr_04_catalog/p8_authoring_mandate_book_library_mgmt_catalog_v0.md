# Stage 8 — Authoring Mandate: book_library_mgmt / catalog
**Stage:** 8 — Authoring Mandate
**CR:** cr_04_catalog
**Status:** DRAFT
**Feeds:** Artifact Authoring

Mechanical. Stage 7's assignments re-ordered into a build sequence; nothing added, nothing dropped.

---

## 1. Build Dependency Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | NEW | catalog | — |
| 2 | 2 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | NEW | catalog | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 |
| 2 | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 2 | The successor boundary for a correction, requiring the record named and the details being changed and nothing else, and the successor act it admits. A boundary and an act are each rendered whole, so a requirement is withdrawn by authoring a successor that does not carry it, and an act names its successor boundary by being authored anew. |
| REPLACE | 2 | The boundary that required three things its operation never read, and the act that named it as its entry. Both stood down and superseded; construction marks them rather than deleting them. Nothing consumes the act, so the substitution reaches nothing further. |
| EXTEND | 1 | One boundary re-rendered whole: the publication year is stated as a number. No step of any act changes anywhere in this mandate. |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | catalog |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | catalog |
| book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | catalog |

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
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | A request to register a further edition of a work the catalog already holds | book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 | staff_credentials, authorization_rules, staff_id, title, author, publication_year, subject, edition_fields, edition_schema, work_fields, work_schema |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | A request to change a registered book's description | book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1 | staff_credentials, authorization_rules, staff_id, identity_key, updated_fields |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| book_library_mgmt::IN_REGISTER_BOOK_V0 | Requires ten things where its act reads eleven, and is not corrected here. The act reads the subject at the top of the request; every present caller sends it nested inside the details of the book. Correcting the boundary moves every caller with it, which this change's seed forbids. Deferred with its ground recorded, to a change where both move together. |

---

## Gate 2 — Mandate Approval

**Gate 2 closes here**, and it freezes scope before authoring begins. After it, any departure is an
Approved Deviation recorded in the authoring manifest — never a silent change.

**Status: CLOSED.** Approved by the business author against the composition `10aa26e1582f…`, the one
`baseline.json` pins, after Construction Completeness read 100% on all six artifacts and no amendment
was found to narrow what it replaces.

What is frozen is two statements of what a catalog operation needs from the person performing it,
brought into agreement with what each operation reads. One boundary is re-rendered whole; one
boundary and the act it admits are superseded, because a requirement is withdrawn by authoring a
successor rather than by amending a predecessor to say less than it said. **A requirement changed by
editing a built artifact is outside this mandate**, and so is the third defect of this subdomain,
which is deferred with its ground recorded because correcting it moves every caller of the boundary
that registers a work.
