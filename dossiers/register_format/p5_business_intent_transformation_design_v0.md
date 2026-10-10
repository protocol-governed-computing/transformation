# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** register_format
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Design subdomain judges each document of the transformation lifecycle against the rule set its
phase declares. A document is admissible when it satisfies every rule its phase declares. A phase
document holds two kinds of content: prose that explains the change to a person, and registers
that state the facts the rules judge. The subdomain governs what a document must say at each phase,
and the verdict it receives.

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
| Carrying registers as structured data apart from the prose | IN_SCOPE | The reading exists; what it reads changes. | S4 authoring_scope #1 |
| A block for structured facts in every document that carries registers | IN_SCOPE | The templates and the projection write it. | S4 authoring_scope #2 |
| Converting a document from the old form to the new | IN_SCOPE | Mechanical, once, and gone with the old reading. | S4 authoring_scope #3 |
| Keeping the construction tests' coverage | IN_SCOPE | A test copy is a design and a mandate. | S4 authoring_scope #4 |
| How a value inside a register is structured | DEFERRED | Routing written as text stays text here. Giving such values a structure is the next change. | S4 authoring_scope deferred #1 |
| Where the rules are declared, and in what language | DEFERRED | That is a later change. | S4 authoring_scope deferred #2 |
| Which rule set judged a document | DEFERRED | A document, a verdict and an approval naming their rule set is a later change, made once the rules are declared outside the code. | S4 authoring_scope deferred #3 |
| Governing and specifying construction on its own | DEFERRED | That is a later change. | S4 authoring_scope deferred #4 |
| Converting or reading dossiers approved under v5 | DEFERRED | They stay as published, and v6 does not read them. | S4 authoring_scope deferred #5 |

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
| No document changes verdict because its form changed. | A change of form is not a change of meaning. A verdict that moves with the form is a regression. | S4 constraint_register #1 |
| One form of phase document exists at a time. | Two forms would need two readings, and the two could disagree about one document. | S4 constraint_register #2 |
| No compatibility with v5. Dossiers approved under v5 stay as published, and this change neither converts nor reads them. | An archived release keeps working at its tag; this change owes it nothing. | S4 constraint_register #3 |
| The old reading retires once this change shows that the old and new forms receive the same verdicts. | The old reading is kept only as long as it is needed to show the forms agree. | S4 constraint_register #4 |
| The delivered dossiers the construction tests reproduce artifacts from are copied and converted as test fixtures before the old reading retires. | The construction tests would otherwise lose most of what they reproduce. | S4 constraint_register #5 |
| One form for every document that carries registers, from the seed to the mandate. | A phase that read one form and a later phase another would need both readings. | S4 constraint_register #6 |
| The business problem statement has no registers and stays prose. | Prose a person wrote is not a register, and has nothing a machine reads exactly. | S4 constraint_register #7 |
| The new form replaces the old form. The two never coexist. | Two forms side by side would be read two ways. | S4 constraint_register #8 |
| What this change replaces is deleted, not stood down. The readers of the old form are removed from the composition with their implementation. | A version nothing can run is not carried. | S4 constraint_register #9 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Judge a document against a rule set | Verdict | An author submitting a document. | IN_SCOPE | S4 events #1 |
| Convert a document to the new form | Document | A test document or a test copy being moved to the new form. | IN_SCOPE | S4 events #2 |
| Retire the old reading | Old reading | Every converted document receiving the same verdict and findings in both forms. | IN_SCOPE | S4 events #3 |
| Give a value inside a register a structure | Register | Deferred to the next change. | DEFERRED | S4 authoring_scope deferred #1 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|---------------------------------------------------------------|---------|----------------|
| design | CT_PURE_PARSE_REGISTERS_V1 | CT | Read a phase document's header and registers from its structured block, and its sections from its prose | S4 gap_register GAP-1 |
| design | CT_PURE_PARSE_PRIOR_PHASES_V1 | CT | Read the upstream phase documents a phase is judged against, each from its structured block | S4 gap_register GAP-1 |

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
