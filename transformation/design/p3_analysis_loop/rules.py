"""The P3 rule set — what makes an Analysis Loop register admissible.

The rules are declared in this phase's register schema, `registry/schema/REGISTER_SCHEMA_P3_V0.json`: its shape,
and an `allOf` entry for every rule beyond it. This module only expands them, so a rule is read and
changed in one place.
"""

from __future__ import annotations

from transformation.design.expand import expanded_rules
from transformation.design.rules import Rule
from transformation.design.schema import load

PHASE = "p3"
SHAPE = load(PHASE)
PRIORS: tuple[str, ...] = SHAPE.priors
# The composition facts this phase grounds against: inspection operation → result key.
OBSERVATIONS: dict[str, str] = SHAPE.observations


def rule_set() -> list[Rule]:
    """The complete declared P3 rule set."""
    return expanded_rules(SHAPE)
