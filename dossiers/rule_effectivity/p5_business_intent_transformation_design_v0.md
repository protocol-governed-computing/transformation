# Stage 5 — Business Intent: transformation / design
**Stage:** 5 — Business Intent
**CR:** rule_effectivity
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
| A rule-set identity that changes only when the rules change | IN_SCOPE | What a document, a verdict and an approval name. | S4 authoring_scope #2 |
| Naming the rule set in a document | IN_SCOPE | Stated in the document's structured data. | S4 authoring_scope #3 |
| Naming the rule set in a verdict | IN_SCOPE | The verdict the judging already returns gains it. | S4 authoring_scope #4 |
| Naming an approval's rule set, and confirming it again | IN_SCOPE | Under a later rule set an approval stands unconfirmed until a person re-confirms it. | S4 authoring_scope #5 |
| Recording that a document was migrated | IN_SCOPE | Stated in the record, not inferred from history. | S4 authoring_scope #6 |
| Declaring a correction's effectivity | IN_SCOPE | Decides whether a correction supersedes a rule set. | S4 authoring_scope #7 |
| Proving identical verdicts across the two forms | IN_SCOPE | Findings are compared, not counts. The condition on which the old reading retires. | S4 authoring_scope #8 |
| How a value inside a register is structured | DEFERRED | Routing written as text stays text here. Giving such values a structure is the next change. | S4 authoring_scope deferred #1 |
| Where the rules are declared, and in what language | DEFERRED | That is a later change. | S4 authoring_scope deferred #2 |
| Governing and specifying construction on its own | DEFERRED | That is a later change. | S4 authoring_scope deferred #3 |
| Rule sets that differ per composition rather than per version | DEFERRED | Nothing has needed it. | S4 authoring_scope deferred #4 |
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
| A verdict names the rule set that rendered it. | A verdict that moves cannot otherwise say whether the document changed or the rules did. | S4 constraint_register #1 |
| An approval names the rule set it was given under. | An approval is a fact about one rule set. Without its name, a change of rules reopens it silently. | S4 constraint_register #2 |
| No document changes verdict because its form changed. | A change of form is not a change of meaning. A verdict that moves with the form is a regression. | S4 constraint_register #3 |
| A rule-set identity changes only when the rules change. | An identity that moves for other reasons would unconfirm approvals no rule touched. | S4 constraint_register #4 |
| An approval under a later rule set stays unconfirmed until a person re-confirms it. | Only a person may close a gate. A machine may report that the rules moved, never that the approval still holds. | S4 constraint_register #5 |
| One form of phase document exists at a time. | Two forms would need two readings, and the two could disagree about one document. | S4 constraint_register #6 |
| A correction declares its own effectivity, retroactive or not, and the rule set records the declaration as governed history. | Nobody can otherwise tell a correction that invalidates approved work from one that cannot. | S4 constraint_register #12 |
| Only a change that can alter a prior document's admissibility creates a new rule-set version. | A version that changes nothing a document is judged by would unconfirm approvals for no reason. | S4 constraint_register #13 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Judge a document against a rule set | Verdict | An author submitting a document. | IN_SCOPE | S4 events #1 |
| Approve a document | Approval | A person closing its gate. | IN_SCOPE | S4 events #2 |
| Supersede a rule set | Rule set | A retroactive correction. | IN_SCOPE | S4 events #3 |
| Record that a document was migrated | Document | An author amending a document to satisfy a later rule set. | IN_SCOPE | S4 events #4 |
| Re-confirm an approval | Approval | A person judging a document whole under a later rule set. | IN_SCOPE | S4 events #5 |
| Declare a correction's effectivity | Correction | A correction to a rule set being made. | IN_SCOPE | S4 events #6 |
| Prove identical verdicts across the two forms | Test document | Converting the test documents to the new form. | IN_SCOPE | S4 capability_graph #8 |
| Give a value inside a register a structure | Register | Deferred to the next change. | DEFERRED | S4 authoring_scope deferred #1 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| design | CT_PURE_PARSE_REGISTERS_V1 | CT | Read a phase document's registers from its structured block, apart from the prose | S4 gap_register GAP-1 |
| design | CT_PURE_PARSE_PRIOR_PHASES_V1 | CT | Read the registers of a document's prior phases from their structured blocks | S4 gap_register GAP-1 |
| design | CT_PURE_EVALUATE_RULES_V1 | CT | Apply a rule set to a parsed document and return a verdict naming that rule set | S4 gap_register GAP-4 |
| design | CC_JUDGE_DOCUMENT_V1 | CC | Judge a seed or change request and return a verdict naming its rule set | S4 gap_register GAP-4 |
| design | CC_JUDGE_AGAINST_SNAPSHOT_V2 | CC | Judge a later phase against the composition and return a verdict naming its rule set | S4 gap_register GAP-4 |
| design | CC_JUDGE_AGAINST_COMPOSITION_V2 | CC | Judge the analysis loop against the composition and return a verdict naming its rule set | S4 gap_register GAP-4 |
| design | WF_P0_SEED_ADMISSIBILITY_V1 | WF | Decide whether a seed is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | WF | Decide whether a change request is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | WF | Decide whether a domain model is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | WF | Decide whether an analysis loop is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | WF | Decide whether a business model is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | WF | Decide whether a business intent is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | WF | Decide whether a governance intent is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | WF | Decide whether a design intent is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | WF | Decide whether an authoring mandate is admissible, under a rule set with an identity | S4 gap_register GAP-2 |
| design | VOCAB_DOCUMENT_STANDING_V0 | VOCAB | The standings a phase document may hold: approved, migrated or re-confirmed | S4 gap_register GAP-6 |
| design | VOCAB_APPROVAL_STANDING_V0 | VOCAB | The standings an approval may hold under a rule set: confirmed or unconfirmed | S4 gap_register GAP-5 |
| design | VOCAB_CORRECTION_EFFECTIVITY_V0 | VOCAB | Whether a correction applies to documents approved before it: retroactive or not | S4 gap_register GAP-7 |

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
