# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** refusal_discharge
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, the design language as it
stands, and the change whose failure raised this one. The rule sets were read as the composition
seals them, rule by rule, rather than from the working tree. What was searched is recorded, not only
what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Refusal | An operation the business states it will not perform, and the condition under which it will not. | Declared in a register at the seed, carried once into the change request. | VERIFIED | S1 business_vocabulary #1 |
| Act | Something the business does as one unit, which completes or is refused. | Declared by a design, rendered by construction. | VERIFIED | S1 business_vocabulary #2 |
| Step | One part of an act, which returns an outcome the act routes on. | Declared by a design, one row per node. | VERIFIED | S1 business_vocabulary #3 |
| Outcome | What a step reports, which decides where the act goes next. | Stated inside the routing a design declares for each step. | VERIFIED | S1 business_vocabulary #4 |
| Ending | Where an act stops. An ending either completes the act or refuses it. | Declared as a node of the act, typed. | VERIFIED | S1 business_vocabulary #5 |
| Discharge | The act, step and outcome that carry a declared refusal out. | Nothing in a design states one. | NOT_FOUND | S1 business_vocabulary #6 |
| Deferral | A declared refusal this change does not carry out, with the owner who will. | Recorded for scope, never for a refusal. | PARTIAL | S1 business_vocabulary #7 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Refusal | The operation refused | What the business will not do. | VERIFIED | S1 identity_and_sameness #1 |
| Refusal | The condition | When it will not do it. | VERIFIED | S1 identity_and_sameness #1 |
| Refusal | What carries it out | Nothing in any phase states this. | NOT_FOUND | S1 system_beliefs #1 |
| Step | Its outcomes | What it may report, each routed somewhere. | VERIFIED | S1 system_beliefs #5 |
| Ending | Whether it refuses | Distinguishes an act that stopped from an act that finished. | VERIFIED | S1 system_beliefs #5 |
| Deferral | Its owner | Who carries the refusal out instead. | NOT_FOUND | S1 constraints #5 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Declaring what the business refuses | The business raising a change | A register of operations and conditions, in the business's own words. | VERIFIED | S1 system_beliefs #1 |
| Carrying the refusals into the change request | The lifecycle | Every row arrives, checked against the seed. | VERIFIED | S1 system_beliefs #1 |
| Asking what carries a refusal out | The rules that judge a design | Nothing. No phase after the change request poses the question. | NOT_FOUND | S1 system_beliefs #2 |
| Designing the act that performs a refused operation | The person raising a change | An act whose steps and outcomes are stated, with nothing tying any of them to a refusal. | PARTIAL | S1 system_beliefs #5 |
| Finding a refusal that was never carried out | Whoever exercises the built function | The act succeeds where it should stop, and the defect is read off the business's own criteria. | VERIFIED | S1 system_beliefs #3 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Carrying the refusals into the change request | 1 | Check every seed row arrived, keyed on the operation and the condition. | A finding where a row was dropped. | VERIFIED | S1 system_beliefs #1 |
| Carrying the refusals into the change request | 2 | Check no row was added that the seed did not state. | A finding where a row was invented. | VERIFIED | S1 system_beliefs #1 |
| Asking what carries a refusal out | 1 | Read the refusals at any phase after the change request. | Nothing — no rule of any later phase names the register. | NOT_FOUND | S1 system_beliefs #2 |
| Designing the act that performs a refused operation | 1 | State the act's steps, their outcomes, and where each outcome routes. | The design's execution topology. | VERIFIED | S1 system_beliefs #5 |
| Designing the act that performs a refused operation | 2 | State which of those steps and outcomes carries which declared refusal. | Nothing — there is no register for it. | NOT_FOUND | S1 requested_outcomes #1 |
| Finding a refusal that was never carried out | 1 | Build the composition and exercise the act. | A run in which the refused operation completes. | VERIFIED | S1 system_beliefs #3 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result | Evidence | Source Finding |
|--------|--------|----------|----------------|
| The refusals a business declares are carried from the seed into the change request and checked for arrival, and no phase after that reads them. | VERIFIED | Every sealed phase rule set was read and each rule's declared register examined. `transformation::WF_P0_SEED_ADMISSIBILITY_V0` declares three rules against `operation_refusals` — the table is present, it has its columns, and it carries no design language. `transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0` declares nine — the same three, four citation rules, and the two that carry the seed: `SEED_ROW_NOT_CARRIED` and `ROW_NOT_IN_SEED`, keyed on the operation and the condition. Twelve rules in total, all at or before the change request. | S1 system_beliefs #1 |
| A design can be judged admissible at every phase while a declared refusal is carried out by nothing. | VERIFIED | The rule sets sealed for P2, P3, P4, P5, P6 and P7 declare **zero** rules against `operation_refusals`. The register is named in P2's document as a stage input, and no rule of that phase or any later one reads it. There is therefore no rule any design could fail on this ground. | S1 system_beliefs #2 |
| A change request declared four refusals and one became nothing at all, and the act ran and did the thing the business refused. | VERIFIED | `blockchain` cr_04_wallet declared four refusals at its seed §18 and carried all four into its change request. Its delivery record states that the refusal *the person has not been accepted, or was rejected* travelled through all nine phases as prose, that there was no branch for a person held but not accepted, and that every phase passed at 100% construction completeness while an unverified person held value. The defect was found by executing the function and checking the result against identity's own criteria. | S1 system_beliefs #3 |
| That change has since been re-authored and all four refusals are now discharged, and three of the four cite something other than the refusal. | VERIFIED | The dossier's execution topology carries a branch for each: the person is not held (`CC_RESOLVE_ACTOR_V0`, NOT_FOUND), has not been accepted (`CC_REQUIRE_ACCEPTED_HOLDER_V0`, VIOLATION), already holds a wallet (`CC_CLAIM_WALLET_IDENTITY_V0`, ALREADY_EXISTS) and states no grounds for a rejection (`CC_REQUIRE_REJECTION_GROUNDS_V0`, VIOLATION). Only the second cites `S1 operation_refusals`; the others cite a dependency, a provisional code and a gap. Nothing asked them to cite the refusal, and nothing would have noticed if none of them had. | S1 system_beliefs #4 |
| A design states its acts, their steps and each step's outcomes, and which ending each outcome routes to. | VERIFIED | The design intent phase declares an execution topology naming the act, the node, the node's type and its routing, and every outcome in that routing names the node it leads to. Endings are nodes of a declared type, and a refusing ending is distinguishable from a completing one. Every fact a discharge would be checked against is already stated by the design. | S1 system_beliefs #5 |
| A phase's declared scope records what the change defers and to whom. | VERIFIED | The business model phase declares an authoring scope carrying deferrals, and the seed declares authority deferrals naming an owner and a condition. Both record what is deferred; neither is keyed to a refusal, so a deferral cannot today be resolved to the refusal it answers. | S1 system_beliefs #6 |
| The composition refuses to seal an obligation nothing is bound to, and the build stops rather than shipping one. | VERIFIED | `fb.governance::INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0` is published, governed by the governance constitution, enforced at compiler meta-validation with `violation_response: FAIL_IMMEDIATELY`. It was met by a real change: the announcement capability's delivery record states the build failed at S4 because no constitution rule named its new invariant, and was fixed by binding one. | S1 system_beliefs #7 |
| The document that judges a design is produced by a generator rather than written. | VERIFIED | The design intent phase declares a generation provenance register naming the artifact, its generator and that generator's sources, and `transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0` is produced that way. One change has been delivered through that path. | S1 system_beliefs #8 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Declares what the seed must state about refusals | transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Requires the register, its columns, and business language in it. | EXACT | Nothing. The business states its refusals here and this change does not touch that. |
| Carries the refusals into the change request | transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | Checks every declared refusal arrived and none was invented. | EXACT | Nothing. It is the last phase that reads the register, and correctly the last that should read it verbatim. |
| Judges a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Declares what a design must state and renders a verdict. | PARTIAL | Asks nothing about what carries a refusal out, and admits a design that carries none out. |
| Judges a mandate | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | Declares the build order and closes the dossier. | PARTIAL | Freezes whatever the design said, including its silence. |
| Evaluates a phase's rules | transformation::CT_PURE_EVALUATE_RULES_V0 | Applies a declared rule set to a parsed design and reports every rule that failed. | EXACT | Nothing — a new rule is a declaration it applies unchanged. |
| Judges a document against the composition | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Passes the composition's published facts to the rules that need them. | EXACT | Nothing. A discharge is checked against the design itself, so no composition fact is required. |
| Refuses an obligation nothing is bound to | fb.governance::INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0 | Fails the build where a declaration resolves to nothing. | EXACT | Nothing — it is the same closure one layer down, and the argument this change borrows. |
| The change whose failure raised this one | blockchain::WF_CREATE_WALLET_V0 | Creates a wallet for an accepted person, refusing one who is not. | EXACT | Nothing now. It was corrected by hand after the fact, which is what this change makes unnecessary. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A design cannot state what discharges a declared refusal. | CRITICAL | The business's strongest rules arrive at the design and stop there. | VERIFIED | S1 requested_outcomes #1 |
| No phase asks whether a declared refusal is carried out. | CRITICAL | A design is judged complete while an operation the business refuses is performed on demand, and the failure is silent. | VERIFIED | S1 requested_outcomes #2 |
| A stated discharge would not be held to the design's own topology. | HIGH | A discharge naming a step that does not exist, or an outcome that routes onward, would document a refusal that does not happen. | VERIFIED | S1 requested_outcomes #3 |
| A refusal owned by someone else cannot be stated as deferred. | HIGH | Without it, a change inheriting a refusal it does not own must either carry it or stay silent, and silence is what this change removes. | PARTIAL | S1 requested_outcomes #4 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The refusal register is checked hardest at the phase where it can least be acted on. | Twelve rules guard its arrival across the seed and the change request; none guards its consequence. Fidelity of transcription was mistaken for governance of content. | VERIFIED | S1 system_beliefs #1 |
| Everything a discharge must be checked against is already stated by the design. | The act, its steps, their outcomes and the type of each ending are all in the design's execution topology. Nothing new needs publishing, and the check is a claim about one document. | VERIFIED | S1 system_beliefs #5 |
| A citation is not a structure. | Three of the four discharged refusals in the only design that discharges any cite something other than the refusal, and the design is correct. A rule reading citations would call correct work red, and would be satisfied by anyone typing the right string. | VERIFIED | S1 system_beliefs #4 |
| The composition already enforces the closure the design pipeline lacks. | An obligation nothing is bound to cannot be sealed, and the build stops. A refusal nothing discharges passes every phase. The two are the same rule at two layers, and only one layer has it. | VERIFIED | S1 system_beliefs #7 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A rule with no subject in the corpus reports clean. | No dossier states a discharge today, so a new rule would pass everywhere on its first run while checking nothing. It must be proved by a probe meant to fail. | HIGH | VERIFIED | S1 acceptance_criteria #2 |
| Only one function has ever exercised the refusal register end to end. | The evidence for the failure is one change request. The shape is general, but the corpus is thin — a reason to derive the rules from what a design states rather than from what one design happened to do. | MEDIUM | VERIFIED | S1 system_beliefs #3 |
| A design that declares no refusals must be judged exactly as it is today. | Most changes declare none. A rule firing on an empty register would make every existing dossier red for a defect none of them has. | HIGH | VERIFIED | S1 acceptance_criteria #5 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| How is a deferral grounded, given that no existing scope record is keyed to a refusal? | DESIGN | The business answered that a deferral must already be present in the change's declared scope, and the scope registers found are not keyed that way. Either the deferral names what it is grounded in, or the grounding is by owner rather than by row. | S1 constraints #5 |
| Is a refusal discharged by an ending that refuses, or by any ending that is not the act's success? | DESIGN | An act may have several endings. The business said the outcome must route to an ending that refuses, and whether an act's endings are typed finely enough to tell one from another is a question for the design language, not for the business. | S1 business_invariants #3 |
