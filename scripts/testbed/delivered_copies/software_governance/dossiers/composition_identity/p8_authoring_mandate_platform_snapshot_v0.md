# Stage 8 — Authoring Mandate: platform / snapshot

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: composition_identity
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
    - Wave: NONE IDENTIFIED
      Step: ''
      Code: ''
      Action (REPLACE, EXTEND, NEW): ''
      Subdomain: ''
      Depends On: ''
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: NONE IDENTIFIED
      Code: ''
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '0'
      Description: The change authors no artifact. Every capability it needs is a requirement added to something that already exists, and the governance surface is authored by hand rather than rendered, so nothing is scheduled for construction.
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '0'
      Description: 'Two amendments are written by hand: the constitution governing trust states which of an attestation''s fields constitute the composition it attests, and the snapshot subdomain requires that constituting unchanged source twice yields one identity. Neither carries a build step.'
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Count: '0'
      Description: Nothing is stood down. The field that leaves the identity is still written and still read; what changes is that it no longer decides what the composition is.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
      Subdomain Field: cryptographic_trust
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
    - Code: NONE IDENTIFIED
      Purpose: ''
      Workflow: ''
      Inputs: ''
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
      Note: Amended by `cryptographic_trust`, not here. What an attestation carries, and which of its fields constitute the composition it attests, is its owner's to declare. This dossier consumes the division and names the artifact rather than writing it.
    - Code: cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0
      Note: Unchanged. The change holds whether the signature is the present placeholder or a real one, so making the signature real stays a separate change.
    - Code: execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0
      Note: 'Unchanged, and the reason the attestation stays a constituent: the runtime refuses a composition whose projection does not match what the attestation binds. Excluding the file rather than the field would drop that binding from the identity.'
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

**Status: CLOSED.** Approved by the business author against the composition `47dd8edc2123…`, the one
`baseline.json` pins. Construction Completeness is not the gate here and was not read as one: the
mandate schedules nothing, so there is nothing to determine and nothing to render.

What is frozen is one field leaving a composition's identity, and one requirement that constituting
unchanged source twice yields one identity. **An amendment to the attestation itself is outside this
mandate** — what an attestation carries is its owning subdomain's to declare, and this dossier
consumes that declaration rather than writing it.
