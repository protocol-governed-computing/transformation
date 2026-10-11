# Stage 7 — Design Intent: platform / conformance

## Machine

```yaml
document:
  phase: p7
  domain: platform
  subdomain: conformance
  cr: enforcement_capability
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Where enforcement status is declared
    business_fact: Every obligation already declares where it is enforced, and two of the five values already route it away from the build.
    resolution: 'Status is a value of `core.enforcement_stage`, governed by a new vocabulary. No second field is added, because two fields that must agree is the defect this change is about. The vocabulary extends nothing: it reserves the `enforcement_stage` category, which no vocabulary held before, and an obligation''s constitution is not a vocabulary that could reserve one.'
    source_finding: {phase: p6, register: boundary_rules, key: A_DEFERRAL_IS_DECLARED_NOT_WRITTEN}
  - decision: How a destination is stated
    business_fact: Three delegations name a mechanism and one names a practice, all in prose nothing reads.
    resolution: An obligation whose stage routes it elsewhere declares `core.enforced_by`, naming the mechanism that carries it. A stage that routes elsewhere without it is refused.
    source_finding: {phase: p6, register: boundary_rules, key: A_DELEGATION_NAMES_ITS_PLACE}
  - decision: Where capability is established
    business_fact: The build already refuses an obligation naming a check no module answers to, at the point the check is derived.
    resolution: 'Capability is established at the same point, from the same two things: the derived check''s module and the obligation''s declared stage. An obligation declaring itself enforced whose module has no refusal-producing path is refused there.'
    source_finding: {phase: p6, register: boundary_rules, key: A_CLAIM_OF_ENFORCEMENT_IS_CHECKED}
  - decision: What capability means, operationally
    business_fact: A check with no refusal path is decidable from the check alone; whether a refusal path is reachable by its own obligation is not decidable in general.
    resolution: The rule is *has a path that produces a refusal*. It is not *has a path this obligation can reach*. The fifteenth instance is corrected by declaration, not caught by rule.
    source_finding: {phase: p6, register: boundary_rules, key: ONLY_WHAT_CAN_BE_DECIDED_IS_REQUIRED}
  - decision: Where the count lives
    business_fact: The build already writes one row per check, naming whether it passed and how many refusals it produced.
    resolution: The row gains the obligation's declared stage, so the count of what is unenforced is read from the record every build already writes. No inspection operation is added.
    source_finding: {phase: p6, register: boundary_rules, key: THE_RELATION_ONLY_GAINS}
  - decision: What happens to the parity obligation
    business_fact: Its content is guaranteed by derivation and holds more strongly than when it was checked by comparison; it is excluded from derivation by name and evaluated by nothing.
    resolution: It is restated with the stage that names derivation as its carrier, and its check module is withdrawn along with the exclusion that named it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - decision: What happens to the obligation that judges quality
    business_fact: It is the one obligation of eighty-nine whose violation warns, its subject is whether a thing is good, and it has no consumers.
    resolution: It is named for its owning subdomain to withdraw. This dossier does not write it, because `capability_contracts` owns it.
    source_finding: {phase: p6, register: ownership, row: 6}
  - decision: Who restates the fourteen
    business_fact: The fourteen are declared by six subdomains, and none of the six is `conformance`.
    resolution: Each is named for its owner to act on. This dossier delivers the mechanism and the vocabulary and writes no obligation it does not own.
    source_finding: {phase: p6, register: boundary_rules, key: AN_OBLIGATION_IS_RESTATED_BY_ITS_OWNER}
  existing_inventory:
  - fqdn: governance::CONSTITUTION_INVARIANTS_V0
    action: REVIEW
    summary: Governs what every obligation declares and how it is enforced
    reason: Gains the requirement that an obligation's declared response to a violation be true of its check, and that a stage routing elsewhere name its destination. The governance surface is authored rather than rendered, so this amendment is written by hand and cited here, not scheduled for construction. Reached by forty-seven obligations on the platform surface.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: conformance::CONSTITUTION_ASSERT_V0
    action: REVIEW
    summary: Defines the structure and semantics of a check, and names the carrier of each of its rules
    reason: Two of its four rules name no carrier and a third names an obligation that never runs. Gains the rule that a declared check is capable of refusing, and a carrier for every rule it declares. Authored by hand, not rendered.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: conformance::INVARIANT_ASSERT_PARITY_V0
    action: REVIEW
    summary: States that every obligation has exactly one check and every check exactly one obligation
    reason: Published, declaring that a violation fails the build immediately, excluded from derivation by name, evaluated by no build, referenced by no artifact. Restated by hand with derivation named as its carrier, because the governance surface is authored rather than rendered.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: compiler::INVARIANT_HANDLER_REGISTRY_CLOSED_V0
    action: REUSE
    summary: Requires every declared check to have a registered implementation before the checking phase begins
    reason: The existing refusal of a check that does not exist, at the point capability is established. Unchanged; named because the new refusal is placed beside it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0
    action: REUSE
    summary: Confirms an obligation delegated to a runtime outcome is bound to one
    reason: The existing confirmation of a delegation, covering one destination. Unchanged; named as the model the new destination follows.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0
    action: REVIEW
    summary: The one obligation of eighty-nine declaring that its violation warns
    reason: Its check returns warnings and reports passed; its subject is whether a thing is good. Named for `capability_contracts` to withdraw; not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: authority::INVARIANT_AUTHORITY_REQUIRED_FOR_EXECUTION_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - fqdn: authority::INVARIANT_AUTHORITY_STATE_WELL_FORMED_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - fqdn: authority::INVARIANT_NO_AMBIENT_AUTHORITY_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - fqdn: authority::INVARIANT_NO_RUNTIME_AUTHORIZATION_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - fqdn: authority::INVARIANT_NO_WORKFLOW_AUTHORIZATION_LOGIC_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - fqdn: authority::INVARIANT_TRACE_AUTHORITY_BINDING_REQUIRED_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - fqdn: actor::INVARIANT_IDENTITY_AUTHORITY_SEPARATION_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `actor` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - fqdn: execution_topology::INVARIANT_NO_RUNTIME_TOPOLOGY_SYNTHESIS_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `execution_topology` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - fqdn: execution_topology::INVARIANT_TOPOLOGY_IMMUTABLE_AFTER_COMPILATION_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
    reason: Named for `execution_topology` to restate with the stage its own prose already states. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  - fqdn: capability_side_effects::INVARIANT_CS_ISOLATED_EXECUTION_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check states the runtime's executor routing carries it
    reason: Named for `capability_side_effects` to restate as carried elsewhere, naming the runtime. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 17}
  - fqdn: capability_side_effects::INVARIANT_CS_TRACEABLE_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check states the runtime execution engine carries it
    reason: Named for `capability_side_effects` to restate as carried elsewhere, naming the runtime. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 18}
  - fqdn: conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check states a phase of the compiler carries it
    reason: Owned by this subdomain, so it is restated by hand as carried elsewhere, naming that phase. The one of the seventeen this dossier may write, and it is authored rather than rendered.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 19}
  - fqdn: surface_contract::INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0
    action: REVIEW
    summary: Declares that a violation fails the build immediately; its check states code review carries it, which is not a mechanism
    reason: Named for `surface_contract` to restate as not yet enforced, since a practice is not a destination a mechanism can confirm. Not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 20}
  - fqdn: conformance::STRUCTURE_CONFORMANCE_POLICY_V0
    action: REVIEW
    summary: Declares what the conformance subdomain compiles
    reason: Unchanged; named because the amended artifacts are compiled under it.
    source_finding: {phase: p6, register: ownership, row: 1}
  new_artifacts:
  - capability: Declaring whether an obligation is enforced
    family: VOCAB
    code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    summary: The places an obligation may be enforced, and what each requires of the obligation that declares it
    owner_subdomain: conformance
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 2}
  rb_declarations: []
  execution_topology: []
  cc_composition: []
  step_bindings: []
  interface_fields:
  - artifact: governance::CONSTITUTION_INVARIANTS_V0
    direction: ATTRIBUTE
    field: core.enforcement_stage
    type: array
    required: 'YES'
    default: null
    meaning: Where the obligation is enforced. Its admissible values are governed by the new vocabulary.
  - artifact: governance::CONSTITUTION_INVARIANTS_V0
    direction: ATTRIBUTE
    field: core.enforced_by
    type: string
    required: 'NO'
    default: null
    meaning: The mechanism that carries the obligation. Required when the declared stage routes the obligation away from the build; refused otherwise.
  - artifact: governance::CONSTITUTION_INVARIANTS_V0
    direction: ATTRIBUTE
    field: core.violation_response
    type: string
    required: 'YES'
    default: null
    meaning: How a violation is answered. Unchanged in form, and now checked against what the derived check can produce.
  - artifact: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    direction: ATTRIBUTE
    field: symbols
    type: object
    required: 'YES'
    default: null
    meaning: Each admissible stage, what carries the obligation there, and whether a destination must be named.
  implementation_bindings: []
  vocabulary_extensions:
  - vocabulary_code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    extends: null
    group: enforcement_stage
    casing: lower_snake
    value: compiler_assertion
    meaning: The build derives a check and runs it. The check must have a path that produces a refusal.
    source_finding: {phase: p6, register: boundary_rules, key: A_CLAIM_OF_ENFORCEMENT_IS_CHECKED}
  - vocabulary_code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    extends: null
    group: enforcement_stage
    casing: lower_snake
    value: compiler_validation
    meaning: A phase of the build carries the obligation directly. The check must have a path that produces a refusal.
    source_finding: {phase: p6, register: boundary_rules, key: A_CLAIM_OF_ENFORCEMENT_IS_CHECKED}
  - vocabulary_code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    extends: null
    group: enforcement_stage
    casing: lower_snake
    value: compiler_meta_validation
    meaning: The build carries the obligation over its own governance surface. The check must have a path that produces a refusal.
    source_finding: {phase: p6, register: boundary_rules, key: A_CLAIM_OF_ENFORCEMENT_IS_CHECKED}
  - vocabulary_code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    extends: null
    group: enforcement_stage
    casing: lower_snake
    value: runtime_outcome
    meaning: The obligation is carried by a violation outcome and its routing. No check is derived. A destination is named.
    source_finding: {phase: p6, register: boundary_rules, key: A_DELEGATION_NAMES_ITS_PLACE}
  - vocabulary_code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    extends: null
    group: enforcement_stage
    casing: lower_snake
    value: composition_conformance
    meaning: The obligation is carried by the assembler over the composed snapshot. No check is derived. A destination is named.
    source_finding: {phase: p6, register: boundary_rules, key: A_DELEGATION_NAMES_ITS_PLACE}
  - vocabulary_code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    extends: null
    group: enforcement_stage
    casing: lower_snake
    value: enforced_elsewhere
    meaning: The obligation is carried by a named mechanism outside the build. No check is derived. A destination is named, and it is confirmed to exist.
    source_finding: {phase: p6, register: boundary_rules, key: A_DELEGATION_NAMES_ITS_PLACE}
  - vocabulary_code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    extends: null
    group: enforcement_stage
    casing: lower_snake
    value: declared_not_enforced
    meaning: The obligation is stated deliberately and carried by nothing yet. No check is derived, no destination is named, and the obligation is counted as unenforced.
    source_finding: {phase: p6, register: boundary_rules, key: A_DEFERRAL_IS_DECLARED_NOT_WRITTEN}
  runtime_policies: []
  artifact_properties:
  - artifact: conformance::INVARIANT_ASSERT_PARITY_V0
    property: core.enforcement_stage
    value: enforced_elsewhere
    source_finding: {phase: p7, register: design_resolution, row: 6}
  - artifact: conformance::INVARIANT_ASSERT_PARITY_V0
    property: core.enforced_by
    value: The step of the build that derives a check from its obligation
    source_finding: {phase: p7, register: design_resolution, row: 6}
  - artifact: conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0
    property: core.enforcement_stage
    value: enforced_elsewhere
    source_finding: {phase: p7, register: design_resolution, row: 2}
  - artifact: conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0
    property: core.enforced_by
    value: The phase of the build that validates test data
    source_finding: {phase: p7, register: design_resolution, row: 2}
  - artifact: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    property: governed_by
    value: vocabulary::CONSTITUTION_VOCABULARY_V0
    source_finding: {phase: p7, register: new_artifacts, key: VOCAB_ENFORCEMENT_STATUS_V0}
  - artifact: conformance::VOCAB_ENFORCEMENT_STATUS_V0
    property: concern
    value: conformance
    source_finding: {phase: p6, register: ownership, row: 2}
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: conformance
    count: '1'
    artifacts: conformance::VOCAB_ENFORCEMENT_STATUS_V0
  generation_provenance: []
  declared_reach: []
  refusal_discharge: []
  refusal_deferrals:
  - operation: Building a composition
    refused_when: An obligation declares itself enforced and its check cannot refuse anything
    deferred_to: The six subdomains that own the fourteen
    until: Each restates its own obligations with the stage that matches what its check does. The rule is written by this change and armed after they have, because arming it first would fail every build on obligations this dossier may not write.
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - operation: Building a composition
    refused_when: An obligation declares enforcement elsewhere and does not name where
    deferred_to: The four subdomains whose obligations delegate in prose
    until: Each names the mechanism its check's own text already states. The rule is written by this change and armed after they have.
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - operation: Admitting an obligation as governance
    refused_when: Its check only reports and never refuses
    deferred_to: capability_contracts
    until: That subdomain withdraws the one obligation of eighty-nine whose violation warns. The rule this change writes refuses a check with no refusal path; this check has one its obligation cannot reach, so the correction is a declaration rather than a refusal.
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  refusal_governance_discharge: []
```

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

---

## 1. Design Decisions Resolution

---

## 2. Artifact Inventory — Existing Artifacts

---

## 3. Artifact Family Mapping — New Artifacts

---

## 4. Runtime Binding (RB) Declarations

---

## 5. Execution Topology

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Implementation Bindings

---

## 10. Vocabulary Extensions

---

## 11. Runtime Policies

---

## 12. Artifact Properties

---

## 13. STRUCTURE Stores

---

## 14. Transport Bindings

---

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

---

## 18. Refusal Discharge

---

## 19. Refusal Deferrals

---

## 20. Refusal Governance Discharge

---

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`10aa26e1582f…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the rendering of one vocabulary, and the hand-authoring of the four
governance amendments §2 cites as REVIEW. It authorizes nothing else.

Two things about this design are worth naming at its closure. The governance surface is authored
rather than constructed, so the constitutions and obligations this change amends are cited and
written by hand; only the vocabulary is rendered. And every refusal the seed states is recorded in
§19 as a deferral rather than a discharge: the rules are written by this change and armed after the
six subdomains that own the fourteen have restated them. Arming them first would fail every build on
obligations this dossier may not write.
