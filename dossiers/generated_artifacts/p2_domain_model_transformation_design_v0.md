# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** generated_artifacts
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot and against the record of
changes already made. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Generated artifact | One a tool produces from something else, carrying a copy of what determines it. | Nine, one per phase. | VERIFIED | S1 business_vocabulary #2 |
| Generator | What an artifact is produced from, with the mechanism that produces it. | A template and a declaration, read by one emission. | VERIFIED | S1 business_vocabulary #3 |
| Authored artifact | One a person writes; the artifact is its own source of truth. | Every other artifact of this domain. | VERIFIED | S1 business_vocabulary #1 |
| Provenance | The record of which generator an artifact came from. | Nothing holds it. | NOT_FOUND | S1 business_vocabulary #4 |
| Agreement | Whether an artifact still matches what generated it. | Checkable, and required by no build. | VERIFIED | S1 business_vocabulary #5 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Generated artifact | What produced it | The generator it came from. | NOT_FOUND | S1 requested_outcomes #1 |
| Generated artifact | Whether it agrees | Whether it still matches what produced it. | VERIFIED | S1 lifecycle_states #1 |
| Generator | What it produces from | The template and the declaration together. | VERIFIED | S1 known_facts #5 |
| Generator | What it produces | The artifact carrying the sealed copy. | VERIFIED | S1 business_vocabulary #3 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Producing an artifact from its generator | A person, by hand | The artifact matches what determines it. | VERIFIED | S1 business_events #1 |
| Checking that an artifact agrees with its generator | A person following a written procedure | A report, believed and not required. | VERIFIED | S1 system_beliefs #4 |
| Delivering a change to a generated artifact through the lifecycle | The person driving a change | Nothing. It has never happened. | NOT_FOUND | S1 system_beliefs #5 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Delivering a change to a generated artifact through the lifecycle | 1 | Name, in the design, the generator the artifact is produced from. | The design. | NOT_FOUND | S1 requested_outcomes #1 |
| Delivering a change to a generated artifact through the lifecycle | 2 | Change the generator, never the artifact. | The generator. | VERIFIED | S1 known_facts #1 |
| Delivering a change to a generated artifact through the lifecycle | 3 | Reach the artifact by invoking the generator. | The artifact. | NOT_FOUND | S1 requested_outcomes #2 |
| Delivering a change to a generated artifact through the lifecycle | 4 | Refuse the build where artifact and generator disagree. | The refusal. | NOT_FOUND | S1 requested_outcomes #3 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Some artifacts of this domain are produced by a generator rather than written. | VERIFIED | Nine are: one workflow per phase, from `WF_P0_SEED_ADMISSIBILITY_V0` through `WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0`. Each carries a sealed copy of its phase's rule set, and the emission that writes them names all nine explicitly. | S1 system_beliefs #1 |
| A design has no way to say that an artifact is produced from something else. | VERIFIED | A design states what an artifact must become, register by register. No register names a generator, and no rule asks for one. | S1 system_beliefs #2 |
| Construction renders an artifact from the design alone, and would overwrite a generated one. | VERIFIED | An amendment renders the artifact that replaces its predecessor. For a generated artifact the result would be overwritten by the next emission, and until then would disagree with what determines it. | S1 system_beliefs #3 |
| A generated artifact's agreement with its generator can be checked, and nothing requires the check. | VERIFIED | The emission reports whether every artifact already matches and returns non-zero when one does not. It is named as a step in a written runbook and as an obligation in a plan document. **No build invokes it.** A procedure nobody is required to follow is a habit. | S1 system_beliefs #4 |
| Two changes to this domain have already been designed and delivered by hand because of this. | VERIFIED | The founding change establishing this subdomain reached P2 and stopped; its closure records the outcome as implemented outside the governed construction path. A later change reached Gate 1, was approved, and closed there for the same cause. Both delivered; neither through the lifecycle. | S1 system_beliefs #5 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Judges a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Declares what a design must state about each artifact. | PARTIAL | Nothing about how an artifact is reached; no register names a generator. |
| Judges a mandate | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | Declares the order artifacts are built in. | PARTIAL | Schedules what a change creates; says nothing about how a generated artifact is produced. |
| Declares what this domain compiles | transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares the design and build subdomains and their sources. | EXACT | Nothing about generation. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A design cannot name the generator an artifact is produced from. | CRITICAL | Without it nothing downstream can know to invoke rather than render. | VERIFIED | S1 system_beliefs #2 |
| Construction cannot invoke a generator. | CRITICAL | The delivery path for nine artifacts does not exist. | VERIFIED | S1 system_beliefs #3 |
| Nothing requires an artifact to agree with its generator. | CRITICAL | A stale sealed copy reports confidently on the wrong rule set, and has done. | VERIFIED | S1 system_beliefs #4 |
| Nothing records which generator an artifact came from. | CRITICAL | Agreement can only be checked where the pairing is already known to a tool. | NOT_FOUND | S1 requested_outcomes #1 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The lifecycle has never delivered a change to itself through itself. Every capability it has was built by hand while a dossier described the intent and stopped. | Two dossiers, both stopped, both delivered outside the path. | VERIFIED | S1 system_beliefs #5 |
| The mechanism that would enforce agreement already exists and is not in force. The gap is enforcement, not capability. | The emission reports agreement and returns non-zero; no build calls it. | VERIFIED | S1 system_beliefs #4 |
| A generated artifact is the only kind whose content is determined somewhere the lifecycle cannot see. Every rule that assumes an artifact is its own source of truth is silently wrong for these nine. | Nine artifacts, each carrying a copy of something declared elsewhere. | VERIFIED | S1 system_beliefs #1 |
| The failure this prevents has occurred: a rule added after a workflow was emitted left a smaller rule set sealed, and every run reported confidently on it. | Recorded by the emission itself as the reason it exists. | VERIFIED | S1 system_beliefs #4 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| This change cannot be delivered through the path it creates, because that path does not exist until it is delivered. It is the last change that must be delivered by hand. | Two prior dossiers stopped for this cause; this one changes the same artifacts. | CRITICAL | VERIFIED | S1 system_beliefs #5 |
| Agreement is documented as a procedure in a runbook and a plan. A written obligation nobody is required to meet is indistinguishable from none. | The check appears in two documents and no build. | MAJOR | VERIFIED | S1 system_beliefs #4 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
