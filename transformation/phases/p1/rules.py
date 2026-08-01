"""The P1 rule set — what makes a Change Request register admissible.

P1 reuses every mechanism P0 established and declares only what is distinctive about it. Fifteen
check kinds already existed; P1 needed exactly one new one (`CELL_MATCHES`), which is the shape a
healthy analysis loop should produce — mostly REUSE, occasionally AUTHOR_NEW, never a wholesale
re-authoring of things that already work.

What is distinctive about P1 is **traceability**. The seed is where business content enters; P1
restates it as governed rows, and each row must cite the seed finding it came from. A row with no
citation is content the phase invented. P0 forbids invention too, but could only check it
indirectly (design tokens); here it is directly checkable, so it is directly checked.
"""

from __future__ import annotations

from transformation.phases.p0.template import (
    ARTIFACT_KIND_PREFIXES,
    CERTAINTY,
    CR_TYPES,
    HEADER_FIELDS,
    SCOPE_RELATIONSHIPS,
)
from transformation.phases.p0.rules import DESIGN_TOKEN_PATTERN
from transformation.phases.p1.template import SECTIONS, SOURCE_FINDING_PATTERN, section
from transformation.phases.rules import Rule, structural_rules


def _traceability_rules() -> list[Rule]:
    """Every row of every table register must cite its seed finding, in a parseable form.

    Derived from the template rather than listed by hand: a register added later is traced
    automatically, and cannot be forgotten. Forgetting one would leave a register where invention
    is silently permitted — the exact hole this phase exists to close.
    """
    out: list[Rule] = []
    for spec in SECTIONS:
        if "Source Finding" not in spec.table_columns:
            continue
        out.append(
            Rule(
                id="ROW_WITHOUT_SOURCE_FINDING",
                check="CELL_NOT_EMPTY",
                section_title=spec.title,
                params={
                    "column": "Source Finding",
                    "detail": "row cites no seed finding — P1 restates the seed, it does not add to it",
                },
                intent="an uncited row is content the phase invented",
            )
        )
        out.append(
            Rule(
                id="SOURCE_FINDING_MALFORMED",
                check="CELL_MATCHES",
                section_title=spec.title,
                params={
                    "column": "Source Finding",
                    "pattern": SOURCE_FINDING_PATTERN,
                    "detail": (
                        "{value!r} does not name a seed register — cite 'CR seed §N …', "
                        "'CR seed Subdomain Purpose', or 'human decision'"
                    ),
                },
                intent="an unparseable citation is not traceability",
            )
        )
    return out


SEMANTIC_RULES: list[Rule] = [
    Rule(
        id="HEADER_FIELD_MISSING",
        check="HEADER_FIELD_PRESENT",
        params={"fields": list(HEADER_FIELDS)},
        intent="the register must say which domain and subdomain it changes",
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
        id="CLASSIFICATION_NOT_IN_VOCABULARY",
        check="CELL_IN_VOCABULARY",
        section_title=section("cr_type").title,
        params={"column": "Classification", "vocabulary": list(CR_TYPES)},
        intent="the classification is the decision P1 exists to record",
    ),
    Rule(
        id="CLASSIFICATION_WITHOUT_RATIONALE",
        check="CELL_NOT_EMPTY",
        section_title=section("cr_type").title,
        params={
            "column": "Rationale",
            "detail": "a classification with no rationale cannot be reviewed at the gate",
        },
        intent="the decision must be reviewable, not merely recorded",
    ),
    Rule(
        id="CERTAINTY_NOT_IN_VOCABULARY",
        check="CELL_IN_VOCABULARY",
        section_title=section("known_facts").title,
        params={"column": "Certainty", "vocabulary": list(CERTAINTY)},
        intent="a business truth carries a rated certainty",
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
        intent="P2 consumes these goals directly; an empty one is an unverifiable belief",
    ),
    Rule(
        id="SCOPE_RELATIONSHIP_NOT_IN_VOCABULARY",
        check="CELL_IN_VOCABULARY",
        section_title=section("governance_scope").title,
        params={"column": "Relationship", "vocabulary": list(SCOPE_RELATIONSHIPS)},
        intent="governance relationships are a controlled vocabulary",
    ),
    Rule(
        id="DESIGN_LEAKED_INTO_REGISTER",
        check="TOKEN_ABSENT",
        params={
            "pattern": DESIGN_TOKEN_PATTERN,
            "detail": "{token!r} is a compiled artifact identifier — design is assigned at P6b",
        },
        intent="P1 classifies business content; it assigns no design",
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
    """The complete declared P1 rule set: structural, then traceability, then semantic."""
    return structural_rules(SECTIONS) + _traceability_rules() + SEMANTIC_RULES
