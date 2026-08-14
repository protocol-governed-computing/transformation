# Stage 6 — Governance Intent: transformation / design
**Stage:** 6 — Governance Intent
**CR:** declared_reach
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `transformation` |
| Primary subdomain | `design` — EXISTING — modified by this CR |
| Authority class | reuse existing — a design declares, a rule set refuses, construction renders; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

What an act consults belongs to the phase that judges a design, which this subdomain owns. What the
built act carries belongs to construction, which is a second subdomain of the same domain and is
declared as a dependency rather than written into from here. Nothing new stands on its own, so no
subdomain is declared.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Stating the bindings an act consults | design | OWNED | | S4 gap_register GAP-1 |
| Naming a binding and deriving its records | design | OWNED | | S4 gap_register GAP-2 |
| Refusing a design whose act reads records it declared no reach to | design | OWNED | | S4 gap_register GAP-3 |
| Refusing a reach no read uses | design | OWNED | | S4 gap_register GAP-4 |
| Passing the store surface to the phase that judges a design | design | OWNED | | S4 gap_register GAP-5 |
| Emitting the reach into the built act | design | OWNED | | S4 gap_register GAP-6 |
| The published facts a rule reasons from | inspection | OWNED | inspection::TI_SI_STORE_LIST_V0 | S4 gap_register GAP-7 |
| Which acts reach which records | design | DEFERRED | | S4 authoring_scope deferred #1 |
| Whether a reach may cross a domain | design | DEFERRED | | S4 authoring_scope deferred #2 |
| Refusing a design whose act writes through a reach | design | DEFERRED | | S4 authoring_scope deferred #3 |

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
| What a design states about reach is what the built act carries | design -> build | transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | GAP | S4 dependency_graph #2 |
| The records a named binding covers, read rather than restated | design -> inspection | inspection::TI_SI_STORE_LIST_V0 | GAP | S4 dependency_graph #3 |
| Which records an act's steps address | design -> inspection | inspection::TI_SI_CAPABILITY_SURFACE_V0 | SATISFIED | S4 dependency_graph #3 |
| The reach the platform admits, which this states rather than invents | design -> runtime_binding | fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0 | SATISFIED | S4 dependency_graph #4 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Judges what a design states about where an act's records live, and has no rule reading what it consults. Generated from a declaration rather than written. | EXTEND | S4 gap_register GAP-1 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares what the domain compiles. Unchanged by this correction; named because the emitted reach is compiled under it. | REVIEW | S4 dependency_graph #2 |
| inspection::TI_SI_STORE_LIST_V0 | Answers every store at once with the count of its bindings and not their identities. The identities are published one store at a time, which a fixed pipeline cannot ask for. | EXTEND | S4 gap_register GAP-7 |
| inspection::TI_SI_CAPABILITY_SURFACE_V0 | Publishes each act's steps and each operation's effect. Already sufficient; named as the fact the new rules derive from. | REUSE | S4 capability_graph #7 |
| fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0 | States the storage resolution model the platform admits, including the reach this change lets a design declare. | REVIEW | S4 dependency_graph #4 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| OWNERSHIP_AND_REACH_ARE_SEPARATE_STATEMENTS | Ownership and reach are structurally distinct, never one register with a column telling them apart. The distinction is carried by where the statement is made, because a column is one word away from its opposite. | S4 constraint_register #1 |
| A_DESIGN_NAMES_A_BINDING_NOT_ITS_RECORDS | A design names a binding and never the records behind it. Restating them is a second copy kept by someone other than the part answerable for them. | S4 constraint_register #2 |
| A_RULE_DERIVES_WHAT_IT_CHECKS | What a rule checks is derived from the composition, never inferred from a name or an implementation. A refusal resting on either holds only until somebody renames or rewrites. | S4 constraint_register #3 |
| THE_DECLARED_SET_AND_THE_USED_SET_ARE_ONE | Every declared reach is used, and every read is declared. Either half alone permits what the other catches, so neither is a rule until both are stated. | S4 constraint_register #4 |
| A_REACH_IS_NEVER_HAND_FINISHED | A reach is never added to a built artifact by hand. It works, passes every check, and is a reach no reviewer saw. | S4 constraint_register #5 |
| A_RULE_IS_HANDED_ITS_FACTS | A rule that is not passed the facts it reasons from reports nothing and is indistinguishable from a rule that checked. The handover is part of this change rather than an assumption about it. | S4 design_decisions #4 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Stating the bindings an act consults | design | S4 gap_register GAP-1 |
| Naming a binding and deriving its records | design | S4 gap_register GAP-2 |
| Refusing a design whose act reads records it declared no reach to | design | S4 gap_register GAP-3 |
| Refusing a reach no read uses | design | S4 gap_register GAP-4 |
| Passing the store surface to the phase that judges a design | design | S4 gap_register GAP-5 |
| Emitting the reach into the built act | design | S4 gap_register GAP-6 |
| The published facts a rule reasons from | inspection | S4 gap_register GAP-7 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
