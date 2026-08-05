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

Both transformation verdicts complete with `Status: SUCCESS`. An inadmissible document is a correct
judgement, not a failed execution — `VIOLATION` there would mean the phase itself is broken.

`differential.py` must be run from the `transformation` directory: it imports `design_baseline` from
`e2e_phases_test`, which sits beside it. `--check` on the emitter is the cheap half of what the
differential proves — it compares counts without booting a snapshot, so it catches a rule added and
never re-emitted in a second rather than a minute.

## The catalog domain has no runtime check yet

`book_library_mgmt` compiles and assembles, and there is deliberately **nothing to run**. What is in
`registry/catalog/` is the retired design's artifact set; the current dossier under
`cr_dossiers/cr_01_catalog/` designs forty artifacts that have not been constructed.

Two scripts that used to appear in check lists no longer exist:

- `cr_01_catalog/execution_validation.py` — validated 9 acceptance criteria against the retired
  design's artifacts. Deleted with that design. The current one declares **18** criteria, and its
  replacement is written after construction.
- `cr_01_catalog/populate_catalog.py` — seeded data for those same artifacts.

Until the artifacts are constructed, the catalog's evidence is its dossier: every phase ADMISSIBLE and
`tc construction check` at 100%. A checklist that still calls those two scripts is older than the
dossier it is checking.

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

`tc phase check` is the right loop while authoring a document. Phases through P1 judge a document
alone and need no snapshot; from P2 a phase grounds claims against the composition, so `--snapshot`
is required for its grounding rules to be checked at all — without it they report that they could
not run rather than quietly passing. The differential
needs an assembled snapshot and compares the sealed rule set against the declared one.
