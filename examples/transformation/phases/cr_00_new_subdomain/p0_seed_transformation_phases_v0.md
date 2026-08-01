# CR Seed — transformation / phases

The human-provided elicitation that P1 consumes, reorganized faithfully from
`p0_business_problem_statement.md`. Human input only — no agent-derived content.

- **Domain:** transformation
- **Primary subdomain:** phases — NEW
- **Secondary subdomain:** none
- **CR version:** V0

---

## Subdomain Purpose (foundational business context)

The Phases subdomain governs how a proposed change to a composition is carried from a person's
problem statement to a decision about whether it may proceed. It owns the pipeline itself: what each
phase consumes and produces, which rules decide admissibility, and who is accountable at each gate.
Other parts of the platform govern what a composition contains; this subdomain governs how a
composition is allowed to change.

---

## 1. CR Type

**NEW_SUBDOMAIN** — `transformation/phases`.
Rationale: the pipeline that decides which changes are admissible is a distinct concern from the
capabilities it admits, and needs its own governance boundary. It extends nothing that exists.

## 2. Business Vocabulary

| Term | Definition |
|------|------------|
| Phase | One governed step of the change pipeline, with declared inputs, outputs and rules. |
| Seed | The business problem statement reorganized into fixed registers, and the only input later phases accept. |
| Seed Phase | The first phase: it turns a person's problem statement into a seed. |
| Rule Set | The declared set of conditions that decide whether a seed is admissible. Governance, not implementation. |
| Check Mechanism | A means of performing one kind of condition test. Implementation; carries no judgement about what should be tested. |
| Verdict | The outcome of applying the rule set to a seed: admissible or inadmissible. There is no partial pass. |
| Finding | One recorded failure of one rule, naming the rule, where it failed, and why that matters. |
| Gate | A point where a person accepts responsibility before the pipeline continues. |
| Author of Record | The person accountable for a seed's content. |
| Business Truth | Something the business authoritatively decides or requires. |
| System Belief | Something believed about what already exists, which must be verified rather than assumed. |
| Clarification | An open question that must be asked and never guessed. |

## 3. Requested Outcomes

1. Establish the seed phase as a governed capability of the platform, with its rules readable from
   the composition rather than from a build tool.
2. Produce a verdict for any offered seed, reporting every rule the seed failed rather than
   stopping at the first failure.
3. Record accountability: a person is the author of record for a seed, and a person confirms at the
   gate that it says what they meant.

## 4. Known Facts — Business Truths

| # | Fact | Certainty |
|---|------|-----------|
| 1 | The change pipeline must be governed the same way the capabilities it admits are governed. | HIGH |
| 2 | The seed phase reorganizes a problem statement; it never decides business content. | HIGH |
| 3 | A seed is either admissible or inadmissible; there is no partial pass and no warning tier. | HIGH |
| 4 | Every rule is applied to every seed; evaluation does not stop at the first failure. | HIGH |
| 5 | The rule set is governance and must be readable from the composition and versioned as declared behavior. | HIGH |
| 6 | A check mechanism is implementation and may live in code, provided it carries no judgement about what should be tested. | HIGH |
| 7 | A person is the author of record for a seed, and a person confirms it at the gate. | HIGH |
| 8 | The seed phase may not add business content the problem statement does not contain. | HIGH |
| 9 | The seed phase may not resolve an open question by guessing. | HIGH |
| 10 | The seed phase may not assign any design. | HIGH |
| 11 | The seed phase may not promote a System Belief into a Business Truth. | HIGH |
| 12 | Changing the rule set requires the same governed change process as any other declared behavior. | HIGH |
| 13 | This change establishes the seed phase and its rule set only. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

| # | Belief (suspected) | Why it matters | Verification Goal |
|---|---------------------|----------------|-------------------|
| 1 | No capability in the current composition decides seed admissibility. | This CR exists to fill that gap; if such a capability exists, the CR scope changes. | Confirm no existing capability produces a seed verdict. |
| 2 | A capability for declaring pure, deterministic transforms already exists. | The check mechanisms are pure transforms and should reuse it rather than author a new form. | Identify the governing declaration for pure capability transforms and its purity obligations. |
| 3 | A capability for declaring governed calls already exists, and forbids orchestration logic inside them. | Determines whether a rule can be a governed call or must be data the phase evaluates. | Identify the governing declaration for capability contracts and what it forbids. |
| 4 | A workflow form already exists that composes governed calls as a fixed graph without iteration. | Determines how the phase applies many rules to many registers. | Identify the workflow declaration and confirm whether iteration is available to it. |
| 5 | An actor form already exists for recording accountability. | The author of record and the gate reviewer are actors. | Identify the actor declaration and how a workflow binds one. |
| 6 | A form for declaring rules as data, separate from the mechanism that enforces them, already exists. | If so, the rule set should reuse it rather than invent a carrier. | Identify how existing rules are declared apart from their enforcement, and whether that form fits a rule set applied to a document. |
| 7 | Vocabulary extension is restricted to specific declared categories. | Determines whether the controlled vocabularies of the seed may be declared as vocabulary. | Identify what may be extended as vocabulary and what may not. |
| 8 | The platform's existing content is largely infrastructure rather than business capability. | Establishes what this subdomain can legitimately reuse. | Identify which existing capabilities are reuse candidates for a pipeline subdomain. |

## 6. Assumptions

| Assumption | Basis |
|------------|-------|
| The seed template's section structure is stable and will not change while this CR is in flight. | It is fixed by the reference elicitation already in use. |
| A person can supply every register by hand, so the pipeline never depends on an automated drafter. | Stated release constraint. |

## 7. Constraints

| Constraint | Source |
|------------|--------|
| What is checked, and why, must be readable from the composition; only how a check runs may live in code. | Business policy |
| The pipeline is reachable only from a local command line, not over any network boundary. | Business policy |
| Dossiers are evidence about a composition and must never become part of one. | Business policy |
| A verdict must be reproducible: the same seed and the same rule set always give the same verdict. | Business policy |

## 8. Business Invariants

| # | Invariant |
|---|-----------|
| 1 | A seed has exactly one verdict. |
| 2 | Every rule in the rule set is applied to every seed offered to the phase. |
| 3 | An inadmissible seed carries at least one finding, and an admissible seed carries none. |
| 4 | Every finding names the rule that produced it. |
| 5 | Every seed has exactly one author of record. |
| 6 | The same seed and rule set always produce the same verdict. |
| 7 | A seed that has not passed the gate is never consumed by a later phase. |

## 9. Lifecycle States

| Object | State | Meaning |
|--------|-------|---------|
| Seed | Drafted | Reorganized from a problem statement; not yet judged. |
| Seed | Admissible | The rule set found no findings. |
| Seed | Inadmissible | At least one finding was recorded; the seed cannot proceed. |
| Seed | Accepted | A person confirmed at the gate that it says what they meant. |
| Rule Set | Active | The declared rules currently deciding admissibility. |
| Rule Set | Superseded | Replaced by a later version through a governed change. |

## 10. Business Events

| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| Seed Offered | When a seed is submitted to the phase for judgement. | The phase has something to decide about. |
| Verdict Reached | When the rule set has been applied in full. | The seed's admissibility is established and recorded. |
| Seed Accepted | When a person confirms the seed at the gate. | Accountability is recorded and later phases may consume it. |
| Seed Rejected | When a verdict is inadmissible, or a person declines at the gate. | The change does not proceed, and the cause is recorded. |

## 11. Authority Boundaries

| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Problem Statement | The person who wrote it |
| Seed content | The author of record |
| Rule Set | Phases |
| Verdict | Phases |
| Finding | Phases |
| Gate acceptance | The gate reviewer |

## 12. Out of Scope

| Item | Reason |
|------|--------|
| The remaining phases of the pipeline. | This change establishes the seed phase only; the rest arrive as later change requests. |
| Automated drafting of a seed. | The pipeline must not depend on it; it may be added later behind the same rules. |
| Reachability over any network boundary. | The pipeline is build-time and local only. |
| Rules that require reading an existing composition. | The seed phase judges a document alone; composition-aware rules belong to later phases. |
| Deciding which parts of a composition may be reused by a later change. | A property of the analysis phase, not the seed phase. |

## 13. Governance Scope

| Scope Item | Relationship |
|------------|--------------|
| phases | CREATED |
| capability_transforms | ADJACENT |
| capability_contracts | ADJACENT |
| workflow | ADJACENT |
| intent | ADJACENT |
| runtime_binding | ADJACENT |
| governance | ADJACENT |

## 14. Clarification Requests

1. How is the rule set carried as declared data? The problem statement requires it to be readable
   from the composition and versioned as declared behavior, but does not say in what form. Belief 6
   is the discovery target; if no existing form fits a rule set applied to a document rather than to
   artifacts, this must be answered before the phase can be designed.
2. Does the phase receive the seed as text, or as a location it must read? The constraint that a
   verdict be reproducible suggests text, but the problem statement does not say.

## 15. Acceptance Criteria

1. A person can offer a seed to the phase and receive a verdict of admissible or inadmissible.
2. An inadmissible seed reports every rule it failed, not only the first.
3. The rules deciding admissibility can be read from the composition without reading any code.
4. Offering the same seed twice produces the same verdict.
5. A seed records exactly one author of record, and a gate acceptance records the person who gave it.
6. A seed that fails the gate is not consumed by any later phase.
