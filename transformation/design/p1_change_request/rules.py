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

from transformation.design.derive import derived_rules
from transformation.design.rules import Rule, dossier_header_rules
from transformation.design.template_reader import load

TEMPLATE = load("p1")



# P1's input is the seed, so the seed is the document it must be judged against. This is the first
# rung of the belief chain — P0 → P1 → P2 → P3 is now checked end to end.
PRIORS = ("p0",)


# P0's whole contract is "faithful rewrite only — no content added, no clarification resolved, no
# design assigned". The *added* half was always checkable from P1 alone: a business register naming
# a compiled artifact is design leaking in, and the derived rules catch it. The *dropped* half never
# was. A change request that quietly loses a requested outcome or an acceptance criterion is a
# perfectly well-formed change request; only the seed says otherwise.
#
# Acceptance criteria matter most here. They are what `execution_validation.py` runs the finished
# composition against, so a criterion dropped at P1 is a business requirement that is never built,
# never tested, and never missed.
#
# Matched on the claim, not on a citation. The seed is cited by section title and the title is
# free-form — CR-0 writes `CR seed §5 Beliefs #1` where CR-1 writes `System Beliefs #1`. A label
# that has already drifted between two change requests is not something to match on; the row itself
# is stable, because P0 and P1 state the same claim in the same words by construction.
SEED_PRESERVATION = (
    ("system_beliefs", "Belief"),
    ("requested_outcomes", "Outcome"),
    ("business_invariants", "Invariant"),
    ("acceptance_criteria", "Criterion"),
    ("known_facts", "Fact"),
    ("business_vocabulary", "Term"),
    ("constraints", "Constraint"),
    # An assumption dropped here is never overturned at P2 — it is simply gone, and nothing records
    # that the change once rested on it.
    ("assumptions", "Assumption"),
    ("business_events", "Event"),
    ("authority_boundaries", "Business Object"),
    ("out_of_scope", "Item"),
    ("governance_scope", "Scope Item"),
    ("identity_and_sameness", "Business Object"),
    ("authority_deferrals", "Business Object"),
    # Keyed on several columns, because no single one identifies the row: `Registered` is a state of
    # both a book and a copy, and one operation refuses under more than one condition.
    ("lifecycle_states", ["Object", "State"]),
    ("lifecycle_transitions", ["Object", "From State", "To State"]),
    ("operation_refusals", ["Operation", "Refused When"]),
)


def _seed_rules() -> list[Rule]:
    """Coverage over every register P1 restates from the seed."""
    out: list[Rule] = []
    for register, key in SEED_PRESERVATION:
        out.append(
            Rule(
                id="SEED_ROW_NOT_CARRIED",
                check="PRIOR_ROWS_PRESENT_BY_KEY",
                register=register,
                params={
                    "prior_phase": "p0",
                    "prior_register": register,
                    # Copied rather than shared: one list object referenced twice emits a YAML
                    # anchor and an alias into the sealed rule set, which is not readable as data.
                    "prior_key_column": list(key) if isinstance(key, list) else key,
                    "key_column": list(key) if isinstance(key, list) else key,
                },
                intent="P0 reorganizes and P1 restates; neither may drop what the business said",
            )
        )
    return out


def rule_set() -> list[Rule]:
    """The complete declared P1 rule set: derived, seed preservation, then the dossier header."""
    return derived_rules(TEMPLATE) + _seed_rules() + dossier_header_rules()
