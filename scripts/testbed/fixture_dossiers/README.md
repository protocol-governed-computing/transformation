# Fixture dossiers — not evidence

These are **test fixtures that happen to be shaped like dossiers**. They are maintained against the
current rule set, deliberately and continuously, and they prove nothing about any change anyone ever
approved.

The dossiers they were cut from live where they belong — `business_domains/book_library_mgmt/
cr_dossiers/` — and are **never amended**. A closed change request is evidence: it records what a
human gated, under the rules in force when they gated it. Editing one to satisfy a rule written
afterwards changes the evidence of an approval that already happened, and its green verdict then
certifies nothing, because nobody closed a gate on the edited text.

That rule and the testbed's needs pull in opposite directions. The testbed needs a complete P0–P8
chain that is admissible *today*, because that is what proves the rule sets, the projection, the
runtime wiring and the construction path still work. The approved dossier needs to stay exactly as
approved. One document cannot do both jobs, and for a while one was being asked to: `cr_01_catalog`
was amended twice to keep the suite green, which is the forbidden act performed for a good reason.

So the two roles are separated. The copy here carries the amendments; the original carries the
approval.

## What consumes these

| script | what it takes |
|---|---|
| `build_payloads.py` | every phase document, as runtime payloads |
| `build_fixtures.py` | `cr_01_catalog`, as the base its negative corpus is derived from |
| `differential.py` | `cr_01_catalog`, driving the transforms directly |
| `projection_test.py` | both P0s, asserting each P1 is what the projection emits |
| `construction_acceptance.py` | both designs, rendered and compared against the built registry |

`construction_acceptance.py` is the one that keeps these honest. It renders from the fixture design
and compares the result against `book_library_mgmt/registry` — the artifacts the *original* dossier
produced and the composition actually holds. An amendment here that changed what the design means
would show up there as a field difference, so the copy cannot drift into describing a different
system.

## Maintaining them

When a rule or a template changes and these go inadmissible, **fix them**. That is what they are for.
Do not touch `business_domains` to make a test pass.

The reverse obligation also holds: an amendment that makes the fixture pass while changing what it
designs is a defect. Run `construction_acceptance.py` after any edit — no field differences is the
bar.

### Where the copy and the original now differ, and why

`cr_01_catalog` inventories `capability_side_effects::CS_MUTABLE_JSON_V0` as **REVIEW** here and as
**EXTEND** in the approved original. The capability did gain an operation for that change — but it is
a platform artifact, and `AMENDED_ARTIFACT_NOT_AUTHORABLE` now refuses a design that claims to amend
one whose family it cannot author. The governance surface is authored, not constructed, so the
extension was a platform act and belongs to a platform dossier rather than to a business change
request that consumed it.

The original stays as approved. It records a change that crossed an authority boundary before that
boundary was stated, which is worth keeping visible rather than editing away.

## When this goes away

`rule_effectivity` is the change that gives the tool a way to say "approved under rule set N". Once a
document can be judged against the rules in force when it was gated, the original dossiers can be
judged directly and this split stops earning its keep. Until then it is the honest arrangement:
neither a fixture pretending to be evidence, nor evidence being edited to serve as a fixture.
