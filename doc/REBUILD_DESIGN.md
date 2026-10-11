# Transformation Rebuild — Design

`REBUILD_CHARTER.md` decides that the module is rebuilt against a frozen oracle. This document is the
design of the rebuilt module. `TRANSFORMATION_UNRAVEL.md` is its analysis, cited by section as "U§".
A human gates this design before any code is written.

---

## 1. What the rebuilt module is

The module still does what the oracle does. A person drives a change through phases P0–P8, each phase
judges a document, and construction renders the artifacts the mandate schedules. Four things change.

1. **A phase document carries its facts as data.** Registers sit in one YAML Machine block, and
   prose sits around it. No table is read.
2. **A phase's rules are declared, not coded.** The shape of each phase's document is a JSON Schema.
   Its claims are invariants. What JSON Schema cannot state is a small annotation layer and 21
   named procedures, each specified by an invariant.
3. **A document, a verdict and an approval name the rule set that judged them.**
4. **Construction is governed on its own,** by its own constitution, invariants and mapping standard.

What does not change is listed in the charter (§4, "Unchanged"). In short: phases and gates, two
compilers, snapshot facts only through `inspector.api.query`, the pinned baseline, CLI only.

---

## 2. The phase document

### 2.1 Form

A phase document is Markdown with one Machine block, laid out as an artifact is:

````markdown
# Stage 3 — Analysis Loop: transformation / design

## Machine

```yaml
document:
  phase: p3
  domain: transformation
  subdomain: design
  cr: version_retirement
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
    - question_id: Q1
      finding: …
  open_questions: []
```

## 1. Analysis Findings

Prose for a person.
````

- **One block per document.** The block holds the header (`document`) and every register
  (`registers`), keyed by register id. The prose holds no fact the block holds, as human-block
  fidelity requires of an artifact.
- **The header replaces the bold header lines.** `Stage`, `CR` and `Feeds` become fields. `Status`
  goes: a document's standing is its verdict, not a field its author sets.
- **`rule_set` names the register schema's `$id`** the document was authored under (§5).
- **The p0 business problem statement stays prose.** It has no registers.

### 2.2 Registers as data

| Oracle convention (U§4.3, U§4.4) | Rebuilt form |
|---|---|
| marker comment and table | a key under `registers` holding a list of mappings |
| column matched by prefix | an exact key, in `snake_case` |
| `NONE IDENTIFIED` row | an empty list. An absent key is a missing register. |
| none markers (`-`, `NONE`, `N/A`) | `null`, or the key left out |
| vocabulary in a column header | a `VOCAB` artifact the schema references |
| routing `OUTCOME -> target; …` | a mapping, outcome to target |
| interface `in: a=b; out: …` | two mappings, `in` and `out` |
| comma-separated names | a list |
| a literal or a generated value in a binding | `{literal: …}` or `{generated: <artifact>}`, never a reserved word |
| a citation `S2 gaps #1` | a mapping `{phase: p2, register: gaps, row: 1}` |
| YAML inside a cell | YAML |

Every row of the left column is a convention the oracle states only in code. None survives.

---

## 3. Declared rules

### 3.1 Where each kind of rule goes

The oracle's 884 rules, sorted by what they constrain (U§6.7), go to three places.

| What the rule constrains | Goes to |
|---|---|
| Shape: presence, required and conditional cells, patterns, vocabularies, cardinality, header fields | the phase's **register schema**, as JSON Schema keywords |
| Relations: a key, a reference between registers, carriage from a prior phase, grounding against the composition | the register schema, as **annotations**, each citing the invariant it realises |
| Bespoke properties (tier B: S 2, G 12, T 7) | **named procedures**, each specified by a statement it realises |

Tier B's seven R kinds stop being procedures. Each becomes a schema constraint or an annotation:
`if`/`then` for a pattern chosen by another cell, a key for composite uniqueness, a reference for a
scoped resolution, and construction derives the module path (U§9.3, finding 3).

### 3.2 The register schema

- **One per phase,** a JSON Schema (draft 2020-12) file in `transformation/registry/schema/`, with an
  `$id` such as `transformation.schemas.REGISTER_SCHEMA_P3_V0`. It mirrors
  `software_governance/registry/schema/`. Schema files are substrate, not artifacts (U§9.1).
- **A meta-schema closes its surface.** `SCHEMA_REGISTER_SCHEMA_V0` admits the keywords the evaluator
  implements and the annotation constructs, and nothing else.
- **Vocabularies are referenced, never copied.** A column's vocabulary is `x-vocab: <VOCAB FQDN>`,
  resolved from the pinned composition when rules are sealed. The templates carry 32 distinct inline
  vocabularies today. Each becomes a `VOCAB` artifact or reuses one that exists.
- **Every constraint declares its finding code.** `x-finding: REGISTER_COLUMN_MISSING`. The finding
  code is what an author reads. It stays shared across rules, as in the oracle (U§9.2).
- **A dispatch selects the schema per phase.** `STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0` maps phase to
  schema `$id` and to the phase's workflow, replacing `catalog.PHASES[].template`.

### 3.3 The annotation layer

Four constructs, the relational part of a schema plus the two the lifecycle adds (U§9.3):

| Construct | States | Example |
|---|---|---|
| `x-key` | which fields identify a row; a second row with the same key is a finding | `(workflow, node)` in p7 topology |
| `x-reference` | a field resolves in another register, optionally scoped by a shared key | a binding's node resolves in the topology of the same workflow |
| `x-carriage` | rows of a prior phase's register are carried here: none dropped, none invented, restatements match | p1 constraints carry the seed's constraints |
| `x-grounding` | a field names an identity that must exist, or must not exist, in the pinned composition | a `NEW` code is unused |

Each annotation names the invariant it realises (`x-realises: transformation::INVARIANT_…_V0`).

### 3.4 Named procedures

The 21 tier-B procedures that remain (U§9.3) stay code. Each is specified outside code:

- **T (7):** by a transformation invariant.
- **S (2):** by the protocol enforcement it anticipates, cited by FQDN.
- **G (12):** by a statement of the composition property, in the language standard (§3.6), until the
  protocol declares it. Declaring them in `software_governance` is the protocol track, outside this
  rebuild (charter §4).

A procedure is invoked from the schema: `x-procedure: <name>`, with its params.

### 3.5 Rule identity and findings

- **A rule's identity is where it is declared:** the schema `$id` plus a JSON Pointer to the
  constraint or annotation. A procedure's identity is the FQDN of the invariant that specifies it, or
  of the statement for a G procedure (U§9.2).
- **Expansion.** `phase emit` expands each schema into rules and seals them into the phase's `WF_P*`,
  as the oracle does. Each sealed rule carries its identity. Sealing is how the schema reaches the
  runtime (U§9.8).
- **A finding carries** the finding code, the rule identity, a structured locator
  `{register, row, field}`, and a detail.
- **A citation names a rule identity,** so `GOVERNING_RULE_IN_SEALED_SET` resolves exactly one rule.

### 3.6 The language standard

`transformation/doc/DESIGN_LANGUAGE.md` specifies what an independent evaluator needs, and nothing it
can take from JSON Schema's own specification:

- the document form (§2);
- the evaluator's subset of JSON Schema, and how a failing keyword becomes a finding;
- the four annotation constructs;
- the 21 procedures, each by the statement that specifies it;
- the finding shape;
- evaluation semantics: every rule is evaluated, with no short-circuit and no warning tier; an
  absent register is a finding; an unsupplied prior differs from a missing register (U§9.5).

### 3.7 Invariants and constitutions

**Two constitutions,** one per concern, matching the subdomains: `CONSTITUTION_DESIGN_V0` (design
admissibility) and `CONSTITUTION_BUILD_V0` (construction determinacy) (U§9.5).

**Eighteen invariants,** `artifact_kind: INVARIANT`, `enforcement_stage: enforced_elsewhere`, with
`enforced_by` naming the phase workflow or the construction workflow (U§6.6).

| Concern | Invariants |
|---|---|
| design (14) | `ROW_PROVENANCE_CITED`, `UPSTREAM_COMMITMENT_CARRIED`, `CONTENT_ENTERS_AT_OWNING_PHASE`, `RESTATEMENT_MATCHES_SOURCE`, `EXISTING_ARTIFACT_OBSERVED`, `NEW_IDENTITY_UNUSED`, `REUSE_FROM_PERMITTING_DOMAIN`, `NO_QUESTION_LEFT_OPEN`, `PHASE_SPEAKS_ITS_RUNG`, `TOUCHED_SUBDOMAIN_DECLARED`, `BUSINESS_REFUSAL_DISCHARGED`, `ANNOUNCEMENT_FROM_COMPLETING_ENDING`, `REACH_DECLARED_AND_USED`, `BUILD_ORDER_TOPOLOGICAL` |
| build (4) | `DESIGN_UNIQUELY_DETERMINES_ARTIFACT`, `RENDER_INVENTS_NOTHING`, `ONE_PRODUCER_PER_ARTIFACT`, `MEANING_CHANGE_IS_NEW_IDENTITY` |

Phase key rules stay in the dispatch as each phase's summary, naming the invariants they profile.

**A closure check** extends `phase meta` (U§3):
- every annotation and procedure cites an invariant or statement that resolves;
- every invariant is realised, or declared not enforced;
- every `enforced_by` names a workflow that exists;
- every S procedure cites a protocol invariant in force;
- every evaluator keyword and construct is used.

### 3.8 Templates

A template is a human guide: elicitation prose, the document contract and guidance. Its Machine block
skeleton is checked against the schema by the closure check, never read as the source of shape
(U§6.5).

---

## 4. The evaluator

### 4.1 Pipeline

```
document text ──► read: split prose / Machine block, parse YAML ──► document data
schema $id ─────► sealed rules (from the phase's WF_P*) ─────────┐
prior documents ► read ──────────────────────────────────────────┤
composition ────► inspector.api.query ───────────────────────────┤
                                                                 ▼
                                       evaluate every rule ──► findings ──► verdict
```

- **Read** does nothing but split and parse. No convention is applied.
- **Evaluate** interprets three things: the evaluator's JSON Schema subset, the four annotation
  constructs, and the procedures. It does not call a third-party validator. That keeps the finding
  codes and details authors read today (U§9.1), which behavioural identity needs.
- `jsonschema`, already a core dependency, validates schemas against the meta-schema. It does not
  judge documents.

### 4.2 Code shape

| Oracle | Rebuilt |
|---|---|
| `design/read.py`, `template_reader.py` (tables) | `design/read.py`: Machine block in, data out |
| `design/p*/rules.py` (9 files, 1,600+ lines of declarations) | gone. Rules come from schemas. |
| `design/derive.py` (template → rules) | `design/expand.py`: schema → sealed rules |
| `design/checks.py` (3,210 lines: 27 kinds, 34 bespoke kinds, conventions) | `design/evaluate/`: keyword subset, four constructs, `procedures/` with one module per procedure |
| `design/catalog.py` | the dispatch structure, read through the composition |
| `design/meta.py` | `design/meta.py`, with the closure check |
| `build/render.py` (21 cell-convention sites) | `build/render.py`, reading structured values |
| `build/completeness.py`, `generators.py`, `sameness.py` | kept, under the build invariants; `sameness`'s applied subset moves into `VOCAB_DECLARATION_REPRESENTATION_V0` (U§9.7) |

Imports stay absolute from `transformation.*`. `inspector.api` stays the only cross-repository import.

---

## 5. Rule effectivity

From `dossiers/rule_effectivity/p0_business_problem_statement.md` and U§9.6:

- **A document names its rule set:** `document.rule_set`, the schema `$id`.
- **A verdict names the rule set that judged it:** `judged_by` is the schema `$id` and its revision,
  not a snapshot path.
- **The schema carries its revision history.** Each revision states what changed and whether it is
  retroactive. A retroactive revision takes a new `$id`.
- **`phase emit --check` refuses** sealed rules that differ from the schema, unless a revision records
  the difference.
- **Approvals re-confirm.** An approval names the rule set it was given under. When that set is
  superseded, the approval stands unconfirmed until a person re-confirms it against the new set.
- **The difference between two rule sets is named rule by rule,** by rule identity.
- **No retention is needed.** A superseded rule set is read from the schema's history and git, not
  from a superseded `WF_P*` kept in the live tree.

---

## 6. Construction

- **Render reads structured values.** Routing, interfaces, bindings and literals arrive as mappings,
  so the cell parsing in `render.py` goes. A literal renders as its value, and `{generated: …}` is
  never rendered: the generator produces it (`ONE_PRODUCER_PER_ARTIFACT`).
- **One literal specification.** The language standard states what a literal is. The design side and
  construction both read it (U§9, obligations).
- **The render transform gains test vectors** pinning how a literal renders (U§9, obligations).
- **A construction-mapping standard,** `transformation/doc/CONSTRUCTION_MAPPING.md`, states how each
  register field becomes an artifact field and under which provenance class. The mapping stays
  code, governed by the four build invariants and specified by the standard, as protocol projection
  is (U§9.7).

---

## 7. Artifacts at the swap

### 7.1 The rule

Single instance (charter §6): each artifact has one live version. An artifact whose meaning is
unchanged keeps its identity. One whose meaning changes takes the next version never used, and names
its predecessor in `supersedes`. Every other version is deleted and recorded.

Meaning is decided by `sameness` over `VOCAB_DECLARATION_REPRESENTATION_V0`, run against the oracle's
declaration. It is never decided by hand.

### 7.2 What the rebuild expects

| Group | Expected outcome |
|---|---|
| Phase workflows `WF_P0`–`WF_P8` | new versions: their sealed rule sets change |
| Readers `CT_PURE_PARSE_REGISTERS`, `CT_PURE_PARSE_PRIOR_PHASES`, evaluator `CT_PURE_EVALUATE_RULES` | new versions: they read and judge a different form |
| Judging contracts `CC_JUDGE_*`, `CC_CONSTRUCT_ARTIFACTS` | identity kept if they only re-point; `sameness` decides |
| Build transforms `CT_PURE_RENDER_ARTIFACTS`, `CT_PURE_MEASURE_COMPLETENESS`, `CT_PURE_ATTRIBUTE_PROVENANCE` | `sameness` decides |
| Intents, runtime bindings, actors | identity kept unless `sameness` finds a change |
| Node keys | renamed to their contract's live code |
| `STRUCTURE_FIGURE_OF_MERIT_POLICY` | V1 kept; V0 deleted |
| New | 2 constitutions, 18 invariants, `STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0`, the `VOCAB` artifacts of §3.2 |
| Deleted | every stood-down transformation artifact, 11 of them listed in `.github/process/notes/rebuild-retirements.yaml` |

The exact table is produced by the build, entered in charter §8, and recorded in the genesis dossier.

### 7.3 Workspace checks the swap touches

- **`published_identity_check.successors()`** reads `superseded_by` on the predecessor. Once the
  predecessor is deleted, a re-point to its successor would read as a change of meaning. It must
  also read `supersedes` on the live successor.
- **The single-instance check** (charter §6) is new.
- **`supersession_agreement`** already accepts a predecessor recorded as deleted.
- **Surface closure** needs the platform fix (charter §6, option B) before the swap.

---

## 8. Proving it against the oracle

### 8.1 The corpus

- **What it holds:**
  - the 71 testbed documents;
  - the 83 e2e payloads;
  - the five catalog fixture dossiers;
  - test copies of the design and mandate of the 16 delivered dossiers that construction acceptance
    reads (U§9.10 R3).
- **The converter** runs the oracle's reader in the oracle worktree. It writes what the reader
  returns as a Machine block, with structured values (§2.2). A cell the converter cannot structure,
  such as a malformed routing string a negative test exists to refuse, is written as the string it
  was. The rebuilt schema then refuses its type.
- **The converter is deleted at the swap,** with nothing left that reads a table.

### 8.2 The comparison

A harness runs the oracle on each Markdown original, as a subprocess against the worktree, and the
rebuild on its conversion. For each document it compares:

1. **the verdict:** identical;
2. **the findings,** as a multiset of (finding code, register, row): identical after the code map;
3. **the detail:** identical for every rule that keeps its finding code.

**The code map** is the one place a difference is allowed. An oracle finding code the structured form
retires (for example a malformed routing string, now a type finding) maps to the rebuilt code that
replaces it. Each entry is a divergence, listed in charter §8 before the code that causes it is
written.

**Declaration identity** compares the oracle's 884 expanded rules with the rebuild's, rule for rule.
Each oracle rule maps to one rebuilt rule identity, or to a divergence that retires it.

### 8.3 Milestones on the branch

The rebuild is one branch, built in milestones. Each milestone ends with the oracle comparison
green, and a red comparison stops the next one.

Structure was planned as its own milestone. It is built with the declared rules instead: a schema
states a value's type, so structured values and the schemas that type them arrive together, and the
generic checks are replaced once rather than reworked and then replaced. The divergences confirmed
for it (charter §8) apply unchanged.

| Milestone | Builds | Proven by |
|---|---|---|
| M1 Form | Machine block reader; converter; writers (projection) | the oracle's findings on every conversion, unchanged |
| M3 Declared rules and structure | in four steps, each ending with the comparison green | |
| — M3.1 Schemas | register schemas from the templates, meta-schema, dispatch, `VOCAB`s | the schemas expand to the oracle's 633 derived rules, rule for rule |
| — M3.2 Declarations | the 250 hand-declared rules as constraints, annotations and procedures; `rules.py` a loader | declaration identity over all 884 rules |
| — M3.3 Structure | structured values, the keyword evaluator, procedures and construction reading structure | the comparison, through the code map |
| — M3.4 Governance | invariants, constitutions, closure check, rule identity, structured locators | the closure check, and the comparison unchanged |
| M4 Effectivity | `rule_set`, `judged_by`, revisions, re-confirmation, the header | its own tests, plus the comparison unchanged |
| M5 Construction | build constitution and invariants, mapping standard, literal vectors | construction identity |

Then come the genesis dossier, the single-instance check, `regression.sh --all`, and the swap
(charter §10).

---

## 9. Decisions for the gate

These were proposed in the analysis and never confirmed. The design depends on each of them.

1. **Tier B dispositions.** R 7 / S 2 / G 12 / T 7 (U§9.3, §3.1 above).
2. **The invariant set and names.** 14 design and 4 build invariants (§3.7). "Carried" and "owned"
   are kept apart.
3. **Constitutions.** Two, `design` and `build` (§3.7).
4. **The evaluator implements its own JSON Schema subset** rather than calling a validator, to keep
   finding codes and details (§4.1).
5. **The language standard and the mapping standard live in `transformation/doc/`** on the branch. Moving
   them to `standards` is a later decision.
6. **G procedures are specified by statements in the language standard,** not by invariants, until
   the protocol declares them (§3.4).
7. **The comparison allows a code map,** each entry a divergence declared before it is built (§8.2).
