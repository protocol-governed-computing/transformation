# Stage 2 — Domain Model Verification: transformation / design

**Stage:** 2 — Domain Model Verification
**CR:** semantic_change
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. Construction's
comparison of an amendment was read, the actions a design may take on an artifact it holds were read
from the phase that declares them, and inspection was asked who refers to three artifacts and
compared with the composition's own record.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Amendment | A change that restates an artifact under the identity it has. | Stated by a design; not stored. | OBSERVED | S1 business_vocabulary #1 |
| The Replacement | A change that gives an artifact a new identity standing in for the old one. | Stated by a design; not stored. | OBSERVED | S1 business_vocabulary #2 |
| The Referrer | An artifact that names another. | Part of the composition; answered by inspection. | OBSERVED | S1 business_vocabulary #5 |
| The Phase Rule Set | The rules a phase judges a document by, sealed in that phase's workflow. | Sealed in the composition; generated. | OBSERVED | S2 belief_verification #2 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Amendment | What it withdraws | Facts a design names as removed from the artifact. | OBSERVED | S2 belief_verification #1 |
| The Referrer | How it names | By full name in a declared reference part, or by short code. | OBSERVED | S2 belief_verification #3 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Build a design | The author of a change | The artifacts the design determines are written, or the build is refused. | OBSERVED | S1 requested_outcomes #1 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Build a design | 1 | Measure whether the design determines every fact it must. | The measure. | OBSERVED | S2 belief_verification #1 |
| Build a design | 2 | When handed the composition, find what each amendment would lose that the design does not withdraw. | A refusal per loss. | OBSERVED | S2 belief_verification #1 |
| Build a design | 3 | Write each artifact and mark each replaced one stood down. | The artifacts. | OBSERVED | S2 belief_verification #4 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Construction compares an amendment with the artifact it restates only for what the amendment would lose, and only when handed the composition. | VERIFIED | `tc construction check` reads each EXTEND row's artifact from the composition and lists the facts it holds that the rendering lacks, less those the design withdraws. An added or altered fact is not looked for. Without `--snapshot` it prints a note and admits the design. A generated artifact inventoried as EXTEND is not compared at all. | S1 system_beliefs #1 |
| A design can name a referrer only by restating it. | VERIFIED | P7's sealed rule set, in transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, admits four actions on an artifact a design holds: REPLACE, REUSE, EXTEND and REVIEW. An EXTEND is rendered whole. REVIEW is not rendered and is written by hand. | S1 system_beliefs #2 |
| The composition's record of references names every artifact that names another. | NOT_FOUND | The record names them: each artifact's canonical references hold every full name in a declared reference part. Inspection does not read it. si.artifact.refs walks the evidence graph, which holds only addressed nodes and drops every edge across domains. Of the 1,008 references the record holds, it misses 342, all into 17 artifacts: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0 is named by 73 artifacts and reported referred to by 1, and workflow::CONSTITUTION_WORKFLOW_V0 by 41 and reported by 2. | S1 system_beliefs #3 |
| Nothing in the design checks what a replaced artifact reaches. | VERIFIED | Construction marks each REPLACE row's artifact superseded and asks nothing about its referrers. The compiler refuses a live reference to it, by artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0, after the design is approved and built. | S1 system_beliefs #4 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Judging a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Carries P7's sealed rules, generated; admits the four actions and the withdrawal register. | PARTIAL | Admits no re-point, and admits a withdrawal. |
| Offering a design | transformation::IN_DESIGN_INTENT_SUBMITTED_V0 | Admits a design for judgement and starts the P7 workflow, named by short code. | EXACT | Nothing for this purpose. |
| Declaring what a reference is and how two declarations compare | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | Names the parts that carry no meaning, the reference parts, the supersession parts and the two comparison rules. | EXACT | Nothing; it is read, unchanged. |
| Keeping a stood-down artifact out of reach | artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 | Refuses a live reference to a stood-down artifact when the composition is compiled. | EXACT | Nothing; it stays the last guard. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Construction does not compare what an amendment adds or alters. | CRITICAL | A change of meaning is built under the old identity. | OBSERVED | S2 belief_verification #1 |
| Construction admits an amendment it never compared. | CRITICAL | Without the composition, any amendment is built. | OBSERVED | S2 belief_verification #1 |
| A design may withdraw a fact. | MAJOR | A withdrawal is a change of meaning, admitted as an amendment. | OBSERVED | S2 belief_verification #1 |
| A design cannot re-point a reference without restating its holder. | MAJOR | A referrer the design language cannot restate cannot follow a replacement. | OBSERVED | S2 belief_verification #2 |
| Nothing in building a design asks what a replacement reaches. | MAJOR | A stale reference is found after approval, by the compiler. | OBSERVED | S2 belief_verification #4 |
| Inspection under-reports who refers to an artifact. | CRITICAL | A replacement cannot learn what it reaches from inspection. | OBSERVED | S2 belief_verification #3 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A generated artifact changes meaning when its generator's sources do. | P7's rule set is generated from the phase's rules and template; this change alters both. | OBSERVED | S2 belief_verification #2 |
| The workflow that judges a design is named in four places outside the composition's record. | The intent that starts it names it by short code; the generator maps each phase to its workflow's file; two test drivers name it in full. | OBSERVED | S2 pps_baseline_fqdns #1 |
| The generator writes into a workflow that exists and never creates one. | It splices the sealed rules, routing and provenance into the file it maps a phase to. | OBSERVED | S2 architectural_observations #1 |
| The record of references is complete; only its reader is not. | Each canonical record holds its references; inspection reads a different graph. | OBSERVED | S2 belief_verification #3 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| This change alters the rules that judge it. | The P7 rule set it changes is the one its own design is checked by. | MAJOR | OBSERVED | S2 architectural_observations #1 |
| A short-code referrer is not in the record. | The intent names the workflow it starts by short code, and short codes are not declared references. | MAJOR | OBSERVED | S2 architectural_observations #2 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
