# INVARIANT_ROW_PROVENANCE_CITED_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_ROW_PROVENANCE_CITED_V0
artifact_kind: INVARIANT
version: V0
governed_by: transformation::CONSTITUTION_DESIGN_V0
authority: pgc.platform
concern: design
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the design compiler, evaluating each phase's sealed rule set over a phase document
assert_projection:
  applies_to_kinds:
  - WF
```

---

## 1. Claim

Every row a phase restates cites where it came from, and every citation resolves.

## 2. Why

A row with no citation is content the phase may have invented, and a citation that resolves to nothing lends a row a provenance it does not have. Either way no reader can trace the claim back to the business statement that justifies it.

## 3. How it is checked

A citation names a register and a row of an earlier phase or of this document, an artifact in the pinned composition, or a human ruling. The rules that realise this refuse a row that cites nothing, a citation naming a register the phase may not cite, and an ordinal past the end of the register it names.
