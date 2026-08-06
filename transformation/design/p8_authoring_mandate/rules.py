"""The P8 rule set — what makes an Authoring Mandate admissible.

Seven registers, their columns, their vocabularies and their traceability come from
`templates/p8_authoring_mandate_template_v0.md`. Declared here is what the template cannot express.

P8 is the last dossier phase and the least creative one, deliberately. It **adds nothing and drops
nothing** — it orders what Stage 7 assigned into the sequence a builder can actually follow.
"Mandate" is the right word: this is not one possible plan but the only ordering the dependency
graph admits. **Gate 2 closes here**, freezing scope; after it, a departure is a recorded deviation
rather than a silent change.

Which makes P8 the one phase whose correctness is a property of **row order**. Every rule before
this judges rows independently — a register is a set of claims, each true or false on its own. Here
a register can consist entirely of well-formed rows and still be wrong:

- a **gap** in the step sequence is an artifact silently dropped between two steps that both look
  fine, and nothing reading a row at a time would see the absence
- a dependency scheduled **after** the thing that needs it makes the mandate unexecutable, and the
  defect is invisible in either row alone

Those two are what separate a topological sort from a list, so they are what this phase checks.

The other discipline is immutability, inherited from Stage 7: every code is copied verbatim. A
re-typed FQDN — even one transposed letter — mints a second, permanently misnamed artifact rather
than referring to the first.
"""

from __future__ import annotations

from transformation.design.derive import derived_rules
from transformation.design.rules import (
    Rule,
    dossier_header_rules,
    governed_hole_rules,
)
from transformation.design.template_reader import load

TEMPLATE = load("p8")

OBSERVATION_OPERATION = "si.artifact.list"

# operation → the key its result carries rows under.
OBSERVATIONS = {OBSERVATION_OPERATION: "artifacts"}

ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"
BINDING_FQDN_PATTERN = r"^[a-z][a-z0-9_.]*::(?:WF|IN|RB|CC|CT|CS|EV|AC|VOCAB|STRUCTURE)_[A-Z0-9_]+_V\d+$"


ORDER_RULES: list[Rule] = [
    Rule(
        id="BUILD_STEPS_NOT_CONTIGUOUS",
        check="COLUMN_SEQUENCE_CONTIGUOUS",
        register="build_order",
        params={"column": "Step", "start": 1},
        intent="the build sequence is total and gapless, because a gap is a dropped artifact",
    ),
    Rule(
        id="DEPENDENCY_SCHEDULED_LATER",
        check="DEPENDENCY_PRECEDES",
        register="build_order",
        params={
            "column": "Code",
            "depends_column": "Depends On",
            "order_column": "Step",
        },
        intent="everything a step depends on is built before it — this is what makes it a sort",
    ),
    Rule(
        id="BUILD_CODE_MALFORMED",
        check="CELL_MATCHES",
        register="build_order",
        params={
            "column": "Code",
            "pattern": BINDING_FQDN_PATTERN,
            "detail": "build code {value!r} must be a binding FQDN copied verbatim from Stage 7",
        },
        intent="a mandate orders binding identities, never re-typed approximations",
    ),
    Rule(
        id="BUILD_CODE_ALREADY_EXISTS",
        check="CITED_ARTIFACTS_ABSENT",
        register="build_order",
        params={
            "column": "Code",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
        },
        intent="an artifact mandated for authoring must not already be in the composition",
    ),
    Rule(
        id="CRITICAL_PATH_NOT_IN_BUILD_ORDER",
        check="CELL_RESOLVES_IN_REGISTER",
        register="critical_path",
        params={
            "column": "Code",
            "target_register": "build_order",
            "target_column": "Code",
            "detail": "the critical path runs through steps the mandate schedules, not past them",
        },
        intent="the critical path is a path through this build order",
    ),
    Rule(
        id="CRITICAL_PATH_NOT_CONTIGUOUS",
        check="COLUMN_SEQUENCE_CONTIGUOUS",
        register="critical_path",
        params={"column": "Position", "start": 1},
        intent="a path is an ordered chain, not an unordered set of steps",
    ),
    Rule(
        id="CAPABILITY_WITHOUT_PURPOSE",
        check="CELL_NOT_EMPTY",
        register="new_capabilities",
        params={
            "column": "Purpose",
            "detail": "capability states no purpose — a builder needs to know what to build, not only its name",
        },
        intent="a mandated capability says what it is for",
    ),
    Rule(
        id="INTENT_WITHOUT_WORKFLOW",
        check="CELL_NOT_EMPTY",
        register="new_intents",
        params={
            "column": "Workflow",
            "detail": "intent names no workflow — an entry point that starts nothing cannot be authored",
        },
        intent="every mandated intent names the workflow it starts",
    ),
]


# P8's mandate is a mechanical derivation of P7's design, so the design is the document it must be
# judged against. `key_rule` in the catalogue has said "must reconcile with p7 exactly" since P8 was
# built; nothing enforced it.
PRIORS = ("p7",)


# The reconciliation the catalogue always claimed. P7 assigns the identities, P8 schedules them, and
# a mandate is correct only when the two sets are the same one.
#
# Neither direction is visible in either document. A build order made entirely of well-formed rows,
# contiguous, topologically sorted, can omit an artifact the design declared — every existing P8
# rule passes it. And a mandate can schedule an identity no phase ever designed, which reads as an
# ordinary row and is a design decision taken by whoever typed it.
RECONCILIATION_RULES: list[Rule] = [
    Rule(
        id="DESIGNED_ARTIFACT_NOT_SCHEDULED",
        check="PRIOR_IDENTITIES_COVERED",
        register="build_order",
        params={
            "prior_phase": "p7",
            "prior_register": "new_artifacts",
            "prior_column": "Code",
            "column": "Code",
            "require": "prior_in_here",
        },
        intent="an artifact the design declared and the mandate never schedules is not deferred, it is lost",
    ),
    Rule(
        id="SCHEDULED_ARTIFACT_NOT_DESIGNED",
        check="PRIOR_IDENTITIES_COVERED",
        register="build_order",
        params={
            "prior_phase": "p7",
            "prior_register": "new_artifacts",
            "prior_column": "Code",
            "column": "Code",
            "require": "here_in_prior",
        },
        intent="a mandate orders the build; it does not get to add to it",
    ),
]


# Placement completeness. `field_declarations` covered eight of CR-1's twenty-five artifacts and
# nothing noticed: every rule judged the rows present, and a compiled artifact without a declared
# subdomain is one construction would have to place by guessing.
COMPLETENESS_RULES: list[Rule] = [
    Rule(
        id="SCHEDULED_ARTIFACT_UNPLACED",
        check="REGISTER_COVERS_REGISTER",
        register="field_declarations",
        params={
            "source_register": "build_order",
            "source_column": "Code",
            "column": "Code",
        },
        intent="every artifact the mandate schedules declares the subdomain it is built into",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared P8 rule set: derived, order discipline, reconciliation, then header."""
    return (
        derived_rules(TEMPLATE)
        + ORDER_RULES
        + RECONCILIATION_RULES
        + COMPLETENESS_RULES
        + governed_hole_rules()
        + dossier_header_rules()
    )
