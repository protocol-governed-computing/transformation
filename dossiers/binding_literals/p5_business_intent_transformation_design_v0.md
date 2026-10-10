# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** binding_literals
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Design subdomain judges each document of the transformation lifecycle against the rule set its
phase declares. A document is admissible when it satisfies every rule its phase declares. The
Design Intent phase holds every statement of where a step's input comes from to a form the runtime
resolves. The subdomain governs what a document must say at each phase, and the verdict it receives.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

---

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| design | Judges each document of the transformation lifecycle against the rule set its phase declares, and governs what a document must say at each phase and the verdict it receives. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Giving a literal one meaning across every rule that judges a binding | IN_SCOPE | The narrower rules are widened to the definition the rooting rule applies. | S4 authoring_scope #1 |
| Stating that a generator determines a value | IN_SCOPE | A reserved source, admitted only for an owner listed as generated. | S4 authoring_scope #2 |
| The rule-effectivity change | DEFERRED | It is parked and resumes against the composition this change produces. | S4 authoring_scope deferred #1 |

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
| A literal has one meaning across every rule that judges a binding. | Two rules that read one statement differently leave the author no statement either accepts. | S4 constraint_register #1 |
| A generator determines only what the design says it does. | A value nobody declared generated is a value nobody can account for. | S4 constraint_register #2 |
| No admissible design becomes inadmissible. | A correction that refuses approved work is a retroactive change, and this one is not. | S4 constraint_register #3 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Judge a binding | Binding | A design intent being checked. | IN_SCOPE | S4 events #1 |
| Declare a value generated | Generated value | An author stating that the generator determines an input. | IN_SCOPE | S4 events #2 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| design | WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | WF | Decide whether a design intent is admissible, reading a literal one way and admitting a value its generator determines | S4 gap_register GAP-1 |

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
