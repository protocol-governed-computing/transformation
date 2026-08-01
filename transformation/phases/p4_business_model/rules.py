"""The P4 rule set — what makes a Business Model register admissible.

Eleven registers, their columns, their vocabularies and their traceability come from
`templates/p4_business_model_template_v0.md`. Declared here is what the template cannot express.

P4 **consolidates**. P2 discovered, P3 decided; P4 is the canonical artifact every later phase
projects from, and its key rule is *consolidation, not re-litigation*. Nothing new is designed
here — which means the defects worth checking are not about any single register saying something
wrong, but about the registers disagreeing with each other.

That is why P4 is the first phase with **cross-register** rules. Every earlier phase judges a
register on its own terms, because discovery has nothing to be consistent with yet. A consolidation
whose capability graph points at a gap nobody declared is broken in a way no single-register rule
can see: each register is individually well-formed, and the document as a whole asserts something
untrue.

The consistency the template states in prose, made mechanical:

- a CRITICAL capability must carry a gap entry, and that entry must name a declared gap
- a declared gap must have an owning subdomain — an unowned gap is nobody's work
- an in-scope capability must reference a gap, so scope traces to evidence rather than intent

`dependency_graph` is the one register permitted to cite existing artifacts by FQDN, so it is also
the one that must be grounded: a dependency on something that is not there is a plan built on a
capability nobody has.
"""

from __future__ import annotations

from transformation.phases.derive import derived_rules
from transformation.phases.rules import Rule, dossier_header_rules
from transformation.phases.template_reader import load

TEMPLATE = load("p4")

OBSERVATION_OPERATION = "si.artifact.list"

# operation → the key its result carries rows under.
OBSERVATIONS = {OBSERVATION_OPERATION: "artifacts"}

ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"


CONSOLIDATION_RULES: list[Rule] = [
    Rule(
        id="CRITICAL_WITHOUT_GAP_ENTRY",
        check="CELL_NOT_EMPTY",
        register="capability_graph",
        params={
            "column": "Gap Register Entry",
            "only_when_column": "Status",
            "only_when_value": "CRITICAL",
            "detail": (
                "capability is CRITICAL but names no gap — work this change request must do has "
                "nowhere to be tracked"
            ),
        },
        intent="every capability that must be authored is a declared gap",
    ),
    Rule(
        id="GAP_ENTRY_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="capability_graph",
        params={
            "column": "Gap Register Entry",
            "target_register": "gap_register",
            "target_column": "Gap Code",
            "only_when_column": "Status",
            "only_when_value": "CRITICAL",
            "detail": "a consolidation may only point at what it consolidated",
        },
        intent="a capability points only at a gap the document itself declares",
    ),
    Rule(
        id="GAP_WITHOUT_OWNER",
        check="CELL_NOT_EMPTY",
        register="gap_register",
        params={
            "column": "Owner Subdomain",
            "detail": "gap names no owning subdomain — an unowned gap is nobody's work",
        },
        intent="every gap has a subdomain accountable for closing it",
    ),
    Rule(
        id="SCOPE_WITHOUT_GAP_REFERENCE",
        check="CELL_NOT_EMPTY",
        register="authoring_scope",
        params={
            "column": "Gap Register Ref",
            "detail": "in-scope capability references no gap — scope must trace to evidence",
        },
        intent="what this change request builds traces to a declared gap, not to intent",
    ),
    Rule(
        id="SCOPE_GAP_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="authoring_scope",
        params={
            "column": "Gap Register Ref",
            "target_register": "gap_register",
            "target_column": "Gap Code",
            "detail": "a consolidation may only point at what it consolidated",
        },
        intent="scope points only at a gap the document itself declares",
    ),
    Rule(
        id="DEPENDENCY_IDENTITY_UNRESOLVED",
        check="CITED_ARTIFACTS_RESOLVE",
        register="dependency_graph",
        params={
            "column": "To",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
        },
        intent="a dependency on an existing artifact must be one that really exists",
    ),
    Rule(
        id="DECISION_WITHOUT_RATIONALE",
        check="CELL_NOT_EMPTY",
        register="design_decisions",
        params={
            "column": "Rationale",
            "detail": "design decision states no rationale — a decision without a reason cannot be reviewed",
        },
        intent="a consolidated decision carries the reasoning that produced it",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared P4 rule set: derived, then consolidation, then the dossier header."""
    return derived_rules(TEMPLATE) + CONSOLIDATION_RULES + dossier_header_rules()
