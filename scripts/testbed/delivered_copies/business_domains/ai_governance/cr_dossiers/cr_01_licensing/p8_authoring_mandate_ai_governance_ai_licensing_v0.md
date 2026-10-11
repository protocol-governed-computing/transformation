# Stage 8 — Authoring Mandate: ai_governance / ai_licensing

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_01_licensing
  Status: DRAFT
  Feeds: Construction
registers:
  build_order:
    columns:
    - Wave
    - Step
    - Code
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Depends On
    rows: []
  critical_path:
    columns:
    - Position
    - Code
    rows: []
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Count: '4'
      Description: The licensing domain's three checks, redeclared whole with the cases that prove them, and the build manifest regenerated so the domain compiles those cases.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Subdomain Field: ai_licensing
    - Code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Subdomain Field: ai_licensing
    - Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Subdomain Field: ai_licensing
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
      Purpose: Evaluate whether license quota remains available under the declared cap
      Inputs: assigned_count, quota
      Outputs: quota_available, remaining
    - Code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
      Purpose: Evaluate whether required training has been completed
      Inputs: training_completed
      Outputs: training_eligible
    - Code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      Purpose: Evaluate license inactivity against a declared threshold
      Inputs: last_active_date, evaluation_date, threshold_days
      Outputs: is_inactive, days_inactive
  new_intents:
    columns:
    - Code
    - Purpose
    - Workflow
    - Inputs
    rows: []
  cross_subdomain_notes:
    columns:
    - Code
    - Note
    rows:
    - Code: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
      Note: Generated, not authored. It describes the whole domain, so it still names agent_governance, which this change does not touch.
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
