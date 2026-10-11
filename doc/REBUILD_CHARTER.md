# Transformation Rebuild — Charter

This charter replaces the delivery plan of `TRANSFORMATION_UNRAVEL.md` §10. The analysis in that
document stands, and becomes the specification of the rebuild.

---

## 1. Why a rebuild

The unravel was planned as five changes, each a dossier judged by the transformation lifecycle.
That plan oscillates instead of progressing.

- **The tool judges its own redesign.** Each defect in the tool blocks the dossier that would fix
  it. The fix must run first as a dossier of its own, and it can hit the next defect.
- **The chain only grew.** Five dossiers were opened. Two were delivered as fixes
  (`binding_literals`, `quoted_literals`). `register_format` is parked behind `version_retirement`,
  and that is blocked by a platform invariant. None of the five reached the target.
- **Succession costs most during development.** Every replacement carried its predecessor, and the
  carried versions then blocked the next change. Development has no consumer of the live tree to
  protect.

The target has not changed: rules visible without reading code, one design language, no
force-fitted concepts.

## 2. The decision

Freeze the current transformation module. It becomes the **oracle**. Rebuild the module on a branch,
designed once from everything the unravel learned. Replace the old module whole when the rebuild
meets the oracle.

This is a rebuild against a fixed oracle, not greenfield. Evolution is never greenfield. The frozen
module and the composition it produced are the baseline the rebuild is measured against.

## 3. The oracle

- The transformation repository, at the checkpoint commit on `dev/18`, tagged `oracle/transformation`.
- The working composition built from that commit, with its regression at 71/71.
- From the tag until the swap, `dev/18` takes no change to transformation except one that the rest
  of the workspace needs to stay green. Each such change is applied on the branch as well.

## 4. Scope

**In scope.** The five changes of the unravel, designed as one:

1. **Format.** Registers carried as a structured block apart from the prose (§9.9). One form, with
   no reading of tables.
2. **Structure.** Values inside cells given structure: routing, bindings, literals and generated
   values (§9.9, and the obligations in §9).
3. **Design unravel.** Rules declared as artifacts, not code (§3, §6):
   - transformation invariants under the platform's lifecycle constitutions (§6a);
   - a register schema per phase;
   - each expanded rule identified by schema `$id` and JSON Pointer (§9.2);
   - findings with structured locators (§4.6);
   - `rules.py` reduced to a loader, `checks.py` kept as the interpreter.
4. **Rule effectivity.** A document, a verdict and an approval name the rule set that judged them
   (§9.6, `dossiers/rule_effectivity/p0_business_problem_statement.md`).
5. **Construction.** Governed and specified on its own, against the same declarations (§9.7).

**Out of scope:**
- re-expressing tier-B kinds (§9.3);
- an independent evaluator (§8.5);
- the protocol track (§9.4);
- any feature not named above.

A need found during the rebuild that is not in this list goes on the list below, not into the build.

**Unchanged.** The doctrine in `transformation/CLAUDE.md`:
- phases P0–P8 and their gates;
- two compilers;
- snapshot facts only through `inspector.api.query`;
- the pinned baseline;
- CLI only, with no boundary contract;
- a deterministic oracle with assistive drafting.

## 5. Acceptance

The rebuild replaces the old module only when every item below holds. A deliberate divergence is
entered in §8 before the build is written, never after it is seen.

1. **The corpus.** Every test document and every delivered dossier, converted mechanically by the
   oracle's reader into the new form. A delivered dossier's original is never edited. The tests read
   its converted copy.
2. **Declaration identity.** The rebuild's expanded rule set equals the oracle's, rule for rule,
   apart from the divergences in §8.
3. **Behavioural identity.** The rebuild gives every corpus document the oracle's verdict and
   findings: the rule, register, row and detail. The oracle runs live beside the rebuild. Its
   output is not replayed from a record.
4. **Construction identity.** From the converted corpus, construction reproduces every artifact the
   oracle reproduces.
5. **Closure.** Every rule cites an invariant that resolves. Every invariant is realised or declared
   not enforced. Every check kind is used (§3).
6. **The workspace.** `regression.sh --all` passes. The rebuild updates `expectations.yaml` only
   for counts that it explains in §8.
7. **The genesis dossier.** One dossier, P0–P8, in the new form, describes the rebuilt module as it
   stands: every transformation artifact at its one live version. The rebuilt module admits it. This
   is a fixed point the rebuild must reach. It does not replace items 2–4, which measure the rebuild
   against something other than itself.
8. **Single instance.** The single-instance check (§6) passes on the transformation domain.

## 6. Identity at the swap

Development is open. `.github/process/retention.yaml` declares that nothing is retained for its own
sake.

**Single instance.** Each artifact exists in exactly one version in the live tree.
- An artifact whose meaning is unchanged keeps its identity.
- An artifact whose meaning changes takes the next version never used before: not in the v5 release,
  not in the live tree, and not in the ledger. It names its predecessor in `supersedes`.
- Every other version is deleted, and recorded in `.github/process/retired_identities.yaml`.
- A deleted name is never reused.
- History is held by the v5 release at its tag, the ledger, `supersedes` on the one live version,
  and git. The live tree holds what runs.

**The single-instance check.** A new workspace check, beside `published_identity_check`. It groups
the live tree by artifact name without its version suffix, and reports any name present in more
than one version. It reads the same ledger. It runs on the transformation domain from the swap, and
on every domain once the sweep (§10, step 7) is done.

**Node keys follow their contract.** A workflow node's key is the live name of the contract it runs.
No node key spells a deleted version, even as a place.

**Surface closure.** A deletion leaves the successor's `supersedes` naming an absent identity. The
platform's surface closure refuses that today. The fix is decided (option B):
- `supersedes` records history and is exempt from surface closure;
- `supersession_agreement` checks it against the ledger;
- it is a `software_governance` change, judged by the frozen oracle, so the oracle does not judge its
  own redesign;
- it lands before the swap.

**What the swap deletes from the transformation domain.**
- Every stood-down artifact, the eleven of `.github/process/notes/rebuild-retirements.yaml` among them.
- Every capability-transform implementation the rebuild no longer names. `implementation_closure`
  shows none is left.
- The table reader, and the converter once it has produced the corpus.
- The test harnesses written for the old form.

**What the swap also deletes.** Everything the rebuild needed and the rebuilt module does not:
- every dossier under `dossiers/`. The genesis dossier (§5, item 7) describes the module as it
  stands and is the only one that remains. Delivered dossiers are held by the v5 release at its
  tag and by git;
- the working documents: `TRANSFORMATION_UNRAVEL.md`, `REGISTER_COVERAGE_VERIFICATION.md`, this
  charter and `REBUILD_DESIGN.md`, once their rulings are restated in `DESIGN_LANGUAGE.md` and the
  repository's `CLAUDE.md`;
- `scripts/rebuild/`, once the oracle is retired;
- the testbed's `delivered_copies/`, and any payload or harness nothing reads.

The repository's `CLAUDE.md` is rewritten for the rebuilt module in the same change.

**What stays.** These are records, not code:
- the v5 release at its tag;
- generator scripts kept under `.github/process/notes/` (v5 ruling C1);
- the parked dossiers (§9).

## 6a. Allocation

The rebuild splits declarations from code, as the platform splits `software_governance` from
`protocol_compiler`.

**Governance goes to `software_governance`.** The transformation invariants live in
`software_governance/registry/lifecycle/invariants/`, as `lifecycle::INVARIANT_…_V0`.
- **Why.** A domain build cannot author an INVARIANT or a CONSTITUTION. The chain relations that make
  one authoritative (declared by a constitution rule, resolved, paired with its ASSERT) are proved
  only on the platform surface, and `governance_chain_closure` refuses a domain build that admits
  either kind.
- **The `lifecycle` namespace.** It is already authorized, and already governs this lifecycle:
  `lifecycle::CONSTITUTION_CHANGE_MGMT_V0` the design pipeline and `CONSTITUTION_CONSTRUCTION_V0`
  construction, both enforced by process alone and written in RI-0's stages. A `transformation`
  namespace on the platform would change the published `STRUCTURE_IDENTITY_V0`, which the compiler
  loads by name.
- **The constitutions are superseded, not added to.** `CONSTITUTION_CHANGE_MGMT_V1` names the 16
  design invariants and the human gates; `CONSTITUTION_CONSTRUCTION_V1` names the 4 construction
  invariants. Both restate their concern in phases. Both V0s are deleted at the swap and recorded
  in the ledger (`.github/process/notes/rebuild-retirements.yaml`): the next release starts from the
  live tree, and v5 keeps them at its tag.
- **`enforced_by` is prose.** A platform artifact cannot name a domain artifact, so each invariant
  states its mechanism in words, as platform invariants enforced elsewhere already do: the design
  compiler evaluating a phase's sealed rule set, or the construction compiler measuring a design.
- **Proved.** The platform compiles them, the governance chain closes, published identity holds,
  and the composition assembles.

**Code and composition stay in the transformation repository.** It keeps both compilers, the CLI,
the transform implementations, and the tool domain that dispatches them: the phase and construction
workflows, the judging contracts, the transforms, intents and bindings. The platform hosts no
workflows or contracts, and the compilers stay replaceable code behind declared rules.

**The repository is renamed `transformation_compilers` at the swap.** The import package, the
domain name and the `transformation::` namespace do not change, so no published identity moves. The
rename touches workspace paths (the regression's domain list, the assembler's candidates,
`release.sh`, `pgc_install`, the snapshot profiles and the instruction files) and the GitHub
repository name. The swap replaces the repository whole, so the rename rides with it.

## 7. Governance exception

The rebuild is not judged by its own lifecycle while it is built, because the tool that would judge
it is the tool being replaced. Its genesis dossier (§5, item 7) is written in the new form and
judged by the rebuilt module once the build is done.

- This is an exception, made openly, and it is the reason for this charter. The generated-artifacts
  exception was declared the last one. This charter re-opens that ruling, so the exception is
  recorded in `.github/process/rulings.md` before the branch opens.
- **What stands in for the lifecycle.** The oracle in §5 decides whether the rebuild is admissible.
  A human approves this charter and the design before any code. A human approves the swap.
- After the swap, every change to transformation goes through the lifecycle again, judged by the
  rebuilt module.

## 8. Divergences and additions

The deliberate differences from the oracle, each with its reason, entered before it is built. The
rebuild starts with these:

| Item | Divergence | Reason |
|---|---|---|
| Form of a phase document | Structured block, not tables | Format, in scope (§4.1). |
| Retained phase workflows and contracts | Deleted, with a ledger entry | Development retains nothing for its own sake (§6). |
| Versions of one artifact | Exactly one in the live tree | Single instance (§6). |
| Node keys that spell a deleted version | Renamed to the contract's live name | Nothing live spells a deleted version (§6). |
| Table reader, converter, old-form harnesses | Deleted | No dead code (§6). |

### M3.1 — schemas

| # | Oracle | Rebuild | Effect |
|---|---|---|---|
| M3.1-1 | `Family` is declared in two orders: p5 `provisional_codes` and p7 `new_artifacts`. | One vocabulary group, `artifact_family`, in p5's order. | The p7 rule's `vocabulary` param, and the detail of its findings, list the values in p5's order. |

### Structure (planned as M2, built in M3)

Confirmed. Structure is built with the register schemas in M3, because half of what a schema states
is the type of a value (design §8.3). Each line says what the oracle does, what the rebuild does, and
what that moves in the comparison. Counts are cells in the converted corpus.

| # | Oracle | Rebuild | Effect on findings |
|---|---|---|---|
| M2-1 | A column is found by the start of its name (C3). | A row is a mapping with exact `snake_case` keys, taken from the template's column name without its vocabulary. A rule names the full key. | None expected. A rule whose param is only a prefix is corrected to the full name. |
| M2-2 | A register's columns are its header row. A missing header is `REGISTER_COLUMN_MISSING` at the register. | Columns are declared by the template. Every row carries every declared key, `null` when it says nothing. A row lacking a key is `REGISTER_COLUMN_MISSING` at that row. | Location moves from register to row. |
| M2-3 | The sentinel row `NONE IDENTIFIED` declares an empty register (C5), 475 cells. | An empty list declares it. | None. Row numbering no longer counts the sentinel. |
| M2-4 | A table with no rows and no sentinel is `REGISTER_EMPTY`, 237 registers. | The key with a `null` value: present, and stating nothing. An empty list is a declared empty register. | None. |
| M2-5 | `—`, `-`, `NONE`, `N/A` mean a cell says nothing (C6), 2,591 cells. | `null`. A kind's own none markers become `null` the same way. | None expected. A vocabulary column that admitted a marker as a value is listed if one appears. |
| M2-6 | Routing is `OUTCOME -> target; …`, malformed segments dropped (§4.4), 2,291 cells. | A mapping, outcome to target. The converter writes a cell it cannot parse as the string it was. | A malformed routing string becomes a type finding. Each such corpus case is listed in the code map. |
| M2-7 | Interface is `in: a=b, …; out: …`, 430 cells. | Two mappings, `in` and `out`. | As M2-6. |
| M2-8 | Name lists are comma-separated, dashes dropped. | Lists. | None expected. |
| M2-9 | A binding is a path, a quoted or numeric literal, or the word `generated`. | A path string, `{literal: …}`, or `{generated: true}`. Construction renders the same values. | `BINDING_SOURCE_MALFORMED` no longer sees literal spellings. `GENERATED_SOURCE_WITHOUT_GENERATOR` reads the typed marker. |
| M2-10 | A test value is YAML inside a cell, and one that does not parse is `TEST_VALUE_UNPARSEABLE`, 744 cells. | A native YAML value. | `TEST_VALUE_UNPARSEABLE` retires: a value that does not parse is a document that does not parse. Its two probes go. |

**Deferred from M2 to M3: citations.** Provenance cells (15,337) carry several idioms: `S2 gaps #1`,
`CR seed §7 Constraints #1`, ordinals like `Q3` and `GAP-1`, literal sources, and free text after a
dash. About 250 rules judge them, most of them carriage rules. Their structure is the carriage
annotation M3 designs (`x-carriage`, design §3.3). Structuring them in M2 would design that twice.
They stay strings in M2.

**Deferred from M2 to M4: the header.** `Stage`, `CR`, `Status` and `Feeds` stay as they are until M4
adds `rule_set` and drops `Status`.

### M3.3a — structure, built

Confirmed with the structure divergences above (M2-1 to M2-10, citations and the header deferred).
Measured over the corpus, the fixtures and the test copies before any code.

| # | Oracle | Rebuild | Effect |
|---|---|---|---|
| M3.3-1 | A gate compares upper-cased values (C8). | Exact comparison, as JSON Schema `const` and `enum`. | Gate columns are vocabulary columns; none of 20,820 vocabulary cells matches only when upper-cased. None expected. |
| M3.3-2 | A vocabulary compares the upper-cased cell (C11). | Exact membership. | None: 0 of 20,820 cells. |
| M3.3-3 | A reference splits its cell on `;` and resolves each part. | A reference cell is one value. | None: no cell of the 21 referencing columns holds a `;`. |
| M3.3-4 | — | A value of the wrong type is `CELL_NOT_OF_TYPE`, one derived rule per typed column. | New rules in p7 (12) and p8 (1) only. A column whose value may be anything declares no type and gets no rule. No corpus document holds a value of the wrong type, so the comparison needs no code map. |
| M3.3-5 | Rule params name columns by title. | Unchanged in M3.3a. A title is read through the schema's key function, the one that keyed the column. | None. The sealed p0 and p1 rule sets do not change. The p7 and p8 workflows that do change, `WF_P7_…_V2` and `WF_P8_…_V1`, were not published in v5, so they are re-emitted in place and need no successor (D3 applies to a published one). |
| M3.3-6 | A governed hole's detail names the column by its heading. | It names the column by its key. | Detail text only; compared without the column. |
| M3.3-7 | Four p7 columns keep a lowercase vocabulary in their title (`Kind (atom, molecule)`), and two rules name a column by its full heading (`Storage Type (CS_…)`). | Titles and params are the bare column names (`Kind`, `Purity`, `Refusal`, `Storage Type`). | None: the rules named the bare names already, and were read by prefix. |
| M3.3-8 | An ending's routing written `emit <moment>` reads as no routes. | `null`. The moment is declared as an `emit.<ending>` property, which construction reads. | None: 6 cells in the cr_05 fixture, and the same notation in 4 delivered blockchain designs. |
| M3.3-9 | A test value is unstated when its cell is blank (`CELL_NOT_EMPTY`). | A test value may be anything, `""` and `null` included, so it is unstated only when its row leaves the column out (`CELL_PRESENT`, `required`). | None: no corpus row leaves a test value blank. |
| M2-2, measured | A register missing a column is a finding even with no rows. | A register with no rows has no column to miss. | 2 documents (`declared_reach`, `refusal_discharge` p7, `vocabulary_extensions`). |

**Lists.** Measured: `Depends On`, `Consumes`, `Produces`, `CS Bindings`, `Generator Sources`,
`Consults`, and `artifact_properties.Value` for the properties that name several values. Every
other column stays one string.

### M3.3b — citations, built

A citation is a mapping naming what it cites, declared once per schema as `$defs/citation`:
`{phase, register, row}` or `{phase, register, key}` for a row, `{phase, register}` for a whole
register, `{artifact}` for an identity in the composition, and `{source: human}` for a human ruling.
No `phase` means this document. A cell citing several holds a list. Typed: every `Source Finding`
column and `verification_results.Origin`. `Evidence` and the seed's `Source` stay prose. Measured
over 15,767 cells: 11,160 by key, 2,967 by ordinal, 1,125 of the seed by section, 492 human, 2
identities, 16 several.

| # | Oracle | Rebuild | Effect |
|---|---|---|---|
| M3.3b-1 | A citation is text read by pattern. A seed is cited by section number and a free-form title (`CR seed §4 Known Facts #14`); `CR seed`, `human decision`, `projection` and `S1 seed` are literal sources. | A mapping. The seed's section resolves to its register at authoring; the title goes. `literal_sources` goes: the seed is `phase: p0`, a ruling is `source: human`, and `projection` and `S1 seed` were used nowhere. Text that is no citation is refused by its type. | `SOURCE_FINDING_UNRESOLVED` shows the mapping; compared by register and row. `I remembered it` is `CELL_NOT_OF_TYPE`, compared as the unresolved citation it was. |
| M3.3b-2 | A row citing nothing has a blank cell (`CELL_NOT_EMPTY`). | `null`, refused by `CITATION_PRESENT` (D1). | Same findings. |
| M3.3b-3 | `CITATION_ORDINAL_UNRESOLVED` reads only `S<n> register #k`, never a seed citation. | It reads every citation with a row, the seed's included. | One fixture: a seed ordinal past the end is reported by both ordinal rules. The overlap goes when they merge in M3.4 (D4). |
| M3.3b-4 | `GOVERNING_RULE_NOT_IN_FORCE` names each phase's workflow by identity, a copy of the emitter's map. | By its code without a version; the version in force is the latest the pinned composition carries. | None. A literal identity cannot be right both against a pin and against the live build once a phase workflow has a successor. |

Multi-citations are each resolved, not only the first (D2). No corpus finding changed by it.
`WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0` is published, so its changed rule set is sealed into
`WF_P1_…_V1`, which supersedes it (D3). `WF_P2`–`WF_P7` are unpublished and re-emitted in place.

### M3.4a — procedures, built

Five procedures are restated in the general language. Three stay procedures, for want of a
construct that would not be one in disguise.

| # | Oracle | Rebuild | Effect |
|---|---|---|---|
| M3.4a-1 | `TOPOLOGY_KEY_UNIQUE`, `CELL_NOT_PREFIXED`, `STORE_PATH_MATCHES_STORAGE`, `BINDING_SOURCE_ROOTED` and `BINDING_SOURCE_WELL_FORMED` are procedures. | A composite `x-key` on `(Workflow, Node)`; a case-insensitive `not: pattern` on `Belief`; one `if`/`then` pattern per storage capability (3); a pattern on `Bound To`; one `if`/`then` pattern per direction (2). | Same rows refused. The general kinds word their findings their own way; compared by code and place. p7 seals 279 rules. p0's rule set changes, and `WF_P0_SEED_ADMISSIBILITY_V0` is published, so `WF_P0_…_V1` supersedes it (D5). |
| M3.4a-2 | Two rules resolve an ordinal citation: `CITATION_ORDINAL_UNRESOLVED` on every traceable register, and `CITATION_ROW_UNRESOLVED` on p1's 19. | One: `CITATION_ORDINAL_UNRESOLVED`, resolving each citation in the phase it names, or in this document (D4). | A row the oracle reported twice is reported once. Compared once per row. p1 seals 189 rules. |

**Kept as procedures.** `CONTRACT_OUTPUT_PRODUCED` and `STEP_BINDINGS_MATCH_INTERFACE` relate a
field to a field of another register scoped by two columns and a direction, or to the keys of a
mapping inside a cell. `DEPENDENCY_PRECEDES` compares positions. A reference able to state these would
carry parameters for one rule each. `CELL_PREFIXED_BY_COLUMN` relates two cells of one row, and
`UNRESOLVED_MARKER_ABSENT` reads every cell of every register but the exempt. Each is specified in
M3.4b. `IMPLEMENTATION_MODULE_CONFORMS` goes with its column in M5 (D6). 26 procedures remain.

### M3.4b — governance, built

- **Twenty invariants,** `lifecycle::INVARIANT_…_V0` in `software_governance` (§6a): the 18 the
  design names, and two it did not. 49 rules state that a design agrees with itself and is complete
  (references that resolve, keys, coverage), and none of the 18 covered them:
  `DESIGN_NAMES_RESOLVE` and `DECLARED_ARTIFACT_FULLY_STATED` do. 16 are design invariants, 4
  construction.
- **Two constitutions superseded,** `lifecycle::CONSTITUTION_CHANGE_MGMT_V1` and
  `CONSTITUTION_CONSTRUCTION_V1`, naming the invariants (§6a).
- **`x-realises`** on every annotation and procedure, and on the seven constraints that realise an
  invariant: an invariant's identity, or for a procedure the protocol has not declared, its statement
  in `DESIGN_LANGUAGE.md`.
- **`DESIGN_LANGUAGE.md`,** the language standard: the document form, the schema, the derived and
  declared rules, the four annotation constructs, every procedure by its invariant or statement,
  findings and evaluation semantics.

No rule changes: sealed rule sets, declarations and the comparison are unchanged.

### M3.4c — identity, locators, dispatch

- **Rule identity.** Every sealed rule carries `identity`: its schema's `$id` and a JSON Pointer to
  where it is declared (DESIGN_LANGUAGE §2.1). Unique within a rule set, and refused at expansion
  when it is not.
- **Findings.** A finding is `{code, rule, locator, detail, intent}`. `code` is the oracle's `rule`;
  `rule` is now the identity. `locator` is `{register, row, field}` and replaces `where`. The
  comparison reads the locator back as the oracle's `where`: the register, then `row <n>` or the
  row's key. The field is not compared, because the oracle never stated it.
- **The dispatch.** `transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0` states each phase's
  schema, workflow, template, gate, key rule and rung. It replaces the catalogue's table and
  `emit.SEALED_IN`. The P7 parameter `phase_workflows` reads it through `x-dispatch`.

No rule changes meaning: sealed rule sets differ only by `identity`, and declarations and the
comparison are unchanged.

### M3.4d — closure and the evaluator's shape

- **Closure.** `meta.closure` and `scripts/testbed/closure_test.py`, a regression step: every
  `x-realises` resolves to an invariant `lifecycle::CONSTITUTION_CHANGE_MGMT_V1` names or a
  statement of `DESIGN_LANGUAGE.md`; every design invariant is realised; every template names its
  schema's registers and columns. A derived rule has no entry to state what it realises, so
  `expand.DERIVED_REALISES` states it for the citation and business-language checks.
  `ROW_PROVENANCE_CITED` is realised only there.
- **Divergence M3.4d-1.** The design's "every `enforced_by` names a workflow that exists" is
  dropped: §6a made `enforced_by` prose.
- **The evaluator.** `checks.py` is the package `design/evaluate/`: `document`, `registry`,
  `common`, `keywords` (18 kinds), `constructs` (13), and `procedures/`, one module per procedure
  (26). The code moved unchanged. `tc phase meta` reads parameter contracts across the package.
- **One rule type.** `Rule.from_mapping` reads a sealed rule; `DeclaredRule` is gone.
- **No phase modules.** The nine `p*/rules.py` loaders are gone. `rule_sets.RULE_SETS` reads each
  phase from the schema the dispatch names. A workflow's sources no longer list a loader.

No rule changes: declarations and the comparison are unchanged.

## 9. The in-flight dossiers

- `binding_literals` and `quoted_literals` stay as delivered. They are part of the oracle.
- `register_format` (P0–P7) and `version_retirement` (P0–P6) are parked and never delivered. They
  are kept as evidence. Their findings are inputs to the design: the readers' shape, the test copies,
  deletion by record, and node keys as places.
- `rule_effectivity` keeps its P0, as the statement of change 4 of the scope.

## 10. Sequence

1. **Checkpoint.** Commit the workspace as it stands, tag the oracle, and record the exception.
2. **Design.** One design document for the whole scope. A human gates it, and it fills §8.
3. **The platform fix.** `supersedes` exempt from surface closure (§6), through the lifecycle,
   judged by the oracle.
4. **Build.** On the branch `rebuild/transformation`, cut from the tag.
5. **Acceptance.** §5, item by item.
6. **Swap.** Squash the branch into `dev/18` as one commit. The oracle's dead artifacts are deleted
   and recorded in the same change. The human runs every git command.
7. **Sweep.** Every other domain that holds stood-down artifacts deletes them, one change per
   domain, through the lifecycle, judged by the rebuilt module. There are 22 today: blockchain 10,
   execution_topology 3, capability_transforms, workload, book_library_mgmt and ai_governance 2
   each, and trace 1. Each change renames the node keys that spell a deleted version and records
   every deletion in the ledger.
8. **Single instance, workspace-wide.** When the last sweep lands, the single-instance check runs
   on every domain and joins the regression.

## 10a. Branches

The human runs every git command.

**Repositories.**
- `transformation` carries the rebuild.
- `.github` carries the expectations, the ledger and the runbook that change with it.
- `software_governance` carries the lifecycle invariants and constitution successors (§6a) on a
  rebuild branch.
- `software_governance` and `protocol_compiler` take the platform fix (§6) on `dev/18`, through the
  lifecycle.

| Repository | Ref | Purpose |
|---|---|---|
| transformation | tag `oracle/transformation` on `dev/18` | The frozen oracle. It never moves. |
| transformation | `rebuild/transformation`, cut from the tag | All rebuild work. |
| .github | `rebuild/transformation`, cut from `dev/18` | Expectations and ledger entries that match the rebuild. |
| software_governance | `rebuild/transformation`, cut from `dev/18` | The lifecycle invariants and the two constitution successors (§6a). |
| transformation | `dev/18` | Frozen (§3). A fix the workspace needs lands here and is cherry-picked onto the rebuild branch. |
| every other repository | `dev/18` | Unchanged. The platform fix lands here before the swap. |

**The oracle runs beside the rebuild.** The venv holds one editable `transformation`, and that is
the rebuild.
- The oracle is a worktree of the tag: `git worktree add ~/pgc-oracle/transformation oracle/transformation`.
- The acceptance harness runs it as a subprocess. Its import root is provisioned through the
  environment, never through `sys.path`.

**Switching.**
- To work on the rebuild, check out `rebuild/transformation` in `transformation`, `.github` and
  `software_governance`.
- To work on anything else, return all three to `dev/18`. Run the regression there to confirm the oracle
  composition still passes.

**Backup.**
- `dev/18` is pushed to the remote.
- The oracle tag and the rebuild branches are pushed as well, so the oracle and the work in progress
  survive the loss of this machine.

**The swap.**
1. Squash `rebuild/transformation` into `dev/18` in `transformation`, as one commit.
2. Squash it into `dev/18` in `.github`, as one commit. The deferred ledger entries
   (`.github/process/notes/rebuild-retirements.yaml`) join `retired_identities.yaml` in this commit.
3. Squash it into `dev/18` in `software_governance`, as one commit.
4. Rename the repository `transformation` to `transformation_compilers`, on GitHub and in the
   workspace, with the path changes of §6a.
5. Run `regression.sh --all` on `dev/18`.
6. After confirmation, rename the three branches `archive/rebuild-transformation`. The oracle tag
   stays.

**Rollback.** Before step 6, `dev/18` in `transformation` returns to the tag, `software_governance`
and `.github` return to their commits before the swap, and the repository rename is undone. That reset is
destructive, so a human decides it.

After the swap, `dev/18` collects for v6 as before.

## 11. Open decisions

- **Branch and tag names.** Proposed: `rebuild/transformation` and `oracle/transformation`.
- **Where the design lives.** Proposed: `transformation/doc/REBUILD_DESIGN.md`, on the branch.
- **Converted corpus location.** Proposed: beside the catalog's existing fixtures, as `register_format`
  found (§9.10 R3).
