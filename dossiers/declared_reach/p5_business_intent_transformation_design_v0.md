# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** declared_reach
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
| Stating the bindings an act consults | IN_SCOPE | The only gap that is not a rule; everything else stands on it. | S4 authoring_scope #1 |
| Naming a binding and deriving its records | IN_SCOPE | What keeps this change from re-creating the copy it serves. | S4 authoring_scope #2 |
| Refusing a design whose act reads records it declared no reach to | IN_SCOPE | Half of one statement; permits a reserve if delivered alone. | S4 authoring_scope #3 |
| Refusing a reach no read uses | IN_SCOPE | The other half; permits a silent reach if delivered alone. | S4 authoring_scope #4 |
| Passing the store surface to the phase that judges a design | IN_SCOPE | Without it every rule above reports nothing and looks like a rule that checked. | S4 authoring_scope #5 |
| Emitting the reach into the built act | IN_SCOPE | Or the declaration is decoration and the act is hand-finished. | S4 authoring_scope #6 |
| The published facts a rule reasons from | IN_SCOPE | Declared already, and published in a shape no rule can consume. | S4 authoring_scope #7 |
| Which acts reach which records | DEFERRED | Each domain's business, stated in its own change. | S4 authoring_scope deferred #1 |
| Whether a reach may cross a domain | DEFERRED | Settled by the platform: it may not. | S4 authoring_scope deferred #2 |
| Refusing a design whose act writes through a reach | DEFERRED | The platform refuses it when the act runs; whether the design layer should refuse it earlier is its own question. | S4 authoring_scope deferred #3 |

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
| Ownership and reach are structurally distinct, never one register with a column telling them apart. | Records an act may only read and records it answers for would then sit one word apart, with nothing between them but whoever remembers to read the column. The distinction is the whole point of declaring a reach, so it is carried by where the statement is made rather than by what it says. | S4 constraint_register #1 |
| A design names a binding and never the records behind it. | Records restated inside the reaching act's design are a second copy, kept by someone other than the part of the business answerable for them, and the two disagree the first time the owner changes anything. That is the arrangement this change exists beside, not one it may re-create one level up. | S4 constraint_register #2 |
| What a rule checks is derived from the composition, never inferred from a name or an implementation. | A refusal that rests on what something is called holds only while everyone names things the same way, and one that rests on how something behaves stops holding the day the behaviour is rewritten. Neither is a rule anybody can rely on having been applied. | S4 constraint_register #3 |
| Every declared reach is used, and every read is declared. | Each half alone permits exactly what the other catches: a reach nobody uses is a permission granted for a purpose no reviewer ever saw stated, and a read nobody declared is the invisible reach this change exists to end. Delivered together they say the same thing twice from opposite sides, which is what makes either checkable. | S4 constraint_register #4 |
| A reach is never added to a built artifact by hand. | The declaration is for the reviewer, and a reach that never appeared in a design was never reviewed however correct it is. Allowing it once makes every other declaration advisory. | S4 constraint_register #5 |
| A reach added by hand works, passes every check, and is a reach no reviewer saw. | Nothing distinguishes a reach that was designed from one that was inserted afterwards, so passing is not evidence of review — which is why the prohibition cannot be enforced by checking the built act and has to be enforced by what the design states. | S4 constraint_register #6 |
| A rule resting on a name is a convention anybody can break by naming something well. | A convention holds while everyone follows it and refuses nobody who does not, so a check built on one reports that a discipline was satisfied every time it was not. | S4 constraint_register #7 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| State the bindings an act consults | Reach | A design being written for an act that reads records another part of the business owns. | IN_SCOPE | S4 capability_graph #1 |
| Derive the records a named binding covers | Binding | A design naming a binding its act consults. | IN_SCOPE | S4 capability_graph #2 |
| Refuse a design whose act reads records it declared no reach to | Reach | A design being judged. | IN_SCOPE | S4 capability_graph #3 |
| Refuse a reach no read uses | Reach | A design being judged. | IN_SCOPE | S4 capability_graph #4 |
| Hand the store surface to the phase that judges a design | Derivation | A design being judged. | IN_SCOPE | S4 capability_graph #5 |
| Emit the reach into the built act | Reach | Construction rendering a design that declared one. | IN_SCOPE | S4 capability_graph #6 |
| Name a store's bindings where every store is answered at once | Derivation | A design being judged. | IN_SCOPE | S4 capability_graph #7 |

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
