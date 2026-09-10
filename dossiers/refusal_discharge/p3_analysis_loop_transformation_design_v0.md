# Stage 3 — Analysis Loop: transformation / design
**Stage:** 3 — Analysis Loop
**CR:** refusal_discharge
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Each gap Stage 2 recorded was worked until the question stopped producing new answers. Both open
questions are closed, and closing the first changed the shape of the change: the refusals are read
from the seed, not carried forward through four phases.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status | Confidence | Resolution Status | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The phase that must refuse an unaccounted refusal cannot see the refusals, and can be given them the way two phases already are. | Decides whether this change adds one register or carries a register through four phases. | OBSERVED | HIGH | CLOSED | Each phase declares which earlier documents it is judged against. The design intent phase declares the business intent and governance intent phases. Two phases already declare the seed directly and skip everything between: business intent reads the seed because it transforms it rather than restating it, and governance intent reads the seed alongside business intent. Declaring the seed at design intent is the same move, already made twice. |
| Q2 | The refusals should be read from the seed rather than the change request. | Decides which document the rules are grounded in. | OBSERVED | HIGH | CLOSED | The seed is the business's own words and the change request restates them; two rules already hold the restatement to the seed, row for row, in both directions. Grounding the discharge in the seed means the design is answerable to what the business wrote rather than to a copy of it, and it costs nothing, because the copy is already proved identical. |
| Q3 | A refusing ending is distinguishable from a completing one by the type the design already declares. | Decides whether the outcome half of a discharge is checkable at all. | OBSERVED | HIGH | CLOSED | The execution topology types every node, and endings carry two distinct types: one for the ending that completes the act and one for every other. Across the corpus, a completing ending is typed as a success exit and a refusing ending is typed as a plain exit. So an outcome routes to a refusal exactly when the node it names is typed as a plain exit, which the design states and no rule needed to invent. |
| Q4 | A deferral cannot be grounded in an existing scope record, and does not need to be. | Decides how a deferred refusal is held to something. | OBSERVED | HIGH | CLOSED | The business model's authoring scope is keyed on a capability and a gap, and the seed's authority deferrals are keyed on a business object. Neither is keyed to a refusal, so a deferral cannot resolve to a row in either. What a deferral must be held to is the thing the business actually said: that the refusal was declared, and that an owner is named. Both are checkable — the first against the seed, the second as a required cell. |
| Q5 | Two registers rather than one with a column telling them apart. | Decides the shape a design states a discharge in. | INFERRED | HIGH | CLOSED | A discharged refusal names an act, a step and an outcome; a deferred one names an owner and a condition. One table holding both would leave three cells empty on every row of one kind and one empty on every row of the other, and a blank that means *not applicable* is indistinguishable from a blank that means *unanswered* — the failure a rule set spent a session auditing. Two registers, and the two are read together only where the question is coverage. |
| Q6 | The coverage question spans two registers, and the kind that asks it reads one. | Decides whether this change authors a new check kind or widens an existing one. | OBSERVED | HIGH | CLOSED | The kind that checks a prior's rows arrived reads a single register. The kind that resolves a cell against another register already accepts several targets, added for exactly this reason: a code may legitimately be declared in either of two places. Widening the first the same way — an optional list defaulting to the single register it reads today — leaves every existing rule identical and asks the question the business asked, which is whether a refusal is accounted for anywhere. |
| Q7 | Grounding a discharge in the topology is one question, not two. | Decides how many check kinds this change authors. | INFERRED | MEDIUM | CLOSED | A discharge names an act, a step and an outcome. Checking that the step belongs to the act and that the outcome is one the step reports is a single traversal of one register, and splitting it would report one defect as two findings on the same row. The second question — whether that outcome leads to a refusal — reads a different row of the same register and is a different claim, so it is its own kind. |
| Q8 | No design in the corpus states a discharge, so every new rule will report clean on its first run. | Decides how the rules are proved. | OBSERVED | HIGH | CLOSED | The register does not exist, so no dossier can have populated it. Four rules in the previous change reported clean for exactly this reason and two of them then found a real defect on their first real subject. Each rule here is proved by a probe built to fail it, and the probes are part of the change. |

---

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result | Evidence |
|------|--------|--------|----------|
| The refusals a business declares are carried from the seed into the change request and checked for arrival, and no phase after that reads them. | S2 belief_verification #1 | CONFIRMED | Twelve rules against the register at the seed and the change request; zero at every phase after. |
| A design can be judged admissible at every phase while a declared refusal is carried out by nothing. | S2 belief_verification #2 | CONFIRMED | Zero rules against the register in the sealed rule sets for P2 through P7, so no design could fail on this ground. |
| A change request declared four refusals and one became nothing at all, and the act ran and did the thing the business refused. | S2 belief_verification #3 | CONFIRMED | The delivery record of that change states the refusal travelled nine phases as prose, that no branch existed for a person held but not accepted, and that the act ran. |
| That change has since been re-authored and all four refusals are now discharged, and three of the four cite something other than the refusal. | S2 belief_verification #4 | CONFIRMED | Four branches in the current topology, and one of the four rows citing the refusal. |
| A design states its acts, their steps and each step's outcomes, and which ending each outcome routes to. | S2 belief_verification #5 | CONFIRMED | Every node is typed and every outcome names the node it leads to, so both halves of a discharge are checkable against the design alone. |
| A phase's declared scope records what the change defers and to whom. | S2 belief_verification #6 | OVERTURNED | The scope records exist but neither is keyed to a refusal, so a deferral cannot resolve into one. What the business requires is met by naming an owner and holding the row to the seed. |
| The composition refuses to seal an obligation nothing is bound to, and the build stops rather than shipping one. | S2 belief_verification #7 | CONFIRMED | The invariant is published, governed, enforced at meta-validation with immediate failure, and was met by a real change. |
| The document that judges a design is produced by a generator rather than written. | S2 belief_verification #8 | CONFIRMED | The generation provenance register names the artifact, its generator and that generator sources, and one change has been delivered that way. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition | Evidence |
|------------|------|-------------|----------|
| The seed's refusal register, as a prior of the design intent phase | data read | EXTEND | The phase declares which priors it reads; this change adds the seed to that declaration, as two phases already do. |
| The design's execution topology | data read | EXISTING | Already stated by every design that declares an act, and the only thing a discharge is checked against. |
| The kind that checks a prior's rows arrived | capability call | EXTEND | Widened to read several registers, defaulting to the one it reads today. |
| The kind that confines a register's rows to a prior's | capability call | REUSE | Applied unchanged to each of the two new registers. |
| The generator that produces a phase's rule set | capability call | REUSE | Invoked to re-emit the judging artifacts; nothing is written by hand. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Re-emitted from the generator with five rules and two registers added, and its declared priors extended by the seed. | 1 | The judging contract reads it; nothing else does. |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Unchanged in substance. A discharge is checked against the design, so no new composition fact is observed. | 1 | It passes observations to the rules; this change declares none. |
| The design intent template | Two registers appended, after the last existing section. | Every future design | A section number must be an integer, so a register is appended rather than placed by subject. |
| Every existing dossier | Unaffected. A change declaring no refusals has nothing to account for, and the registers admit an empty declaration. | 8 | The rules are driven by the seed's rows; with none, they have no subjects. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions -->
| Capability | Decision | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Stating what discharges a declared refusal | AUTHOR_NEW | No register anywhere states it, and the design intent phase is where acts, steps and outcomes exist. | Reading it from citations, rejected because a citation is written where an author found it natural; extending the storage or topology registers, rejected because a discharge is a claim about a refusal rather than about a node. | S2 gaps #1 |
| Stating that a refusal is deferred, and to whom | AUTHOR_NEW | A refusal owned by someone else must be answerable, and silence is what this change removes. | Overloading the discharge register with a disposition column, rejected at Q5; grounding the deferral in an existing scope record, overturned at Q4. | S2 gaps #4 |
| Refusing a design that leaves a declared refusal unaccounted for | EXTEND | The kind that checks a prior's rows arrived does exactly this, for one register; the question spans two. | Authoring a new kind, rejected because it would duplicate a kind that differs only in reading a list where it reads a scalar. | S2 gaps #2 |
| Refusing a discharge or deferral naming a refusal the business never declared | REUSE | The kind that confines a register's rows to a prior's answers it unchanged, once per register. | Nothing else was needed. | S2 gaps #2 |
| Holding a discharge to the act and step it names | AUTHOR_NEW | No kind reads an act, a step and an outcome together against the topology. | The kind that resolves a cell against another register, rejected because it would confirm the step exists somewhere and not that it belongs to the act named. | S2 gaps #3 |
| Holding a discharge's outcome to an ending that refuses | AUTHOR_NEW | No kind asks where an outcome leads, and an outcome routing onward does not refuse. | Folding it into the kind above, rejected at Q7 because it is a claim about a different row. | S2 gaps #3 |
| Giving the design intent phase the seed | EXTEND | The rules must read the refusals the business declared, and the phase does not see them today. | Carrying the register forward through the business model, business intent and governance intent phases, rejected because it would add three registers and three carry rules to say what the seed already says, and every intermediate copy is a copy that can drift. | S3 analysis_findings Q1 |

---

## 6. Placement Decision

<!-- register:placement_decision -->
| Decision | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | The change is entirely in how a design is judged: two registers of the design intent phase, five rules, two check kinds and one prior declaration. Nothing is built, rendered or executed. | S2 pps_baseline_fqdns #3 |

---

## 7. Discovery Saturation

<!-- register:saturation -->
| Criterion | Status | Evidence |
|-----------|--------|----------|
| Every belief carried from the change request is resolved | SATISFIED | Eight beliefs, all verified against the sealed composition and the corpus. |
| Every gap has an authoring decision | SATISFIED | Four gaps, seven decisions; no gap is left to the design phase to invent. |
| Every open question the domain model raised is closed | SATISFIED | Both closed at Q1 and Q4, one of them by overturning the assumption behind it. |
| The change needs no fact that is not already published or stated | SATISFIED | Every check reads the design's own registers or the seed. |
| Each new rule has a way of being proved that does not depend on the corpus | SATISFIED | A probe per rule, built to fail, because no existing document states a discharge. |
| No further question changes the shape of the change | SATISFIED | The last question that did was Q1, and it removed three registers from the change rather than adding any. |
