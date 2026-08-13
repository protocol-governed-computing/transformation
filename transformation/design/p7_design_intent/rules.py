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

OBSERVATIONS = {
    OBSERVATION_OPERATION: "artifacts",
    CAPABILITY_OBSERVATION: "capabilities",
    TRANSFORM_OBSERVATION: "transforms",
    CONTRACT_OBSERVATION: "contracts",
    STORE_OBSERVATION: "stores",
}

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
    # is in `doc/THE_SHAPE_OF_A_CHANGE_V0.md` §7. Citing one of these is untouched; three dossiers
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
            "detail": "transform names no module — an implementation nobody can locate is not designed",
        },
        intent="a declared implementation says where it lives",
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
        + event_naming_rules("new_artifacts", "Code")
        + governed_hole_rules()
        + dossier_header_rules()
    )
