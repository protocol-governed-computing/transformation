# Business Intent: [domain] / [subdomain]
**Domain:** [domain]  
**Subdomain:** [subdomain]  
**Version:** V0  
**Status:** DRAFT  
**Pipeline Stage:** Stage 5 — Business Intent (WHAT)  
**Produced by:** v0.5.0 SDLC authoring pipeline  

---

## Document Contract

**This artifact is a structured register document — not a narrative.** The Business Intent captures
the irreducible WHAT — purpose, scope, invariants, actions, and provisional artifact codes. Purpose
(§1) is short prose (the one irreducible business narrative a compiler can never derive); everything
else — including Identity Semantics (§4) — is registers. The worker emits register ROWS; a
deterministic renderer owns the document. A required cell with no basis in the seed or the snapshot
is not a cell this phase can write: it is a question that belonged to P0 or P1 and was carried past
its gate. Send it back to be asked and answered — never fabricated, never left blank, and never
hedged with `UNRESOLVED`. A hole declared here is invisible to every phase downstream, which reads
the cell as decided.

VALID OUTPUT:
- The Purpose prose section (§1) filled for this subdomain
- Populated register tables (every required register below), every cell stating a decided value
- Business-language descriptions in content columns

INVALID OUTPUT:
- Narrative essays replacing the registers
- Implementation bindings, JSONPath, op codes, module paths, or content hashes (those are Stage 7)

A required register with no rows renders as `| NONE IDENTIFIED |`.

---

### Provisional codes

This is the first stage that assigns **provisional** artifact codes (`provisional_codes`). They are
provisional — Stage 7 assigns the binding domain-qualified FQDNs. Each carries a `_V0` suffix.
Workflow nodes are IN / CC / EXIT only; a sub-workflow call is a gateway CC, never a nested WF. EV
artifacts record facts, never trigger execution.

---

## Stage Inputs — Questions for the Human

| # | Question for the Human | How the Agent Uses the Answer (Intent) |
|---|------------------------|----------------------------------------|
| 1 | In one paragraph: what does this subdomain govern, and why does it exist? | Becomes §1 Purpose — the scope of authority everything hangs from. |
| 2 | For each business record: does history matter, can values be corrected, is deletion allowed? | Selects the Record Model in `business_objects`. |
| 3 | Which field uniquely identifies each record, where does it come from, what does a duplicate mean? | Becomes the `identity_semantics` register (§4). |
| 4 | What is always forbidden or always required, and what is the business reason? | Becomes `invariants`. |
| 5 | What verbs can be performed on these records, and who/what triggers each? | Becomes `actions` — each in-scope action yields one Intent and one Workflow. |

---

### Citing a prior row

Every row carries a `Source Finding` naming where its content came from. A citation resolves when it
names one of:

- **a register this phase may cite**, by id and ordinal — `known_facts #14`;
- **the same, by section**, prefixed with the phase that declared it — `S1 §4 Known Facts #14`;
- **a literal source** — `CR seed`, `human decision`, `projection`, `S1 seed`;
- **an artifact already in the baseline**, by exact identity — `blockchain::WF_REGISTER_ACTOR_V0`.

Separate several citations with `;`. One resolvable citation grounds the row.

**A carried claim is carried verbatim.** Where a register restates a row an earlier phase declared —
a belief, an authoring decision, a capability — the text must match that row exactly. Tightening a
sentence while citing the row it came from is how a claim drifts from what was decided, so the rules
treat a tidier synonym as a new claim and refuse it. Cite it as it stands, or change it in the phase
that owns it.

---

## 1. Subdomain Purpose

*One short paragraph: what this subdomain governs, what authority it establishes, what lifecycle it
manages, and the business rationale for its existence. Write for a business stakeholder. No artifact
names.*

*This paragraph is not written here for the first time. The business author stated it at P0, as the
one irreducible narrative no compiled artifact can derive, and P1 through P4 have no register to
carry it in. This phase therefore says which it is doing: **INHERITED**, and the paragraph is the
seed's, word for word; or **REFINED**, and the Refinement column states what this phase adds that
the seed did not say. Human semantic content enters the dossier once. A later phase may preserve it
or supersede it in the open — never quietly replace it.*

<!-- register:subdomain_purpose business_language -->

[Purpose paragraph for [domain]/[subdomain].]

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|

---

### Purpose of every subdomain this change touches

*The paragraph above is this document's own subdomain. A change may touch more than one — its
classifications say which — and a subdomain changed with nothing said about what it governs is
changed blindly. One row per subdomain the change touches, including this document's own.*

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|

---

## 2. Scope Boundary

*What V0 commits to vs. what is explicitly deferred. A vague scope boundary is a governance defect. Status ∈ IN_SCOPE | DEFERRED.*

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|

---

## 3. Business Objects

*The business records this subdomain maintains and WHY each takes its form. Record Model ∈ MUTABLE_STATE (current state, correctable) | APPEND_ONLY_JOURNAL (immutable history) | IDENTITY_REGISTRY (stable key→address) | HYBRID. Business language.*

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|

---

## 4. Identity Semantics

*Which field uniquely identifies each record, where it comes from, what a duplicate means, and any
cross-subdomain identity relationship. The compiler cannot infer identity semantics from field
names — this is irreducible business knowledge. A cell not derivable from the seed is a question the
seed's Clarification Requests should have asked and its author answered; return to that gate rather
than guessing it here or hedging it as a hole.*

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|

---

## 5. Business Invariants

*Non-negotiable rules with a business reason. A rule without a business reason is a technical constraint and belongs elsewhere.*

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|

---

## 6. Business Actions

*Every verb performable on this subdomain's objects, in plain business language. Each in-scope action maps to one Intent and one Workflow. Status ∈ IN_SCOPE | DEFERRED.*

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|

---

## 7. Provisional Artifact Codes

*Provisional codes for every artifact this change authors — Stage 7 assigns the binding FQDNs. Each
carries `_V0`. `summary` is business language.*

*The family vocabulary spans every kind a business change request authors, not only the four a
reader meets first. A transform that forms a business key, the moment a record enters the catalog,
the stores a subdomain owns and the bindings that reach them are all things the business asked for,
and a family that could not name them left them outside the P5→P7 closure entirely: an artifact
scheduled at Stage 7 with no provisional code is one no business intent ever named, and
`AUTHORED_ARTIFACT_WITHOUT_INTENT` is what now refuses it. `CS` is absent deliberately — a capability
side effect is substrate, and a business change request reuses one rather than authoring it.*

<!-- register:provisional_codes optional business_language=summary -->
| Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|------------------|-------------------------|---------|----------------|

---

## 8. Cross-Subdomain References

*Capability Contracts defined in another subdomain and referenced by this subdomain's workflows. `cc_code` is the existing FQDN; do not re-document it here.*

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | business_model_[subdomain]_v0.md | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |

---

## gov_projection — Governed Handoff to Stage 6

*The bounded inputs and emit keys mirror the engine's gov_projection schema exactly
(`contracts/gov_projection.py`): S5 consumes the S4 discovery output plus the S1 release boundary
and emits the WHAT. Emit keys match the register ids above exactly (Purpose §1 / Identity Semantics
§4 / Business Objects §3 are this stage's record, not forwarded fields).*

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | out_of_scope |
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · constraint_register |
| **Emits** → Stage 6 | scope_boundary · invariants · actions · provisional_codes · cross_subdomain_refs |
