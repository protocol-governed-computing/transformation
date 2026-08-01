# Analysis Loop — book_library_mgmt / catalog

**Stage:** 3 — Analysis Loop
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

> P3 decides. P2 discovered what exists and deferred the extend-vs-new question; P3 resolves it by
> evidence and commits every capability to REUSE, EXTEND or AUTHOR_NEW. Grounding is not inherited:
> every prior finding is re-checked against the composition, and an overturned answer is marked,
> never erased.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| S2-OQ-1 | Retirement applies to the bibliographic work record only; a copy record is withdrawn with the work it belongs to, not independently. | The lifecycle a design must support has one retirable object, not two. | OPEN | MEDIUM | CLOSED | Business author answered at the S2 gate; the composition holds nothing that could settle it. |
| S2-GAP-1 | No authoritative record for a bibliographic work or a physical copy exists anywhere in the composition. | Every requested outcome rests on records this change must author. | OBSERVED | HIGH | CLOSED | Vocabulary search returns no identity for book, library, bibliographic or copy. |
| S2-GAP-3 | A durable record of a performed action exists but carries another subdomain's shape and writes to a store that subdomain owns exclusively. | The mechanism is reusable; the audit shape and its store are not. | OBSERVED | HIGH | CLOSED | ai_governance::CC_APPEND_AUDIT_EVENT_V0 writes to a store declared by ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0. |
| S2-GAP-4 | The authority that grants staff authorization is undecided, and patron management is deferred. | Authorization is checked as a precondition; who grants it is a later change. | OPEN | MEDIUM | OPEN | No capability in the composition governs library staff authorization. |
| S2-DC-2 | Search and retrieval are business operations and leave a durable record like any other. | Two read operations acquire an audit step they would not otherwise have. | OPEN | MEDIUM | CLOSED | Business author answered at the S2 gate; the requirement is stated for every business operation. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| No capability in the current composition manages a library catalog. | S2 belief_verification #1 | CONFIRMED | Re-checked against the composition: no identity for book, library, bibliographic or copy; the only catalog identities publish the inspection operation list. |
| The platform offers a governed form in which a business capability of this kind can be declared. | S2 belief_verification #2 | CONFIRMED | ai_governance::IN_PROVISION_AI_LICENSE_V0, ai_governance::CC_PROVISION_LICENSE_V0, ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 |
| The platform already records business operations in a way that can be audited afterwards. | S2 belief_verification #3 | CONFIRMED | ai_governance::CC_APPEND_AUDIT_EVENT_V0 over capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| Keyed mutable state is available for records that are updated in place. | S2 pps_baseline_fqdns | CONFIRMED | capability_side_effects::CS_MUTABLE_JSON_V0 is consumed by 12 artifacts across the composition. |
| The audit mechanism could be reused as-is, including its shape. | S2 pps_baseline_fqdns Fit PARTIAL | OVERTURNED | ai_governance::CC_APPEND_AUDIT_EVENT_V0 binds a store its own subdomain declares; a subdomain owns its stores exclusively, so the contract cannot be reused unchanged. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| Keyed mutable state for records updated in place | storage mechanism | REUSE | capability_side_effects::CS_MUTABLE_JSON_V0 |
| Append-only durable record for performed operations | storage mechanism | REUSE | capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| Storage declaration owned by this subdomain | governance declaration | AUTHOR_NEW | ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 declares another subdomain's stores; ownership is exclusive. |
| Business actor for library staff | actor | AUTHOR_NEW | ai_governance::AC_EMPLOYEE_V0 names an employee and asserts no authorization. |
| Authority granting staff authorization | governance boundary | INVESTIGATE | No capability in the composition governs it; patron management is deferred. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | transitive consumer closure | 12 | si.topology.impact impacted_count=12 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | transitive consumer closure | 21 | si.topology.impact impacted_count=21 |
| ai_governance::CC_APPEND_AUDIT_EVENT_V0 | transitive consumer closure | 9 | si.topology.impact impacted_count=9 |
| ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 | transitive consumer closure | 0 | si.topology.impact impacted_count=0 |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Hold a catalog record that can be updated in place | REUSE | The mechanism holds keyed state and enforces no business rule over it, which is exactly what a record store must do. | capability_side_effects::CS_MUTABLE_JSON_V0 ; capability_side_effects::CS_REGISTRY_V0 | S3 dependency_discoveries Keyed mutable state |
| Append a durable record of a performed operation | REUSE | Appending to a record that is never rewritten is what auditability requires, and the mechanism decides nothing about what may happen. | capability_side_effects::CS_APPENDONLY_JSONL_V0 ; capability_side_effects::CS_MUTABLE_JSON_V0 | S3 dependency_discoveries Append-only durable record |
| Register a book | AUTHOR_NEW | Nothing in the composition registers a library material; the operation carries catalog semantics that no existing pipeline expresses. | transformation::CT_PURE_EVALUATE_RULES_V0 ; ai_governance::CC_PROVISION_LICENSE_V0 | S3 analysis_findings S2-GAP-1 |
| Register a physical copy against one work | AUTHOR_NEW | The one-work rule is the business invariant stated most firmly and nothing existing enforces it. | capability_side_effects::CS_REGISTRY_V0 ; ai_governance::CC_VALIDATE_ELIGIBILITY_V0 | S3 analysis_findings S2-GAP-1 |
| Update bibliographic information | AUTHOR_NEW | Replacing descriptive content on a governed record has no existing counterpart. | ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0 | S3 analysis_findings S2-GAP-1 |
| Retire an obsolete record | AUTHOR_NEW | Retirement marks a record no longer current; the nearest existing behaviour reclaims a licence, which is a different act. | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | S3 analysis_findings S2-OQ-1 |
| Search the catalog | AUTHOR_NEW | No existing capability selects business records by staff-supplied terms. | ai_governance::CC_CHECK_TOOL_DECLARED_V0 | S3 analysis_findings S2-GAP-1 |
| Retrieve complete book details | AUTHOR_NEW | Assembling a work with the copies belonging to it has no existing counterpart. | workload::CC_COMPUTE_COLLATZ_STEP_V0 | S3 analysis_findings S2-GAP-1 |
| Record that a catalog operation was performed | AUTHOR_NEW | The append mechanism is reused, but the audit contract binds a store its own subdomain owns exclusively, so the catalog declares its own. | ai_governance::CC_APPEND_AUDIT_EVENT_V0 ; ai_governance::CC_RECORD_GOVERNED_ACTION_V0 | S3 verification_results The audit mechanism could be reused as-is |
| Confirm the staff member is authorized | AUTHOR_NEW | Authorization is a precondition of every operation; the existing actor form names an employee and asserts nothing about permission. | ai_governance::AC_EMPLOYEE_V0 ; ai_governance::CC_ENFORCE_LICENSE_CAP_V0 | S3 dependency_discoveries Business actor for library staff |
| Declare the stores this subdomain owns | AUTHOR_NEW | A subdomain owns its stores exclusively and declares them itself. | ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 | S3 dependency_discoveries Storage declaration |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| NEW_SUBDOMAIN | catalog | The catalog describes what the library holds and owns those records exclusively; nothing existing describes holdings, so there is no boundary to extend. | S3 analysis_findings S2-GAP-1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All three S2 CRITICAL gaps resolve to committed AUTHOR_NEW decisions. |
| No open analyst questions | SATISFIED | Both S2 open questions are closed; the one remaining OPEN item is a deferred governance boundary, not an analyst question. |
| No dependency expansion in the last pass | SATISFIED | The final pass surfaced no dependency the previous pass had not already recorded. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Five items re-checked; the one OVERTURNED item is resolved by an AUTHOR_NEW decision recorded above. |
| Every INFERRED finding promoted, accepted, or carried with a reason | SATISFIED | The two OPEN findings answered at the gate are carried with the business author's answer as their reason; the authorization boundary is carried forward as a deferred dependency. |
