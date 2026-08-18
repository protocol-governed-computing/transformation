# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** refusal_discharge
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
| Stating what discharges a declared refusal | IN_SCOPE | The register the whole change turns on; every rule stands on it. | S4 authoring_scope #1 |
| Refusing a design that leaves a declared refusal unaccounted for | IN_SCOPE | The closure itself. Without it the register is optional documentation. | S4 authoring_scope #2 |
| Stating that a refusal is deferred, and to whom | IN_SCOPE | Without it a change inheriting a refusal must carry it or stay silent, and silence is what this change removes. | S4 authoring_scope #3 |
| Holding a discharge to the act and step it names | IN_SCOPE | A register read only for presence documents intent and enforces nothing. | S4 authoring_scope #4 |
| Holding a discharge's outcome to an ending that refuses | IN_SCOPE | A step whose failing outcome routes onward does not refuse, however plainly the register says so. | S4 authoring_scope #5 |
| Refusing a discharge or deferral naming a refusal the business never declared | IN_SCOPE | The other half of coverage; alone, the first half admits refusals nobody approved. | S4 authoring_scope #6 |
| Giving the design intent phase the seed | IN_SCOPE | The phase cannot refuse what it cannot see. | S4 authoring_scope #7 |
| Reading a prior's rows across several registers | IN_SCOPE | Coverage spans two registers and the kind that asks it reads one. | S4 authoring_scope #8 |
| Which operations a business refuses, and when | DEFERRED | Each business states its own, in its own change. | S1 out_of_scope #1 |
| How an act performs a refusal | DEFERRED | The design decides that; this change asks only which step does and on what outcome. | S1 out_of_scope #2 |
| Whether the built act refuses when it runs | DEFERRED | The platform decides that, and proving it is a matter of exercising the act. | S1 out_of_scope #4 |

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
| A discharge is stated in a register, never inferred from a citation. | A citation is written where an author found it natural and left out where they did not, so a check built on one calls correct work red and is satisfied by anyone typing the right string. What the business is owed is a statement it can read, not a convention it has to trust. | S4 constraint_register #1 |
| A discharge names the act, the step and the outcome. | Naming the act alone would be answered by any act that refuses anything at all, and naming the step without the outcome would be answered by a step that reports its judgement and carries on. The three together are the smallest statement that means the operation actually stops. | S4 constraint_register #2 |
| A stated discharge is checked against the design's own topology. | A register read only for presence records what somebody intended and enforces nothing, which is the failure this change exists to end rather than to repeat one level up. Everything the check needs is already in the design, so taking the statement on trust would be a choice rather than a limitation. | S4 constraint_register #3 |
| No discharge or deferral names a refusal the business did not declare. | A design accounting for a refusal nobody approved is either inventing business rules or carrying a row left behind by a rewording, and both are things a reviewer should be shown rather than left to notice. | S4 constraint_register #4 |
| A deferral names its owner. | A refusal deferred to nobody is a refusal abandoned with a form filled in. Naming the owner is what makes a deferral an answer instead of a way of passing the check. | S4 constraint_register #5 |
| A design that declares no refusals is judged exactly as it is today. | Most changes declare none, and a closure that makes every existing dossier red for a defect none of them has would be abandoned within a week rather than obeyed. | S4 constraint_register #6 |
| The judging artifacts are re-emitted by their generator, never written by hand. | A rule set written by hand beside its declaration is the drift the generator exists to remove, and this change adds rules to exactly that artifact. | S4 constraint_register #7 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| State what discharges a declared refusal | Discharge | A design being written for a change whose business declared a refusal. | IN_SCOPE | S4 capability_graph #1 |
| Refuse a design that leaves a declared refusal unaccounted for | Refusal | A design being judged. | IN_SCOPE | S4 capability_graph #2 |
| State that a refusal is deferred, and to whom | Deferral | A design being written for a refusal it does not own. | IN_SCOPE | S4 capability_graph #3 |
| Hold a discharge to the act and step it names | Discharge | A design being judged. | IN_SCOPE | S4 capability_graph #4 |
| Hold a discharge's outcome to an ending that refuses | Ending | A design being judged. | IN_SCOPE | S4 capability_graph #5 |
| Refuse a discharge or deferral naming a refusal the business never declared | Refusal | A design being judged. | IN_SCOPE | S4 capability_graph #6 |
| Give the design intent phase the seed | Refusal | A design being judged. | IN_SCOPE | S4 capability_graph #7 |
| Read a prior's rows across several registers | Discharge | A design being judged for coverage. | IN_SCOPE | S4 capability_graph #8 |

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
