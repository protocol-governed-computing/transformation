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

~/protocol-governed-computing/snapshot_assembler/assemble.sh
```

Every domain that declares source must be compiled — the assembler refuses otherwise rather than
silently producing a smaller composition. If a compile step is skipped it names the command to run.

## Check

```bash
python ~/protocol-governed-computing/transformation/scripts/testbed/e2e_phases.py

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
| `e2e_phases.py` | `E2E PASSED` — every phase, both admissible and inadmissible, exit 0 |
| collatz | `SUCCESS`, `all_terminate: true` |
| govern agent action | `SUCCESS` |
| provision licensing | `SUCCESS` first run against a fresh `data/`; `ALREADY_EXISTS` on any re-run |

Both transformation verdicts complete with `Status: SUCCESS`. An inadmissible document is a correct
judgement, not a failed execution — `VIOLATION` there would mean the phase itself is broken.

## Why the phase check is a script

`e2e_phases.py` executes each compiled workflow through `protocol_runtime` and asserts the verdict,
finding count and rules evaluated. It is not the same evidence as the differential:

- `differential.py` drives the capability transforms directly — it proves the rule sets and the
  check logic, and nothing about workflow wiring.
- `e2e_phases.py` boots the assembled snapshot and dispatches workflows — it proves the IN/WF/CC
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
