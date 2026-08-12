"""The generators construction may invoke, and how it asks whether one already agrees.

A design names the generator an artifact is reached by. Construction reaches it by *invoking* that
generator and never by writing the artifact itself — refusing outright would leave the delivery of
every generated artifact ungoverned, and rendering it directly would make construction a second
producer of the same truth. Two producers drift, and the drift is silent until something reads the
stale one.

**The registry is closed**, exactly as the check-kind registry is. A design naming a generator
nothing here declares is fail-hard, never a silently skipped artifact: resolving an arbitrary dotted
path at runtime would let a design point construction at any callable in the interpreter, and an
artifact reached by something nobody admitted is an artifact nobody governs. Adding a generator is a
change to this file, which is where it can be reviewed.

Each entry answers two questions, and they are different questions. `invoke` reaches the artifact.
`stale` reports whether the artifact already agrees with what produces it — asked without changing
the answer, which is what makes it usable as a build gate rather than as a habit.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from transformation.design import emit as phase_emit


@dataclass(frozen=True)
class Generator:
    """One admitted generator: what it produces its artifacts with, and how it is questioned."""

    name: str
    invoke: Callable[[], object]
    stale: Callable[[], list[str]]
    summary: str


def _phase_workflows_stale() -> list[str]:
    return [e.filename for e in phase_emit.check()]


GENERATORS: dict[str, Generator] = {
    phase_emit.GENERATOR: Generator(
        name=phase_emit.GENERATOR,
        invoke=phase_emit.emit_rule_sets,
        stale=_phase_workflows_stale,
        summary="the phase workflows and the rule set each of them seals",
    ),
}


class UnknownGenerator(KeyError):
    """A design named a generator construction is not permitted to invoke."""


def resolve(name: str) -> Generator:
    """The admitted generator by the name a design gave it, or fail hard."""
    if name not in GENERATORS:
        raise UnknownGenerator(
            f"unknown generator {name!r}; construction may invoke {sorted(GENERATORS)}"
        )
    return GENERATORS[name]
