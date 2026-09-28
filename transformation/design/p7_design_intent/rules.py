"""The P7 rule set — what makes a Design Intent register admissible.

Sixteen registers, their columns, their vocabularies and their traceability come from
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

The last thing P7 owns is how an artifact is **reached**, and it was the last thing it could not say.
Every register describes what an artifact must become; a generated artifact's interesting fact is
that its source of truth is elsewhere, and a design naming only the artifact schedules a copy that
the next emission overwrites. `generation_provenance` names the generator and the sources read with
it, and construction invokes that rather than becoming a second producer of the same artifact.
"""

from __future__ import annotations

from transformation.design.families import authorable_fqdn_pattern, binding_fqdn_pattern
from transformation.design.derive import derived_rules
from transformation.design.rules import (
    event_naming_rules,
    Rule,
    dossier_header_rules,
    governed_hole_rules,
)
from transformation.design.template_reader import load

TEMPLATE = load("p7")

OBSERVATION_OPERATION = "si.artifact.list"

# operation → the key its result carries rows under.
# P7 grounds against two surfaces. The artifact list resolves identities; the capability surface
# says what an operation actually yields, which is the one fact that distinguishes a step producing
# a real field from a step producing a wish.
CAPABILITY_OBSERVATION = "si.capability.surface"

TRANSFORM_OBSERVATION = "si.capability.surface#transforms"

# What a capability contract requires. A reused contract declares nothing in the design —
# it already exists — so the only place its interface can be read is the composition.
CONTRACT_OBSERVATION = "si.capability.surface#contracts"

# Which records each binding covers. A design names a binding and never the records behind it, so
# the reach it declares is checkable only against a surface that answers the other half — and this
# is the surface that answers it for every store at once, which is the only shape a fixed pipeline
# can ask for.
STORE_OBSERVATION = "si.store.list"

# Which rules are in force, and in which artifact. A refusal may be carried out by a rule of the
# pipeline rather than by a step of the domain's own acts, and a citation nobody resolves documents
# intent and enforces nothing. The sealed set is what a pin names, so it is what is asked.
RULE_SET_OBSERVATION = "si.rule_set.list"

# Which places each composed workflow already has, by key. A design that amends a workflow routes to
# places it does not redeclare, and those resolve only against the composition.
WORKFLOW_OBSERVATION = "si.behavior_logic.list"

OBSERVATIONS = {
    OBSERVATION_OPERATION: "artifacts",
    CAPABILITY_OBSERVATION: "capabilities",
    TRANSFORM_OBSERVATION: "transforms",
    CONTRACT_OBSERVATION: "contracts",
    STORE_OBSERVATION: "stores",
    RULE_SET_OBSERVATION: "carriers",
    WORKFLOW_OBSERVATION: "workflows",
}


def _phase_workflows() -> dict[str, str]:
    """phase id → the artifact carrying its sealed rule set.

    Declared with the rule rather than inferred in the check: the snapshot publishes identities and
    knows nothing of phases, and it should stay that way. `emit` already owns the mapping because it
    is the generator that writes those artifacts, so this reads it rather than keeping a second copy.
    """
    from transformation.design.emit import SEALED_IN, workflow_fqdn

    return {phase: workflow_fqdn(phase) for phase in SEALED_IN}

ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"

# A binding FQDN: domain-qualified, family-prefixed, explicitly versioned.
BINDING_FQDN_PATTERN = binding_fqdn_pattern()

# An identity a design may amend, which is narrower than one it may cite.
AUTHORABLE_FQDN_PATTERN = authorable_fqdn_pattern()


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
    # A design amends by re-rendering whole, so it may only amend what it could have authored. The
    # governance surface has no family and no builder: a constitution's content is argument, and a
    # register that determined it would have to carry the argument. So a governance change is
    # authored by a person under a governed dossier and its dossier is complete at P6 — the ruling
    # is in `THE_SHAPE_OF_A_CHANGE_V0.md` §7. Citing one of these is untouched; three dossiers
    # reached P6 before the boundary was stated, and none of them could be told it here.
    Rule(
        id="AMENDED_ARTIFACT_NOT_AUTHORABLE",
        check="CELL_MATCHES",
        register="existing_inventory",
        params={
            "column": "FQDN",
            "pattern": AUTHORABLE_FQDN_PATTERN,
            "only_when_column": "Action",
            "only_when_value": "EXTEND",
            "detail": (
                "amends {value!r}, whose family this design cannot author — an amended artifact is "
                "rendered whole, so this schedules a document to be rewritten from registers that "
                "never held its content. The governance surface is authored, not constructed: cite "
                "it with REUSE or REVIEW, and deliver the change by authoring it"
            ),
        },
        intent="a design amends only what it could have authored",
    ),
    Rule(
        id="REPLACED_ARTIFACT_NOT_AUTHORABLE",
        check="CELL_MATCHES",
        register="existing_inventory",
        params={
            "column": "FQDN",
            "pattern": AUTHORABLE_FQDN_PATTERN,
            "only_when_column": "Action",
            "only_when_value": "REPLACE",
            "detail": (
                "replaces {value!r}, whose family this design cannot author — a replacement is a "
                "rendering like any other. The governance surface is authored, not constructed"
            ),
        },
        intent="a design replaces only what it could have authored",
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
            # A keyed node is a place, not an identity; what must resolve is the contract it runs.
            # So a key with a blank `Runs` is read as a code, and refused as one nobody declared.
            "prefer_column": "Runs",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
            # A terminal is a property of the graph, not an artifact anyone declares.
            "exempt_prefixes": ["EXIT"],
            "detail": (
                "a binding identity is immutable, so a spelling variant is a second artifact "
                "rather than a synonym"
            ),
        },
        intent="every node in the topology runs an identity this design actually assigned",
    ),
    Rule(
        id="TOPOLOGY_NODE_REPEATED",
        check="TOPOLOGY_KEY_UNIQUE",
        register="execution_topology",
        intent="a node names one place in its workflow",
    ),
    Rule(
        id="TOPOLOGY_ROUTE_UNRESOLVED",
        check="TOPOLOGY_ROUTE_RESOLVES",
        register="execution_topology",
        params={"exempt_prefixes": ["EXIT"], "observation": WORKFLOW_OBSERVATION},
        intent="control reaches only a node the workflow declares or already has, or an ending",
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
    # The em-dash in either column is a declaration: the step's output is data, and the branches
    # are the operation's own statuses. Asked as "is the cell filled?", both of these were
    # satisfied by that dash on all 62 CS steps in the corpus, so neither had ever bound a design.
    # Grounded instead in what the operation answers, they bite exactly where the doctrine means
    # them to — a branch the store cannot produce, with nothing named that produces it.
    Rule(
        id="OBSERVATION_WITHOUT_INTERPRETATION",
        check="OUTCOME_GROUNDED_IN_OPERATION",
        register="cc_composition",
        params={
            "column": "Interpreted By",
            "kind_column": "Kind",
            "kind_value": "CS",
            "routing_column": "Routing",
            "status_column": "Semantic Status",
            "observation": CAPABILITY_OBSERVATION,
            "detail": (
                "branches on {outcomes}, which {operation} does not answer — it answers "
                "{answers}. An outcome the store cannot produce comes from an interpretation, and "
                "this step names none, so the branch is a decision nothing makes"
            ),
        },
        intent="an outcome the operation cannot answer names the transform that produces it",
    ),
    Rule(
        id="OBSERVATION_WITHOUT_SEMANTIC_STATUS",
        check="OUTCOME_GROUNDED_IN_OPERATION",
        register="cc_composition",
        params={
            "column": "Semantic Status",
            "kind_column": "Kind",
            "kind_value": "CS",
            "routing_column": "Routing",
            "status_column": "Semantic Status",
            "observation": CAPABILITY_OBSERVATION,
            "detail": (
                "routes on {outcomes} and declares no semantic status — {operation} answers "
                "{answers}, so the outcome routed on is an interpretation's, and the workflow "
                "branch it feeds has nothing declared to route on"
            ),
        },
        intent="an interpretation names the outcome it yields, closing the route",
    ),
    # The other two em-dash columns, grounded the same way. `Store` was read by nothing at all, and
    # `Consumes` was read only where it named something — so a step addressing no store and a step
    # handing an operation nothing were both unexamined declarations. What decides each is published:
    # a capability's category, and an operation's inputs.
    Rule(
        id="STORE_UNGROUNDED_IN_CAPABILITY",
        check="STORE_GROUNDED_IN_CAPABILITY",
        register="cc_composition",
        params={
            "column": "Store",
            "capability_column": "Capability",
            "storage_category": "storage",
            "observation": CAPABILITY_OBSERVATION,
            "detail_missing": (
                "names no store on {capability}, which keeps records — a storage step that "
                "addresses nothing is a read or a write with no subject"
            ),
            "detail_spurious": (
                "names a store on {capability}, which keeps none — the step addresses records "
                "that capability has no way to hold"
            ),
        },
        intent="a step addresses a store exactly when its capability keeps one",
    ),
    Rule(
        id="STEP_CONSUMES_NOTHING_FROM_OPERATION_WITH_INPUT",
        check="CONSUMPTION_GROUNDED_IN_OPERATION",
        register="cc_composition",
        params={
            "column": "Consumes",
            "capability_column": "Capability",
            "kind_column": "Kind",
            "kind_value": "CS",
            "observation": CAPABILITY_OBSERVATION,
            "detail": (
                "consumes nothing and invokes {operation}, which accepts {accepts} — the "
                "operation receives no value for what it takes, and the step reports success on "
                "having addressed nothing"
            ),
        },
        intent="a step consuming nothing invokes an operation that takes nothing",
    ),
    # The two halves of one statement, and neither is a rule alone: refusing an unused reach permits
    # a read nobody declared, and refusing an undeclared read permits a reach held in reserve. Both
    # read the binding a design names and derive the records from the composition, because a design
    # that restated them would be the second copy this change exists beside.
    Rule(
        id="DECLARED_REACH_UNUSED",
        check="REACH_IS_USED",
        register="declared_reach",
        params={
            "register": "declared_reach",
            "topology_register": "execution_topology",
            "composition_register": "cc_composition",
            "observation": STORE_OBSERVATION,
            "contract_observation": CONTRACT_OBSERVATION,
            "detail": (
                "declares a reach to {binding} and reads nothing it covers — that binding answers "
                "for {stores}, and no step this act runs addresses any of them. A permission "
                "granted for nothing is one whose purpose nobody reviewed"
            ),
        },
        intent="every reach an act declares is used by a read that act performs",
    ),
    Rule(
        id="UNDECLARED_REACH_READ",
        check="READ_IS_DECLARED",
        register="execution_topology",
        params={
            "register": "declared_reach",
            "rb_register": "rb_declarations",
            "topology_register": "execution_topology",
            "composition_register": "cc_composition",
            "observation": STORE_OBSERVATION,
            "contract_observation": CONTRACT_OBSERVATION,
            "detail": (
                "reads {store}, which {binding} does not cover and no declared reach names — the "
                "act reaches records another part of the business owns and its design does not say "
                "so, which is invisible until the act runs"
            ),
        },
        intent="an act reads nothing it did not declare a reach to",
    ),
    Rule(
        id="CROSS_SUBDOMAIN_WRITE",
        check="CROSS_SUBDOMAIN_REACH_READ_ONLY",
        register="execution_topology",
        params={
            "topology_register": "execution_topology",
            "new_register": "new_artifacts",
            "artifact_observation": OBSERVATION_OPERATION,
            "capability_observation": CAPABILITY_OBSERVATION,
            "contract_observation": CONTRACT_OBSERVATION,
        },
        intent="an act reaching into another subdomain reads what it holds and never changes it",
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
    # A vocabulary that extends nothing is a base vocabulary, which is a decision. Left blank it is
    # indistinguishable from a design that forgot, and construction renders `extends: ''` either
    # way — the same silence `declared_empty` exists to break everywhere else. So the design writes
    # the none marker and construction reads it as the statement it is.
    Rule(
        id="VOCABULARY_WITHOUT_EXTENDS",
        check="CELL_NOT_EMPTY",
        register="vocabulary_extensions",
        params={
            "column": "Extends",
            "detail": (
                "vocabulary says nothing about what it extends — a base vocabulary declares that "
                "with the none marker, because an empty cell and an omission render the same thing"
            ),
        },
        intent="a vocabulary states what it extends, or states that it extends nothing",
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
# The seed joins them for the refusals. P7 must refuse a design that leaves a declared refusal
# unaccounted for, and it cannot refuse what it cannot see: the register lives in the seed, and P5
# and P6 neither carry it nor should. Carrying it forward instead would mean a register and a carry
# rule in each intermediate phase, restating what the seed already says and free to drift from it —
# and P5 and P6 already declare `p0` directly, so this is the mechanism the pipeline has rather than
# a new one.
PRIORS = ("p5", "p6", "p0")


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
            # A code is bound by authoring the artifact or by extending the one that already
            # carries the identity. Without the second, a change request that extends anything is
            # unauthorable: the code must appear in `new_artifacts` to satisfy this rule and must
            # not, because `NEW_CODE_ALREADY_EXISTS` refuses an identity the composition already
            # holds. The two rules were each correct and jointly unsatisfiable.
            "union": [{
                "register": "existing_inventory",
                "column": "FQDN",
                "only_when_column": "Action",
                "only_when_value": "EXTEND",
            }],
        },
        intent="a capability the business asked for and the design never bound is declined, not deferred",
    ),
    Rule(
        id="AUTHORED_ARTIFACT_WITHOUT_INTENT",
        check="PRIOR_IDENTITIES_COVERED",
        register="new_artifacts",
        params={
            "prior_phase": "p5",
            "prior_register": "provisional_codes",
            "prior_column": "Provisional Code",
            "column": "Code",
            "require": "here_in_prior",
            "match_on": "bare_code",
        },
        intent="an artifact the design authors is one the business asked for, never one it invented",
    ),
]


# Construction completeness — the obligation that a declared artifact is actually specified.
#
# P7 declared six workflows and gave three of them a topology, declared eight capability contracts
# and composed five, and was ADMISSIBLE at fifty-seven rules. Every rule judged the rows that were
# present; nothing required the rows that were absent. The information had somewhere to live and no
# obligation to exist — a deficiency in the language's *constraints*, not in its expressiveness.
#
# One rule per family, because the obligation differs by family: a workflow needs a topology, a
# contract needs a composition, a transform needs an implementation, and none needs the others'.
COMPLETENESS_RULES: list[Rule] = [
    Rule(
        id="WORKFLOW_WITHOUT_TOPOLOGY",
        check="REGISTER_COVERS_REGISTER",
        register="execution_topology",
        params={
            "source_register": "new_artifacts",
            "source_column": "Code",
            "column": "Workflow",
            "only_when_column": "Family",
            "only_when_value": "WF",
        },
        intent="a workflow with no declared graph is a workflow construction would have to invent",
    ),
    Rule(
        id="WORKFLOW_WITHOUT_RUNTIME_BINDING",
        check="REGISTER_COVERS_REGISTER",
        register="rb_declarations",
        params={
            "source_register": "new_artifacts",
            "source_column": "Code",
            "column": "Binds WF",
            "only_when_column": "Family",
            "only_when_value": "WF",
        },
        intent="a workflow with no runtime binding cannot resolve the capabilities it composes",
    ),
    Rule(
        id="CONTRACT_WITHOUT_COMPOSITION",
        check="REGISTER_COVERS_REGISTER",
        register="cc_composition",
        params={
            "source_register": "new_artifacts",
            "source_column": "Code",
            "column": "CC Code",
            "only_when_column": "Family",
            "only_when_value": "CC",
        },
        intent="a capability contract with no declared pipeline specifies nothing to build",
    ),
    Rule(
        id="TRANSFORM_WITHOUT_IMPLEMENTATION",
        check="REGISTER_COVERS_REGISTER",
        register="implementation_bindings",
        params={
            "source_register": "new_artifacts",
            "source_column": "Code",
            "column": "CT Code",
            "only_when_column": "Family",
            "only_when_value": "CT",
        },
        intent="a transform is the one family that points outside the composition; the path is designed, not discovered",
    ),
    # A REPLACE says an artifact is superseded, and until now said it only in prose. Construction
    # had no concept of the action at all — `_scheduled` admitted an amendment when its action was
    # EXTEND and nothing else — so a design could retire a workflow, emit, and leave the retired one
    # in place, compiled and dispatchable, with the build reporting success. The design must name
    # what supersedes it, because "superseded" with no successor is a deletion wearing a softer word.
    Rule(
        id="REPLACED_ARTIFACT_WITHOUT_SUCCESSOR",
        check="REGISTER_COVERS_REGISTER",
        register="artifact_properties",
        params={
            "source_register": "existing_inventory",
            "source_column": "FQDN",
            "column": "Value",
            "only_when_column": "Action",
            "only_when_value": "REPLACE",
            "covered_only_when_column": "Property",
            "covered_only_when_value": "supersedes",
        },
        intent="an artifact this design replaces is named by whatever supersedes it",
    ),
    # A vocabulary states the group its values belong to and the spelling they take. Both were
    # literals in the renderer until a vocabulary that was not a result status carried a group it
    # did not belong to and a spelling its values did not have, and the platform refused it. A
    # design that says neither leaves the renderer to choose, which is a second design authority.
    Rule(
        id="VOCABULARY_WITHOUT_GROUP",
        check="CELL_NOT_EMPTY",
        register="vocabulary_extensions",
        params={
            "column": "Group",
            "detail": (
                "vocabulary names no group for its values — the renderer would supply one, and it "
                "supplies the same one to every vocabulary whatever the values mean"
            ),
        },
        intent="a vocabulary states the group its values belong to",
    ),
    Rule(
        id="VOCABULARY_WITHOUT_CASING",
        check="CELL_NOT_EMPTY",
        register="vocabulary_extensions",
        params={
            "column": "Casing",
            "detail": (
                "vocabulary names no spelling for its values — the renderer would supply one, and a "
                "spelling its values do not have is refused by the platform that reads them"
            ),
        },
        intent="a vocabulary states the spelling its values take",
    ),
    Rule(
        id="VOCABULARY_WITHOUT_VALUES",
        check="REGISTER_COVERS_REGISTER",
        register="vocabulary_extensions",
        params={
            "source_register": "new_artifacts",
            "source_column": "Code",
            "column": "Vocabulary Code",
            "only_when_column": "Family",
            "only_when_value": "VOCAB",
        },
        intent="a vocabulary that declares no value admits nothing",
    ),
]


# The new registers carry identities like every other, and the same immutability discipline applies:
# a spelling variant is a second artifact, not a synonym.
# The roots a binding source may name. Execution offers these and nothing else: the workflow
# payload, the contract's own inputs, a prior step or CC's results, the raw result of the step being
# bound, and the step's status. A source rooted anywhere else names a place that does not exist, and
# every layer below treats it as a literal string instead of saying so.
#
# `result_status` is a value root, not a scope — the step's status is a scalar, so it is addressed
# whole and correctly carries no field. The other four are scopes and are addressed through one.
# What each storage capability writes on disk. Declared here because a CS states its format only in
# the prose of its configuration schema; nothing machine-readable carries it.
STORE_FORMATS = {
    "CS_MUTABLE_JSON_V0": ".json",
    "CS_REGISTRY_V0": ".jsonl",
    "CS_APPENDONLY_JSONL_V0": ".jsonl",
}

BINDING_ROOTS = ["payload", "inputs", "results", "capability_result", "result_status"]
BINDING_VALUE_ROOTS = ["result_status"]

INTERFACE_RULES: list[Rule] = [
    Rule(
        id="BINDING_STEP_OWNER_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="step_bindings",
        params={
            "column": "Owner",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
        },
        intent="a binding belongs to a workflow or contract this design declared",
    ),
    Rule(
        id="INTERFACE_ARTIFACT_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="interface_fields",
        params={
            "column": "Artifact",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
        },
        intent="a field belongs to an artifact this design declared",
    ),
    Rule(
        id="BINDING_READS_UNPUBLISHED_FIELD",
        check="BINDING_SOURCE_PUBLISHED",
        register="step_bindings",
        params={
            "step_register": "cc_composition",
            "observation": CAPABILITY_OBSERVATION,
        },
        intent="a binding reads a field the operation yields, never one it was hoped would exist",
    ),
    Rule(
        id="STEP_NAMES_UNPUBLISHED_OPERATION",
        check="STEP_OPERATION_PUBLISHED",
        register="cc_composition",
        params={"observation": CAPABILITY_OBSERVATION},
        intent="a step invokes an operation the capability offers, never one it was assumed to have",
    ),
    Rule(
        id="STEP_CONSUMES_UNDECLARED_INPUT",
        check="STEP_CONSUMES_PUBLISHED",
        register="cc_composition",
        params={"observation": CAPABILITY_OBSERVATION},
        intent="a step hands an operation fields it accepts, never ones it was hoped would exist",
    ),
    Rule(
        id="IMPLEMENTATION_WITHOUT_MODULE",
        check="CELL_NOT_EMPTY",
        register="implementation_bindings",
        params={
            "column": "Module",
            # An atom only. A molecule's steps are its specification and it has no module to name;
            # `MOLECULE_DECLARES_IMPLEMENTATION` holds it to that.
            "only_when_column": "Kind",
            "only_when_value": "atom",
            "detail": "transform names no module — an implementation nobody can locate is not designed",
        },
        intent="a declared implementation says where it lives",
    ),
    Rule(
        id="IMPLEMENTATION_WITHOUT_KIND",
        check="CELL_NOT_EMPTY",
        register="implementation_bindings",
        params={
            "column": "Kind",
            "detail": (
                "transform declares no kind — whether it runs an implementation or a stream of "
                "steps decides every other rule this row is held to"
            ),
        },
        intent="a transform says whether it is an atom or a molecule",
    ),
    Rule(
        id="IMPLEMENTATION_KIND_UNKNOWN",
        check="CELL_MATCHES",
        register="implementation_bindings",
        params={
            "column": "Kind",
            "pattern": r"^(atom|molecule)$",
            "detail": (
                "kind is {value!r}; a transform is an atom, which runs an implementation, or a "
                "molecule, which runs its declared steps, and the schema admits nothing else"
            ),
        },
        intent="kind is one of the two the runtime can run",
    ),
    Rule(
        id="IMPLEMENTATION_MODULE_MISPLACED",
        check="IMPLEMENTATION_MODULE_CONFORMS",
        register="implementation_bindings",
        params={
            "code_column": "CT Code",
            "module_column": "Module",
            "namespace_template": "{domain}.implementation.capability_transforms.atoms",
        },
        intent="a transform's module is where its domain resolves implementations, named for the artifact",
    ),
    Rule(
        id="IMPLEMENTATION_WITHOUT_REFUSAL",
        check="CELL_NOT_EMPTY",
        register="implementation_bindings",
        params={
            "column": "Refusal",
            "detail": (
                "transform declares no refusal — whether a judgement is raised or returned is the "
                "one fact that says if a step routing on it can ever fail, and both look the same "
                "from outside"
            ),
        },
        intent="a transform says how it expresses a judgement about its subject",
    ),
    Rule(
        id="IMPLEMENTATION_REFUSAL_UNKNOWN",
        check="CELL_MATCHES",
        register="implementation_bindings",
        params={
            "column": "Refusal",
            "pattern": r"^(raises|returns|never)$",
            "detail": (
                "refusal is {value!r}; a transform raises its judgement, returns it, or makes "
                "none, and the schema admits nothing else"
            ),
        },
        intent="refusal is one of the three the composition can act on",
    ),
    Rule(
        id="INTERPRETATION_TRANSFORM_CANNOT_REFUSE",
        check="INTERPRETATION_TRANSFORM_REFUSES",
        register="cc_composition",
        params={
            "column": "Interpreted By",
            "status_column": "Semantic Status",
            "observation": TRANSFORM_OBSERVATION,
            "design_register": "implementation_bindings",
            "design_code_column": "CT Code",
            "design_refusal_column": "Refusal",
        },
        intent="an interpretation can fail, or the branch it feeds is unreachable",
    ),
    Rule(
        id="IMPLEMENTATION_CALLABLE_UNCONVENTIONAL",
        check="CELL_MATCHES",
        register="implementation_bindings",
        params={
            "column": "Callable",
            "pattern": r"^execute$",
            "detail": (
                "callable is {value!r}; every transform in the composition is entered through "
                "`execute`, and a loader given another name finds nothing"
            ),
        },
        intent="a transform is entered the one way every transform is entered",
    ),
    Rule(
        id="BINDING_WITHOUT_SOURCE",
        check="CELL_NOT_EMPTY",
        register="step_bindings",
        params={
            "column": "Bound To",
            "detail": "field is bound to nothing — construction would have to choose a source",
        },
        intent="every declared input names where its value comes from",
    ),
    Rule(
        id="STORE_PATH_FORMAT_MISMATCH",
        check="STORE_PATH_MATCHES_STORAGE",
        register="structure_stores",
        params={
            "storage_column": "Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0)",
            "path_column": "Proposed Path",
            "formats": STORE_FORMATS,
        },
        intent="a store is named for the format its capability actually writes",
    ),
    Rule(
        id="BINDING_SOURCE_UNROOTED",
        check="BINDING_SOURCE_ROOTED",
        register="step_bindings",
        params={"roots": BINDING_ROOTS, "value_roots": BINDING_VALUE_ROOTS},
        intent="a source that names a place is rooted in one execution scope actually offers",
    ),
    Rule(
        id="NODE_INPUT_UNBOUND",
        check="NODE_INPUT_BOUND",
        register="step_bindings",
        params={
            "topology_register": "execution_topology",
            "fields_register": "interface_fields",
            "observation": CONTRACT_OBSERVATION,
        },
        intent="a workflow hands a contract everything that contract says it requires",
    ),
    Rule(
        id="BINDING_SOURCE_UNREACHABLE",
        check="BINDING_SOURCE_REACHABLE",
        register="step_bindings",
        params={
            "topology_register": "execution_topology",
            # `results.<node>.<field>`, and the same reference inside a composed literal.
            "pattern": r"results\.([A-Za-z][A-Za-z0-9_.:]*?)\.",
        },
        intent="a source that names another node must name one this workflow reaches",
    ),
]



# A composition and its bindings are two halves of one statement, and nothing held them together.
# Each of these caught a defect that passed every other rule at 100% Construction Completeness and
# failed at execution: a step consuming three inputs and binding one, an output written to
# `results.record` where the runtime reads `capability_result.record`, and a contract declaring an
# output no step of it emits.
COMPOSITION_INTEGRITY_RULES: list[Rule] = [
    Rule(
        id="STEP_INTERFACE_NOT_CONFORMANT",
        check="STEP_INTERFACE_CONFORMS",
        register="cc_composition",
        params={"observation": TRANSFORM_OBSERVATION},
        intent="a transform handed an input it does not declare receives nothing under that name",
    ),
    Rule(
        id="STEP_BINDING_NOT_IN_INTERFACE",
        check="STEP_BINDINGS_MATCH_INTERFACE",
        register="step_bindings",
        params={"composition_register": "cc_composition"},
        intent="a binding outside the interface feeds a capability input that does not exist",
    ),
    Rule(
        id="STEP_INPUT_UNBOUND",
        check="STEP_INPUTS_BOUND",
        register="step_bindings",
        params={"composition_register": "cc_composition", "fields_register": "interface_fields"},
        intent="a capability handed no value for an input it declares receives a null",
    ),
    Rule(
        id="BINDING_SOURCE_MALFORMED",
        check="BINDING_SOURCE_WELL_FORMED",
        register="step_bindings",
        params={
            # A step result is addressed by the step that produced it, never bare.
            "output_pattern": r"^(?:capability_result\.[A-Za-z_][A-Za-z0-9_]*|result_status)$",
            "input_pattern": (
                r"^(?:inputs\.[A-Za-z_][A-Za-z0-9_.]*"
                r"|payload\.[A-Za-z_][A-Za-z0-9_.]*"
                r"|results\.[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_.]*"
                r"|[\[{].*[\]}]"
                r"|[A-Za-z_][A-Za-z0-9_]*)$"
            ),
            "detail": (
                "an output is written to capability_result.<field> or result_status; an input "
                "reads inputs.<field>, payload.<field>, results.<step>.<field>, or is a literal"
            ),
        },
        intent="a reference the runtime cannot resolve is indistinguishable from one it can",
    ),
    Rule(
        id="CONTRACT_OUTPUT_UNPRODUCED",
        check="CONTRACT_OUTPUT_PRODUCED",
        register="interface_fields",
        params={"bindings_register": "step_bindings"},
        intent="a declared output no step emits gives every caller a name that resolves to nothing",
    ),
]


# A generator, as construction must be able to reach it: an importable module and the callable
# inside it. A path to a script is not this — the composition imports, it does not shell out, and a
# generator nothing can import is a generator only a person can run.
GENERATOR_PATTERN = r"^[a-z_][a-z0-9_]*(?:\.[a-z_][a-z0-9_]*)*:[a-z_][a-z0-9_]*$"


# Every register above describes what an artifact must *become*. None of them says how it is
# *reached*, and for an artifact nobody types that is the only interesting fact about it: its rules
# live in a template and in code, the artifact carries a sealed copy, and a change meaning to alter
# the rules must alter what generates them. A design with no way to say so cannot be built from — the
# nine phase workflows were designed through six phases and stopped here, because the language they
# exist to govern could not express the one thing that mattered about them.
GENERATION_RULES: list[Rule] = [
    Rule(
        id="GENERATED_ARTIFACT_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="generation_provenance",
        params={
            "column": "Artifact",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
            "detail": (
                "provenance is stated about an artifact this design neither authors nor carries "
                "over — a generator for something nothing schedules produces nothing"
            ),
        },
        intent="provenance belongs to an artifact the design actually declares",
    ),
    Rule(
        id="ARTIFACT_HAS_TWO_GENERATORS",
        check="COLUMN_VALUES_UNIQUE",
        register="generation_provenance",
        params={
            "column": "Artifact",
            "detail": (
                "{value} is generated twice, first at row {first} — an artifact has exactly one "
                "producer, and two producers of one truth drift"
            ),
        },
        intent="one artifact, one producer, so agreement with the generator means something",
    ),
    Rule(
        id="GENERATOR_UNNAMED",
        check="CELL_NOT_EMPTY",
        register="generation_provenance",
        params={
            "column": "Generator",
            "detail": (
                "artifact is declared generated and names no generator — construction has nothing "
                "to invoke and no way to reach it"
            ),
        },
        intent="a generated artifact names what produces it",
    ),
    Rule(
        id="GENERATOR_UNREACHABLE",
        check="CELL_MATCHES",
        register="generation_provenance",
        params={
            "column": "Generator",
            "pattern": GENERATOR_PATTERN,
            "detail": (
                "generator {value!r} must be module:callable — construction imports its generator "
                "and a script it can only shell out to is one nothing governs"
            ),
        },
        intent="a generator is invocable from the composition, not only by a person at a terminal",
    ),
    Rule(
        id="GENERATOR_SOURCES_UNNAMED",
        check="CELL_NOT_EMPTY",
        register="generation_provenance",
        params={
            "column": "Generator Sources",
            "detail": (
                "generator names no sources — a template and the declaration read with it are one "
                "generator, and naming neither permits regenerating from a stale pairing"
            ),
        },
        intent="a generator is its sources together, so a change to either is a change to it",
    ),
]


# The pair of cells that identifies a declared refusal. The seed states it in business language and
# the design answers it in the same words: there is no code for a refusal, and inventing one would
# put a business fact behind an identity only this pipeline can read.
REFUSAL_KEY = ["Operation", "Refused When"]

# Twelve rules across P0 and P1 guard the refusal register's arrival and, until these five, none
# guarded its consequence. A refusal was declared by the business, restated by the change request,
# and then carried unread through six phases into a composition where nothing performed it.
REFUSAL_RULES: list[Rule] = [
    Rule(
        id="REFUSAL_UNACCOUNTED",
        check="PRIOR_ROWS_PRESENT_BY_KEY",
        register="refusal_discharge",
        params={
            "prior_phase": "p0",
            "prior_register": "operation_refusals",
            "prior_key_column": REFUSAL_KEY,
            "key_column": REFUSAL_KEY,
            # Accounted for is discharged, deferred, or refused by the governance surface. Reading
            # one register alone would report the other two as omissions and make them unusable by
            # existing. The three are separate registers because they answer with different facts —
            # a place in the topology, a person and a condition, a rule of the pipeline — and one
            # table holding all three would leave most of its cells empty on every row.
            "registers": ["refusal_discharge", "refusal_deferrals",
                          "refusal_governance_discharge"],
        },
        intent="every refusal the business declared is carried out here or owned by someone else",
    ),
    Rule(
        id="DISCHARGE_UNDECLARED_REFUSAL",
        check="ROWS_CONFINED_TO_PRIOR",
        register="refusal_discharge",
        params={
            "prior_phase": "p0",
            "prior_register": "operation_refusals",
            "prior_key_column": REFUSAL_KEY,
            "key_column": REFUSAL_KEY,
        },
        intent="a discharge answers a refusal the business declared, never one the design invented",
    ),
    Rule(
        id="DEFERRAL_UNDECLARED_REFUSAL",
        check="ROWS_CONFINED_TO_PRIOR",
        register="refusal_deferrals",
        params={
            "prior_phase": "p0",
            "prior_register": "operation_refusals",
            "prior_key_column": REFUSAL_KEY,
            "key_column": REFUSAL_KEY,
        },
        intent="a deferral hands on a refusal the business declared, never one nobody approved",
    ),
    Rule(
        id="DEFERRAL_OWNER_UNNAMED",
        check="CELL_NOT_EMPTY",
        register="refusal_deferrals",
        params={
            "column": "Deferred To",
            "detail": (
                "names no owner — a refusal handed on to nobody is a refusal dropped in language "
                "that sounds like a plan"
            ),
        },
        intent="a deferred refusal names who will carry it out",
    ),
    Rule(
        id="GOVERNANCE_DISCHARGE_UNDECLARED_REFUSAL",
        check="ROWS_CONFINED_TO_PRIOR",
        register="refusal_governance_discharge",
        params={
            "prior_phase": "p0",
            "prior_register": "operation_refusals",
            "prior_key_column": REFUSAL_KEY,
            "key_column": REFUSAL_KEY,
        },
        intent="the governance surface is cited for a refusal the business declared, never for one it did not",
    ),
    Rule(
        id="GOVERNING_RULE_PHASE_MALFORMED",
        check="CELL_MATCHES",
        register="refusal_governance_discharge",
        params={
            "column": "Phase",
            "pattern": r"^p[0-8]$",
            "detail": (
                "{value!r} is not a phase — a rule is named by its phase and its identifier "
                "together, written p0 through p8, because an identifier alone names nine rules"
            ),
        },
        intent="a cited rule is located in the phase whose rule set holds it",
    ),
    Rule(
        id="GOVERNING_RULE_UNNAMED",
        check="CELL_NOT_EMPTY",
        register="refusal_governance_discharge",
        params={
            "column": "Governing Rule",
            "detail": (
                "cites no rule — a refusal said to be carried out by the governance surface and "
                "naming nothing there is prose, and prose refuses nothing"
            ),
        },
        intent="a governance-surface discharge names the rule that refuses",
    ),
    Rule(
        id="GOVERNING_RULE_NOT_IN_FORCE",
        check="GOVERNING_RULE_IN_SEALED_SET",
        register="refusal_governance_discharge",
        params={
            "observation": RULE_SET_OBSERVATION,
            "phase_workflows": _phase_workflows(),
        },
        intent="a rule said to carry out a refusal is really in force where the design is pinned",
    ),
    Rule(
        id="DISCHARGE_NOT_IN_TOPOLOGY",
        check="DISCHARGE_GROUNDED_IN_TOPOLOGY",
        register="refusal_discharge",
        params={},
        intent="a discharge names a step the act has and an outcome that step reports",
    ),
    Rule(
        id="DISCHARGE_DOES_NOT_REFUSE",
        check="DISCHARGE_OUTCOME_REFUSES",
        register="refusal_discharge",
        params={},
        intent="the outcome a discharge names stops the act rather than continuing it",
    ),
]


# An announcement was declared and ungoverned. `multi_emission` gave an act the ability to announce
# several moments at one ending and left open that nothing counted an announcement; six acts then
# announced eight moments and no rule read one. These two are what read them, and they add no
# register: the site is already in `artifact_properties` and the ending is already typed in
# `execution_topology`.
EMISSION_PROPERTY_PREFIX = "emit."

EMISSION_RULES: list[Rule] = [
    Rule(
        id="EMISSION_NOT_FROM_COMPLETING_ENDING",
        check="EMISSION_GROUNDED_IN_ENDING",
        register="artifact_properties",
        params={"property_prefix": EMISSION_PROPERTY_PREFIX, "refusal_property": "moment",
                "refusal_value": "refusal"},
        intent="a moment is announced from an ending the act has, and one that completes it — or, "
               "for a moment declared a refusal, one that refuses it",
    ),
    Rule(
        id="EMITTED_EVENT_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="artifact_properties",
        params={
            "column": "Value",
            "only_when_column": "Property",
            "only_when_prefix": EMISSION_PROPERTY_PREFIX,
            # An announced moment is authored by this design or carried from the composition, and a
            # design that extends an act announces moments it did not author — so both registers
            # answer, exactly as they do for a code assigned at P7.
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
            "detail": "an announced moment must be an identity this design declares",
        },
        intent="an act announces a moment that exists, never one nothing declares",
    ),
]


# A molecule is declared as its steps rather than as an implementation, and the steps are what these
# read. What a molecule may not be — one containing itself, one declared deterministic over a step
# that is not, one emitting a result nothing deterministic consumed — is the compiler's to refuse,
# under the constitutions that govern molecules and non-deterministic atoms; stating it here too
# would be a second authority on the same rule. What only the design can be held to is that the
# steps are stated at all, and stated in a form construction can render without choosing anything.
MOLECULE_SOURCE_PATTERN = (
    r"^(?:inputs\.[A-Za-z_][A-Za-z0-9_.]*"
    r"|results\.[A-Za-z_][A-Za-z0-9_.]*"
    r"|iterator"
    r"|accumulator\.[A-Za-z_][A-Za-z0-9_.]*"
    r"|[\[{].*[\]}]"
    r'|""'
    r"|-?[0-9]+"
    r"|[A-Za-z_][A-Za-z0-9_-]*)$"
)

MOLECULE_RULES: list[Rule] = [
    Rule(
        id="MOLECULE_DECLARES_IMPLEMENTATION",
        check="CELL_MATCHES",
        register="implementation_bindings",
        params={
            "column": "Module",
            "only_when_column": "Kind",
            "only_when_value": "molecule",
            "pattern": r"^(?:—|-)$",
            "detail": (
                "a molecule names module {value!r}; a molecule is run as its declared steps, and a "
                "module beside them is a second account of what it does"
            ),
        },
        intent="a molecule is its steps, never an implementation as well",
    ),
    Rule(
        id="MOLECULE_WITHOUT_STEPS",
        check="REGISTER_COVERS_REGISTER",
        register="molecule_steps",
        params={
            "source_register": "implementation_bindings",
            "source_column": "CT Code",
            "column": "CT Code",
            "only_when_column": "Kind",
            "only_when_value": "molecule",
        },
        intent="a molecule with no declared steps specifies nothing to run",
    ),
    Rule(
        id="MOLECULE_STEP_OWNER_NOT_MOLECULE",
        check="CELL_RESOLVES_IN_REGISTER",
        register="molecule_steps",
        params={
            "column": "CT Code",
            "target_register": "implementation_bindings",
            "target_column": "CT Code",
            "target_only_when_column": "Kind",
            "target_only_when_value": "molecule",
            "detail": "steps belong to a transform this design declares a molecule",
        },
        intent="only a molecule has steps",
    ),
    Rule(
        id="MOLECULE_STEP_KIND_UNKNOWN",
        check="CELL_MATCHES",
        register="molecule_steps",
        params={
            "column": "Kind",
            "pattern": r"^(atom|molecule|loop)$",
            "detail": (
                "step kind is {value!r}; a step runs an atom, a molecule once, or a molecule once "
                "per member of a collection, and the compiler lowers nothing else"
            ),
        },
        intent="a step is one of the three the compiler lowers",
    ),
    Rule(
        id="MOLECULE_STEP_WITHOUT_KIND",
        check="CELL_NOT_EMPTY",
        register="molecule_steps",
        params={"column": "Kind", "detail": "step declares no kind — construction would have to choose how it runs"},
        intent="every step says how it runs",
    ),
    Rule(
        id="MOLECULE_STEP_TARGET_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="molecule_steps",
        params={
            "column": "Target",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
            "detail": "a step runs a transform this design declares or carries over",
        },
        intent="a step runs something that exists",
    ),
    Rule(
        id="MOLECULE_STEP_WITHOUT_TARGET",
        check="CELL_NOT_EMPTY",
        register="molecule_steps",
        params={"column": "Target", "detail": "step runs nothing — construction would have to choose what"},
        intent="every step names the transform it runs",
    ),
    Rule(
        id="MOLECULE_STEP_UNNAMED",
        check="CELL_NOT_EMPTY",
        register="molecule_steps",
        params={
            "column": "Step",
            "detail": "step has no symbol — a result nothing can name is a result no later step can read",
        },
        intent="every step's result has a name later steps read it by",
    ),
    Rule(
        id="LOOP_WITHOUT_COLLECTION",
        check="CELL_NOT_EMPTY",
        register="molecule_steps",
        params={
            "column": "Over",
            "only_when_column": "Kind",
            "only_when_value": "loop",
            "detail": "loop names no collection — its passes would have no stated bound",
        },
        intent="a loop runs once per member of a collection the composition can see",
    ),
    Rule(
        id="LOOP_COLLECTION_UNROOTED",
        check="CELL_MATCHES",
        register="molecule_steps",
        params={
            "column": "Over",
            "only_when_column": "Kind",
            "only_when_value": "loop",
            "pattern": r"^inputs\.[A-Za-z_][A-Za-z0-9_.]*$",
            "detail": (
                "loop runs over {value!r}; a loop's collection is a field the molecule is handed, "
                "inputs.<field>, so its length is fixed before the first pass and never by one"
            ),
        },
        intent="a loop's length never depends on the data it computes",
    ),
    Rule(
        id="LOOP_WITHOUT_ITERATOR",
        check="CELL_NOT_EMPTY",
        register="molecule_steps",
        params={
            "column": "Iterator",
            "only_when_column": "Kind",
            "only_when_value": "loop",
            "detail": "loop names no iterator — its body is handed a member under no name",
        },
        intent="a loop's body receives each member under a declared name",
    ),
    Rule(
        id="LOOP_FIELDS_OUTSIDE_LOOP",
        check="CELL_MATCHES",
        register="molecule_steps",
        params={
            "column": "Over",
            "only_when_column": "Kind",
            "only_when_values": ["atom", "molecule"],
            "pattern": r"^(?:—|-)$",
            "detail": "a step that is not a loop names collection {value!r}, which nothing reads",
        },
        intent="a collection is stated where it bounds something",
    ),
    Rule(
        id="MOLECULE_WITHOUT_EMISSION",
        check="REGISTER_COVERS_REGISTER",
        register="molecule_steps",
        params={
            "source_register": "implementation_bindings",
            "source_column": "CT Code",
            "column": "CT Code",
            "only_when_column": "Kind",
            "only_when_value": "molecule",
            "covered_present_column": "Emits",
        },
        intent="a molecule yields a value, and says which step it comes from",
    ),
    Rule(
        id="MOLECULE_EMITS_TWICE",
        check="COLUMN_VALUES_UNIQUE",
        register="molecule_steps",
        params={
            "column": "CT Code",
            "only_when_present_column": "Emits",
            "detail": (
                "{value} emits a second value, first at row {first} — a molecule yields exactly one, "
                "and two leave a caller to guess which it was handed"
            ),
        },
        intent="a molecule yields exactly one value",
    ),
    Rule(
        id="MOLECULE_BINDING_STEP_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="molecule_step_bindings",
        params={
            "column": "Step",
            "target_register": "molecule_steps",
            "target_column": "Step",
            "detail": "a binding belongs to a step this design declares",
        },
        intent="a binding hands a value to a step that exists",
    ),
    Rule(
        id="MOLECULE_BINDING_WITHOUT_SOURCE",
        check="CELL_NOT_EMPTY",
        register="molecule_step_bindings",
        params={
            "column": "Bound To",
            "detail": "field is bound to nothing — construction would have to choose a source",
        },
        intent="every molecule binding names where its value comes from",
    ),
    Rule(
        id="MOLECULE_BINDING_SOURCE_MALFORMED",
        check="CELL_MATCHES",
        register="molecule_step_bindings",
        params={
            "column": "Bound To",
            "pattern": MOLECULE_SOURCE_PATTERN,
            "detail": (
                "source is {value!r}; a molecule binding reads inputs.<field>, results.<step>.<field>, "
                "iterator, accumulator.<field>, or is a literal"
            ),
        },
        intent="a reference the runtime cannot resolve is indistinguishable from one it can",
    ),
    Rule(
        id="LOOP_UPDATE_NOT_FROM_RESULT",
        check="CELL_MATCHES",
        register="molecule_step_bindings",
        params={
            "column": "Bound To",
            "only_when_column": "Role",
            "only_when_value": "UPDATE",
            "pattern": r"^results\.[A-Za-z_][A-Za-z0-9_.]*$",
            "detail": (
                "a carried value is updated from {value!r}; it is taken from what the pass produced, "
                "results.<field>, or the loop carries forward something no pass computed"
            ),
        },
        intent="what a loop carries forward is what each pass produced",
    ),
]


# A transform's implementation lives outside the composition, so the composition vouches for its
# declaration and never for its code; its cases are the proof, run in its domain's build on every build
# (conformance::CONSTITUTION_TEST_DATA_V2). The build cannot tell a transform authored today from one
# that predates vectors — nothing records when a transform was authored — but the design can: every
# transform authored or amended from now on arrives through one. So the obligation is enforced here.
#
# What a case must say about its transform — outputs it declares, assertion forms, recorded results
# for exactly its non-deterministic steps — is the compiler's to refuse, against the transform as
# sealed. Stating it here too would be a second authority on the same rule.
VECTOR_RULES: list[Rule] = [
    Rule(
        id="TRANSFORM_WITHOUT_VECTOR",
        check="REGISTER_COVERS_REGISTER",
        register="test_cases",
        params={
            "source_register": "new_artifacts",
            "source_column": "Code",
            "column": "CT Code",
            "only_when_column": "Family",
            "only_when_value": "CT",
        },
        intent="a transform authored here enters the composition with its proof",
    ),
    Rule(
        id="AMENDED_TRANSFORM_WITHOUT_VECTOR",
        check="REGISTER_COVERS_REGISTER",
        register="test_cases",
        params={
            "source_register": "existing_inventory",
            "source_column": "FQDN",
            "column": "CT Code",
            "only_when_column": "Action",
            "only_when_value": "EXTEND",
            "only_when_source_pattern": r"^CT_",
        },
        intent="a transform this change amends is proven as it will be",
    ),
    Rule(
        id="TEST_CASE_TRANSFORM_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="test_cases",
        params={
            "column": "CT Code",
            "target_registers": ["new_artifacts", "existing_inventory"],
            "target_column": "Code",
            "target_columns": ["Code", "FQDN"],
            "detail": "a case proves a transform this design declares or carries over",
        },
        intent="a case tests something that exists",
    ),
    Rule(
        id="TEST_CASE_UNNAMED",
        check="CELL_NOT_EMPTY",
        register="test_cases",
        params={"column": "Case", "detail": "case has no name — a failure nothing can name is one nobody can find"},
        intent="every case is named",
    ),
    Rule(
        id="TEST_CASE_NAME_MALFORMED",
        check="CELL_MATCHES",
        register="test_cases",
        params={
            "column": "Case",
            "pattern": r"^[a-z][a-z0-9_]*$",
            "detail": "case is named {value!r}; a case is named in lower case, words joined by underscores",
        },
        intent="a case name is a stable identifier",
    ),
    Rule(
        id="TEST_VALUE_CASE_UNDECLARED",
        check="CELL_RESOLVES_IN_REGISTER",
        register="test_case_values",
        params={
            "column": "Case",
            "target_register": "test_cases",
            "target_column": "Case",
            "detail": "a value belongs to a case this design declares",
        },
        intent="a value is handed to, or expected of, a case that exists",
    ),
    Rule(
        id="TEST_VALUE_WITHOUT_FIELD",
        check="CELL_NOT_EMPTY",
        register="test_case_values",
        params={"column": "Field", "detail": "value names no field — construction would have to choose one"},
        intent="every value names the field it is for",
    ),
    Rule(
        id="TEST_VALUE_EMPTY",
        check="CELL_NOT_EMPTY",
        register="test_case_values",
        params={
            "column": "Value",
            "detail": "value is empty — write the literal, and \"\" for the empty string",
        },
        intent="every value is stated",
    ),
    Rule(
        id="TEST_VALUE_UNPARSEABLE",
        check="CELL_PARSES_AS_YAML",
        register="test_case_values",
        params={
            "column": "Value",
            "detail": "value {value!r} is not a YAML literal ({problem}) — construction would keep it "
                      "as text; quote it if text is meant",
        },
        intent="every value is read as the design wrote it",
    ),
]


def rule_set() -> list[Rule]:
    """P7's rule set: derived, binding discipline, ladder closure, completeness, interface, header."""
    return (
        derived_rules(TEMPLATE)
        + BINDING_RULES
        + LADDER_RULES
        + COMPLETENESS_RULES
        + INTERFACE_RULES
        + COMPOSITION_INTEGRITY_RULES
        + GENERATION_RULES
        + REFUSAL_RULES
        + EMISSION_RULES
        + MOLECULE_RULES
        + VECTOR_RULES
        + event_naming_rules("new_artifacts", "Code")
        + governed_hole_rules()
        + dossier_header_rules()
    )
