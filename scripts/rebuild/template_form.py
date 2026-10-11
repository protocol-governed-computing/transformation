"""Templates in the Machine-block form (M5, D7), written from the register schemas.

A template keeps its prose: elicitation, the document contract and guidance. What the table form
put in the prose moves to one Machine-block skeleton, generated from the schema:
- the bold header lines become the `document` header;
- each register marker and its table become a reference to the register in the block;
- the handoff table is written from the schema's `x-consumes` and `x-emits`;
- the passages about table conventions (the empty-register sentinel, `;`-separated citations) are
  restated for the block.

    python scripts/rebuild/template_form.py
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

from transformation.design.catalog import PHASES
from transformation.design.schema import load

TEMPLATES = Path(__file__).resolve().parents[2] / "transformation" / "templates"
HEADER_LINE = re.compile(r"^\*\*[A-Z][A-Za-z ]*:\*\*")
MARKER = re.compile(r"^<!-- register:([a-z0-9_]+)[^>]*-->\s*$")
SENTINEL = re.compile(r"A required register with no rows (MUST render|renders|MUST be rendered) as")
# Prose that names the table form's conventions, restated for the block.
WORDING = {"Populated register tables": "Populated registers",
           "`open_questions = NONE IDENTIFIED`": "`open_questions: []`",
           "Empty (`NONE IDENTIFIED`)": "Empty (`[]`)"}

EMPTY = ("A register with nothing to state is `[]`, declared empty. A register left `null` states nothing,\n"
         "and a required register that states nothing is refused.\n")

CITING = """### Citing a prior row

Every row carries a `source_finding` naming where its content came from. A citation is a mapping:

- **a row of a register**, by ordinal or by key, in the phase that declared it:
  `{phase: p1, register: known_facts, row: 14}`. A citation that names no phase names this document;
- **an artifact already in the baseline**, by exact identity: `{artifact: blockchain::WF_REGISTER_ACTOR_V0}`;
- **a person**: `{source: human}`.

Several citations are a list. A row that cites nothing is `null`, and is refused where the register
requires provenance.

**A carried claim is carried verbatim.** Where a register restates a row an earlier phase declared —
a belief, an authoring decision, a capability — the text must match that row exactly. Tightening a
sentence while citing the row it came from is how a claim drifts from what was decided, so the rules
treat a tidier synonym as a new claim and refuse it. Cite it as it stands, or change it in the phase
that owns it.
"""


def skeleton(phase: str) -> str:
    """The Machine block a document of this phase fills in."""
    shape = load(phase)
    document = {"phase": phase, "domain": "<domain>", "subdomain": "<subdomain>", "cr": "<change>",
                "rule_set": shape.schema_id}
    registers = {}
    for register in shape.registers:
        registers[register.id] = [{k: None for k in register.keys}] if register.columns else None
    text = yaml.safe_dump({"document": document, "registers": registers}, sort_keys=False,
                          allow_unicode=True, width=100)
    if "approval" in shape.document:
        text = text.replace(f"  rule_set: {shape.schema_id}\n",
                            f"  rule_set: {shape.schema_id}\n"
                            f"  # approval: {{gate: ..., rule_set: ..., state: APPROVED}} — when the gate closes\n")
    return f"## Machine\n\n```yaml\n{text}```\n"


def handoff(phase: str) -> list[str]:
    shape = load(phase)
    priors = ", ".join(shape.priors) or "the human"
    rows = ["| Direction | Registers |", "|-----------|-----------|"]
    rows.append(f"| **Consumes** ← {priors} | {' · '.join(shape.consumes) or 'the business problem statement'} |")
    rows.append(f"| **Emits** | {' · '.join(shape.emits)} |")
    return [r + "\n" for r in rows]


def migrate(text: str, phase: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = [lines[0], "\n", skeleton(phase)]
    i = 1
    while i < len(lines) and (HEADER_LINE.match(lines[i]) or not lines[i].strip()):
        i += 1
    if i < len(lines) and lines[i].startswith("---"):
        i += 1
    out.append("\n")
    in_handoff = False
    while i < len(lines):
        line = lines[i]
        marker = MARKER.match(line)
        if marker:
            out.append(f"Register `{marker.group(1)}` in the Machine block.\n")
            i += 1
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                i += 1
            continue
        if line.startswith("### Citing a prior row"):
            out.append(CITING)
            i += 1
            while i < len(lines) and not lines[i].startswith("---"):
                i += 1
            out.append("\n")
            continue
        if SENTINEL.search(line):
            out.append(EMPTY)
            i += 1
            while i < len(lines) and lines[i].strip():
                i += 1
            # The sentinel row it showed, and the sentence that followed it, go with it.
            while i < len(lines) and (not lines[i].strip() or lines[i].lstrip().startswith("|")):
                i += 1
            if i < len(lines) and lines[i].startswith("A prose-only or empty"):
                while i < len(lines) and lines[i].strip():
                    i += 1
            out.append("\n")
            continue
        for old, new in WORDING.items():
            line = line.replace(old, new)
        if line.startswith("## gov_projection"):
            in_handoff = True
        if in_handoff and line.startswith("| Direction"):
            out += handoff(phase)
            i += 1
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                i += 1
            continue
        out.append(line)
        i += 1
    return re.sub(r"\n{3,}", "\n\n", "".join(out))


if __name__ == "__main__":
    for spec in PHASES:
        path = TEMPLATES / spec.template
        path.write_text(migrate(path.read_text(encoding="utf-8"), spec.id), encoding="utf-8")
        print(f"  {spec.id}  {spec.template}")
