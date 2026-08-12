# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** rule_expressiveness
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

---


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
| Stating which subdomain a classification applies to | IN_SCOPE | A column on the classification, not a register of its own. | S4 authoring_scope #1 |
| Deriving the span of a change from its classifications | IN_SCOPE | Derived, never declared a second time. | S4 authoring_scope #2 |
| Requiring a purpose for every subdomain a change touches | IN_SCOPE | Possible only once the span is stated. | S4 authoring_scope #3 |
| Requiring an owner for every subdomain a change touches | IN_SCOPE | The same. | S4 authoring_scope #4 |
| Recording a dependency that exists and is altered | IN_SCOPE | A fifth way of disposing of a dependency. | S4 authoring_scope #5 |
| Counting a register's rows | IN_SCOPE | A new way of judging. Applied to no register. | S4 authoring_scope #6 |
| Changes that span two domains rather than two subdomains | DEFERRED | A span that has never occurred cannot be specified honestly. | S4 authoring_scope deferred #1 |
| Applying a row count to any particular register | DEFERRED | Each is its own judgement about what that register means. | S4 authoring_scope deferred #2 |
| Anything in the construction half of the lifecycle | DEFERRED | Only the phases that judge a design are touched. | S4 authoring_scope deferred #3 |

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
| A rule can only be written if some way of judging can express it. | A rule nobody can write is a rule nothing enforces, and the gap is invisible because there is nothing to look at. | S4 constraint_register #1 |
| Every subdomain a change touches has its purpose stated and its owner declared. | A subdomain changed with nothing said about what it governs is changed blindly, and one with no owner is answerable to nobody. | S4 constraint_register #2 |
| The span of a change is derived from what its classifications say, and stated nowhere else. | Two statements of one thing can disagree, and nothing would reconcile them. | S4 constraint_register #3 |
| A phase judges documents only against rules it declares. | A phase judging by anything else is judging by something nobody can read. | S4 constraint_register #4 |
| No existing verdict changes except where one of the three gaps caused it. | A correction that moves an unrelated verdict has changed something nobody asked to change. | S4 constraint_register #5 |
| A change may carry more than one classification. | A change that creates one subdomain and modifies another is two kinds of change, honestly stated. | S4 constraint_register #8 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Judge a document against a phase | Phase | An author submitting a document. | IN_SCOPE | S4 events #1 |
| State which subdomain a classification applies to | Classification | An author classifying a change. | IN_SCOPE | S4 capability_graph #1 |
| Derive the span of a change | Span | A phase needing to know what the change touches. | IN_SCOPE | S4 capability_graph #2 |
| Record a dependency that exists and is altered | Register | An author disposing of a dependency. | IN_SCOPE | S4 capability_graph #5 |
| Constrain how many rows a register has | Rule | A rule being written against a register. | IN_SCOPE | S4 capability_graph #6 |
| Apply a row count to a particular register | Register | Deferred. | DEFERRED | S4 authoring_scope deferred #2 |

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
