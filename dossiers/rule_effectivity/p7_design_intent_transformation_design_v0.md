# Stage 7 — Design Intent: transformation / design
**Stage:** 7 — Design Intent
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW: the binding identities and the declarations they carry. Every artifact this change acts on
changes meaning, so each is replaced by a new version, redeclared whole.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Where a document carries its registers | The judging receives the same data in either form. | One YAML Machine block per phase document, the first fenced yaml block, holds a header mapping and a registers mapping. Each register is a list of rows, each row a mapping from column name to string value, columns in declared order; a narrative register is a string. The reader takes a register's columns from its first row, so an empty register keeps the one-row sentinel, its first column reading NONE IDENTIFIED and the others empty. Prose stays Markdown around the block, and the reader returns the header, sections and registers the table reader returned. Values inside cells stay strings. | S4 design_decisions #1 |
| What construction reads | Construction meets this change only through the shared reading. | The construction contract runs the new reading in place of the old and keeps its own splitting of values inside cells. It keeps its identity; only the name of the reading it runs changes. | S4 design_decisions #2 |
| What a rule-set identity is | The identity follows the rules themselves, not the phase's workflow version. | Each phase has a register schema, a JSON file whose $id is the identity, such as transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0. In this change it holds the $id, a digest of the rule set sealed in its workflow, and its revision history; its shape is filled in by the change that moves the rules out of the code. The workflow seals the $id as a literal input beside the rule set. Emission refuses a sealed rule set whose digest the schema does not record. | S4 design_decisions #3 |
| How a document is judged under the rule set it names | A superseded rule set stays available in the composition. | The check selects the phase workflow whose sealed identity equals the rule set the document names, and the current workflow. It reports both verdicts, each naming its rule set. A document naming a rule set no workflow seals is refused, never judged by a substitute. | S4 design_decisions #4 |
| What happens to v5 dossiers | Dossiers approved under v5 stay as published. | Nothing reads them. The table reader is the converter for the test documents only, and is deleted once the two forms are shown to receive the same findings. | S4 design_decisions #5 |
| How a document, an approval and its standing are recorded | A document is judged against both the rules it was authored under and the current rules. | The header names the rule set the document was authored under (rule_set), the rule set its approval was given under (approved_under) and its standing (standing), a value of the document-standing vocabulary. The gate reviewer writes approved_under and standing. Whether an approval holds is derived, never stored: the judging reports it confirmed when approved_under equals the rule set judging, and unconfirmed otherwise. | S4 design_decisions #6 |
| How a migration is recorded | A document amended to satisfy a later rule set says so. | Its standing reads migrated and migrated_from names the rule set it was approved under. A person re-confirming it sets standing to reconfirmed and approved_under to the later rule set. | S4 gap_register GAP-6 |
| How a correction declares its effectivity | A correction declares its own effectivity, and the rule set records the declaration as governed history. | A correction adds a revision to the phase's schema: the new digest, its effectivity from the correction-effectivity vocabulary, and for a retroactive correction the documents it affects. A retroactive correction takes a new $id and so a new workflow version; a correction that is not retroactive keeps the $id. | S4 gap_register GAP-7 |
| How identical verdicts are proven | Different findings can produce the same count. | Each test document is converted mechanically by the table reader and judged in both forms by the same rule set. The findings are compared by rule, register, row and detail. Any difference is a regression, and the table reader is deleted only when there is none. | S4 gap_register GAP-8 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW) | Summary | Reason | Source Finding |
|------|--------------------------------------------------|---------|--------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V0 | REPLACE | Parse phase document text into structured registers | Its meaning changes, so CT_PURE_PARSE_REGISTERS_V1 supersedes it. | S6 pps_artifacts_requiring_action #1 |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | REPLACE | Parse the upstream phase documents a phase is judged against | Its meaning changes, so CT_PURE_PARSE_PRIOR_PHASES_V1 supersedes it. | S6 pps_artifacts_requiring_action #2 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | REPLACE | Evaluate a declared rule set against parsed registers | Its meaning changes, so CT_PURE_EVALUATE_RULES_V1 supersedes it. | S6 pps_artifacts_requiring_action #3 |
| transformation::CC_JUDGE_DOCUMENT_V0 | REPLACE | Parse a phase document and judge it against a declared rule set | Its meaning changes, so CC_JUDGE_DOCUMENT_V1 supersedes it. | S6 pps_artifacts_requiring_action #4 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | REPLACE | Parse a phase document and its priors, observe the composition, and judge them together | Its meaning changes, so CC_JUDGE_AGAINST_SNAPSHOT_V2 supersedes it. | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | REPLACE | Parse a phase document and its priors, observe the composition and its declarations, and judge them together | Its meaning changes, so CC_JUDGE_AGAINST_COMPOSITION_V2 supersedes it. | S6 pps_artifacts_requiring_action #6 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | REPLACE | Decide whether an offered seed is admissible | It gains a sealed rule-set identity, so WF_P0_SEED_ADMISSIBILITY_V1 supersedes it. | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | REPLACE | Decide whether an offered Change Request register is admissible | It gains a sealed rule-set identity, so WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 supersedes it. | S6 pps_artifacts_requiring_action #8 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V1 | REPLACE | Decide whether an offered Domain Model register is admissible | It gains a sealed rule-set identity, so WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 supersedes it. | S6 pps_artifacts_requiring_action #9 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V1 | REPLACE | Decide whether an offered Analysis Loop register is admissible | It gains a sealed rule-set identity, so WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 supersedes it. | S6 pps_artifacts_requiring_action #10 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V1 | REPLACE | Decide whether an offered Business Model register is admissible | It gains a sealed rule-set identity, so WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 supersedes it. | S6 pps_artifacts_requiring_action #11 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V1 | REPLACE | Decide whether an offered Business Intent register is admissible | It gains a sealed rule-set identity, so WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 supersedes it. | S6 pps_artifacts_requiring_action #12 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V1 | REPLACE | Decide whether an offered Governance Intent register is admissible | It gains a sealed rule-set identity, so WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 supersedes it. | S6 pps_artifacts_requiring_action #13 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 | REPLACE | Decide whether an offered Design Intent register is admissible | It gains a sealed rule-set identity, so WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 supersedes it. | S6 pps_artifacts_requiring_action #14 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V1 | REPLACE | Decide whether an offered Authoring Mandate is admissible | It gains a sealed rule-set identity, so WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 supersedes it. | S6 pps_artifacts_requiring_action #15 |
| transformation::IN_SEED_SUBMITTED_V0 | REPOINT | Offer a seed document for admissibility judgement | Starts WF_P0_SEED_ADMISSIBILITY_V0; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #7 |
| transformation::IN_CHANGE_REQUEST_SUBMITTED_V0 | REPOINT | Offer a Change Request register for admissibility judgement | Starts WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #8 |
| transformation::IN_DOMAIN_MODEL_SUBMITTED_V0 | REPOINT | Offer a Domain Model register for admissibility judgement | Starts WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V1; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #9 |
| transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0 | REPOINT | Offer an Analysis Loop register for admissibility judgement | Starts WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V1; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #10 |
| transformation::IN_BUSINESS_MODEL_SUBMITTED_V0 | REPOINT | Offer a Business Model register for admissibility judgement | Starts WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V1; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #11 |
| transformation::IN_BUSINESS_INTENT_SUBMITTED_V0 | REPOINT | Offer a Business Intent register for admissibility judgement | Starts WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V1; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #12 |
| transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0 | REPOINT | Offer a Governance Intent register for admissibility judgement | Starts WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V1; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #13 |
| transformation::IN_DESIGN_INTENT_SUBMITTED_V0 | REPOINT | Offer a Design Intent register for admissibility judgement | Starts WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #14 |
| transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0 | REPOINT | Offer an Authoring Mandate for admissibility judgement | Starts WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V1; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #15 |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | REPOINT | Measure a design, refuse it if under-determined, and render the artifacts it schedules | Runs the reading this change replaces; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #16 |
| transformation::AC_GATE_REVIEWER_V0 | REUSE |  | Closes a gate, and re-confirms an approval under a later rule set. | S6 pps_artifacts_requiring_action #17 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | REUSE |  | Binds read-only observation for every phase workflow. Unchanged; the new workflows bind it. | transformation::RB_TRANSFORMATION_BINDINGS_V0 |
| capability_side_effects::CS_SNAPSHOT_QUERY_V0 | REUSE |  | The observation the later phases' contracts compose. Unchanged. | capability_side_effects::CS_SNAPSHOT_QUERY_V0 |
| transformation::CC_PERSIST_ARTIFACTS_V0 | REVIEW |  | Names a replaced contract in its explanation only. Unchanged. | transformation::CC_PERSIST_ARTIFACTS_V0 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | REVIEW |  | Declares what the domain compiles. Unchanged; named because the authored artifacts are compiled under it. | S6 pps_artifacts_requiring_action #18 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|---------------------------------------------------------------|------|---------|-----------------|--------|----------------|
| Reading a phase document's registers from its structured block | CT | transformation::CT_PURE_PARSE_REGISTERS_V1 | Read a phase document's header and registers from its Machine block, and its sections from its prose | design | NEW | S6 governance_outcome #1 |
| Reading a prior phase's registers from its structured block | CT | transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | Read the upstream phase documents a phase is judged against, each from its Machine block | design | NEW | S6 governance_outcome #1 |
| Judging a document and naming the rule set that judged it | CT | transformation::CT_PURE_EVALUATE_RULES_V1 | Evaluate a declared rule set against a parsed document, naming the rule set and whether the document's approval holds under it | design | NEW | S6 governance_outcome #4 |
| Judging a seed or change request under a named rule set | CC | transformation::CC_JUDGE_DOCUMENT_V1 | Parse a phase document and judge it against a declared rule set, naming that rule set in the verdict | design | NEW | S6 governance_outcome #4 |
| Judging a later phase against the composition under a named rule set | CC | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | Parse a phase document and its priors, observe the composition, and judge them together under a named rule set | design | NEW | S6 governance_outcome #4 |
| Judging the analysis loop against the composition under a named rule set | CC | transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | Parse an analysis loop and its priors, observe the composition's declarations, and judge them together under a named rule set | design | NEW | S6 governance_outcome #4 |
| Deciding whether a seed is admissible under a named rule set | WF | transformation::WF_P0_SEED_ADMISSIBILITY_V1 | Decide whether a seed is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Deciding whether a change request is admissible under a named rule set | WF | transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | Decide whether a change request is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Deciding whether a domain model is admissible under a named rule set | WF | transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | Decide whether a domain model is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Deciding whether an analysis loop is admissible under a named rule set | WF | transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | Decide whether an analysis loop is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Deciding whether a business model is admissible under a named rule set | WF | transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | Decide whether a business model is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Deciding whether a business intent is admissible under a named rule set | WF | transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | Decide whether a business intent is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Deciding whether a governance intent is admissible under a named rule set | WF | transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | Decide whether a governance intent is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Deciding whether a design intent is admissible under a named rule set | WF | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | Decide whether a design intent is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Deciding whether an authoring mandate is admissible under a named rule set | WF | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | Decide whether an authoring mandate is admissible, under a rule set with an identity | design | NEW | S6 governance_outcome #2 |
| Recording the standing of a phase document | VOCAB | transformation::VOCAB_DOCUMENT_STANDING_V0 | The standings a phase document may hold: approved, migrated or re-confirmed | design | NEW | S6 governance_outcome #6 |
| Reporting whether an approval holds under the rule set judging it | VOCAB | transformation::VOCAB_APPROVAL_STANDING_V0 | The standings an approval may hold under a rule set: confirmed or unconfirmed | design | NEW | S6 governance_outcome #5 |
| Declaring whether a correction applies to documents approved before it | VOCAB | transformation::VOCAB_CORRECTION_EFFECTIVITY_V0 | Whether a correction applies to documents approved before it: retroactive or not | design | NEW | S6 governance_outcome #7 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P0_SEED_ADMISSIBILITY_V1 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #7 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #8 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #9 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #10 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #11 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #12 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #13 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #14 |
| transformation::RB_TRANSFORMATION_BINDINGS_V0 | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | execution::STRUCTURE_RUNTIME_EXECUTION_V0 | S6 pps_artifacts_requiring_action #15 |

---

## 5. Execution Topology

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | transformation::IN_SEED_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_DOCUMENT_V1; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | transformation::IN_CHANGE_REQUEST_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_DOCUMENT_V1; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #8 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #8 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | transformation::IN_DOMAIN_MODEL_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #9 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #9 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #9 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #9 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_AGAINST_COMPOSITION_V2; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #10 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #10 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #10 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #10 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | transformation::IN_BUSINESS_MODEL_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #11 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #11 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #11 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #11 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | transformation::IN_BUSINESS_INTENT_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #12 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #12 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #12 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #12 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #13 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #13 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #13 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #13 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::IN_DESIGN_INTENT_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #14 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #14 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0 |  | IN | ACK -> transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #15 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 |  | CC | SUCCESS -> EXIT_JUDGED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED; NOT_FOUND -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #15 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | EXIT_JUDGED |  | EXIT_SUCCESS | — | S6 pps_artifacts_requiring_action #15 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #15 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| transformation::CC_JUDGE_DOCUMENT_V1 | 1 | parse_registers | transformation::CT_PURE_PARSE_REGISTERS_V1 | CT | PURE_PARSE_REGISTERS | — | document_text | header, sections, registers | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: document_text=document_text; out: header=header, sections=sections, registers=registers |
| transformation::CC_JUDGE_DOCUMENT_V1 | 2 | parse_priors | transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | CT | PURE_PARSE_PRIOR_PHASES | — | prior_texts | priors | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: prior_texts=prior_texts; out: priors=priors |
| transformation::CC_JUDGE_DOCUMENT_V1 | 3 | evaluate_rules | transformation::CT_PURE_EVALUATE_RULES_V1 | CT | PURE_EVALUATE_RULES | — | header, sections, registers, document_text, rule_set, observed, priors, rule_set_id | verdict, findings, rules_evaluated, rule_set, approval_standing | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: header=header, sections=sections, registers=registers, document_text=document_text, rule_set=rule_set, observed=observed, priors=priors, rule_set_id=rule_set_id; out: verdict=verdict, findings=findings, rules_evaluated=rules_evaluated, rule_set=rule_set, approval_standing=approval_standing |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 1 | parse_registers | transformation::CT_PURE_PARSE_REGISTERS_V1 | CT | PURE_PARSE_REGISTERS | — | document_text | header, sections, registers | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: document_text=document_text; out: header=header, sections=sections, registers=registers |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 2 | parse_priors | transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | CT | PURE_PARSE_PRIOR_PHASES | — | prior_texts | priors | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: prior_texts=prior_texts; out: priors=priors |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 3 | observe_composition | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | CS | QUERY | — | operation, params | observation | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS |  |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 4 | observe_capabilities | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | CS | QUERY | — | operation, params | observation | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS |  |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 5 | observe_reuse_visibility | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | CS | QUERY | — | operation, params | observation | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS |  |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 6 | observe_store_list | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | CS | QUERY | — | operation, params | observation | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS |  |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 7 | observe_rule_set_list | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | CS | QUERY | — | operation, params | observation | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS |  |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 8 | observe_behavior_logic_list | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | CS | QUERY | — | operation, params | observation | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS |  |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | 9 | evaluate_rules | transformation::CT_PURE_EVALUATE_RULES_V1 | CT | PURE_EVALUATE_RULES | — | header, sections, registers, document_text, rule_set, observed, priors, rule_set_id | verdict, findings, rules_evaluated, rule_set, approval_standing | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: header=header, sections=sections, registers=registers, document_text=document_text, rule_set=rule_set, observed=observed, priors=priors, rule_set_id=rule_set_id; out: verdict=verdict, findings=findings, rules_evaluated=rules_evaluated, rule_set=rule_set, approval_standing=approval_standing |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | 1 | parse_registers | transformation::CT_PURE_PARSE_REGISTERS_V1 | CT | PURE_PARSE_REGISTERS | — | document_text | header, sections, registers | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: document_text=document_text; out: header=header, sections=sections, registers=registers |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | 2 | parse_priors | transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | CT | PURE_PARSE_PRIOR_PHASES | — | prior_texts | priors | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: prior_texts=prior_texts; out: priors=priors |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | 3 | observe_composition | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | CS | QUERY | — | operation, params | observation | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS |  |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | 4 | observe_declarations | capability_side_effects::CS_SNAPSHOT_QUERY_V0 | CS | QUERY | — | operation, params | observation | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS |  |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | 5 | evaluate_rules | transformation::CT_PURE_EVALUATE_RULES_V1 | CT | PURE_EVALUATE_RULES | — | header, sections, registers, document_text, rule_set, observed, priors, rule_set_id | verdict, findings, rules_evaluated, rule_set, approval_standing | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: header=header, sections=sections, registers=registers, document_text=document_text, rule_set=rule_set, observed=observed, priors=priors, rule_set_id=rule_set_id; out: verdict=verdict, findings=findings, rules_evaluated=rules_evaluated, rule_set=rule_set, approval_standing=approval_standing |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | document_text | payload.seed_text | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | prior_texts | {} | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #7 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P0_SEED_V0" | S7 design_resolution #3 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #8 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #8 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #8 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P1_CHANGE_REQUEST_V0" | S7 design_resolution #3 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #9 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #9 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #9 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P2_DOMAIN_MODEL_V0" | S7 design_resolution #3 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #10 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #10 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #10 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0" | S7 design_resolution #3 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #11 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #11 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #11 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P4_BUSINESS_MODEL_V0" | S7 design_resolution #3 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #12 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #12 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #12 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P5_BUSINESS_INTENT_V0" | S7 design_resolution #3 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #13 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #13 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #13 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P6_GOVERNANCE_INTENT_V0" | S7 design_resolution #3 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #14 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #14 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #14 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P7_DESIGN_INTENT_V0" | S7 design_resolution #3 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | document_text | payload.register_text | S6 pps_artifacts_requiring_action #15 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | prior_texts | payload.prior_texts | S6 pps_artifacts_requiring_action #15 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set | the rule set emission seals from the phase's declaration | S6 pps_artifacts_requiring_action #15 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set_id | "transformation.schemas.SCHEMA_REGISTERS_P8_AUTHORING_MANDATE_V0" | S7 design_resolution #3 |
| transformation::CC_JUDGE_DOCUMENT_V1 | evaluate_rules | OUTPUT | verdict | capability_result.verdict | S6 pps_artifacts_requiring_action #4 |
| transformation::CC_JUDGE_DOCUMENT_V1 | evaluate_rules | OUTPUT | findings | capability_result.findings | S6 pps_artifacts_requiring_action #4 |
| transformation::CC_JUDGE_DOCUMENT_V1 | evaluate_rules | OUTPUT | rules_evaluated | capability_result.rules_evaluated | S6 pps_artifacts_requiring_action #4 |
| transformation::CC_JUDGE_DOCUMENT_V1 | evaluate_rules | OUTPUT | rule_set | capability_result.rule_set | S6 pps_artifacts_requiring_action #4 |
| transformation::CC_JUDGE_DOCUMENT_V1 | evaluate_rules | OUTPUT | approval_standing | capability_result.approval_standing | S6 pps_artifacts_requiring_action #4 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_composition | INPUT | operation | "si.artifact.list" | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_composition | INPUT | params | {} | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_capabilities | INPUT | operation | "si.capability.surface" | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_capabilities | INPUT | params | {} | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_reuse_visibility | INPUT | operation | "si.snapshot.summary" | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_reuse_visibility | INPUT | params | {} | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_store_list | INPUT | operation | "si.store.list" | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_store_list | INPUT | params | {} | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_rule_set_list | INPUT | operation | "si.rule_set.list" | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_rule_set_list | INPUT | params | {} | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_behavior_logic_list | INPUT | operation | "si.behavior_logic.list" | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | observe_behavior_logic_list | INPUT | params | {} | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | evaluate_rules | OUTPUT | verdict | capability_result.verdict | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | evaluate_rules | OUTPUT | findings | capability_result.findings | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | evaluate_rules | OUTPUT | rules_evaluated | capability_result.rules_evaluated | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | evaluate_rules | OUTPUT | rule_set | capability_result.rule_set | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | evaluate_rules | OUTPUT | approval_standing | capability_result.approval_standing | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | observe_composition | INPUT | operation | "si.artifact.list" | S6 pps_artifacts_requiring_action #6 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | observe_composition | INPUT | params | {} | S6 pps_artifacts_requiring_action #6 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | observe_declarations | INPUT | operation | "si.snapshot.summary" | S6 pps_artifacts_requiring_action #6 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | observe_declarations | INPUT | params | {} | S6 pps_artifacts_requiring_action #6 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | evaluate_rules | OUTPUT | verdict | capability_result.verdict | S6 pps_artifacts_requiring_action #6 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | evaluate_rules | OUTPUT | findings | capability_result.findings | S6 pps_artifacts_requiring_action #6 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | evaluate_rules | OUTPUT | rules_evaluated | capability_result.rules_evaluated | S6 pps_artifacts_requiring_action #6 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | evaluate_rules | OUTPUT | rule_set | capability_result.rule_set | S6 pps_artifacts_requiring_action #6 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | evaluate_rules | OUTPUT | approval_standing | capability_result.approval_standing | S6 pps_artifacts_requiring_action #6 |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | INPUT | document_text | string | YES |  | The full text of the phase document — never a path, never read from disk |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | OUTPUT | header | object | YES |  | Header field name to declared value |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | OUTPUT | sections | array | YES |  | Ordered sections, each with number, title, text, and any table columns and rows |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | OUTPUT | registers | array | YES |  | Registers addressed by their marker id, each with columns and rows |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | INPUT | prior_texts | object | YES |  | Phase id → full text of that phase's document, supplied by the calling workflow. Empty when |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | OUTPUT | priors | object | YES |  | Phase id → parsed document as header, sections and registers |
| transformation::CT_PURE_EVALUATE_RULES_V1 | INPUT | header | object | YES |  | Header fields as parsed from the document |
| transformation::CT_PURE_EVALUATE_RULES_V1 | INPUT | sections | array | YES |  | Parsed document sections |
| transformation::CT_PURE_EVALUATE_RULES_V1 | INPUT | registers | array | YES |  | Parsed registers, addressed by marker id — how a rule locates what it governs |
| transformation::CT_PURE_EVALUATE_RULES_V1 | INPUT | document_text | string | YES |  | The original document text, for whole-document rules |
| transformation::CT_PURE_EVALUATE_RULES_V1 | INPUT | rule_set | array | YES |  | The declared rules deciding admissibility — supplied by the calling workflow |
| transformation::CT_PURE_EVALUATE_RULES_V1 | INPUT | observed | object | YES |  | Facts gathered about the composition, keyed by the inspection operation that produced each. |
| transformation::CT_PURE_EVALUATE_RULES_V1 | INPUT | priors | object | YES |  | The upstream phase documents this one is judged against, parsed, keyed by phase id. Empty |
| transformation::CT_PURE_EVALUATE_RULES_V1 | OUTPUT | verdict | string | YES |  | ADMISSIBLE when no rule failed, INADMISSIBLE otherwise |
| transformation::CT_PURE_EVALUATE_RULES_V1 | OUTPUT | findings | array | YES |  | One entry per failed rule, naming the rule, where it failed, and why it matters |
| transformation::CT_PURE_EVALUATE_RULES_V1 | OUTPUT | rules_evaluated | integer | YES |  | How many rules were applied — every rule in the set, always |
| transformation::CT_PURE_EVALUATE_RULES_V1 | INPUT | rule_set_id | string | YES |  | The identity of the rule set supplied, as its phase's register schema declares it |
| transformation::CT_PURE_EVALUATE_RULES_V1 | OUTPUT | rule_set | string | YES |  | The identity of the rule set that rendered the verdict |
| transformation::CT_PURE_EVALUATE_RULES_V1 | OUTPUT | approval_standing | string | NO |  | Whether the document's approval holds under that rule set: confirmed or unconfirmed; absent when the document names no approval |
| transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | document_text | string | YES |  | document_text |
| transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | prior_texts | object | YES |  | Phase id → full text of the upstream document. Empty when this phase reads none — which for |
| transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | rule_set | array | YES |  | rule_set |
| transformation::CC_JUDGE_DOCUMENT_V1 | OUTPUT | verdict | string | YES |  | verdict |
| transformation::CC_JUDGE_DOCUMENT_V1 | OUTPUT | findings | array | YES |  | findings |
| transformation::CC_JUDGE_DOCUMENT_V1 | OUTPUT | rules_evaluated | integer | YES |  | rules_evaluated |
| transformation::CC_JUDGE_DOCUMENT_V1 | INPUT | rule_set_id | string | YES |  | The identity of the rule set supplied, as its phase's register schema declares it |
| transformation::CC_JUDGE_DOCUMENT_V1 | OUTPUT | rule_set | string | YES |  | The identity of the rule set that rendered the verdict |
| transformation::CC_JUDGE_DOCUMENT_V1 | OUTPUT | approval_standing | string | NO |  | Whether the document's approval holds under that rule set: confirmed or unconfirmed; absent when the document names no approval |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | document_text | string | YES |  | document_text |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | prior_texts | object | YES |  | Phase id → full text of the upstream document. Empty when this phase reads none; the rule |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set | array | YES |  | rule_set |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | OUTPUT | verdict | string | YES |  | verdict |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | OUTPUT | findings | array | YES |  | findings |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | OUTPUT | rules_evaluated | integer | YES |  | rules_evaluated |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | INPUT | rule_set_id | string | YES |  | The identity of the rule set supplied, as its phase's register schema declares it |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | OUTPUT | rule_set | string | YES |  | The identity of the rule set that rendered the verdict |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | OUTPUT | approval_standing | string | NO |  | Whether the document's approval holds under that rule set: confirmed or unconfirmed; absent when the document names no approval |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | INPUT | document_text | string | YES |  | document_text |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | INPUT | prior_texts | object | YES |  | Phase id → full text of the upstream document. Empty when the caller handed none over; the |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | INPUT | rule_set | array | YES |  | rule_set |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | OUTPUT | verdict | string | YES |  | verdict |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | OUTPUT | findings | array | YES |  | findings |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | OUTPUT | rules_evaluated | integer | YES |  | rules_evaluated |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | INPUT | rule_set_id | string | YES |  | The identity of the rule set supplied, as its phase's register schema declares it |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | OUTPUT | rule_set | string | YES |  | The identity of the rule set that rendered the verdict |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | OUTPUT | approval_standing | string | NO |  | Whether the document's approval holds under that rule set: confirmed or unconfirmed; absent when the document names no approval |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | transformation.implementation.capability_transforms.atoms.ct_pure_parse_registers_v1 | execute | PURE_PARSE_REGISTERS | atom | ct_pure | never | S7 new_artifacts CT_PURE_PARSE_REGISTERS_V1 |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | transformation.implementation.capability_transforms.atoms.ct_pure_parse_prior_phases_v1 | execute | PURE_PARSE_PRIOR_PHASES | atom | ct_pure | never | S7 new_artifacts CT_PURE_PARSE_PRIOR_PHASES_V1 |
| transformation::CT_PURE_EVALUATE_RULES_V1 | transformation.implementation.capability_transforms.atoms.ct_pure_evaluate_rules_v1 | execute | PURE_EVALUATE_RULES | atom | ct_pure | returns | S7 new_artifacts CT_PURE_EVALUATE_RULES_V1 |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|
| transformation::VOCAB_DOCUMENT_STANDING_V0 | NONE | document_standing | lower_snake | approved | A person closed the document's gate under the rule set it names. | S7 new_artifacts VOCAB_DOCUMENT_STANDING_V0 |
| transformation::VOCAB_DOCUMENT_STANDING_V0 | NONE | document_standing | lower_snake | migrated | The document was amended to satisfy a later rule set, and nobody has re-confirmed it. | S7 new_artifacts VOCAB_DOCUMENT_STANDING_V0 |
| transformation::VOCAB_DOCUMENT_STANDING_V0 | NONE | document_standing | lower_snake | reconfirmed | A person judged the document whole under a later rule set and closed its gate again. | S7 new_artifacts VOCAB_DOCUMENT_STANDING_V0 |
| transformation::VOCAB_APPROVAL_STANDING_V0 | NONE | approval_standing | lower_snake | confirmed | The approval was given under the rule set the document is judged against. | S7 new_artifacts VOCAB_APPROVAL_STANDING_V0 |
| transformation::VOCAB_APPROVAL_STANDING_V0 | NONE | approval_standing | lower_snake | unconfirmed | The document is judged against a rule set other than the one its approval was given under, and no person has re-confirmed it. | S7 new_artifacts VOCAB_APPROVAL_STANDING_V0 |
| transformation::VOCAB_CORRECTION_EFFECTIVITY_V0 | NONE | correction_effectivity | lower_snake | retroactive | The correction can alter a prior document's admissibility. It takes a new rule-set identity and names the documents it affects. | S7 new_artifacts VOCAB_CORRECTION_EFFECTIVITY_V0 |
| transformation::VOCAB_CORRECTION_EFFECTIVITY_V0 | NONE | correction_effectivity | lower_snake | not_retroactive | The correction cannot alter a prior document's admissibility. It is recorded as a revision under the same identity. | S7 new_artifacts VOCAB_CORRECTION_EFFECTIVITY_V0 |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| NONE IDENTIFIED |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | supersedes | transformation::CT_PURE_PARSE_REGISTERS_V0 | S7 existing_inventory CT_PURE_PARSE_REGISTERS_V0 |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | supersedes | transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | S7 existing_inventory CT_PURE_PARSE_PRIOR_PHASES_V0 |
| transformation::CT_PURE_EVALUATE_RULES_V1 | supersedes | transformation::CT_PURE_EVALUATE_RULES_V0 | S7 existing_inventory CT_PURE_EVALUATE_RULES_V0 |
| transformation::CC_JUDGE_DOCUMENT_V1 | supersedes | transformation::CC_JUDGE_DOCUMENT_V0 | S7 existing_inventory CC_JUDGE_DOCUMENT_V0 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2 | supersedes | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | S7 existing_inventory CC_JUDGE_AGAINST_SNAPSHOT_V1 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V2 | supersedes | transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | S7 existing_inventory CC_JUDGE_AGAINST_COMPOSITION_V1 |
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | supersedes | transformation::WF_P0_SEED_ADMISSIBILITY_V0 | S7 existing_inventory WF_P0_SEED_ADMISSIBILITY_V0 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | supersedes | transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | S7 existing_inventory WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | supersedes | transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V1 | S7 existing_inventory WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V1 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | supersedes | transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V1 | S7 existing_inventory WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V1 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | supersedes | transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V1 | S7 existing_inventory WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V1 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | supersedes | transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V1 | S7 existing_inventory WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V1 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | supersedes | transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V1 | S7 existing_inventory WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V1 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | supersedes | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 | S7 existing_inventory WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | supersedes | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V1 | S7 existing_inventory WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V1 |
| transformation::VOCAB_DOCUMENT_STANDING_V0 | governed_by | vocabulary::CONSTITUTION_VOCABULARY_V0 | S7 new_artifacts VOCAB_DOCUMENT_STANDING_V0 |
| transformation::VOCAB_APPROVAL_STANDING_V0 | governed_by | vocabulary::CONSTITUTION_VOCABULARY_V0 | S7 new_artifacts VOCAB_APPROVAL_STANDING_V0 |
| transformation::VOCAB_CORRECTION_EFFECTIVITY_V0 | governed_by | vocabulary::CONSTITUTION_VOCABULARY_V0 | S7 new_artifacts VOCAB_CORRECTION_EFFECTIVITY_V0 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| REPLACE | design | 15 | transformation::CT_PURE_PARSE_REGISTERS_V0, transformation::CT_PURE_PARSE_PRIOR_PHASES_V0, transformation::CT_PURE_EVALUATE_RULES_V0, transformation::CC_JUDGE_DOCUMENT_V0, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1, transformation::CC_JUDGE_AGAINST_COMPOSITION_V1, transformation::WF_P0_SEED_ADMISSIBILITY_V0, transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0, transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V1, transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V1, transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V1, transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V1, transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V1, transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V1, transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V1 |
| EXTEND | design | 0 |  |
| NEW | design | 18 | transformation::CT_PURE_PARSE_REGISTERS_V1, transformation::CT_PURE_PARSE_PRIOR_PHASES_V1, transformation::CT_PURE_EVALUATE_RULES_V1, transformation::CC_JUDGE_DOCUMENT_V1, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V2, transformation::CC_JUDGE_AGAINST_COMPOSITION_V2, transformation::WF_P0_SEED_ADMISSIBILITY_V1, transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1, transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2, transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2, transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2, transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2, transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2, transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2, transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2, transformation::VOCAB_DOCUMENT_STANDING_V0, transformation::VOCAB_APPROVAL_STANDING_V0, transformation::VOCAB_CORRECTION_EFFECTIVITY_V0 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| transformation::WF_P0_SEED_ADMISSIBILITY_V1 | transformation.design.emit:emit_rule_sets | templates/p0_change_seed_template_v0.md, transformation/design/p0_change_seed/rules.py, registry/design/capability_contracts/CC_JUDGE_DOCUMENT_V1.md, registry/schema/SCHEMA_REGISTERS_P0_SEED_V0.json | S7 design_resolution #3 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1 | transformation.design.emit:emit_rule_sets | templates/p1_change_request_template_v0.md, transformation/design/p1_change_request/rules.py, registry/design/capability_contracts/CC_JUDGE_DOCUMENT_V1.md, registry/schema/SCHEMA_REGISTERS_P1_CHANGE_REQUEST_V0.json | S7 design_resolution #3 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2 | transformation.design.emit:emit_rule_sets | templates/p2_domain_model_template_v0.md, transformation/design/p2_domain_model/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V2.md, registry/schema/SCHEMA_REGISTERS_P2_DOMAIN_MODEL_V0.json | S7 design_resolution #3 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2 | transformation.design.emit:emit_rule_sets | templates/p3_analysis_loop_template_v0.md, transformation/design/p3_analysis_loop/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_COMPOSITION_V2.md, registry/schema/SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0.json | S7 design_resolution #3 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2 | transformation.design.emit:emit_rule_sets | templates/p4_business_model_template_v0.md, transformation/design/p4_business_model/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V2.md, registry/schema/SCHEMA_REGISTERS_P4_BUSINESS_MODEL_V0.json | S7 design_resolution #3 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2 | transformation.design.emit:emit_rule_sets | templates/p5_business_intent_template_v0.md, transformation/design/p5_business_intent/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V2.md, registry/schema/SCHEMA_REGISTERS_P5_BUSINESS_INTENT_V0.json | S7 design_resolution #3 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2 | transformation.design.emit:emit_rule_sets | templates/p6_governance_intent_template_v0.md, transformation/design/p6_governance_intent/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V2.md, registry/schema/SCHEMA_REGISTERS_P6_GOVERNANCE_INTENT_V0.json | S7 design_resolution #3 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | transformation.design.emit:emit_rule_sets | templates/p7_design_intent_template_v0.md, transformation/design/p7_design_intent/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V2.md, registry/schema/SCHEMA_REGISTERS_P7_DESIGN_INTENT_V0.json | S7 design_resolution #3 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2 | transformation.design.emit:emit_rule_sets | templates/p8_authoring_mandate_template_v0.md, transformation/design/p8_authoring_mandate/rules.py, registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V2.md, registry/schema/SCHEMA_REGISTERS_P8_AUTHORING_MANDATE_V0.json | S7 design_resolution #3 |

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| NONE IDENTIFIED |

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| NONE IDENTIFIED |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|
| NONE IDENTIFIED |

---

## 20. Refusal — Governance-Surface Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|
| Judging a document | The document is in the old form, after this change | p0 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p1 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p2 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p3 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p4 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p5 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p6 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p7 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p8 | REGISTER_MISSING | S0 operation_refusals #1 |

---

## 21. Molecule Steps

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---------|------|-----------------------------|--------|------|----------|-------|----------------|
| NONE IDENTIFIED |

---

## 22. Molecule Step Bindings

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---------|------|-----------------------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 23. Test Cases

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---------|------|---------------------------------------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | SUCCESS | human decision |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | reads_each_prior_from_its_machine_block | SUCCESS | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | SUCCESS | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | SUCCESS | human decision |

---

## 24. Test Case Values

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---------|------|------------------------------------------|-------|-------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | INPUT | document_text | "# Stage 1\n\n```yaml\nheader: {CR: rule_effectivity, rule_set: transformation.schemas.SCHEMA_REGISTERS_P1_CHANGE_REQUEST_V0}\nregisters:\n  known_facts:\n  - {Fact: An approval names its rule set., Certainty: HIGH}\n```\n" | human decision |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | EXPECTED | header | {CR: rule_effectivity, rule_set: transformation.schemas.SCHEMA_REGISTERS_P1_CHANGE_REQUEST_V0} | human decision |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | EXPECTED | sections | [] | human decision |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | EXPECTED | registers | [{id: known_facts, columns: [Fact, Certainty], rows: [{Fact: An approval names its rule set., Certainty: HIGH}], text: ''}] | human decision |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | reads_each_prior_from_its_machine_block | INPUT | prior_texts | {p1: "# Stage 1\n\n```yaml\nheader: {CR: rule_effectivity, rule_set: transformation.schemas.SCHEMA_REGISTERS_P1_CHANGE_REQUEST_V0}\nregisters:\n  known_facts:\n  - {Fact: An approval names its rule set., Certainty: HIGH}\n```\n"} | human decision |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | reads_each_prior_from_its_machine_block | EXPECTED | priors | {p1: {header: {CR: rule_effectivity, rule_set: transformation.schemas.SCHEMA_REGISTERS_P1_CHANGE_REQUEST_V0}, sections: [], registers: [{id: known_facts, columns: [Fact, Certainty], rows: [{Fact: An approval names its rule set., Certainty: HIGH}], text: ''}]}} | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | INPUT | header | {rule_set: transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0, approved_under: transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0} | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | INPUT | sections | [] | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | INPUT | registers | [] | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | INPUT | document_text | "" | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | INPUT | rule_set | [] | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | INPUT | rule_set_id | transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0 | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | INPUT | observed | {} | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | INPUT | priors | {} | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | EXPECTED | verdict | ADMISSIBLE | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | EXPECTED | findings | [] | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | EXPECTED | rules_evaluated | 0 | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | EXPECTED | rule_set | transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0 | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_the_judging_rule_set_confirmed | EXPECTED | approval_standing | confirmed | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | INPUT | header | {rule_set: transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0, approved_under: transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V1} | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | INPUT | sections | [] | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | INPUT | registers | [] | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | INPUT | document_text | "" | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | INPUT | rule_set | [] | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | INPUT | rule_set_id | transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0 | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | INPUT | observed | {} | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | INPUT | priors | {} | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | EXPECTED | verdict | ADMISSIBLE | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | EXPECTED | findings | [] | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | EXPECTED | rules_evaluated | 0 | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | EXPECTED | rule_set | transformation.schemas.SCHEMA_REGISTERS_P3_ANALYSIS_LOOP_V0 | human decision |
| transformation::CT_PURE_EVALUATE_RULES_V1 | reports_an_approval_under_another_rule_set_unconfirmed | EXPECTED | approval_standing | unconfirmed | human decision |

---

## 25. Withdrawn Facts

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|----------|------|--------|----------------|

---

## Gate 1 — Design Approval

**Gate 1 closes here.** The full dossier (Stages 0–7) is presented for review as a body.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 6 — Governance Intent | Ownership, artifacts requiring action, boundary rules | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
