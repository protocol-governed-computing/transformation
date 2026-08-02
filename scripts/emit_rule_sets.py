"""Regenerate the sealed rule set inside each phase workflow from its Python declaration.

A phase declares its rules once, in `transformation/phases/pN_*/rules.py`. The compiled workflow
carries a *copy* of that declaration, because the rules travel in the artifact where they can be
sealed, versioned and inspected. Two copies of one truth drift, and this one drifted silently:
adding a rule after emitting a workflow left 52 rules sealed against 55 declared, and every run
reported confidently on the smaller set.

So the copy is generated, never typed. Edit `rules.py`, run this, commit the workflow.

Run:  python scripts/emit_rule_sets.py [--check]
Exit: 0 if every workflow already matched (or was rewritten), 1 under --check if any differed.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
WORKFLOWS = REPO / "registry" / "phases" / "workflows"

# phase id → the workflow artifact carrying its sealed rule set.
SEALED_IN = {
    "p0": "WF_P0_SEED_ADMISSIBILITY_V0.md",
    "p1": "WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0.md",
    "p2": "WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0.md",
    "p3": "WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0.md",
    "p4": "WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0.md",
    "p5": "WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0.md",
    "p6": "WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0.md",
    "p7": "WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0.md",
    "p8": "WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0.md",
}

RULE_SET_INDENT = 8


def declared(phase_id: str) -> list[dict]:
    """A phase's rule set as the plain data a workflow seals.

    Both locators are emitted when a rule declares a register. `section_title` alone unbinds a
    derived rule from the register it was derived for, and `register` alone loses the fallback P0
    depends on — the failure mode is a rule that resolves to nothing and passes silently.
    """
    from transformation.cli import RULE_SETS

    out = []
    for rule in RULE_SETS[phase_id].rule_set():
        entry: dict = {"id": rule.id, "check": rule.check}
        if rule.register:
            entry["register"] = rule.register
        if rule.section_title and rule.section_title != rule.register:
            entry["section_title"] = rule.section_title
        if rule.params:
            entry["params"] = rule.params
        if rule.intent:
            entry["intent"] = rule.intent
        out.append(entry)
    return out


def render(rules: list[dict]) -> str:
    """The rule set as it appears inside the workflow's `Machine` block.

    Dumped with aliases left on: several phases repeat one large `known_registers` list across
    dozens of rules, and expanding it every time would bury the declaration in its own boilerplate.
    """
    body = yaml.dump(rules, sort_keys=False, width=100, allow_unicode=True, default_flow_style=False)
    pad = " " * RULE_SET_INDENT
    return "".join(f"{pad}{line}\n" if line.strip() else "\n" for line in body.splitlines())


def splice(text: str, rendered: str) -> str:
    """Replace the `rule_set:` block in a workflow artifact, leaving everything else untouched.

    The block runs from its key to the next line indented shallower than the key — the node's
    `next:` routing. Rewriting the whole YAML document instead would reformat hand-written
    structure and strip the comments that explain it.
    """
    lines = text.splitlines(keepends=True)
    key = " " * RULE_SET_INDENT + "rule_set:"
    starts = [i for i, line in enumerate(lines) if line.rstrip("\n") == key]
    if len(starts) != 1:
        raise SystemExit(f"expected exactly one {key!r} line, found {len(starts)}")
    start = starts[0]

    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].lstrip()
        if not stripped:
            continue
        if len(lines[i]) - len(stripped) < RULE_SET_INDENT:
            end = i
            break

    return "".join(lines[:start + 1]) + rendered + "".join(lines[end:])


def main() -> int:
    check_only = "--check" in sys.argv
    differed = 0

    for phase_id, filename in SEALED_IN.items():
        path = WORKFLOWS / filename
        rules = declared(phase_id)
        current = path.read_text(encoding="utf-8")
        updated = splice(current, render(rules))

        if updated == current:
            print(f"  OK       {phase_id}  {len(rules):>3} rules  {filename}")
            continue

        differed += 1
        if check_only:
            print(f"  DRIFTED  {phase_id}  {len(rules):>3} rules  {filename}")
        else:
            path.write_text(updated, encoding="utf-8")
            print(f"  WROTE    {phase_id}  {len(rules):>3} rules  {filename}")

    if check_only and differed:
        print(f"\n{differed} workflow(s) carry a rule set that is not what the phase declares.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
