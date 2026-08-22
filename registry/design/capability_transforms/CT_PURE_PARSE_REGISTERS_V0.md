# CT_PURE_PARSE_REGISTERS_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_PARSE_REGISTERS_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Read a phase document into the registers a rule set can be applied to.

**Phase-neutral by design.** Every phase document in the pipeline has the same shape — header
fields, numbered sections, pipe tables — so every phase parses the same way and differs only in
which rule set it then applies. P1 through P7 reuse this transform.

`document_text` is the **document itself**, never a location to read. A pure CT may not touch the
filesystem — doing so would make the transform non-deterministic and unreplayable, and would put
I/O inside a transform. The caller reads the file and supplies its content, so the same text always
parses to the same registers.

This transform **reports what a document contains and judges nothing**. A malformed document yields
a partial structure rather than an error, because a parse failure would report a syntax problem
where the author needs a governance finding. Deciding admissibility belongs to the rule set.

---

## Machine

```yaml
fqdn: transformation::CT_PURE_PARSE_REGISTERS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: design
core:
  summary: Parse phase document text into structured registers
  refusal: never
  description: |
    Splits a phase document into its header fields, its numbered sections, and its registers.

    A register is addressed by the `<!-- register:id -->` marker an authored document repeats from
    its template — a stable identity that survives retitling and stays unambiguous when one section
    carries several registers. Sections remain for documents that predate the templates.

    Judges nothing: an absent register is simply absent from the result, and the rule set decides
    what that means.
  inputs:
    document_text:
      type: string
      required: true
      description: The full text of the phase document — never a path, never read from disk
  outputs:
    header:
      type: object
      required: true
      description: Header field name to declared value
    sections:
      type: array
      required: true
      description: Ordered sections, each with number, title, text, and any table columns and rows
    registers:
      type: array
      required: true
      description: Registers addressed by their marker id, each with columns and rows
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_PARSE_REGISTERS
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_parse_registers_v0
    callable: execute
```
