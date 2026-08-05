# End-to-End Runbook

A clean-slate build of the composition, then one check per domain.

The transformation phases are checked by a single script rather than one runbook line per phase.
The phase count grows; the runbook does not.

---

## Build

```bash
cd ~/protocol-governed-computing

~/protocol-governed-computing/protocol_compiler/compile.sh

~/protocol-governed-computing/protocol_compiler/compile_domain.sh ~/protocol-governed-computing/conformance_workloads/workloads/collatz

~/protocol-governed-computing/protocol_compiler/compile_domain.sh ~/protocol-governed-computing/transformation

~/protocol-governed-computing/protocol_compiler/compile_domain.sh ~/protocol-governed-computing/snapshot_inspector

~/protocol-governed-computing/protocol_compiler/compile_domain.sh ~/protocol-governed-computing/business_domains/ai_governance

~/protocol-governed-computing/protocol_compiler/compile_domain.sh ~/protocol-governed-computing/business_domains/book_library_mgmt

~/protocol-governed-computing/snapshot_assembler/assemble.sh
```

Every domain that declares source must be compiled — the assembler refuses otherwise rather than
silently producing a smaller composition. If a compile step is skipped it names the command to run.

`book_library_mgmt` was missing from this list until a clean-slate run tripped over it: the domain had
source and no compiled output, the assembler refused, and every runtime check afterwards failed on a
snapshot that had never been written. A build list that omits a domain is indistinguishable from a
domain that declares no source, which is why the assembler names the command rather than proceeding.

## Check

```bash
python ~/protocol-governed-computing/transformation/scripts/emit_rule_sets.py --check

python ~/protocol-governed-computing/transformation/scripts/testbed/e2e_phases_test.py

cd ~/protocol-governed-computing/transformation && python scripts/testbed/differential.py

~/protocol-governed-computing/protocol_runtime/run.sh run --wf workload::WF_COLLATZ_CONJECTURE_V0 --payload ~/protocol-governed-computing/conformance_workloads/workloads/collatz/test_payloads/01_happy_path.json --data-root ~/protocol-governed-computing/data/collatz

mkdir -p ~/protocol-governed-computing/data/ai_governance/ai_governance/ai_licensing

cp ~/protocol-governed-computing/business_domains/ai_governance/testbed/agent_governance/seed_data/license_facts.json ~/protocol-governed-computing/data/ai_governance/ai_governance/ai_licensing/

~/protocol-governed-computing/protocol_runtime/run.sh run --wf ai_governance::WF_GOVERN_AGENT_ACTION_V0 --payload ~/protocol-governed-computing/business_domains/ai_governance/testbed/agent_governance/test_payloads/01_valid_standard_action.json --data-root ~/protocol-governed-computing/data/ai_governance

~/protocol-governed-computing/protocol_runtime/run.sh run --wf ai_governance::WF_PROVISION_AI_LICENSING_V0 --payload ~/protocol-governed-computing/business_domains/ai_governance/testbed/ai_licensing/test_payloads/provision_ai_licensing_payload.json --data-root ~/protocol-governed-computing/data/ai_governance

python ~/protocol-governed-computing/business_domains/book_library_mgmt/testbed/catalog/execution_validation.py

python ~/protocol-governed-computing/transformation/scripts/testbed/construction_acceptance.py
```

Every path is absolute; the `cd` is convenience only.

## Expected

| Check | Result |
|---|---|
| `emit_rule_sets.py --check` | every phase `OK` — the sealed rule set matches the declared one |
| `e2e_phases_test.py` | `E2E PASSED` — every phase, both admissible and inadmissible, exit 0 |
| `differential.py` | `DIFFERENTIAL PASSED` — both paths agree on every corpus document |
| collatz | `SUCCESS`, `all_terminate: true` |
| govern agent action | `SUCCESS` |
| provision licensing | `SUCCESS` first run against a fresh `data/`; `ALREADY_EXISTS` on any re-run |
| `execution_validation.py` | `23/23 criteria hold` — the catalog's nine workflows against the CR's §15 |
| `construction_acceptance.py` | `42/43 artifacts reproduced (0 field difference(s))` |

Both transformation verdicts complete with `Status: SUCCESS`. An inadmissible document is a correct
judgement, not a failed execution — `VIOLATION` there would mean the phase itself is broken.

`differential.py` must be run from the `transformation` directory: it imports `design_baseline` from
`e2e_phases_test`, which sits beside it. `--check` on the emitter is the cheap half of what the
differential proves — it compares counts without booting a snapshot, so it catches a rule added and
never re-emitted in a second rather than a minute.

## The catalog subdomain

`book_library_mgmt/catalog` is constructed and runs. Its nine workflows are exercised by one script,
which is the **only check in this runbook that proves the catalog does anything**:

```bash
python ~/protocol-governed-computing/business_domains/book_library_mgmt/testbed/catalog/execution_validation.py
```

It dispatches real workflows through `protocol_runtime` against a fresh temp data root and asserts the
CR's §15 acceptance criteria — 23 of them — reading the stores it wrote rather than the status it was
handed. State accumulates deliberately across scenarios, so the order is part of the evidence and the
run is not idempotent; that is why it starts from an empty data root every time.

It takes an optional snapshot path, defaulting to `~/protocol-governed-computing/snapshot`.

**Why it exists, and why the other checks do not replace it.** Every document check passed —
P0–P8 ADMISSIBLE, `tc construction check` 100%, construction acceptance at 0 field differences,
conformance PASSED, `e2e_phases_test.py` green — against a composition whose stores held binding
expressions instead of records, because every cross-step source had been authored without its
`results.` root and the runtime read each one as a literal string. Document checks prove a design
determines its artifacts. Only execution proves the artifacts do anything.

Individual workflows can be dispatched directly:

```bash
~/protocol-governed-computing/protocol_runtime/run.sh run \
  --wf book_library_mgmt::WF_SEARCH_CATALOG_V0 \
  --payload <payload.json> \
  --data-root ~/protocol-governed-computing/data/book_library_mgmt
```

The nine are `WF_REGISTER_BOOK_V0` · `WF_REGISTER_PHYSICAL_COPY_V0` ·
`WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0` · `WF_RETIRE_BOOK_RECORD_V0` · `WF_RETIRE_PHYSICAL_COPY_V0` ·
`WF_REINSTATE_BOOK_RECORD_V0` · `WF_REINSTATE_PHYSICAL_COPY_V0` · `WF_SEARCH_CATALOG_V0` ·
`WF_RETRIEVE_BOOK_DETAILS_V0`. Every one takes `staff_credentials`, `authorization_rules` and
`staff_id`: authorization is read, never granted, so the caller supplies both the credentials and the
rules they are checked against. `execution_validation.py`'s `book_payload()` is the worked example.

## Constructing a design into artifacts

The loop to run after **any** edit to a dossier's P7 or P8. Skipping a step leaves the snapshot
describing a design that no longer exists:

```bash
D=~/protocol-governed-computing/business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog

tc construction check $D                       # 100% or the design does not determine its artifacts

python - <<'EOF'                               # construct + persist, through the governed workflow
import sys; W = "/Users/bp/protocol-governed-computing"
for r in ("software_governance", "business_domains", "transformation", "conformance_workloads"):
    sys.path.insert(0, f"{W}/{r}")
from pathlib import Path
from runtime import api
D = Path(W) / "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog"
r = api.run_workflow(
    wf_fqdn="transformation::WF_CONSTRUCT_ARTIFACTS_V0",
    payload={"design_text": (D / "p7_design_intent_book_library_mgmt_catalog_v0.md").read_text(),
             "mandate_text": (D / "p8_authoring_mandate_book_library_mgmt_catalog_v0.md").read_text(),
             "threshold": 100.0},
    snapshot_root=f"{W}/snapshot", data_root=f"{W}/data/transformation")
print(r.status, (r.surface or {}).get("written"), "artifact(s)")
EOF

# promote — a separate, deliberate act; construction writes to data/, not into the domain
rsync -rc ~/protocol-governed-computing/data/transformation/construction/registry/catalog/ \
         ~/protocol-governed-computing/business_domains/book_library_mgmt/registry/catalog/

python ~/protocol-governed-computing/transformation/scripts/testbed/construction_acceptance.py

~/protocol-governed-computing/protocol_compiler/compile_domain.sh ~/protocol-governed-computing/business_domains/book_library_mgmt
~/protocol-governed-computing/snapshot_assembler/assemble.sh

python ~/protocol-governed-computing/business_domains/book_library_mgmt/testbed/catalog/execution_validation.py
```

Construction writes into `data/transformation/construction/registry/` through
`CS_TEXT_ARTIFACT_V0 WRITE_ALL`. **Promotion into the domain is a separate act** — a `tc construction
build` CLI was added once and removed, because it duplicated a governed path with an ungoverned one.

`construction_acceptance.py` compares what the design renders against what the registry holds. Expect
**42/43 at 0 field differences**: the one miss is the hand-authored
`STRUCTURE_BUILD_BOOK_LIBRARY_MGMT_CONFIG_V0`, which no design renders.

## After changing a phase's rules

The rule set is declared in `transformation/design/<phase>/rules.py` and **sealed** into that phase's
workflow artifact. Editing the declaration alone leaves `tc phase check` and the governed workflow
evaluating different rule sets:

```bash
python ~/protocol-governed-computing/transformation/scripts/emit_rule_sets.py           # re-seal
~/protocol-governed-computing/protocol_compiler/compile_domain.sh ~/protocol-governed-computing/transformation
~/protocol-governed-computing/snapshot_assembler/assemble.sh
python ~/protocol-governed-computing/transformation/scripts/testbed/build_fixtures.py   # derive
python ~/protocol-governed-computing/transformation/scripts/testbed/build_payloads.py
```

`--check` first will name the drifted phase. Fixtures and payloads are **derived from the live
dossier** — never hand-edit one; change the dossier or the mutator in `build_fixtures.py`. A derived
fixture cannot go stale silently: the derivation raises rather than producing a wrong fixture.

A new rule needs four things, or it is untested: the check in `design/checks.py`, the `Rule` in the
phase's `rules.py`, a mutator plus `FIXTURES` row in `build_fixtures.py`, and entries in
`build_payloads.py` (source, priors, register key), `e2e_phases_test.py` (`CASES`) and
`differential.py` (`PRIORS_BY_DOCUMENT`).

## Why the phase check is a script

`e2e_phases_test.py` executes each compiled workflow through `protocol_runtime` and asserts the verdict,
finding count and rules evaluated. It is not the same evidence as the differential:

- `differential.py` drives the capability transforms directly — it proves the rule sets and the
  check logic, and nothing about workflow wiring.
- `e2e_phases_test.py` boots the assembled snapshot and dispatches workflows — it proves the IN/WF/CC
  wiring, node bindings and routing.

A workflow that bound `$.capability_result.header` across nodes passed the differential and failed
immediately under the runtime, because workflow nodes read the intent payload rather than a previous
node's result. Both checks are needed; neither substitutes for the other.

## Faster loops

```bash
tc phase list
tc phase check --phase p0 <seed.md>
tc phase check --phase p1 <register.md>
tc phase check --phase p2 <register.md> --snapshot ~/protocol-governed-computing/snapshot

cd ~/protocol-governed-computing/transformation && python scripts/testbed/differential.py
```

From P2 a phase also needs its **priors**, or the handoff between phases goes unchecked:
P1←p0 · P2←p1 · P3←p2 · P4←p3 · **P5 none (it rejects `--prior`)** · P6←p5 · P7←p5+p6 · P8←p7.

```bash
D=~/protocol-governed-computing/business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog
tc phase check --phase p7 $D/p7_design_intent_book_library_mgmt_catalog_v0.md \
   --prior p5=$D/p5_business_intent_book_library_mgmt_catalog_v0.md \
   --prior p6=$D/p6_governance_intent_book_library_mgmt_catalog_v0.md \
   --snapshot /tmp/pgc_cr01_design_baseline
```

A CR is judged against the composition it was **designed** against, never one that already contains
its own output — every identity it assigns would collide. That baseline is reproduced on demand by
`design_baseline()` in `e2e_phases_test.py`, and is stale whenever a source domain has been recompiled
since it was built.

`tc phase check` is the right loop while authoring a document. Phases through P1 judge a document
alone and need no snapshot; from P2 a phase grounds claims against the composition, so `--snapshot`
is required for its grounding rules to be checked at all — without it they report that they could
not run rather than quietly passing. The differential
needs an assembled snapshot and compares the sealed rule set against the declared one.
