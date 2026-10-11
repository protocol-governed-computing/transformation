# Stage 8 — Authoring Mandate: ai_governance / reclaim and parameter result

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_02_reclaim_and_parameters
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
    rows:
    - Wave: '1'
      Step: '1'
      Code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: ai_licensing
      Depends On: —
    - Wave: '1'
      Step: '2'
      Code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: agent_governance
      Depends On: —
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    - Position: '2'
      Code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '2'
      Description: The reclaim, answering a refused removal, and the parameter check, reporting whether every declared rule passed.
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Count: '2'
      Description: The published versions they stand in for, stood down unchanged.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Subdomain Field: ai_licensing
    - Code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Subdomain Field: agent_governance
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
      Purpose: Reclaim license from inactive user
      Inputs: license_id, employee_id, last_active_date, evaluation_date, threshold_days
      Outputs: result_status, is_inactive, days_inactive
    - Code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
      Purpose: Enforce declared parameter constraints for an authorized tool
      Inputs: tool_name, parameters
      Outputs: rules, validation_result
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
    rows: []
```

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Two contracts are built, each in its subdomain; the published versions they replace are
stood down, and the reclaim act and the governed action are re-pointed to them.

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
