# Domain Model — transformation / phases

**Stage:** 2 — Domain Model Verification
**CR:** new_subdomain
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

> P2 verifies the semantic model inherited from P1 against the compiled snapshot. It discovers
> facts; it does not decide. Every belief P1 recorded gets a result, and `NOT_FOUND` is a final
> answer — absence is a finding, not a reason to keep searching.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Seed | The business problem statement reorganized into fixed registers. | Held as a document outside the composition; never stored as protocol state. | NOT_FOUND | S1 business_vocabulary Seed |
| Rule Set | The declared conditions deciding whether a document is admissible. | Carried as declared input on the phase workflow, sealed with it. | NOT_FOUND | S1 business_vocabulary Rule Set |
| Verdict | The outcome of applying a rule set: admissible or inadmissible. | Returned by the phase; not persisted. | NOT_FOUND | S1 business_vocabulary Verdict |
| Finding | One recorded failure of one rule. | Returned within the verdict; not persisted. | NOT_FOUND | S1 business_vocabulary Finding |
| Author of Record | The person accountable for a document's content. | An actor identity bound by the phase workflow. | VERIFIED | S1 business_vocabulary Author of Record |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Verdict | admissibility | Whether the document may proceed to the next phase. | NOT_FOUND | S1 business_invariants #1 |
| Verdict | rules evaluated | How many rules were applied — every rule, always. | NOT_FOUND | S1 business_invariants #2 |
| Finding | rule | The rule that produced the finding. | NOT_FOUND | S1 business_invariants #4 |
| Rule Set | active version | The declared rules currently deciding admissibility. | NOT_FOUND | S1 lifecycle_states Rule Set |
| Rule Set | sealed copy | The rules as carried in the phase's own compiled artifact, generated from the declaration rather than typed. | OBSERVED | S1 known_facts #14 |
| Seed | carried form | The whole document, travelling with the request as text rather than as a location to be read. | NOT_FOUND | S1 known_facts #16 |
| Verdict | reproducibility | A verdict is reproducible from what was judged, which is why nothing is read from a location at judging time. | NOT_FOUND | S1 known_facts #17 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Judge a document | The author of record offering it | A verdict, with every failed rule reported, over the document text it was handed | NOT_FOUND | S1 requested_outcomes #2 |
| Accept at a gate | The gate reviewer | The document may be consumed by the next phase | NOT_FOUND | S1 business_events Seed Accepted |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Judge a document | 1 | Read the document into its registers | The registers | NOT_FOUND | S1 requested_outcomes #2 |
| Judge a document | 2 | Apply every declared rule | The findings | NOT_FOUND | S1 business_invariants #2 |
| Judge a document | 3 | Reach a verdict | The verdict | NOT_FOUND | S1 business_invariants #1 |

## 3. Belief Verification

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------|----------|----------------|
| No capability in the current composition decides seed admissibility. | NOT_FOUND | No capability produces an admissibility verdict; the only governed call in the domain is transformation::CC_JUDGE_DOCUMENT_V0, authored by this CR. | S1 system_beliefs #1 |
| A capability for declaring pure, deterministic transforms already exists. | VERIFIED | capability_transforms::CT_PURE_COMPARE_EQUAL_V0, capability_transforms::CT_PURE_EXTRACT_V0 | S1 system_beliefs #2 |
| A capability for declaring governed calls already exists, and forbids orchestration logic inside them. | VERIFIED | transformation::CC_JUDGE_DOCUMENT_V0 composes steps in a pipeline; chaining inside a call is forbidden and enforced at compile time. | S1 system_beliefs #3 |
| A workflow form already exists that composes governed calls as a fixed graph without iteration. | VERIFIED | transformation::WF_P0_SEED_ADMISSIBILITY_V0, transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | S1 system_beliefs #4 |
| An actor form already exists for recording accountability. | VERIFIED | transformation::AC_SEED_AUTHOR_V0, transformation::AC_GATE_REVIEWER_V0, transformation::AC_REGISTER_AUTHOR_V0 | S1 system_beliefs #5 |
| A form for declaring rules as data, separate from the mechanism that enforces them, already exists. | NOT_FOUND | No declaration form carries rules applied to a document; the rule set travels as declared workflow input instead. | S1 system_beliefs #6 |
| Vocabulary extension is restricted to specific declared categories. | VERIFIED | Vocabulary extension contributes only to the categories a reserving declaration marks extensible; no other category admits domain entries. | S1 system_beliefs #7 |
| The platform's existing content is largely infrastructure rather than business capability. | VERIFIED | The composition is dominated by constitutions, invariants and transport contracts; capability_side_effects::CS_MUTABLE_JSON_V0 and capability_transforms::CT_PURE_EXTRACT_V0 are among the few reusable mechanisms. | S1 system_beliefs #8 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|------------|------|--------------|-----|-----------|
| Snapshot observation | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | Reads an assembled snapshot through the governed inspection surface. | EXACT | Nothing — it is read-only by construction. |
| Mutable JSON store | capability_side_effects::CS_MUTABLE_JSON_V0 | Key-addressable JSON state with last-write-wins. | MISMATCH | The phases persist nothing; no store is needed. |
| Judge a document | transformation::CC_JUDGE_DOCUMENT_V0 | Parses a document and evaluates a declared rule set against it. | PARTIAL | It observes nothing, so it cannot ground a claim about the composition. |
| Author of record | transformation::AC_REGISTER_AUTHOR_V0 | The human accountable for a register's content. | EXACT | Nothing. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| No governed call grounds a claim against the composition. | CRITICAL | A phase that verifies beliefs cannot be built from what exists; judging alone is not grounding. | NOT_FOUND | S2 belief_verification A capability for declaring governed calls |
| No declaration form carries rules applied to a document. | MEDIUM | The rule set travels as declared workflow input, which is sound but is not a reusable form. | NOT_FOUND | S1 system_beliefs #6 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language=observation -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Judging and grounding are separable concerns: one reads a document, the other reads the composition. | transformation::CC_JUDGE_DOCUMENT_V0 performs the first and binds nothing. | VERIFIED | S2 gaps No governed call grounds a claim |
| Observation is a side effect, not a transform: the same query answers differently against different compositions. | capability_side_effects::CS_SNAPSHOT_QUERY_V0 is declared read-only with a bound subject. | VERIFIED | S1 constraints A verdict must be reproducible |
| A rule set held in the artifact that applies it can be compared against its declaration, so the two cannot drift unnoticed. | The seed settles that the sealed copy is generated rather than typed and that the two are compared on every run; nothing in the composition holds a rule set apart from the workflow that applies it. | OBSERVED | S1 known_facts #15 |
| A phase handed the document itself observes nothing at judging time beyond what it was given. | transformation::CC_JUDGE_DOCUMENT_V0 parses a document and evaluates a declared rule set against it, and observes nothing; the seed settles that the document travels with the request. | OBSERVED | S1 known_facts #16 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language=concern -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Grounding is only meaningful against the composition the document was written about; against an unrelated snapshot every citation looks like new design. | The identity taxonomy cannot separate proposed-new from fabricated without the CR's declared new artifacts. | MEDIUM | VERIFIED | S1 constraints A verdict must be reproducible |

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Should the pipeline's own domain be excluded from reuse search when a business change request runs? | scope | A library change request must not be offered a pipeline mechanism as a reuse candidate. | S2 gaps No governed call grounds a claim |
