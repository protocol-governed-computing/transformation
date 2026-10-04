# Stage 2 — Domain Model Verification: transformation / design

**Stage:** 2 — Domain Model Verification
**CR:** routing_closure
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. The observing
capability's declaration was read for the outcomes it can report, each judging contract's steps for
the outcomes they answer, each phase workflow for the outcomes it routes, and the generator for what
it writes into each artifact.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Phase | One stage a change document passes through, with its own rules and its own verdict. | Not stored; declared once and carried by its workflow. | OBSERVED | S1 business_vocabulary #1 |
| The Observation | A question a phase asks the composition about itself before it judges. | Not stored; asked of one governed capability each time a phase runs. | OBSERVED | S1 business_vocabulary #2 |
| The Judgement | A phase's verdict: judged, or rejected. | Recorded in the phase's trace. Unchanged by this change. | OBSERVED | S1 business_vocabulary #4 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Observation | Its answer | One of four: an answer, a refused question, a failure to reach the composition, or nothing found. | OBSERVED | S2 belief_verification #1 |
| The Judgement | Its ending | Judged or rejected. Unchanged by this change. | OBSERVED | S1 lifecycle_states #1 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Judge a document against the composition | The author of a change | The document is judged, or rejected. | OBSERVED | S1 requested_outcomes #1 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Judge a document against the composition | 1 | Read the document and the documents it was handed. | None. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Judge a document against the composition | 2 | Ask the composition each question the phase's rules read. | None. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Judge a document against the composition | 3 | Judge the document against its rules and the answers. | The verdict, in the trace. | OBSERVED | S2 pps_baseline_fqdns #1 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Every step that asks the composition a question answers three of the four ways, and not nothing found. | VERIFIED | capability_side_effects::CS_SNAPSHOT_QUERY_V0 declares SUCCESS, NOT_FOUND, VIOLATION and BACKEND_ERROR for QUERY, and passes through the status the inspector reports. Each of the eight observing steps — six in transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 and two in transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 — answers SUCCESS, VIOLATION and BACKEND_ERROR, and not NOT_FOUND. Neither contract declares NOT_FOUND among the outcomes it can end with. | S1 system_beliefs #1 |
| The phase workflows route a judgement, a refusal and a failed observation, and not nothing found. | VERIFIED | The seven phase workflows that observe, P2 to P8, route SUCCESS to EXIT_JUDGED and VIOLATION and BACKEND_ERROR to EXIT_REJECTED, and route nothing for NOT_FOUND. P0 and P1 observe nothing and route both outcomes their contract declares. | S1 system_beliefs #2 |
| The observing steps and the routing are written by hand beside a generator that writes the rest of the same artifacts. | VERIFIED | `transformation.design.emit:emit_rule_sets` writes each phase workflow's sealed rule set and provenance, and the snapshot judge's observation map and any observing step it lacks. It writes the routing of no workflow, and leaves an observing step it did not create as it found it. Its template for a new observing step answers three outcomes. | S1 system_beliefs #3 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Judging against the composition | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Reads a document, observes the composition six ways, and judges. | PARTIAL | Its observing steps do not answer nothing found. |
| Judging against the composition's declarations | transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 | Reads a document, observes the composition two ways, and judges. | PARTIAL | Its observing steps do not answer nothing found. |
| Judging a document alone | transformation::CC_JUDGE_DOCUMENT_V0 | Reads and judges a document without observing anything. | EXACT | Nothing for this purpose; it observes nothing. |
| Observing the composition | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | Answers a published inspection question about the bound composition. | EXACT | Nothing; it declares the four ways it answers. |
| Generating the phase artifacts | transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0 | Carries P2's sealed rules, generated; routes a judgement. | PARTIAL | Its routing is written by hand and omits nothing found. The same holds for P3 to P8. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Eight observing steps do not answer nothing found. | CRITICAL | A phase whose observation finds nothing carries on and judges against an observation that did not arrive. | OBSERVED | S2 belief_verification #1 |
| Seven phase workflows do not route nothing found. | MAJOR | Once the steps answer it, the phase stops with no declared ending. | OBSERVED | S2 belief_verification #2 |
| The answers and the routing are hand-kept beside the generator. | MAJOR | The next way of answering the capability gains is answered nowhere. | OBSERVED | S2 belief_verification #3 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The pipeline has in itself the gap it refuses in the changes it judges. | P7 refuses a design whose act leaves an outcome unanswered. The phases that apply that rule leave one. | OBSERVED | S2 belief_verification #1 |
| The generator already owns everything around the gap. | It writes each workflow's rules and provenance and each judge's observation map, so the answers and the routing can be derived where the rest is. | OBSERVED | S2 belief_verification #3 |
| The open standard now requires both closures. | `v1` Changes 3 and 4 of the Open PGC Standard require a composed step to answer every outcome its capability declares, and construction to refuse an outcome no route answers. | OBSERVED | S2 belief_verification #1 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The capability's outcomes cannot be read by the generator from their declaration. | The platform's declarations are not shipped with its package, by design. | MINOR | OBSERVED | S2 belief_verification #3 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
