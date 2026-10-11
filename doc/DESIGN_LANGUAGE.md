# The Design Language

This document specifies the language the design compiler judges: the form of a phase document, the
register schema that declares its shape, the rules a schema declares, and how they are evaluated.
An evaluator that implements what is written here judges a phase document as the design compiler
does, without reading the compiler's code.

What the rules realise is declared in the platform's governance surface: the lifecycle invariants
under `lifecycle::CONSTITUTION_CHANGE_MGMT_V1`. A named procedure that realises a property of the
composition rather than of design is specified here, by a statement (§6.2).

---

## 1. The phase document

A phase document is Markdown with one `## Machine` section. The section holds one fenced YAML block,
opened by a line `` ```yaml `` and closed by a line `` ``` `` that starts at column 0. An indented
fence inside a value closes nothing. Everything outside the block is prose, and no rule reads prose.

The block holds two keys:

- `header`: the document's header fields, each a string.
- `registers`: one key per register the phase declares.

A register's value is one of four things:

| Value | Means |
|---|---|
| a list of rows | the register states these rows |
| `[]` | the register is declared empty |
| `null` | the register is present and states nothing |
| a string | a text-only register |

A register absent from the block is missing. Missing, declared empty and stating nothing are three
different statements, and rules tell them apart.

A row is a mapping from column key to value. A column key is the column's title in `snake_case`;
`#` is keyed `number`. A value is text, or `null` when the row says there is nothing to state,
unless the schema types the column:

| Column type | Value |
|---|---|
| list | a list of names |
| routing | a mapping from outcome to target |
| interface | `{in: {…}, out: {…}}`, each a mapping from the capability's name to the design's |
| binding | a path string, `{literal: v}`, or `{generated: true}` |
| citation | a citation (§1.1), a list of several, or `null` for none |
| test value | any YAML value; a row that leaves the column out states no value |

### 1.1 Citations

A citation names where a row came from:

| Form | Cites |
|---|---|
| `{phase: p2, register: gaps, row: 1}` | a row by its ordinal |
| `{phase: p4, register: gap_register, key: GAP-05}` | a row by what it says |
| `{phase: p3, register: placement_decision}` | a whole register |
| `{artifact: <identity>}` | an artifact in the pinned composition |
| `{source: human}` | a ruling only a human can make |

A citation without `phase` cites this document. The seed is `phase: p0`.

---

## 2. The register schema

Each phase declares its document's shape in a register schema: a JSON Schema (draft 2020-12) file
with an `$id`, `transformation.schemas.REGISTER_SCHEMA_P<n>_V<k>`. The meta-schema
`SCHEMA_REGISTER_SCHEMA_V0` closes the surface: a keyword the evaluator does not implement is
refused when the schema is read, so a schema never says more than is enforced.

A schema declares:

- **Registers**, under `properties.registers.properties`. A table register is an array of rows; a
  text register is a string. `minItems: 1` means the register may not be empty. `x-section` names the
  document section it sits in. `x-business-language` names the columns that must hold business
  prose, or `true` for every column but the citing ones.
- **Columns**, under each register's `items.properties`. A column has a `title`, the type of its
  value (§1), and optionally `x-vocab: {artifact, group}`, a group of a `VOCABULARY` artifact its
  value must belong to. A vocabulary is referenced, never copied. A type several columns share is
  declared once under `$defs` and named by `$ref`.
- **The handoff**: `x-consumes` and `x-emits`, and `x-priors`, the earlier phases a document is
  judged against.
- **Observations**: `x-observations`, the inspection operations whose results the procedures read,
  each under the key it is read by.
- **Declared rules**: `allOf`, an ordered list (§4).

---

## 3. Rules derived from shape

Every schema expands into these rules, in this order, for each register it declares. They need no
entry in `allOf`.

| Finding | Refuses |
|---|---|
| `REGISTER_MISSING` | a declared register absent from the block |
| `REGISTER_EMPTY` | a text register with no text, or a register declared non-empty with no rows |
| `REGISTER_COLUMN_MISSING` | a row lacking a required column |
| `CELL_NOT_IN_VOCABULARY` | a value outside its column's vocabulary group |
| `CELL_NOT_OF_TYPE` | a value that is not of its column's type |
| `DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE` | an artifact code in a business-language column |
| `ROW_WITHOUT_SOURCE_FINDING` | a row whose citation is `null` or absent |
| `SOURCE_FINDING_UNRESOLVED` | a row none of whose citations names a register the phase may cite, the seed, a ruling or an artifact |
| `CITATION_ORDINAL_UNRESOLVED` | a citation naming a row past the end of the register it names |

A citation is resolved in the phase it names, or in this document when it names none. A register
in a prior that was not supplied is not read, and is not reported.

---

## 4. Declared rules

`allOf` is an ordered list. One entry is one rule, and the order is part of the rule set's meaning:
a sealed rule set is compared as a list.

Every entry carries:

- `x-finding`: the finding `code` an author reads, the rule's `intent`, and its `detail` text when it
  has one. A code is shared by every rule that finds the same kind of defect.
- `x-register`: the register it governs, unless it is about the whole document.
- `x-realises`: the invariant it realises, or the statement that specifies it. Required of every
  annotation and procedure.
- `x-columns`: the titles of columns it names that the register does not declare, which must be
  absent.

An entry states one of three things: a constraint (§4.1), an annotation (§5), or a procedure (§6).

### 4.1 Constraints

A constraint is written in this subset of JSON Schema, and nothing else:

| Keyword | Where | States |
|---|---|---|
| `minItems` | entry | the register has at least this many rows |
| `maxItems` | entry | the register has at most this many rows |
| `properties.header.required` | entry | these header fields are present |
| `properties.header.properties.<f>.pattern` | entry | these header fields match the pattern |
| `items.properties.<k>.minLength: 1` | entry | the column states a value |
| `items.properties.<k>.pattern` | entry | a text value in the column matches the pattern |
| `items.properties.<k>.not.pattern` | entry | no text value in the columns contains the pattern |
| `items.required` | entry | every row carries the column |
| `items.not.required` | entry | no row carries the column |
| `items.not.properties.<k>.const` | entry | no row holds this value in the column |
| `items.if` / `items.then` | entry | the constraint in `then` binds only the rows `if` selects, by `const` or `enum` on one column |

A pattern constrains text. A typed value, or a cell stating nothing, is not matched. A pattern is
anchored at the start of the value.

### 4.2 From a failing keyword to a finding

A constraint that fails yields one finding per row it fails on, or one for the register. The finding
carries the entry's code and intent. Its place is the register and the row. Its detail is the entry's
`detail`, with `{value}` replaced by the failing value, or `{token}` by the matched text, where the
detail names it.

---

## 5. Annotations

An annotation relates rows to other rows. It carries a `mode` and the `params` the mode reads.

### 5.1 `x-key`

| Mode | States |
|---|---|
| `unique` | no two rows carry the same value in the key's columns, compared on the bare identity |
| `contiguous` | the key's numbers run from 1 without a gap |

### 5.2 `x-reference`

| Mode | States |
|---|---|
| `resolves` | each value in the column names a row of the target register, optionally only for rows a gate selects |
| `covers` | each row of the target register is named by some row here |

### 5.3 `x-carriage`

Carriage relates this document to a register of a prior phase.

| Mode | States |
|---|---|
| `present_by_key` | each prior row reappears here, matched on its key columns |
| `confined` | each row here appears in the prior register |
| `cited` | each prior row is cited by some row here |
| `matches_cited` | a row citing a prior row states what that row stated |
| `identities_covered` | each identity the prior declares appears here |
| `prose` | the prior's text register is carried here |

A prior that was not supplied is reported once, as unchecked. A register missing from a supplied
prior is reported as the prior's defect.

### 5.4 `x-grounding`

Grounding relates the document to the pinned composition.

| Mode | States |
|---|---|
| `exists` | each identity the column claims exists in the composition |
| `absent` | each identity the column declares new does not |
| `reuse_eligible` | each reuse candidate comes from a domain that permits reuse |

---

## 6. Procedures

A procedure is a named check the general language cannot state as one rule:
`x-procedure: {name, params}`. Each is specified outside the code that runs it.

### 6.1 Specified by an invariant

| Procedure | Realises |
|---|---|
| `DISCHARGE_GROUNDED_IN_TOPOLOGY` | `BUSINESS_REFUSAL_DISCHARGED` |
| `DISCHARGE_OUTCOME_REFUSES` | `BUSINESS_REFUSAL_DISCHARGED` |
| `GOVERNING_RULE_IN_SEALED_SET` | `BUSINESS_REFUSAL_DISCHARGED` |
| `EMISSION_GROUNDED_IN_ENDING` | `ANNOUNCEMENT_FROM_COMPLETING_ENDING` |
| `READ_IS_DECLARED` | `REACH_DECLARED_AND_USED` |
| `REACH_IS_USED` | `REACH_DECLARED_AND_USED` |
| `DEPENDENCY_PRECEDES` | `BUILD_ORDER_TOPOLOGICAL` |
| `STEP_BINDINGS_MATCH_INTERFACE` | `DESIGN_NAMES_RESOLVE` |
| `CONTRACT_OUTPUT_PRODUCED` | `DESIGN_NAMES_RESOLVE` |
| `CELL_PREFIXED_BY_COLUMN` | `DESIGN_NAMES_RESOLVE` |
| `IMPLEMENTATION_MODULE_CONFORMS` | `DESIGN_NAMES_RESOLVE` |
| `UNRESOLVED_MARKER_ABSENT` | `NO_QUESTION_LEFT_OPEN` |

Each invariant is `lifecycle::INVARIANT_<name>_V0`.

### 6.2 Specified by a statement

These check properties of the composition a design will produce. Two anticipate a refusal the
protocol pipeline already makes. Twelve check a property nothing in the protocol pipeline refuses:
the design compiler is their only enforcement, until the protocol declares them.

#### STEP_OPERATION_PUBLISHED

A step names an operation its capability offers. A capability absent from the composition's
surface is reported, not skipped. The compiler refuses the same step at S4.

#### TOPOLOGY_ROUTE_RESOLVES

Every routing target is a node of the same workflow, or an ending. A target is a node's key, not a
contract. A route to a place the design does not redeclare resolves against the composition's
workflow. The build refuses an unresolved route when it verifies the dispatch.

#### BINDING_SOURCE_REACHABLE

A source rooted at another node names a node the workflow runs.

#### BINDING_SOURCE_PUBLISHED

An output binding reads a field the step's operation publishes.

#### STEP_INTERFACE_CONFORMS

A transform step hands its transform only the inputs the transform declares, and reads only the
outputs it answers, as the step's interface maps them.

#### NODE_INPUT_BOUND

A workflow node is handed every input its contract requires. An optional input left unbound is a
declaration that the node does not supply it.

#### ENTRANCE_SUPPLIES_GATE

An entrance supplies every field the gate of the workflow it invokes requires. The gate is the
workflow's `IN` node where the design states the topology, and otherwise the intent the composition
declares for it.

#### STEP_INPUTS_BOUND

Every input a step consumes is bound.

#### STEP_CONSUMES_PUBLISHED

A side-effect step hands its operation only fields the operation accepts.

#### CONSUMPTION_GROUNDED_IN_OPERATION

A side-effect step that consumes nothing invokes an operation that takes no input.

#### STORE_GROUNDED_IN_CAPABILITY

A step names a store exactly when its capability keeps records.

#### CROSS_SUBDOMAIN_REACH_READ_ONLY

An act reaching into another subdomain only reads what that subdomain holds. Whether an operation
writes is read from the operation's published `effect`, never from its name.

#### OUTCOME_GROUNDED_IN_OPERATION

A step branches only on outcomes its operation answers, or names the transform that interprets
the observation and the status that interpretation yields.

#### INTERPRETATION_TRANSFORM_REFUSES

A transform named to interpret an observation can refuse it: it raises, rather than returning its
judgement as a value.

---

## 7. Findings and verdict

A finding carries:

- the finding code;
- where it was found: the register, and the row where the rule reads rows;
- a detail, stating what is wrong in the author's terms;
- the intent of the rule that found it.

A document is `ADMISSIBLE` when no rule finds anything, and `INADMISSIBLE` otherwise.

---

## 8. Evaluation semantics

- **Every rule is evaluated,** in its sealed order. There is no short-circuit and no warning tier.
  An author needs the whole finding set, and a rule that never runs cannot be trusted.
- **The rule set is always supplied.** An evaluator has no default rule set: a default would judge
  one phase's document by another phase's rules.
- **An unknown rule kind fails the evaluation.** A rule skipped reports nothing over a subject
  nobody judged.
- **Emptiness is declared, never inferred.** `[]` and `null` are statements; an absent register is a
  finding.
- **An unsupplied prior differs from a missing register.** The first is the caller's omission and is
  reported as an unchecked handoff. The second is the upstream author's defect.
- **The composition is observed, never read directly.** Every fact about the pinned composition
  arrives through the inspection interface, as the observations the schema declares.
