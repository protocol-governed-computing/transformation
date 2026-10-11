# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_04_catalog
  Status: DRAFT
  Feeds: Artifact Authoring
registers:
  build_order:
    columns:
    - Wave
    - Step
    - Code
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Depends On
    rows:
    - Wave: '1'
      Step: '1'
      Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: —
    - Wave: '2'
      Step: '2'
      Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: catalog
      Depends On: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    - Position: '2'
      Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '2'
      Description: The successor boundary for a correction, requiring the record named and the details being changed and nothing else, and the successor act it admits. A boundary and an act are each rendered whole, so a requirement is withdrawn by authoring a successor that does not carry it, and an act names its successor boundary by being authored anew.
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Count: '2'
      Description: The boundary that required three things its operation never read, and the act that named it as its entry. Both stood down and superseded; construction marks them rather than deleting them. Nothing consumes the act, so the substitution reaches nothing further.
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '1'
      Description: 'One boundary re-rendered whole: the publication year is stated as a number. No step of any act changes anywhere in this mandate.'
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Subdomain Field: catalog
    - Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Subdomain Field: catalog
    - Code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Subdomain Field: catalog
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: NONE IDENTIFIED
      Purpose: ''
      Inputs: ''
      Outputs: ''
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows:
    - Code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Purpose: A request to register a further edition of a work the catalog already holds
      Workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      Inputs: staff_credentials, authorization_rules, staff_id, title, author, publication_year, subject, edition_fields, edition_schema, work_fields, work_schema
    - Code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Purpose: A request to change a registered book's description
      Workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      Inputs: staff_credentials, authorization_rules, staff_id, identity_key, updated_fields
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: book_library_mgmt::IN_REGISTER_BOOK_V0
      Note: Requires ten things where its act reads eleven, and is not corrected here. The act reads the subject at the top of the request; every present caller sends it nested inside the details of the book. Correcting the boundary moves every caller with it, which this change's seed forbids. Deferred with its ground recorded, to a change where both move together.
```

Mechanical. Stage 7's assignments re-ordered into a build sequence; nothing added, nothing dropped.

---

## 1. Build Dependency Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Subdomain Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes

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
