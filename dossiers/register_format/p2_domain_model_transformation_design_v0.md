# Stage 2 — Domain Model Discovery: transformation / design
**Stage:** 2 — Domain Model Discovery
**CR:** register_format
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, against how the phases
and construction read a document, and against the tests that read delivered dossiers. What was
searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Phase | One step of the transformation lifecycle, with a rule set of its own. | One declared workflow per phase, owned by this subdomain. | VERIFIED | S1 business_vocabulary #1 |
| Rule set | The rules a phase declares, against which it judges a document. | A copy held inside the phase's workflow, produced from the phase's template and its declaration together. | VERIFIED | S1 business_vocabulary #2 |
| Register | The part of a phase document that states facts the rules judge. | A table inside the document's prose, marked by a comment above it. | VERIFIED | S1 business_vocabulary #3 |
| Prose | The part of a phase document that explains the change to a person. | The rest of the same text. | VERIFIED | S1 business_vocabulary #4 |
| Verdict | The result of judging a document against a rule set: admissible or inadmissible. | Returned by the judging, and held by nobody. | VERIFIED | S1 business_vocabulary #5 |
| Finding | One reason a verdict gives for a document being inadmissible. | Part of the verdict: the rule that raised it, where it was found, and a detail. | VERIFIED | S1 business_vocabulary #6 |
| Old form | Registers written as tables inside the prose. | Every phase document and test document today. | VERIFIED | S1 business_vocabulary #7 |
| New form | Registers carried as structured data in a block of their own, apart from the prose. | Nothing holds it. | NOT_FOUND | S1 business_vocabulary #8 |
| Test copy | A copy of a delivered dossier that the construction tests reproduce artifacts from. | Exists for one domain only, as maintained fixtures; every other domain is read from its delivered dossiers. | VERIFIED | S1 business_vocabulary #9 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Register | Structured form | The register's facts, held as data apart from the prose. | NOT_FOUND | S1 requested_outcomes #1 |
| Finding | Rule | The rule that raised it. | VERIFIED | S1 business_vocabulary #6 |
| Finding | Location | The register and row it concerns, written into its text. | VERIFIED | S1 business_vocabulary #6 |
| Finding | Detail | What the rule found. | VERIFIED | S1 business_vocabulary #6 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Judging a document against a phase | The person driving a change | A verdict, and the findings that explain it. | VERIFIED | S1 business_events #1 |
| Reproducing artifacts from delivered dossiers | The construction tests | Each artifact a design determines, compared with the one built. | VERIFIED | S1 system_beliefs #6 |
| Converting a document | Nothing performs it today | A document in the new form. | NOT_FOUND | S1 business_events #2 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Judging a document against a phase | 1 | Read the registers out of the document's text, by the reading conventions. | None. | VERIFIED | S1 system_beliefs #2 |
| Judging a document against a phase | 2 | Judge each rule the phase declares against them. | The findings. | VERIFIED | S1 business_events #1 |
| Judging a document against a phase | 3 | Render the verdict. | The verdict. | VERIFIED | S1 business_events #1 |
| Reproducing artifacts from delivered dossiers | 1 | Read the design and the mandate of each dossier, by the same reading. | None. | VERIFIED | S1 system_beliefs #6 |
| Reproducing artifacts from delivered dossiers | 2 | Render each artifact they determine and compare it with the one built. | A difference report. | VERIFIED | S1 system_beliefs #6 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| A phase document carries prose and registers in one Markdown text, with each register a table inside the prose. | VERIFIED | Each register is a pipe table opened within three lines of a marker comment naming its register. The judging reads the whole text and finds each table by its marker. | S1 system_beliefs #1 |
| The rules read each register through conventions that only the code states. | VERIFIED | The phase's workflow carries its rules and no reading convention. The reading is done by `transformation::CT_PURE_PARSE_REGISTERS_V0`, whose declaration states its inputs and outputs and none of the conventions. No artifact in the pinned snapshot states them. | S1 system_beliefs #2 |
| Fourteen reading conventions and seven formats inside cells exist today. | VERIFIED | Counted from the reading and judging code: fourteen conventions decide what a section, register, table, column, empty register, silent cell, gated row, header field, claim, vocabulary match, pattern and identity are. Seven values inside cells carry a format of their own. | S1 system_beliefs #3 |
| A column is found by the start of its name, a row reading NONE IDENTIFIED means an empty register, and a dash means a cell says nothing. | VERIFIED | A column is matched by the start of its name, first match first. A row whose first cell reads NONE IDENTIFIED and whose other cells are blank counts as no rows. A dash, a hyphen, NONE or N/A means the cell says nothing. | S1 system_beliefs #4 |
| Routing is written as text, an outcome and a target joined by an arrow, and the code splits it. | VERIFIED | A routing value is written as outcomes and targets joined by arrows and separated by semicolons. Both the judging and construction split it themselves. | S1 system_beliefs #5 |
| The construction tests reproduce artifacts from copies of delivered dossiers. | VERIFIED | They read the design and the mandate of 21 dossiers across seven roots: 42 documents. The catalog's 5 dossiers are maintained fixtures; the other 16, in six roots, are read where they were delivered, in the old form. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Reads a document's registers | transformation::CT_PURE_PARSE_REGISTERS_V0 | Returns the header, the sections and the registers of a document's text. | PARTIAL | Read the new form. It reads the old form only, through conventions it states nowhere. |
| Reads a document's prior phases | transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | Returns the registers of the upstream documents a phase judges against. | PARTIAL | The same. |
| Judges a document | transformation::CC_JUDGE_DOCUMENT_V0 | Composes the reading and the judging. | EXACT | Nothing here; it binds the reading by name. |
| Judges a document against the composition | transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | Composes the reading and the judging with the facts the snapshot answers. | EXACT | Nothing here; it binds the reading by name. |
| Judges an analysis loop against the composition | transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | Composes the reading and the judging with the declarations the composition holds. | EXACT | Nothing here; it binds the reading by name. |
| Constructs artifacts from a design | transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Reads a design and a mandate, then measures, renders and writes. | EXACT | Nothing here; it binds the reading by name. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A document's facts are readable only through conventions held in code. | CRITICAL | Nobody can reproduce a verdict without that code. | VERIFIED | S1 system_beliefs #2 |
| No document has a block for structured facts apart from its prose. | CRITICAL | There is nowhere to put the facts but tables inside the prose. | VERIFIED | S1 requested_outcomes #1 |
| Nothing converts a document from the old form to the new. | MAJOR | Neither the test documents nor the test copies can move to the new form. | VERIFIED | S1 business_events #2 |
| Sixteen of the dossiers the construction tests read have no test copy. | MAJOR | Once the old reading retires, the tests lose six of their seven roots. | VERIFIED | S1 system_beliefs #6 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Every consumer of a register reads it as data after one reading step. Changing the form changes the reading, not the judging. | The judging, the derivation of rules and construction all receive registers as data from the reading. | VERIFIED | S1 requested_outcomes #3 |
| The readers' implementation is the old reading itself. Retiring the old reading leaves the readers nothing to run, so they cannot be stood down and carried. | Both readers name one implementation, which reads tables. | VERIFIED | S1 constraints #7 |
| The construction tests read only a dossier's design and mandate, so a test copy needs only those two documents. | Each dossier contributes its design and its mandate and nothing else. | VERIFIED | S1 system_beliefs #6 |
| Dossiers delivered during this cycle are in the old form too, not only those approved under v5. | The construction tests read dossiers delivered in this cycle, in the old form. | VERIFIED | S1 constraints #3 |
| Construction splits values written inside cells itself, so values stay text in the new form. | Construction splits routing values itself. | VERIFIED | S1 system_beliefs #5 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A finding's location is written into its text rather than held apart, so findings are compared as text. | The register and row a finding concerns appear only in its location string. | MINOR | VERIFIED | S1 identity_and_sameness #1 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
