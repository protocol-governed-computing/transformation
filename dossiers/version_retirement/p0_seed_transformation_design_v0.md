# Change Seed — transformation / design

**Stage:** 0 — Change Seed
**CR:** version_retirement
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Design subdomain judges each document of the transformation lifecycle against the rule set its
phase declares, through phase workflows and the contracts they run. Those workflows and contracts
change as the lifecycle changes, and each replaced version is stood down. The subdomain governs what
a document must say at each phase, the verdict it receives, and the artifacts that render it.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| design | MODIFY | Every replaced version of a phase workflow or contract is carried in the live tree though nothing runs it, because the checks assume a replaced version stays. This declares when a replaced version is retained, lets one be deleted by a recorded act, and deletes the domain's versions nothing needs. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Replaced version | An artifact a successor supersedes, stood down and no longer run. |
| Retention condition | A reason the standard gives to keep a replaced version: something still names it, or a sealed composition containing it is still relied on. |
| Retention | Keeping a replaced version in the live tree. |
| Deletion | Removing a replaced version from the live tree by a recorded human act. |
| Deletion record | What a deletion states: the deleted identity, the person who decided, and the determination that no retention condition held. |
| Release | A sealed composition, archived at its tag and cited by its DOI. |
| Stable baseline | The declared point at which development ends and retention conditions begin to bind. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| When a replaced version is retained is declared once, where every check reads it: during development, nothing in the live tree is retained for its own sake. |
| A replaced version can be deleted by a recorded human act, the record naming what the standard requires. |
| Every check accepts a deletion so recorded, and refuses one that is not recorded. |
| A deleted name is never used again. |
| The stood-down versions of this domain that nothing needs are deleted, each with its record. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A change of meaning is a new identity, and a replaced version names its successor before it goes. | HIGH |
| A superseded thing is retained only while a retention condition holds; once none holds, a person may delete it by a governed act. | HIGH |
| The platform is in development, and no release is a stable baseline yet. | HIGH |
| A consumer of a release uses the release, at its tag, and no consumer depends on the live tree. | HIGH |
| A sealed release keeps every identity it holds. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Thirty-three artifacts in the live tree are stood down, across eight domains, and nothing executes them. | It sizes what is carried. | Count the stood-down artifacts by domain, and establish whether anything runs one. |
| The check that a published identity still means what it meant treats an identity the live tree no longer holds as a finding. | It forbids any published version from leaving. | Confirm how the check treats an identity missing from the live tree. |
| The check that each supersession is stated the same way on both sides needs both sides present. | It forbids deleting either side. | Confirm what the check does when one side is absent. |
| The check that every transform's implementation exists keeps the code of a stood-down transform alive. | It forbids retiring code a stood-down transform names. | Confirm whether the check distinguishes a stood-down transform. |
| A stood-down artifact that names another keeps that one alive too, so one replacement holds a chain. | It is why a deletion is never local. | Trace the chains of stood-down artifacts in this domain. |
| Two stood-down judging contracts, bound by seven stood-down phase workflows, still name the readers the format change replaces. | It is what blocks the format change. | Trace what names the readers the format change replaces. |
| Nothing records a deletion, and nothing states when retention applies. | It is why retention is assumed in code. | Establish whether any artifact or check records a deletion or declares retention. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| The standard does not change. It already bounds retention and defines deletion. This change realizes it. | Business author |
| Identity and succession stay mandatory. A change of meaning is still a new identity, and a replaced version still names its successor before it goes. | Business author |
| A deleted name is never reused. Releases are cited by the identities they hold. | Business author |
| Releases are untouched. A sealed release keeps every identity it holds, at its tag. | Business author |
| Development ends at a declared point. When a stable baseline is declared, retention conditions begin to bind, by changing the declaration rather than the code. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A replaced version leaves the live tree only by a recorded deletion. |
| A deleted name is never used again. |
| A change of meaning is a new identity. |
| When retention applies is declared once, and every check reads that declaration. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Artifact version | Current | It is run, or it is what the live tree names. |
| Artifact version | Stood down | A successor supersedes it, and it is carried in the live tree. |
| Artifact version | Deleted | It is gone from the live tree, its deletion is on record, and its name is retired. |
| Development | Open | No stable baseline is declared, and nothing is retained for its own sake. |
| Development | Closed | A stable baseline is declared, and retention conditions bind. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A version was replaced | A change of meaning authors a successor | The predecessor is stood down and names its successor. |
| A version was deleted | A person decides no retention condition holds and removes it | The record names the identity, the person and the determination, and the name is retired. |
| A stable baseline was declared | A person declares the end of development | Retention conditions begin to bind. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Deciding a deletion | A person |
| Declaring a stable baseline | A person |
| The versions of this domain | design |
| A sealed release | The published record |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| What retention conditions apply after development | That is decided when a stable baseline is declared. |
| The form a phase document carries its facts in | That is the format change, which waits for this one. |
| Declaring the first stable baseline | That is a later change. |
| Deleting other domains' stood-down versions | Each domain deletes its own, in its own change, under the declaration this change makes. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| design | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| When a replaced version is retained is declared once, and every check that assumed retention reads the declaration. |
| A replaced version deleted with its record passes every check. |
| A replaced version removed without a record is refused. |
| A name that was deleted cannot be used again. |
| The stood-down versions of this domain that nothing needs are gone from the live tree, each with its record. |
| A sealed release still holds every identity it was sealed with. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Artifact version | Its identity, name and version together | Their identities are the same, whether or not either is still in the live tree. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Artifact version | Current | Stood down | A change of meaning authoring its successor | What named it is re-pointed at the successor. |
| Artifact version | Stood down | Deleted | A person deciding no retention condition holds | The record is written and the name is retired. Nothing live may still name it. |
| Development | Open | Closed | A person declaring a stable baseline | Retention conditions begin to bind. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Removing a replaced version | No deletion record names it | A version leaves the live tree only by a recorded human act. |
| Naming a new artifact | The name was deleted | A deleted name is never used again. |
| Deleting a version | Something live still names it | A deletion leaves nothing pointing at a version that is gone. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| What retention conditions apply after development | The declaration of a stable baseline | A stable baseline is declared. |
| Other domains' stood-down versions | Each domain's own change | Each domain makes it. |
