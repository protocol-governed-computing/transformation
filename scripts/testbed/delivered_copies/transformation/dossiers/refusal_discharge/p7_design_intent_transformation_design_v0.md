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
  - decision: The refusals are read from the seed rather than carried forward.
    business_fact: The rules that judge a design must read the refusals the business declared.
    resolution: The design intent phase declares `p0` among its priors, alongside `p5` and `p6`. Business intent and governance intent already declare it, so the mechanism exists and this change uses it rather than adding one. The alternative was three registers and three carry rules across the intermediate phases, restating what the seed says and able to drift from it.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: A discharge is stated in one register and a deferral in another.
    business_fact: A discharge names an act, a step and an outcome; a deferral names an owner and a condition.
    resolution: Two registers of the design language, `refusal_discharge` and `refusal_deferrals`, declared in `templates/p7_design_intent_template_v0.md` and governed by rules in `transformation/design/p7_design_intent/rules.py`. One table holding both would leave several cells empty on every row, and a blank meaning *not applicable* is indistinguishable from one meaning *unanswered*.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: Coverage is asked of both registers at once.
    business_fact: Every refusal the business declared is accounted for, as discharged or as deferred.
    resolution: One rule, reading the seed's refusals against both registers. The kind that checks a prior's rows arrived reads a single register; it gains an optional list of registers defaulting to the one it reads today, exactly as the kind that resolves a cell against another register already does. Every existing rule using it is unchanged.
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - decision: A discharge is held to the design's own topology.
    business_fact: A register read only for presence documents intent and enforces nothing.
    resolution: Two rules and two check kinds. The first resolves the act and step against `execution_topology` and requires the outcome to be one that step reports. The second reads the node that outcome routes to and requires it to be an ending that refuses. Both read the design alone; no composition fact is observed.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: A refusing ending is one typed as a plain exit.
    business_fact: An outcome that routes onward does not refuse, however plainly the register says it does.
    resolution: The topology types every node, and the corpus types a completing ending as a success exit and every refusing one as a plain exit. The rule reads that type; it does not read the node's name, which would be a convention anybody could break by naming an exit well.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: A deferral is held to the seed and to naming an owner.
    business_fact: A deferral names its owner, and no deferral names a refusal the business did not declare.
    resolution: The register's rows are confined to the seed's refusals by the same kind that confines the discharge register, and the owner column is required. Neither the authoring scope nor the seed's authority deferrals is keyed to a refusal, so there is nothing else to resolve into.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: Each new rule is proved by a probe built to fail it.
    business_fact: No document in the corpus states a discharge, so every new rule would report clean while checking nothing.
    resolution: Five probes, one per rule, in the phase testbed alongside the existing inadmissible fixtures. A rule whose probe passes has been shown to fire; a rule that only reports clean has been shown nothing.
    source_finding: {phase: p4, register: design_decisions, row: 7}
  - decision: The change is delivered through the pipeline, naming the generator of the documents it amends.
    business_fact: The judging artifacts are re-emitted by their generator, never written by hand.
    resolution: The three amended artifacts are declared in §16 with their generator and its sources. Construction invokes the generator and writes none of them.
    source_finding: {phase: p4, register: constraint_register, row: 7}
  existing_inventory:
  - fqdn: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    action: EXTEND
    summary: 'Phase 7 of the change pipeline: decide whether an offered Design Intent register is admissible'
    reason: Carries the rule set that judges a design. Gains two registers, five rules, and the seed among its declared priors.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
    action: EXTEND
    summary: Parse a phase document and its priors, observe the composition, and judge them together
    reason: Generated from every phase's rule module read together, so it is re-emitted when any of them changes. This change declares no observation, so what it passes is unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: transformation::CT_PURE_EVALUATE_RULES_V0
    action: EXTEND
    summary: Apply a declared rule set to a parsed design and report every rule that failed
    reason: Carries the check kinds the rules are built from. Gains two kinds, and one existing kind gains an optional parameter.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: transformation::WF_P0_SEED_ADMISSIBILITY_V0
    action: REVIEW
    summary: ''
    reason: 'Declares the register the business states its refusals in. Unchanged: what the business may say is not what this change touches.'
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - fqdn: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
    action: REVIEW
    summary: ''
    reason: Holds the change request's restatement to the seed in both directions. Unchanged, and the reason a rule may read the seed instead of the restatement.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - fqdn: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
    action: REVIEW
    summary: ''
    reason: Declares what the domain compiles. Unchanged; named because the amended artifacts are compiled under it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  new_artifacts: []
  rb_declarations: []
  execution_topology: []
  cc_composition: []
  step_bindings: []
  interface_fields: []
  implementation_bindings: []
  vocabulary_extensions: []
  runtime_policies: []
  artifact_properties: []
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: EXTEND
    subdomain: design
    count: '3'
    artifacts: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0, transformation::CT_PURE_EVALUATE_RULES_V0
  - action: NEW
    subdomain: design
    count: '0'
    artifacts: ''
  generation_provenance:
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - templates/p7_design_intent_template_v0.md
    - transformation/design/p7_design_intent/rules.py
    source_finding: {phase: p4, register: constraint_register, row: 7}
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - transformation/design/meta.py
    - transformation/design/p0_change_seed/rules.py
    - transformation/design/p1_change_request/rules.py
    - transformation/design/p2_domain_model/rules.py
    - transformation/design/p3_analysis_loop/rules.py
    - transformation/design/p4_business_model/rules.py
    - transformation/design/p5_business_intent/rules.py
    - transformation/design/p6_governance_intent/rules.py
    - transformation/design/p7_design_intent/rules.py
    - transformation/design/p8_authoring_mandate/rules.py
    source_finding: {phase: p4, register: constraint_register, row: 7}
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V0
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - transformation/design/checks.py
    source_finding: {phase: p4, register: constraint_register, row: 7}
  declared_reach: []
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
