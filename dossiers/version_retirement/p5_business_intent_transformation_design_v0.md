# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** version_retirement
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Design subdomain judges each document of the transformation lifecycle against the rule set its
phase declares, through phase workflows and the contracts they run. Those workflows and contracts
change as the lifecycle changes, and each replaced version is stood down. The subdomain governs what
a document must say at each phase, the verdict it receives, and the artifacts that render it.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

---

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| design | Judges each document of the transformation lifecycle against the rule set its phase declares, and governs what a document must say at each phase, the verdict it receives, and the artifacts that render it. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Declaring when a replaced version is retained | IN_SCOPE | One declaration every check reads. | S4 authoring_scope #1 |
| Recording a deletion | IN_SCOPE | One ledger, carrying what the standard requires. | S4 authoring_scope #2 |
| Accepting a recorded deletion in every check that assumed retention | IN_SCOPE | The published-identity and supersession checks read the ledger. | S4 authoring_scope #3 |
| Refusing a deleted name used again | IN_SCOPE | Reuse and dangling references are refused by one check. | S4 authoring_scope #4 |
| Deleting this domain's stood-down versions | IN_SCOPE | Eleven deletions, each recorded. | S4 authoring_scope #5 |
| What retention conditions apply after development | DEFERRED | That is decided when a stable baseline is declared. | S4 authoring_scope deferred #1 |
| Declaring the first stable baseline | DEFERRED | That is a later change. | S4 authoring_scope deferred #2 |
| Deleting other domains' stood-down versions | DEFERRED | Each domain deletes its own, in its own change. | S4 authoring_scope deferred #3 |
| The form a phase document carries its facts in | DEFERRED | That is the format change, which waits for this one. | S4 authoring_scope deferred #4 |

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
| A replaced version leaves the live tree only by a recorded deletion. | A removal nobody recorded cannot be told from a loss. | S4 constraint_register #1 |
| A deleted name is never used again. | A release is cited by the identities it holds, and a reused name would change what a citation means. | S4 constraint_register #2 |
| A change of meaning is a new identity. | Deletion ends a version; it never lets a meaning change under an old name. | S4 constraint_register #3 |
| When retention applies is declared once, and every check reads that declaration. | Two places deciding retention could disagree about one version. | S4 constraint_register #4 |
| The standard does not change. It already bounds retention and defines deletion. This change realizes it. | The standard already says what a deletion must record. | S4 constraint_register #5 |
| Identity and succession stay mandatory. A replaced version still names its successor before it goes. | Deletion follows succession; it does not replace it. | S4 constraint_register #6 |
| Releases are untouched. A sealed release keeps every identity it holds, at its tag. | A consumer of a release uses the release, not the live tree. | S4 constraint_register #7 |
| When a stable baseline is declared, retention conditions begin to bind, by changing the declaration rather than the code. | Ending development must not need a change to any check. | S4 constraint_register #8 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Delete a replaced version | Replaced version | A person determining that no retention condition holds. | IN_SCOPE | S4 events #2 |
| Record a deletion | Deletion record | A replaced version being deleted. | IN_SCOPE | S4 events #2 |
| Replace a version | Replaced version | A change of meaning authoring a successor. | IN_SCOPE | S4 events #1 |
| Declare a stable baseline | Retention declaration | Deferred to a later change. | DEFERRED | S4 authoring_scope deferred #2 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|---------------------------------------------------------------|---------|----------------|
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
