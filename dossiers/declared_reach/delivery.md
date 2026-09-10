# Delivery — declared_reach

**Authorized by:** Gate 1 and Gate 2, both renewed, against composition `2e7815febb7e…`
**Delivered:** a design can state the bindings its act consults, the rules refuse a design that
reads what it never declared or declares what it never reads, and construction emits the declaration
into the act
**First adoption:** `cr_04_wallet`, whose act declares the binding it consults and refuses a wallet to
a person the business has not accepted

---

## What was authored

**`si.store.list` names the bindings it counts.** The surface computed `binding_count` as a sum over
each declaration's bindings and then discarded the bindings themselves. It now publishes them
sorted beside the count — the count's own input, projected rather than derived, and `si.store.show`
is untouched. `TI_SI_STORE_LIST_V0`'s catalog summary was amended to say so, because a summary that
still described the old answer would be the copy nobody regenerates.

**The emission produces the observing step, not only the map that names it.** The judging contract's
`observed` map has been generated since the map and `OBSERVATIONS` drifted; the *step* the map points
at was still hand-written, and the emission could only report that one was missing — which it did,
correctly, and then left somebody to write it. Now `step_name` derives the step from the operation
and `splice_observing_steps` places any missing one before `evaluate_rules`, the step that reads
them. Adding `si.store.list` to the P7 module's `OBSERVATIONS` was the whole of the change: the
generator wrote `observe_store_list` and its map entry from that one line.

**The register.** `declared_reach` in the P7 template — `Act`, `Consults`, `Source Finding`.
Ownership stays in `rb_declarations` and is exactly one; reach is here and may be several. Two
registers rather than one with a column telling them apart, which is the business constraint stated
at P0 and the reason it is stated: a column would put them a typo apart with nothing between them
but the rule that reads it. The register names a binding and never the records behind it.

**The two rules, delivered together because neither is a rule alone.**

- `DECLARED_REACH_UNUSED` — a declared reach that no step the act runs reads. Alone, refusing this
  permits a read nobody declared.
- `UNDECLARED_REACH_READ` — a store an act addresses that neither its own binding nor any declared
  reach covers. Alone, refusing this permits a reach held in reserve.

Both derive the records from the composition: `si.store.list` inverted to `binding → stores`, and
the act's reads taken from the contract surface for a contract that exists and from the design's own
composition for one it authors. A binding the composition does not publish is not judged, and the
reason is stated where the skip is — the reach that matters consults another subdomain's existing
binding, and refusing a binding this design authors would refuse a design for being new.

**Construction emits the reach.** `consults` is written onto the act that declared it, omitted where
none is declared — the schema admits absence, and a present-but-empty list is a different claim.
Without this half the register is decoration and the act is finished by hand, which works, passes
every check, and is a reach no reviewer saw.

P7 is 145 → **152**.

---

## What it took, and what it found

**The design language cannot state a dotted literal, and finding that out changed the design.** The
first P7 draft did what an EXTEND asks for and redeclared `CC_JUDGE_AGAINST_SNAPSHOT_V0` whole —
seven composition steps, fifteen bindings, six interface fields. Twenty-three findings came back, and
one class of them was not an authoring mistake: `BINDING_SOURCE_WELL_FORMED` admits `inputs.<field>`,
`payload.<field>`, `results.<step>.<field>`, a bracketed literal, or a bare identifier — no dots. An
operation identity is `si.store.list`. That contract was hand-authored and had never been through the
pipeline, so nothing had ever needed to write one.

The resolution was not to work around it. The contract's observing step is the last hand-kept copy of
a declaration that already lives in a phase's rule module, so the emission produces it, both amended
artifacts fall under one generator, and construction writes neither. The gap does not arise rather
than being avoided.

**The inspection surface was declared sufficient and was not, and the correction went to where the
claim was made.** P4's dependency graph read `design -> inspection … SATISFIED`, citing S3's third
analysis finding: *nothing new needs publishing*. The facts were all published; the *shape* was not.
`si.store.list` answers every store at once and names no bindings; `si.store.show` names them one
store per call, and a capability contract is a fixed pipeline with no iteration — which is the same
sentence `capability_surface.py` opens with, one level down.

Correcting only the dependency graph would have left the false finding standing at S3 for the rest of
the dossier to cite. So Q3 and authoring decision 7 were rewritten, GAP-7 was raised against
`inspection`, and every phase from P3 forward was re-judged. Both gates were withdrawn and re-closed
as renewed, each recording what was false. **This was not an approved deviation**: a deviation would
have delivered the right code under a design that still said the surface was sufficient.

**Section 17, not 4b.** The register was first placed after `rb_declarations`, where it belongs by
subject. The document reader parses a section number as an integer and `4b` is a hard failure.
Appending it avoided renumbering sixteen sections across nine documents; where it belongs by subject
and where it can go are different questions, and the second one won.

**The rules found the defect they were written for, on the first real design they judged.** Neither
had a subject in the corpus — every design in the composition declares no reach — so each was proved
by probe. But `cr_04_wallet`'s P7, judged against the new rule set with nothing tampered:

```
WF_CREATE_WALLET_V0: reads blockchain::ACTORS, which RB_WALLET_BINDINGS_V0 does not cover
                     and no declared reach names
WF_CREATE_WALLET_V0: reads blockchain::CONTACT_ADDRESS_REGISTRY, same
```

That is the wallet's undeclared reach, refused at design time instead of surfacing when the act
runs. The probe covered the rest: declaring the reach the act actually makes silences both rules;
declaring one to a binding the act never reads fires `DECLARED_REACH_UNUSED` and names the records
that binding answers for.

**The chain was proved by rendering, not by reading.**

```
fqdn             blockchain::WF_CREATE_WALLET_V0
runtime_binding  blockchain::RB_WALLET_BINDINGS_V0
consults         ['blockchain::RB_IDENTITY_BINDINGS_V0']
```

---

## What this change did not do

It states no reach for any act. Which acts reach which records is each domain's business, deferred at
P0 and unchanged here.

It does not refuse a design whose act *writes* through a reach. The platform refuses that when the
act runs; whether the design layer should refuse it earlier is deferred and remains so.

It found the wallet's undeclared reach and the wallet found, in return, that a rule can be stated at
P0 and never become a branch. Both are corrected in `cr_04_wallet`.

---

## The path this change took

It is the first change to a phase's rule set delivered through the pipeline rather than by hand,
using the capability `generated_artifacts` delivered and nothing had used since. The path held: the
design named the generator and its sources, the mandate scheduled no build step because the change
authors no artifact, and what it froze was the amendment set and the way it is reached.

What the path cost is the dotted literal and the section number — both found by driving a real change
through it, neither visible from reading it.
