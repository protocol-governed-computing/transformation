"""The P1 rule set — what makes a Change Request register admissible.

Almost all of it is derived from `templates/p1_change_request_template_v0.md`: the fifteen
registers, their columns, the controlled vocabularies declared inline in the column headers, which
registers may be empty, and which columns hold business language. That template is the tested
original; restating any of it here would create a second declaration that can disagree with it —
which is exactly what the first cut of this file did, at 109 hand-written rules against a register
shape that turned out to be wrong in several places.

What remains hand-declared is only what the template cannot express: the document header, which
sits above the registers and belongs to no register.

The purity rung (`business_language`, per field manual §4.2) is enforced through the template's own
per-register flags rather than as a phase-wide rule, because the flag is where the exceptions live.
"""

from __future__ import annotations

from transformation.phases.derive import derived_rules
from transformation.phases.rules import Rule, dossier_header_rules
from transformation.phases.template_reader import load

TEMPLATE = load("p1")



def rule_set() -> list[Rule]:
    """The complete declared P1 rule set: derived from the template, then the dossier header."""
    return derived_rules(TEMPLATE) + dossier_header_rules()
