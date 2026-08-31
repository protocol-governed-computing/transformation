# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** rule_expressiveness
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot and against the rule sets
the phases declare. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Phase | One step a change passes through, declaring a rule set and rendering a verdict. | Nine declared artifacts, one per phase, owned by this subdomain. | VERIFIED | S1 business_vocabulary #1 |
| Rule | A single thing a phase requires, judged mechanically. | Declared inside the phase that requires it. | VERIFIED | S1 business_vocabulary #2 |
| Check kind | A way of judging that rules are written in. | Not declared as an artifact. It exists only where the judging is carried out. | VERIFIED | S1 business_vocabulary #3 |
| Register | A table in a document, carrying rows of one sort. | Declared by the phase that requires it. | VERIFIED | S1 business_vocabulary #4 |
| Classification | What kind of change a change request is. | A register of the change request. | VERIFIED | S1 business_vocabulary #5 |
| Span | The set of subdomains one change touches. | Nothing holds it. It is not stated anywhere. | NOT_FOUND | S1 business_vocabulary #7 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Classification | Kind | New, extension, modification or retirement. | VERIFIED | S1 business_vocabulary #5 |
| Classification | Rationale | Why the change is of that kind. | VERIFIED | S1 business_vocabulary #5 |
| Classification | Subdomain | Which part of the system the classification applies to. | NOT_FOUND | S1 requested_outcomes #1 |
| Rule | What it requires | The thing a document must satisfy. | VERIFIED | S1 business_vocabulary #2 |
| Rule | Way of judging | The check kind the rule is written in. | VERIFIED | S1 business_vocabulary #3 |
| Register | Presence | Whether the register is there at all. | VERIFIED | S1 business_vocabulary #4 |
| Register | Columns | The columns the register must carry. | VERIFIED | S1 business_vocabulary #4 |
| Register | Non-emptiness | Whether the register has any rows. | VERIFIED | S1 business_vocabulary #4 |
| Register | Row count | How many rows the register may have. | NOT_FOUND | S1 requested_outcomes #4 |
| Disposition | Way of disposing | What a change does about something it depends on. | VERIFIED | S1 business_vocabulary #8 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Judging a document against a phase | The person driving a change | A verdict, and the findings that explain it. | VERIFIED | S1 business_events #1 |
| Stating which subdomains a change touches | The person driving a change | The span of the change, and what each subdomain receives. | NOT_FOUND | S1 requested_outcomes #1 |
| Requiring a purpose and an owner for every subdomain touched | The phases that judge intent and placement | A subdomain changed blindly is refused. | NOT_FOUND | S1 requested_outcomes #2 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Judging a document against a phase | 1 | Read the document's registers. | None. | VERIFIED | S1 business_events #1 |
| Judging a document against a phase | 2 | Judge each rule the phase declares against them. | The findings. | VERIFIED | S1 business_events #1 |
| Judging a document against a phase | 3 | Render a verdict, and separately a figure of merit. | The verdict. | VERIFIED | S1 lifecycle_states #1 |
| Stating which subdomains a change touches | 1 | State each subdomain, and the kind of change it receives. | The classifications. | NOT_FOUND | S1 requested_outcomes #1 |
| Requiring a purpose and an owner for every subdomain touched | 1 | Take the subdomains from what the classifications say. | None. | NOT_FOUND | S1 known_facts #4 |
| Requiring a purpose and an owner for every subdomain touched | 2 | Refuse where any of them lacks a purpose or an owner. | A finding naming the subdomain. | NOT_FOUND | S1 acceptance_criteria #2 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The phases judge documents against rule sets they declare, and those rule sets are governed artifacts rather than code. | VERIFIED | Thirty-eight artifacts are held for this domain. Nine of them are the phases — `transformation::WF_P0_SEED_ADMISSIBILITY_V0` through `transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0` — each owned by the design subdomain, each carrying its own rule set. | S1 system_beliefs #1 |
| A change request states a kind of change and not the subdomain it applies to. | VERIFIED | The classification register declares exactly three columns: the classification, its rationale, and where the row came from. No column names a subdomain. | S1 system_beliefs #2 |
| A dependency may be disposed of as existing, reused, authored new, or still under investigation, and in no other way. | VERIFIED | The dependency register admits a controlled vocabulary of exactly those four. A fifth is refused as not being one of them. | S1 system_beliefs #3 |
| No way of judging can constrain how many rows a register has. | VERIFIED | Forty-two ways of judging are declared. Three concern a register's shape: that it is present, that it carries named columns, and that it has rows at all. None counts them. | S1 system_beliefs #4 |
| A subdomain touched by a change can pass every phase without its purpose being stated or its owner declared. | VERIFIED | No rule in any phase ties a subdomain a change touches to a purpose or to an owner, because no phase knows which subdomains a change touches. Observed in practice: a wallet change also modified an identity function, and identity received neither, while every phase returned admissible. | S1 system_beliefs #5 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Judges a change request | transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | Declares what a change request must contain, including its classification. | PARTIAL | The classification names no subdomain, so nothing can say what the change touches. |
| Judges a seed | transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Declares what the seed must contain, including its classification. | PARTIAL | The same. |
| Judges an analysis | transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0 | Declares the ways a dependency may be disposed of, and separately the decisions a change commits to. | PARTIAL | A dependency that exists and is altered cannot be recorded as such. |
| Judges a statement of intent | transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0 | Requires a purpose for the subdomain the document is about. | PARTIAL | Requires nothing of any other subdomain the change touches. |
| Judges a statement of placement | transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0 | Requires an owner for each capability. | PARTIAL | Requires no owner for a subdomain the change touches but names no capability of. |
| Declares what the domain compiles | transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares the design and build subdomains and their sources. | EXACT | Nothing about the three gaps. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A classification names no subdomain, so the span of a change is unstated and underivable. | CRITICAL | A change touching two subdomains cannot say so. Everything below follows from it. | VERIFIED | S1 system_beliefs #2 |
| No rule requires a purpose for a subdomain a change touches. | CRITICAL | A subdomain can be changed with nothing said about what it governs. | VERIFIED | S1 system_beliefs #5 |
| No rule requires an owner for a subdomain a change touches. | CRITICAL | A subdomain can be changed and be answerable to nobody. | VERIFIED | S1 system_beliefs #5 |
| A dependency that exists and is altered cannot be recorded as such. | CRITICAL | The record says a dependency is merely present while the next register says it is being changed, and nothing reconciles them. | VERIFIED | S1 system_beliefs #3 |
| No way of judging counts a register's rows. | CRITICAL | A register meant to carry one answer may carry several, and no rule anyone could write today would notice. | VERIFIED | S1 system_beliefs #4 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A rule set can only be as expressive as the ways of judging it is written in. Three of the five gaps are absences in that vocabulary rather than rules nobody wrote. | Forty-two ways of judging; none counts rows, and the dependency vocabulary is closed at four. | VERIFIED | S1 business_invariants #1 |
| The lifecycle that governs change is itself a compiled domain, so changing it is an authoring act judged by the same phases it declares. | The nine phases are artifacts of this domain, owned by this subdomain. | VERIFIED | S1 system_beliefs #1 |
| Two registers of one phase hold contradictory statements about the same dependency, and the phase declares no rule relating them. | The dependency register admits four dispositions; the decisions register admits an extension the dependency register cannot express. | VERIFIED | S1 system_beliefs #3 |
| A phase requires a purpose for the subdomain a document is about, and the document is about one subdomain by construction. Nothing was wrong with that rule until a change touched two. | The statement of intent requires a purpose; it has no notion of a second subdomain. | VERIFIED | S1 system_beliefs #5 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The defect the first gap causes was found by a change passing, not failing. A dossier was admissible at every phase while a subdomain it modified had no purpose and no owner. | Observed on a real change carried through seven phases. | CRITICAL | VERIFIED | S1 system_beliefs #5 |
| Correcting what a phase requires makes documents that were admissible inadmissible. Every existing dossier must be re-judged. | Five dossiers exist against these phases. | MAJOR | VERIFIED | S1 constraints #1 |
| Making a constraint expressible and applying it are separate acts. Adding the ability to count rows changes no verdict until some rule uses it. | No register declares a row count today. | MINOR | VERIFIED | S1 known_facts #8 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
