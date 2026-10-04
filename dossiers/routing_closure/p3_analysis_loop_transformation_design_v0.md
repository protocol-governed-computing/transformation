# Stage 3 — Analysis Loop: transformation / design

**Stage:** 3 — Analysis Loop

**CR:** routing_closure

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

Each gap carried from Stage 2 is driven to a committed decision against the pinned composition. The
question throughout is one: where a phase's answer to an observation is stated, so that every
answer the capability can give has one.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | Each of the eight observing steps answers NOT_FOUND by ending its contract with it, as it already answers VIOLATION and BACKEND_ERROR. | No step carries on past an observation that did not arrive. | OBSERVED | HIGH | CLOSED | S2 belief_verification #1; S1 known_facts #3 |
| Q2 | Both judging contracts declare NOT_FOUND among the outcomes they can end with, because their steps now end them with it. | Each contract states every way it can end. | OBSERVED | HIGH | CLOSED | S2 belief_verification #1 |
| Q3 | Each of the seven observing phase workflows routes NOT_FOUND to EXIT_REJECTED, the ending it already sends every other non-judgement to. | No ending is added. | OBSERVED | HIGH | CLOSED | S2 belief_verification #2; S1 known_facts #2 |
| Q4 | The generator writes the answers and the routing. An observing step's answers are generated from the outcomes the capability declares, and a workflow's routing from the outcomes its judging contract declares: SUCCESS keeps the ending the workflow names, and every other outcome is routed to the rejected ending. | A way of answering the capability gains is answered and routed at the next emission, and `tc phase emit --check` refuses a build that has not caught up. | OBSERVED | HIGH | CLOSED | S2 belief_verification #3; S1 constraints #3 |
| Q5 | The capability's outcomes are held once in the generator, because the platform's declarations are not shipped with its package. The platform change that accompanies this one makes the compiler compare every step's answers against the capability it binds, so the copy cannot then disagree with the declaration and build. | One named copy, checked at compile time, in place of nine unchecked ones. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #1 |
| Q6 | P0 and P1 observe nothing. Their routing already answers their contract, and generating it changes nothing they route; their provenance gains the contract their routing is generated from. | Two workflows change in provenance only. | OBSERVED | HIGH | CLOSED | S2 belief_verification #2 |
| Q7 | Every judgement on observations that succeed is unchanged: no rule changes, and each change adds an answer for NOT_FOUND and touches no other. | Every document judged before is judged the same. | OBSERVED | HIGH | CLOSED | S1 constraints #1 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| Every step that asks the composition a question answers three of the four ways, and not nothing found. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 and Q2 |
| The phase workflows route a judgement, a refusal and a failed observation, and not nothing found. | S2 belief_verification #2 | CONFIRMED | Resolved in Q3 and Q6 |
| The observing steps and the routing are written by hand beside a generator that writes the rest of the same artifacts. | S2 belief_verification #3 | CONFIRMED | Resolved in Q4 |
| Eight observing steps do not answer nothing found. | S2 gaps #1 | CONFIRMED | Resolved in Q1 |
| Seven phase workflows do not route nothing found. | S2 gaps #2 | CONFIRMED | Resolved in Q3 |
| The answers and the routing are hand-kept beside the generator. | S2 gaps #3 | CONFIRMED | Resolved in Q4 |
| The capability's outcomes cannot be read by the generator from their declaration. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q5 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| The judging contracts | Capability contracts | EXTEND | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 and transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 answer and declare NOT_FOUND |
| The phase workflows | Workflows | EXTEND | The nine phase workflows have their routing generated; seven gain a route for NOT_FOUND |
| The generator | Construction machinery | EXTEND | `transformation.design.emit:emit_rule_sets` writes the answers and the routing |
| The observing capability | Platform capability | REUSE | capability_side_effects::CS_SNAPSHOT_QUERY_V0, unchanged |
| Judging a document alone | Capability contract | REUSE | transformation::CC_JUDGE_DOCUMENT_V0, unchanged |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Amended — six observing steps answer NOT_FOUND, and the contract declares it | 12 | si.topology.impact impacted_count 12 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 | Amended — two observing steps answer NOT_FOUND, and the contract declares it | 2 | si.topology.impact impacted_count 2 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0 | Amended — routes NOT_FOUND; routing generated. P3 to P8 alike | 0 | si.topology.impact impacted_count 0 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Amended — provenance names its judging contract. P1 alike | 0 | si.topology.impact impacted_count 0 |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Answer every way an observation can answer | EXTEND | Each observing step ends its contract on any answer but success, and the contract declares it. | Letting a phase judge without the observation was checked and rejected by the business: nothing is indistinguishable from a pass. | S3 analysis_findings Q1 |
| Reject a judgement whose observation found nothing | EXTEND | Each observing phase routes it to the rejected ending it already has. | A separate ending was checked and rejected: a phase judges or rejects. | S3 analysis_findings Q3 |
| Generate the answers and the routing | EXTEND | The generator that writes the rest of these artifacts writes these parts too, from what the capability and the contracts declare. | Answering by hand, as the steps were written, was checked and rejected: the hand-kept copy is the gap. | S3 analysis_findings Q4 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | Every artifact that changes, and the generator, belongs to design. | S3 analysis_findings Q4 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The one CRITICAL gap resolves to eight steps that end on nothing found |
| No open analyst questions | SATISFIED | All seven findings are CLOSED. The business answered where nothing found ends, at the seed |
| No dependency expansion in the last pass | SATISFIED | A second pass followed the steps into the contracts and the workflows; a third over all nine workflows found only provenance in P0 and P1 |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All seven items re-grounded and CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
