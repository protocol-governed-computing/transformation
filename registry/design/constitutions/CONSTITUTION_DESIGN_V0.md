# CONSTITUTION_DESIGN_V0

## Machine

```yaml
fqdn: transformation::CONSTITUTION_DESIGN_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: design
core:
  enforcement_model: compiler_enforced
  governs:
  - INVARIANT
rules:
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_ROW_PROVENANCE_CITED_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_UPSTREAM_COMMITMENT_CARRIED_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_CONTENT_ENTERS_AT_OWNING_PHASE_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_RESTATEMENT_MATCHES_SOURCE_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_EXISTING_ARTIFACT_OBSERVED_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_NEW_IDENTITY_UNUSED_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_REUSE_FROM_PERMITTING_DOMAIN_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_NO_QUESTION_LEFT_OPEN_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_PHASE_SPEAKS_ITS_RUNG_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_TOUCHED_SUBDOMAIN_DECLARED_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_BUSINESS_REFUSAL_DISCHARGED_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_ANNOUNCEMENT_FROM_COMPLETING_ENDING_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_REACH_DECLARED_AND_USED_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_BUILD_ORDER_TOPOLOGICAL_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_DESIGN_NAMES_RESOLVE_V0
- applies_to: PHASE_DOCUMENT
  enforced_by: transformation::INVARIANT_DECLARED_ARTIFACT_FULLY_STATED_V0
```

---

## 1. Design admissibility

A phase document is admissible when every rule its phase seals is satisfied. The rules are declared in the phase's register schema and sealed into the phase workflow. Each relational rule and each named procedure realises one of the invariants below, and the evaluator enforces them all, with no short-circuit and no warning tier.
