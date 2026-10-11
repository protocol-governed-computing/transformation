# Domain Model — transformation / phases

## Machine

```yaml
header:
  Stage: 2 — Domain Model Verification
  CR: new_subdomain
  Status: DRAFT
  Feeds: Stage 3 — Analysis Loop
registers:
  entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Evidence Status
    - Source Finding
    rows:
    - Entity: Seed
      Description: The business problem statement reorganized into fixed registers.
      Store Model: Held as a document outside the composition; never stored as protocol state.
      Evidence Status: NOT_FOUND
      Source Finding: S1 business_vocabulary Seed
    - Entity: Rule Set
      Description: The declared conditions deciding whether a document is admissible.
      Store Model: Carried as declared input on the phase workflow, sealed with it.
      Evidence Status: NOT_FOUND
      Source Finding: S1 business_vocabulary Rule Set
    - Entity: Verdict
      Description: 'The outcome of applying a rule set: admissible or inadmissible.'
      Store Model: Returned by the phase; not persisted.
      Evidence Status: NOT_FOUND
      Source Finding: S1 business_vocabulary Verdict
    - Entity: Finding
      Description: One recorded failure of one rule.
      Store Model: Returned within the verdict; not persisted.
      Evidence Status: NOT_FOUND
      Source Finding: S1 business_vocabulary Finding
    - Entity: Author of Record
      Description: The person accountable for a document's content.
      Store Model: An actor identity bound by the phase workflow.
      Evidence Status: VERIFIED
      Source Finding: S1 business_vocabulary Author of Record
  entity_attributes:
    columns:
    - Entity
    - Attribute
    - Meaning
    - Evidence Status
    - Source Finding
    rows:
    - Entity: Verdict
      Attribute: admissibility
      Meaning: Whether the document may proceed to the next phase.
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 business_invariants #1'
    - Entity: Verdict
      Attribute: rules evaluated
      Meaning: How many rules were applied — every rule, always.
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 business_invariants #2'
    - Entity: Finding
      Attribute: rule
      Meaning: The rule that produced the finding.
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 business_invariants #4'
    - Entity: Rule Set
      Attribute: active version
      Meaning: The declared rules currently deciding admissibility.
      Evidence Status: NOT_FOUND
      Source Finding: S1 lifecycle_states Rule Set
  business_processes:
    columns:
    - Process
    - Initiator
    - Outcome
    - Evidence Status
    - Source Finding
    rows:
    - Process: Judge a document
      Initiator: The author of record offering it
      Outcome: A verdict, with every failed rule reported
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 requested_outcomes #2'
    - Process: Accept at a gate
      Initiator: The gate reviewer
      Outcome: The document may be consumed by the next phase
      Evidence Status: NOT_FOUND
      Source Finding: S1 business_events Seed Accepted
  process_steps:
    columns:
    - Process
    - 'Step #'
    - Action
    - Record Produced
    - Evidence Status
    - Source Finding
    rows:
    - Process: Judge a document
      'Step #': '1'
      Action: Read the document into its registers
      Record Produced: The registers
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 requested_outcomes #2'
    - Process: Judge a document
      'Step #': '2'
      Action: Apply every declared rule
      Record Produced: The findings
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 business_invariants #2'
    - Process: Judge a document
      'Step #': '3'
      Action: Reach a verdict
      Record Produced: The verdict
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 business_invariants #1'
  belief_verification:
    columns:
    - Belief
    - Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE)
    - Evidence
    - Source Finding
    rows:
    - Belief: No capability in the current composition decides seed admissibility.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): NOT_FOUND
      Evidence: No capability produces an admissibility verdict; the only governed call in the domain is transformation::CC_JUDGE_DOCUMENT_V0, authored by this CR.
      Source Finding: 'S1 system_beliefs #1'
    - Belief: A capability for declaring pure, deterministic transforms already exists.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: capability_transforms::CT_PURE_COMPARE_EQUAL_V0, capability_transforms::CT_PURE_EXTRACT_V0
      Source Finding: 'S1 system_beliefs #2'
    - Belief: A capability for declaring governed calls already exists, and forbids orchestration logic inside them.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: transformation::CC_JUDGE_DOCUMENT_V0 composes steps in a pipeline; chaining inside a call is forbidden and enforced at compile time.
      Source Finding: 'S1 system_beliefs #3'
    - Belief: A workflow form already exists that composes governed calls as a fixed graph without iteration.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: transformation::WF_P0_SEED_ADMISSIBILITY_V0, transformation::WF_P9_IMAGINARY_V0
      Source Finding: 'S1 system_beliefs #4'
    - Belief: An actor form already exists for recording accountability.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: transformation::AC_SEED_AUTHOR_V0, transformation::AC_GATE_REVIEWER_V0, transformation::AC_REGISTER_AUTHOR_V0
      Source Finding: 'S1 system_beliefs #5'
    - Belief: A form for declaring rules as data, separate from the mechanism that enforces them, already exists.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): NOT_FOUND
      Evidence: No declaration form carries rules applied to a document; the rule set travels as declared workflow input instead.
      Source Finding: 'S1 system_beliefs #6'
    - Belief: Vocabulary extension is restricted to specific declared categories.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: Vocabulary extension contributes only to the categories a reserving declaration marks extensible; no other category admits domain entries.
      Source Finding: 'S1 system_beliefs #7'
    - Belief: The platform's existing content is largely infrastructure rather than business capability.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: The composition is dominated by constitutions, invariants and transport contracts; capability_side_effects::CS_MUTABLE_JSON_V0 and capability_transforms::CT_PURE_EXTRACT_V0 are among the few reusable mechanisms.
      Source Finding: 'S1 system_beliefs #8'
  pps_baseline_fqdns:
    columns:
    - Capability
    - FQDN
    - What It Does
    - Fit (EXACT, PARTIAL, MISMATCH)
    - Cannot Do
    rows:
    - Capability: Snapshot observation
      FQDN: capability_side_effects::CS_SNAPSHOT_QURY_V0
      What It Does: Reads an assembled snapshot through the governed inspection surface.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing — it is read-only by construction.
    - Capability: Mutable JSON store
      FQDN: capability_side_effects::CS_MUTABLE_JSON_V0
      What It Does: Key-addressable JSON state with last-write-wins.
      Fit (EXACT, PARTIAL, MISMATCH): MISMATCH
      Cannot Do: The phases persist nothing; no store is needed.
    - Capability: Judge a document
      FQDN: transformation::CC_JUDGE_DOCUMENT_V0
      What It Does: Parses a document and evaluates a declared rule set against it.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: It observes nothing, so it cannot ground a claim about the composition.
    - Capability: Author of record
      FQDN: workload::AC_REGISTER_AUTHOR_V0
      What It Does: The human accountable for a register's content.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing.
  gaps:
    columns:
    - Gap
    - Severity
    - Impact
    - Evidence Status
    - Source Finding
    rows:
    - Gap: No governed call grounds a claim against the composition.
      Severity: CRITICAL
      Impact: A phase that verifies beliefs cannot be built from what exists; judging alone is not grounding.
      Evidence Status: NOT_FOUND
      Source Finding: S2 belief_verification A capability for declaring governed calls
    - Gap: No declaration form carries rules applied to a document.
      Severity: MEDIUM
      Impact: The rule set travels as declared workflow input, which is sound but is not a reusable form.
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 system_beliefs #6'
  architectural_observations:
    columns:
    - Observation
    - Evidence
    - Evidence Status
    - Source Finding
    rows:
    - Observation: 'Judging and grounding are separable concerns: one reads a document, the other reads the composition.'
      Evidence: transformation::CC_JUDGE_DOCUMENT_V0 performs the first and binds nothing.
      Evidence Status: VERIFIED
      Source Finding: S2 gaps No governed call grounds a claim
    - Observation: 'Observation is a side effect, not a transform: the same query answers differently against different compositions.'
      Evidence: capability_side_effects::CS_SNAPSHOT_QUERY_V0 is declared read-only with a bound subject.
      Evidence Status: VERIFIED
      Source Finding: S1 constraints A verdict must be reproducible
  discovery_concerns:
    columns:
    - Concern
    - Evidence
    - Severity
    - Evidence Status
    - Source Finding
    rows:
    - Concern: Grounding is only meaningful against the composition the document was written about; against an unrelated snapshot every citation looks like new design.
      Evidence: The identity taxonomy cannot separate proposed-new from fabricated without the CR's declared new artifacts.
      Severity: MEDIUM
      Evidence Status: VERIFIED
      Source Finding: S1 constraints A verdict must be reproducible
  open_questions:
    columns:
    - Question
    - Category
    - Why It Matters
    - Source Finding
    rows:
    - Question: Should the pipeline's own domain be excluded from reuse search when a business change request runs?
      Category: scope
      Why It Matters: A library change request must not be offered a pipeline mechanism as a reuse candidate.
      Source Finding: S2 gaps No governed call grounds a claim
```

> P2 verifies the semantic model inherited from P1 against the compiled snapshot. It discovers
> facts; it does not decide. Every belief P1 recorded gets a result, and `NOT_FOUND` is a final
> answer — absence is a finding, not a reason to keep searching.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions for Stage 3
