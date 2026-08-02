"""The P7 rule set — what makes a Design Intent register admissible.

Eight registers, their columns, their vocabularies and their traceability come from
`templates/p7_design_intent_template_v0.md`. Declared here is what the template cannot express.

P7 answers **HOW**, and it is where identity becomes binding. P5 assigned provisional codes, P6
placed capabilities in subdomains; P7 turns those into domain-qualified FQDNs that later phases,
the compiler and the runtime will all use verbatim. **Gate 1 closes here** — the dossier is
reviewed as a body before any mandate may be drafted.

One rule inverts everything the pipeline has done so far. Every earlier phase cites artifacts that
exist and is wrong when a citation does not resolve. P7 assigns identities that *will* exist, and
is wrong when one **does**: a code colliding with something already in the composition is not a new
artifact but a silent redefinition of an old one. `CITED_ARTIFACTS_ABSENT` is the only rule here
that reads a successful resolution as the defect, and it is the reason this phase must ground.

**Data-to-decision closure** is the second thing P7 owns, and CR-1 proved it the hard way: a
composition can be fully admissible, materialize, compile, and still let an unauthorized caller
through — because a `CS` read reports whether the *lookup* succeeded, not what it *found*. Routing a
workflow on that status is routing on "the store answered", which is always true.

So a step that reads external state must declare the transform that interprets its output and the
status that interpretation yields. Raw observations never determine workflow behaviour directly. The
missing transform was not an implementation bug; it was a missing design element, and this is where
design elements are assigned.

The rest is immutability discipline. A binding FQDN is assigned once and reused as the exact same
string everywhere, because a spelling variant of the same concept does not read as a synonym — it
creates a second, permanently misnamed artifact. So every code referenced in the topology, in a
runtime binding, or in a composition must be declared: as new here, or as an existing artifact
carried over. A reference to neither is a name nobody owns.
"""

from __future__ import annotations

from transformation.phases.derive import derived_rules
from transformation.phases.rules import Rule, dossier_header_rules
from transformation.phases.template_reader import load

TEMPLATE = load("p7")

OBSERVATION_OPERATION = "si.artifact.list"

# operation → the key its result carries rows under.
OBSERVATIONS = {OBSERVATION_OPERATION: "artifacts"}

ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"

# A binding FQDN: domain-qualified, family-prefixed, explicitly versioned.
BINDING_FQDN_PATTERN = r"^[a-z][a-z0-9_.]*::(?:WF|IN|RB|CC|CT|CS|EV|AC|STRUCTURE)_[A-Z0-9_]+_V\d+$"


BINDING_RULES: list[Rule] = [
    Rule(
        id="NEW_CODE_ALREADY_EXISTS",
        check="CITED_ARTIFACTS_ABSENT",
        register="new_artifacts",
        params={
            "column": "Code",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
        },
        intent="an identity assigned as new must not already name something else",
    ),
    Rule(
        id="NEW_CODE_MALFORMED",
        check="CELL_MATCHES",
        register="new_artifacts",
        params={
            "column": "Code",
            "pattern": BINDING_FQDN_PATTERN,
            "detail": "binding code {value!r} must be domain::FAMILY_NAME_V<n>",
        },
        intent="a binding identity is domain-qualified, family-prefixed and versioned",
    ),
    Rule(
        id="EXISTING_INVENTORY_UNRESOLVED",
        check="CITED_ARTIFACTS_RESOLVE",
        register="existing_inventory",
        params={
            "column": "FQDN",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
        },
        intent="an artifact carried over from the composition must really be in it",
    ),
    Rule(
        id="TOPOLOGY_WORKFLOW_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="execution_topology",
        params={
            "column": "Workflow",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
        },
        intent="a workflow in the topology is one this design declared or carried over",
    ),
    Rule(
        id="TOPOLOGY_NODE_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="execution_topology",
        params={
            "column": "Node",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
            "detail": (
                "a binding identity is immutable, so a spelling variant is a second artifact "
                "rather than a synonym"
            ),
        },
        intent="every node in the topology is an identity this design actually assigned",
    ),
    Rule(
        id="RB_BINDS_UNDECLARED_WORKFLOW",
        check="CELL_RESOLVES_IN_REGISTER",
        register="rb_declarations",
        params={
            "column": "Binds WF",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
        },
        intent="a runtime binding binds a workflow that exists in this design",
    ),
    Rule(
        id="RB_CODE_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="rb_declarations",
        params={
            "column": "RB Code",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
        },
        intent="a runtime binding is itself a declared artifact, never implicit",
    ),
    Rule(
        id="COMPOSITION_CC_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="cc_composition",
        params={
            "column": "CC Code",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
        },
        intent="a composition belongs to a capability contract this design declared",
    ),
    Rule(
        id="COMPOSITION_STEP_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="cc_composition",
        params={
            "column": "Capability",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
        },
        intent="a step invokes a capability that is declared new or carried over, never invented inline",
    ),
    Rule(
        id="OBSERVATION_WITHOUT_INTERPRETATION",
        check="CELL_NOT_EMPTY",
        register="cc_composition",
        params={
            "column": "Interpreted By",
            "only_when_column": "Kind",
            "only_when_value": "CS",
            "detail": (
                "a step that reads external state names no interpreting transform — a raw "
                "observation cannot drive business routing, because the status it carries says "
                "the store answered, not what it found"
            ),
        },
        intent="every read of external state declares how its output becomes a decision",
    ),
    Rule(
        id="OBSERVATION_WITHOUT_SEMANTIC_STATUS",
        check="CELL_NOT_EMPTY",
        register="cc_composition",
        params={
            "column": "Semantic Status",
            "only_when_column": "Kind",
            "only_when_value": "CS",
            "detail": (
                "a step that reads external state names no semantic status — the workflow branch "
                "it feeds has nothing declared to route on"
            ),
        },
        intent="an interpretation names the outcome it yields, closing the route",
    ),
    Rule(
        id="INTERPRETATION_TRANSFORM_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="cc_composition",
        params={
            "column": "Interpreted By",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
            "detail": "an interpreting transform is an artifact like any other, declared or carried over",
        },
        intent="the transform that turns an observation into a decision is itself governed",
    ),
    Rule(
        id="STORE_WITHOUT_PROPOSED_PATH",
        check="CELL_NOT_EMPTY",
        register="structure_stores",
        params={
            "column": "Proposed Path",
            "detail": "store declares no proposed path — a store nobody can locate is not designed",
        },
        intent="a declared store says where it will live",
    ),
]


# P7 is where the purity ladder is paid off. P5 names capabilities the business asked for and is
# forbidden to bind them; P7 binds. The design document it must be judged against is therefore P5's.
PRIORS = ("p5", "p6")


# One direction only, and the asymmetry is the point.
#
# Every provisional code must acquire a binding identity: P5 is the last phase that speaks for what
# the business asked for, so a code that reaches P7 and is never assigned is a capability the
# business requested and the design quietly declined to build. Nothing else would notice — P7's
# register is complete and well formed without it.
#
# The reverse is not a defect. P7 legitimately assigns artifacts P5 could not have named: a
# STRUCTURE, an RB, a CT are design-layer artifacts below the rung P5 is allowed to reach. Checking
# containment both ways would reject every correct design for doing its job — the same over-flagging
# the identity taxonomy exists to prevent.
LADDER_RULES: list[Rule] = [
    # P6 records which cross-subdomain dependencies an artifact already in the composition
    # satisfies. P7 is where a satisfied dependency becomes inventory the design commits to reusing;
    # one that never arrives is a dependency the design silently took on without declaring.
    Rule(
        id="SATISFIED_DEPENDENCY_NOT_INVENTORIED",
        check="PRIOR_IDENTITIES_COVERED",
        register="existing_inventory",
        params={
            "prior_phase": "p6",
            "prior_register": "cross_subdomain_deps",
            "prior_column": "Existing Artifact",
            "column": "FQDN",
            "require": "prior_in_here",
        },
        intent="a dependency declared satisfied by an existing artifact must be inventoried as reuse",
    ),
    Rule(
        id="PROVISIONAL_CODE_NEVER_BOUND",
        check="PRIOR_IDENTITIES_COVERED",
        register="new_artifacts",
        params={
            "prior_phase": "p5",
            "prior_register": "provisional_codes",
            "prior_column": "Provisional Code",
            "column": "Code",
            "require": "prior_in_here",
            # P5 must not namespace a provisional code and P7 must namespace an assigned one; the
            # two cells state one identity at two rungs.
            "match_on": "bare_code",
        },
        intent="a capability the business asked for and the design never bound is declined, not deferred",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared P7 rule set: derived, binding discipline, ladder closure, header."""
    return derived_rules(TEMPLATE) + BINDING_RULES + LADDER_RULES + dossier_header_rules()
