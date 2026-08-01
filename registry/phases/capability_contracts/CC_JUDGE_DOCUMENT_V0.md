# CC_JUDGE_DOCUMENT_V0

## Header (Mandatory)

- **Artifact Code:** CC_JUDGE_DOCUMENT_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE
- **Dependencies:** CT_PURE_PARSE_REGISTERS_V0, CT_PURE_EVALUATE_RULES_V0

---

## 1. Intent

Judge a phase document against a declared rule set: read it into registers, then apply every rule
and report what failed.

Reused by every phase. Each phase supplies its own document and its own rule set; the mechanism is
the same one.

---

## 2. Rationale

Parsing and evaluating are two steps of one governed capability rather than two capabilities. A
workflow composes capability *calls*, and data does not flow between them — a node reads the intent
payload, not a previous node's result. Chaining belongs inside a contract's pipeline, where step two
reads step one through `$.results.parse_registers.*`.

Keeping the two transforms separate still matters: parsing judges nothing and evaluating knows
nothing about markdown, so each can be reused or replaced without disturbing the other.

Admissibility must be reproducible — the same document and the same rule set always give the same
verdict. The rule set arrives as an input rather than as embedded content, so what is governed can
be read from the composition without reading any code.

---

## 3. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_PARSE_REGISTERS_V0 | CT | Parse |
| 2 | CT_PURE_EVALUATE_RULES_V0 | CT | Evaluate |

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
| SUCCESS | The rule set was applied in full and a verdict reached |
| VIOLATION | The input was unusable, or a rule named an unimplemented check kind |

---

## Machine

```yaml
fqdn: transformation::CC_JUDGE_DOCUMENT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Parse a phase document and judge it against a declared rule set
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
    on_input_failure: VIOLATION
  pipeline:
  - step: parse_registers
    transform: transformation::CT_PURE_PARSE_REGISTERS_V0
    inputs:
      document_text: $.inputs.document_text
    outputs:
      header: $.capability_result.header
      sections: $.capability_result.sections
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit

  - step: evaluate_rules
    transform: transformation::CT_PURE_EVALUATE_RULES_V0
    inputs:
      header: $.results.parse_registers.header
      sections: $.results.parse_registers.sections
      document_text: $.inputs.document_text
      rule_set: $.inputs.rule_set
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
  description: Reads a phase document into registers and evaluates every declared rule against it
```
