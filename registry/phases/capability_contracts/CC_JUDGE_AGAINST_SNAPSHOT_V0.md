# CC_JUDGE_AGAINST_SNAPSHOT_V0

## Header (Mandatory)

- **Artifact Code:** CC_JUDGE_AGAINST_SNAPSHOT_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE
- **Dependencies:** CT_PURE_PARSE_REGISTERS_V0, CS_SNAPSHOT_QUERY_V0, CT_PURE_EVALUATE_RULES_V0

---

## 1. Intent

Judge a phase document against a declared rule set **and against the composition it describes**.

Reused by every phase that grounds claims. Each supplies its own document and rule set; the
mechanism is the same one.

---

## 2. Why this is a separate contract

`CC_JUDGE_DOCUMENT_V0` judges a document alone and binds nothing. That is sufficient while a rule
is a property of what the register says about itself — structure, vocabulary, traceability.

It stops being sufficient the moment a register claims something already exists. That is a claim
about the assembled composition, and no amount of reading the document can settle it. Grounding
needs an observation, an observation is a side effect, and a contract that binds a side effect is a
different contract from one that binds none.

Both remain: a phase that grounds nothing should not acquire a capability it does not use, and a
contract that always observed would make every phase depend on a snapshot being present.

---

## 3. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_PARSE_REGISTERS_V0 | CT | Parse |
| 2 | CS_SNAPSHOT_QUERY_V0 | CS | QUERY |
| 3 | CT_PURE_EVALUATE_RULES_V0 | CT | Evaluate |

---

## 4. Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| document_text | string | true | Full text of the phase document |
| rule_set | array | true | The declared rules deciding admissibility |

---

## 5. Outputs

| Field | Type | Description |
|-------|------|-------------|
| verdict | string | ADMISSIBLE or INADMISSIBLE |
| findings | array | One entry per failed rule |
| rules_evaluated | integer | Number of rules applied |

---

## 6. Result Status Contract

| Status | Condition |
|--------|-----------|
| SUCCESS | The composition was observed, the rule set applied in full, and a verdict reached |
| VIOLATION | The input was unusable, or a rule named an unimplemented check kind |
| BACKEND_ERROR | The bound snapshot could not be read |

---

## Machine

```yaml
fqdn: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Parse a phase document, observe the composition, and judge both together
  inputs:
    document_text:
      type: string
      required: true
    rule_set:
      type: array
      required: true
  outputs:
    verdict:
      type: string
    findings:
      type: array
    rules_evaluated:
      type: integer
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: parse_registers
    transform: transformation::CT_PURE_PARSE_REGISTERS_V0
    inputs:
      document_text: $.inputs.document_text
    outputs: {}
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit

  # Observation is a governed capability, never an ad hoc read. The snapshot observed is the one
  # this workflow executes from, bound by the runtime binding rather than named by a caller.
  - step: observe_composition
    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    op: QUERY
    inputs:
      operation: si.artifact.list
      params: {}
    outputs: {}
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit

  - step: evaluate_rules
    transform: transformation::CT_PURE_EVALUATE_RULES_V0
    inputs:
      header: $.results.parse_registers.capability_result.header
      sections: $.results.parse_registers.capability_result.sections
      registers: $.results.parse_registers.capability_result.registers
      document_text: $.inputs.document_text
      rule_set: $.inputs.rule_set
      # Keyed by the operation that produced it, so a rule can say which observation it relied on.
      observed:
        si.artifact.list: $.results.observe_composition.capability_result.result.artifacts
    outputs:
      verdict: $.capability_result.verdict
      findings: $.capability_result.findings
      rules_evaluated: $.capability_result.rules_evaluated
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
extensions:
  description: Grounds a phase document against the composition it is executing within
```
