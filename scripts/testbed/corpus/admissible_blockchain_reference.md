# Change Seed — blockchain / chain

**Stage:** 0 — Change Seed
**CR:** blockchain_chain_v0
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

The reference subject, carried over from RI-0's elicitation for `blockchain/chain` and reorganized
into the seed's registers. It is here because it was authored independently of this template: a
template that only fits the document it was derived from proves nothing.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Chain subdomain maintains the official blockchain ledger. It records every block that has been
accepted by the network and preserves the complete history of the blockchain from the beginning.
Other subdomains decide which blocks should be accepted, but the Chain subdomain is responsible for
maintaining the authoritative record once that decision has been made. This authoritative ledger is
the foundation that the rest of the blockchain system relies on.

## 1. CR Type

<!-- register:cr_type business_language -->
| Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|----------------|-----------|
| NEW_SUBDOMAIN | The canonical ledger is a distinct concern from block proposal and needs its own governance boundary; it is not an extension of an existing subdomain. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Chain | The authoritative, ordered, append-only ledger of committed blocks. |
| Block | A unit of the ledger produced by a proposer and recorded on the chain; carries the transactions of its round. |
| Proposed Block | A block produced by a proposer in the consensus loop, not yet committed and not yet authoritative. |
| Commit | To make a proposed block part of the canonical chain: its content is hashed as its signature, it is linked to its predecessor, and it is recorded as canonical. Commit is irreversible. |
| Genesis Block | The chain's first block. It has the same form as any block and contains the first system transaction — a mint crediting the mint wallet — performed by the Genesis Actor. |
| Bootstrap | The one-time genesis sequence that establishes the initial chain and supply, before the consensus loop runs. |
| Genesis Actor | The special, permanent actor that receives the initial minted supply at bootstrap and owns the mint wallet thereafter. |
| Proposer | The validator selected to produce a block in a given round. |
| BachiCoin | The system's unit of value; the supply is a closed monetary system. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Establish a closed, canonical chain that commits proposer-produced blocks to an authoritative, append-only record. |
| Bootstrap the chain from a genesis block that mints the initial supply to a Genesis Actor before the consensus loop runs. |
| For this increment, commit all proposed blocks directly to the chain, with attestation and finalization deferred to future iterations. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A canonical chain is required as the authoritative record of committed blocks. | HIGH |
| A genesis bootstrap is required, and must occur before consensus execution begins. | HIGH |
| The genesis block shall mint an initial supply of 1,000,000 BachiCoin. | HIGH |
| The initial supply shall be assigned to a Genesis Actor, which is permanent and owns the mint wallet. | HIGH |
| Minting occurs only during genesis bootstrap; no minting and no burning occur in this release. | HIGH |
| For this development increment, all proposer-produced blocks are committed to the chain. | HIGH |
| Attestation and finalization are intentionally deferred to a future iteration. | HIGH |
| Consensus proposes; the chain records and is the authoritative source of committed history. | HIGH |
| In this release, the chain commits every proposed block without additional validation. | HIGH |
| On commit, a block and its contained transactions become authoritative and immutable. | HIGH |
| Wallet balances are derived from committed transactions and reconciled on the chain after commit; the chain does not maintain independent balance state. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The current implementation does not yet provide a chain that commits proposed blocks. | This CR exists to fill that gap; if a commit capability already exists, the CR scope changes. | Confirm no existing capability commits proposed blocks to a ledger. |
| A consensus loop already exists that proposes blocks and drives slot processing. | The chain commits exactly the blocks this loop proposes — its upstream producer. | Identify the governing workflows, their producers, the records emitted, and the owning subdomain. |
| A block-proposal capability already exists. | Defines the input the chain commit consumes. | Identify the capability that produces a proposed block and the record it emits. |
| A validator registry already exists. | Validators feed proposer selection upstream of the chain. | Identify where validators are registered and how proposer selection reads it. |
| A wallet capability already exists. | Genesis mints the initial supply to the mint wallet held by the Genesis Actor. | Identify the wallet capability and how a balance or mint is recorded. |
| A transaction capability already exists. | Part of the pipeline from actor to wallet to transaction to mempool. | Identify the transaction capability and its place in that pipeline. |
| A mempool already exists. | Transactions queue there before block formation. | Identify the mempool store and how transactions queue before a block is formed. |
| An orchestration subdomain already exists. | Drives slot processing and the consensus loop. | Identify the orchestration driver and what it invokes. |
| Adjacent subdomains exist: identity, wallet, transaction, mempool, consensus, orchestration. | Establishes the neighbourhood the new chain subdomain plugs into. | Confirm each named subdomain exists and note its owning boundary. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| All proposed blocks are good and are committed as finalized, with no rejection path this increment. | Incremental-development decision; attestation and finalization deferred. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Closed monetary system — no supply enters or leaves except by the system's own rules. | Business policy |
| The chain is immutable — a committed block cannot be altered or removed. | Business policy |
| Genesis supply is fixed at 1,000,000 BachiCoin, minted to the Genesis Actor at bootstrap. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Exactly one genesis block exists per chain. |
| Genesis executes exactly once at bootstrap and is never replayed. |
| Total supply is conserved and equals 1,000,000 BachiCoin. |
| A committed block is immutable — it never changes or disappears. |
| Every committed block has exactly one predecessor, except the genesis block. |
| A block cannot be committed twice. |
| The canonical chain is the authoritative source of committed history; a proposed block is not authoritative until committed. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Chain | Uninitialized | No genesis block yet; the chain is not established. |
| Chain | Active | Genesis created; the chain accepts and commits blocks. |
| Block | Proposed | Produced by a proposer; not yet committed and not authoritative. |
| Block | Committed | Recorded in the canonical chain; immutable and authoritative. |
| Genesis Block | Created Once | The single first block, established at bootstrap; permanent. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| Genesis Created | Once, at bootstrap, before the consensus loop runs. | Establishes the chain and the initial monetary state. |
| Block Proposed | When a proposer produces a block in a round. | A candidate block exists; not yet authoritative. |
| Block Committed | When a proposed block is committed to the canonical chain. | The block and its transactions become authoritative and immutable. |
| Balance Reconciled | After a block is committed, when wallet balances are recomputed from the committed transactions. | Wallet balances become consistent with the canonical committed history. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Proposed Block | Consensus |
| Committed Block | Chain |
| Committed History | Chain |
| Monetary Supply | Genesis at bootstrap, then Chain |
| Wallet Balance | Chain, derived by reconciliation from committed transactions rather than owned as independent state |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| The attestation step of the proof-of-stake progression. | Deferred to a future iteration; all proposed blocks treated as good this increment. |
| The finalization step of the proof-of-stake progression. | Deferred to a future iteration; proposed blocks committed directly. |
| Fork resolution. | Not part of this release; the chain commits every proposed block. |
| Chain reorganization. | Not part of this release; committed history is immutable. |
| Slashing. | Validator penalties are out of scope this release. |
| Rewards. | Validator and proposer rewards are out of scope this release. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| chain | CREATED |
| consensus_pos | ADJACENT |
| orchestration | ADJACENT |
| wallet | ADJACENT |
| transaction | ADJACENT |
| mempool | ADJACENT |
| identity | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |  |  |  |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| The chain begins with a genesis block that records the assignment of the initial 1,000,000 BachiCoin supply to the Genesis Actor. |
| Blocks accepted by the chain appear in the authoritative ledger in proposal order. |
| A block recorded in the ledger never changes or disappears. |
| The total recorded supply on the ledger is 1,000,000 BachiCoin, held initially by the Genesis Actor. |
| Once committed, a block and its contained transactions are treated as authoritative. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
