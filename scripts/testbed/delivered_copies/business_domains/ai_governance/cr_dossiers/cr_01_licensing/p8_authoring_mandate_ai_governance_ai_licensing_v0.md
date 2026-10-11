# Stage 8 — Authoring Mandate: ai_governance / ai_licensing

## Machine

```yaml
document:
  phase: p8
  domain: ai_governance
  subdomain: ai_licensing
  cr: cr_01_licensing
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order: null
  critical_path: null
  mandate_artifact_summary:
  - action: EXTEND
    count: '4'
    description: The licensing domain's three checks, redeclared whole with the cases that prove them, and the build manifest regenerated so the domain compiles those cases.
  field_declarations:
  - code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    subdomain_field: ai_licensing
  new_capabilities:
  - code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    purpose: Evaluate whether license quota remains available under the declared cap
    inputs: assigned_count, quota
    outputs: quota_available, remaining
  - code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    purpose: Evaluate whether required training has been completed
    inputs: training_completed
    outputs: training_eligible
  - code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    purpose: Evaluate license inactivity against a declared threshold
    inputs: last_active_date, evaluation_date, threshold_days
    outputs: is_inactive, days_inactive
  new_intents: null
  cross_subdomain_notes:
  - code: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
    note: Generated, not authored. It describes the whole domain, so it still names agent_governance, which this change does not touch.
```

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the three checks are redeclared whole with their
cases, and the build manifest is regenerated.

---

## 1. Build Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes
