# Transformation Unravel — Rules Out of the Compilers

The Design Compiler and the Construction Compiler are peers of the protocol compiler. Each judges
documents against rules. This document analyses moving the authority for those rules out of Python
and into governed artifacts owned by `transformation`, so that a compiler's behaviour is declared
and its implementation only interprets it.

§0–§3 state the value, the diagnosis, the position and the target shape. §4–§8 are the evidence:
the inventory, the mirror of the protocol architecture, the test corpus and rule coverage. §9 lists
what the analysis has not yet settled. §10 states how the change is delivered once it has.

---

## 0. Strategic value

The test of this change is that an independent implementer can reproduce every verdict from the
artifacts alone, without reading the current implementation. This is the property the protocol
compiler already has.

Measured against that test:

| Needed to reimplement a phase | Visible as an artifact today? |
|---|---|
| Which rules apply, with ids, kinds, params and intent | **Yes.** They are sealed and fully expanded in `WF_P*_ADMISSIBILITY` (242 rules at P7). |
| What each of the 61 check kinds means | **No.** It is defined only by `design/checks.py`. |
| How a document is read: register markers, table rows, sentinels (`NONE IDENTIFIED`), none-markers, governed-hole markers | **No.** It is defined only by `design/read.py` and `checks.py`. |
| What snapshot observations a check may consult | **Partly.** `CC_JUDGE_AGAINST_SNAPSHOT_V1` names the operations. Their use is in code. |
| Why a rule exists | **No.** The reason is in docstrings. |

`scripts/testbed/differential.py` compares the genesis oracle with the compiled phase. Both paths
import `transformation.design.checks` and `transformation.design.read`. The comparison therefore
proves that the rule set travels intact. It does not prove that the semantics are independent.

**Conclusion.** The value is real, but most of it is not where the first framing put it. The rules are
already visible. What an independent implementation lacks is a specification of the **check-kind
vocabulary** and the **document model**. Moving rules out of `rules.py` with no kind specification
does not meet the test. Specifying the kinds meets most of it even before authority is inverted.

What follows from this:

- The highest-value artifact is a check-kind specification: one entry per kind, giving its
  parameters, its document-model inputs, and its exact finding condition. It is the counterpart of
  the protocol compiler's assertion-handler contracts.
- The evidence that the test is met is a second evaluator written from the specification alone that
  agrees finding-for-finding with `checks.py` over the fixture corpus (`fixture_dossiers/cr_01…05`,
  `corpus_p7`).
- Invariants (the reason a rule exists) carry real value for review and citation. They are not needed
  for reimplementation, and come second.
- Where the hand-declared rules live is settled in §6.7: in the register schema, with no new kind.

---

## 1. Diagnosis

### Already separated

- **Check kinds are an interpreter.** `design/checks.py` holds 61 check kinds, each registered with
  `@check(kind)`. A kind knows *how* to test; it names no phase and no register.
- **Rules are declarations.** A `Rule` is `id`, `check`, `register`, `params`, `intent`: data, not code.
  The nine phases declare 883 of them.
- **The rule set checks itself.** `phase meta` proves every rule resolves to a kind and every kind is
  used.
- **Rules are already visible.** `emit_rule_sets` seals each phase's rule set into
  `registry/design/workflows/WF_P*_ADMISSIBILITY_V*.md`.
- **Most rules derive from a document.** Registers, columns and vocabularies come from
  `templates/p*_template_v0.md`. Only the remainder is hand-declared in `p*/rules.py`.

### Not separated

1. **Authority runs the wrong way.** The `WF_P*` artifacts are *generated from* Python. The hand-declared
   rules (250 across the nine phases, 107 of them at P7) have Python as their source of
   truth, and the artifact is a copy of it.
2. **The normative claim has no identity.** The reason a rule exists lives in docstrings: P0 is a
   faithful rewrite only; P7 is where identity becomes binding, so a resolving citation is the
   defect; data-to-decision closure. Nothing can cite these, version them, or show which rules
   realise them.
3. **Shift-left checks restate protocol invariants without citing them.** Some design checks exist to
   catch at design time what the protocol compiler would refuse at S4. One example is the
   step-binding check written after a clock read reached S4. Those checks reproduce a
   `software_governance` invariant and do not name it.
4. **Construction rules are embedded.** `build/completeness.py` and `build/sameness.py` hold their
   measures in code. `sameness` already reads part of its policy from
   `artifact::VOCAB_DECLARATION_REPRESENTATION_V0`, and the rest is inline.

---

## 2. Position

Transformation owns these rules. They govern change, not the governed system, so they belong
under a transformation constitution, not in `software_governance`.

The `INVARIANT` kind is reused, not duplicated. An `IV_` kind would create a second kind for one
concept, and its prefix would sit next to `IN_` (intent).

One invariant per rule (883 files) is the wrong grain. Which protocol concepts carry over, and
which do not, is settled in §6.

Every embedded rule falls into one of three classes:

- **Transformation-owned.** Claims about change documents and construction. These become
  transformation invariants, realised by register-schema annotations or by procedures (§6.7).
- **Shift-left.** Early checks of a protocol invariant. The rule cites the existing
  `software_governance` FQDN and does not restate it.
- **Hygiene.** Fail-fast guards inside the implementation. These stay as code and are not
  governance.

---

## 3. Target shape

- Transformation invariants are `artifact_kind: INVARIANT`, governed by a transformation
  constitution. They are enforced by the phase workflows (`enforcement_stage: enforced_elsewhere`,
  `enforced_by` naming the workflow). §6.2 gives the full mapping.
- The `WF_P*_ADMISSIBILITY` workflows judge against declared artifacts instead of carrying a copy
  generated from Python.
- `p*/rules.py` shrinks to a loader. `checks.py` and the build measures remain the interpreter.
- Register shapes, constraints and invariant-citing annotations live in a register schema per
  phase (§6.7). Expanded rules are derived from it, each with a unique identity (§8.2).
- A closure check extends `phase meta`:
  - every annotation cites an invariant that resolves;
  - every invariant is realised by at least one annotation or procedure, or is declared
    `declared_not_enforced`;
  - every `enforced_by` names a phase workflow that exists;
  - every shift-left annotation or procedure cites a `software_governance` invariant that is in force;
  - every check kind is used.

---

## 4. Inventory

The inventory is read-only. It was taken from `design/checks.py`, `read.py`, `evaluate.py`,
`oracle.py`, `catalog.py`, the nine `p*/rules.py` modules and `build/`.

### 4.1 Rule population

| Phase | Rules | Derived from template | Hand-declared |
|---|---|---|---|
| p0 | 83 | 75 | 8 |
| p1 | 189 | 131 | 58 |
| p2 | 74 | 66 | 8 |
| p3 | 51 | 38 | 13 |
| p4 | 79 | 68 | 11 |
| p5 | 79 | 63 | 16 |
| p6 | 53 | 39 | 14 |
| p7 | 242 | 135 | 107 |
| p8 | 33 | 18 | 15 |
| **Total** | **883** | **633** | **250** |

The 633 derived rules already take their authority from a document, the phase template. Only the
250 hand-declared rules have Python as their source.

### 4.2 The check-kind vocabulary has two tiers

All 61 kinds are used. They fall into two tiers that call for different treatment.

**Tier A: general predicates (27 kinds, 849 rules).** These are parameterised tests over registers,
reused across phases. All of their behaviour is in their params plus the document model (§4.3).

| Kind | Rules | Params | Notes |
|---|---|---|---|
| CELL_NOT_EMPTY | 115 | column, detail, only_when_* | row gate (§4.3 C8) |
| TABLE_PRESENT | 113 | — | absence is a finding, not a skip |
| TABLE_HAS_COLUMNS | 113 | columns | column match by prefix (C3) |
| SOURCE_FINDING_RESOLVES | 76 | column, known_registers, literal_sources | citation grammar (§4.4) |
| CITED_ORDINAL_RESOLVES | 76 | column | reads prior registers |
| CELL_TOKEN_ABSENT | 74 | columns, pattern, detail | regex dialect (C12) |
| TABLE_HAS_ROWS | 64 | minimum (default 1) | sentinel excluded (C5) |
| CELL_IN_VOCABULARY | 44 | column, vocabulary | cell upper-cased; vocabulary compared as written (C11) |
| PRIOR_ROWS_PRESENT_BY_KEY | 20 | prior_phase, prior_register, key_column(s), prior_key_column, prior_only_when_*, registers | key claim join (C10) |
| ROWS_CONFINED_TO_PRIOR | 20 | prior_phase, prior_register, key_column(s), prior_key_column | inverse of the above |
| CELL_RESOLVES_IN_REGISTER | 20 | 14 params (target_*, only_when_*, exempt_prefixes, none_markers, prefer_column) | the widest param contract |
| CELL_MATCHES | 20 | column, pattern, detail, only_when_* | regex dialect (C12) |
| CITATION_ROW_UNRESOLVED | 19 | column | **reads the phase templates and every declared register, beyond its params (§4.5)** |
| REGISTER_COVERS_REGISTER | 11 | source_*, covered_*, only_when_* | none markers (C6) |
| PRIOR_IDENTITIES_COVERED | 10 | prior_*, column, match_on, require, union | |
| UNRESOLVED_MARKER_ABSENT | 9 | markers (default `GOVERNED_HOLE_MARKERS`), exempt, detail | scans every register; strips `*_\`` emphasis |
| HEADER_FIELD_PRESENT | 9 | fields | header from preamble only (C9) |
| HEADER_FIELD_MATCHES | 9 | fields, pattern | anchored at start, not full match (C12) |
| CITED_ARTIFACTS_RESOLVE | 8 | column, pattern, observation, only_when_*, detail_missing | observation-shape normalisation (§4.5); single-edit "near" suggestion |
| ROW_ABSENT_WHEN | 4 | column, value, detail | |
| SECTION_HAS_TEXT, PRIOR_ROWS_CITED, PRIOR_ROW_MATCHES_CITED, TABLE_ROW_COUNT, CITED_ARTIFACTS_ABSENT, OUTCOME_GROUNDED_IN_OPERATION, COLUMN_VALUES_UNIQUE, COLUMN_SEQUENCE_CONTIGUOUS | 2 each | — | |

**Tier B: bespoke procedures (34 kinds, 1 rule each, 26 of them at P7).** Each one is a single rule
whose logic lives in code. Most read hard-coded column names (`Workflow`, `Node`, `Runs`, `Direction`,
`Field`, `Owner`, `Bound To`, `CC Code`, `Step Name`, `Interface`, `Consults`, `Act`, `Store`, …)
instead of taking them as params. Together they hardcode about 100 column references across 30 column
names, and they parse cell sub-grammars (§4.4). These are rules dressed as mechanisms. They are where
the independent-implementation test fails hardest.

| Kind | Phase | Class | Candidate protocol invariant (by name; §9.3 tests each against its text) |
|---|---|---|---|
| TOPOLOGY_KEY_UNIQUE | p7 | shift-left | WF_NODE_KEY_BINDING_UNIQUE, TOPOLOGY_STEP_ID_UNIQUE |
| TOPOLOGY_ROUTE_RESOLVES | p7 | shift-left | WF_ROUTING_CLOSED, TOPOLOGY_ROUTING_COMPLETE |
| NODE_INPUT_BOUND | p7 | shift-left | CC_INPUTS_SATISFIED |
| STEP_INPUTS_BOUND | p7 | shift-left | CC_INPUTS_SATISFIED, TOPOLOGY_INPUT_REFERENCE_DECLARED |
| ENTRANCE_SUPPLIES_GATE | p7 | shift-left | IN_WORKFLOW_BINDING, WF_ENTRY_INTENT |
| STEP_OPERATION_PUBLISHED | p7 | shift-left | CC_CAPABILITY_BINDING_VALID |
| STEP_CONSUMES_PUBLISHED | p7 | shift-left | CC_CAPABILITY_BINDING_VALID |
| CONSUMPTION_GROUNDED_IN_OPERATION | p7 | shift-left | CC_CAPABILITY_BINDING_VALID |
| STEP_INTERFACE_CONFORMS | p7 | shift-left | CT_INPUT_TYPED, CT_SURFACE_CLOSED |
| STEP_BINDINGS_MATCH_INTERFACE | p7 | shift-left | CT_SURFACE_CLOSED |
| BINDING_SOURCE_PUBLISHED | p7 | shift-left | TOPOLOGY_INPUT_REFERENCE_DECLARED |
| BINDING_SOURCE_REACHABLE | p7 | shift-left | TOPOLOGY_INPUT_REFERENCE_DECLARED, BINDING_INTEGRITY |
| BINDING_SOURCE_WELL_FORMED | p7 | shift-left | BINDING_INTEGRITY |
| BINDING_SOURCE_ROOTED | p7 | shift-left | BINDING_INTEGRITY |
| CONTRACT_OUTPUT_PRODUCED | p7 | shift-left | TOPOLOGY_CONTRACT_CLOSED |
| STORE_GROUNDED_IN_CAPABILITY | p7 | shift-left | CC_STORAGE_OP_CONFORMANCE |
| STORE_PATH_MATCHES_STORAGE | p7 | shift-left | CC_STORAGE_OP_CONFORMANCE |
| CROSS_SUBDOMAIN_REACH_READ_ONLY | p7 | shift-left | RB_STORAGE_SUBDOMAIN_OWNED |
| READ_IS_DECLARED | p7 | shift-left | RB_BINDING_POLICY_CONFORMANCE |
| REACH_IS_USED | p7 | shift-left | RB_BINDING_POLICY_CONFORMANCE |
| IMPLEMENTATION_MODULE_CONFORMS | p7 | shift-left | IMPLEMENTATION_ADMISSIBLE |
| CELL_PARSES_AS_YAML | p7 | shift-left | TEST_DATA_MATCH_CT_OUTPUT |
| INTERPRETATION_TRANSFORM_REFUSES | p7 | **protocol gap** | none: data-to-decision closure was found because the compiler admitted its violation (CR-1) |
| DISCHARGE_GROUNDED_IN_TOPOLOGY | p7 | transformation-owned | refusal discharge |
| DISCHARGE_OUTCOME_REFUSES | p7 | transformation-owned | refusal discharge |
| GOVERNING_RULE_IN_SEALED_SET | p7 | transformation-owned | rule pinning |
| EMISSION_GROUNDED_IN_ENDING | p7 | transformation-owned | announcement design; touches WF_ANNOUNCEMENT_DISTINCT |
| DEPENDENCY_PRECEDES | p8 | transformation-owned | build order is a sort |
| COLUMN_ABSENT | p0 | transformation-owned | truth/belief split |
| CELL_NOT_PREFIXED | p0 | transformation-owned | belief never promoted to fact |
| REUSE_CANDIDATE_ELIGIBLE | p3 | transformation-owned | reuse only from a permitting domain |
| CELL_PREFIXED_BY_COLUMN | p5 | transformation-owned | provisional family agreement |
| PRIOR_PROSE_CARRIED | p5 | transformation-owned | purpose authored once |

Three of the p0, p5 and p3 entries (COLUMN_ABSENT, CELL_NOT_PREFIXED, CELL_PREFIXED_BY_COLUMN) are
already general predicates that happen to be used once. They belong to tier A in substance.

### 4.3 Document-model conventions stated in no artifact

An independent reader has to reproduce each of these. Today each is defined only by code.

| # | Convention | Source |
|---|---|---|
| C1 | A section is a `##` heading, optionally numbered `N.` or `Na.`. Deeper headings do not break sections. | `read.HEADING` |
| C2 | A register is `<!-- register:id -->`. Its table must open within the next 3 lines, or else it is narrative up to the next heading or marker. The first register with an id wins. | `read.parse_text`, `evaluate._register_block` |
| C3 | A column is addressed by **prefix**, and the first header that starts with the name wins. | `checks._cell` |
| C4 | A table is the first pipe table with a divider row. Ragged rows are padded or truncated. `\|` escapes a pipe. A duplicate header keeps the last cell. | `read._read_table`, `_split_row` |
| C5 | The emptiness sentinel is a row whose first cell is `NONE IDENTIFIED` (any case) and whose other cells are blank. It is not content, but it still counts in row numbering. | `checks.is_sentinel`, `_content_rows` |
| C6 | The none markers are `—`, `-`, `NONE` and `N/A`. A cell holding one says nothing. Some kinds take their own `none_markers` instead. | `checks.NONE_MARKERS` |
| C7 | A register rule with no marker in the document falls back to a case-insensitive section-title prefix match on the register id. | `checks._block`, `DeclaredRule.from_mapping` |
| C8 | `only_when_column` with `only_when_value`, or with `only_when_values`, gates rows. The comparison is case-insensitive. | `checks._gated_out` |
| C9 | Header fields are `**Name:** value` lines, bulleted or bare, read only before the first `##`. | `read.BULLET_FIELD` |
| C10 | A row's claim is its key columns, each whitespace-normalised, joined with ` · `. | `checks._claim` |
| C11 | Vocabulary membership upper-cases the cell and compares it with the vocabulary as written, so vocabularies must be upper-case. | `_cell_in_vocabulary` |
| C12 | Patterns use Python `re`. `pattern.match` (anchored at the start) and search are both in use, and which one applies is per kind. | several |
| C13 | An identity is compared bare: whitespace-normalised, with everything up to the last `::` dropped. | `checks._bare_identity` |
| C14 | A prior phase that was not supplied is a distinct finding from a supplied prior that lacks the register. | `evaluate.has_prior`, `checks._prior_rows` |

### 4.4 Cell sub-grammars

Several cells carry a grammar of their own. None of these grammars is declared anywhere.

- **Routing:** `OUTCOME -> destination; …`. Malformed segments are dropped silently.
- **Interface:** `in: cap=design, …; out: cap=design, …`.
- **Citation, two idioms:** `<register_id> #n` (an optional stage prefix is ignored), and `§N … #n` for
  the seed, resolved through the template's section numbers.
- **Name list:** comma-separated, with the dash markers dropped.
- **Binding source:** an input pattern and an output pattern, given as params, plus numeric literals
  (`_is_number`).
- **Test value:** YAML.
- **Artifact token:** `derive.ARTIFACT_TOKEN_PATTERN`, a closed family list (`AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF`).

### 4.5 Inputs beyond the rule's params

- **Templates.** `CITATION_ROW_UNRESOLVED` loads the prior phase's template and every declared register
  (`template_reader.load`, `derive._all_declared_registers`). Its verdict depends on files that the
  sealed rule never names.
- **Param defaults.** Some defaults live in code, not in the sealed rule: `topology_register` defaults to
  `execution_topology`, `workflow_column` to `Workflow`, `node_column` to `Node`, `minimum` to 1, and
  `markers` to `GOVERNED_HOLE_MARKERS`.
- **Observation shapes.** Kinds read fields of `si.*` results that only code names, for example
  `artifact|fqdn|fqdn_id`, `domain`, `operations[].output|input|result_status_values`, `capability`,
  `category`, `transform`, `refusal`, `steps[].store`, `bindings`, `key` and `store`.
  `CC_JUDGE_AGAINST_SNAPSHOT_V1` names the operations, but not the fields read from them.
- **Derive constants.** `LITERAL_SOURCES` (`CR seed`, `human decision`, `projection`, `S1 seed`) is
  sealed into params, which is fine. The family list in the artifact-token pattern is code.

### 4.6 Finding identity

A finding is `(rule, where, detail, intent)`.

- **`where` is free text.** 46 of the 61 kinds write `"<register> row N"`. The other 15 write the
  register, or `header`, or `document`.
- **The column and the offending value appear only in `detail`.**
- **`rule` is a finding code, not a rule identity** (§9.2).

So finding-for-finding equivalence between two implementations can be judged only by parsing
`where` and matching `detail` as English text. A conformance test needs a structured locator: row
ordinal, column and value.

### 4.7 Invariant candidates

- **Phase key rules (9).** These are already declared, in `catalog.PHASES[].key_rule`. Examples:
  "Faithful rewrite only — no content added, no clarification resolved, no design assigned" (p0),
  "Consolidation, not re-litigation" (p4), and "No new artifact codes; cross-subdomain writes
  forbidden" (p6).
- **Cross-cutting doctrine** stated in docstrings:
  - emptiness is declared, never inferred;
  - every rule is evaluated, with no short-circuit;
  - there is no warning tier;
  - an unchecked handoff must not look like a preserved one;
  - identity becomes binding at P7, where a resolving citation is the defect;
  - data-to-decision closure;
  - absence of a register is a finding, not a skip.
- **Rule groups (35 named groups).** Examples are `SEED_DISCIPLINE_RULES`, `BELIEF_PRESERVATION_RULES`,
  `CONSOLIDATION_RULES`, `PURITY_RULES`, `PLACEMENT_RULES`, and P7's `BINDING`, `INTERFACE`,
  `MOLECULE` and `REFUSAL` groups. A group is the natural unit for "the rules that realise one
  invariant".

On this evidence an invariant set is a few dozen claims, not hundreds.

### 4.8 Class 3 (hygiene)

No rule is hygiene. Implementation guards exist, such as fail-hard dispatch, the duplicate-kind
check, and a reader that never raises, but they sit outside the rule set already.

### 4.9 Construction compiler

Construction holds its behaviour in a different form. It is a mapping, not a predicate set.

- **`render.py` (1,397 lines)** maps P7 and P8 registers to Machine-block fields, family by family
  (`_BUILDERS`, `BUILD_PHASES`). It uses code-held tables: `INTENT_OUTCOMES`, `TRANSFORM_CONSTITUTIONS`,
  `HEADER_ONLY_PROPERTIES`, `WORKFLOW_STRUCTURE`, and the four provenance classes
  (`stated_by_design`, `governed_elsewhere`, `supplied_by_renderer`, `carried_from_predecessor`).
- **`completeness.py`** derives its requirement list from `render`, so it cannot drift from it, and it
  is specified exactly as well as `render` is.
- **`sameness.py`** is already half-declared. Its policy is `artifact::VOCAB_DECLARATION_REPRESENTATION_V0`,
  but the subset of declared rules it applies (`APPLIED`) is code.
- **`generators.py`** is a closed registry in code, like the check-kind registry.

For construction, the independent-implementation test calls for a **mapping specification**: register
column to artifact field, with a provenance class for each. That is a different and larger artifact
than a check-kind specification.

---

## 5. What the inventory changes

1. **Most of the gain is cheap.** Tier A (27 kinds) plus the document model (C1–C14) plus the
   sub-grammars specify 849 of the 883 rules. That is where specification starts.
2. **Tier B needs a decision per kind, not a specification per kind.** That means 34 kinds, or 29
   once the five general predicates that happen to be used once are set aside (§6.7). For each
   there are three options:
   - re-express it as a tier-A kind over declared column params, which removes the hard-coded columns;
   - for shift-left kinds, cite the protocol invariant and specify the kind as that invariant's
     early check;
   - keep it as a named procedure with its own specification.

   A specification that copied 34 procedures out of code would be exactly what this change exists to
   replace.
3. **The protocol has a gap.** Data-to-decision closure (`INTERPRETATION_TRANSFORM_REFUSES`) is enforced
   only at design time. The protocol compiler admitted a violation of it. This is a candidate
   `software_governance` invariant, and the design rule would then become shift-left. §9.3 finds
   eleven more composition properties in the same position.
4. **Finding identity comes before the differential.** Add a structured locator to findings first.
   Otherwise a second evaluator can be compared only by message text.
5. **Hidden inputs must become params.** The template reads in `CITATION_ROW_UNRESOLVED` and the
   code-held param defaults belong in the sealed rule. Then a rule set is closed under what it names.
6. **Authority inversion is smaller than it looked.** It concerns the 250 hand-declared rules, not 883.
   §6.7 settles where the hand-declared rules go.
7. **Construction is a different kind of work.** It needs a mapping specification, not a check
   specification. Whether it belongs to this change is open (§9.7).

---

## 6. Mirroring the protocol architecture

A protocol concept carries over only where it does the same job on the transformation side. Where
no protocol concept does the job, the asymmetry is stated and not stretched over.

### 6.1 How the protocol side actually works

- **Invariant, assert and handler are one to one to one.** `INVARIANT_ASSERT_PARITY_V0` requires
  exactly one `ASSERT_*` per `INVARIANT_*`, and the build derives the `ASSERT`. Each has its own
  handler module (102 in `governance_engine/assertions/handlers/`). There is no parameterised rule
  language: every check is a dedicated procedure.
- **The invariant's prose is the handler's specification.** `core.description`, `anti_patterns` and
  `clarification` state what the handler must refuse. A reimplementer reads these, not the handler.
- **Shape is JSON Schema.** The schema files live in `software_governance/registry/schema/` and are
  selected per kind by `STRUCTURE_SCHEMA_DISPATCH_V0`. The schema language is an external standard,
  so its semantics come for free.
- **`STRUCTURE` is declared configuration and dispatch, not document shape.** Examples are the
  scheduling mode, the placement profile, the schema dispatch table, and transformation's own
  `STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0` and `STRUCTURE_FIGURE_OF_MERIT_POLICY_V*`.
- **`CONSTITUTION` is one per concern.** It states what the concern covers and who holds authority.
- **An invariant need not be enforced by the compiler.** `enforcement_stage: enforced_elsewhere` with
  `enforced_by` is an established form, used by `ASSERT_PARITY` itself.
- **Transformation has no constitution of its own.** Its registry artifacts (`WF`, `CC`, `CT`, `IN`,
  `RB`, `AC`, `VOCAB`, `STRUCTURE`) are ordinary protocol artifacts, governed by platform
  constitutions. What has no constitution is the concern those artifacts implement: admissibility of
  change documents, and determinacy of construction.

### 6.2 Mappings that hold

| Protocol concept | Same job on the transformation side |
|---|---|
| `CONSTITUTION` per concern | One per transformation concern: design admissibility and construction determinacy. These match the repo's two subdomains, `design` and `build`. |
| `INVARIANT` + derived `ASSERT` + one handler | **Tier B** (§4.2). Each of the 34 bespoke kinds is one rule with its own procedure, the protocol pattern exactly. Each becomes an `INVARIANT` whose prose specifies the procedure, `enforced_elsewhere` and enforced by its phase workflow. Shift-left ones cite the protocol invariant they anticipate. |
| `INVARIANT` (doctrine) | The phase key rules (`catalog.PHASES[].key_rule`) and the cross-cutting doctrine in §4.7. |
| `VOCAB` | The controlled vocabularies now written inline in template column headers, plus lifecycle states, none markers, the emptiness sentinel and the artifact family list. |
| `STRUCTURE` | Dispatch and configuration only: phase → shape, phase → workflow, figure-of-merit policy. |
| Schema files + `STRUCTURE_SCHEMA_DISPATCH_V0` | Register shapes per phase (registers, columns, optionality, flags), taken out of the templates. |
| `TEST_DATA` for a transform | Vectors for the evaluator transforms (`ct_pure_evaluate_rules_v0`, `ct_pure_parse_registers_v0`): small register payloads paired with expected findings, one set per handler. |

### 6.3 Mappings rejected

- **Templates as `STRUCTURE`.** `STRUCTURE` is configuration. Document shape is schema's job.
- **Template-derived rules as `ASSERT`.** An `ASSERT` derives from a normative claim. These rules
  derive from shape, so they are schema validation. The protocol side does not materialise schema
  checks as rules at all, because its validator applies the schema directly. Sealing the 633
  expanded rules is a transformation choice. It is kept only if it earns its place (for example
  through rule pinning in `rule_effectivity`), and it is labelled derived either way.
- **Dossiers as `TEST_DATA`.** Dossiers are evidence, not artifacts, and must not enter the
  snapshot. The fixture corpus remains testbed evidence. Only per-handler vectors qualify.
- **A new `IV_` kind.** It would duplicate `INVARIANT`.

### 6.4 An asymmetry that is kept

**Tier A, the parameterised rule language, has no protocol counterpart, and should not be forced into
one.** The protocol side judges YAML, so it borrows JSON Schema and needs no language of its own.
Transformation judges Markdown registers. No external schema language covers prefix-matched columns,
emptiness sentinels, cross-phase row preservation or citation ordinals, so transformation owns one.

The counterpart of JSON Schema's specification is therefore a **standard document**, not an artifact
kind. It covers:

- the document model (C1–C14);
- the cell sub-grammars (§4.4);
- the semantics of the 27 general kinds;
- the finding shape, with a structured locator (§4.6).

It sits beside the protocol's Machine Block specification, and it is what an independent evaluator
is written from.

### 6.5 Templates, unbundled

A template does four jobs today. Each goes to the place that already does that job:

| Content of a template | Goes to |
|---|---|
| Registers, columns, optionality, per-register flags | the phase's register schema (§6.2) |
| Inline controlled vocabularies | `VOCAB` |
| Rule hints such as `business_language=capability` | the register schema, as declared flags |
| Elicitation prose, the document contract, guidance to the author | the template, which remains a human guide |

The register schema is the authority. The template's register skeleton is checked against it, or
generated from it. Two authorities for one shape would recreate the drift this change removes.
`derive.py` (schema → expanded rules) needs specifying only for an independent *authoring*
toolchain. An independent evaluator reads sealed rules or the schema directly.

### 6.6 Enforcement outside the compiler, verified

`protocol_compiler/compiler/stages/s4_govern.py` (`_NON_COMPILER_STAGES`, `_derive_assert`) settles
it:

- An invariant whose `enforcement_stage` includes `enforced_elsewhere` derives **no** `ASSERT`, so no
  handler is demanded. The code says why: a handler written only to satisfy the demand would pass
  unconditionally.
- `SCHEMA_INVARIANT_V0` requires `core.enforced_by` whenever the stage routes enforcement elsewhere,
  and refuses it otherwise. The field is a free string. The schema does not check that it resolves.
- The invariant must still be named by a constitution rule. `ASSERT_GOVERNANCE_DECLARATION_RESOLVES`
  checks this.
- `runtime_outcome` looks closer, since it is enforced by a CC outcome and WF routing. It is not a
  fit: its required `runtime_binding.over_store` names a business store, and a phase judgement is
  over a document, not a store.

So transformation invariants are `enforced_elsewhere`, with `enforced_by` naming the phase workflow.
Nothing on the protocol side proves that name resolves. The transformation closure check (§3) must
prove it.

### 6.7 The rule-group test

**The test was whether each named rule group states exactly one claim. It fails.** The groups are
organised by register and theme, not by claim:

- `DECISION_RULES` carries six claims: reuse eligibility, alternatives shown, rationale given,
  alternatives exist, impact evidenced, and verification evidenced.
- `PURITY_RULES` carries seven, and `PLACEMENT_RULES` eight.
- `BINDING_RULES` (23), `INTERFACE_RULES` (19) and `MOLECULE_RULES` (18) each mix identity, topology,
  reach, interface, store and format claims.

Option (a), an invariant per group, is therefore not available as framed. It also fails a second
way: `SCHEMA_INVARIANT_V0` has `additionalProperties: false` at the top level and in `core`. Carrying
rule bindings in an invariant would change a protocol schema to accommodate a transformation
need, which is the force-fit this section exists to avoid.

**Sorting the 250 hand-declared rules by what they constrain gives a different answer:**

| What the rule constrains | Rules | Distinct claims | Where it belongs |
|---|---|---|---|
| Shape: required cell, conditionally required cell, pattern, enumeration, uniqueness, row cardinality, header fields | 86 | each its own | the register schema, as constraints |
| References inside the document: a cell resolves in another register, one register covers another, a sequence is contiguous | 33 | each its own | the register schema, as references and cardinality |
| Carriage between phases: nothing dropped, nothing invented, restated rows cite and match their source, citations resolve | 74 | a handful | the register schema, as annotations that cite an invariant |
| Grounding against the snapshot: cited identities exist, new identities do not, reuse comes only from a permitting domain | 11 | three | the register schema, as annotations that cite an invariant |
| Closure: no governed hole left open, no blocking or business clarification outstanding | 13 | three | the register schema, as annotations that cite an invariant |
| Rung purity: no binding token below the rung that admits it | 4 | one | the register schema, as annotations that cite an invariant |
| Bespoke procedures (tier B, §4.2) | 29 | each its own | `INVARIANT`, one to one, `enforced_elsewhere` |

The shape and reference rows are what a schema does on the protocol side. The protocol uses JSON
Schema there, with descriptions, `if`/`then` and enumerations.

The carriage, grounding, closure and purity rows are a small set of normative claims (about a dozen
by this reading). Each is applied register by register. A claim applied per register is an
**annotation on the register** that cites the invariant it realises. That has the same structure as
a protocol constitution rule citing its invariant with `rules[].enforced_by`.

**Conclusion.** The register schema carries the shape, the references, and the invariant-citing
annotations. The invariants carry the claims. Expanded rules are derived from the schema, as the 633
template-derived rules already are. That leaves:

- no rule set to author;
- no `RULE_SET` kind;
- no change to the protocol's invariant schema.

The test that would refute this is a hand-declared rule that is neither a schema constraint nor an
application of a declared claim. Of the 250, only the 29 tier-B procedures are, and they are
invariants in their own right.

---

## 7. The test corpus

### 7.1 What exists

| Corpus | Size | What it exercises |
|---|---|---|
| Authored dossiers across six domains (`cr_dossiers/`, `dossiers/`) | 34 dossiers, 307 phase documents | real changes, almost all admissible |
| Testbed negatives (`scripts/testbed/corpus*`) | 71 documents, 69 inadmissible | one defect per document, verdict and finding count asserted by `e2e_phases_test.py` |
| Testbed fixtures (`fixture_dossiers/cr_01…05`) | 5 dossiers | the differential's seeds |

### 7.2 What it can prove

Yes, the corpus serves. The unravel changes where rules are declared, not what they judge, so its
acceptance test is **identity of verdicts**: every document, before and after, gives the same
verdict and the same findings, including `detail` text. Both sides run the same `checks.py`, so
exact text comparison is valid here. The structured locator in §4.6 is needed only later, for an
independent evaluator.

- **The authored dossiers prove the absence of new false refusals.** A rule that tightened by
  accident in the move refuses a document that passes today.
- **The testbed negatives prove the absence of lost refusals.** A rule that loosened by accident,
  or went missing, stops a finding that fires today.

### 7.3 What it cannot prove yet

1. **Coverage is unmeasured.** Nothing records which of the 883 rules fire on at least one
   document. A rule that fires on nothing can disappear in the move and every comparison stays
   green. Rule-level coverage must be measured first. Every rule that never fires needs a negative
   document before the move, or a recorded reason why none can exist.
2. **Pinned snapshots may be gone.** Grounding rules and most tier-B kinds read `observed`, which
   comes from the dossier's pinned snapshot. Many pins name compositions that no longer exist as a
   build. The fix is to record each document's `observed` and `priors` once, under today's code, and
   replay them, so the comparison depends on no snapshot.
3. **Old verdicts are not all admissible.** Rules are retroactive (`rule_effectivity`), so a delivered
   dossier may carry findings under today's rules. The baseline is whatever today's code returns,
   recorded, not an assumption that every delivered dossier passes.
4. **A negative isolates one defect.** It shows that a rule fires, not that it fires alone.
   `e2e_phases_test.py` already asserts the exact set of rule ids that fire for each payload. The
   recorded baseline adds `where` and `detail`.

### 7.4 Its status

The corpus remains **testbed evidence**, not `TEST_DATA` (§6.3). Dossiers stay out of the snapshot.
The recorded verdicts (document, observations, priors, findings) are a testbed artifact of this
change. They are produced before the move and compared after it.

---

## 8. Rule coverage

### 8.1 Method

A read-only harness judged every corpus document in-process with `oracle.evaluate`. It used the
working-tree rule sets, priors resolved the way `scripts/testbed/priors.py` resolves them, and
observations gathered the way `tc phase check` gathers them.

- **Testbed documents and e2e payloads** were judged against the CR-1 design baseline that
  `e2e_phases_test.design_baseline()` reproduces, which is also what the e2e suite and the
  differential use.
- **Authored dossiers** were judged against the working `snapshot/`.

As a check on the harness itself, it reproduces all 83 e2e cases exactly, with the same verdict and
the same set of rule ids.

| Corpus | Documents |
|---|---|
| Intended negatives (testbed `inadmissible_*` and inadmissible e2e payloads) | 138 |
| Admissible probes (testbed and e2e) | 16 |
| Authored dossier documents (33 dossiers with a seed) | 273 |

### 8.2 A rule has no unique identity

`(phase, id, register, check)` identifies 877 of the 883 rules. The other six share it with a
sibling. Each is the same vocabulary rule applied to two or three columns of one register
(`CELL_NOT_IN_VOCABULARY` on `clarification_requests` in p0 and p1, on `analysis_findings` in p3, and
on `interface_fields` and `transport_bindings` in p7). They differ only in `params.column`.

§9.2 analyses what a rule identity should be. The figures below count the 877 distinct keys.

### 8.3 Coverage

| Phase | Rules | Fire on a negative | Fire only on an authored document | Never fire |
|---|---|---|---|---|
| p0 | 82 | 45 | 0 | 37 |
| p1 | 188 | 129 | 1 | 58 |
| p2 | 74 | 48 | 0 | 26 |
| p3 | 49 | 31 | 0 | 18 |
| p4 | 79 | 51 | 0 | 28 |
| p5 | 79 | 57 | 2 | 20 |
| p6 | 53 | 41 | 0 | 12 |
| p7 | 240 | 149 | 18 | 73 |
| p8 | 33 | 20 | 0 | 13 |
| **Total** | **877** | **571 (65%)** | **21** | **285 (32%)** |

By source:

| Source | Rules | Fire on a negative | Never fire |
|---|---|---|---|
| Derived from templates | 627 | 374 | 238 |
| Hand-declared | 250 | 197 | 47 |

**What never fires.**

- **The derived rules that never fire are almost all per-register structure:** `TABLE_HAS_COLUMNS`
  (100), `TABLE_PRESENT` (82) and `TABLE_HAS_ROWS` (55). Each negative removes one register or one
  column, so most register instances of these kinds are never exercised. The kinds themselves fire.
- **Of the 47 hand-declared rules that never fire, 29 are named in a dedicated design test**
  (`molecule_design_test.py`, `vector_design_test.py`, `vector_value_design_test.py`,
  `keyed_node_design_test.py`, `entrance_gate_design_test.py`). Those scripts build their own cases
  inline and were not part of this run. That a rule is named there is not proof that it fires.
- **18 hand-declared rules are exercised nowhere:**
  - `SEED_ROW_NOT_CARRIED` on 12 of its 17 registers (only `business_invariants`,
    `acceptance_criteria`, `known_facts`, `assumptions` and `business_events` are exercised);
  - `BORROWED_CAPABILITY_NOT_DECLARED_CROSSING` (p6);
  - `SATISFIED_DEPENDENCY_NOT_INVENTORIED`, `WORKFLOW_WITHOUT_TOPOLOGY`,
    `TRANSFORM_WITHOUT_IMPLEMENTATION` and `VOCABULARY_WITHOUT_VALUES` (p7);
  - `UNDECLARED_REACH_READ` (p7). This is the only tier-B kind, `READ_IS_DECLARED`, with no negative
    anywhere.
- **Four check kinds never fire in the three corpora:** `TOPOLOGY_KEY_UNIQUE`,
  `ENTRANCE_SUPPLIES_GATE`, `CELL_PARSES_AS_YAML` and `READ_IS_DECLARED`. The first three have
  design tests. The fourth has none.

### 8.4 The authored dossiers under today's rules

- **No pin matches the working snapshot.** All 33 pins name compositions other than today's.
- **64 of 273 documents are inadmissible today**, across 25 of the 33 dossiers. Their causes:
  - **32 are retroactive structure:** `REGISTER_COLUMN_MISSING` (26) and `REGISTER_MISSING` (19), with
    `REFUSAL_UNACCOUNTED`, `WITHDRAWAL_IS_A_CHANGE_OF_MEANING` and the vector rules behind them.
    These documents were admissible when approved, and rules added since reject them. This is the
    `rule_effectivity` problem, measured.
  - **The rest are grounding against the wrong composition:** `NEW_CODE_ALREADY_EXISTS` (15) and
    `BUILD_CODE_ALREADY_EXISTS` (15) fire because today's snapshot holds what those dossiers
    authored. `*_IDENTITY_UNRESOLVED` fires because it no longer holds what they cited.

**Consequence for §7.** The authored corpus cannot be used as "admissible, so must stay
admissible". It serves only through the recorded baseline: today's verdict and findings for each
document, with its observations and priors captured once and replayed.

### 8.5 What this means for the acceptance test

Behavioural comparison alone cannot cover the third of the rules that never fire. A rule lost in
the move would go unnoticed. Two levels of acceptance close that:

1. **Declaration identity.** The expanded rule set after the move equals the expanded rule set
   before it, rule for rule: id, check, register, params, intent. This covers all 883 rules,
   whether they fire or not. It compares the full content of each rule as a multiset, so it needs no
   rule identity. A rule identity (§9.2) is needed only to *report* which rule differs. The
   differential already compares rule sets at this level, between the Python declaration and the
   sealed copy.
2. **Behavioural identity.** The recorded baseline replays identically. This covers the evaluator,
   the document model and the evaluation path, which a declaration comparison cannot see.

The coverage gap matters for the work that changes behaviour, not for the move:

- tier-B kinds re-expressed as general kinds (§5, item 2);
- an independent evaluator written from the specification (§0).

Each of those needs a negative for every rule it touches. The 18 rules exercised nowhere, and
`READ_IS_DECLARED` above all, need negatives before that work starts.

---

## 9. Open questions

The analysis has not yet settled these. Each one changes what is delivered. A question that has been
analysed carries its analysis and a proposed answer.

### Decision checklist

**Governing constraint.** Strategic, not a workaround, and KISS. v6 is not backward compatible with
v5. The v5 composition, its dossiers and its evidence remain as published, at tag `v5`.

**Settled.**

- [x] Registers move to a YAML Machine block in every register-bearing phase document, seed to
  mandate. Prose stays Markdown (§9.9).
- [x] The work is four changes, in order and not conflated: format, then structure, then the design
  unravel, then construction. The protocol fixes are a separate track (§9.9, §9.7).
- [x] `rule_effectivity` is re-authored from p0 as the format change. Its asks become that change's
  acceptance obligations (§9.6).
- [x] No Markdown reader survives into v6. Delivered v5 dossiers are neither converted nor read. The
  test corpus is converted once, mechanically, and the old reader is used only to prove that
  conversion (§9.9).
- [x] No `IV_` kind. Transformation invariants reuse `INVARIANT`, with
  `enforcement_stage: enforced_elsewhere` (§2, §6.6).
- [x] Protocol defects are fixed only by designed, versioned changes, never in place (§9.4).
- [x] **Approvals re-confirm.** When the rule set an approval was given under is superseded, the
  approval stands unconfirmed until a human re-confirms it against the new set (§9.6).
- [x] **A document names its register schema's `$id`**, the stabler of the two identities (§9.6).
- [x] **Schema files are JSON**, as every protocol schema is (§9.1).
- [x] **Vocabularies are `VOCAB` artifacts:** declared once, visible, and referenced by the schema,
  never copied into it (§9.1).
- [x] **The general-language extensions dissolve.** Under YAML and JSON Schema none needs a home-grown
  kind (§9.3).
- [x] **Independent construction is a goal**, by separation of concerns: its own change, constitution,
  invariants and mapping standard, as for the design compiler (§9.7).
- [x] **Carrier.** Register schemas are JSON Schema substrate files sealed into the `WF_P*` workflows,
  option (A) (§9.1, §9.8).
- [x] **Rule identity.** The schema `$id` plus a JSON Pointer; for a tier-B rule, its invariant's FQDN
  (§9.2). The `$id` is the rule-set identity a document, a verdict and an approval name.
- [x] **Effectivity is recorded in the schema's revision history.** A correction declares there whether
  it is retroactive. No separate artifact holds it (§9.6).
- [x] **The schema file arrives with the format change, carrying identity only.** Each phase's register
  schema holds its `$id`, a digest of the rule set sealed in its `WF_P*`, and its revision history.
  `phase emit --check` refuses sealed rules that differ from the digest unless a revision records
  the change, and a retroactive revision takes a new `$id`. The design unravel fills in the shape
  under the same `$id`, as a non-retroactive revision (§9.6, §9.9).
- [x] **In-flight dossiers need no special handling.** A dossier open when its rule set changes falls
  under the re-confirmation policy (§9.6).

**Proposed; awaiting confirmation.**

- [ ] **Tier B dispositions.** R 7 / S 2 / T 7 / G 12 (§9.3).
- [ ] **Invariant set and names.** 14 design and 4 construction invariants. `NOTHING_DROPPED` and
  `NOTHING_INVENTED` are kept separate (§9.5).
- [ ] **Constitutions.** Two, one per concern: `design` and `build` (§9.5).

**Obligations carried into later changes.** Found while delivering `binding_literals` and
`quoted_literals`, which change 1 waited on. Each is owned by the change named, and closes there.

- [ ] **Structure (change 2): `generated` becomes a typed marker.** It is a reserved word in a string
  cell today, read case-insensitively. That is a sub-grammar, which is what change 2 removes. Under
  YAML a generated value is stated by its own key or tag, never by a word a literal could also spell.
- [ ] **Design unravel (change 3): one specification of a literal.** The design side defines a literal
  in `LITERAL_FORMS` (`p7_design_intent/rules.py`) and construction in `render._binding`. They agree
  today and nothing holds them together. The language specification states it once, and both read it.
- [ ] **Construction (change 4): the render transform's vectors pin how a literal renders.**
  `quoted_literals` corrected `CT_PURE_RENDER_ARTIFACTS_V0`'s implementation without a new identity,
  because its declaration says nothing about literals. A behaviour the declaration does not state is
  one sameness cannot see; test vectors make it declared.

**Separate track, outside `transformation`.**

- [ ] Propose the 12 G properties as `software_governance` invariants, initially
  `declared_not_enforced` (§9.4, §9.5).
- [ ] A designed, versioned fix for the protocol defects of §9.4. The 11 payload bindings close
  through blockchain GAP-09 first.
- [ ] Vocabulary drift on the protocol side: `SCHEMA_INVARIANT_V0` admits the enforcement stage
  `compiler_discovery`, which `VOCAB_ENFORCEMENT_STATUS_V0` does not list. The schema copies a
  vocabulary instead of referencing it (§9.1).

### 9.1 Register-schema format

**Facts.**

- **What templates declare today.** The 9 templates carry 115 registers. A register is declared by
  `<!-- register:id flags -->` above a header row. Columns come from the header, and inline
  vocabularies from the header text (`Direction (INPUT, OUTPUT, ATTRIBUTE)`). There are three flags:
  `optional` (50 registers), `business_language` with an optional scope (72), and `optional_columns`
  (1). `template_reader.Register` holds the result: id, section number, title, columns,
  vocabularies, flags and scoped flags.
- **How the protocol declares shape.** It uses JSON Schema (draft 2020-12) files in
  `software_governance/registry/schema/`. Each has an `$id` such as
  `software_governance.schemas.SCHEMA_INVARIANT_V0`, and `STRUCTURE_SCHEMA_DISPATCH_V0` (an artifact)
  selects one per kind. The schema files are **not artifacts**: `SCHEMA` has no `artifact_kind` in
  the compiler's kind registry. They are **not in the snapshot**: the compiler reads them from the
  governance registry when it validates artifacts, before sealing.
- **Where transformation judges.** At runtime. `CC_JUDGE_DOCUMENT_V0` runs inside a `WF_P*` workflow,
  and its rules arrive as a literal node input (`inputs.rule_set`) sealed in the workflow's Machine
  block. Whatever judges a document must therefore be in the snapshot. Nothing may enter at
  execution that the snapshot does not hold.
- **No existing artifact kind carries a shape.** `STRUCTURE` is constitutionally the configuration
  authority for discovery, loading and routing (`CONSTITUTION_STRUCTURE_V0` §1). `ENTITY` is a
  registered prefix with no artifact, no schema and no constitution anywhere in the workspace.
  `SCHEMA` is not an artifact kind.

**Can JSON Schema itself be the format?** Measured over the 883 rules, applied to the parsed
register data:

| | Rules |
|---|---|
| Expressible in JSON Schema in principle: presence, columns, row counts, required cells, enumerations, patterns, header fields, prohibited tokens | 580 (66%) |
| Not expressible: references between registers, carriage between phases, citations, grounding against the snapshot, tier-B procedures | 303 (34%) |

Even the 580 do not carry over unchanged:

- **Columns.** JSON Schema matches property names exactly, but columns are matched by prefix (C3).
- **Vocabularies.** `enum` is exact, but cells are upper-cased before comparison (C11).
- **Patterns.** `pattern` is an unanchored ECMA-262 search, but the rules use Python `re` and often an
  anchored `match` (C12).
- **Sentinels.** The emptiness sentinel and the none markers (C5, C6) would have to be restated in
  every constraint.
- **Findings.** A JSON Schema validator reports its own errors. The finding codes and detail that
  authors read today would change, which breaks behavioural identity (§8.5).

So JSON Schema could not be the format without a second mechanism for a third of the rules, and
without changing what authors see for the rest. This is the asymmetry of §6.4, measured. The
protocol borrows JSON Schema because its data is YAML. Transformation judges Markdown registers and
needs a language of its own.

**Where JSON Schema does belong.** It is the meta-schema. On the protocol side, JSON Schema validates
declarations (artifacts). On the transformation side, the same role is validating register-schema
declarations: a `SCHEMA_REGISTER_SCHEMA_V0` that closes their surface, per the `CONSTITUTION_STRUCTURE_V0`
rule that a description names its required fields and closes its surface.

**Proposed format.** A register schema per phase, declared as data:

- **Registers:** id, section, optionality, and the `business_language` scope.
- **Columns:** name, optionality, vocabulary reference, and constraints. Each constraint is a
  general check kind with its params.
- **References:** a cell resolves in another register; one register covers another.
- **Annotations:** carriage from a prior phase, grounding, closure and purity. Each cites the
  invariant it realises.

Its evaluation semantics are the language specification of §6.4: the document model, the
sub-grammars, and the general kinds. JSON Schema likewise has a meta-schema and a specification.

**Where it lives: two carriers.**

| | (A) Substrate file, sealed into the workflow | (B) Compiled artifact in the snapshot |
|---|---|---|
| Protocol counterpart | exactly how protocol schemas work: files with an `$id`, selected by a dispatch | none; it would be a new artifact kind |
| Reaches the runtime | through the expanded rules sealed in `WF_P*`, as today | by observation of the artifact, as `GOVERNING_RULE_IN_SEALED_SET` already observes sealed rule sets |
| Changes outside `transformation` | none | a new kind in `protocol_compiler`'s kind registry, its schema and constitution in `software_governance` |
| Rule identity (§9.2) | the schema's `$id` plus a JSON Pointer, carried into each expanded rule | the schema's FQDN plus a JSON Pointer |
| Versioning and pinning | new schema file version; the sealed `WF` version is the pin, as now | artifact version and supersession |
| Generated copy | kept: the sealed rules, with `phase emit --check` | removed |

**Proposed answer: (A).** It is the protocol's own arrangement, and it changes nothing outside
`transformation`. It also satisfies the sealing principle through the sealed workflow. (B) earns
its new kind only if a requirement arises that a sealed copy cannot meet. Nothing in this analysis
has found one: `rule_effectivity`'s pinning already works through sealed workflow versions.

**Consequences.**

- Register schemas live in `transformation/registry/schema/`, mirroring `software_governance/registry/schema/`.
  A dispatch from phase to schema replaces `catalog.PHASES[].template` as the choice of shape.
- The templates keep their human role (§6.5). Their register markers, columns and inline
  vocabularies are checked against the schema by the closure check (§3) instead of being read as
  the source. Generating the skeleton would turn an authored guide into a generated artifact.
- `derive.py` becomes the expansion of a schema into sealed rules. Its behaviour is specified as part
  of the language, because the sealed rules must be reproducible from the schema.
- §9.8 is answered as a consequence: under (A), sealing is how the schema reaches the runtime, so it
  is required, not optional.

**Decided.**

- **Format.** §9.9 makes JSON Schema the register-schema format.
- **Schema files are JSON.** That is what every protocol schema is, and nothing warrants an
  exception. Phase documents carry YAML Machine blocks, as artifacts do. Schemas are JSON, as the
  protocol's are.
- **Vocabularies are `VOCAB` artifacts,** declared once and visible. A register schema references a
  vocabulary by FQDN, and expansion resolves it from the compiled snapshot when the rules are sealed
  (`phase emit` already takes `--snapshot`). It is never copied. The protocol shows what copying
  costs: `SCHEMA_INVARIANT_V0` restates the enforcement stages as an `enum`, and has drifted from
  `VOCAB_ENFORCEMENT_STATUS_V0` by one value (`compiler_discovery`).

### 9.2 Rule identity

**Facts.**

- **`id` is a finding code, not a rule identity.** The 883 rules carry 180 distinct ids. 162 ids
  are used by exactly one rule, and the rest are shared: `REGISTER_MISSING` and
  `REGISTER_COLUMN_MISSING` 113 times each (one per register, in every phase), `SOURCE_FINDING_UNRESOLVED` 76
  times, `SEED_ROW_NOT_CARRIED` 17 times. Within a single phase, 66 ids are shared. This is
  deliberate. The id tells an author what kind of defect was found, and one kind of defect recurs
  across registers.
- **No natural key is unique.** `(phase, id, register, check)` identifies 877 of 883 rules (§8.2).
- **Citation already depends on identity.** `GOVERNING_RULE_IN_SEALED_SET` resolves a cited
  `(phase, id)` by membership in the sealed set. A shared id resolves if any rule carries it.
  Citing `REGISTER_MISSING` at p7 resolves against 25 rules, and the citation cannot say which one.
- **No delivered dossier cites a governing rule.** All ten `refusal_governance_discharge` registers in
  delivered dossiers hold `NONE IDENTIFIED`. The only citations are testbed fixtures, and they cite
  ids that are unique in their phase. Moving citations to a new identity costs nothing in delivered
  work.

**Two concepts are conflated in `id`.** One is the **finding code**, which says *what is wrong* and
is read by the author. The other is the **rule identity**, which says *which declared constraint*
and is used by citation, pinning, coverage, difference reports and invariant realisation. The
protocol keeps these apart:

- An invariant is identified by its FQDN, and its derived assert takes its name from the invariant
  (`INVARIANT_X` → `ASSERT_X`).
- JSON Schema reports a failure by the location of the failing keyword in the schema, separately
  from the keyword itself.

**Options.**

| Option | Assessment |
|---|---|
| Author a unique name per rule | Rejected. 633 rules are derived and nobody authors them. A hand-kept name is a second declaration that drifts from the first. |
| Extend the natural key with a discriminating param | Rejected. Which param discriminates (`column`, `columns`, `target_register`, …) varies by kind, so the key would be ad hoc per kind. |
| **The rule's location in its declaration** | **Proposed.** It is unique by construction, since one location holds one constraint, and it is derived rather than authored. |

**Proposed answer.** A rule's identity is where it is declared:

- **A schema constraint:** the register schema's identity, plus the path to the constraint (phase
  schema → register → column → constraint). For example, the vocabulary constraint on
  `interface_fields.Direction` at p7. This is the JSON Schema counterpart.
- **An annotation:** the register schema's identity, plus the path to the annotation. The annotation
  also names the invariant it realises.
- **A tier-B procedure:** the FQDN of its invariant, one to one. This is the protocol's
  `INVARIANT_X` → `ASSERT_X` counterpart.

The finding code stays what it is: the author-facing name of the defect, shared across rules.

**Consequences.**

- **A finding carries both.** It carries the finding code and the rule identity, together with the
  structured locator of §4.6.
- **Citations move to the rule identity.** `GOVERNING_RULE_IN_SEALED_SET` then resolves one rule, not
  a membership test over a shared code.
- **A changed constraint is a different rule.** Renaming a column changes the identity of every
  constraint on it. That is the intended reading.
- **`rule_effectivity` gains a rule-level difference.** That change versions rule sets as a whole. With
  identities, the difference between two versions names the rules added, removed and changed, which
  is what separating a migrated document from an authored one needs (§9.6).
- **No identity is needed for the move itself.** Declaration identity compares full rule content
  (§8.5). Identity is needed to report and to cite.

**Syntax.** Under the carrier proposed in §9.1 (A), a rule's identity is the register schema's `$id`
plus a JSON Pointer to the constraint or annotation, carried into each expanded rule when it is
sealed. A tier-B rule's identity is its invariant's FQDN.

### 9.3 Tier B, kind by kind

**Scope.** Tier B is 28 kinds carrying 29 rules: the 34 single-use kinds of §4.2, less the six that
§6.7 placed in the register schema, plus `OUTCOME_GROUNDED_IN_OPERATION`, which has two rules. All
but `DEPENDENCY_PRECEDES` (p8) are p7 rules.

**Method.** Each kind was read from its docstring and its rule's params. Each candidate protocol
invariant was then read twice:

- **its text:** `core.description`, or the prose rule where the description is empty;
- **its enforcement:** the handler in `governance_engine/assertions/handlers/`, and the analysis the
  compiler pre-computes for it in `stages/s4_govern.py`, plus any other stage found to refuse the
  same condition.

A keyword sweep over all 103 protocol invariants looked for counterparts the candidates missed.

**The by-name mapping of §4.2 does not survive.** Three examples from the text alone:

- `ENTRANCE_SUPPLIES_GATE` → `IN_WORKFLOW_BINDING` / `WF_ENTRY_INTENT`: those concern the existence and
  uniqueness of the entry intent.
- `CROSS_SUBDOMAIN_REACH_READ_ONLY` → `RB_STORAGE_SUBDOMAIN_OWNED`: that one concerns who maintains a
  storage description.
- `TOPOLOGY_ROUTE_RESOLVES` → `WF_ROUTING_CLOSED`: that one concerns completeness of routing.

The handlers then removed three more counterparts that the text had seemed to confirm (below).

**Four classes.**

| Class | Meaning | Disposition |
|---|---|---|
| **R**: re-expressible | Logic inside the document that a general kind could state with declared params | becomes a register-schema constraint |
| **S**: shift-left, enforced | Checks at design time a property the protocol pipeline actually refuses | stays a procedure, specified as the early check of that enforcement |
| **G**: composition property, not enforced | A property of the sealed artifacts that nothing in the protocol pipeline refuses | a protocol gap: the design compiler is its only enforcement |
| **T**: transformation-owned | A property of design notation or design concepts that no artifact carries | stays a procedure, specified by its own transformation invariant |

**Kind by kind.**

| Kind | Checks | Class | Protocol counterpart, as enforced |
|---|---|---|---|
| `DEPENDENCY_PRECEDES` | every dependency is scheduled before its dependant | R | none; mandate concept |
| `TOPOLOGY_KEY_UNIQUE` | a (workflow, node) key occurs once | R | none. `WF_NODE_KEY_BINDING_UNIQUE` is a different property (one contract used twice must differ in inputs). A workflow's nodes are a YAML mapping, so a duplicate key is not refused: it is silently collapsed. |
| `BINDING_SOURCE_WELL_FORMED` | a source has the form the runtime resolves | R | not enforced at workflow level (see `BINDING_SURFACE_CLOSED` below). At step level, `TOPOLOGY_INPUT_REFERENCE_DECLARED` checks `$.results.<step>` references only. |
| `BINDING_SOURCE_ROOTED` | a source is rooted in a scope execution offers | R | as above |
| `STORE_PATH_MATCHES_STORAGE` | a store path carries its storage capability's extension | R | none. `RB_BINDING_POLICY_CONFORMANCE` requires a non-empty `policy.path` for file-path storage, not its format. |
| `CONTRACT_OUTPUT_PRODUCED` | every declared contract output is produced by a step | R | partial, at another level. `CT_OUTPUT_CONTRACT_MATCH` matches a transform's outputs to its contract's keys. |
| `IMPLEMENTATION_MODULE_CONFORMS` | a transform's module sits where its domain resolves implementations | R | none. `IMPLEMENTATION_ADMISSIBLE` requires a non-empty module and callable, not their location. |
| `STEP_OPERATION_PUBLISHED` | a step's operation is one its capability offers | S | `CC_STORAGE_OP_CONFORMANCE`, enforced for storage steps (it passes when the capability declares no operations) |
| `TOPOLOGY_ROUTE_RESOLVES` | every routing target is a node of the workflow, or an ending | S | enforced by S8 `_verify_dispatch_routing` ("routes to … which the workflow does not declare", E403). This is an unnamed verification, not an invariant. `WF_EXECUTION_PATH_VALID`, whose text promises it, does not check it. |
| `BINDING_SOURCE_REACHABLE` | a source naming another node names one the workflow runs | G | `BINDING_SURFACE_CLOSED` states it, but its analysis checks something else (below) |
| `BINDING_SOURCE_PUBLISHED` | an output binding reads a field the operation publishes | G | `CC_INPUTS_SATISFIED` states the workflow-level half, but is never evaluated (below) |
| `STEP_INTERFACE_CONFORMS` | a transform step hands only inputs the transform declares | G | none. `CT_INPUT_TYPED` skips any bound input the transform does not declare, and checks types only. |
| `NODE_INPUT_BOUND` | a workflow node supplies every input its contract requires | G | none |
| `ENTRANCE_SUPPLIES_GATE` | a transport entrance supplies everything its gate requires | G | none |
| `STEP_INPUTS_BOUND` | every input a step consumes is bound | G | none |
| `STEP_CONSUMES_PUBLISHED` | a step hands an operation only fields it accepts | G | none |
| `CONSUMPTION_GROUNDED_IN_OPERATION` | a step consuming nothing invokes an operation that takes nothing | G | none |
| `STORE_GROUNDED_IN_CAPABILITY` | a step names a store exactly when its capability keeps one | G | none |
| `CROSS_SUBDOMAIN_REACH_READ_ONLY` | an act reaching into another subdomain only reads | G | none; this is p6's key rule, "cross-subdomain writes forbidden" |
| `OUTCOME_GROUNDED_IN_OPERATION` (2 rules) | a step branches only on outcomes its operation answers, or names the interpretation | G | none; sibling of `NONDETERMINISM_NOT_ROUTED` |
| `INTERPRETATION_TRANSFORM_REFUSES` | an interpreting transform can refuse | G | none |
| `DISCHARGE_GROUNDED_IN_TOPOLOGY` | a refusal discharge names a real step and outcome | T | design concept: refusal discharge |
| `DISCHARGE_OUTCOME_REFUSES` | the discharged outcome routes to a refusing ending | T | design concept: refusal discharge |
| `EMISSION_GROUNDED_IN_ENDING` | a moment is announced from a completing ending | T | reads design refusal declarations; `WF_ANNOUNCEMENT_DISTINCT` is about distinctness only |
| `GOVERNING_RULE_IN_SEALED_SET` | a cited rule is in force in the pinned composition | T | design concept: rule citation; changes with §9.2 |
| `REACH_IS_USED` | every declared reach is used | T | design concept: declared reach |
| `READ_IS_DECLARED` | an act reads nothing it did not declare a reach to | T | design concept: declared reach |
| `STEP_BINDINGS_MATCH_INTERFACE` | a binding names only fields the step's Interface cell declares | T | design notation: the Interface sub-grammar |

**Tally.** R 7, S 2, G 12 (13 rules), T 7.

**What reading the handlers changed.** Three counterparts that the text confirmed are not enforced:

- **`BINDING_SURFACE_CLOSED`.** Its text and handler docstring state source closure (`$.payload.<field>`
  in the intent's payload schema, `$.results.<NODE>.<field>` in that contract's outputs, no other
  grammar). The analysis behind it, `_analyze_wf_binding_surface`, checks something else: that every
  transform and side effect a workflow's contracts bind has a runtime-binding mapping.
- **`CC_INPUTS_SATISFIED`.** Its analysis is set to `PASSED` for every workflow (`s4_govern.py`,
  alongside `cc_dependencies` and `cc_unused_outputs`), so its handler can never refuse.
- **`CT_INPUT_TYPED`.** It checks the type of each bound input the transform declares. It skips inputs
  the transform does not declare, and it does not ask whether declared inputs are bound.

Nothing else in the pipeline validates workflow-level `$.payload` or `$.results` sources at build:
neither S2 nor S5 nor S8. A wrong source surfaces at execution. That is consistent with the
transformation doctrine's own record of a `$.capability_result.header` binding that passed every
phase check and failed on its first dispatch.

**Findings.**

1. **The protocol gap is twelve kinds wide.** Twelve properties of the sealed composition are refused
   only when a design passes through p7:
   - binding-source closure;
   - required inputs supplied, at the node, step and entrance;
   - interface conformance;
   - operation input conformance;
   - store grounding;
   - read-only cross-subdomain reach;
   - data-to-decision closure.

   An artifact authored or generated outside the pipeline is never checked for any of them.
2. **Data-to-decision closure has a protocol sibling.** `NONDETERMINISM_NOT_ROUTED` forbids routing on
   what a non-deterministic atom said, with a deterministic step between. Data-to-decision closure
   forbids routing on what a raw observation said, with an interpretation between.
3. **None of the R kinds has an enforced protocol counterpart.** They become register-schema
   constraints that cite nothing on the protocol side. On Markdown they would have needed four
   extensions to the general language. Under YAML and JSON Schema (§9.9), each has a strategic home
   instead:
   - **A pattern chosen by another cell's value:** JSON Schema `if`/`then`. Native; no extension.
   - **A pattern templated by a header value** (a module path built from the domain): the value is
     determined, so a design should not state it. Construction derives it, and the rule disappears
     with the column.
   - **Uniqueness over a composite key:** a register declares its **key**.
   - **A reference scoped to rows sharing a key:** a **reference** that names the key it is scoped by.

   The last two are the general case of what the annotation layer already does: keys and references
   between registers, as in a relational schema, with carriage and grounding beside them. The
   annotation layer is therefore four constructs: key, reference, carriage, grounding. It is not a
   set of special kinds.
4. **Procedures that remain: 21** (S 2, G 12, T 7). For S, the specification is the enforcement it
   anticipates. For G, it is the protocol invariant once one exists, and until then a transformation
   statement of the property. For T, it is a transformation invariant.

**What remains open.** For G: whether each property becomes an enforced protocol invariant (§9.4).

### 9.4 The protocol gap

§9.3 found twelve composition properties that only the design compiler enforces. Open: whether each
becomes an enforced `software_governance` invariant. Once it does, the design rule becomes its
shift-left check (class S). Each is a change outside `transformation`.

Reading the handlers also found three defects on the protocol side. They are recorded here because
they bear on the gap. They are not changed by this analysis.

| Defect | Where | Effect |
|---|---|---|
| `CC_INPUTS_SATISFIED`, `CC_NO_MISSING_DEPENDENCIES` and `CC_NO_UNUSED_OUTPUTS` are in force with `enforcement_stage: compiler_validation`, but their analyses are set to `PASSED` unconditionally | `protocol_compiler/compiler/stages/s4_govern.py`, the per-artifact analysis loop | three invariants that can never refuse; the vacuous assertion `s4_govern.py` itself warns against, and the case `declared_not_enforced` exists to state honestly |
| `BINDING_SURFACE_CLOSED`'s analysis checks runtime-binding coverage, not the source closure its text states | `_analyze_wf_binding_surface` | binding sources are unchecked at build, while the invariant reads as enforcing them |
| `WF_EXECUTION_PATH_VALID`'s analysis checks only that a workflow has a start edge or contained nodes | `_analyze_wf_execution_graph` | of what its text promises, `next` targets are refused at S8 and unresolved contracts at S5. Reachability, acyclicity and terminal endings were not traced to any enforcement. |
| `BINDING_SURFACE_CLOSED`'s handler acts only on an analysis status of `VIOLATION`, which nothing produces; every structural analysis reports `FAILED` | `assert_binding_surface_closed_v0.py` | the assertion passes every workflow, whatever its analysis finds |
| The runtime-binding coverage that analysis does compute demands a mapping for every transform as well as every side effect | `_analyze_wf_binding_surface` | it contradicts `CONSTITUTION_RUNTIME_BINDING_V0` ("bind CS artifacts exclusively"). Because it never fires, the contradiction has gone unseen. |
| The assertion runner does not read an invariant's `violation_response` | `_execute_assertions` | any violation fails the build; a `WARN` invariant is honoured only if its handler returns `warnings` instead |

**What enforcing the stated texts would cost, measured over the 50 workflows (37 in force).**

| Check, as its text states it | Findings |
|---|---|
| `WF_EXECUTION_PATH_VALID`: start, reachability, terminal endings | 0 |
| `CC_NO_MISSING_DEPENDENCIES`: a result read only from a node on every path to its reader | 0 |
| `BINDING_SURFACE_CLOSED`: grammar, results node, results field | 0 |
| `BINDING_SURFACE_CLOSED`: payload field declared by the start intent | 11: ten blockchain bindings, one `WF_P5_…_V1` |
| `CC_NO_UNUSED_OUTPUTS` (`WARN`) | 219, mostly `result_status` |

The 11 payload bindings are not new. `admission_contract_fidelity` already reports them, red by
design, as the blockchain gap GAP-09. Closing them means new versions of the five start intents:

- **Identity.** Adding an input changes an intent's meaning, so `published_identity` refuses an
  edit in place.
- **Construction.** The edited intents no longer reproduce from their dossiers, so
  `construction_acceptance` refuses them.

The protocol fixes are therefore not independent of the domains. The payload half of
`BINDING_SURFACE_CLOSED` can be enforced only once GAP-09 is closed through the owning changes.

### 9.5 The invariant set

**Sources.** The candidates come from four places. Each source is placed where its job is, whether
or not that place is an invariant:

- **the annotation rules (§6.7):** 324 rules carrying 45 distinct intents (carriage 26, grounding 11,
  closure 3, purity 5);
- **the T procedures (§9.3)**;
- **the phase key rules** in `catalog.PHASES[].key_rule`;
- **the doctrine** in docstrings (§4.7).

**Doctrine that is not an invariant.** Three doctrine claims describe how the evaluator works, not
what a document must be:

- every rule is evaluated, with no short-circuit and no warning tier;
- emptiness is declared, never inferred, and an absent register is a finding;
- an unsupplied prior is a different finding from a missing register.

They belong to the language standard (§6.4), as evaluation semantics. An invariant states what
must be true of a document or a composition.

**Phase key rules are not invariants either.** Each one is a phase's profile of lifecycle-wide
claims. "Faithful rewrite only" (p0) is nothing dropped plus nothing invented. "Business language
only" (p1) and "no bindings, no paths" (p5) are rung purity. "Mechanical derivation; must reconcile
with p7 exactly" (p8) is nothing dropped plus nothing invented again. Declaring them as invariants
too would state each claim twice. They stay in the catalog as each phase's summary and name the
invariants they profile. One exception is "the full dossier is reviewed as a body" (p7): that is a
human gate, which no invariant can check.

**Proposed design-admissibility invariants (concern `design`).**

| Invariant | Claim | Realised by |
|---|---|---|
| `PROVENANCE_CITED` | every restated row cites its source, and every citation resolves | 171 rules: `SOURCE_FINDING_RESOLVES`, `CITED_ORDINAL_RESOLVES`, `CITATION_ROW_UNRESOLVED` |
| `NOTHING_DROPPED` | a commitment made upstream is carried, never silently lost | `SEED_ROW_NOT_CARRIED` and 11 other carriage rules (beliefs, consolidation, placement, refusals, scheduling, binding, purpose) |
| `NOTHING_INVENTED` | content enters at the phase that owns it, never later | `ROW_NOT_IN_SEED`, the three undeclared-refusal rules, `SCHEDULED_ARTIFACT_NOT_DESIGNED`, `AUTHORED_ARTIFACT_WITHOUT_INTENT` |
| `RESTATEMENT_FAITHFUL` | a row citing an upstream row addresses that row, not a substitute | `BELIEF_RESTATED_FROM_P1`, `BELIEF_RESULT_RESTATED_FROM_P2` |
| `EXISTING_IS_OBSERVED` | a claim about an existing artifact resolves in the pinned composition | 8 `CITED_ARTIFACTS_RESOLVE` rules |
| `NEW_IS_NEW` | an identity assigned as new names nothing that exists | `NEW_CODE_ALREADY_EXISTS`, `BUILD_CODE_ALREADY_EXISTS` |
| `REUSE_BOUNDED` | reuse is offered only from a domain that permits it | `REUSE_CANDIDATE_NOT_ELIGIBLE` |
| `QUESTIONS_CLOSED` | no governed hole and no blocking or business question is left open | 13 closure rules |
| `RUNG_PURITY` | a phase speaks only the vocabulary its rung admits | 74 purity rules |
| `SPAN_DECLARED` | every subdomain a change touches has its purpose stated, its owner declared, and what it authors named | the three `TOUCHED_SUBDOMAIN_*` rules |
| `REFUSAL_DISCHARGED` | every refusal the business declared is refused by a real step and outcome, deferred to a named owner, or carried by an in-force rule | `DISCHARGE_GROUNDED_IN_TOPOLOGY`, `DISCHARGE_OUTCOME_REFUSES`, `GOVERNING_RULE_IN_SEALED_SET`, `REFUSAL_UNACCOUNTED`, the deferral rules |
| `ANNOUNCEMENT_FROM_COMPLETION` | a moment is announced from an ending that completes the act | `EMISSION_GROUNDED_IN_ENDING` |
| `REACH_DECLARED_AND_USED` | an act reads only what it declared a reach to, and uses every reach it declared | `READ_IS_DECLARED`, `REACH_IS_USED` |
| `BUILD_ORDER_IS_A_SORT` | the mandate builds every dependency before its dependant, without gaps | `DEPENDENCY_PRECEDES`, the contiguity rules |

`STEP_BINDINGS_MATCH_INTERFACE` (T) is left out deliberately. It checks the Interface sub-grammar
against the bindings, which is notation consistency. It becomes a schema reference once that
notation is structured (§9.9).

**Proposed construction-determinacy invariants (concern `build`).**

| Invariant | Claim | Realised by |
|---|---|---|
| `UNIQUELY_DETERMINED` | a design states every fact construction renders, or construction stops | `completeness.py` (`UNIQUELY_DETERMINED_OR_STOP`, 100% required) |
| `RENDER_INVENTS_NOTHING` | every rendered value is read from a register or a constitution-fixed default | `render.py`'s provenance classes |
| `ONE_PRODUCER` | an artifact reached by a generator is never also rendered | `generators.py`, `GENERATION_RULES` |
| `MEANING_CHANGE_IS_NEW_IDENTITY` | an amendment that changes meaning takes a new identity | `sameness.py`, over `VOCAB_DECLARATION_REPRESENTATION_V0` |

**The twelve G properties are not transformation invariants.** They are truths about the
composition, so the protocol owns them. The protocol already has the form for a truth stated and
enforced by nothing yet: `enforcement_stage: declared_not_enforced`. The pure arrangement is:

- each G property becomes a `software_governance` invariant, initially `declared_not_enforced`;
- the design rule cites it as its early check (class S);
- the protocol enforces it later, by a designed and versioned change (§9.4).

That is a change outside `transformation`.

**Constitutions.** There are two concerns, design admissibility and construction determinacy.
They map onto the repo's two subdomains, `design` and `build`, which are already the `concern` of its
workflows. The protocol's practice is one constitution per concern, so the proposal is two.

**Size.** 14 design invariants and 4 construction invariants. That is well inside the "few dozen"
estimate of §4.7, and each one is realised by at least one rule or procedure.

**Proposed names.** They follow the protocol's subject-then-predicate style (`CC_NO_UNUSED_OUTPUTS`,
`NONDETERMINISM_NOT_ROUTED`), in the `transformation` namespace, as `INVARIANT_<NAME>_V0`.

| Working name | Proposed name |
|---|---|
| `PROVENANCE_CITED` | `ROW_PROVENANCE_CITED` |
| `NOTHING_DROPPED` | `UPSTREAM_COMMITMENT_CARRIED` |
| `NOTHING_INVENTED` | `CONTENT_ENTERS_AT_OWNING_PHASE` |
| `RESTATEMENT_FAITHFUL` | `RESTATEMENT_MATCHES_SOURCE` |
| `EXISTING_IS_OBSERVED` | `EXISTING_ARTIFACT_OBSERVED` |
| `NEW_IS_NEW` | `NEW_IDENTITY_UNUSED` |
| `REUSE_BOUNDED` | `REUSE_FROM_PERMITTING_DOMAIN` |
| `QUESTIONS_CLOSED` | `NO_QUESTION_LEFT_OPEN` |
| `RUNG_PURITY` | `PHASE_SPEAKS_ITS_RUNG` |
| `SPAN_DECLARED` | `TOUCHED_SUBDOMAIN_DECLARED` |
| `REFUSAL_DISCHARGED` | `BUSINESS_REFUSAL_DISCHARGED` |
| `ANNOUNCEMENT_FROM_COMPLETION` | `ANNOUNCEMENT_FROM_COMPLETING_ENDING` |
| `REACH_DECLARED_AND_USED` | `REACH_DECLARED_AND_USED` |
| `BUILD_ORDER_IS_A_SORT` | `BUILD_ORDER_TOPOLOGICAL` |
| `UNIQUELY_DETERMINED` | `DESIGN_UNIQUELY_DETERMINES_ARTIFACT` |
| `RENDER_INVENTS_NOTHING` | `RENDER_INVENTS_NOTHING` |
| `ONE_PRODUCER` | `ONE_PRODUCER_PER_ARTIFACT` |
| `MEANING_CHANGE_IS_NEW_IDENTITY` | `MEANING_CHANGE_IS_NEW_IDENTITY` |

**Carried and owned stay two invariants.** They fail differently, and they are realised by different
rules: one is a dropped row upstream, the other an invented row downstream. The p0 and p8 key rules
profile both. Refusals and scheduling use them apart. One invariant would make a finding say less
about which way a document went wrong.

### 9.6 Relation to `rule_effectivity`

**What it asks.** The dossier `transformation/dossiers/rule_effectivity` (p0–p6 admissible, halted at
p7) asks for four things:

1. a rule set has a version, and a document says which one it was authored under;
2. a verdict states the rule set it was rendered against;
3. a dossier migrated to a later rule set is distinguishable from one authored under it;
4. what happens to an approval when the rules it was given under change is stated.

**Where it stands.**

- **Its blocker is gone.** It halted because p7 could not name a generator. `generated_artifacts`
  closed that gap and has since been delivered.
- **Its asks have partly shipped.** `tc phase check` now judges by the rule set sealed in the
  pinned composition by default, and reports `judged_by`. That is ask 2 in part: it names a snapshot
  path, not a rule-set identity. The sealed `WF_P*` versions (V0, V1) are rule-set versions in effect,
  but no document states which one it was authored under (ask 1). Nothing records a migration
  (ask 3), and nothing states an approval policy (ask 4).
- **Its problem is now measured.** Under today's rules, 32 delivered documents are refused for
  structure added after they were approved (§8.4).
- **Its design has gone stale.** Its p6 `pps_artifacts_requiring_action` declares `EXTEND` on
  `WF_P0`…`WF_P8_…_V0`. Seven of those nine have since been superseded by V1, and its pinned baseline
  is not today's composition. It needs re-authoring before p7 whatever is decided here.

**What the repo's doctrine says.** A new subject that touches an artifact an in-flight dossier
declares is a child of that dossier. A child is not raised as a new change: the in-flight dossier is
re-authored from p0 (`transformation/CLAUDE.md`, "When a change is a new CR"). The changes of
§9.9 touch the nine phase workflows, which `rule_effectivity` declares. So leaving it halted while
those changes proceed is not an option the doctrine allows.

**How its asks fall onto the changes.**

| Ask | Where it lands naturally |
|---|---|
| 1. a document names its rule set | **format**: a Machine-block field naming the sealed rule-set identity (the `WF_P*` version, or the register schema's `$id`) |
| 2. a verdict names its rule set | **format**: `judged_by` becomes that identity instead of a snapshot path |
| 3. migrated versus authored | **format**: converting an in-flight document to YAML is itself a migration, and its Machine block records it |
| 4. approval under changed rules | a policy statement, independent of format, but small, and needed as soon as a document carries its rule set |

The format change *needs* asks 1 and 3. It cannot convert documents without saying which were
converted, and it introduces the Machine block where both naturally live. Rule identity (§9.2) then
gives a rule-level difference between two rule-set versions.

**Options.**

| Option | Assessment |
|---|---|
| **Re-author `rule_effectivity` from p0 as the format change** | **Recommended.** It meets the child doctrine. The re-authoring is owed anyway, because its design is stale. Its measured problem becomes the format change's motivation, and the Machine block gives every ask a home. It is not conflation: both concern how a phase document states what judged it, and the unravel stays a separate, later change. |
| Deliver it first, on Markdown | Possible: re-author against today's V1 workflows, and add a rule-set field to the Markdown header. The format change then moves that field into the Machine block and records the migrations, so the same ground is designed twice. |
| Fold it into the unravel | Rejected. It conflates exactly what §9.9 separates. |

**Proposed answer.** Re-author `rule_effectivity` from p0 as change 1 of §9.9 (format). Its four
asks are the format change's acceptance obligations, alongside behavioural identity. Its p0
problem statement carries forward as evidence. Its halted p1–p6, its halt note and its stale pin are
removed from the tree; git history keeps them.

**Decided.**

- **Ask 4: approvals re-confirm.** An approval names the rule set it was given under. When that set
  is superseded, the approval stands unconfirmed until a human re-confirms it against the new set.
  It neither lapses silently nor survives silently. This also covers a dossier that is in flight
  when its rules change.
- **A document names its register schema's `$id`.** A `WF_P*` version changes whenever its workflow
  changes for any reason (topology, bindings, the contracts it runs) even when no rule has. A schema
  `$id` changes only when the register shape or its constraints do. Under a re-confirmation policy,
  naming the workflow version would demand re-confirmations no rule change caused.

### 9.7 Construction scope

**What construction holds** (§4.9):

- **`render.py`** maps p7 and p8 registers onto Machine-block fields, family by family, using
  code-held tables and four provenance classes.
- **`completeness.py`** derives its requirements from `render`.
- **`sameness.py`** applies part of a declared policy (`VOCAB_DECLARATION_REPRESENTATION_V0`).
- **`generators.py`** is a closed registry in code.

**What the protocol mirror says.** The protocol compiler's projections (S5 and S6) are code. No
artifact declares how a graph becomes a canonical or tokenized projection. Its behaviour is fixed
by invariants (what must hold) and by the standards (how projection works). Construction is the
same kind of thing: a deterministic projection, from design registers to artifacts. The pure
mirror is therefore:

- invariants and a constitution for what construction must guarantee: the four of §9.5;
- a standard describing the mapping, if independent construction is ever a goal.

Moving the mapping into declared data has no protocol counterpart. It would be the force-fit §6
exists to avoid.

**What the other changes do to it anyway.**

- **The format and structure changes simplify `render.py` for free.** Routing, interface and
  binding cells arrive as mappings, so its 21 cell-convention sites go.
- **`sameness.py`'s `APPLIED` subset** is a code-held choice over a declared policy. It is small, and
  it belongs with the `MEANING_CHANGE_IS_NEW_IDENTITY` invariant.

**Decided: independent construction is a goal**, by separation of concerns. The two compilers fail
differently and are fixed by different people (`transformation/CLAUDE.md`), so each is governed and
specified on its own.

- **Its own change (change 4),** after the design unravel. It is not part of it.
- **Its content:**
  - the `build` constitution;
  - the four construction invariants;
  - a **construction-mapping standard**, stating how each register field becomes an artifact field
    and under which provenance class;
  - `sameness.py`'s `APPLIED` subset moved into the declaration it serves.
- **No declared mapping.** The mapping stays code, governed by invariants and specified by the
  standard, as protocol projection is.
- **In the format and structure changes:** `render.py` reads the new shape. That is required anyway.

### 9.8 Sealing derived rules

The protocol does not materialise schema checks as rules (§6.3). Under the carrier proposed in §9.1
(A), sealing is how a register schema reaches the runtime, so the expanded rules stay sealed in the
`WF_P*` workflows. This question stays open only if §9.1 settles on (B).

### 9.9 Register format: Markdown tables or a YAML Machine block

**The question.** Should a phase document carry its registers as a YAML Machine block, the way an
artifact carries its declaration, with the prose beside it as the human block?

**What the Markdown table format costs today.** Most of the home-grown language in §4.3 and §4.4
exists only because registers are Markdown tables:

- **Reading tables:** prefix-matched columns (C3), escaped pipes and ragged rows (C4), and the
  three-line window between marker and table (C2).
- **Emptiness and silence:** the `NONE IDENTIFIED` sentinel row (C5) and the none markers (C6).
- **Cell sub-grammars:** routing `OUTCOME -> target; …`, interface `in: a=b; out: …`, comma-separated
  name lists, and YAML inside a cell (§4.4).
- **Its effect on schemas:** it is why JSON Schema could not be the register-schema format without
  mismatches (§9.1).

**What a YAML Machine block changes.**

| Today | As YAML |
|---|---|
| a register marker plus a table | a key holding a list of mappings |
| a column matched by prefix | an exact key |
| a `NONE IDENTIFIED` row | an empty list, which is distinct from an absent key |
| a none marker in a cell | `null` or an absent key |
| a routing cell | a mapping, outcome → target |
| an Interface cell | two mappings, `in` and `out` |
| a comma list | a list |
| YAML inside a cell | YAML |

Once registers are data, JSON Schema expresses the 580 shape rules of §9.1 **without** the five
mismatches listed there. That makes the protocol's own arrangement (JSON Schema files plus a
dispatch) the register-schema format. The asymmetry of §6.4 shrinks to what JSON Schema cannot
state anywhere:

- references between registers;
- carriage between phases;
- grounding against the snapshot.

Those are exactly the invariant-citing annotations of §6.7. The language Transformation must own
becomes that annotation layer, instead of a document model plus sub-grammars plus 27 kinds.

**What stays as it is.**

- Prose stays prose. The p0 business problem statement is human writing, and every phase document
  keeps its narrative beside the Machine block.
- Human-block fidelity applies as it does to artifacts: the prose declares nothing the Machine block
  holds.
- A dossier stays evidence, not an artifact. A Machine block is read by the evaluator, and nothing
  puts the document in the snapshot.

**What it costs.**

- **Authors write YAML instead of tables** for registers. For business registers this is a real cost
  to readability. For p7's 47-row topology and 280 bindings, tables are already unreadable, and CLM's
  were generated.
- **Delivered dossiers are never edited.** Their 273 documents stay Markdown. Either the Markdown
  reader is kept for documents judged under a pinned, older rule set, or each document is converted
  as a recorded migration. That is exactly the distinction `rule_effectivity` asks for, migrated
  versus authored (§9.6).
- **The acceptance test changes form.** Detail text will differ. The conversion itself is mechanical,
  though: `read.parse_text` already returns registers as data, and serialising that is the YAML. So
  equivalence can be shown per document and per rule identity, by judging the Markdown original and
  its mechanical conversion side by side.

**Assessment.** It is consistent with the protocol: a declaration in a Machine block, prose in the
human block, and JSON Schema for shape. It is also KISS: it removes the most fragile half of the
home-grown language, rather than specifying it so that an independent implementer can reproduce
it. Specifying the Markdown conventions (§0) is what independent implementation needs if the
format stays. With YAML, most of that specification is no longer needed, because JSON Schema
already is one.

**Proposed answer.** Yes, for registers. Prose stays Markdown. It changes earlier answers:

- **§9.1:** JSON Schema becomes the register-schema format. The proposed own-format carrier (A) still
  holds, with JSON Schema files in its place.
- **§5, item 1, and §0:** the specification effort shrinks from the 27 general kinds and the
  document model to the annotation layer.
- **§9.3:** the R kinds and `STEP_BINDINGS_MATCH_INTERFACE` become schema constraints or references
  more simply.

**Full, partial or none.**

| Option | Assessment |
|---|---|
| **None** | Viable. Independent implementation then needs the Markdown conventions specified (C1–C14, the sub-grammars, the 27 kinds), and the most fragile part of the language stays in place. |
| **Partial** (p5–p8 only) | Rejected. Two live formats means two readers, two schema languages, and carriage rules that cross formats: p5 cites p4 rows, and p7 cites p0. It keeps all the Markdown complexity and adds YAML. |
| **Full** (every register-bearing document, seed to mandate) | **Recommended.** One live format. The p0 business problem statement is prose, has no registers, and is unaffected. Business registers are short lists of statements, so as YAML they stay readable, with the narrative beside them. |

**Is the rework justified?** Yes, because the format is behind one boundary. Every consumer reads
registers as parsed data, through `read.parse_text` and the CLI's `_dossier_registers`. That
includes `checks.py`, `derive.py`, `render.py` and `completeness.py`.

- **A YAML reader that returns the same shape changes nothing downstream.** `checks.py`, with its
  74 references to the table conventions, keeps working unchanged on the same values.
- **The writers change:** templates, the p1 projection (`project.py`) and anything that emits a
  dossier document.
- **The corpus is converted mechanically,** with the existing reader as the converter.

**What is converted, and what is not.** v6 is not backward compatible with v5.

| Material | In v6 | Why |
|---|---|---|
| **Delivered v5 dossiers** | Neither converted nor read | They are evidence of what v5 approved, and stay at tag `v5`. `construction_acceptance` restarts on v6-format dossiers. |
| **In-flight dossiers** | Re-authored in the new format | No migration machinery. The re-confirmation policy (§9.6) covers what was approved. `rule_effectivity` is re-authored in any case. |
| **The test corpus** (71 testbed documents, 83 e2e payloads, the fixture dossiers) | Converted once, mechanically | It tests the live evaluator, so it must be in the live format to keep testing refusals. |

**No Markdown reader survives.** The old reader is the converter. It is used during the format change
to show that every corpus document gives identical findings as Markdown and as its conversion.
Once that is shown, it is deleted with the table conventions.

**Phase it; do not conflate.** These are four changes, each with an acceptance test of its own.
The order is forced: the third's schema format depends on the first two, and the fourth reads the
shape the second settles. Done the other way round,
a Markdown-specific schema language would be specified and then discarded.

1. **Format.** Registers move to a YAML Machine block, behaviour unchanged. The YAML reader yields
   `parse_text`'s shape, so the sub-grammars and the sentinel survive as string values for now.
   Acceptance: every corpus document gives identical findings as Markdown and as its mechanical
   conversion.
2. **Structure.** Sub-grammars become mappings and lists, the sentinel becomes an empty list, and
   none markers become `null`. The convention code in `checks.py` and `read.py` is deleted, so this
   change is net negative in code. Acceptance: identical verdicts on the converted corpus.
3. **Design unravel.** JSON Schema register schemas, `VOCAB` references, key, reference, carriage
   and grounding annotations, rule identity, the `design` constitution and invariants, and authority
   moved out of `rules.py` (§6.7, §9.1, §9.2, §9.3, §9.5).
4. **Construction.** The `build` constitution and invariants, and the construction-mapping standard
   (§9.7).

The protocol work (§9.4: the defects and the twelve G invariants) is a separate track in
`software_governance` and `protocol_compiler`. It is not a step of these three.

---

## 10. Delivery

Delivery follows the analysis. It is not started until §9 is settled.

**The vehicle.** The generated-artifacts exception has been spent, so each change travels as a
transformation dossier, P0 through P8, like any other lifecycle change. Its own documents are
judged under the rule set in force when it starts.

**Four changes, in order (§9.9):** format (re-authored from `rule_effectivity`, §9.6), then
structure, then the design unravel, then construction. Each is a dossier of its
own, with its own acceptance test. The protocol work of §9.4 is a separate track.

**Groundwork that precedes the dossier.** None of it changes behaviour:

- the recorded baseline: each corpus document's verdict and findings, with its observations and
  priors captured for replay (§7.3, §8.4);
- a rule identity on expanded rules (§9.2), so that a difference or a coverage gap names the rule it
  concerns;
- a structured locator on findings (§4.6), needed before any independent evaluator is compared.

**Acceptance.** Two levels (§8.5):

1. **Declaration identity.** The expanded rule set after the change equals the one before it, rule
   for rule.
2. **Behavioural identity.** The recorded baseline replays identically.

`phase meta`, the differential and `e2e_phases_test.py` stay green throughout.

**Behaviour-changing work comes after.** Re-expressing tier-B kinds and writing an independent
evaluator from the specification both change or test behaviour. Each needs a negative for every
rule it touches (§8.5), starting with the 18 rules exercised nowhere today.
