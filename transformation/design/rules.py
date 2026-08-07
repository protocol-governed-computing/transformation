"""The rule declaration shared by every phase.

A rule is data: what it is called, which register it governs, which check kind evaluates it, and
with what parameters. No rule logic lives here and no governance intent lives in `checks.py`.

Structural rules — register present, columns declared, table non-empty — are *derived* from a
phase's template by `derive.py`, so a template stays the single declaration of its document's
shape. Every phase gets the same structural discipline for free and declares only what is
distinctive about it. What this module publishes is the `Rule` type itself and the few rule
factories more than one phase composes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable


@dataclass(frozen=True)
class Rule:
    """One declared admissibility rule.

    `id` is the finding code the oracle emits. `register` names the register identity the rule
    governs — stable across retitling — with `section_title` as the fallback for a document that
    carries no register markers. Either may be None for a whole-document rule. `check` names a
    kind in `checks.py`, and `params` must satisfy that kind's contract; `tc phase meta` asserts
    both.
    """

    id: str
    check: str
    section_title: str | None = None
    register: str | None = None
    params: dict[str, Any] = field(default_factory=dict)
    intent: str = ""


# A dossier document states which phase it is, which CR it belongs to, where it stands in the
# lifecycle, and which phase it feeds. The seed uses a different header entirely (domain and
# subdomain), because the seed is where a CR's identity is established rather than carried.
DOSSIER_HEADER_FIELDS = ("Stage", "CR", "Status", "Feeds")

# Field manual §4.1a — the lifecycle a change travels, distinct from the phase it has reached.
LIFECYCLE_STATES = (
    "DRAFT",
    "CONSTRUCTION_COMPLETE",
    "ADMITTED_UNVALIDATED",
    "EXECUTION_VALIDATED",
    "PROMOTED",
)


def governed_hole_rules(exempt: Iterable[str] = ()) -> list[Rule]:
    """No register may declare a cell unresolved instead of stating it.

    A hole was previously admissible anywhere: a cell reading `UNRESOLVED` satisfies every rule that
    asks whether a cell is filled, and no rule asked whether what filled it was an answer. The
    phases that legitimately hold an open question — a clarification register, a gap register —
    declare themselves exempt, so the question is *registered* rather than scattered through the
    registers a later phase reads as decided.
    """
    return [
        Rule(
            id="REGISTER_CELL_UNRESOLVED",
            check="UNRESOLVED_MARKER_ABSENT",
            params={
                "exempt": list(exempt),
                "detail": (
                    "{column!r} declares the question unanswered ({marker}) rather than answering "
                    "it — ask it as a clarification, do not hedge it in a register"
                ),
            },
            intent="an unanswered question left in a register reads as decided to every later phase",
        )
    ]


def clarification_closure_rules(register: str = "clarification_requests") -> list[Rule]:
    """A phase may not hand on a clarification still marked blocking.

    Asking is what the register is for; the rule is about *when* the document is consumed. A
    blocking question is the author's own statement that a later phase cannot proceed without the
    answer, and the phase that proceeds anyway answers it by invention.
    """
    return [
        Rule(
            id="BLOCKING_CLARIFICATION_OUTSTANDING",
            check="ROW_ABSENT_WHEN",
            register=register,
            params={
                "column": "Blocking",
                "value": "YES",
                "detail": (
                    "a blocking clarification is unanswered — resolve it with the named owner and "
                    "fold the answer into the document before any phase consumes it"
                ),
            },
            intent="a blocking question the next phase never sees is answered by invention",
        )
    ]


def dossier_header_rules() -> list[Rule]:
    """The header every dossier phase document carries."""
    return [
        Rule(
            id="HEADER_FIELD_MISSING",
            check="HEADER_FIELD_PRESENT",
            params={"fields": list(DOSSIER_HEADER_FIELDS)},
            intent="a dossier document states its phase, its CR, its lifecycle state, and what it feeds",
        ),
        Rule(
            id="LIFECYCLE_STATE_NOT_IN_VOCABULARY",
            check="HEADER_FIELD_MATCHES",
            params={
                "fields": ["Status"],
                "pattern": r"^(" + "|".join(LIFECYCLE_STATES) + r")\b",
            },
            intent="the lifecycle axis is a controlled vocabulary, not free text",
        ),
    ]
