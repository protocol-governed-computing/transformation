"""Construction Completeness — the Construction lifecycle's admission gate.

A phase document is admitted by `tc phase check` against a declared rule set. A *design* is admitted
to construction by this: does it uniquely determine the artifacts it specifies? `UNIQUELY_DETERMINED_
OR_STOP` is the rule, and a percentage below the threshold is a refusal, not a report.

    CR-1 as first authored     54.8%
    construction requirement   100%, or the generator is inventing design

**The requirement list is derived, never declared.** It is the shape `render_all` emits, walked leaf
by leaf, so it cannot drift from construction — it *is* construction. An earlier version kept a
hand-written list and read 100% while the generator could reproduce one artifact in twenty-five: it
asked whether a contract declared a pipeline and never whether each step declared its store. A
hand-maintained list of what construction needs is a second opinion about construction, and the
weaker one. The declared list held 170 facts; the derived one holds 710.

**This needs nothing to have been built.** That is what separates it from the acceptance harness,
which compares a render against artifacts that already exist and can therefore only ever judge CR-1.
This judges a design on its own, which is what every CR after the first needs before a line of it is
authored.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field

from transformation.build.render import requirements


@dataclass
class Completeness:
    """What a design determines, and what it leaves to the generator to invent."""

    facts: list[tuple[str, str, bool]] = field(default_factory=list)

    @property
    def determined(self) -> int:
        return sum(1 for _, _, ok in self.facts if ok)

    @property
    def total(self) -> int:
        return len(self.facts)

    @property
    def percentage(self) -> float:
        return 100.0 * self.determined / self.total if self.total else 0.0

    @property
    def by_artifact(self) -> dict[str, list[tuple[str, bool]]]:
        out: dict[str, list[tuple[str, bool]]] = {}
        for code, path, ok in self.facts:
            out.setdefault(code, []).append((path, ok))
        return out

    @property
    def undetermined(self) -> Counter:
        """Undetermined facts by field, with list indices collapsed."""
        counts: Counter = Counter()
        for _, path, ok in self.facts:
            if not ok:
                counts[re.sub(r"\[\d+\]", "[]", path)] += 1
        return counts

    def meets(self, threshold: float) -> bool:
        return self.percentage + 1e-9 >= threshold


def measure(p7: dict, p8: dict) -> Completeness:
    """Measure a design against what construction requires of it."""
    return Completeness(facts=requirements(p7, p8))
