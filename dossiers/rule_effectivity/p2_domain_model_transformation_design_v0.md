# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** rule_effectivity
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, against the rule sets the
phases declare, and against how the phases read a document. What was searched is recorded, not only
what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Phase | One step of the lifecycle, with a rule set of its own. | One declared workflow per phase, owned by this subdomain. Seven phases hold a second version beside the first. | VERIFIED | S1 business_vocabulary #1 |
| Rule set | The rules a phase declares, against which it judges a document. | A copy held inside the phase's workflow, produced from the phase's template and its declaration together. | VERIFIED | S1 business_vocabulary #2 |
| Register | The part of a phase document that states facts the rules judge. | A table inside the document's prose, marked by a comment above it. | VERIFIED | S1 business_vocabulary #3 |
| Prose | The part of a phase document that explains the change to a person. | The rest of the same text. | VERIFIED | S1 business_vocabulary #4 |
| Verdict | The result of judging a document against a rule set. | Returned by the judging, and held by nobody. | VERIFIED | S1 business_vocabulary #5 |
| Finding | One reason a verdict gives for a document being inadmissible. | Part of the verdict. | VERIFIED | S1 business_vocabulary #6 |
| Approval | A person closing a document's gate under a rule set. | A lifecycle state in the document's header. Nothing records the rule set. | VERIFIED | S1 business_vocabulary #7 |
| Rule-set identity | The name of a rule set, which changes only when the rules change. | Nothing holds it. | NOT_FOUND | S1 business_vocabulary #8 |
| Rule-set version | A rule set created by a change that can alter a prior document's admissibility. | A new version of a phase's workflow. It is created whenever the workflow changes, whether or not a rule did. | VERIFIED | S1 business_vocabulary #9 |
| Effectivity | Whether a correction applies to documents approved before it. | Nothing holds it. | NOT_FOUND | S1 business_vocabulary #15 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Verdict | Admissibility | Admissible or inadmissible. | VERIFIED | S1 business_vocabulary #5 |
| Verdict | Findings | The reasons for an inadmissible verdict. | VERIFIED | S1 business_vocabulary #6 |
| Verdict | Rule set | The rule set the verdict was rendered against. | NOT_FOUND | S1 requested_outcomes #4 |
| Document | Rule set | The rule set the document was authored under. | NOT_FOUND | S1 requested_outcomes #3 |
| Document | Migrated | Whether the document was amended to satisfy a later rule set. | NOT_FOUND | S1 requested_outcomes #5 |
| Approval | Rule set | The rule set the approval was given under. | NOT_FOUND | S1 requested_outcomes #6 |
| Register | Structured form | The register's facts, held as data apart from the prose. | NOT_FOUND | S1 requested_outcomes #1 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Judging a document against a phase | The person driving a change | A verdict, and the findings that explain it. | VERIFIED | S1 business_events #1 |
| Approving a document | A person at the gate | The document's lifecycle state moves on. | VERIFIED | S1 business_events #2 |
| Correcting a rule set | The person changing the lifecycle | The phase's copy of its rule set is produced again. | VERIFIED | S1 business_events #6 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Judging a document against a phase | 1 | Read the registers out of the document's text, by the reading conventions. | None. | VERIFIED | S1 system_beliefs #2 |
| Judging a document against a phase | 2 | Judge each rule the phase declares against them. | The findings. | VERIFIED | S1 business_events #1 |
| Judging a document against a phase | 3 | Render the verdict. | The verdict, naming no rule set. | VERIFIED | S1 system_beliefs #6 |
| Approving a document | 1 | Close the gate by moving the document's lifecycle state on. | The header's state. | VERIFIED | S1 system_beliefs #7 |
| Correcting a rule set | 1 | Change the phase's template or declaration, and produce its copy again. | A new copy of the rule set. | VERIFIED | S1 system_beliefs #9 |
| Correcting a rule set | 2 | Declare whether the correction is retroactive. | None. | NOT_FOUND | S1 known_facts #8 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| A phase document carries prose and registers in one Markdown text, with each register a table inside the prose. | VERIFIED | Each register is a pipe table opened within three lines of a marker comment naming its register. The judging reads the whole text and finds each table by its marker. | S1 system_beliefs #1 |
| The rules read each register through conventions that only the code states. | VERIFIED | The phase's workflow carries its rules, and no reading convention. The reading is done by `transformation::CT_PURE_PARSE_REGISTERS_V0`, whose declaration states its inputs and outputs and none of the conventions. No artifact in the pinned snapshot states them. | S1 system_beliefs #2 |
| Fourteen reading conventions and seven formats inside cells exist today. | VERIFIED | Counted from the reading and judging code: fourteen conventions decide what a section, register, table, column, empty register, silent cell, gated row, header field, claim, vocabulary match, pattern and identity are. Seven values inside cells carry a format of their own. | S1 system_beliefs #3 |
| A column is found by the start of its name, a row reading NONE IDENTIFIED means an empty register, and a dash means a cell says nothing. | VERIFIED | A column is matched by the start of its name, first match first. A row whose first cell reads NONE IDENTIFIED and whose other cells are blank counts as no rows. A dash, a hyphen, NONE or N/A means the cell says nothing. | S1 system_beliefs #4 |
| Routing is written as text, an outcome and a target joined by an arrow, and the code splits it. | VERIFIED | A routing value is written as outcomes and targets joined by arrows and separated by semicolons. Both the judging and the construction split it themselves. | S1 system_beliefs #5 |
| A verdict names no rule set. | VERIFIED | The verdict returned by the judging carries the verdict, the findings and the number of rules evaluated. The command-line check also reports where it read the rules from, as a location on disk. Neither names a rule-set identity. | S1 system_beliefs #6 |
| An approval is silently reopened when the rules move, and nobody is told. | VERIFIED | A document's header carries its phase, its change, its lifecycle state and what it feeds. Nothing records the rule set an approval was given under, and nothing reports when that rule set changes. | S1 system_beliefs #7 |
| A document amended to satisfy a later rule reads exactly like one written under that rule from the start. | VERIFIED | No header field, register or record states that a document was amended to satisfy a later rule. | S1 system_beliefs #8 |
| Every rule written later applies to every document ever written, the next time anyone looks. | VERIFIED | The check judges by the rule set held in the composition it is given. A document judged against its own pinned composition meets the rules of that composition. None of the 33 pins names the working composition, and the working tree rebuilds none of them, so in practice a document meets today's rules. | S1 system_beliefs #9 |
| 32 of 273 delivered documents fail rules that were added after their approval. | VERIFIED | Re-measured against the rules in force and the working composition: 64 of 273 delivered documents are inadmissible. 32 fail on registers or columns added after their approval. The rest fail because their pinned composition is not the working one. | S1 system_beliefs #10 |
| One added column once made every dossier inadmissible, and five delivered dossiers were amended by hand to pass again. | INSUFFICIENT_EVIDENCE | The earlier statement of this change records the instance, and names one commit as holding the reasoning. That commit was not located in the history searched. | S1 system_beliefs #11 |
| The old form leaves a document no exact place to name its rule set. | VERIFIED | The header holds four fields, and the registers hold the change's business facts. Neither has a field for a rule set, and a free-text field would be read through the same conventions as everything else. | S1 system_beliefs #12 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Reads a document's registers | transformation::CT_PURE_PARSE_REGISTERS_V0 | Returns the header, the sections and the registers of a document's text. | PARTIAL | Reads only the old form, through conventions it states nowhere. |
| Reads a document's prior phases | transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | Returns the registers of the upstream documents a phase judges against. | PARTIAL | The same. |
| Judges a document against declared rules | transformation::CT_PURE_EVALUATE_RULES_V0 | Applies every declared rule and returns the verdict and its findings. | PARTIAL | Names no rule set in the verdict it returns. |
| Judges a document | transformation::CC_JUDGE_DOCUMENT_V0 | Composes the reading and the judging into one step. | PARTIAL | The same. |
| Judges a document against the composition | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | Composes the reading and the judging with the facts the snapshot answers. | PARTIAL | The same. |
| Judges a seed | transformation::WF_P0_SEED_ADMISSIBILITY_V0 | Carries the seed's rule set and renders its verdict. | PARTIAL | Carries no rule-set identity. |
| Judges a change request | transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | Carries the change request's rule set and renders its verdict. | PARTIAL | The same. |
| Judges a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2 | Carries the design's rule set and renders its verdict. | PARTIAL | The same. |
| Judges a mandate | transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V1 | Carries the mandate's rule set and gates the approval that ends design. | PARTIAL | The approval it gates names no rule set. |
| Declares what the domain compiles | transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | Declares the design and build subdomains and their sources. | EXACT | Nothing about the form of a document or its rule set. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A document's facts are readable only through conventions held in code. | CRITICAL | Nobody can reproduce a verdict without that code. | VERIFIED | S1 system_beliefs #2 |
| Nothing holds a rule-set identity. | CRITICAL | A document, a verdict and an approval have nothing to name. | VERIFIED | S1 system_beliefs #6 |
| A verdict names no rule set. | CRITICAL | A changed verdict cannot say whether the document or the rules changed. | VERIFIED | S1 system_beliefs #6 |
| An approval names no rule set. | CRITICAL | An approval is reopened silently when the rules move. | VERIFIED | S1 system_beliefs #7 |
| Nothing records that a document was migrated. | MAJOR | A migrated document reads as one authored under the later rules. | VERIFIED | S1 system_beliefs #8 |
| A rule-set version changes whenever its workflow changes, whether or not a rule did. | MAJOR | It cannot serve as an identity that changes only when the rules change. | VERIFIED | S1 known_facts #7 |
| A correction declares nothing about its effectivity. | MAJOR | Nobody can tell a correction that invalidates approved work from one that cannot. | VERIFIED | S1 known_facts #8 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The two problems share one cause. The old form holds facts as text inside prose, so neither a convention nor a rule-set name has an exact place. | The header has four fields; every register is a table read through conventions. | VERIFIED | S1 known_facts #11 |
| Every consumer of a register reads it as data after the reading step. Changing the form changes the reading, not the judging. | The judging, the derivation of rules and the construction all receive registers as data from the reading. | VERIFIED | S1 requested_outcomes #7 |
| The construction half also splits values written inside cells, so it reads the old form too. | Construction splits routing values itself. | VERIFIED | S1 system_beliefs #5 |
| Judging by the rules held in a pinned composition already exists. It protects a document only while its pinned composition can be rebuilt. | None of the 33 pins names the working composition. | VERIFIED | S1 system_beliefs #9 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The instance that shows the problem occurred could not be confirmed from the record. | The commit the earlier statement names was not located. | MINOR | INSUFFICIENT_EVIDENCE | S1 system_beliefs #11 |
| Construction reads the old form, so one form after this change reaches beyond the judging. | Construction splits values inside cells itself. | MAJOR | VERIFIED | S1 constraints #5 |
| A workflow version cannot be the rule-set identity, because it changes for reasons other than the rules. | Seven phases hold a second workflow version. | MAJOR | VERIFIED | S1 business_invariants #4 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
