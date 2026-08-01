"""The P0 rule set — what makes a change seed admissible.

The seed's sixteen registers, their columns, their inline vocabularies and which may be empty come
from `templates/p0_change_seed_template_v0.md`. Unlike P1 through P7 that template is *authored*
rather than salvaged: RI-0 began at the change request and consumed a hand-built elicitation whose
provenance nothing recorded.

What is declared here is what the template cannot express — the discipline that makes a seed a
faithful rewrite rather than a rewrite with additions:

- a System Belief must stay a belief, and must state what verification would settle it
- a belief must never carry a certainty rating, which is what makes a statement a fact
- open questions must be stated, including as "none"

The purity rung is `business_language` throughout, and the template flags every register as such,
so a compiled artifact identity anywhere in the seed is caught by the derived rules.
"""

from __future__ import annotations

from transformation.phases.derive import derived_rules
from transformation.phases.rules import Rule, dossier_header_rules
from transformation.phases.template_reader import load

TEMPLATE = load("p0")

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


SEED_DISCIPLINE_RULES: list[Rule] = [
    Rule(
        id="BELIEF_CARRIES_CERTAINTY",
        check="COLUMN_ABSENT",
        register="system_beliefs",
        params={
            "column": "Certainty",
            "detail": "beliefs must not carry a Certainty column — that would make them facts",
        },
        intent="the truth/belief split is what P2 verification depends on",
    ),
    Rule(
        id="BELIEF_WITHOUT_VERIFICATION_GOAL",
        check="CELL_NOT_EMPTY",
        register="system_beliefs",
        params={
            "column": "Verification Goal",
            "detail": "every belief must state what P2 has to establish",
        },
        intent="an unverifiable belief silently becomes an assumption",
    ),
    Rule(
        id="BELIEF_STATED_AS_FACT",
        check="CELL_NOT_PREFIXED",
        register="system_beliefs",
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
]


def rule_set() -> list[Rule]:
    """The complete declared P0 rule set: derived, then seed discipline, then the dossier header."""
    return derived_rules(TEMPLATE) + SEED_DISCIPLINE_RULES + dossier_header_rules()
