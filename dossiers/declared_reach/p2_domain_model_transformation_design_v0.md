# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** declared_reach
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, the design language as it
stands, and the change that is blocked on this one. What was searched is recorded, not only what was
found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Act | Something the business does as one unit, which completes or is refused. | Declared by a design, rendered by construction. | VERIFIED | S1 business_vocabulary #1 |
| Reach | An act reading records another part of the business owns. | The platform carries one; no design states one. | NOT_FOUND | S1 business_vocabulary #2 |
| Binding | What connects an act to the descriptions of the records it works against. | One per act in a design; several admitted by the platform. | VERIFIED | S1 business_vocabulary #3 |
| Owned | The records an act writes, described by whoever answers for them. | Stated by a design, one per act. | VERIFIED | S1 business_vocabulary #4 |
| Consulted | The records an act reads and never writes. | Nothing in a design says which these are. | NOT_FOUND | S1 business_vocabulary #5 |
| Derivation | A fact read from the composition rather than restated in a design. | Used by several rules already. | VERIFIED | S1 business_vocabulary #7 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Act | The binding it owns | Where its own records live. | VERIFIED | S1 system_beliefs #1 |
| Act | The bindings it consults | Which other records it reads. | NOT_FOUND | S1 system_beliefs #1 |
| Binding | The records it covers | What an act reaches through it. | VERIFIED | S1 system_beliefs #4 |
| Capability | The records it reads | What an act performing it must have declared. | VERIFIED | S1 system_beliefs #4 |
| Operation | Whether it reads or writes | What makes a read distinguishable from a write. | VERIFIED | S1 system_beliefs #4 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Designing an act that reads only its own records | The person raising a change | A design stating one binding, judged and rendered as it is today. | VERIFIED | S1 system_beliefs #1 |
| Designing an act that reads another part's records | The person raising a change | A design with nowhere to state the reach, which is where the change stops. | VERIFIED | S1 system_beliefs #3 |
| Judging a design for what it reaches | The rules that judge a design | Nothing about storage reach, because a design cannot state one. | VERIFIED | S1 system_beliefs #5 |
| Delivering a change to a phase's rule set | The person making the change | A generated document, which the lifecycle can now name a generator for and never has. | VERIFIED | S1 system_beliefs #6 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Designing an act that reads another part's records | 1 | State the binding the act owns. | The design's storage declaration. | VERIFIED | S1 system_beliefs #1 |
| Designing an act that reads another part's records | 2 | State the bindings it consults. | Nothing — there is no register for it. | NOT_FOUND | S1 requested_outcomes #1 |
| Designing an act that reads another part's records | 3 | Have construction render the reach into the built act. | Nothing — construction renders what the design states. | NOT_FOUND | S1 requested_outcomes #2 |
| Judging a design for what it reaches | 1 | Derive which records the act's composed capabilities read. | Available, from what the composition publishes. | VERIFIED | S1 system_beliefs #4 |
| Judging a design for what it reaches | 2 | Compare that against the reaches the design declared. | Nothing — there are no declared reaches to compare against. | NOT_FOUND | S1 requested_outcomes #3 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| A design states one binding per act and has no register for a second. | VERIFIED | The design language declares one runtime binding per act, naming the storage that resolves its records, and construction renders exactly that. No register in any phase carries a second binding, and no column distinguishes one an act owns from one it reads. | S1 system_beliefs #1 |
| The platform admits an act that declares the bindings it consults, and refuses a write through one. | VERIFIED | `runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0` §2a states the resolution model, `runtime_binding::INVARIANT_RB_STORAGE_SUBDOMAIN_OWNED_V0` holds a binding to describing only its own subdomain's records, and a workflow may declare the bindings it consults. The composition resolves them together and refuses a write to a consulted record when the act runs. | S1 system_beliefs #2 |
| A change exists that needs a reach, is raised and pinned, and stops where it would state one. | VERIFIED | `blockchain/cr_dossiers/cr_04_wallet` is raised and pinned to this same composition. Its act `blockchain::WF_CREATE_WALLET_V0` reuses `blockchain::CC_RESOLVE_ACTOR_V0`, which reads records `blockchain::STRUCTURE_IDENTITY_STORAGE_V0` describes; its own binding names `blockchain::STRUCTURE_WALLET_STORAGE_V0`. It halts on its second step, and its P0 records that it must not be hand-delivered. | S1 system_beliefs #3 |
| The composition publishes which records a binding covers, and which records a composed capability reads. | VERIFIED | `si.store.list` gives every store with the structure that declares it and the bindings that reach it; `si.store.show` gives each store's bindings with the contracts that consume them; `si.capability.surface` gives each contract's steps with the store each addresses and each operation's declared effect. Read and write are distinguishable without inference. | S1 system_beliefs #4 |
| The rules that judge a design already refuse a reach in one direction, and have no counterpart for storage. | VERIFIED | `CROSS_SUBDOMAIN_REACH_READ_ONLY` refuses an act that reaches a writing contract across a subdomain boundary, working from the published contract surface and each operation's effect. Nothing equivalent exists for the records an act reads. | S1 system_beliefs #5 |
| The document that judges a design is produced by a generator rather than written. | VERIFIED | `transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0` carries a sealed rule set produced from a template and a declaration read together, and `emit_rule_sets --check` compares the two. The lifecycle can name a generator in a design, and no change has ever used that. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Judges a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Declares what a design must state and renders a verdict. | PARTIAL | Asks nothing about the records an act reads, because a design cannot state them. |
| Judges a mandate | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | Declares the build order and closes the dossier. | PARTIAL | Schedules what construction renders, which does not include a reach. |
| Renders artifacts from a design | transformation::CT_PURE_RENDER_ARTIFACTS_V0 | Emits every artifact a mandate schedules, from the design that determines it. | PARTIAL | Renders one binding per act; nothing carries a second. |
| Evaluates a phase's rules | transformation::CT_PURE_EVALUATE_RULES_V0 | Applies a declared rule set to a parsed design and reports every rule that failed. | EXACT | Nothing — a new rule is a declaration it applies unchanged. |
| Judges a document against the composition | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Passes the composition's published facts to the rules that need them. | PARTIAL | Passes what the phases declare they observe; a rule needing store facts needs them declared. |
| States the resolution model | runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0 | Declares what an act may reach and whose description is authoritative. | EXACT | Nothing — this change states in a design what that constitution admits. |
| Holds a binding to its own records | runtime_binding::INVARIANT_RB_STORAGE_SUBDOMAIN_OWNED_V0 | Refuses a binding naming another subdomain's description. | EXACT | Nothing. It closes the copy; this change opens the declaration. |
| The act that needs it | blockchain::WF_CREATE_WALLET_V0 | Creates a wallet for an accepted person. | MISMATCH | Stops on its second step until its change request can state a reach. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A design has no register for the bindings an act consults. | CRITICAL | A change needing a reach cannot state it, and the ways available are all ungoverned. | VERIFIED | S1 system_beliefs #1 |
| Construction renders no reach, because a design states none. | CRITICAL | What a design declares and what the built act carries would not match. | NOT_FOUND | S1 requested_outcomes #2 |
| No rule refuses an act that reads records it declared no reach to. | CRITICAL | The defect stays invisible until the act runs, which is what it did. | NOT_FOUND | S1 requested_outcomes #3 |
| No rule refuses a reach nothing uses. | MAJOR | A permission granted for nothing, that nothing would notice. | NOT_FOUND | S1 requested_outcomes #4 |
| The rules that judge a design are not passed what the composition publishes about stores. | MAJOR | A rule that cannot see its subject reports nothing and looks like a rule that checked. | VERIFIED | S1 system_beliefs #4 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Everything the rules need is already published; nothing new has to be observed about the world. Which records a binding covers, which contracts consume them, and whether an operation reads or writes are all declared facts. | Three published surfaces answer all three questions. | VERIFIED | S1 system_beliefs #4 |
| The design layer must be *passed* those facts, which is a separate thing from their being published. A rule reads what its phase declares it observes, and the phase that judges a design declares two surfaces today. | The judging contract passes what each phase declares, and a phase that declares nothing about stores gets nothing. | VERIFIED | S1 system_beliefs #4 |
| The shape this change needs already exists one direction over. A rule refuses an act reaching a writing contract across a boundary, derived from the same published facts. | That rule reasons from the contract surface and each operation's effect. | VERIFIED | S1 system_beliefs #5 |
| The platform half is delivered and unused. The capability exists, is proven against a real composition, and no act declares a reach — this change is what lets one. | The composition seals a reach for no act today. | VERIFIED | S1 system_beliefs #2 |
| This change amends a generated document, and the capability for that was delivered and never used. A design can name the generator an artifact is produced from, and no change has. | The rule set is produced from a template and a declaration, and the generator is invocable from a design. | VERIFIED | S1 system_beliefs #6 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The easy delivery is the ungoverned one. Adding the reach to the built act by hand works, passes every check, and was done once already as a probe before being reverted. | The act ran correctly with a hand-added declaration, and every check passed. | CRITICAL | VERIFIED | S1 known_facts #7 |
| A rule that is not passed the facts it needs reports nothing and is indistinguishable from a rule that checked. This has happened three times in recent changes, twice in one week. | A rule read observations nobody passed it and returned no findings. | CRITICAL | VERIFIED | S1 system_beliefs #4 |
| A change to a phase's rule set has never been delivered through the pipeline, so the path this change would take has never been exercised end to end. | The capability exists and no change has used it. | MAJOR | VERIFIED | S1 system_beliefs #6 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
