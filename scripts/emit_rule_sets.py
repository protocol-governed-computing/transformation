"""Invoke the phase-workflow generator from a terminal.

The generator itself is `transformation.design.emit` — inside the package, because construction has
to be able to import and invoke it. This is the other caller: a person who has just edited a rule
module or a template and wants the workflows brought back into agreement.

Run:  python scripts/emit_rule_sets.py [--check]
Exit: 0 if every workflow already matched (or was rewritten), 1 under --check if any differed.
"""

from __future__ import annotations

import sys

from transformation.design.emit import emit


def main() -> int:
    check_only = "--check" in sys.argv
    results = emit(check_only=check_only)

    for e in results:
        state = "OK      " if not e.drifted else ("DRIFTED " if check_only else "WROTE   ")
        print(f"  {state} {e.phase}  {e.rules:>3} rules  {e.filename}")

    drifted = [e for e in results if e.drifted]
    if check_only and drifted:
        print(f"\n{len(drifted)} workflow(s) do not agree with the generator that produces them.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
