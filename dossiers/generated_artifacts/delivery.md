# Delivery — generated_artifacts

**Delivered by hand, once**, under `GAP-5` and the boundary rule `THE_LAST_EXCEPTION`. `halt.md`
records why the pipeline could not carry this change to P7: the design had to say *"this artifact is
reached by invoking that generator"*, and P7 had no register in which to say it. That register is
what this delivery adds, so the change could only be delivered outside the path it creates.

**The exemption is now spent.** No later change to this subdomain may claim it, because the path
exists.

---

## What was delivered

### GAP-2 — a design may name the generator an artifact is reached by

P7 gained a sixteenth register, `generation_provenance`, and the five rules that govern it.

| | |
|---|---|
| Register | `Artifact · Generator · Generator Sources · Source Finding`, optional |
| Rules | `GENERATED_ARTIFACT_UNDECLARED`, `ARTIFACT_HAS_TWO_GENERATORS`, `GENERATOR_UNNAMED`, `GENERATOR_UNREACHABLE`, `GENERATOR_SOURCES_UNNAMED` |
| Mechanism | one new check kind, `COLUMN_VALUES_UNIQUE` — 43 kinds became 44 |
| Rule set | 762 rules became 772: five declared, five derived from the register's own shape |

`ARTIFACT_HAS_TWO_GENERATORS` is `ONE_ARTIFACT_ONE_PRODUCER` made checkable, and it needed a
mechanism nothing else in the pipeline had: every other register check asks whether a row says the
right thing, and this asks whether the register says one thing about a subject at all.

`GENERATOR_UNREACHABLE` holds a generator to `module:callable`. A generator only a person at a
terminal can run is one construction cannot invoke, and `GAP-3` would be undeliverable against it.

### GAP-1 — an artifact states that it is generated, and by what

Each of the nine phase workflows now carries a `## Generated Artifact` section, emitted by the
generator alongside the sealed rule set. It names the generator, names the sources read with it, and
states that the artifact is a copy which is never corrected directly.

Provenance is stated *by the artifact* rather than held in a list beside it —
`PROVENANCE_BELONGS_TO_THE_ARTIFACT` — because a second statement of one truth can disagree with the
thing it describes. It sits outside the `Machine` block, which is the only part of the document the
compiler reads, so a fact for the reader stays a fact for the reader.

### GAP-3 — construction reaches a generated artifact by invoking its generator

The generator moved from `scripts/emit_rule_sets.py` into `transformation/design/emit.py`, inside the
package, because construction has to be able to import and invoke it. The script remains as the
terminal's way in and now calls the same code.

`transformation/build/render.py` drops a generated artifact before rendering rather than after: a
renderer that produced the file and then discarded it would still have decided what the file says.
The artifact is still scheduled and still measured — what the design owes for it is the generator,
and that is the one fact measured against it.

`transformation/build/generators.py` holds the generators construction may invoke, and **the registry
is closed**, exactly as the check-kind registry is. Resolving an arbitrary dotted path at runtime
would let a design point construction at any callable in the interpreter; an artifact reached by
something nobody admitted is an artifact nobody governs.

### GAP-4 — the build refuses when an artifact and its generator disagree

`tc construction check` now asks every admitted generator whether its artifacts already agree, and
refuses when they do not. `tc construction emit` invokes each generator and refuses if anything still
disagrees afterwards — a generator that has run and left its artifacts stale has not produced them.
`tc phase emit --check` is the same question asked directly.

The check existed before this change and returned non-zero correctly. Nothing required it, and a
written obligation nobody must meet is indistinguishable from none.

---

## The design, in the language the delivery created

This is what P7 could not hold. It is recorded here because the change is judged on what it produced,
and the register it added is the only place its own artifacts can be described.

| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| transformation::WF_P0_SEED_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p0_change_seed_template_v0.md, transformation/design/p0_change_seed/rules.py | S4 gap_register GAP-1 |
| transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p1_change_request_template_v0.md, transformation/design/p1_change_request/rules.py | S4 gap_register GAP-1 |
| transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p2_domain_model_template_v0.md, transformation/design/p2_domain_model/rules.py | S4 gap_register GAP-1 |
| transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p3_analysis_loop_template_v0.md, transformation/design/p3_analysis_loop/rules.py | S4 gap_register GAP-1 |
| transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p4_business_model_template_v0.md, transformation/design/p4_business_model/rules.py | S4 gap_register GAP-1 |
| transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p5_business_intent_template_v0.md, transformation/design/p5_business_intent/rules.py | S4 gap_register GAP-1 |
| transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p6_governance_intent_template_v0.md, transformation/design/p6_governance_intent/rules.py | S4 gap_register GAP-1 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p7_design_intent_template_v0.md, transformation/design/p7_design_intent/rules.py | S4 gap_register GAP-2 |
| transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0 | transformation.design.emit:emit_rule_sets | templates/p8_authoring_mandate_template_v0.md, transformation/design/p8_authoring_mandate/rules.py | S4 gap_register GAP-1 |

One generator, nine artifacts. `ONE_ARTIFACT_ONE_PRODUCER` constrains the direction that matters —
an artifact has one producer — and says nothing about a producer serving several artifacts, which is
what a generator is for.

Each row names two sources and they are one generator: the template declares the registers and their
columns, the rule module declares what remains, and the emission reads both. Naming either alone
would permit regenerating from a stale pairing — `A_GENERATOR_IS_ITS_SOURCES_TOGETHER`.

---

## Files this delivery touched

| File | |
|---|---|
| `templates/p7_design_intent_template_v0.md` | the `generation_provenance` register |
| `transformation/design/p7_design_intent/rules.py` | the five rules that govern it |
| `transformation/design/checks.py` | `COLUMN_VALUES_UNIQUE` |
| `transformation/design/emit.py` | **new** — the generator, importable |
| `scripts/emit_rule_sets.py` | reduced to the terminal's way in |
| `transformation/build/generators.py` | **new** — the closed registry of admitted generators |
| `transformation/build/render.py` | a generated artifact is reached, not rendered |
| `transformation/cli.py` | `tc phase emit`, and the agreement gate on `construction check` / `construction emit` |
| the nine `registry/design/workflows/WF_P*_ADMISSIBILITY_V0.md` | **regenerated, never edited** |

The nine were reached by invoking the generator. That is the whole point of the change, and it is
also how the change was delivered: the one part of this delivery that was *not* by hand.

---

## What follows

`register_coverage` becomes deliverable *through* the pipeline rather than beside it — the first
change in this subdomain's history that will be.

`generation_provenance` is optional, and correctly so: most changes touch no generated artifact and
a required register would make them state that they do not. The obligation is on the artifact, not
on every design.
