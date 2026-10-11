# Stage 7 — Design Intent: platform / structure

## Machine

```yaml
document:
  phase: p7
  domain: platform
  subdomain: structure
  cr: schema_governance
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: How a kind's disposition is recorded
    business_fact: A kind absent from the dispatch table is absent for three different reasons and one representation.
    resolution: 'The dispatch table carries a disposition per kind, drawn from a vocabulary: described, or exempt with a ground. A kind carrying neither is refused.'
    source_finding: {phase: p6, register: boundary_rules, key: EVERY_KIND_HAS_A_DISPOSITION}
  - decision: What makes a description a description
    business_fact: One is dispatched, requires no field, closes no surface, and reads as governance.
    resolution: The constitution governing structural declarations states that a description names at least one required field and closes its surface. A kind dispatched to one that does neither is refused.
    source_finding: {phase: p6, register: boundary_rules, key: A_DESCRIPTION_STATES_SOMETHING}
  - decision: How drift is reported
    business_fact: Three divergences, none recorded, all found by a build refusing correct work.
    resolution: Every dispatched description is measured against every artifact of its kind on each build, and a description that refuses one is reported before it is enforced.
    source_finding: {phase: p6, register: boundary_rules, key: DRIFT_IS_REPORTED_NOT_DISCOVERED}
  - decision: Who corrects a drifted description
    business_fact: The three describe kinds owned by `actor`, `event` and `intent`.
    resolution: Each is cited for its owner. This dossier states the requirement and the report; it writes no description.
    source_finding: {phase: p6, register: boundary_rules, key: A_KINDS_SHAPE_IS_ITS_OWNERS}
  - decision: Who describes the two undescribed kinds
    business_fact: Both are transport boundary contracts, 44 artifacts.
    resolution: Cited for `transport`. Same ground.
    source_finding: {phase: p6, register: boundary_rules, key: A_KINDS_SHAPE_IS_ITS_OWNERS}
  - decision: Whether any artifact is authored here
    business_fact: Every capability but one is a requirement added to something that exists.
    resolution: 'One vocabulary is authored: the dispositions a kind may have. The governance surface is authored by hand rather than rendered, so the two amendments are cited and not scheduled.'
    source_finding: {phase: p6, register: ownership, row: 1}
  existing_inventory:
  - fqdn: structure::STRUCTURE_SCHEMA_DISPATCH_V0
    action: REVIEW
    summary: Declares which description governs each artifact kind
    reason: Gains a disposition per kind, so an exemption and an oversight stop being the same absence. Authored by hand, not rendered.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: structure::CONSTITUTION_STRUCTURE_V0
    action: REVIEW
    summary: Governs what a structural declaration is
    reason: Gains what a description must state to count as one, and that every kind carries a disposition. Authored by hand.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: artifact::INVARIANT_SCHEMA_CONFORMANCE_V0
    action: REUSE
    summary: Checks each declaration against the description its kind is dispatched to
    reason: Correct and unchanged; it is only ever handed ten kinds, which is the dispatch table's doing rather than its own.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: actor::CONSTITUTION_ACTOR_V0
    action: REVIEW
    summary: Governs what an actor is
    reason: Its description expects a role and forbids the attributes every actor carries, across 11 artifacts. Named for `actor` to correct.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: event::CONSTITUTION_EVENT_V0
    action: REVIEW
    summary: Governs what a moment is
    reason: Its description forbids content 20 event declarations carry. Named for `event` to correct.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: intent::CONSTITUTION_INTENT_V0
    action: REVIEW
    summary: Governs what a boundary admits
    reason: Its description rejects a whole number as a type across 31 declarations. Named for `intent` to correct.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0
    action: REVIEW
    summary: Governs the boundary contracts
    reason: Its two kinds carry 44 artifacts described by nothing. Named for `transport` to describe.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: trace::CONSTITUTION_TRACE_EXECUTION_V0
    action: REUSE
    summary: Governs the runtime trace
    reason: Named because four descriptions counted as failing to close a surface describe runtime data of this sort. Unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  new_artifacts:
  - capability: Recording that a kind needs no description
    family: VOCAB
    code: structure::VOCAB_SCHEMA_DISPOSITION_V0
    summary: The dispositions a kind may have toward description, and which of them the build admits
    owner_subdomain: structure
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 3}
  rb_declarations: []
  execution_topology: []
  cc_composition: []
  step_bindings: []
  interface_fields:
  - artifact: structure::VOCAB_SCHEMA_DISPOSITION_V0
    direction: ATTRIBUTE
    field: symbols
    type: object
    required: 'YES'
    default: null
    meaning: The two dispositions a kind may have and what each means. A kind carrying neither is refused, which needs no symbol of its own.
  implementation_bindings: []
  vocabulary_extensions:
  - vocabulary_code: structure::VOCAB_SCHEMA_DISPOSITION_V0
    extends: null
    group: schema_disposition
    casing: lower_snake
    value: described
    meaning: A description governs the kind and the build reads it. The description must name at least one required field and close its surface.
    source_finding: {phase: p7, register: design_resolution, row: 2}
  - vocabulary_code: structure::VOCAB_SCHEMA_DISPOSITION_V0
    extends: null
    group: schema_disposition
    casing: lower_snake
    value: exempt
    meaning: The kind needs no description and the ground is stated beside the disposition. Admitted, and readable as a decision rather than an absence.
    source_finding: {phase: p7, register: design_resolution, row: 1}
  runtime_policies: []
  artifact_properties:
  - artifact: structure::VOCAB_SCHEMA_DISPOSITION_V0
    property: governed_by
    value: vocabulary::CONSTITUTION_VOCABULARY_V0
    source_finding: {phase: p7, register: new_artifacts, key: VOCAB_SCHEMA_DISPOSITION_V0}
  - artifact: structure::VOCAB_SCHEMA_DISPOSITION_V0
    property: concern
    value: structure
    source_finding: {phase: p6, register: ownership, row: 3}
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: structure
    count: '1'
    artifacts: structure::VOCAB_SCHEMA_DISPOSITION_V0
  generation_provenance: []
  declared_reach: []
  refusal_discharge: []
  refusal_deferrals:
  - operation: Building a composition
    refused_when: A declaration carries content the description of its kind does not name
    deferred_to: structure
    until: Carried today for ten kinds and extended to every kind that gains a description. Recorded as a deferral because the kinds whose descriptions are corrected elsewhere are dispatched by their owners, not here.
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - operation: Building a composition
    refused_when: An artifact kind is neither described nor recorded as exempt
    deferred_to: structure
    until: The dispatch table carries a disposition for every kind. Armed once every kind has one, because arming it first would refuse every build on kinds this dossier does not describe.
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - operation: Dispatching a description
    refused_when: It refuses an artifact the composition currently carries
    deferred_to: structure
    until: The report is written by this change and names such a description before it is enforced. The dispatch itself is the owning subdomain's act, once its description is corrected.
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
`8f82acb652c8…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the authoring of one vocabulary and the hand-authoring of the two
amendments §2 cites for this subdomain. It authorizes nothing else.

The scope narrowed twice in discovery and both narrowings are the finding. Five open surfaces were
two populations, and four of them describe runtime data rather than declarations — miscounted because
a directory and a naming convention are all that identify a description's population. And a kind
dispatched to a description that describes nothing reads as governed, so **the count of dispatched
kinds measures neither coverage nor governance**, which is why this change delivers a report rather
than a tally.
