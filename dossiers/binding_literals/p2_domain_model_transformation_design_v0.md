# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** binding_literals
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the rule set the Design Intent phase seals in
the pinned snapshot, against the code that applies it, and against a design judged by it. What was
searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Binding | A design's statement of where a step's input comes from. | A row of the Design Intent's step-bindings register: an owner, a step, a direction, a field and a source. | VERIFIED | S1 business_vocabulary #1 |
| Reference | A binding to a value the runtime offers: the starting intent, the contract's own inputs, or an earlier step's result. | A source rooted in one of five names the runtime offers. | VERIFIED | S1 business_vocabulary #2 |
| Literal | A binding to a value the design fixes. | A source no rule roots. Two rules decide separately what counts as one. | VERIFIED | S1 business_vocabulary #3 |
| Generator | What produces an artifact in place of construction writing it. | A row of the Design Intent's generation-provenance register, naming the generator and everything it reads. | VERIFIED | S1 business_vocabulary #4 |
| Generated value | An input whose value the generator of the artifact that holds it determines. | Nothing states it. | NOT_FOUND | S1 business_vocabulary #5 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Binding | Source | Where the value comes from, as the design writes it. | VERIFIED | S1 business_vocabulary #1 |
| Literal | Meaning | Whether a written source is a value the design fixes. | VERIFIED | S1 requested_outcomes #1 |
| Generated value | Generator | The generator that determines the value. | NOT_FOUND | S1 requested_outcomes #2 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Judging a binding | The person driving a change | Each rule that judges a binding admits or refuses it. | VERIFIED | S1 business_events #1 |
| Declaring a value generated | The person driving a change | Nothing: no statement of it exists. | NOT_FOUND | S1 business_events #2 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Judging a binding | 1 | One rule decides whether the source is a reference the runtime offers, or a literal. | A finding when it is rooted in a name the runtime does not offer. | VERIFIED | S1 system_beliefs #1 |
| Judging a binding | 2 | Another rule decides whether the source is written in a form the runtime resolves. | A finding when it matches none of the forms the rule admits. | VERIFIED | S1 system_beliefs #1 |
| Declaring a value generated | 1 | State that the generator determines the input. | None. | NOT_FOUND | S1 requested_outcomes #2 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Two rules of the Design Intent phase judge the same binding: one asks whether it is a reference the runtime offers, the other whether it is written in a form the runtime resolves. | VERIFIED | The phase's sealed rule set holds BINDING_SOURCE_UNROOTED and BINDING_SOURCE_MALFORMED, both over the step-bindings register's source column. Five other rules judge a binding too, none of them its form. | S1 system_beliefs #1 |
| Written plain, a dotted literal is refused as a reference to a source the runtime does not offer. | VERIFIED | Judged in a design: a plain si.artifact.list is reported as rooted in si, which execution does not offer. | S1 system_beliefs #2 |
| Written in quotes, a dotted literal is accepted as a literal by one rule and refused by the other, which admits a literal only as a single word or an inline list or mapping. | VERIFIED | The rooting rule passes any source opening with a quote. The form rule admits an input only as a reference, a single word, or a value opening with a bracket or brace. Judged in a design, a quoted si.artifact.list is refused as not a form the runtime resolves. | S1 system_beliefs #3 |
| No spelling of a dotted literal satisfies both rules. | VERIFIED | Plain, it fails the rooting rule. Quoted, it fails the form rule. Wrapped in brackets, it is a list and no longer the value. The two rules also disagree on numbers and on qualified identities, which the rooting rule treats as literals and the form rule refuses. | S1 system_beliefs #4 |
| Every contract that observes the composition binds a dotted literal, so no design can redeclare one. | VERIFIED | Both contracts in force that observe the composition, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 and transformation::CC_JUDGE_AGAINST_COMPOSITION_V1, hand each observing step an operation name such as si.artifact.list. The boundary contracts of the inspection domain carry such names too, in a register these rules do not judge. | S1 system_beliefs #5 |
| A phase workflow hands its judging contract the rule set the generator seals into it. | VERIFIED | Each phase workflow names its judging contract with a rule-set input whose value the generator writes when it seals the workflow. | S1 system_beliefs #6 |
| A generated value left unbound is refused as missing, and bound to a description is refused as malformed. | VERIFIED | Judged in a design: an unbound rule-set input is reported as an input the contract requires and the workflow does not hand it; a description in its place is refused by the form rule. | S1 system_beliefs #7 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Judges a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 | Carries the Design Intent's rule set, including every rule that judges a binding, and renders its verdict. | PARTIAL | Holds two rules that disagree about what a literal is, and no statement for a generated value. |
| Judges a document against the composition | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | Composes the reading and the judging with the facts the snapshot answers. | EXACT | Nothing here; it is what a design cannot redeclare. |
| Judges an analysis loop against the composition | transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | Composes the reading and the judging with the declarations the composition holds. | EXACT | Nothing here; it is what a design cannot redeclare. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Two rules disagree about what a literal is. | CRITICAL | A dotted literal, a number or a qualified identity has no admissible spelling, so no design can redeclare a contract that binds one. | VERIFIED | S1 system_beliefs #4 |
| Nothing states that a generator determines a value. | CRITICAL | A design cannot redeclare a workflow whose rule set a generator seals without leaving an input unstated or stating something false. | VERIFIED | S1 system_beliefs #7 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The rooting rule already defines a literal: no dot, a qualified identity, a number, or a value opening with a quote, bracket or brace. The form rule restates a narrower definition. | The rooting rule's exemptions and the form rule's input pattern, read side by side. | VERIFIED | S1 requested_outcomes #1 |
| The molecule bindings carry their own form rule, which admits numbers and an empty quoted value but no other quoted value. | The molecule form rule's pattern. | VERIFIED | S1 business_invariants #1 |
| Earlier designs never met the defect, because they extended the generated workflows and contracts rather than replacing them, and extended artifacts are not redeclared through these registers. | The designs that touched these artifacts extended them and named their generator. | VERIFIED | S1 system_beliefs #5 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The molecule bindings define a literal a third way. One meaning across every rule that judges a binding reaches them too. | The molecule form rule's pattern differs from both step-binding rules. | MAJOR | VERIFIED | S1 business_invariants #1 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
