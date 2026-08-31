# Change Seed — transformation / build

**Stage:** 0 — Change Seed
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Build subdomain governs the passage from an approved design to the artifacts it determines: the
measure that decides whether a design determines them, the rendering of each artifact from what the
design states, and the writing of the result where its binding says it belongs. Its authority is to
refuse a design that does not determine what it schedules. It decides nothing about what a design
should contain.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| build | MODIFY | The measure of whether a design determines its artifacts counts the facts the renderer asks for, so a fact the renderer supplies from its own text is invisible to it. Two artifacts were written carrying facts nobody designed, and the measure read complete. What the measure counts is restated against what the artifact needs. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Design | The approved statement of what is to be built. |
| Mandate | The approved statement of what is to be built in what order. |
| Rendering | Producing an artifact from what the design states. |
| Determined fact | Something about an artifact that the design states. |
| Invented fact | Something about an artifact the renderer supplies from its own text, from a path, or from anywhere but the design. |
| The measure | The count of how much of an artifact the design determines. |
| Complete | Every fact the measure counts is determined; below it, nothing is written. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A fact an artifact carries is stated by the design or the design is refused. |
| A vocabulary's group name and spelling rule are stated by the design that schedules it. |
| Nothing is written that the mandate did not schedule. |
| A domain is named by a design, never inferred from where a change sits. |
| The measure counts what the artifact needs, not what the renderer asks for. |
| An artifact that is rendered is admissible when it is next built. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A fact the design does not state is one the renderer must invent. | HIGH |
| A renderer that invents design is a second design authority nobody approved. | HIGH |
| The measure refuses anything below complete, and nothing is written unless everything can be. | HIGH |
| A vocabulary was written under a group name taken from the renderer's own text. | HIGH |
| The same group name and spelling rule are applied to every vocabulary the renderer will ever write. | HIGH |
| The spelling rule applied says upper case and the designed values are lower case. | HIGH |
| The platform refused that vocabulary when the composition was next built. | HIGH |
| A build manifest was written for a subdomain, declaring it a business domain importing the platform. | HIGH |
| That subdomain is part of the platform, and the manifest was inferred from where the change sat. | HIGH |
| The mandate scheduled one artifact and two were written. | HIGH |
| The measure read complete in both cases. | HIGH |
| What the measure counts is derived from the shape the renderer emits, so a fact the renderer does not ask for cannot be counted. | HIGH |
| Construction had never written to disk before, so an invented fact was previously absorbed by a hand-written artifact. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The population the measure counts is derived from the renderer rather than from the artifact. | The whole of this change. | Establish how the population is determined, and confirm the two can only ever agree. |
| A vocabulary's group name and spelling rule are literals in the renderer. | One instance. | Confirm both, and confirm no design may state either. |
| A build manifest is written when the renderer judges the domain to have none. | The other instance. | Establish what decides that the domain has none, and what supplies the domain's name. |
| No design register carries a group name, a spelling rule or a domain name. | Says whether the fix adds registers or reuses ones that exist. | Establish, for each invented fact, whether any register could have carried it. |
| Every family the renderer writes may carry invented facts, not only these two. | Says whether this is two instances or a pattern across the renderer. | Establish, for every family, which of its rendered facts come from the design and which from the renderer. |
| Nothing else was written that the mandate did not schedule. | Bounds what one emit produced. | Compare what was written against what the mandate scheduled, for both changes emitted so far. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| The literals were written when one shape was the only shape, and were never revisited. | The group name is the one a result status would carry, and the first vocabularies rendered were of that kind. |
| A design's author would have stated the missing facts had there been anywhere to state them. | The same author stated every fact the design did ask for, and measured complete. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| The measure keeps its threshold; a design below complete still writes nothing. | Business author |
| A fact is added to what the measure counts, never removed to make a design pass. | Business author |
| Nothing is written that the mandate did not schedule. | Business author |
| A renderer supplies no fact from a path, a directory or a dossier's location. | Business author |
| An artifact that is rendered is admissible to the platform, or the rendering is wrong. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every fact an artifact carries is stated by the design that determines it. |
| The measure counts what the artifact needs. |
| Nothing is written that the mandate did not schedule. |
| No fact is derived from where a file or a dossier sits. |
| A rendered artifact is admissible to the platform that will build it. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Design | Under-determined | The design does not state everything its artifacts need, and the measure says so. |
| Design | Determined | The design states everything its artifacts need. |
| Design | Measured complete and under-determined | The measure reads complete and the renderer still invents. This is the state this change ends. |
| Artifact | Rendered and inadmissible | Written from a design, and refused by the platform that built it. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A design was measured | Before anything is written | The design determines its artifacts, or nothing is written. |
| An artifact was written | When a design measures complete | What the design states becomes the artifact. |
| An artifact was written carrying a fact nobody designed | Today, whenever a renderer sources a fact from its own text | The artifact has an author the approval never named. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What an artifact needs | The family the artifact belongs to |
| What the measure counts | The build subdomain |
| What a design states | The design that states it |
| Which domain an artifact belongs to | The design that schedules it |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| What any particular design should state | Each change's business. |
| The rule set each phase declares | The design subdomain's own concern; this one is about what construction does with an approved design. |
| The artifacts already written by the two emits | Corrected by re-rendering once the design can state what they need. |
| Whether construction should write to disk at all | Settled; it does, and that is what made the invented facts visible. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| build | MODIFIED |
| design | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| Is a build manifest something a design ever schedules, or something outside construction entirely? | Decides whether the manifest gains a design that determines it or is removed from what construction writes. | NO | GOVERNANCE |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A design that does not state a vocabulary's group name or spelling rule is refused. |
| A design that states them renders a vocabulary the platform admits. |
| The vocabulary that was refused is rendered admissible from a design that states what it needs. |
| No artifact is written that the mandate did not schedule. |
| A design naming no domain is refused rather than having one inferred. |
| Every fact each family carries is either stated by a design or refused, and the list is readable. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Determined fact | The artifact it belongs to and its name within it | Both are equal. |
| Rendered artifact | The identity the design gives it | Two renderings carry one identity. |
| The measure | The design it measures | One design has one measurement. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Design | Measured complete and under-determined | Under-determined | The measure counting a fact the renderer used to supply. | Designs that read complete now read short, and each states the fact it was never asked for. |
| Design | Under-determined | Determined | Its author stating the fact. | The artifact is rendered carrying what the design says, and is admissible where it was refused. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Rendering an artifact | The design does not state a fact the artifact carries | A fact the design does not state is one the renderer invents, and an artifact with an author nobody approved is not a governed artifact. |
| Writing a construction | An artifact was produced that the mandate did not schedule | A mandate freezes scope, and something written outside it was never approved by anyone. |
| Rendering an artifact | Its domain would have to be inferred from where a file or a dossier sits | A domain read from a path is a domain nobody declared, and moving a file would silently change what was built. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| The rule set each phase declares | design | A fact this change adds needs a phase to carry it, and that phase's rules are that subdomain's to state. |
| What a build manifest is and who determines it | A ruling | The clarification this seed raises is answered. |
