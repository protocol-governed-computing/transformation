# Stage 7 — Design Intent: transformation / design

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: refusal_discharge
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
    - Decision: The refusals are read from the seed rather than carried forward.
      Business Fact: The rules that judge a design must read the refusals the business declared.
      Resolution: The design intent phase declares `p0` among its priors, alongside `p5` and `p6`. Business intent and governance intent already declare it, so the mechanism exists and this change uses it rather than adding one. The alternative was three registers and three carry rules across the intermediate phases, restating what the seed says and able to drift from it.
      Source Finding: 'S4 design_decisions #1'
    - Decision: A discharge is stated in one register and a deferral in another.
      Business Fact: A discharge names an act, a step and an outcome; a deferral names an owner and a condition.
      Resolution: Two registers of the design language, `refusal_discharge` and `refusal_deferrals`, declared in `templates/p7_design_intent_template_v0.md` and governed by rules in `transformation/design/p7_design_intent/rules.py`. One table holding both would leave several cells empty on every row, and a blank meaning *not applicable* is indistinguishable from one meaning *unanswered*.
      Source Finding: 'S4 design_decisions #2'
    - Decision: Coverage is asked of both registers at once.
      Business Fact: Every refusal the business declared is accounted for, as discharged or as deferred.
      Resolution: One rule, reading the seed's refusals against both registers. The kind that checks a prior's rows arrived reads a single register; it gains an optional list of registers defaulting to the one it reads today, exactly as the kind that resolves a cell against another register already does. Every existing rule using it is unchanged.
      Source Finding: 'S4 design_decisions #6'
    - Decision: A discharge is held to the design's own topology.
      Business Fact: A register read only for presence documents intent and enforces nothing.
      Resolution: Two rules and two check kinds. The first resolves the act and step against `execution_topology` and requires the outcome to be one that step reports. The second reads the node that outcome routes to and requires it to be an ending that refuses. Both read the design alone; no composition fact is observed.
      Source Finding: 'S4 design_decisions #5'
    - Decision: A refusing ending is one typed as a plain exit.
      Business Fact: An outcome that routes onward does not refuse, however plainly the register says it does.
      Resolution: The topology types every node, and the corpus types a completing ending as a success exit and every refusing one as a plain exit. The rule reads that type; it does not read the node's name, which would be a convention anybody could break by naming an exit well.
      Source Finding: 'S4 design_decisions #3'
    - Decision: A deferral is held to the seed and to naming an owner.
      Business Fact: A deferral names its owner, and no deferral names a refusal the business did not declare.
      Resolution: The register's rows are confined to the seed's refusals by the same kind that confines the discharge register, and the owner column is required. Neither the authoring scope nor the seed's authority deferrals is keyed to a refusal, so there is nothing else to resolve into.
      Source Finding: 'S4 design_decisions #4'
    - Decision: Each new rule is proved by a probe built to fail it.
      Business Fact: No document in the corpus states a discharge, so every new rule would report clean while checking nothing.
      Resolution: Five probes, one per rule, in the phase testbed alongside the existing inadmissible fixtures. A rule whose probe passes has been shown to fire; a rule that only reports clean has been shown nothing.
      Source Finding: 'S4 design_decisions #7'
    - Decision: The change is delivered through the pipeline, naming the generator of the documents it amends.
      Business Fact: The judging artifacts are re-emitted by their generator, never written by hand.
      Resolution: The three amended artifacts are declared in §16 with their generator and its sources. Construction invokes the generator and writes none of them.
      Source Finding: 'S4 constraint_register #7'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: 'Phase 7 of the change pipeline: decide whether an offered Design Intent register is admissible'
      Reason: Carries the rule set that judges a design. Gains two registers, five rules, and the seed among its declared priors.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Parse a phase document and its priors, observe the composition, and judge them together
      Reason: Generated from every phase's rule module read together, so it is re-emitted when any of them changes. This change declares no observation, so what it passes is unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: transformation::CT_PURE_EVALUATE_RULES_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): EXTEND
      Summary: Apply a declared rule set to a parsed design and report every rule that failed
      Reason: Carries the check kinds the rules are built from. Gains two kinds, and one existing kind gains an optional parameter.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: transformation::WF_P0_SEED_ADMISSIBILITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: ''
      Reason: 'Declares the register the business states its refusals in. Unchanged: what the business may say is not what this change touches.'
      Source Finding: 'S4 constraint_register #4'
    - FQDN: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: ''
      Reason: Holds the change request's restatement to the seed in both directions. Unchanged, and the reason a rule may read the seed instead of the restatement.
      Source Finding: 'S4 design_decisions #1'
    - FQDN: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: ''
      Reason: Declares what the domain compiles. Unchanged; named because the amended artifacts are compiled under it.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
  new_artifacts:
    columns:
    - Capability
    - Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE)
    - Code
    - Summary
    - Owner Subdomain
    - Status
    - Source Finding
    rows:
    - Capability: NONE IDENTIFIED
      Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE): ''
      Code: ''
      Summary: ''
      Owner Subdomain: ''
      Status: ''
      Source Finding: ''
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
    - Artifact: NONE IDENTIFIED
      Direction (INPUT, OUTPUT, ATTRIBUTE): ''
      Field: ''
      Type: ''
      Required (YES, NO): ''
      Default: ''
      Meaning: ''
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
    - Value
    - Meaning
    - Source Finding
    rows:
    - Vocabulary Code: NONE IDENTIFIED
      Extends: ''
      Value: ''
      Meaning: ''
      Source Finding: ''
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
    - Artifact: NONE IDENTIFIED
      Property: ''
      Value: ''
      Source Finding: ''
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
    - Action (REPLACE, EXTEND, NEW): EXTEND
      Subdomain: design
      Count: '3'
      Artifacts: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0, transformation::CT_PURE_EVALUATE_RULES_V0
    - Action (REPLACE, EXTEND, NEW): NEW
      Subdomain: design
      Count: '0'
      Artifacts: ''
  generation_provenance:
    columns:
    - Artifact
    - Generator
    - Generator Sources
    - Source Finding
    rows:
    - Artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
      Generator: transformation.design.emit:emit_rule_sets
      Generator Sources: templates/p7_design_intent_template_v0.md, transformation/design/p7_design_intent/rules.py
      Source Finding: 'S4 constraint_register #7'
    - Artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
      Generator: transformation.design.emit:emit_rule_sets
      Generator Sources: transformation/design/meta.py, transformation/design/p0_change_seed/rules.py, transformation/design/p1_change_request/rules.py, transformation/design/p2_domain_model/rules.py, transformation/design/p3_analysis_loop/rules.py, transformation/design/p4_business_model/rules.py, transformation/design/p5_business_intent/rules.py, transformation/design/p6_governance_intent/rules.py, transformation/design/p7_design_intent/rules.py, transformation/design/p8_authoring_mandate/rules.py
      Source Finding: 'S4 constraint_register #7'
    - Artifact: transformation::CT_PURE_EVALUATE_RULES_V0
      Generator: transformation.design.emit:emit_rule_sets
      Generator Sources: transformation/design/checks.py
      Source Finding: 'S4 constraint_register #7'
  declared_reach:
    columns:
    - Act
    - Consults
    - Source Finding
    rows:
    - Act: NONE IDENTIFIED
      Consults: ''
      Source Finding: ''
```

HOW. Binding FQDNs are assigned here; business facts and placement decisions are not repeated.

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

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

---

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`6e1e571dbbb8…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the amendment of the three artifacts §2 marks EXTEND, each
re-emitted by the generator §16 declares, and nothing else. No register of this design names an
artifact to author, and §15 states that plainly: three EXTEND, zero NEW.

**This is the last design that will not have to account for its own refusals.** The seed of this
change declares four, and under the rule set in the pinned composition nothing asks what carries any
of them out — which is the defect, stated by the dossier that removes it. Each of the four is
discharged by a rule this change authors, and where they are stated is §1, because the register that
would hold them does not exist until this change delivers it.

**What this approval does not have that the last one had.** cr_03 was gated after Construction
Completeness read 100%, and that figure is the evidence a design uniquely determines its artifacts.
There is no such figure here: nothing in this change is rendered from a design register, so
Construction Completeness has nothing to read. The equivalent evidence arrives later and from
elsewhere — `emit_rule_sets --check` agreeing after the rules are written, and five probes each
built to fail. Approving this design is approving that substitution.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | Ownership, dependencies, artifacts requiring action | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
