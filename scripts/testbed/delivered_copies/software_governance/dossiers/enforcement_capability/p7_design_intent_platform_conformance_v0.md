# Stage 7 — Design Intent: platform / conformance

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: enforcement_capability
  Status: DRAFT
  Feeds: Stage 8 — Authoring Mandate
registers:
  design_resolution:
    columns:
    - Decision
    - Business Fact
    - Resolution
    - Source Finding
    rows:
    - Decision: Where enforcement status is declared
      Business Fact: Every obligation already declares where it is enforced, and two of the five values already route it away from the build.
      Resolution: 'Status is a value of `core.enforcement_stage`, governed by a new vocabulary. No second field is added, because two fields that must agree is the defect this change is about. The vocabulary extends nothing: it reserves the `enforcement_stage` category, which no vocabulary held before, and an obligation''s constitution is not a vocabulary that could reserve one.'
      Source Finding: S6 boundary_rules A_DEFERRAL_IS_DECLARED_NOT_WRITTEN
    - Decision: How a destination is stated
      Business Fact: Three delegations name a mechanism and one names a practice, all in prose nothing reads.
      Resolution: An obligation whose stage routes it elsewhere declares `core.enforced_by`, naming the mechanism that carries it. A stage that routes elsewhere without it is refused.
      Source Finding: S6 boundary_rules A_DELEGATION_NAMES_ITS_PLACE
    - Decision: Where capability is established
      Business Fact: The build already refuses an obligation naming a check no module answers to, at the point the check is derived.
      Resolution: 'Capability is established at the same point, from the same two things: the derived check''s module and the obligation''s declared stage. An obligation declaring itself enforced whose module has no refusal-producing path is refused there.'
      Source Finding: S6 boundary_rules A_CLAIM_OF_ENFORCEMENT_IS_CHECKED
    - Decision: What capability means, operationally
      Business Fact: A check with no refusal path is decidable from the check alone; whether a refusal path is reachable by its own obligation is not decidable in general.
      Resolution: The rule is *has a path that produces a refusal*. It is not *has a path this obligation can reach*. The fifteenth instance is corrected by declaration, not caught by rule.
      Source Finding: S6 boundary_rules ONLY_WHAT_CAN_BE_DECIDED_IS_REQUIRED
    - Decision: Where the count lives
      Business Fact: The build already writes one row per check, naming whether it passed and how many refusals it produced.
      Resolution: The row gains the obligation's declared stage, so the count of what is unenforced is read from the record every build already writes. No inspection operation is added.
      Source Finding: S6 boundary_rules THE_RELATION_ONLY_GAINS
    - Decision: What happens to the parity obligation
      Business Fact: Its content is guaranteed by derivation and holds more strongly than when it was checked by comparison; it is excluded from derivation by name and evaluated by nothing.
      Resolution: It is restated with the stage that names derivation as its carrier, and its check module is withdrawn along with the exclusion that named it.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - Decision: What happens to the obligation that judges quality
      Business Fact: It is the one obligation of eighty-nine whose violation warns, its subject is whether a thing is good, and it has no consumers.
      Resolution: It is named for its owning subdomain to withdraw. This dossier does not write it, because `capability_contracts` owns it.
      Source Finding: 'S6 ownership #6'
    - Decision: Who restates the fourteen
      Business Fact: The fourteen are declared by six subdomains, and none of the six is `conformance`.
      Resolution: Each is named for its owner to act on. This dossier delivers the mechanism and the vocabulary and writes no obligation it does not own.
      Source Finding: S6 boundary_rules AN_OBLIGATION_IS_RESTATED_BY_ITS_OWNER
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: governance::CONSTITUTION_INVARIANTS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Governs what every obligation declares and how it is enforced
      Reason: Gains the requirement that an obligation's declared response to a violation be true of its check, and that a stage routing elsewhere name its destination. The governance surface is authored rather than rendered, so this amendment is written by hand and cited here, not scheduled for construction. Reached by forty-seven obligations on the platform surface.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: conformance::CONSTITUTION_ASSERT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Defines the structure and semantics of a check, and names the carrier of each of its rules
      Reason: Two of its four rules name no carrier and a third names an obligation that never runs. Gains the rule that a declared check is capable of refusing, and a carrier for every rule it declares. Authored by hand, not rendered.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: conformance::INVARIANT_ASSERT_PARITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: States that every obligation has exactly one check and every check exactly one obligation
      Reason: Published, declaring that a violation fails the build immediately, excluded from derivation by name, evaluated by no build, referenced by no artifact. Restated by hand with derivation named as its carrier, because the governance surface is authored rather than rendered.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: compiler::INVARIANT_HANDLER_REGISTRY_CLOSED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Requires every declared check to have a registered implementation before the checking phase begins
      Reason: The existing refusal of a check that does not exist, at the point capability is established. Unchanged; named because the new refusal is placed beside it.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Confirms an obligation delegated to a runtime outcome is bound to one
      Reason: The existing confirmation of a delegation, covering one destination. Unchanged; named as the model the new destination follows.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: The one obligation of eighty-nine declaring that its violation warns
      Reason: Its check returns warnings and reports passed; its subject is whether a thing is good. Named for `capability_contracts` to withdraw; not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: authority::INVARIANT_AUTHORITY_REQUIRED_FOR_EXECUTION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
    - FQDN: authority::INVARIANT_AUTHORITY_STATE_WELL_FORMED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #9'
    - FQDN: authority::INVARIANT_NO_AMBIENT_AUTHORITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #10'
    - FQDN: authority::INVARIANT_NO_RUNTIME_AUTHORIZATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #11'
    - FQDN: authority::INVARIANT_NO_WORKFLOW_AUTHORIZATION_LOGIC_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #12'
    - FQDN: authority::INVARIANT_TRACE_AUTHORITY_BINDING_REQUIRED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `authority` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #13'
    - FQDN: actor::INVARIANT_IDENTITY_AUTHORITY_SEPARATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `actor` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #14'
    - FQDN: execution_topology::INVARIANT_NO_RUNTIME_TOPOLOGY_SYNTHESIS_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `execution_topology` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #15'
    - FQDN: execution_topology::INVARIANT_TOPOLOGY_IMMUTABLE_AFTER_COMPILATION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check has no refusal-producing path
      Reason: Named for `execution_topology` to restate with the stage its own prose already states. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #16'
    - FQDN: capability_side_effects::INVARIANT_CS_ISOLATED_EXECUTION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check states the runtime's executor routing carries it
      Reason: Named for `capability_side_effects` to restate as carried elsewhere, naming the runtime. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #17'
    - FQDN: capability_side_effects::INVARIANT_CS_TRACEABLE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check states the runtime execution engine carries it
      Reason: Named for `capability_side_effects` to restate as carried elsewhere, naming the runtime. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #18'
    - FQDN: conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check states a phase of the compiler carries it
      Reason: Owned by this subdomain, so it is restated by hand as carried elsewhere, naming that phase. The one of the seventeen this dossier may write, and it is authored rather than rendered.
      Source Finding: 'S6 pps_artifacts_requiring_action #19'
    - FQDN: surface_contract::INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares that a violation fails the build immediately; its check states code review carries it, which is not a mechanism
      Reason: Named for `surface_contract` to restate as not yet enforced, since a practice is not a destination a mechanism can confirm. Not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #20'
    - FQDN: conformance::STRUCTURE_CONFORMANCE_POLICY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares what the conformance subdomain compiles
      Reason: Unchanged; named because the amended artifacts are compiled under it.
      Source Finding: 'S6 ownership #1'
  new_artifacts:
    columns:
    - Capability
    - Family
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: Declaring whether an obligation is enforced
      Family: VOCAB
      Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Summary: The places an obligation may be enforced, and what each requires of the obligation that declares it
      Owner Subdomain: conformance
      Status: NEW
      Source Finding: 'S6 governance_outcome #2'
  rb_declarations:
    columns:
    - RB Code
    - Binds WF
    - CS Bindings
    - Storage Structure
    - Source Finding
    rows:
    - RB Code: NONE IDENTIFIED
      Binds WF: ''
      CS Bindings: ''
      Storage Structure: ''
      Source Finding: ''
  execution_topology:
    columns:
    - Workflow
    - Node
    - Node Type (IN, CC, EXIT, EXIT_SUCCESS)
    - Routing
    - Source Finding
    rows:
    - Workflow: NONE IDENTIFIED
      Node: ''
      Node Type (IN, CC, EXIT, EXIT_SUCCESS): ''
      Routing: ''
      Source Finding: ''
  cc_composition:
    columns:
    - CC Code
    - Step
    - Step Name
    - Capability
    - Kind (CT, CS)
    - Operation
    - Store
    - Consumes
    - Produces
    - Routing
    - Interpreted By
    - Semantic Status
    - Interface
    rows:
    - CC Code: NONE IDENTIFIED
      Step: ''
      Step Name: ''
      Capability: ''
      Kind (CT, CS): ''
      Operation: ''
      Store: ''
      Consumes: ''
      Produces: ''
      Routing: ''
      Interpreted By: ''
      Semantic Status: ''
      Interface: ''
  step_bindings:
    columns:
    - Owner
    - Step
    - Direction (INPUT, OUTPUT)
    - Field
    - Bound To
    - Source Finding
    rows:
    - Owner: NONE IDENTIFIED
      Step: ''
      Direction (INPUT, OUTPUT): ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  interface_fields:
    columns:
    - Artifact
    - Direction (INPUT, OUTPUT, ATTRIBUTE)
    - Field
    - Type
    - Required (YES, NO)
    - Default
    - Meaning
    rows:
    - Artifact: governance::CONSTITUTION_INVARIANTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: core.enforcement_stage
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: Where the obligation is enforced. Its admissible values are governed by the new vocabulary.
    - Artifact: governance::CONSTITUTION_INVARIANTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: core.enforced_by
      Type: string
      Required (YES, NO): 'NO'
      Default: —
      Meaning: The mechanism that carries the obligation. Required when the declared stage routes the obligation away from the build; refused otherwise.
    - Artifact: governance::CONSTITUTION_INVARIANTS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: core.violation_response
      Type: string
      Required (YES, NO): 'YES'
      Default: —
      Meaning: How a violation is answered. Unchanged in form, and now checked against what the derived check can produce.
    - Artifact: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: symbols
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: Each admissible stage, what carries the obligation there, and whether a destination must be named.
  implementation_bindings:
    columns:
    - CT Code
    - Module
    - Callable
    - Operation
    - Kind (atom, molecule)
    - Purity (ct_pure, ct_impure)
    - Refusal (raises, returns, never)
    - Source Finding
    rows:
    - CT Code: NONE IDENTIFIED
      Module: ''
      Callable: ''
      Operation: ''
      Kind (atom, molecule): ''
      Purity (ct_pure, ct_impure): ''
      Refusal (raises, returns, never): ''
      Source Finding: ''
  vocabulary_extensions:
    columns:
    - Vocabulary Code
    - Extends
    - Group
    - Casing
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Extends: NONE
      Group: enforcement_stage
      Casing: lower_snake
      Value: compiler_assertion
      Meaning: The build derives a check and runs it. The check must have a path that produces a refusal.
      Source Finding: S6 boundary_rules A_CLAIM_OF_ENFORCEMENT_IS_CHECKED
    - Vocabulary Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Extends: NONE
      Group: enforcement_stage
      Casing: lower_snake
      Value: compiler_validation
      Meaning: A phase of the build carries the obligation directly. The check must have a path that produces a refusal.
      Source Finding: S6 boundary_rules A_CLAIM_OF_ENFORCEMENT_IS_CHECKED
    - Vocabulary Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Extends: NONE
      Group: enforcement_stage
      Casing: lower_snake
      Value: compiler_meta_validation
      Meaning: The build carries the obligation over its own governance surface. The check must have a path that produces a refusal.
      Source Finding: S6 boundary_rules A_CLAIM_OF_ENFORCEMENT_IS_CHECKED
    - Vocabulary Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Extends: NONE
      Group: enforcement_stage
      Casing: lower_snake
      Value: runtime_outcome
      Meaning: The obligation is carried by a violation outcome and its routing. No check is derived. A destination is named.
      Source Finding: S6 boundary_rules A_DELEGATION_NAMES_ITS_PLACE
    - Vocabulary Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Extends: NONE
      Group: enforcement_stage
      Casing: lower_snake
      Value: composition_conformance
      Meaning: The obligation is carried by the assembler over the composed snapshot. No check is derived. A destination is named.
      Source Finding: S6 boundary_rules A_DELEGATION_NAMES_ITS_PLACE
    - Vocabulary Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Extends: NONE
      Group: enforcement_stage
      Casing: lower_snake
      Value: enforced_elsewhere
      Meaning: The obligation is carried by a named mechanism outside the build. No check is derived. A destination is named, and it is confirmed to exist.
      Source Finding: S6 boundary_rules A_DELEGATION_NAMES_ITS_PLACE
    - Vocabulary Code: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Extends: NONE
      Group: enforcement_stage
      Casing: lower_snake
      Value: declared_not_enforced
      Meaning: The obligation is stated deliberately and carried by nothing yet. No check is derived, no destination is named, and the obligation is counted as unenforced.
      Source Finding: S6 boundary_rules A_DEFERRAL_IS_DECLARED_NOT_WRITTEN
  runtime_policies:
    columns:
    - RB Code
    - Capability
    - Key
    - Value
    - Source Finding
    rows:
    - RB Code: NONE IDENTIFIED
      Capability: ''
      Key: ''
      Value: ''
      Source Finding: ''
  artifact_properties:
    columns:
    - Artifact
    - Property
    - Value
    - Source Finding
    rows:
    - Artifact: conformance::INVARIANT_ASSERT_PARITY_V0
      Property: core.enforcement_stage
      Value: enforced_elsewhere
      Source Finding: 'S7 design_resolution #6'
    - Artifact: conformance::INVARIANT_ASSERT_PARITY_V0
      Property: core.enforced_by
      Value: The step of the build that derives a check from its obligation
      Source Finding: 'S7 design_resolution #6'
    - Artifact: conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0
      Property: core.enforcement_stage
      Value: enforced_elsewhere
      Source Finding: 'S7 design_resolution #2'
    - Artifact: conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0
      Property: core.enforced_by
      Value: The phase of the build that validates test data
      Source Finding: 'S7 design_resolution #2'
    - Artifact: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Property: governed_by
      Value: vocabulary::CONSTITUTION_VOCABULARY_V0
      Source Finding: S7 new_artifacts VOCAB_ENFORCEMENT_STATUS_V0
    - Artifact: conformance::VOCAB_ENFORCEMENT_STATUS_V0
      Property: concern
      Value: conformance
      Source Finding: 'S6 ownership #2'
  structure_stores:
    columns:
    - Store Name
    - Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)
    - Proposed Path
    - Used By
    - Source Finding
    rows:
    - Store Name: NONE IDENTIFIED
      Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0): ''
      Proposed Path: ''
      Used By: ''
      Source Finding: ''
  transport_bindings:
    columns:
    - Artifact
    - Direction (INGRESS, EGRESS)
    - Operation
    - Handler Kind (WF_INVOCATION, SNAPSHOT_READ)
    - Handler Target
    - Field
    - Bound To
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Direction (INGRESS, EGRESS): ''
      Operation: ''
      Handler Kind (WF_INVOCATION, SNAPSHOT_READ): ''
      Handler Target: ''
      Field: ''
      Bound To: ''
      Source Finding: ''
  artifact_summary:
    columns:
    - Action (REPLACE, EXTEND, NEW)
    - Subdomain
    - Count
    - Artifacts
    rows:
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: conformance
      Count: '1'
      Artifacts: conformance::VOCAB_ENFORCEMENT_STATUS_V0
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: NONE IDENTIFIED
      Generator: ''
      Generator Sources: ''
      Source Finding: ''
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: NONE IDENTIFIED
      Consults: ''
      Source Finding: ''
  refusal_discharge:
    columns:
    - Operation
    - Refused When
    - Act
    - Step
    - Outcome
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Act: ''
      Step: ''
      Outcome: ''
      Source Finding: ''
  refusal_deferrals:
    columns:
    - Operation
    - Refused When
    - Deferred To
    - Until
    - Source Finding
    rows:
    - Operation: Building a composition
      Refused When: An obligation declares itself enforced and its check cannot refuse anything
      Deferred To: The six subdomains that own the fourteen
      Until: Each restates its own obligations with the stage that matches what its check does. The rule is written by this change and armed after they have, because arming it first would fail every build on obligations this dossier may not write.
      Source Finding: 'S1 operation_refusals #1'
    - Operation: Building a composition
      Refused When: An obligation declares enforcement elsewhere and does not name where
      Deferred To: The four subdomains whose obligations delegate in prose
      Until: Each names the mechanism its check's own text already states. The rule is written by this change and armed after they have.
      Source Finding: 'S1 operation_refusals #2'
    - Operation: Admitting an obligation as governance
      Refused When: Its check only reports and never refuses
      Deferred To: capability_contracts
      Until: That subdomain withdraws the one obligation of eighty-nine whose violation warns. The rule this change writes refuses a check with no refusal path; this check has one its obligation cannot reach, so the correction is a declaration rather than a refusal.
      Source Finding: 'S1 operation_refusals #3'
  refusal_governance_discharge:
    columns:
    - Operation
    - Refused When
    - Phase
    - Governing Rule
    - Source Finding
    rows:
    - Operation: NONE IDENTIFIED
      Refused When: ''
      Phase: ''
      Governing Rule: ''
      Source Finding: ''
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
