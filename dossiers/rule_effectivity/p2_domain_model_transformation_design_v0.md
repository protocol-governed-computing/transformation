# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, the dossiers themselves,
and the recorded history of changes made to them. What was searched is recorded, not only what was
found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Rule set | What a phase judges a document against, at a moment in time. | Nine, one per phase. | VERIFIED | S1 business_vocabulary #1 |
| Rule-set version | A named state of the rule set. | Nothing holds one. The rule set has no version in any form. | NOT_FOUND | S1 business_vocabulary #2 |
| Effectivity | A correction's declaration of whether it is retroactive. | Nothing holds one. | NOT_FOUND | S1 business_vocabulary #3 |
| Approval | A gate closed on a dossier. | Recorded in the dossier, without saying under what. | VERIFIED | S1 business_vocabulary #6 |
| Migration | A dossier amended to satisfy a later rule set. | Recorded in one commit message and nowhere else. | VERIFIED | S1 business_vocabulary #7 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Approval | The version it was given under | Which rules the gate was closed against. | NOT_FOUND | S1 requested_outcomes #3 |
| Verdict | The version it was rendered against | Which rules produced this answer. | NOT_FOUND | S1 acceptance_criteria #6 |
| Correction | Its effectivity | Whether it can alter a prior dossier's admissibility. | NOT_FOUND | S1 requested_outcomes #1 |
| Correction | The dossiers it affects | Named where it is retroactive. | NOT_FOUND | S1 requested_outcomes #4 |
| Dossier | Its state | Approved, migrated, or re-approved. | NOT_FOUND | S1 lifecycle_states #1 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Judging a document | The person driving a change | A verdict, against the rules in force at that moment. | VERIFIED | S1 system_beliefs #1 |
| Closing a gate on a dossier | A person | An approval, recorded without saying under what rules. | VERIFIED | S1 system_beliefs #2 |
| Correcting a rule set | The person making the correction | A changed rule set, with no statement of whom it affects. | VERIFIED | S1 system_beliefs #3 |
| Migrating a dossier to a later rule set | The person making the correction | A dossier that passes, indistinguishable from one that always did. | VERIFIED | S1 system_beliefs #4 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Correcting a rule set | 1 | Declare whether the correction is retroactive. | The declaration. | NOT_FOUND | S1 requested_outcomes #1 |
| Correcting a rule set | 2 | Where retroactive, create a version and name the dossiers affected. | The version, and the list. | NOT_FOUND | S1 requested_outcomes #4 |
| Correcting a rule set | 3 | Where non-retroactive, create nothing and disturb nothing. | Nothing. | NOT_FOUND | S1 known_facts #8 |
| Closing a gate on a dossier | 1 | Pin the rule-set version the approval was given under. | The pin. | NOT_FOUND | S1 requested_outcomes #3 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| A document is judged only against the rules in force when it is judged. | VERIFIED | A verdict states the phase, the finding count and the rules declared, and names no version of them. Re-running the same document after a correction yields a different answer with nothing to say which of the two changed. | S1 system_beliefs #1 |
| Nothing records which rules a document was approved under. | VERIFIED | No dossier in either domain carries a rule-set version. The only document mentioning one is the problem statement of a sibling change proposing them. | S1 system_beliefs #2 |
| A correction cannot say whether it is retroactive. | VERIFIED | A change to a rule set is a change to a template or a declaration. Neither carries a statement of effect on prior documents, and no rule asks for one. | S1 system_beliefs #3 |
| Dossiers have already been amended to satisfy rules written after their approval, and nothing in them says so. | VERIFIED | Three completed dossiers were amended, then restored to their approved text. The amendment, its reason and its reversal survive in commit messages; nothing in the dossiers records either. | S1 system_beliefs #4 |
| A rule set has no version at all. | VERIFIED | Rules are counted and their consistency reported; the count is not a version, and nothing distinguishes one state of the rule set from another. | S1 system_beliefs #5 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Judges a seed | transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Declares what a seed must contain and renders a verdict. | PARTIAL | Names no version of the rules it used. |
| Judges a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Declares what a design must state and renders a verdict. | PARTIAL | The same. |
| Judges a mandate | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | Declares the build order and renders a verdict, closing the dossier. | PARTIAL | The approval it gates records no version. |
| Declares what this domain compiles | transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares the design and build subdomains. | EXACT | Nothing about versioning. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A correction cannot declare its effectivity. | CRITICAL | Nothing else follows without it: no version, no affected list, no distinction between states. | VERIFIED | S1 system_beliefs #3 |
| The rule set has no version. | CRITICAL | An approval cannot pin what it was given under. | VERIFIED | S1 system_beliefs #5 |
| An approval records no version. | CRITICAL | An approval that still stands cannot be told from one whose rules have moved. | VERIFIED | S1 system_beliefs #2 |
| A retroactive correction names no affected dossiers. | CRITICAL | Which dossiers a change invalidates is discovered later, by them failing. | VERIFIED | S1 requested_outcomes #4 |
| A migrated dossier is indistinguishable from an approved one. | CRITICAL | The corpus makes a stronger claim than it earned, and did. | VERIFIED | S1 system_beliefs #4 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Every rule is retroactive by default, because nothing can declare otherwise. A correction that could not possibly affect a prior document invalidates it exactly as one that could. | Two corrections were made in one session: one changed no verdict, one invalidated every dossier that existed. Neither could say which it was. | VERIFIED | S1 system_beliefs #3 |
| The distinction between approved and migrated exists in the record only where someone wrote it in prose. | Three dossiers amended and restored; the reasoning survives in commit messages and in no dossier. | VERIFIED | S1 system_beliefs #4 |
| The same principle is enforced elsewhere and unenforced here. A completed change is never re-pinned to a later composition; nothing stops it being re-judged by a later rule set. | The baseline pin is enforced and refuses before any phase runs. No equivalent exists for rules. | VERIFIED | S1 known_facts #11 |
| A rule count is not a version. Counting rules says how many there are, not which state of them a document was judged against. | The rule set reports its count and its consistency, and nothing more. | VERIFIED | S1 system_beliefs #5 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Three completed dossiers were amended to satisfy rules written after their approval, and the only record is a commit message. Restoring them was a judgement made afterwards, not a rule enforced at the time. | The amendment, its reason and its reversal are all in git and in no dossier. | CRITICAL | VERIFIED | S1 system_beliefs #4 |
| The tool makes the wrong act the easy one. A closed dossier reads as failing, and the only way to make it pass is to amend it. | Three dossiers currently read inadmissible, correctly, and nothing in the tool says the red is deliberate. | MAJOR | VERIFIED | S1 constraints #1 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
