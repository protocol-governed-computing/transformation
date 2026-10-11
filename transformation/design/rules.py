"""The rule declaration shared by every phase.

A rule is data: what it is called, which register it governs, which check kind evaluates it, and
with what parameters. No rule logic lives here and no governance intent lives in `checks.py`.

Every rule is declared in a phase's register schema. Those that follow from shape are derived by
`expand.py`; the rest are the schema's `allOf` entries, decoded by `declared.py`. This module
publishes only the `Rule` type they become.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


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
