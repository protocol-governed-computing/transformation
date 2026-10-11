# Stage 7 — Design Intent: platform / structure

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: schema_governance
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
    - Decision: How a kind's disposition is recorded
      Business Fact: A kind absent from the dispatch table is absent for three different reasons and one representation.
      Resolution: 'The dispatch table carries a disposition per kind, drawn from a vocabulary: described, or exempt with a ground. A kind carrying neither is refused.'
      Source Finding: S6 boundary_rules EVERY_KIND_HAS_A_DISPOSITION
    - Decision: What makes a description a description
      Business Fact: One is dispatched, requires no field, closes no surface, and reads as governance.
      Resolution: The constitution governing structural declarations states that a description names at least one required field and closes its surface. A kind dispatched to one that does neither is refused.
      Source Finding: S6 boundary_rules A_DESCRIPTION_STATES_SOMETHING
    - Decision: How drift is reported
      Business Fact: Three divergences, none recorded, all found by a build refusing correct work.
      Resolution: Every dispatched description is measured against every artifact of its kind on each build, and a description that refuses one is reported before it is enforced.
      Source Finding: S6 boundary_rules DRIFT_IS_REPORTED_NOT_DISCOVERED
    - Decision: Who corrects a drifted description
      Business Fact: The three describe kinds owned by `actor`, `event` and `intent`.
      Resolution: Each is cited for its owner. This dossier states the requirement and the report; it writes no description.
      Source Finding: S6 boundary_rules A_KINDS_SHAPE_IS_ITS_OWNERS
    - Decision: Who describes the two undescribed kinds
      Business Fact: Both are transport boundary contracts, 44 artifacts.
      Resolution: Cited for `transport`. Same ground.
      Source Finding: S6 boundary_rules A_KINDS_SHAPE_IS_ITS_OWNERS
    - Decision: Whether any artifact is authored here
      Business Fact: Every capability but one is a requirement added to something that exists.
      Resolution: 'One vocabulary is authored: the dispositions a kind may have. The governance surface is authored by hand rather than rendered, so the two amendments are cited and not scheduled.'
      Source Finding: 'S6 ownership #1'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: structure::STRUCTURE_SCHEMA_DISPATCH_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Declares which description governs each artifact kind
      Reason: Gains a disposition per kind, so an exemption and an oversight stop being the same absence. Authored by hand, not rendered.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: structure::CONSTITUTION_STRUCTURE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Governs what a structural declaration is
      Reason: Gains what a description must state to count as one, and that every kind carries a disposition. Authored by hand.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: artifact::INVARIANT_SCHEMA_CONFORMANCE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Checks each declaration against the description its kind is dispatched to
      Reason: Correct and unchanged; it is only ever handed ten kinds, which is the dispatch table's doing rather than its own.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: actor::CONSTITUTION_ACTOR_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Governs what an actor is
      Reason: Its description expects a role and forbids the attributes every actor carries, across 11 artifacts. Named for `actor` to correct.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: event::CONSTITUTION_EVENT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Governs what a moment is
      Reason: Its description forbids content 20 event declarations carry. Named for `event` to correct.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: intent::CONSTITUTION_INTENT_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Governs what a boundary admits
      Reason: Its description rejects a whole number as a type across 31 declarations. Named for `intent` to correct.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
    - FQDN: transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Governs the boundary contracts
      Reason: Its two kinds carry 44 artifacts described by nothing. Named for `transport` to describe.
      Source Finding: 'S6 pps_artifacts_requiring_action #7'
    - FQDN: trace::CONSTITUTION_TRACE_EXECUTION_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Governs the runtime trace
      Reason: Named because four descriptions counted as failing to close a surface describe runtime data of this sort. Unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #8'
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
    - Capability: Recording that a kind needs no description
      Family: VOCAB
      Code: structure::VOCAB_SCHEMA_DISPOSITION_V0
      Summary: The dispositions a kind may have toward description, and which of them the build admits
      Owner Subdomain: structure
      Status: NEW
      Source Finding: 'S6 governance_outcome #3'
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
    - Artifact: structure::VOCAB_SCHEMA_DISPOSITION_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: symbols
      Type: object
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The two dispositions a kind may have and what each means. A kind carrying neither is refused, which needs no symbol of its own.
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
    - Vocabulary Code: structure::VOCAB_SCHEMA_DISPOSITION_V0
      Extends: NONE
      Group: schema_disposition
      Casing: lower_snake
      Value: described
      Meaning: A description governs the kind and the build reads it. The description must name at least one required field and close its surface.
      Source Finding: 'S7 design_resolution #2'
    - Vocabulary Code: structure::VOCAB_SCHEMA_DISPOSITION_V0
      Extends: NONE
      Group: schema_disposition
      Casing: lower_snake
      Value: exempt
      Meaning: The kind needs no description and the ground is stated beside the disposition. Admitted, and readable as a decision rather than an absence.
      Source Finding: 'S7 design_resolution #1'
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
    - Artifact: structure::VOCAB_SCHEMA_DISPOSITION_V0
      Property: governed_by
      Value: vocabulary::CONSTITUTION_VOCABULARY_V0
      Source Finding: S7 new_artifacts VOCAB_SCHEMA_DISPOSITION_V0
    - Artifact: structure::VOCAB_SCHEMA_DISPOSITION_V0
      Property: concern
      Value: structure
      Source Finding: 'S6 ownership #3'
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
      Subdomain: structure
      Count: '1'
      Artifacts: structure::VOCAB_SCHEMA_DISPOSITION_V0
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
      Refused When: A declaration carries content the description of its kind does not name
      Deferred To: structure
      Until: Carried today for ten kinds and extended to every kind that gains a description. Recorded as a deferral because the kinds whose descriptions are corrected elsewhere are dispatched by their owners, not here.
      Source Finding: 'S1 operation_refusals #1'
    - Operation: Building a composition
      Refused When: An artifact kind is neither described nor recorded as exempt
      Deferred To: structure
      Until: The dispatch table carries a disposition for every kind. Armed once every kind has one, because arming it first would refuse every build on kinds this dossier does not describe.
      Source Finding: 'S1 operation_refusals #2'
    - Operation: Dispatching a description
      Refused When: It refuses an artifact the composition currently carries
      Deferred To: structure
      Until: The report is written by this change and names such a description before it is enforced. The dispatch itself is the owning subdomain's act, once its description is corrected.
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
`8f82acb652c8…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the authoring of one vocabulary and the hand-authoring of the two
amendments §2 cites for this subdomain. It authorizes nothing else.

The scope narrowed twice in discovery and both narrowings are the finding. Five open surfaces were
two populations, and four of them describe runtime data rather than declarations — miscounted because
a directory and a naming convention are all that identify a description's population. And a kind
dispatched to a description that describes nothing reads as governed, so **the count of dispatched
kinds measures neither coverage nor governance**, which is why this change delivers a report rather
than a tally.
