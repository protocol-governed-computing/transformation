# What remains before `transformation/` is done at this feature level

The feature level is: a **Design Compiler** that runs P0–P8 with declared priors, and a
**Construction Compiler** that turns an admissible design into domain artifacts, reproducing 93/93
artifacts across two domains with no field differences. That much is built and green. What follows is
what is unfinished *at that level* — not the next feature.

## The shape of the debt, in one number — closed

```
                      before        after
229 distinct rule ids
 ever observed to fire     63          222
                        27.5%        96.9%
corpus documents           40           83
```

**Seven rule identifiers in ten had never been seen to fail.** The repair was documents, not rules:
thirty negative corpus documents across P0–P8, each naming the rules it must fire, wired into the
same e2e harness that already drove every phase through the runtime. No rule was authored, no design
construct added.

```
P0 13/13   P3 21/21   P6 21/22   P8 19/19
P1 16/16   P4 18/18   P7 74/80
P2 16/16   P5 24/24
```

**What the pass found, which is the point of it.** Two rules that could not fire at all, one that is
silent on every citation a real document carries, one that skips most of its own register, five with
no subject anywhere in the corpus, nine registers whose missing column was undetectable, and one
genuine defect in an existing fixture that no rule had ever reported. Every one of those was
invisible while the rules were merely *declared*.

### The seven that remain, and why each is not a document

```
UNDECLARED_REACH_READ                       P7   needs the dossier specified below
BORROWED_CAPABILITY_NOT_DECLARED_CROSSING   P6   needs the same dossier

NEW_CODE_ALREADY_EXISTS                     P7   reachable; the added artifact's cascade drowns
SATISFIED_DEPENDENCY_NOT_INVENTORIED        P7     the fixture — see the readability note below
TRANSFORM_WITHOUT_IMPLEMENTATION            P7
VOCABULARY_WITHOUT_VALUES                   P7
WORKFLOW_WITHOUT_TOPOLOGY                   P7
```

**Cross-subdomain reach looked like five rules needing a dossier and was four rules needing the right
identifier.** `declared_reach.Consults` names a **runtime binding**, not a store;
`declared_reach.Act` names a **workflow**, not a contract; and `cc_composition.Store` names a store
by its **bare name**, not its key. With `ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0` as the reach
and `LICENSE_FACTS` as the store, `DECLARED_REACH_UNUSED`, `CROSS_SUBDOMAIN_WRITE` and
`NODE_INPUT_UNBOUND` all fire from one corpus document against cr_01's own priors.

## The dossier two rules still need

`UNDECLARED_REACH_READ` and `BORROWED_CAPABILITY_NOT_DECLARED_CROSSING` cannot be reached by cutting
a document from any existing fixture, and the reason is worth stating precisely rather than as "no
subject exists".

**Why `UNDECLARED_REACH_READ` skips almost everything.** It compares the stores an act reads against
the stores its *own* binding covers, and it leaves alone any act whose binding the composition does
not publish — deliberately: *"what it owns is undecided, so what it reaches cannot be told apart from
it."* Every change that **authors** its own runtime binding is therefore invisible to it. cr_01
authors `RB_CATALOG_BINDINGS_V0`, so under cr_01's pin the rule has nothing to judge. cr_03 extends a
published binding and would qualify — but its `cc_composition` is `NONE IDENTIFIED`, so a row added
to give the act a read trips `COMPOSITION_CC_UNDECLARED` before the reach rule is reached.

**Why `BORROWED_CAPABILITY_NOT_DECLARED_CROSSING` has no subject.** It reconciles P6's
`cross_subdomain_deps` against P5's `cross_subdomain_refs`, and **all eight P5 documents in the
workspace declare that register empty or `NONE IDENTIFIED`** — three fixture CRs and five dossiers.
The register has never carried a row.

**What the dossier has to be.** One change request, against a domain that already exists in its
pinned baseline:

```
extends an existing subdomain          so its RB is published and _own_binding resolves
P5  cross_subdomain_refs               names one borrowed CC from another subdomain
P6  cross_subdomain_deps               that CC, Status SATISFIED, Existing Artifact named
P7  new_artifacts / existing_inventory declares the composed CC, so the composition rules pass
P7  cc_composition                     that CC runs a step reading the other subdomain's store,
                                       named by its bare store name
P7  declared_reach                     left empty — which is the defect the probe reports
```

The admissible form of that dossier declares the reach; the corpus document cut from it omits the
`declared_reach` row. Both rules then fire, and a third register — `declared_reach` — stops being
carried by nothing anywhere in the workspace.

**It is worth authoring for its own sake, not only for two rules.** `declared_reach` was designed,
delivered and never once exercised by a document. A register that no dossier fills is a register
whose rules are believed rather than observed, which is the condition this whole pass exists to end.

**A correct check can make a fixture useless as evidence.** Dropping a vocabulary-bearing column at
P1 fired `CELL_NOT_IN_VOCABULARY` thirty-nine times; dropping `field_declarations` at P8 fired
`SCHEDULED_ARTIFACT_UNPLACED` forty-two. Both checks were right and both fixtures were unreadable.
The remaining five above are the same hazard, unrecut.

**Where a rule lives, so nobody has to ask.** Rules are declared in Python, generated into the
`WF_P*_ADMISSIBILITY_V0` workflow artifacts, compiled, and **sealed into the composition** — all 24
P5 rule ids are in `snapshot/canonical/transformation/workflows/`. `tc phase check --snapshot` reads
the sealed set rather than the working tree, because a dossier's pin already names the rule set. The
rules are live; the corpus is the evidence that they fire.

## Are the rules domain-neutral? The rules yes, the evidence no.

Measured rather than asserted, because "the rules read the template, not the content" is exactly the
kind of claim that is true by inspection and false in one place nobody checked.

**By inspection:** zero domain nouns across all nine compiled rule sets. In `checks.py`, eight
mentions — seven in docstrings, one an example identity inside a help string. Nothing branches on a
domain.

**By experiment:** the three structural corpus documents were rewritten from a library catalog into
freight logistics — consignments, containers, seal numbers, waybills, a `manifest` subdomain — and
re-judged.

```
P3   identical.  8 rules, same rules, same order
P5   superset.   the same 5, plus TOUCHED_SUBDOMAIN_AUTHORS_NOTHING
                                 + TOUCHED_SUBDOMAIN_WITHOUT_PURPOSE
P6   superset.   the same 5, plus IN_SCOPE_CAPABILITY_UNPLACED ×12
                                 + TOUCHED_SUBDOMAIN_UNOWNED
```

**Every extra rule is a prior-coupled rule doing its job.** The rewrite renamed the subdomain while
its priors still declare `catalog`, so the document genuinely stopped answering for the change
request it belongs to. That is the finding those rules exist to report. The rules that read only the
document fired identically on a business domain that shares no noun with the original.

So the neutrality boundary sits exactly where it should: **document-local rules are domain-neutral in
fact; prior-coupled rules are domain-*coupled* by design**, and the experiment separates them
cleanly.

**What is not neutral is the corpus.**

```
phase  change requests exercised
P0     blockchain_chain_v0 · cr_01_catalog · new_subdomain
P1     cr_01_catalog · new_subdomain
P2     cr_01_catalog · new_subdomain
P3     cr_01_catalog
P4     cr_01_catalog
P5     cr_01_catalog
P6     cr_01_catalog
P7     cr_01_catalog · cr_03_catalog
P8     cr_01_catalog
```

Five of nine phases are demonstrated by one subdomain of one domain, and every rule demonstrated in
this pass was demonstrated against `book_library_mgmt/catalog`. Only P0 reaches a second business
domain. The freight experiment is evidence that this matters less than the table suggests — but it
was an experiment, not a corpus document, and it is not in the suite. **A second-domain corpus
document at P3–P6 is the cheap way to make the argument permanent rather than remembered.**

## Five kinds of unfinished, in the order they should be taken

### 1. Rulings owed on work already built

Decisions, not code. Each blocks nothing and compounds if left.

- **Amendment-set completeness.** A design named one artifact of the seven it amended. The count is a
  moment, not a property, and nothing checks that the set a design declares is the set it changes.
- **The rule-count in a mandate is a guess.** Projections come out low (~157 projected against 179
  actual) because a register costs five derived rules whether required or not, and nothing computes
  that at authoring time.
- **A delivered dossier carries a stale opening line.** Recorded rather than edited, on the standing
  rule that a delivered dossier is not amended — but the rule wants stating once, not re-deciding per
  dossier.

### 2. Coverage, by corpus — **done**, except for the ten above

Thirty documents, P0–P8, 27.5% → 95.6%. What is left is not more of the same: five rules whose
subject does not exist anywhere in the corpus, and five whose fixture would drown in cascade unless
recut. The first five want a dossier that borrows a capability across subdomains and declares its
reach — one dossier, five rules, and the only remaining structural hole in the evidence.

### 3. The last generator without an agreement check — **the claim was wrong**

`tc construction emit` was carried for several sessions as the one generator that does not re-derive
its output and refuse a mismatch. Measured: **everything it writes is already compared.**
`construction_acceptance.py` renders the accumulated design and compares it against the registry
semantically, Machine-block scoped, 93/93 across two domains — and it compares the generated build
manifest too, explicitly, so that a `build_manifest` which stopped deriving what the composition
holds would be caught. A second `--check` on `emit` would have re-asked a question already answered.

**What was actually unchecked is one level up: `DOMAINS` is a hand-kept pair.**

That is the same shape `SEQUENCED` was introduced to remove. The harness's own comment records the
cost: the *sequence* used to be a literal list, a missed entry compared a built artifact against a
design that was no longer its design of record, and cr_03 cost twelve differences that read as
construction defects before anyone thought to look at the list. The *domain* list stayed literal.

Two ways it can go stale, and neither reports anything today:

- a third domain whose dossiers determine artifacts is reproduced by nothing;
- `sequence()` recognises only `cr_NN_`, so a **base-code domain's** dossiers — deliberately
  unnumbered as `dossiers/<subject>/` per `CLAUDE.md` — cannot enter the corpus at all, whatever
  they declare.

**The check asks the question the list can go stale on, of the workspace rather than of a second
list.** Every dossier root whose P7 schedules an artifact must be one `DOMAINS` reads; the catalog's
fixture substitution is named so a deliberate override is not read as an omission. Both probes were
authored, observed to fail, and reverted:

```
drop blockchain from DOMAINS                      → UNCOVERED business_domains/blockchain/cr_dossiers
give transformation/dossiers/declared_reach one
  new artifact — the unnumbered, base-code form   → UNCOVERED transformation/dossiers
```

The second is the one worth having. It is the hazard that could not have been found by reading the
list, because the form it takes is a directory `sequence()` was never able to see.

### 4. Two forks in flight

- **`register_coverage`** — **closed unbuilt by ruling.** Its three named instances were checked
  against the design language as it stands: two were closed by work done since and neither closure
  had been recorded against the fork, which is why it read as parked rather than two-thirds
  delivered. The third is still true and is a different question — whether an artifact every field of
  which is compiler configuration belongs in the design language at all. `closure.md`, and the
  evidence in `doc/REGISTER_COVERAGE_VERIFICATION.md`.
- **`rule_effectivity`** — P0–P6 admissible, P7 authorable. Applicability: which rules are in force
  for which change kinds. Compounds with everything above, blocks nothing.

### 5. One unbuilt refusal form

Prohibition by absence — the third form of declared refusal, the two others being built. It needs a
dossier whose material supplies an identity to prohibit; the obvious candidate does not.

## On just-in-time design, and separation of concerns

The concern is fair and the answer is not uniform across it.

**Where JIT is not what happened.** The governance-authority work of this cycle touched
`software_governance`, `protocol_compiler` docs and one new file in `standards/process`. It changed no
transformation rule and added no design-language construct. Those are different repos and different
concerns, and the boundary held.

**Where the concern is real.** Rules enter the design language *per dossier* — a CR lands, and the
rules that would have caught its defect are authored with it. That is a good instinct and a bad
cadence: the rule count has grown with the change requests while the corpus has grown with almost
nothing. 820 rules against 40 documents, 20 of them for one phase, is the measurable form of
"spreading rules without coordination." The rules themselves are coordinated — `meta_test` proves
every declared rule resolves to a declared mechanism, and no rule is orphaned. What is uncoordinated
is **evidence**, not structure.

**What a coordinated pass looks like.** Stop authoring rules at this feature level. Spend the pass on
item 2, then take the rulings in item 1 with real documents underneath them. A rule with a corpus
document that fires it is worth more than three rules with none, and the ratio here is currently
seven-to-three the wrong way.

## What "done at this feature level" would mean

- Rule demonstration above a stated floor, with the phases named where it is not met and why.
- The four rulings in item 1 taken, each recorded where the rule lives rather than in a handoff.
- `tc construction emit` agreeing with itself.
- Both in-flight forks either delivered or explicitly closed unbuilt.

None of that is new capability. All of it is closing what is already open.
