# Stage 1 — Change Request: Clarification & Fact Capture: transformation / build
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|---------|-------------------------------------------------------------------|---------|--------------|
| build | MODIFY | The measure of whether a design determines its artifacts counts the facts the renderer asks for, so a fact the renderer supplies from its own text is invisible to it. Two artifacts were written carrying facts nobody designed, and the measure read complete. What the measure counts is restated against what the artifact needs. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Design | The approved statement of what is to be built. | CR seed §2 Business Vocabulary #1 |
| Mandate | The approved statement of what is to be built in what order. | CR seed §2 Business Vocabulary #2 |
| Rendering | Producing an artifact from what the design states. | CR seed §2 Business Vocabulary #3 |
| Determined fact | Something about an artifact that the design states. | CR seed §2 Business Vocabulary #4 |
| Invented fact | Something about an artifact the renderer supplies from its own text, from a path, or from anywhere but the design. | CR seed §2 Business Vocabulary #5 |
| The measure | The count of how much of an artifact the design determines. | CR seed §2 Business Vocabulary #6 |
| Complete | Every fact the measure counts is determined; below it, nothing is written. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A fact an artifact carries is stated by the design or the design is refused. | CR seed §3 Requested Outcomes #1 |
| A vocabulary's group name and spelling rule are stated by the design that schedules it. | CR seed §3 Requested Outcomes #2 |
| Nothing is written that the mandate did not schedule. | CR seed §3 Requested Outcomes #3 |
| A domain is named by a design, never inferred from where a change sits. | CR seed §3 Requested Outcomes #4 |
| The measure counts what the artifact needs, not what the renderer asks for. | CR seed §3 Requested Outcomes #5 |
| An artifact that is rendered is admissible when it is next built. | CR seed §3 Requested Outcomes #6 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A fact the design does not state is one the renderer must invent. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A renderer that invents design is a second design authority nobody approved. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| The measure refuses anything below complete, and nothing is written unless everything can be. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A vocabulary was written under a group name taken from the renderer's own text. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| The same group name and spelling rule are applied to every vocabulary the renderer will ever write. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| The spelling rule applied says upper case and the designed values are lower case. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The platform refused that vocabulary when the composition was next built. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A build manifest was written for a subdomain, declaring it a business domain importing the platform. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| That subdomain is part of the platform, and the manifest was inferred from where the change sat. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| The mandate scheduled one artifact and two were written. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| The measure read complete in both cases. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| What the measure counts is derived from the shape the renderer emits, so a fact the renderer does not ask for cannot be counted. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| Construction had never written to disk before, so an invented fact was previously absorbed by a hand-written artifact. | HIGH | CR seed §4 Known Facts — Business Truths #13 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The population the measure counts is derived from the renderer rather than from the artifact. | The whole of this change. | Establish how the population is determined, and confirm the two can only ever agree. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| A vocabulary's group name and spelling rule are literals in the renderer. | One instance. | Confirm both, and confirm no design may state either. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| A build manifest is written when the renderer judges the domain to have none. | The other instance. | Establish what decides that the domain has none, and what supplies the domain's name. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| No design register carries a group name, a spelling rule or a domain name. | Says whether the fix adds registers or reuses ones that exist. | Establish, for each invented fact, whether any register could have carried it. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Every family the renderer writes may carry invented facts, not only these two. | Says whether this is two instances or a pattern across the renderer. | Establish, for every family, which of its rendered facts come from the design and which from the renderer. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| Nothing else was written that the mandate did not schedule. | Bounds what one emit produced. | Compare what was written against what the mandate scheduled, for both changes emitted so far. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| The literals were written when one shape was the only shape, and were never revisited. | The group name is the one a result status would carry, and the first vocabularies rendered were of that kind. | CR seed §6 Assumptions #1 |
| A design's author would have stated the missing facts had there been anywhere to state them. | The same author stated every fact the design did ask for, and measured complete. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| The measure keeps its threshold; a design below complete still writes nothing. | Business author | CR seed §7 Constraints #1 |
| A fact is added to what the measure counts, never removed to make a design pass. | Business author | CR seed §7 Constraints #2 |
| Nothing is written that the mandate did not schedule. | Business author | CR seed §7 Constraints #3 |
| A renderer supplies no fact from a path, a directory or a dossier's location. | Business author | CR seed §7 Constraints #4 |
| An artifact that is rendered is admissible to the platform, or the rendering is wrong. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every fact an artifact carries is stated by the design that determines it. | CR seed §8 Business Invariants #1 |
| The measure counts what the artifact needs. | CR seed §8 Business Invariants #2 |
| Nothing is written that the mandate did not schedule. | CR seed §8 Business Invariants #3 |
| No fact is derived from where a file or a dossier sits. | CR seed §8 Business Invariants #4 |
| A rendered artifact is admissible to the platform that will build it. | CR seed §8 Business Invariants #5 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Design | Under-determined | The design does not state everything its artifacts need, and the measure says so. | CR seed §9 Lifecycle States #1 |
| Design | Determined | The design states everything its artifacts need. | CR seed §9 Lifecycle States #2 |
| Design | Measured complete and under-determined | The measure reads complete and the renderer still invents. This is the state this change ends. | CR seed §9 Lifecycle States #3 |
| Artifact | Rendered and inadmissible | Written from a design, and refused by the platform that built it. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A design was measured | Before anything is written | The design determines its artifacts, or nothing is written. | CR seed §10 Business Events #1 |
| An artifact was written | When a design measures complete | What the design states becomes the artifact. | CR seed §10 Business Events #2 |
| An artifact was written carrying a fact nobody designed | Today, whenever a renderer sources a fact from its own text | The artifact has an author the approval never named. | CR seed §10 Business Events #3 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What an artifact needs | The family the artifact belongs to | CR seed §11 Authority Boundaries #1 |
| What the measure counts | The build subdomain | CR seed §11 Authority Boundaries #2 |
| What a design states | The design that states it | CR seed §11 Authority Boundaries #3 |
| Which domain an artifact belongs to | The design that schedules it | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| What any particular design should state | Each change's business. | CR seed §12 Out of Scope #1 |
| The rule set each phase declares | The design subdomain's own concern; this one is about what construction does with an approved design. | CR seed §12 Out of Scope #2 |
| The artifacts already written by the two emits | Corrected by re-rendering once the design can state what they need. | CR seed §12 Out of Scope #3 |
| Whether construction should write to disk at all | Settled; it does, and that is what made the invented facts visible. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| build | MODIFIED | CR seed §13 Governance Scope #1 |
| design | ADJACENT | CR seed §13 Governance Scope #2 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| Is a build manifest something a design ever schedules, or something outside construction entirely? | Decides whether the manifest gains a design that determines it or is removed from what construction writes. | NO | GOVERNANCE | CR seed §14 Clarification Requests #1 |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| A design that does not state a vocabulary's group name or spelling rule is refused. | CR seed §15 Acceptance Criteria #1 |
| A design that states them renders a vocabulary the platform admits. | CR seed §15 Acceptance Criteria #2 |
| The vocabulary that was refused is rendered admissible from a design that states what it needs. | CR seed §15 Acceptance Criteria #3 |
| No artifact is written that the mandate did not schedule. | CR seed §15 Acceptance Criteria #4 |
| A design naming no domain is refused rather than having one inferred. | CR seed §15 Acceptance Criteria #5 |
| Every fact each family carries is either stated by a design or refused, and the list is readable. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Determined fact | The artifact it belongs to and its name within it | Both are equal. | CR seed §16 Identity and Sameness #1 |
| Rendered artifact | The identity the design gives it | Two renderings carry one identity. | CR seed §16 Identity and Sameness #2 |
| The measure | The design it measures | One design has one measurement. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Design | Measured complete and under-determined | Under-determined | The measure counting a fact the renderer used to supply. | Designs that read complete now read short, and each states the fact it was never asked for. | CR seed §17 Lifecycle Transitions #1 |
| Design | Under-determined | Determined | Its author stating the fact. | The artifact is rendered carrying what the design says, and is admissible where it was refused. | CR seed §17 Lifecycle Transitions #2 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Rendering an artifact | The design does not state a fact the artifact carries | A fact the design does not state is one the renderer invents, and an artifact with an author nobody approved is not a governed artifact. | CR seed §18 Operation Refusals #1 |
| Writing a construction | An artifact was produced that the mandate did not schedule | A mandate freezes scope, and something written outside it was never approved by anyone. | CR seed §18 Operation Refusals #2 |
| Rendering an artifact | Its domain would have to be inferred from where a file or a dossier sits | A domain read from a path is a domain nobody declared, and moving a file would silently change what was built. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| The rule set each phase declares | design | A fact this change adds needs a phase to carry it, and that phase's rules are that subdomain's to state. | CR seed §19 Authority Deferrals #1 |
| What a build manifest is and who determines it | A ruling | The clarification this seed raises is answered. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
