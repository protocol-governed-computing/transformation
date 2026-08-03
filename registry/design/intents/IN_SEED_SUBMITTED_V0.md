# IN_SEED_SUBMITTED_V0

## Header (Mandatory)

- **Artifact Code:** IN_SEED_SUBMITTED_V0
- **Artifact Kind:** intent
- **Governed By:** CONSTITUTION_INTENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

A seed is offered to the seed phase for judgement.

`seed_text` is the document itself. The driver reads the file; nothing downstream touches the
filesystem, which is what makes a verdict reproducible.

---

## Machine

```yaml
fqdn: transformation::IN_SEED_SUBMITTED_V0
artifact_kind: INTENT
version: v0
governed_by: fb.intent::CONSTITUTION_INTENT_V0

core:
  summary: Offer a seed document for admissibility judgement
  workflow: WF_P0_SEED_ADMISSIBILITY_V0

  inputs:
    seed_text:
      type: string
      required: true
      description: Full text of the seed document — supplied by the driver, never read downstream
    author_of_record:
      type: string
      required: true
      description: Identity of the person accountable for the seed's content

  outcomes:
    ACK:
      description: Seed accepted for judgement
    NACK:
      description: Seed not accepted for judgement
```
