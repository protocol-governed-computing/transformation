"""The rule declaration shared by every phase.

A rule is data: what it is called, which register it governs, which check kind evaluates it, and
with what parameters. No rule logic lives here and no governance intent lives in `checks.py`.

Structural rules — section present, numbered, table shaped — are *derived* from a phase's template
rather than restated, so a template stays the single declaration of its document's shape. Every
phase gets the same structural discipline for free and declares only what is distinctive about it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable


@dataclass(frozen=True)
class Rule:
    """One declared admissibility rule.

    `id` is the finding code the oracle emits. `section_title` names the register the rule
    governs, or None for whole-document rules. `check` names a kind in `checks.py`.
    """

    id: str
    check: str
    section_title: str | None = None
    register: str | None = None
    params: dict[str, Any] = field(default_factory=dict)
    intent: str = ""


def structural_rules(sections: Iterable) -> list[Rule]:
    """Derive presence / numbering / table rules from a phase's template declaration."""
    out: list[Rule] = []
    for spec in sections:
        out.append(
            Rule(
                id="SECTION_MISSING",
                check="SECTION_PRESENT",
                section_title=spec.title,
                intent="every declared register must be present",
            )
        )
        if spec.number is not None:
            out.append(
                Rule(
                    id="SECTION_MISNUMBERED",
                    check="SECTION_NUMBERED",
                    section_title=spec.title,
                    params={"number": spec.number},
                    intent="registers are referenced by number downstream",
                )
            )
        if spec.table_columns:
            out.append(
                Rule(
                    id="TABLE_MISSING",
                    check="TABLE_PRESENT",
                    section_title=spec.title,
                    intent="a register must be readable as rows, not prose",
                )
            )
            out.append(
                Rule(
                    id="TABLE_COLUMN_MISSING",
                    check="TABLE_HAS_COLUMNS",
                    section_title=spec.title,
                    params={"columns": list(spec.table_columns)},
                    intent="downstream phases read these columns by name",
                )
            )
            if not spec.may_be_empty:
                out.append(
                    Rule(
                        id="TABLE_EMPTY",
                        check="TABLE_HAS_ROWS",
                        section_title=spec.title,
                        intent="an empty required register asserts nothing",
                    )
                )
    out.append(
        Rule(
            id="SECTION_OUT_OF_ORDER",
            check="SECTIONS_ASCENDING",
            intent="section order is part of the template contract",
        )
    )
    return out
