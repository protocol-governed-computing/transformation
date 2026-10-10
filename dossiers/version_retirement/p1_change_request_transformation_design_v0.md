# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** version_retirement
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
| design | MODIFY | Every replaced version of a phase workflow or contract is carried in the live tree though nothing runs it, because the checks assume a replaced version stays. This declares when a replaced version is retained, lets one be deleted by a recorded act, and deletes the domain's versions nothing needs. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Replaced version | An artifact a successor supersedes, stood down and no longer run. | CR seed §2 Business Vocabulary #1 |
| Retention condition | A reason the standard gives to keep a replaced version: something still names it, or a sealed composition containing it is still relied on. | CR seed §2 Business Vocabulary #2 |
| Retention | Keeping a replaced version in the live tree. | CR seed §2 Business Vocabulary #3 |
| Deletion | Removing a replaced version from the live tree by a recorded human act. | CR seed §2 Business Vocabulary #4 |
| Deletion record | What a deletion states: the deleted identity, the person who decided, and the determination that no retention condition held. | CR seed §2 Business Vocabulary #5 |
| Release | A sealed composition, archived at its tag and cited by its DOI. | CR seed §2 Business Vocabulary #6 |
| Stable baseline | The declared point at which development ends and retention conditions begin to bind. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| When a replaced version is retained is declared once, where every check reads it: during development, nothing in the live tree is retained for its own sake. | CR seed §3 Requested Outcomes #1 |
| A replaced version can be deleted by a recorded human act, the record naming what the standard requires. | CR seed §3 Requested Outcomes #2 |
| Every check accepts a deletion so recorded, and refuses one that is not recorded. | CR seed §3 Requested Outcomes #3 |
| A deleted name is never used again. | CR seed §3 Requested Outcomes #4 |
| The stood-down versions of this domain that nothing needs are deleted, each with its record. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A change of meaning is a new identity, and a replaced version names its successor before it goes. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A superseded thing is retained only while a retention condition holds; once none holds, a person may delete it by a governed act. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| The platform is in development, and no release is a stable baseline yet. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A consumer of a release uses the release, at its tag, and no consumer depends on the live tree. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A sealed release keeps every identity it holds. | HIGH | CR seed §4 Known Facts — Business Truths #5 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Thirty-three artifacts in the live tree are stood down, across eight domains, and nothing executes them. | It sizes what is carried. | Count the stood-down artifacts by domain, and establish whether anything runs one. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The check that a published identity still means what it meant treats an identity the live tree no longer holds as a finding. | It forbids any published version from leaving. | Confirm how the check treats an identity missing from the live tree. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The check that each supersession is stated the same way on both sides needs both sides present. | It forbids deleting either side. | Confirm what the check does when one side is absent. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The check that every transform's implementation exists keeps the code of a stood-down transform alive. | It forbids retiring code a stood-down transform names. | Confirm whether the check distinguishes a stood-down transform. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| A stood-down artifact that names another keeps that one alive too, so one replacement holds a chain. | It is why a deletion is never local. | Trace the chains of stood-down artifacts in this domain. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| Two stood-down judging contracts, bound by seven stood-down phase workflows, still name the readers the format change replaces. | It is what blocks the format change. | Trace what names the readers the format change replaces. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |
| Nothing records a deletion, and nothing states when retention applies. | It is why retention is assumed in code. | Establish whether any artifact or check records a deletion or declares retention. | CR seed §5 Existing-System Beliefs — Requiring Verification #7 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| NONE IDENTIFIED |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| The standard does not change. It already bounds retention and defines deletion. This change realizes it. | Business author | CR seed §7 Constraints #1 |
| Identity and succession stay mandatory. A change of meaning is still a new identity, and a replaced version still names its successor before it goes. | Business author | CR seed §7 Constraints #2 |
| A deleted name is never reused. Releases are cited by the identities they hold. | Business author | CR seed §7 Constraints #3 |
| Releases are untouched. A sealed release keeps every identity it holds, at its tag. | Business author | CR seed §7 Constraints #4 |
| Development ends at a declared point. When a stable baseline is declared, retention conditions begin to bind, by changing the declaration rather than the code. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A replaced version leaves the live tree only by a recorded deletion. | CR seed §8 Business Invariants #1 |
| A deleted name is never used again. | CR seed §8 Business Invariants #2 |
| A change of meaning is a new identity. | CR seed §8 Business Invariants #3 |
| When retention applies is declared once, and every check reads that declaration. | CR seed §8 Business Invariants #4 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Artifact version | Current | It is run, or it is what the live tree names. | CR seed §9 Lifecycle States #1 |
| Artifact version | Stood down | A successor supersedes it, and it is carried in the live tree. | CR seed §9 Lifecycle States #2 |
| Artifact version | Deleted | It is gone from the live tree, its deletion is on record, and its name is retired. | CR seed §9 Lifecycle States #3 |
| Development | Open | No stable baseline is declared, and nothing is retained for its own sake. | CR seed §9 Lifecycle States #4 |
| Development | Closed | A stable baseline is declared, and retention conditions bind. | CR seed §9 Lifecycle States #5 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A version was replaced | A change of meaning authors a successor | The predecessor is stood down and names its successor. | CR seed §10 Business Events #1 |
| A version was deleted | A person decides no retention condition holds and removes it | The record names the identity, the person and the determination, and the name is retired. | CR seed §10 Business Events #2 |
| A stable baseline was declared | A person declares the end of development | Retention conditions begin to bind. | CR seed §10 Business Events #3 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Deciding a deletion | A person | CR seed §11 Authority Boundaries #1 |
| Declaring a stable baseline | A person | CR seed §11 Authority Boundaries #2 |
| The versions of this domain | design | CR seed §11 Authority Boundaries #3 |
| A sealed release | The published record | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| What retention conditions apply after development | That is decided when a stable baseline is declared. | CR seed §12 Out of Scope #1 |
| The form a phase document carries its facts in | That is the format change, which waits for this one. | CR seed §12 Out of Scope #2 |
| Declaring the first stable baseline | That is a later change. | CR seed §12 Out of Scope #3 |
| Deleting other domains' stood-down versions | Each domain deletes its own, in its own change, under the declaration this change makes. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| design | MODIFIED | CR seed §13 Governance Scope #1 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| NONE IDENTIFIED |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| When a replaced version is retained is declared once, and every check that assumed retention reads the declaration. | CR seed §15 Acceptance Criteria #1 |
| A replaced version deleted with its record passes every check. | CR seed §15 Acceptance Criteria #2 |
| A replaced version removed without a record is refused. | CR seed §15 Acceptance Criteria #3 |
| A name that was deleted cannot be used again. | CR seed §15 Acceptance Criteria #4 |
| The stood-down versions of this domain that nothing needs are gone from the live tree, each with its record. | CR seed §15 Acceptance Criteria #5 |
| A sealed release still holds every identity it was sealed with. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Artifact version | Its identity, name and version together | Their identities are the same, whether or not either is still in the live tree. | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Artifact version | Current | Stood down | A change of meaning authoring its successor | What named it is re-pointed at the successor. | CR seed §17 Lifecycle Transitions #1 |
| Artifact version | Stood down | Deleted | A person deciding no retention condition holds | The record is written and the name is retired. Nothing live may still name it. | CR seed §17 Lifecycle Transitions #2 |
| Development | Open | Closed | A person declaring a stable baseline | Retention conditions begin to bind. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Removing a replaced version | No deletion record names it | A version leaves the live tree only by a recorded human act. | CR seed §18 Operation Refusals #1 |
| Naming a new artifact | The name was deleted | A deleted name is never used again. | CR seed §18 Operation Refusals #2 |
| Deleting a version | Something live still names it | A deletion leaves nothing pointing at a version that is gone. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| What retention conditions apply after development | The declaration of a stable baseline | A stable baseline is declared. | CR seed §19 Authority Deferrals #1 |
| Other domains' stood-down versions | Each domain's own change | Each domain makes it. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
