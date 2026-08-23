# Stage 5 — Business Intent: transformation / build
**Stage:** 5 — Business Intent
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Build subdomain governs the passage from an approved design to the artifacts it determines: the
measure that decides whether a design determines them, the rendering of each artifact from what the
design states, and the writing of the result where its binding says it belongs. Its authority is to
refuse a design that does not determine what it schedules. It decides nothing about what a design
should contain.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| build | Governs the passage from an approved design to the artifacts it determines, and refuses a design that does not determine what it schedules. | S1 cr_type #1 |
| design | Governs how a proposed change is judged before anything is built: the phases, the rule set each declares, and the registers a phase admits. It owns the register a vocabulary's group and spelling belong in. | S4 gap_register GAP-3 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Reporting where each rendered value came from | IN_SCOPE | The one fact the measure needs and cannot derive; only the renderer knows it. | S4 authoring_scope #1 |
| Measuring a design | IN_SCOPE | The population stays derived from the renderer; only the test per leaf changes. | S4 authoring_scope #2 |
| Stating a vocabulary's group and spelling | IN_SCOPE | The register carrying a vocabulary's values has the rows and lacks the columns. | S4 authoring_scope #3 |
| Declaring that something else governs a fact | IN_SCOPE | Without it the change would refuse an event's moment field, which a constitution rightly fixes. | S4 authoring_scope #4 |
| Writing a build manifest | IN_SCOPE | Removed from construction; every field of it is compiler configuration. | S4 authoring_scope #5 |
| Founding a domain the compiler can discover | DEFERRED | Construction stops writing the manifest; who produces it instead is a ruling this change does not make. | S4 authoring_scope deferred #1 |
| Re-measuring every design already written | DEFERRED | Each dossier's own act, once the stricter test is in force. | S4 authoring_scope deferred #2 |
| The nine families never yet emitted | DEFERRED | Two emits are a thin basis; each family's first emission is where a further invention would surface. | S4 authoring_scope deferred #3 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| NONE IDENTIFIED |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| Every fact an artifact carries is stated by the design that determines it, or by something declared to govern it. | A fact the design does not state is one the renderer invents, and an artifact with an author nobody approved is not a governed artifact. The exception is narrow and must be declared: an event's moment field is supplied because the event constitution fixes it, and a design restating what a constitution settles would be stating it twice. | S4 constraint_register #7 |
| The measure counts what the artifact needs, and tests where each value came from. | Testing whether a value is present cannot distinguish one the design supplied from one the renderer did. Provenance is the only test that can, and only the renderer knows it. | S4 constraint_register #2 |
| The measure's population stays derived from the renderer. | A hand-maintained list is a second opinion about construction, and the weaker one — it read complete while the renderer could reproduce one artifact in twenty-five. Deriving the population is what stops it drifting, and that property is worth keeping even though it is also the blind spot. | S4 constraint_register #6 |
| A default is an invention. | A design that omits a default measures complete, which is exactly what the two literals did. That a default can be overridden and a literal cannot is a difference in remedy, not in what happened: in both cases the renderer supplied the value. | S4 constraint_register #8 |
| Nothing is written that the mandate did not schedule. | A mandate freezes scope at a gate, and something written outside it was approved by nobody. | S4 constraint_register #3 |
| No fact is derived from where a file or a dossier sits. | A domain read from a path is a domain nobody declared, and moving a file would silently change what was built. It has been invisible only because namespace and domain are the same word in a business domain. | S4 constraint_register #4 |
| A rendered artifact is admissible to the platform that will build it. | A rendering the platform refuses is a rendering that was wrong, whatever the measure said about the design behind it. | S4 constraint_register #5 |
| The measure keeps its threshold. | Anything below complete means the renderer would supply the remainder, and a partial design admitted is a design authority nobody approved. | S4 constraint_register #1 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Report where a rendered value came from | Provenance | Each leaf of each artifact being rendered. | IN_SCOPE | S4 capability_graph #1 |
| Refuse a design whose artifact carries a fact the design did not state | Design | A design being measured. | IN_SCOPE | S4 capability_graph #2 |
| State the group and spelling a vocabulary's values take | Design | A design scheduling a vocabulary. | IN_SCOPE | S4 capability_graph #3 |
| Declare that a constitution fixes a fact the design need not state | Determined fact | A renderer supplying a fact a constitution already settles. | IN_SCOPE | S4 capability_graph #4 |
| Refuse to write an artifact the mandate did not schedule | Mandate | A construction being written. | IN_SCOPE | S4 capability_graph #5 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| build | CT_PURE_ATTRIBUTE_PROVENANCE_V0 | CT | Report, for each leaf of a rendered artifact, whether the design stated it, a constitution governs it, or the renderer supplied it | S4 gap_register GAP-1 |
| build | VOCAB_FACT_PROVENANCE_V0 | VOCAB | The origins a rendered fact may have, and which of them a design may be measured complete on | S4 gap_register GAP-1 |

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|
| NONE IDENTIFIED |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | Capability graph, gaps, design decisions, authoring scope | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |
