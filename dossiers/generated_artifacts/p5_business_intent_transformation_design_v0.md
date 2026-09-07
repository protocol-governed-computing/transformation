# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** generated_artifacts
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Design subdomain governs how a proposed change is judged before anything is built. It holds the
phases a change passes through, the rule set each phase declares, and the verdict a document
receives against them. Its authority is to refuse: a document that does not say what its phase
requires does not proceed, and a phase that reaches for language belonging to a later phase is out
of bounds. It governs what may be said at each stage of a change and in what order, and it decides
nothing about what any particular change should do.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| design | Governs how a proposed change is judged before anything is built — the phases, the rule set each declares, and the verdict a document receives against them. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Stating, on an artifact, that it is generated and by what | IN_SCOPE | The fact belongs to the artifact, not to the tool that writes it. | S4 authoring_scope #1 |
| Naming, in a design, the generator an artifact is reached by | IN_SCOPE | The artifact stays the thing scheduled; the generator is the means. | S4 authoring_scope #2 |
| Reaching a generated artifact by invoking its generator | IN_SCOPE | The only arrangement with a single producer. | S4 authoring_scope #3 |
| Refusing a build when an artifact and its generator disagree | IN_SCOPE | The check exists; nothing acts on it. | S4 authoring_scope #4 |
| Delivering this change by hand, once, and recording it | IN_SCOPE | The last change requiring an exception. | S4 authoring_scope #5 |
| Generated artifacts outside this lifecycle | DEFERRED | Nothing outside it is generated yet. | S4 authoring_scope deferred #1 |
| Whether a design can state an artifact it amends | DEFERRED | A separate problem with its own change. | S4 authoring_scope deferred #2 |
| How a document authored under one rule set is judged under a later one | DEFERRED | A separate problem with its own change. | S4 authoring_scope deferred #3 |
| Judging whether generating an artifact is a good idea | DEFERRED | It is done today; this change governs it rather than judging it. | S4 authoring_scope deferred #4 |

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
| A generator is authoritative over the artifact it produces. | A disagreement is not a difference of opinion; it is proof the copy is stale, and correcting the copy leaves the generator still producing the old value. | S4 constraint_register #1 |
| An artifact and the generator that produced it agree, and the build refuses when they do not. | A stale copy reports confidently on the wrong thing, and has done: a rule added after a workflow was emitted left a smaller rule set sealed, and every run believed it. | S4 constraint_register #2 |
| One artifact has one generator. | Two producers of one truth drift, and the drift is silent until something reads the stale one. | S4 constraint_register #3 |
| A change to a generated artifact is delivered by changing its generator. | Changing the artifact instead lasts until whoever next runs the tool. | S4 constraint_register #4 |
| A generated artifact is never edited directly. | It is sealed output, with the standing the snapshot has. Editing one is the same class of error as editing the snapshot by hand. | S4 constraint_register #5 |
| Construction never becomes a second producer of an artifact a generator already produces. | The arrangement that keeps one producer authoritative is the only one where agreement is meaningful. | S4 constraint_register #6 |
| A template and the declaration it is read with are one generator. | Neither determines the artifact alone, and naming either separately would permit regenerating from a stale pairing. | S4 constraint_register #8 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Declare that an artifact is generated, and by what | Generated artifact | An artifact being produced rather than written. | IN_SCOPE | S4 capability_graph #1 |
| Name the generator an artifact is reached by | Design | A design scheduling a generated artifact. | IN_SCOPE | S4 capability_graph #2 |
| Invoke a generator to reach its artifact | Construction | Construction reaching a generated artifact. | IN_SCOPE | S4 capability_graph #3 |
| Refuse a build on disagreement | Build | An artifact and its generator disagreeing. | IN_SCOPE | S4 capability_graph #4 |
| Report whether an artifact agrees with its generator | Agreement | A build running. | IN_SCOPE | S4 capability_graph #6 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| NONE IDENTIFIED |

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
