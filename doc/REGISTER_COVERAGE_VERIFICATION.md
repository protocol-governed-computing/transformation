# `register_coverage` — the four instances, checked against today's design language

The fork asks one question: **can a design state, for an artifact it amends, every fact that artifact
carries?** It rests on four observed instances of one pattern — *a fact the authoring path never had
to state because authoring supplies it, and the amending path must state and cannot.*

Nothing is fixed here. Each instance is checked and classified, and the ruling follows from the
classification rather than preceding it.

## The document names three, not four

`p0_business_problem_statement.md` reads *"Four instances, all found by carrying one real change to
the point of construction:"* and then names three. There is no fourth paragraph, headed or unheaded.

That is a finding about the P0 rather than about the design language, and it is the reason this pass
exists: **a count is a moment and the things counted are the property.** Either an instance was
dropped in authoring or the count was never right, and neither can be established now. What can be
established is the state of the three that are named.

## 1. A build configuration cannot be amended at all

> *Adding a second subdomain to a domain's build declaration loses fifty-one facts … No register in
> the design holds any of them, at any shape.*

**Still true as stated, and intentionally so. Needs an architectural ruling, not a register.**

No register holds a build configuration's fields — measured, the built manifest carries **56 leaf
facts** across twelve top-level keys, and `p6.storage_governance`, `p7.structure_stores` and
`p8.build_order` between them hold none of them. The P0 is right about that.

What has changed is that the facts are no longer *lost*. `render.build_manifest` derives the whole
artifact, and `construction_acceptance.py` compares the generated manifest against the built one on
every run — **0 differences**. So the manifest is reproducible from the design; it is simply
reproduced by derivation rather than stated in a register. `cli.py` says so in as many words: *"It is
not an artifact any phase designs — every field of it is compiler configuration."*

**And subdomain plurality specifically is expressible.** `build_manifest` derives `subdomains` from
the distinct `Subdomain Field` values in `p8.field_declarations`, so a change adding a second
subdomain states it exactly the way it states the first. The P0's own example is the part that no
longer holds.

What remains is the general claim: fifty-odd facts of compiler configuration sit outside the design
language, reachable only through a generator. **Whether that is a gap is an architectural question,
not a business one** — the same question `generated_artifacts` settled for artifacts whose source of
truth is a generator, asked now of one that is configuration rather than behaviour. It has never been
forced, because no change has yet amended a build configuration in a way derivation could not cover.

## 2. An amended artifact cannot state its subdomain

**No longer true.**

`p8.field_declarations` carries `Code | Subdomain Field`, and the renderer reads an artifact's
subdomain from there rather than from `new_artifacts`:

```
render.py:304   subdomain = {bare(cell(r, "Code")): cell(r, "Subdomain Field")
                             for r in rows(p8, "field_declarations")}
```

It is stated, and its absence is refused: `AMENDED_ARTIFACT_UNPLACED` requires every artifact a P7
inventories as `EXTEND` to appear in `field_declarations`. That rule was demonstrated for the first
time this session — the probe had to be cut from cr_02, because cr_01's P7 declares no EXTEND row at
all — and it fires by name.

The same commit history shows the fix being learned rather than designed: `render.py:372` records
that reading `new_artifacts` alone *"was correct for exactly as long as every change request authored
its own actor,"* and that the first extension change resolved to no actor context while every design
rule passed.

## 3. A vocabulary that extends nothing cannot say so

**No longer true.**

`Extends` accepts a declared-emptiness sentinel, and the renderer distinguishes it from an unfilled
cell:

```
render.py:657   if extends in ("—", "-", "NONE"):
                    extends = ""
                    declared_empty.append("extends")
```

The comment above it states the P0's problem in the P0's own terms — *"a vocabulary nobody finished
and one deliberately rooted look identical, and only one of them is designed."* `VOCABULARY_WITHOUT_EXTENDS`
still requires the cell to be non-empty, so silence is refused and a declaration is admitted. That is
the distinction the instance asked for.

## Ruling

**The fork does not survive as written, and should not be closed silently either.**

```
1  build configuration        still true · intentionally implicit → wants an architectural ruling
2  amended artifact subdomain no longer true                      → closed
3  vocabulary extends nothing no longer true                      → closed
4  —                          the document names three            → cannot be established
```

Two of the three named instances were closed by work done since, and neither closure was recorded
against this fork — which is why it read as parked rather than as two-thirds delivered.

What is left is **not the change `register_coverage` describes.** Its P0 asks for "a register per
fact" so that an amendment states the artifact whole; that premise was answered for artifacts and is
now answered for the two instances above. The residue is one question about **compiler configuration**
— whether an artifact every field of which is configuration belongs in the design language at all, or
belongs to the generator that derives it, as `generated_artifacts` ruled for behaviour.

That question deserves its own statement, against evidence that does not yet exist: no change has
amended a build configuration. **The honest disposition is to close `register_coverage` on the record
above and raise the configuration question when a change forces it** — not to keep a fork open whose
stated subject is two-thirds resolved and whose remaining third is a different question.
