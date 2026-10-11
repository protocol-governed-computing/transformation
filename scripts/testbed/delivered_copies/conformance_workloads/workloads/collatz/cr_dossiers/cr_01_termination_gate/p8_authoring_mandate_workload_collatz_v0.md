# Stage 8 — Authoring Mandate: workload / collatz

## Machine

```yaml
header:
  Stage: 8 — Authoring Mandate
  CR: cr_01_termination_gate
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
      Code: workload::CC_VERIFY_TERMINATION_V1
      Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: collatz
      Depends On: —
  critical_path:
    columns:
    - Position
    - Code
    rows:
    - Position: '1'
      Code: workload::CC_VERIFY_TERMINATION_V1
  mandate_artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Count
    - Description
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Count: '1'
      Description: The termination gate, refusing unless every sequence ended at 1.
    - Action (REPLACE, EXTEND, NEW): REPLACE
      Count: '1'
      Description: The termination gate it stands in for.
  field_declarations:
    columns:
    - Code
    - Subdomain Field
    rows:
    - Code: workload::CC_VERIFY_TERMINATION_V1
      Subdomain Field: collatz
  new_capabilities:
    columns:
    - Code
    - Purpose
    - Inputs
    - Outputs
    rows:
    - Code: workload::CC_VERIFY_TERMINATION_V1
      Purpose: Verify all Collatz sequences terminate at 1
      Inputs: sequences
      Outputs: all_terminate, non_terminating, conjecture_holds
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
nothing. One contract is built in its subdomain; the one it replaces is stood down, and the workflow
re-pointed to the new one.

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
