# Change Seed — blockchain / chain

## Machine

```yaml
header:
  Stage: 0 — Change Seed
  CR: blockchain_chain_v0
  Status: probably fine
  Feeds: Stage 1 — Change Request
registers:
  subdomain_purpose: |2

    The Chain subdomain maintains the official blockchain ledger. It records every block that has been
    accepted by the network and preserves the complete history of the blockchain from the beginning.
    Other subdomains decide which blocks should be accepted, but the Chain subdomain is responsible for
    maintaining the authoritative record once that decision has been made. This authoritative ledger is
    the foundation that the rest of the blockchain system relies on.
  cr_type:
    columns:
    - Subdomain
    - Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE)
    - Rationale
    rows:
    - Subdomain: chain
      Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE): INVENTED_SUBDOMAIN
      Rationale: The canonical ledger is a distinct concern from block proposal and needs its own governance boundary; it is not an extension of an existing subdomain.
  business_vocabulary:
    columns:
    - Term
    - Definition
    rows:
    - Term: Chain
      Definition: Implemented by CT_COMMIT_BLOCK_V0. The authoritative, ordered, append-only ledger of committed blocks.
    - Term: Block
      Definition: A unit of the ledger produced by a proposer and recorded on the chain; carries the transactions of its round.
    - Term: Proposed Block
      Definition: A block produced by a proposer in the consensus loop, not yet committed and not yet authoritative.
    - Term: Commit
      Definition: 'To make a proposed block part of the canonical chain: its content is hashed as its signature, it is linked to its predecessor, and it is recorded as canonical. Commit is irreversible.'
    - Term: Genesis Block
      Definition: The chain's first block. It has the same form as any block and contains the first system transaction — a mint crediting the mint wallet — performed by the Genesis Actor.
    - Term: Bootstrap
      Definition: The one-time genesis sequence that establishes the initial chain and supply, before the consensus loop runs.
    - Term: Genesis Actor
      Definition: The special, permanent actor that receives the initial minted supply at bootstrap and owns the mint wallet thereafter.
    - Term: Proposer
      Definition: The validator selected to produce a block in a given round.
    - Term: BachiCoin
      Definition: The system's unit of value; the supply is a closed monetary system.
  requested_outcomes:
    columns:
    - Outcome
    rows:
    - Outcome: Establish a closed, canonical chain that commits proposer-produced blocks to an authoritative, append-only record.
    - Outcome: Bootstrap the chain from a genesis block that mints the initial supply to a Genesis Actor before the consensus loop runs.
    - Outcome: For this increment, commit all proposed blocks directly to the chain, with attestation and finalization deferred to future iterations.
  known_facts:
    columns:
    - Fact
    - Certainty (HIGH, MEDIUM, LOW)
    rows:
    - Fact: A canonical chain is required as the authoritative record of committed blocks.
      Certainty (HIGH, MEDIUM, LOW): PROBABLY
    - Fact: A genesis bootstrap is required, and must occur before consensus execution begins.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The genesis block shall mint an initial supply of 1,000,000 BachiCoin.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: The initial supply shall be assigned to a Genesis Actor, which is permanent and owns the mint wallet.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Minting occurs only during genesis bootstrap; no minting and no burning occur in this release.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: For this development increment, all proposer-produced blocks are committed to the chain.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Attestation and finalization are intentionally deferred to a future iteration.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Consensus proposes; the chain records and is the authoritative source of committed history.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: In this release, the chain commits every proposed block without additional validation.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: On commit, a block and its contained transactions become authoritative and immutable.
      Certainty (HIGH, MEDIUM, LOW): HIGH
    - Fact: Wallet balances are derived from committed transactions and reconciled on the chain after commit; the chain does not maintain independent balance state.
      Certainty (HIGH, MEDIUM, LOW): HIGH
  system_beliefs:
    columns:
    - Belief
    - Why It Matters
    - Verification Goal
    rows:
    - Belief: The current implementation does not yet provide a chain that commits proposed blocks.
      Why It Matters: This CR exists to fill that gap; if a commit capability already exists, the CR scope changes.
      Verification Goal: Confirm no existing capability commits proposed blocks to a ledger.
    - Belief: A consensus loop already exists that proposes blocks and drives slot processing.
      Why It Matters: The chain commits exactly the blocks this loop proposes — its upstream producer.
      Verification Goal: Identify the governing workflows, their producers, the records emitted, and the owning subdomain.
    - Belief: There is a block-proposal capability.
      Why It Matters: Defines the input the chain commit consumes.
      Verification Goal: ''
    - Belief: A validator registry already exists.
      Why It Matters: Validators feed proposer selection upstream of the chain.
      Verification Goal: Identify where validators are registered and how proposer selection reads it.
    - Belief: A wallet capability already exists.
      Why It Matters: Genesis mints the initial supply to the mint wallet held by the Genesis Actor.
      Verification Goal: Identify the wallet capability and how a balance or mint is recorded.
    - Belief: A transaction capability already exists.
      Why It Matters: Part of the pipeline from actor to wallet to transaction to mempool.
      Verification Goal: Identify the transaction capability and its place in that pipeline.
    - Belief: A mempool already exists.
      Why It Matters: Transactions queue there before block formation.
      Verification Goal: Identify the mempool store and how transactions queue before a block is formed.
    - Belief: An orchestration subdomain already exists.
      Why It Matters: Drives slot processing and the consensus loop.
      Verification Goal: Identify the orchestration driver and what it invokes.
    - Belief: 'Adjacent subdomains exist: identity, wallet, transaction, mempool, consensus, orchestration.'
      Why It Matters: Establishes the neighbourhood the new chain subdomain plugs into.
      Verification Goal: Confirm each named subdomain exists and note its owning boundary.
  assumptions:
    columns:
    - Assumption
    - Basis
    rows:
    - Assumption: All proposed blocks are good and are committed as finalized, with no rejection path this increment.
      Basis: Incremental-development decision; attestation and finalization deferred.
  constraints:
    columns:
    - Constraint
    - Source
    rows:
    - Constraint: Closed monetary system — no supply enters or leaves except by the system's own rules.
      Source: Business policy
    - Constraint: The chain is immutable — a committed block cannot be altered or removed.
      Source: Business policy
    - Constraint: Genesis supply is fixed at 1,000,000 BachiCoin, minted to the Genesis Actor at bootstrap.
      Source: Business policy
  business_invariants:
    columns:
    - Invariant
    rows:
    - Invariant: Exactly one genesis block exists per chain.
    - Invariant: Genesis executes exactly once at bootstrap and is never replayed.
    - Invariant: Total supply is conserved and equals 1,000,000 BachiCoin.
    - Invariant: A committed block is immutable — it never changes or disappears.
    - Invariant: Every committed block has exactly one predecessor, except the genesis block.
    - Invariant: A block cannot be committed twice.
    - Invariant: The canonical chain is the authoritative source of committed history; a proposed block is not authoritative until committed.
  lifecycle_states:
    columns:
    - Object
    - State
    - Meaning
    rows:
    - Object: Chain
      State: Uninitialized
      Meaning: No genesis block yet; the chain is not established.
    - Object: Chain
      State: Active
      Meaning: Genesis created; the chain accepts and commits blocks.
    - Object: Block
      State: Proposed
      Meaning: Produced by a proposer; not yet committed and not authoritative.
    - Object: Block
      State: Committed
      Meaning: Recorded in the canonical chain; immutable and authoritative.
    - Object: Genesis Block
      State: Created Once
      Meaning: The single first block, established at bootstrap; permanent.
  business_events:
    columns:
    - Event
    - When It Occurs
    - Significance
    rows:
    - Event: Genesis Created
      When It Occurs: Once, at bootstrap, before the consensus loop runs.
      Significance: Establishes the chain and the initial monetary state.
    - Event: Block Proposed
      When It Occurs: When a proposer produces a block in a round.
      Significance: A candidate block exists; not yet authoritative.
    - Event: Block Committed
      When It Occurs: When a proposed block is committed to the canonical chain.
      Significance: The block and its transactions become authoritative and immutable.
    - Event: Balance Reconciled
      When It Occurs: After a block is committed, when wallet balances are recomputed from the committed transactions.
      Significance: Wallet balances become consistent with the canonical committed history.
  authority_boundaries:
    columns:
    - Business Object
    - Authoritative Owner
    rows:
    - Business Object: Proposed Block
      Authoritative Owner: Consensus
    - Business Object: Committed Block
      Authoritative Owner: Chain
    - Business Object: Committed History
      Authoritative Owner: Chain
    - Business Object: Monetary Supply
      Authoritative Owner: Genesis at bootstrap, then Chain
    - Business Object: Wallet Balance
      Authoritative Owner: Chain, derived by reconciliation from committed transactions rather than owned as independent state
  out_of_scope:
    columns:
    - Item
    - Reason
    rows:
    - Item: The attestation step of the proof-of-stake progression.
      Reason: Deferred to a future iteration; all proposed blocks treated as good this increment.
    - Item: The finalization step of the proof-of-stake progression.
      Reason: Deferred to a future iteration; proposed blocks committed directly.
    - Item: Fork resolution.
      Reason: Not part of this release; the chain commits every proposed block.
    - Item: Chain reorganization.
      Reason: Not part of this release; committed history is immutable.
    - Item: Slashing.
      Reason: Validator penalties are out of scope this release.
    - Item: Rewards.
      Reason: Validator and proposer rewards are out of scope this release.
  governance_scope:
    columns:
    - Scope Item
    - Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT)
    rows:
    - Scope Item: chain
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): INVENTED
    - Scope Item: consensus_pos
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: orchestration
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: wallet
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: transaction
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: mempool
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
    - Scope Item: identity
      Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT): ADJACENT
  clarification_requests:
    columns:
    - Question
    - Why Needed
    - Blocking (YES, NO)
    - Owner (HUMAN, SNAPSHOT, GOVERNANCE)
    rows:
    - Question: NONE IDENTIFIED
      Why Needed: ''
      Blocking (YES, NO): ''
      Owner (HUMAN, SNAPSHOT, GOVERNANCE): ''
  acceptance_criteria:
    columns:
    - Criterion
    rows:
    - Criterion: The chain begins with a genesis block that records the assignment of the initial 1,000,000 BachiCoin supply to the Genesis Actor.
    - Criterion: Blocks accepted by the chain appear in the authoritative ledger in proposal order.
    - Criterion: A block recorded in the ledger never changes or disappears.
    - Criterion: The total recorded supply on the ledger is 1,000,000 BachiCoin, held initially by the Genesis Actor.
    - Criterion: Once committed, a block and its contained transactions are treated as authoritative.
  identity_and_sameness:
    columns:
    - Business Object
    - Identified By
    - Two Are The Same When
    rows: []
  lifecycle_transitions:
    columns:
    - Object
    - From State
    - To State
    - Triggered By
    - Cascade
    rows: []
  operation_refusals:
    columns:
    - Operation
    - Refused When
    - Business Reason
    rows: []
  authority_deferrals:
    columns:
    - Business Object
    - Deferred To
    - Until
    rows: []
```

The reference subject, carried over from RI-0's elicitation for `blockchain/chain` and reorganized
into the seed's registers. It is here because it was authored independently of this template: a
template that only fits the document it was derived from proves nothing.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals
