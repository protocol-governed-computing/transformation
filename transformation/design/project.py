"""Deterministic projections — a phase document that its prior uniquely determines.

Most phases decide something. P1 stopped deciding anything the moment blocking clarifications
became inadmissible at P0: with no open question left to interrogate, a change request is the seed's
registers plus, per row, the citation saying where it came from. Its inputs are the seed; its output
is determined; there is no design choice remaining. That is a compiler pass, not an authoring task,
and it is the same transition the Construction Compiler made when a design that uniquely determines
its artifacts stopped being rewritten by hand.

**The amendment ruling.** A question discovered while restating the seed amends P0 and is projected
again. It never enters at P1. Before the projection ran, P1 was where a second author could add a
row the business never said — the failure `ROW_NOT_IN_SEED` exists to catch — and P0's Clarification
Requests were one of two places a question could be asked. There is now one place, and human
semantic content enters the dossier exactly once.

**What P1's rule set governs afterwards.** A projected P1 cannot fail `SEED_ROW_NOT_CARRIED` or
`ROW_NOT_IN_SEED`: it was built from the rows those rules check. Reading its verdict as evidence
about the *change* would be vacuity of the kind this codebase keeps rediscovering. Those 169 rules
govern **amendment** — a P1 edited after projection, or authored by hand — and the derived fixtures
are what keeps them exercised. The check on a freshly projected P1 proves the projection, which is
worth running and is not the same claim.

A projection refuses to run against an inadmissible prior. Projecting a seed that still carries an
open blocking clarification would launder the question into a document that looks settled.
"""

from __future__ import annotations

from typing import Callable

import yaml

from transformation.design.checks import EMPTINESS_SENTINEL, is_sentinel
from transformation.design.evaluate import ParsedDocument
from transformation.design.schema import PhaseShape as PhaseTemplate, load

# The column a projected row's provenance goes in, and the shape of the citation. P1 cites the seed
# by section and row ordinal; the ordinal is what makes a citation checkable, and hand-typing it is
# what makes it wrong — `#12` pointing at row 11 resolves to a claim the row does not make, and
# nothing downstream can tell.
PROVENANCE_COLUMN = "Source Finding"


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(
    str, lambda d, v: d.represent_scalar("tag:yaml.org,2002:str", v, style="|" if "\n" in v else None))


def _template_layout(template: PhaseTemplate) -> list[tuple[str, str, str, list[str]]]:
    """(number, title, register id, column headings) in template order.

    The template is the single declaration of the document's shape, so the projection reads it
    rather than restating it. A register added to the template appears in the projection with no
    code change; one restated here would be a second declaration that can disagree.

    Headings are taken verbatim from the template's own header row, not from the parsed column
    names: `Certainty (HIGH, MEDIUM, LOW)` declares both the column and the values it admits, and a
    projection that emitted the bare name would strip the vocabulary out of the document while the
    rules went on enforcing it.

    The section a register is cited by is the template's. Every seed numbers its sections as the
    template does, so the citation names a section the seed's reader finds.
    """
    return [
        (register.section_number or "", register.section_title, register.id, list(register.headings))
        for register in template.registers
    ]


def _value(row: dict[str, str], heading: str) -> str:
    """A row's value for a column heading, matched the way the checks match one.

    A heading carrying a controlled vocabulary is longer in one document than another —
    `Relationship (CREATED, ADJACENT)` became `Relationship (CREATED, EXTENDED, …)` when P1's
    vocabulary was widened — so the column is addressed by its name, never by the whole heading.
    """
    name = heading.split("(")[0].strip()
    for key, value in row.items():
        if key.startswith(name):
            return str(value).strip()
    return ""


def project_p1(prior: ParsedDocument) -> str:
    """The change request the seed determines: its registers, each row cited to where it was said."""
    template = load("p1")
    by_id = {register["id"]: register for register in prior.registers}
    cr = prior.header.get("CR", "")
    subject = (prior.raw.splitlines() or [""])[0].split("—")[-1].strip()

    registers: dict[str, dict] = {}
    headings: list[str] = []
    for number, title, register_id, columns in _template_layout(template):
        source = by_id.get(register_id)
        content = [dict(row) for row in (source.get("rows") or [])] if source else []
        rows = []
        for ordinal, row in enumerate(content, start=1):
            # The emptiness sentinel is not a row and is projected as itself. Citing it to a seed
            # finding invents a finding — the seed said the register has no entries, which is not
            # something any row of it said.
            if is_sentinel(row):
                rows.append(dict(zip(columns, [EMPTINESS_SENTINEL] + [""] * (len(columns) - 1))))
                continue
            values = [_value(row, column) for column in columns[:-1]]
            values.append(f"CR seed §{number} {title} #{ordinal}")
            rows.append(dict(zip(columns, values)))
        registers[register_id] = {"columns": columns, "rows": rows}
        headings += [f"## {number}. {title}", "", "---", ""]

    machine = yaml.dump(
        {"header": {"Stage": "1 — Change Request (Clarification & Fact Capture)", "CR": cr,
                    "Status": "DRAFT", "Feeds": "Stage 2 — Domain Model Discovery"},
         "registers": registers},
        Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=100000)

    emits = " · ".join(register.id for register in template.registers)
    parts = [
        f"# Stage 1 — Change Request: Clarification & Fact Capture: {subject}",
        "",
        "## Machine",
        "",
        "```yaml",
        machine.rstrip("\n"),
        "```",
        "",
        "Projected from the change seed. Every row is the seed's own, cited to the section it was",
        "said in. S1 interrogates and does not author: a question raised by restating the seed",
        "amends the seed and is projected again, so no row here states business content the seed",
        "does not.",
        "",
        "---",
        "",
        *headings,
        "## gov_projection — Governed Handoff to Stage 2",
        "",
        "| Direction | Fields |",
        "|-----------|--------|",
        "| **Consumes** ← CR seed | human elicitation answers (the seed) |",
        f"| **Emits** → Stage 2 | {emits} |",
    ]
    return "\n".join(parts) + "\n"


# phase → (the prior it is projected from, the projection). A phase absent from this table is one a
# human still decides; adding an entry is a ruling that it no longer is.
PROJECTIONS: dict[str, tuple[str, Callable[[ParsedDocument], str]]] = {
    "p1": ("p0", project_p1),
}
