# AC_SEED_AUTHOR_V0

## Header (Mandatory)

- **Artifact Code:** AC_SEED_AUTHOR_V0
- **Artifact Kind:** actor
- **Governed By:** CONSTITUTION_ACTOR_IDENTITY_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The person accountable for a seed's content.

A seed is a faithful rewrite of a business problem statement, and someone must answer for whether it
says what the business meant. Declaring that as an actor makes authorship a property of the
composition rather than a convention: the pipeline cannot run without one, and no automated drafter
can occupy this role.

---

## Machine

```yaml
fqdn: transformation::AC_SEED_AUTHOR_V0
artifact_kind: ACTOR
version: v0
governed_by: fb.actor::CONSTITUTION_ACTOR_IDENTITY_V0
core:
  summary: Author of record for a seed
  description: The human accountable for the content of a seed offered to the seed phase.
  type: human
  attributes:
    role:
      type: string
      required: true
      value: seed_author
```
