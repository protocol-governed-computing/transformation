# Stage 8 — Authoring Mandate: ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p8
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '2'
    code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    action: NEW
    subdomain: agent_governance
    depends_on: null
  critical_path:
  - position: '1'
    code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
  - position: '2'
    code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
  mandate_artifact_summary:
  - action: NEW
    count: '2'
    description: The reclaim, answering a refused removal, and the parameter check, reporting whether every declared rule passed.
  - action: REPLACE
    count: '2'
    description: The published versions they stand in for, stood down unchanged.
  field_declarations:
  - code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    subdomain_field: ai_licensing
  - code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    subdomain_field: agent_governance
  new_capabilities:
  - code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1
    purpose: Reclaim license from inactive user
    inputs: license_id, employee_id, last_active_date, evaluation_date, threshold_days
    outputs: result_status, is_inactive, days_inactive
  - code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
    purpose: Enforce declared parameter constraints for an authorized tool
    inputs: tool_name, parameters
    outputs: rules, validation_result
  new_intents: null
  cross_subdomain_notes: null
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
