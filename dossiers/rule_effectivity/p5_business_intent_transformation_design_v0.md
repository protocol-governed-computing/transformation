# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** rule_effectivity
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
| Declaring, on a correction, whether it is retroactive | IN_SCOPE | First in the chain; nothing else is reachable without it. | S4 authoring_scope #1 |
| Naming a state of the rule set | IN_SCOPE | A version, created only where admissibility could have changed. | S4 authoring_scope #2 |
| Pinning, on an approval, the version it was given under | IN_SCOPE | What distinguishes an approval that stands from one whose rules moved. | S4 authoring_scope #3 |
| Naming the dossiers a retroactive correction affects | IN_SCOPE | A declared output, not an emergent discovery. | S4 authoring_scope #4 |
| Carrying a dossier's state on the dossier | IN_SCOPE | Approved, migrated, re-approved. | S4 authoring_scope #5 |
| Stating, in a verdict, the version it was rendered against | IN_SCOPE | One more thing said about a judgement already described. | S4 authoring_scope #6 |
| Reporting a deliberate refusal as deliberate | IN_SCOPE | Without it the easy act stays the wrong one. | S4 authoring_scope #7 |
| Deciding whether any particular correction is retroactive | DEFERRED | Each correction decides, when it is made. | S4 authoring_scope deferred #1 |
| Rule sets that differ per composition rather than per version | DEFERRED | Nothing has needed it. | S4 authoring_scope deferred #2 |
| Anything about generated artifacts | DEFERRED | A separate problem with its own change. | S4 authoring_scope deferred #3 |
| Whether a design can state an artifact it amends | DEFERRED | A separate problem with its own change. | S4 authoring_scope deferred #4 |

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
| An approval is valid under the rules it was given, and states which those were. | If an approval is only ever a statement about today's rules then no gate was ever closed — it was provisionally closed pending every future rule, and "approved" means "not yet invalidated". | S4 constraint_register #1 |
| A rule-set version exists only where admissibility could have changed. | A version that cannot invalidate anything makes the version meaningless as a signal, and a document would fall behind for corrections that could never have affected it. | S4 constraint_register #2 |
| Every correction declares its effectivity. | A correction that cannot say whom it affects leaves every prior approval in doubt, and two corrections that touch the same files can differ entirely in effect. | S4 constraint_register #3 |
| A migrated dossier is never presented as an approved one. | It passes now and was taught to. A dossier that always said this and one taught to say it afterwards are different claims, and the second is weaker. | S4 constraint_register #4 |
| A closed dossier is never amended to satisfy rules written after its approval. | Amending it changes the evidence of an approval that already happened, so the dossier on disk is no longer the one anyone gated. | S4 constraint_register #5 |
| A non-retroactive correction disturbs no dossier and creates no version. | Its declaration is what makes that claim checkable rather than assumed. | S4 constraint_register #6 |
| Naming the dossiers a retroactive change affects is part of that change. | Discovered later, they are discovered by failing, unannounced and all at once. | S4 constraint_register #7 |
| A completed change may be left at the version it was approved under. | A completed change is not obliged to answer rules written after it closed, for the same reason its baseline is never re-pinned forward. | S4 constraint_register #8 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Declare a correction's effectivity | Effectivity | A correction being made. | IN_SCOPE | S4 capability_graph #1 |
| Create a rule-set version | Rule-set version | A retroactive correction being declared. | IN_SCOPE | S4 capability_graph #2 |
| Pin the version an approval was given under | Approval | A gate being closed. | IN_SCOPE | S4 capability_graph #3 |
| Name the dossiers a correction affects | Affected dossiers | A retroactive correction being declared. | IN_SCOPE | S4 capability_graph #4 |
| Record a dossier's state | Dossier | A dossier being approved, migrated or re-approved. | IN_SCOPE | S4 capability_graph #5 |
| State the version a verdict was rendered against | Verdict | A document being judged. | IN_SCOPE | S4 capability_graph #6 |
| Report a refusal as deliberate | Verdict | A dossier failing because its rules moved rather than because it is wrong. | IN_SCOPE | S4 capability_graph #7 |

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
