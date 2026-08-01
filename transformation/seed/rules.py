"""The P0 rule set — the behavior half of the oracle.

Every rule that decides seed admissibility is *declared here as data*: what it is called, which
register it governs, which check kind evaluates it, and with what parameters. No rule logic lives
in this file and no governance intent lives in `checks.py`.

The consequence that matters: "what governs a seed?" is answered by reading this list or running
`tc seed rules` — never by reading Python control flow. A rule can be quoted in evidence, diffed
across releases, and counted. Adding a rule is an entry here; it requires new code only when it
needs a mechanism that does not yet exist.

Structural rules (section present, numbered, table shaped) are *derived* from the template rather
than restated, so the template stays the single declaration of the seed's shape.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from transformation.seed.template import (
    ARTIFACT_KIND_PREFIXES,
    CERTAINTY,
    CR_TYPES,
    HEADER_FIELDS,
    SCOPE_RELATIONSHIPS,
    SECTIONS,
    section,
)


@dataclass(frozen=True)
class Rule:
    """One declared admissibility rule.

    `id` is the finding code the oracle emits. `section_title` names the register the rule
    governs, or None for whole-document rules. `check` names a kind in `checks.py`.
    """

    id: str
    check: str
    section_title: str | None = None
    params: dict[str, Any] = field(default_factory=dict)
    intent: str = ""


# A belief written with the grammar of an assertion. P0's cardinal sin is promoting a System Belief
# to a Known Fact; these openers are how it happens in prose.
ASSERTIVE_OPENERS = (
    "there is ",
    "there are ",
    "the system provides ",
    "the system has ",
    "it is confirmed ",
    "confirmed: ",
)

DESIGN_TOKEN_PATTERN = (
    r"\b(?:" + "|".join(ARTIFACT_KIND_PREFIXES) + r")_[A-Z0-9_]+_V\d+\b"
)


def _structural_rules() -> list[Rule]:
    """Derive presence / numbering / table rules from the template declaration."""
    out: list[Rule] = []
    for spec in SECTIONS:
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


SEMANTIC_RULES: list[Rule] = [
    Rule(
        id="HEADER_FIELD_MISSING",
        check="HEADER_FIELD_PRESENT",
        params={"fields": list(HEADER_FIELDS)},
        intent="the seed must say which domain and subdomain it changes",
    ),
    Rule(
        id="HEADER_MALFORMED",
        check="HEADER_FIELD_MATCHES",
        params={
            "fields": ["Domain", "Primary subdomain"],
            "pattern": r"^[a-z][a-z0-9_]*",
        },
        intent="domain and subdomain are identifiers, not prose",
    ),
    Rule(
        id="CR_TYPE_NOT_DECLARED",
        check="SECTION_DECLARES_ONE_OF",
        section_title=section("cr_type").title,
        params={"vocabulary": list(CR_TYPES)},
        intent="exactly one CR type; the transformation is one kind of change or another",
    ),
    Rule(
        id="CERTAINTY_NOT_IN_VOCABULARY",
        check="CELL_IN_VOCABULARY",
        section_title=section("known_facts").title,
        params={"column": "Certainty", "vocabulary": list(CERTAINTY)},
        intent="a business truth carries a rated certainty",
    ),
    Rule(
        id="FACT_EMPTY",
        check="CELL_NOT_EMPTY",
        section_title=section("known_facts").title,
        params={"column": "Fact", "detail": "Fact is empty"},
        intent="a rated row with no claim is not a fact",
    ),
    Rule(
        id="BELIEF_CARRIES_CERTAINTY",
        check="COLUMN_ABSENT",
        section_title=section("system_beliefs").title,
        params={
            "column": "Certainty",
            "detail": "beliefs must not carry a Certainty column — that would make them facts",
        },
        intent="the truth/belief split is what P2 verification depends on",
    ),
    Rule(
        id="BELIEF_WITHOUT_VERIFICATION_GOAL",
        check="CELL_NOT_EMPTY",
        section_title=section("system_beliefs").title,
        params={
            "column": "Verification Goal",
            "detail": "every belief must state what P2 has to establish",
        },
        intent="an unverifiable belief silently becomes an assumption",
    ),
    Rule(
        id="BELIEF_WITHOUT_RATIONALE",
        check="CELL_NOT_EMPTY",
        section_title=section("system_beliefs").title,
        params={
            "column": "Why it matters",
            "detail": "every belief must scope why it matters to this CR",
        },
        intent="an unscoped belief cannot be closed",
    ),
    Rule(
        id="BELIEF_STATED_AS_FACT",
        check="CELL_NOT_PREFIXED",
        section_title=section("system_beliefs").title,
        params={
            "column": "Belief",
            "prefixes": list(ASSERTIVE_OPENERS),
            "detail": (
                "belief is asserted, not suspected ({prefix!r}) — "
                "state it as a belief or move it to Known Facts"
            ),
        },
        intent="P0 must not promote a System Belief to a Known Fact",
    ),
    Rule(
        id="SCOPE_RELATIONSHIP_NOT_IN_VOCABULARY",
        check="CELL_IN_VOCABULARY",
        section_title=section("governance_scope").title,
        params={"column": "Relationship", "vocabulary": list(SCOPE_RELATIONSHIPS)},
        intent="governance relationships are a controlled vocabulary",
    ),
    Rule(
        id="DESIGN_LEAKED_INTO_SEED",
        check="TOKEN_ABSENT",
        params={
            "pattern": DESIGN_TOKEN_PATTERN,
            "detail": (
                "{token!r} is a compiled artifact identifier — P0 must not assign design"
            ),
        },
        intent="P0 rewrites business prose; design is assigned at P6b",
    ),
    Rule(
        id="CLARIFICATIONS_UNSTATED",
        check="SECTION_HAS_TEXT",
        section_title=section("clarification_requests").title,
        params={
            "detail": "state the open questions or '(none)' — an empty section asserts nothing"
        },
        intent="silence is not the same as 'no open questions'",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared rule set, structural first."""
    return _structural_rules() + SEMANTIC_RULES
