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
  - decision: What is excluded from a composition's identity
    business_fact: The attestation carries two fields the runtime enforces and one that records when the signing happened.
    resolution: The exclusion is stated as a field within a named file, not as a path. The enumeration that lists constituents excludes that field from the value it takes over the attestation's bytes, and takes the value over what remains.
    source_finding: {phase: p6, register: boundary_rules, key: DETERMINATIVE_CONTENT_STAYS}
  - decision: Where the exclusion is stated
    business_fact: Two exclusions already exist, each naming its ground where the exclusion is made.
    resolution: The new exclusion is added beside them, in the same list, carrying its own ground. Nothing is excluded by directory, by suffix or by convention.
    source_finding: {phase: p6, register: boundary_rules, key: EXCLUSION_IS_DECLARED}
  - decision: Who states which fields constitute
    business_fact: What an attestation carries is the cryptographic trust subdomain's to declare.
    resolution: '`cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0` states the division. This dossier consumes it and does not write it; the constitution is cited for its owner to author.'
    source_finding: {phase: p6, register: boundary_rules, key: AN_ATTESTATION_IS_STATED_BY_ITS_OWNER}
  - decision: How a rebuild is required to reproduce
    business_fact: Nothing requires it today, which is why twenty failing pins went unreported.
    resolution: An obligation of the snapshot subdomain requires that constituting the same source twice yields one identity, carried by the assembler over a composition it has just built.
    source_finding: {phase: p6, register: boundary_rules, key: A_REBUILD_REPRODUCES}
  - decision: What the change does not claim
    business_fact: Two builds on one machine minutes apart is what was measured.
    resolution: The obligation is stated over a rebuild of unchanged source, not over builds on different machines. A further instability is a further change.
    source_finding: {phase: p6, register: boundary_rules, key: ONLY_WHAT_WAS_MEASURED_IS_CLAIMED}
  - decision: Whether any artifact is authored
    business_fact: Every capability this change needs is a requirement added to something that exists.
    resolution: No artifact is authored. The governance surface is authored by hand rather than rendered, so every row of §2 is cited and none is scheduled.
    source_finding: {phase: p6, register: ownership, row: 1}
  existing_inventory:
  - fqdn: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
    action: REVIEW
    summary: Governs what may be trusted and how a build attests what it produced
    reason: Gains the statement of which of an attestation's fields constitute the composition it attests and which accompany it. Authored by hand by its owning subdomain, not rendered, and not written here.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: cryptographic_trust::INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0
    action: REVIEW
    summary: Requires a build to declare the trust arrangement it runs under
    reason: Requires the declaration and nothing about what the resulting attestation may contribute to an identity. Named as the obligation the new statement sits beside.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0
    action: REUSE
    summary: 'Declares the arrangement in force: local, unsigned'
    reason: What makes a placeholder signature admissible. Unchanged, and named because the change holds whether the signature is a placeholder or real.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: compiler::INVARIANT_ARTIFACT_CONTENT_HASH_DECLARED_V0
    action: REUSE
    summary: Requires an artifact to declare a value over its content
    reason: Covers an artifact. A composition's identity is taken over files rather than artifacts, and this is the nearest existing requirement.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: artifact::INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0
    action: REVIEW
    summary: Requires one artifact to carry one identity everywhere it appears
    reason: The same requirement stated for an artifact. Nothing states it for a composition, which is the gap this change fills.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0
    action: REUSE
    summary: Confirms an obligation delegated to a runtime outcome is bound to one
    reason: The runtime's refusal of a composition whose projection does not match its attestation is why the attestation stays a constituent. Unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  new_artifacts: []
  rb_declarations: []
  execution_topology: []
  cc_composition: []
  step_bindings: []
  interface_fields:
  - artifact: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
    direction: ATTRIBUTE
    field: attestation.constitutes
    type: array
    required: 'YES'
    default: null
    meaning: The fields of an attestation that constitute the composition it attests. A composition's identity is taken over these.
  - artifact: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
    direction: ATTRIBUTE
    field: attestation.accompanies
    type: array
    required: 'YES'
    default: null
    meaning: The fields of an attestation that record about the composition rather than constitute it. A composition's identity is taken over the attestation with these removed.
  implementation_bindings: []
  vocabulary_extensions: []
  runtime_policies: []
  artifact_properties:
  - artifact: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
    property: attestation.accompanies
    value: signed_at
    source_finding: {phase: p7, register: design_resolution, row: 1}
  - artifact: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
    property: attestation.constitutes
    value: tokenized_projection_hash, attestation_hash
    source_finding: {phase: p7, register: design_resolution, row: 1}
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: snapshot
    count: '0'
    artifacts: ''
  generation_provenance: []
  declared_reach: []
  refusal_discharge: []
  refusal_deferrals:
  - operation: Verifying a composition
    refused_when: A file it carries as a constituent does not match the bytes its identity was taken over
    deferred_to: snapshot
    until: Already carried today, and unchanged by this. It is recorded here rather than as a discharge because this change adds no act; what it changes is which bytes the identity is taken over.
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - operation: Verifying a composition
    refused_when: It is read somewhere other than where its identity says it was built for
    deferred_to: snapshot
    until: Already carried today, and unchanged by this. Recorded for the same reason.
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - operation: Verifying a composition against a pin
    refused_when: The identity differs
    deferred_to: snapshot
    until: Already carried today. What changes is that a difference will mean the compositions differ, which is the point of the change rather than a new refusal.
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
`47dd8edc2123…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the hand-authoring of the two amendments §2 cites, and nothing else.
This design schedules no artifact and construction renders none.

The design's whole substance is two declarations: an attestation's projection binding and the value
over it constitute the composition, and the moment it was signed accompanies it. Excluding the file
rather than the field was considered and refused, because the runtime enforces the binding and
dropping it from the identity is the opposite of what this change wants.
