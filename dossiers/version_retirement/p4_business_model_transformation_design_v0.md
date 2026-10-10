# Stage 4 — Business Model: transformation / design
**Stage:** 4 — Business Model
**CR:** version_retirement
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Person deciding a deletion | Determines that no retention condition holds and removes a replaced version. | Deciding — the sole authority for a deletion. | S1 authority_boundaries #1 |
| Person declaring a stable baseline | Declares the end of development. | Deciding — the sole authority for when retention conditions bind. | S1 authority_boundaries #2 |
| Workspace checks | Compare the live tree with the release, with each supersession and with the record of deletions. | Checking — decide nothing; refuse what is not recorded. | S1 system_beliefs #2 |

<!-- register:bm_entities business_language -->
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Replaced version | An artifact a successor supersedes, stood down and no longer run. | An artifact in the live tree whose declaration names its successor. | S2 entities #1 |
| Retention condition | A reason the standard gives to keep a replaced version: something still names it, or a sealed composition containing it is still relied on. | Stated in the standard; nothing in the platform declares or checks one. | S2 entities #2 |
| Retention | Keeping a replaced version in the live tree. | Assumed by the checks; declared nowhere. | S2 entities #3 |
| Deletion | Removing a replaced version from the live tree by a recorded human act. | One removal is named in the published-identity check's own code, with a reason. | S2 entities #4 |
| Deletion record | What a deletion states: the deleted identity, the person who decided, and the determination that no retention condition held. | The one named removal states an identity and a reason, and no deciding person. | S2 entities #5 |
| Release | A sealed composition, archived at its tag and cited by its DOI. | The sealed v5 composition, held in the release repository at its tag. | S2 entities #6 |
| Stable baseline | The declared point at which development ends and retention conditions begin to bind. | Nothing declares one. | S2 entities #7 |

<!-- register:resources optional business_language -->
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The retention declaration | One file of the workspace process, read by every check, stating when a replaced version is retained. | S3 analysis_findings Q1 |
| The ledger of deletions | One file of the workspace process recording each deletion as the standard requires. | S3 analysis_findings Q2 |

<!-- register:events business_language -->
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A version was replaced | A change of meaning authors a successor | The predecessor is stood down and names its successor. | S1 business_events #1 |
| A version was deleted | A person decides no retention condition holds and removes it | The record names the identity, the person and the determination, and the name is retired. | S1 business_events #2 |
| A stable baseline was declared | A person declares the end of development | Retention conditions begin to bind. | S1 business_events #3 |

<!-- register:relationships optional business_language -->
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Workspace checks | read | Retention declaration | Declaring when a replaced version is retained. | S3 authoring_decisions #1 |
| Ledger | records | Deletion | Recording a deletion. | S3 authoring_decisions #2 |
| Workspace checks | accept | Deletion record | Accepting a recorded deletion in every check that assumed retention. | S3 authoring_decisions #3 |
| Deletion | releases | Implementation | Releasing a stood-down transform's code. | S3 authoring_decisions #4 |
| Workspace checks | refuse | Retired name | Refusing a deleted name used again. | S3 authoring_decisions #5 |
| Person deciding a deletion | deletes | Replaced version | Deleting this domain's stood-down versions. | S3 authoring_decisions #6 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|------------|----------------|--------|--------------------|-------|
| Declaring when a replaced version is retained | S3 authoring_decisions #1 | CRITICAL | GAP-1 | One declaration every check reads. |
| Recording a deletion | S3 authoring_decisions #2 | CRITICAL | GAP-2 | One ledger, carrying what the standard requires. |
| Accepting a recorded deletion in every check that assumed retention | S3 authoring_decisions #3 | CRITICAL | GAP-3 | The published-identity and supersession checks read the ledger. |
| Refusing a deleted name used again | S3 authoring_decisions #5 | CRITICAL | GAP-4 | Reuse and dangling references are refused by one check. |
| Deleting this domain's stood-down versions | S3 authoring_decisions #6 | CRITICAL | GAP-5 | Eleven deletions, each recorded. |
| Releasing a stood-down transform's code | S3 authoring_decisions #4 | SATISFIED |  | Deleting the transform releases it; the implementation check is unchanged. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| NONE IDENTIFIED |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | A replaced version leaves the live tree only by a recorded deletion. | S1 business_invariants #1 | invariant |
| 2 | A deleted name is never used again. | S1 business_invariants #2 | invariant |
| 3 | A change of meaning is a new identity. | S1 business_invariants #3 | invariant |
| 4 | When retention applies is declared once, and every check reads that declaration. | S1 business_invariants #4 | invariant |
| 5 | The standard does not change. It already bounds retention and defines deletion. This change realizes it. | S1 constraints #1 | governance rule |
| 6 | Identity and succession stay mandatory. A replaced version still names its successor before it goes. | S1 constraints #2 | governance rule |
| 7 | Releases are untouched. A sealed release keeps every identity it holds, at its tag. | S1 constraints #4 | governance rule |
| 8 | When a stable baseline is declared, retention conditions begin to bind, by changing the declaration rather than the code. | S1 constraints #5 | governance rule |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|------------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Declaring when a replaced version is retained | design | NEW |
| GAP-2 | S3 authoring_decisions #2 | Recording a deletion | design | NEW |
| GAP-3 | S3 authoring_decisions #3 | Accepting a recorded deletion in every check that assumed retention | design | EXTEND |
| GAP-4 | S3 authoring_decisions #5 | Refusing a deleted name used again | design | EXTEND |
| GAP-5 | S3 authoring_decisions #6 | Deleting this domain's stood-down versions | design | NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Retention is declared once, in the workspace process, and during development declares that nothing is retained for its own sake. | S3 analysis_findings Q1 | Three checks assume retention, and all are workspace process. | Rules out any check deciding retention in its own code. |
| 2 | One ledger records every deletion: identity, deciding person, determination, and the change that deleted it. The removal coded in the published-identity check moves into it. | S3 analysis_findings Q2 | The standard's record is a declaration, not code. | Rules out a deletion that leaves no record. |
| 3 | The published-identity and supersession checks accept an absent identity only when the ledger records it. | S3 analysis_findings Q3 | A recorded deletion passes; an unrecorded removal is a finding. | Rules out exempting stood-down artifacts by category. |
| 4 | The implementation check is unchanged. | S3 analysis_findings Q4 | It reads only artifacts present. | Rules out teaching it about supersession. |
| 5 | A recorded identity present in the live tree is a finding, and so is a live artifact naming one, other than a successor naming its predecessor. | S3 analysis_findings Q5 | One check refuses reuse and dangling references. | Rules out deleting what something live still names. |
| 6 | A node's name in a workflow is a place, not a reference. | S3 analysis_findings Q6 | Each such node runs its successor's contract. | Rules out renaming nodes to delete their predecessors. |
| 7 | Eleven stood-down artifacts of this domain are deleted at delivery, each with its record. | S3 analysis_findings Q7 | Nothing runs them, and the release retains ten of them. | Rules out deleting another domain's artifacts here. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|------------|------------------|
| Declaring when a replaced version is retained | GAP-1 |
| Recording a deletion | GAP-2 |
| Accepting a recorded deletion in every check that assumed retention | GAP-3 |
| Refusing a deleted name used again | GAP-4 |
| Deleting this domain's stood-down versions | GAP-5 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| What retention conditions apply after development | That is decided when a stable baseline is declared. |
| Declaring the first stable baseline | That is a later change. |
| Deleting other domains' stood-down versions | Each domain deletes its own, in its own change, under the declaration this change makes. |
| The form a phase document carries its facts in | That is the format change, which waits for this one. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
