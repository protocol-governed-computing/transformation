# Stage 3 — Analysis Loop: transformation / design
**Stage:** 3 — Analysis Loop
**CR:** declared_reach
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot and the published surfaces rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The five gaps are one declaration and three checks that stand on it, plus one thing that must be handed over before any of the checks can see anything. Stating the reach is the only gap that is not a rule. | Fixes what the change delivers and the order the pieces depend on. | OBSERVED | HIGH | CLOSED | Four gaps reduce to comparisons against a declaration that does not exist yet; the fifth is that the rules are not passed the facts to compare with. |
| Q2 | The two checks are halves of one statement and neither works alone. Refusing an undeclared read permits a reach held in reserve; refusing an unused reach permits a read nobody declared. Delivered together, the declared set and the used set are the same set. | Rules out shipping either half as a smaller first pass. | OBSERVED | HIGH | CLOSED | Each check constrains one direction of the same correspondence. |
| Q3 | One thing needs publishing, and it is a shape rather than a fact. Which records a binding covers, which contracts consume them, and whether an operation reads or writes are all declared — but the binding identities reach a rule only one store at a time, and a rule is handed every store at once. So the change adds rules, no observation of the world, and one projection of what is already counted. | Adds an obligation in a second repository, and settles that it is a publication rather than a derivation. | OBSERVED | HIGH | CLOSED | The all-stores surface counts a store's bindings and does not name them; the surface that names them answers about one store, and a capability contract is a fixed pipeline with no iteration. |
| Q4 | Publishing a fact and passing it to a rule are different things, and the second is where rules have silently failed before. The phase must declare the store surface among what it observes, or every check here reports nothing and looks exactly like a check that passed. | Makes the handover an explicit part of the change rather than an assumption. | OBSERVED | HIGH | CLOSED | Rules have read observations nobody passed them three times, twice within one week. |
| Q5 | A design names a binding and derives its records, which is what keeps this change from re-creating the defect it serves. Restating another part's records inside the reaching act's design would be a copy maintained by someone other than their owner — the same shape as the storage description the platform change refused. | Settles what the register carries, and why the smaller-looking option is the wrong one. | OBSERVED | HIGH | CLOSED | The platform refuses a binding that describes another subdomain's records for exactly this reason. |
| Q6 | The delivery path is itself unexercised. The document this change amends is generated, a design can name its generator, and no change has ever done so — so the change carries a risk that has nothing to do with reach and should be expected to surface. | Names a risk that belongs to the path rather than to the design. | OBSERVED | HIGH | CLOSED | The capability was delivered and has never been used by any change. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| A design states one binding per act and has no register for a second. | S2 belief_verification #1 | CONFIRMED | Re-read: one binding per act, and no register carries a second or distinguishes owned from consulted. |
| The platform admits an act that declares the bindings it consults, and refuses a write through one. | S2 belief_verification #2 | CONFIRMED | Re-read: the model is stated, the invariant holds it, and the refusal runs. |
| A change exists that needs a reach, is raised and pinned, and stops where it would state one. | S2 belief_verification #3 | CONFIRMED | Re-read: raised, pinned to this composition, and its P0 records that it must not be hand-delivered. |
| The composition publishes which records a binding covers, and which records a composed capability reads. | S2 belief_verification #4 | CONFIRMED | Re-queried: the store surface gives bindings and consumers, the capability surface gives steps and effects. |
| The rules that judge a design already refuse a reach in one direction, and have no counterpart for storage. | S2 belief_verification #5 | CONFIRMED | Re-read: the existing rule reasons from the same published facts and addresses contracts rather than records. |
| The document that judges a design is produced by a generator rather than written. | S2 belief_verification #6 | CONFIRMED | Re-read: the rule set is generated, the generator is nameable in a design, and no change has named it. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| A register stating the bindings an act consults | declaration | AUTHOR_NEW | No register carries one. |
| The rule that an act reads nothing it did not declare | declaration | AUTHOR_NEW | Nothing compares reads against declarations. |
| The rule that every declared reach is used | declaration | AUTHOR_NEW | Nothing notices a permission granted for nothing. |
| The store surface, among what the design phase observes | mechanism | EXTEND | Published, and not passed to the phase that would use it. |
| The published facts themselves | mechanism | REUSE | Stores, their bindings and consumers, and each operation's effect are all declared. |
| The renderer that emits an act | mechanism | EXTEND | Emits one binding; must emit the reach a design states. |
| The rule that refuses a writing reach across a boundary | mechanism | REUSE | The shape this change follows, one direction over. |
| The generator that produces the judging document | mechanism | REUSE | Nameable from a design, and never named. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Gains a register and three rules, and is regenerated rather than edited. | 0 | Nothing in the composition consumes a phase; it is invoked from outside. |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Passes the store surface to the phase that judges a design. | 9 | Nine phase workflows are judged through it. |
| transformation::CT_PURE_RENDER_ARTIFACTS_V0 | Emits the reach a design states into the act it renders. | 2 | Two contracts in the build subdomain reach it. |
| Every design already written | Unchanged. An act that declares no reach is judged exactly as it is today. | 8 | Eight dossiers exist across three domains. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Stating the bindings an act consults | AUTHOR_NEW | A design cannot say it, and every way of proceeding without saying it is ungoverned. | A column on the existing storage register was rejected by the business: ownership and reach would be a typo apart, with a rule reading the column the only thing between them. | S2 gaps #1 |
| Naming a binding and deriving its records | AUTHOR_NEW | The binding is the owning part's declaration of its own records; restating them in the reaching act's design is a copy maintained by someone other than their owner. | Stating the records was rejected: it would let a rule check the reach against itself while re-creating the second copy this line of work exists to remove. | S2 gaps #1 |
| Refusing a design whose act reads records it declared no reach to | AUTHOR_NEW | It is the defect the blocked change hit, caught where a reviewer sees it rather than when the act runs. | Leaving it to the platform's run-time refusal was rejected: that refuses a *write*, and an undeclared *read* would still be invisible until execution. | S2 gaps #3 |
| Refusing a reach no read uses | AUTHOR_NEW | A permission granted for nothing is a permission whose purpose nobody reviewed. | Allowing a reserve was rejected by the business: a reach is scoped to a stated purpose. | S2 gaps #4 |
| Passing the store surface to the phase that judges a design | EXTEND | Publishing a fact and handing it to a rule are different things, and rules that were not handed their facts have reported nothing three times. | Deriving store facts inside the rule was rejected: a rule reaching past the observations its phase declares is the coupling the judging contract exists to prevent. | S2 gaps #5 |
| Emitting the reach into the built act | EXTEND | What a design states and what the act carries must be the same, or the declaration is decoration. | Leaving the reach to be added after construction was rejected: that is the hand delivery this change removes. | S2 gaps #2 |
| The published facts a rule reasons from | EXTEND | Stores, their bindings and consumers, and each operation's effect are declared, and one of them is published in a shape no rule can consume: the all-stores surface counts a store's bindings without naming them. | Asking per store was rejected: a contract is a fixed pipeline with no iteration, so a rule that had to ask store by store could not be expressed at all. Deriving the binding inside the rule was rejected for the same reason decision 5 gives. | S2 architectural_observations #1 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | design | What a design may state and what refuses it are what this subdomain governs; the rendering half is adjacent and follows what the design states. | S2 belief_verification #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | Three resolved by authoring what does not exist, and the fourth by handing a published fact to the phase that needs it. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the six raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Eight dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Six items re-grounded; all six CONFIRMED. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All six findings are OBSERVED. None rests on inference. |
