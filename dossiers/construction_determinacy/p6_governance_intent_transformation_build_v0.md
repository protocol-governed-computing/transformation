# Stage 6 — Governance Intent: transformation / build
**Stage:** 6 — Governance Intent
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `build` — EXISTING — modified by this CR |
| Authority class | reuse existing — a design states, a renderer produces, a measure refuses; no new actor type |
| Governing constitutions | `workflow::CONSTITUTION_WORKFLOW_V0`, `vocabulary::CONSTITUTION_VOCABULARY_V0` |

Measuring a design, rendering its artifacts and writing them is what this subdomain governs, so
reporting where each value came from, testing provenance rather than emptiness, and ceasing to write
an artifact no mandate scheduled all belong here. Two artifacts stand on their own and are authored
in this subdomain.

**The register a vocabulary's group and spelling belong in is not this subdomain's to write.** A
phase's registers and the rule set that judges them are the design subdomain's, and this dossier
names the register requiring action rather than amending it. **Nor is the manifest replaced here:**
construction stops writing it, and who founds a domain the compiler can discover is a ruling this
change does not make.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Reporting where each rendered value came from | build | OWNED | transformation::CT_PURE_RENDER_ARTIFACTS_V0 | S4 gap_register GAP-1 |
| Measuring a design | build | OWNED | transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | S4 gap_register GAP-2 |
| Declaring that something else governs a fact | build | OWNED | | S4 gap_register GAP-4 |
| Writing a build manifest | build | OWNED | transformation::CC_PERSIST_ARTIFACTS_V0 | S4 gap_register GAP-5 |
| Stating a vocabulary's group and spelling | design | DEFERRED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | S4 gap_register GAP-3 |
| Carrying out a construction | build | SATISFIED | transformation::WF_CONSTRUCT_ARTIFACTS_V0 | S4 capability_graph #4 |
| Admitting a design for construction | build | SATISFIED | transformation::IN_CONSTRUCTION_REQUESTED_V0 | S4 capability_graph #6 |
| Binding the construction lifecycle | build | SATISFIED | transformation::RB_CONSTRUCTION_BINDINGS_V0 | S4 dependency_graph #1 |
| Founding a domain the compiler can discover | build | DEFERRED | | S4 authoring_scope deferred #1 |
| Re-measuring every design already written | build | DEFERRED | | S4 authoring_scope deferred #2 |
| The nine families never yet emitted | build | DEFERRED | | S4 authoring_scope deferred #3 |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| The register in which a vocabulary's group and spelling are stated | build -> design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | GAP | S4 dependency_graph #2 |
| The design and mandate a construction is offered | build -> design | transformation::IN_CONSTRUCTION_REQUESTED_V0 | SATISFIED | S4 dependency_graph #2 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | Renders every family from the design, and supplies a vocabulary's group and spelling from its own text, three defaults, and one field a constitution fixes. Reports nothing about where any value came from. | EXTEND | S4 gap_register GAP-1 |
| transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | Walks the renderer's output leaf by leaf and counts a leaf determined when it is not empty. Cannot distinguish a value the design supplied from one the renderer did. | EXTEND | S4 gap_register GAP-2 |
| transformation::CC_PERSIST_ARTIFACTS_V0 | Writes what the mandate schedules, and also founds a build manifest when no file of its name exists beneath the root, taking the domain from the namespace of the first scheduled artifact. | EXTEND | S4 gap_register GAP-5 |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Names the three steps that measure, render and write. Unchanged in shape; two of its three steps change. | REVIEW | S4 capability_graph #4 |
| transformation::WF_CONSTRUCT_ARTIFACTS_V0 | Measures a design, refuses it if under-determined, and renders the artifacts it schedules. The act is right. | REVIEW | S4 capability_graph #4 |
| transformation::IN_CONSTRUCTION_REQUESTED_V0 | Offers an approved design and mandate for construction. What is offered is correct; what is done with it is not. | REUSE | S4 capability_graph #6 |
| transformation::RB_CONSTRUCTION_BINDINGS_V0 | Runtime bindings for the construction lifecycle. Unchanged. | REUSE | S4 dependency_graph #1 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Carries the rule set that judges a design. Its vocabulary register states a value and its meaning, and has no column for the group the values belong to or the spelling they must take. Named for `design` to extend; not written here. | REVIEW | S4 gap_register GAP-3 |
| vocabulary::CONSTITUTION_VOCABULARY_V0 | Governs what a vocabulary is and what it must declare. Named because the artifact refused by the platform was refused against a rule this constitution carries. | REVIEW | S2 belief_verification #2 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_FACT_HAS_A_STATED_ORIGIN | Every fact an artifact carries is stated by the design that determines it, or by something declared to govern it. A fact the design does not state is one the renderer invents, and an artifact with an author nobody approved is not a governed artifact. | S4 constraint_register #7 |
| PROVENANCE_IS_THE_TEST | The measure tests where each value came from, not whether there is one. Presence cannot distinguish a value the design supplied from one the renderer did. | S4 constraint_register #2 |
| THE_POPULATION_STAYS_DERIVED | What the measure counts remains the renderer's own output, walked leaf by leaf. A hand-maintained list is a second opinion about construction and the weaker one. | S4 constraint_register #6 |
| A_DEFAULT_IS_AN_INVENTION | A fallback the renderer supplies is a fact the design did not state. That it can be overridden is a difference in remedy, not in what happened. | S4 constraint_register #8 |
| NOTHING_OUTSIDE_THE_MANDATE | Nothing is written that the mandate did not schedule. A mandate freezes scope at a gate, and something written outside it was approved by nobody. | S4 constraint_register #3 |
| NO_FACT_FROM_A_PATH | No fact is derived from where a file or a dossier sits. A domain read from a path is a domain nobody declared, and moving a file would silently change what was built. | S4 constraint_register #4 |
| A_RENDERING_IS_ADMISSIBLE | An artifact that is rendered is admissible to the platform that will build it, or the rendering was wrong whatever the measure said about the design behind it. | S4 constraint_register #5 |
| THE_THRESHOLD_HOLDS | The measure keeps its threshold. Anything below complete means the renderer would supply the remainder. | S4 constraint_register #1 |
| A_REGISTER_IS_EXTENDED_BY_ITS_OWNER | A phase's registers and the rule set that judges them are the design subdomain's. This dossier names the register requiring action and does not amend it. | S4 dependency_graph #2 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Reporting where each rendered value came from | build | S4 gap_register GAP-1 |
| Measuring a design | build | S4 gap_register GAP-2 |
| Declaring that something else governs a fact | build | S4 gap_register GAP-4 |
| Writing a build manifest | build | S4 gap_register GAP-5 |

---

## Gate 1 — Design Approval
