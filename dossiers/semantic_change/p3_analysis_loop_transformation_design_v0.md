# Stage 3 — Analysis Loop: transformation / design

**Stage:** 3 — Analysis Loop

**CR:** semantic_change

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

The six gaps and two concerns carried from Stage 2 are driven to committed decisions against the
pinned composition.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | Construction compares every amendment with the artifact the composition holds, by the platform's declaration: explanation is ignored where it is text, an unordered list is read as a set, and a reference naming the declared successor of what it named is the same reference. Any other difference is a change of meaning and is refused, naming each place. A generated amendment is compared once its generator has run. | No change of meaning is built under an old identity. The comparison of what an amendment loses becomes part of it. | OBSERVED | HIGH | CLOSED | S2 gaps #1 |
| Q2 | A design that amends, replaces or re-points anything is refused when construction is not handed the composition. | No amendment is built uncompared. | OBSERVED | HIGH | CLOSED | S2 gaps #2 |
| Q3 | The phase that judges a design no longer admits a withdrawal. | A withdrawal can only arrive as a replacement. | OBSERVED | HIGH | CLOSED | S2 gaps #3 |
| Q4 | A design may re-point an artifact it holds. Construction rewrites, in that artifact, every value in a declared reference part that names an artifact the design replaces, by full name or by short code, to that artifact's declared successor, and changes nothing else. | A referrer follows a replacement without being restated. | OBSERVED | HIGH | CLOSED | S2 gaps #4 |
| Q5 | For each artifact a design replaces, construction asks inspection who refers to it. Each live referrer must itself be replaced, amended or re-pointed by the design; one in another domain is refused and named, because a design builds one domain. | What a replacement reaches is accounted for before it is built. | OBSERVED | HIGH | CLOSED | S2 gaps #5 |
| Q6 | Inspection answers who refers to an artifact from the composition's record of references, together with the execution edges it already walks. | Every referrer is reported, across domains. | OBSERVED | HIGH | CLOSED | S2 gaps #6; S2 architectural_observations #4 |
| Q7 | The rules that judge a design change, so the workflow carrying them is replaced by a new version. The generator maps the design phase to the new workflow. The new workflow's hand-written parts are carried from the old one, and the generator writes its rules, routing and provenance. | This change follows the rule it builds. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #1; S2 architectural_observations #3 |
| Q8 | The intent that starts the design phase is re-pointed to the new workflow by hand, because a design can re-point only once this change's rules are sealed. The two test drivers that name the workflow in full move with it. | The one short-code referrer is accounted for, and named. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #2; S2 architectural_observations #2 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| Construction compares an amendment with the artifact it restates only for what the amendment would lose, and only when handed the composition. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 and Q2 |
| A design can name a referrer only by restating it. | S2 belief_verification #2 | CONFIRMED | Resolved in Q4 |
| The composition's record of references names every artifact that names another. | S2 belief_verification #3 | OVERTURNED | The record does; inspection does not read it. Resolved in Q6 |
| Nothing in the design checks what a replaced artifact reaches. | S2 belief_verification #4 | CONFIRMED | Resolved in Q5 |
| This change alters the rules that judge it. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q7 |
| A short-code referrer is not in the record. | S2 discovery_concerns #2 | CONFIRMED | Resolved in Q8 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| How two declarations compare | Vocabulary | REUSE | artifact::VOCAB_DECLARATION_REPRESENTATION_V1, read by exact identity |
| Judging a design | Workflow | AUTHOR_NEW | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 is replaced by its next version |
| Offering a design | Intent | EXISTING | transformation::IN_DESIGN_INTENT_SUBMITTED_V0, re-pointed by hand |
| Who refers to an artifact | Inspection query | EXISTING | si.artifact.refs, whose answer is completed from the record |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Stood down; started by one intent, by short code | 1 | The intent's workflow; the record holds no full-name reference to it |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Judge a design | AUTHOR_NEW | Its rules change, so its workflow is a new version that stands in for the old. | Amending the workflow in place was rejected: it changes what the workflow decides. | S3 analysis_findings Q7 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | The rules a design is judged by are the design subdomain's. | S3 analysis_findings Q7 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The three CRITICAL gaps resolve in Q1, Q2 and Q6 |
| No open analyst questions | SATISFIED | All eight findings are CLOSED |
| No dependency expansion in the last pass | SATISFIED | A second search for what names the design workflow found nothing beyond Q8 |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | The one OVERTURNED item resolves in Q6 |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
