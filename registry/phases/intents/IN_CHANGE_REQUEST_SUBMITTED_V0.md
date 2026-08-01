# IN_CHANGE_REQUEST_SUBMITTED_V0

## Header (Mandatory)

- **Artifact Code:** IN_CHANGE_REQUEST_SUBMITTED_V0
- **Artifact Kind:** intent
- **Governed By:** CONSTITUTION_INTENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

A Change Request register is offered to P1 for judgement.

`register_text` is the document itself. The driver reads the file; nothing downstream touches the
filesystem, which is what makes a verdict reproducible — the same rule established at P0 and
carried forward unchanged.

---

## Machine

```yaml
fqdn: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
artifact_kind: INTENT
version: v0
governed_by: fb.intent::CONSTITUTION_INTENT_V0

core:
  summary: Offer a Change Request register for admissibility judgement
  workflow: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0

  inputs:
    register_text:
      type: string
      required: true
      description: Full text of the P1 register — supplied by the driver, never read downstream
    author_of_record:
      type: string
      required: true
      description: Identity of the person accountable for the register's content

  outcomes:
    ACK:
      description: Register accepted for judgement
    NACK:
      description: Register not accepted for judgement
```
