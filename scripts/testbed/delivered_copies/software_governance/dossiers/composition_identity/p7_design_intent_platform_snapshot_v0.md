# Stage 7 — Design Intent: platform / snapshot

## Machine

```yaml
header:
  Stage: 7 — Design Intent
  CR: composition_identity
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
    - Decision: What is excluded from a composition's identity
      Business Fact: The attestation carries two fields the runtime enforces and one that records when the signing happened.
      Resolution: The exclusion is stated as a field within a named file, not as a path. The enumeration that lists constituents excludes that field from the value it takes over the attestation's bytes, and takes the value over what remains.
      Source Finding: S6 boundary_rules DETERMINATIVE_CONTENT_STAYS
    - Decision: Where the exclusion is stated
      Business Fact: Two exclusions already exist, each naming its ground where the exclusion is made.
      Resolution: The new exclusion is added beside them, in the same list, carrying its own ground. Nothing is excluded by directory, by suffix or by convention.
      Source Finding: S6 boundary_rules EXCLUSION_IS_DECLARED
    - Decision: Who states which fields constitute
      Business Fact: What an attestation carries is the cryptographic trust subdomain's to declare.
      Resolution: '`cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0` states the division. This dossier consumes it and does not write it; the constitution is cited for its owner to author.'
      Source Finding: S6 boundary_rules AN_ATTESTATION_IS_STATED_BY_ITS_OWNER
    - Decision: How a rebuild is required to reproduce
      Business Fact: Nothing requires it today, which is why twenty failing pins went unreported.
      Resolution: An obligation of the snapshot subdomain requires that constituting the same source twice yields one identity, carried by the assembler over a composition it has just built.
      Source Finding: S6 boundary_rules A_REBUILD_REPRODUCES
    - Decision: What the change does not claim
      Business Fact: Two builds on one machine minutes apart is what was measured.
      Resolution: The obligation is stated over a rebuild of unchanged source, not over builds on different machines. A further instability is a further change.
      Source Finding: S6 boundary_rules ONLY_WHAT_WAS_MEASURED_IS_CLAIMED
    - Decision: Whether any artifact is authored
      Business Fact: Every capability this change needs is a requirement added to something that exists.
      Resolution: No artifact is authored. The governance surface is authored by hand rather than rendered, so every row of §2 is cited and none is scheduled.
      Source Finding: 'S6 ownership #1'
  existing_inventory:
    columns:
    - FQDN
    - Action (REPLACE, REUSE, EXTEND, REVIEW)
    - Summary
    - Reason
    - Source Finding
    rows:
    - FQDN: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Governs what may be trusted and how a build attests what it produced
      Reason: Gains the statement of which of an attestation's fields constitute the composition it attests and which accompany it. Authored by hand by its owning subdomain, not rendered, and not written here.
      Source Finding: 'S6 pps_artifacts_requiring_action #1'
    - FQDN: cryptographic_trust::INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Requires a build to declare the trust arrangement it runs under
      Reason: Requires the declaration and nothing about what the resulting attestation may contribute to an identity. Named as the obligation the new statement sits beside.
      Source Finding: 'S6 pps_artifacts_requiring_action #2'
    - FQDN: cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: 'Declares the arrangement in force: local, unsigned'
      Reason: What makes a placeholder signature admissible. Unchanged, and named because the change holds whether the signature is a placeholder or real.
      Source Finding: 'S6 pps_artifacts_requiring_action #3'
    - FQDN: compiler::INVARIANT_ARTIFACT_CONTENT_HASH_DECLARED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Requires an artifact to declare a value over its content
      Reason: Covers an artifact. A composition's identity is taken over files rather than artifacts, and this is the nearest existing requirement.
      Source Finding: 'S6 pps_artifacts_requiring_action #4'
    - FQDN: artifact::INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REVIEW
      Summary: Requires one artifact to carry one identity everywhere it appears
      Reason: The same requirement stated for an artifact. Nothing states it for a composition, which is the gap this change fills.
      Source Finding: 'S6 pps_artifacts_requiring_action #5'
    - FQDN: execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0
      Action (REPLACE, REUSE, EXTEND, REVIEW): REUSE
      Summary: Confirms an obligation delegated to a runtime outcome is bound to one
      Reason: The runtime's refusal of a composition whose projection does not match its attestation is why the attestation stays a constituent. Unchanged.
      Source Finding: 'S6 pps_artifacts_requiring_action #6'
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
    - Capability: NONE IDENTIFIED
      Family: ''
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
    - Artifact: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: attestation.constitutes
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The fields of an attestation that constitute the composition it attests. A composition's identity is taken over these.
    - Artifact: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
      Direction (INPUT, OUTPUT, ATTRIBUTE): ATTRIBUTE
      Field: attestation.accompanies
      Type: array
      Required (YES, NO): 'YES'
      Default: —
      Meaning: The fields of an attestation that record about the composition rather than constitute it. A composition's identity is taken over the attestation with these removed.
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
    - Artifact: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
      Property: attestation.accompanies
      Value: signed_at
      Source Finding: 'S7 design_resolution #1'
    - Artifact: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
      Property: attestation.constitutes
      Value: tokenized_projection_hash, attestation_hash
      Source Finding: 'S7 design_resolution #1'
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
      Subdomain: snapshot
      Count: '0'
      Artifacts: ''
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
    - Operation: Verifying a composition
      Refused When: A file it carries as a constituent does not match the bytes its identity was taken over
      Deferred To: snapshot
      Until: Already carried today, and unchanged by this. It is recorded here rather than as a discharge because this change adds no act; what it changes is which bytes the identity is taken over.
      Source Finding: 'S1 operation_refusals #1'
    - Operation: Verifying a composition
      Refused When: It is read somewhere other than where its identity says it was built for
      Deferred To: snapshot
      Until: Already carried today, and unchanged by this. Recorded for the same reason.
      Source Finding: 'S1 operation_refusals #2'
    - Operation: Verifying a composition against a pin
      Refused When: The identity differs
      Deferred To: snapshot
      Until: Already carried today. What changes is that a difference will mean the compositions differ, which is the point of the change rather than a new refusal.
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
`47dd8edc2123…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the hand-authoring of the two amendments §2 cites, and nothing else.
This design schedules no artifact and construction renders none.

The design's whole substance is two declarations: an attestation's projection binding and the value
over it constitute the composition, and the moment it was signed accompanies it. Excluding the file
rather than the field was considered and refused, because the runtime enforces the binding and
dropping it from the identity is the opposite of what this change wants.
