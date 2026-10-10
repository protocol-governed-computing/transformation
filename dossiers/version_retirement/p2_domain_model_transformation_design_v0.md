# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** version_retirement
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the live tree, the pinned snapshot, the sealed
release and the checks that read them. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Replaced version | An artifact a successor supersedes, stood down and no longer run. | An artifact in the live tree whose declaration names its successor. | VERIFIED | S1 business_vocabulary #1 |
| Retention condition | A reason the standard gives to keep a replaced version: something still names it, or a sealed composition containing it is still relied on. | Stated in the standard; nothing in the platform declares or checks one. | NOT_FOUND | S1 business_vocabulary #2 |
| Retention | Keeping a replaced version in the live tree. | Assumed by the checks; declared nowhere. | VERIFIED | S1 business_vocabulary #3 |
| Deletion | Removing a replaced version from the live tree by a recorded human act. | One removal is named in the published-identity check's own code, with a reason. | VERIFIED | S1 business_vocabulary #4 |
| Deletion record | What a deletion states: the deleted identity, the person who decided, and the determination that no retention condition held. | The one named removal states an identity and a reason, and no deciding person. | VERIFIED | S1 business_vocabulary #5 |
| Release | A sealed composition, archived at its tag and cited by its DOI. | The sealed v5 composition, held in the release repository at its tag. | VERIFIED | S1 business_vocabulary #6 |
| Stable baseline | The declared point at which development ends and retention conditions begin to bind. | Nothing declares one. | NOT_FOUND | S1 business_vocabulary #7 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Replaced version | Successor | The version that supersedes it. | VERIFIED | S1 business_vocabulary #1 |
| Deletion record | Deciding person | Who decided the deletion. | NOT_FOUND | S1 business_vocabulary #5 |
| Deletion record | Determination | That no retention condition held. | NOT_FOUND | S1 business_vocabulary #5 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Replacing a version | A change of meaning | The predecessor is stood down, names its successor, and what named it is re-pointed. | VERIFIED | S1 business_events #1 |
| Deleting a version | A person | The identity is removed and named in a check's code with a reason. | VERIFIED | S1 business_events #2 |
| Declaring a stable baseline | A person | Nothing: no declaration exists. | NOT_FOUND | S1 business_events #3 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Replacing a version | 1 | Author the successor, naming the predecessor. | The successor's declaration. | VERIFIED | S1 business_events #1 |
| Replacing a version | 2 | Stand the predecessor down, naming the successor. | The predecessor's declaration. | VERIFIED | S1 business_events #1 |
| Replacing a version | 3 | Re-point what named the predecessor. A workflow keeps the node's name and changes what it runs. | The re-pointed declarations. | VERIFIED | S1 business_events #1 |
| Deleting a version | 1 | Remove the identity and name it, with a reason, in the published-identity check. | A line in the check's code. | VERIFIED | S1 business_events #2 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Thirty-three artifacts in the live tree are stood down, across eight domains, and nothing executes them. | VERIFIED | 33 counted: transformation 11, blockchain 10, execution_topology 3, and capability_transforms, workload, book_library_mgmt and ai_governance 2 each, trace 1. No live artifact runs one. Nine are spelled by live workflows as the names of nodes that run their successors. | S1 system_beliefs #1 |
| The check that a published identity still means what it meant treats an identity the live tree no longer holds as a finding. | VERIFIED | Every identity of the sealed v5 composition that the working composition lacks is a finding, unless the check's own code names it as removed, with a reason. | S1 system_beliefs #2 |
| The check that each supersession is stated the same way on both sides needs both sides present. | VERIFIED | It reads every successor's predecessors and every predecessor's successors; a successor naming a predecessor that is absent is reported as one that does not name it back. | S1 system_beliefs #3 |
| The check that every transform's implementation exists keeps the code of a stood-down transform alive. | VERIFIED | It reads every transform artifact in the tree, stood down or not, and requires each named module on disk. | S1 system_beliefs #4 |
| A stood-down artifact that names another keeps that one alive too, so one replacement holds a chain. | VERIFIED | In this domain, seven stood-down phase workflows bind two stood-down judging contracts, which name the two readers. | S1 system_beliefs #5 |
| Two stood-down judging contracts, bound by seven stood-down phase workflows, still name the readers the format change replaces. | VERIFIED | `transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0` and `transformation::CC_JUDGE_AGAINST_COMPOSITION_V0` each bind both readers; the phase workflows for phases 2 to 8 at version 0 bind them. | S1 system_beliefs #6 |
| Nothing records a deletion, and nothing states when retention applies. | NOT_FOUND | A deletion is recorded: the published-identity check names one removal in its code, with a reason, and the change log describes it. It names no deciding person, and it covers only identities the release published. Nothing states when retention applies. | S1 system_beliefs #7 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Judges a document against the composition | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0 | Stood down; succeeded by its version 1. | MISMATCH | Run: nothing binds it but stood-down workflows. |
| Judges an analysis loop against the composition | transformation::CC_JUDGE_AGAINST_COMPOSITION_V0 | Stood down; succeeded by its version 1. | MISMATCH | The same. |
| Judges a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 | Stood down; succeeded by its version 2. | MISMATCH | Run: no intent starts it. |
| Rates a document's figure of merit | transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V0 | Stood down; succeeded by its version 1. | MISMATCH | Govern: nothing reads it. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Nothing declares when a replaced version is retained. | CRITICAL | Retention is assumed by three checks, and no decision can change it. | VERIFIED | S1 system_beliefs #7 |
| A deletion record lives in a check's code and names no deciding person. | CRITICAL | A deletion is a code edit, not a declared act, and the standard's record is incomplete. | VERIFIED | S1 system_beliefs #7 |
| The supersession check cannot tell a recorded deletion from a missing artifact. | CRITICAL | No predecessor can be deleted while its successor names it. | VERIFIED | S1 system_beliefs #3 |
| The implementation check does not know an artifact is stood down. | MAJOR | A stood-down transform's code can never be retired. | VERIFIED | S1 system_beliefs #4 |
| Nothing refuses a deleted name used again. | MAJOR | A new artifact could take a retired identity, and a citation would change meaning. | VERIFIED | S1 constraints #3 |
| Nothing declares a stable baseline. | MINOR | The end of development is undated, but nothing depends on it yet. | VERIFIED | S1 constraints #5 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A re-pointed workflow keeps a node's name and changes what it runs, so a live workflow spells a stood-down identity as a place name. Nine stood-down identities are spelled this way. | Each such node's name is the predecessor's code and its contract is the successor. | VERIFIED | S1 system_beliefs #1 |
| The one existing deletion record is code in a check, written by hand, and covers only identities the release published. A deletion of an identity never published leaves no record anywhere. | The check's removal list, and the change log entry it cites. | VERIFIED | S1 system_beliefs #7 |
| Releases hold every identity they were sealed with, independently of the live tree. Two stood-down artifacts were never released, so deleting either leaves it in no archive: the design phase's workflow at its version 1, and the Collatz workload's termination contract at its version 1. | The sealed v5 composition holds 31 of the 33 stood-down artifacts, and both readers the format change replaces; it lacks transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 and workload::CC_VERIFY_TERMINATION_V1. | VERIFIED | S1 known_facts #5 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Whether a node's name counts as naming an artifact decides whether nine stood-down identities can be deleted and whether their names are reused. | Nine live nodes are named with stood-down identities. | MAJOR | VERIFIED | S1 business_invariants #2 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
