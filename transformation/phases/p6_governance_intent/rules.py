"""The P6 rule set — what makes a Governance Intent register admissible.

Six registers, their columns, their vocabularies and their traceability come from
`templates/p6_governance_intent_template_v0.md`. Declared here is what the template cannot express.

P6 answers **WHERE**: which subdomain owns each capability, which owns each store, and what crosses
a boundary. It is the phase that draws lines.

The purity ladder does something here that is worth stating, because it looks like a step backwards
and is not. P5 *requires* provisional artifact codes; P6 *forbids* them. Each rung admits its own
vocabulary rather than everything below it — P6's vocabulary is placement, and a capability at this
rung is named in business language and placed in a **subdomain**. A row naming `CC_REGISTER_BOOK_V0`
has answered a question P6 is not asking and pre-empted one Stage 7 owns. Existing artifacts remain
citable by exact FQDN throughout, because citing what already exists is observation, not design.

The rule this phase exists to enforce is ownership exclusivity: **a store is written only by
capabilities of the subdomain that owns it.** When a change needs a peer's store written, the
writing capability belongs to that peer and is declared as a dependency gap. That is not checkable
from a single cell, so what is checked is the discipline that makes it visible: a dependency
declares its direction, a satisfied one cites the artifact that satisfies it, and every capability
named in the outcome was placed in the ownership register first.
"""

from __future__ import annotations

from transformation.phases.derive import derived_rules
from transformation.phases.rules import Rule, dossier_header_rules
from transformation.phases.template_reader import load

TEMPLATE = load("p6")

OBSERVATION_OPERATION = "si.artifact.list"

# operation → the key its result carries rows under.
OBSERVATIONS = {OBSERVATION_OPERATION: "artifacts"}

ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"

# A provisional code — the vocabulary Stage 5 admits and this stage does not.
PROVISIONAL_CODE_PATTERN = r"\b(?:AC|IN|WF|CC|CT|CS|EV|RB)_[A-Z0-9_]+_V\d+\b"

# `this_subdomain → peer`, in either arrow form.
DIRECTION_PATTERN = r"^[a-z][a-z0-9_]*\s*(?:->|→)\s*[a-z][a-z0-9_]*$"


PLACEMENT_RULES: list[Rule] = [
    Rule(
        id="PROVISIONAL_CODE_IN_PLACEMENT",
        check="CELL_TOKEN_ABSENT",
        register="ownership",
        params={
            "columns": ["Capability", "Owner Subdomain"],
            "pattern": PROVISIONAL_CODE_PATTERN,
            "detail": (
                "{token!r} in {column!r} — this stage places capabilities in subdomains; naming an "
                "artifact answers a question Stage 7 owns"
            ),
        },
        intent="placement names a subdomain, never an artifact",
    ),
    Rule(
        id="STORAGE_CODE_IN_PLACEMENT",
        check="CELL_TOKEN_ABSENT",
        register="storage_governance",
        params={
            "columns": ["Storage Need", "Purpose", "Subdomain"],
            "pattern": PROVISIONAL_CODE_PATTERN,
            "detail": "{token!r} in {column!r} — a storage need is business language, not an artifact",
        },
        intent="a store is described by what it holds, not by what will write it",
    ),
    Rule(
        id="SATISFIED_WITHOUT_EXISTING_ARTIFACT",
        check="CELL_NOT_EMPTY",
        register="ownership",
        params={
            "column": "Existing Artifact",
            "only_when_column": "Disposition",
            "only_when_value": "SATISFIED",
            "detail": (
                "capability is SATISFIED but names no existing artifact — a claim that something "
                "already covers this needs the something"
            ),
        },
        intent="a satisfied capability names what satisfies it",
    ),
    Rule(
        id="EXISTING_ARTIFACT_UNRESOLVED",
        check="CITED_ARTIFACTS_RESOLVE",
        register="ownership",
        params={
            "column": "Existing Artifact",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
        },
        intent="an artifact said to cover a capability must be one that really exists",
    ),
    Rule(
        id="PPS_ACTION_IDENTITY_UNRESOLVED",
        check="CITED_ARTIFACTS_RESOLVE",
        register="pps_artifacts_requiring_action",
        params={
            "column": "FQDN",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
        },
        intent="an artifact this change will act on must be one the composition carries",
    ),
    Rule(
        id="DEPENDENCY_DIRECTION_MALFORMED",
        check="CELL_MATCHES",
        register="cross_subdomain_deps",
        params={
            "column": "Direction",
            "pattern": DIRECTION_PATTERN,
            "detail": "direction {value!r} must read `this_subdomain -> peer` — a boundary has two sides",
        },
        intent="a dependency states which way it crosses the boundary",
    ),
    Rule(
        id="DEPENDENCY_SATISFIED_WITHOUT_ARTIFACT",
        check="CELL_NOT_EMPTY",
        register="cross_subdomain_deps",
        params={
            "column": "Existing Artifact",
            "only_when_column": "Status",
            "only_when_value": "SATISFIED",
            "detail": (
                "dependency is SATISFIED but names no existing artifact — an unsatisfied "
                "dependency declared satisfied is how a gap goes missing"
            ),
        },
        intent="a satisfied dependency names the artifact that satisfies it",
    ),
    Rule(
        id="OUTCOME_CAPABILITY_UNPLACED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="governance_outcome",
        params={
            "column": "Capability",
            "target_register": "ownership",
            "target_column": "Capability",
        },
        intent="the outcome restates placement, it does not introduce it",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared P6 rule set: derived, then placement, then the dossier header."""
    return derived_rules(TEMPLATE) + PLACEMENT_RULES + dossier_header_rules()
