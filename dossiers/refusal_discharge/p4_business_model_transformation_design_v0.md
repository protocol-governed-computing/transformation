# Stage 4 — Business Model: transformation / design
**Stage:** 4 — Business Model
**CR:** refusal_discharge
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

The canonical consolidation. Nothing here is re-litigated; every row is carried from a finding the
analysis loop closed.

---

## 1. Business Model

<!-- register:actors business_language -->
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The business | States the operations it refuses and the condition for each. | Declaring — a refusal is the business's own rule and nobody else's. | S1 authority_boundaries #2 |
| The design | States what carries each declared refusal out, or who will. | Answering — it accounts for what the business declared. | S1 authority_boundaries #3 |
| The rules that judge a design | Refuse a design that leaves a declared refusal unaccounted for, or accounts for it in a way the design does not support. | Refusing — the authority of the design subdomain is to refuse. | S1 subdomain_purpose |

<!-- register:bm_entities business_language -->
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Refusal | An operation the business states it will not perform, and the condition under which it will not. | Declared once in the seed and restated in the change request. | S2 entities #1 |
| Act | Something the business does as one unit, which completes or is refused. | Declared by a design in its execution topology. | S2 entities #2 |
| Step | One part of an act, which returns an outcome the act routes on. | One row of the topology, typed and routed. | S2 entities #3 |
| Ending | Where an act stops, either completing it or refusing it. | A node of the topology, typed. | S2 entities #5 |
| Discharge | The act, step and outcome that carry a declared refusal out. | Nothing states one today. | S2 entities #6 |
| Deferral | A declared refusal this change does not carry out, with the owner who will. | Nothing states one for a refusal today. | S2 entities #7 |

<!-- register:resources optional business_language -->
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A refusal was accounted for | A design states what discharges a declared refusal, or who it is deferred to | What the business refuses becomes designed behaviour a reviewer can read. | S1 business_events #1 |
| A design was refused for an unaccounted refusal | A design reaches the design intent phase with a declared refusal it says nothing about | The omission is caught where a reviewer sees it rather than when the act runs. | S1 business_events #2 |
| A design was refused for a discharge that does not hold | A design names a step its act does not have, or an outcome that does not refuse | A stated discharge that would not stop the operation is not a discharge. | S1 business_events #3 |

<!-- register:relationships optional business_language -->
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Design | accounts for | Refusal | State what discharges a declared refusal, or who it is deferred to. | S3 authoring_decisions #1 |
| Discharge | names | Step | Hold a discharge to the act and step it names. | S3 authoring_decisions #5 |
| Step | routes to | Ending | Hold a discharge's outcome to an ending that refuses. | S3 authoring_decisions #6 |
| Rules | read | Refusal | Give the design intent phase the seed. | S3 authoring_decisions #7 |

---

## 2. Capability Graph

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Stating what discharges a declared refusal | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The register the whole change turns on. |
| Refusing a design that leaves a declared refusal unaccounted for | S3 authoring_decisions #3 | CRITICAL | GAP-2 | The closure the composition already has one layer down. |
| Stating that a refusal is deferred, and to whom | S3 authoring_decisions #2 | HIGH | GAP-3 | Without it, a change inheriting a refusal must either carry it or stay silent. |
| Holding a discharge to the act and step it names | S3 authoring_decisions #5 | HIGH | GAP-4 | A register read only for presence documents intent and enforces nothing. |
| Holding a discharge's outcome to an ending that refuses | S3 authoring_decisions #6 | HIGH | GAP-5 | A step whose failing outcome routes onward does not refuse the operation. |
| Refusing a discharge or deferral naming a refusal the business never declared | S3 authoring_decisions #4 | MEDIUM | GAP-6 | The second half of coverage; without it a design may account for refusals nobody approved. |
| Giving the design intent phase the seed | S3 authoring_decisions #7 | CRITICAL | GAP-7 | The phase cannot refuse what it cannot see. |
| Reading a prior's rows across several registers | S3 analysis_findings Q6 | HIGH | GAP-8 | Coverage spans two registers and the kind that asks it reads one. |

---

## 3. Dependency Graph

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| design | design | data read | SATISFIED | S3 dependency_discoveries #2 — the execution topology states every fact a discharge is checked against. |
| design | design | capability call | EXTEND | S3 dependency_discoveries #1 — the design intent phase must declare the seed as a prior, as two phases already do. |
| design | design | capability call | EXTEND | S3 dependency_discoveries #3 — the kind that checks a prior's rows arrived is widened to read several registers. |

---

## 4. Constraint Register

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | A discharge is stated in a register, never inferred from a citation. | S1 constraints #1 | Business author |
| 2 | A discharge names the act, the step and the outcome. | S1 constraints #2 | Business author |
| 3 | A stated discharge is checked against the design's own topology. | S1 constraints #3 | Business author |
| 4 | No discharge or deferral names a refusal the business did not declare. | S1 constraints #4 | Business author |
| 5 | A deferral names its owner. | S1 constraints #5 | Business author |
| 6 | A design that declares no refusals is judged exactly as it is today. | S1 acceptance_criteria #5 | Business author |
| 7 | The judging artifacts are re-emitted by their generator, never written by hand. | S2 pps_baseline_fqdns #5 | Governance |

---

## 5. Gap Register

<!-- register:gap_register -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|------------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Stating what discharges a declared refusal | design | AUTHOR_NEW |
| GAP-2 | S3 authoring_decisions #3 | Refusing a design that leaves a declared refusal unaccounted for | design | EXTEND |
| GAP-3 | S3 authoring_decisions #2 | Stating that a refusal is deferred, and to whom | design | AUTHOR_NEW |
| GAP-4 | S3 authoring_decisions #5 | Holding a discharge to the act and step it names | design | AUTHOR_NEW |
| GAP-5 | S3 authoring_decisions #6 | Holding a discharge's outcome to an ending that refuses | design | AUTHOR_NEW |
| GAP-6 | S3 authoring_decisions #4 | Refusing a discharge or deferral naming a refusal the business never declared | design | REUSE |
| GAP-7 | S3 authoring_decisions #7 | Giving the design intent phase the seed | design | EXTEND |
| GAP-8 | S3 analysis_findings Q6 | Reading a prior's rows across several registers | design | EXTEND |

---

## 6. Design Decisions

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The refusals are read from the seed, not carried forward through the intermediate phases. | S3 analysis_findings Q1 | The phase that must refuse cannot see them, and two phases already declare the seed directly. Carrying the register forward would add three registers and three carry rules to restate what the seed already says, and every intermediate copy can drift. | The design intent phase declares the seed among its priors. |
| 2 | A discharge is stated in its own register, and a deferral in another. | S3 analysis_findings Q5 | One table holding both leaves several cells empty on every row, and a blank meaning *not applicable* is indistinguishable from a blank meaning *unanswered*. | Two registers, read together only where the question is coverage. |
| 3 | A refusing ending is one typed as a plain exit; a completing one is typed as a success exit. | S3 analysis_findings Q3 | The design already types every node, and across the corpus the two kinds of ending are typed distinctly. Nothing is invented and nothing new is published. | A discharge's outcome must route to a node typed as a plain exit. |
| 4 | A deferral is held to the seed and to naming an owner, not to a scope record. | S3 analysis_findings Q4 | Neither the authoring scope nor the seed's authority deferrals is keyed to a refusal, so a deferral cannot resolve into either. | A deferred refusal must be one the business declared, and must name an owner. |
| 5 | Grounding a discharge in the topology is one rule; grounding its outcome in a refusing ending is another. | S3 analysis_findings Q7 | The first is one traversal of one register and splitting it would report one defect twice; the second reads a different row and makes a different claim. | Two check kinds rather than one or three. |
| 6 | The coverage kind is widened rather than duplicated. | S3 analysis_findings Q6 | The kind that resolves a cell against another register already accepts a list of targets, added for the same reason. An optional list defaulting to today's single register leaves every existing rule identical. | Every existing rule using that kind must be unchanged, and proved so. |
| 7 | Every new rule is proved by a probe built to fail it. | S3 analysis_findings Q8 | No document in the corpus states a discharge, so each rule would otherwise report clean while checking nothing. | The probes are part of the change, not a step someone may skip. |

---

## 7. Authoring Scope

<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|------------|------------------|
| Stating what discharges a declared refusal | GAP-1 |
| Refusing a design that leaves a declared refusal unaccounted for | GAP-2 |
| Stating that a refusal is deferred, and to whom | GAP-3 |
| Holding a discharge to the act and step it names | GAP-4 |
| Holding a discharge's outcome to an ending that refuses | GAP-5 |
| Refusing a discharge or deferral naming a refusal the business never declared | GAP-6 |
| Giving the design intent phase the seed | GAP-7 |
| Reading a prior's rows across several registers | GAP-8 |
