# CC_JUDGE_AGAINST_COMPOSITION_V0

## Header (Mandatory)

- **Artifact Code:** CC_JUDGE_AGAINST_COMPOSITION_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE
- **Dependencies:** CT_PURE_PARSE_REGISTERS_V0, CS_SNAPSHOT_QUERY_V0, CT_PURE_EVALUATE_RULES_V0

---

## 1. Intent

Judge a phase document against a declared rule set, the artifacts the composition publishes, **and
what each domain declares about itself**.

---

## 2. Why a second observation

`CC_JUDGE_AGAINST_SNAPSHOT_V0` observes the artifact list, which answers *does this identity
exist*. That is the whole question while a phase is discovering what is there.

A phase that **decides** asks a further one: *may this artifact be offered to this change request
at all?* That is not a property of the artifact — it is a property of the domain that owns it, and
a domain declares it. So this contract gathers the composition summary as well, and the two
observations answer different questions: one resolves an identity, the other bounds the search
space an identity may be drawn from.

Both remain separate contracts. A phase that only discovers should not acquire an observation it
does not use, and folding the two would make P2 depend on a declaration it never reads.

---

## 3. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_PARSE_REGISTERS_V0 | CT | Parse |
| 2 | CS_SNAPSHOT_QUERY_V0 | CS | QUERY (si.artifact.list) |
| 3 | CS_SNAPSHOT_QUERY_V0 | CS | QUERY (si.snapshot.summary) |
| 4 | CT_PURE_EVALUATE_RULES_V0 | CT | Evaluate |

---

## Machine

```yaml
fqdn: transformation::CC_JUDGE_AGAINST_COMPOSITION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Parse a phase document, observe the composition and its declarations, and judge them together
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

  - step: observe_declarations
    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    op: QUERY
    inputs:
      operation: si.snapshot.summary
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
        si.snapshot.summary: $.results.observe_declarations.capability_result.result.reuse_visibility
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
  description: Grounds a phase document against the composition and the declarations of the domains within it
```
