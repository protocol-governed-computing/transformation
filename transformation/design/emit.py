"""The generator behind every phase workflow — its sealed rule set, and the provenance saying so.

A phase declares its rules once, in `transformation/design/pN_*/rules.py`, over the registers its
template declares. The compiled workflow carries a *copy* of that declaration, because the rules
travel in the artifact where they can be sealed, versioned and inspected. Two copies of one truth
drift, and this one drifted silently: adding a rule after emitting a workflow left 52 rules sealed
against 55 declared, and every run reported confidently on the smaller set.

So the copy is generated, never typed, and this module is the generator. **A template and the
declaration read with it are one generator** — neither determines the artifact alone, and naming
either separately would permit regenerating from a stale pairing.

Two things are emitted into each workflow, and they answer different questions. The `rule_set:`
block is what the phase judges by. The `## Generated Artifact` section is what the artifact says
about itself: that it is generated, by what, and from which sources. Provenance belongs to the
artifact rather than to a list beside it, because a second statement of one truth can disagree with
the thing it describes.

**The generator is authoritative.** Where a workflow and this module disagree, the workflow is
stale — a disagreement is not a difference of opinion. Correcting the artifact would leave the
generator still producing the old value, so the fix would last until whoever next ran the emission.
`check()` is what makes that enforceable rather than merely stated.

This lives inside the package rather than under `scripts/` because construction must be able to
*invoke* it: a generated artifact is reached by invoking its generator, and a generator only a
person at a terminal can run is one nothing governs. `scripts/emit_rule_sets.py` remains as the
terminal's way in.
"""

from __future__ import annotations

from dataclasses import dataclass
import pathlib
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WORKFLOWS = REPO / "registry" / "design" / "workflows"

# phase id → the workflow artifact carrying its sealed rule set.
SEALED_IN = {
    "p0": "WF_P0_SEED_ADMISSIBILITY_V0.md",
    "p1": "WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0.md",
    "p2": "WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0.md",
    "p3": "WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0.md",
    "p4": "WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0.md",
    "p5": "WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0.md",
    "p6": "WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0.md",
    "p7": "WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0.md",
    "p8": "WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0.md",
}

# How a design names this generator, and how construction reaches it. One spelling, read by the
# provenance the artifacts carry and by the register a design states — the same string in both, or
# the agreement check compares a design against a generator it did not name.
GENERATOR = "transformation.design.emit:emit_rule_sets"

def workflow_fqdn(phase_id: str) -> str:
    """The identity of the artifact carrying a phase's sealed rule set.

    Derived from the one map above rather than restated, because a second spelling of which workflow
    belongs to which phase is a second thing to get wrong — and the thing it would get wrong is which
    rules a document is judged by.
    """
    return f"transformation::{SEALED_IN[phase_id][:-len('.md')]}"


RULE_SET_INDENT = 8

# The contract every phase workflow invokes, and the one place a phase's observations are handed to
# the evaluator. Its `observed` map was hand-authored while `OBSERVATIONS` declared the same thing in
# Python, and the two drifted exactly as two copies of one truth do: the map passed two keys where
# four were declared, so a rule reading the transform surface found nothing and returned nothing, and
# had been doing so through the compiled path since it was written.
JUDGE_CONTRACT = "registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V0.md"
CONTRACTS = REPO / "registry" / "design" / "capability_contracts"

OBSERVED_INDENT = 6

# The step that reads every observation, and therefore the one every observing step must precede.
# Named once: the emission places steps relative to it, and a second spelling would place them
# somewhere the runtime has already passed.
OBSERVATION_CONSUMER = "evaluate_rules"

PROVENANCE_HEADING = "## Generated Artifact"

# The section is placed where a reader meets the artifact, before its narrative begins. Every one of
# these workflows opens the same way, and an anchor that is not there is fail-hard rather than a
# section quietly appended somewhere nobody looks.
PROVENANCE_ANCHOR = "## 1. Intent"


def observations() -> dict[str, str]:
    """Every observation any phase declares, as `key -> the field its result carries`.

    The union across phases, because one contract judges all of them and its pipeline observes the
    same operations whatever phase invoked it. A phase that does not read a key is handed it and
    ignores it, which costs nothing; a phase that reads a key nobody passed is the defect this
    exists to prevent.
    """
    from transformation.design.meta import RULE_MODULES

    out: dict[str, str] = {}
    for module in RULE_MODULES.values():
        for key, field in (getattr(module, "OBSERVATIONS", {}) or {}).items():
            out[key] = field
    return dict(sorted(out.items()))


def observing_steps(text: str) -> dict[str, str]:
    """`operation -> the step that performs it`, read out of the contract's own pipeline.

    Derived rather than declared here. Which step observes which operation is a fact the contract
    already states, and restating it would create the second copy this whole change is removing.
    """
    steps: dict[str, str] = {}
    current = ""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- step: "):
            current = stripped[len("- step: "):].strip()
        elif stripped.startswith("operation: ") and current:
            steps[stripped[len("operation: "):].strip()] = current
    return steps


def render_observed(text: str) -> str:
    """The `observed` map as the contract carries it, one line per declared observation."""
    steps = observing_steps(text)
    pad = " " * OBSERVED_INDENT
    lines = [f"{pad}observed:\n"]
    for key, field in observations().items():
        operation = key.split("#", 1)[0]
        step = steps.get(operation)
        if step is None:
            raise SystemExit(
                f"{JUDGE_CONTRACT} observes no {operation!r}, which a phase declares it reads. "
                f"A key nobody produces is a rule that cannot see its subject"
            )
        lines.append(f"{pad}  {key}: $.results.{step}.capability_result.result.{field}\n")
    return "".join(lines)


def step_name(operation: str) -> str:
    """The step that performs an operation, named from the operation itself.

    Derived so that adding an observation is one line in a phase's rule module. Naming the step by
    hand would put the operation in the declaration and the step in the contract, which is the pair
    that has to be kept in step — the same pair the `observed` map was generated to stop copying.
    """
    return "observe_" + operation.split("#", 1)[0].replace("si.", "", 1).replace(".", "_")


def render_observing_step(operation: str) -> str:
    """One pipeline step asking the bound snapshot capability one question.

    The step is the last hand-kept copy of a declaration that already lives in a phase's rule
    module. Generated, an observation a phase declares reaches the rules that read it; hand-written,
    the emission could only report that it was missing — which it did, correctly, and then left
    somebody to write the step themselves.
    """
    return (
        f"  - step: {step_name(operation)}\n"
        f"    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0\n"
        f"    op: QUERY\n"
        f"    inputs:\n"
        f"      operation: {operation}\n"
        f"      params: {{}}\n"
        f"    outputs: {{}}\n"
        f"    result_surface:\n"
        f"    - SUCCESS\n"
        f"    - VIOLATION\n"
        f"    - BACKEND_ERROR\n"
        f"    on_result:\n"
        f"      SUCCESS: continue\n"
        f"      VIOLATION: exit\n"
        f"      BACKEND_ERROR: exit\n"
    )


def splice_observing_steps(text: str) -> str:
    """Place a step for every declared observation the contract does not already perform.

    Inserted before the step that reads them, because the runtime chains by result and a step
    consuming an observation produced after it reads nothing. Only the missing ones are written: a
    step already there is the contract's own, and regenerating it would discard whatever a reviewer
    put in its comments.
    """
    have = observing_steps(text)
    missing = [op for op in sorted({k.split("#", 1)[0] for k in observations()})
               if op not in have]
    if not missing:
        return text
    lines = text.splitlines(keepends=True)
    anchor = [i for i, line in enumerate(lines)
              if line.rstrip("\n") == f"  - step: {OBSERVATION_CONSUMER}"]
    if len(anchor) != 1:
        raise SystemExit(
            f"expected exactly one {OBSERVATION_CONSUMER!r} step in {JUDGE_CONTRACT} to place an "
            f"observing step before, found {len(anchor)}"
        )
    at = anchor[0]
    return "".join(lines[:at]) + "".join(render_observing_step(op) for op in missing) \
        + "".join(lines[at:])


def splice_observed(text: str, rendered: str) -> str:
    """Replace the `observed:` block, leaving the rest of the contract untouched."""
    lines = text.splitlines(keepends=True)
    key = " " * OBSERVED_INDENT + "observed:"
    starts = [i for i, line in enumerate(lines) if line.rstrip("\n") == key]
    if len(starts) != 1:
        raise SystemExit(f"expected exactly one {key!r} line, found {len(starts)}")
    start = starts[0]

    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].lstrip()
        if not stripped:
            continue
        if len(lines[i]) - len(stripped) <= OBSERVED_INDENT:
            end = i
            break
    return "".join(lines[:start]) + rendered + "".join(lines[end:])


@dataclass(frozen=True)
class Emission:
    """What one workflow's generation produced, and whether it had drifted."""

    phase: str
    filename: str
    rules: int
    drifted: bool


def sources(phase_id: str) -> list[str]:
    """Everything the emission reads for one phase, as repo-relative paths.

    The template declares the registers and their columns; the rule module declares what remains.
    Both, together, are the generator — so both are named, and a change to either is a change to it.
    P0 has no vendored template, being new in this rehost, so its declaration is the whole of it.
    """
    from transformation.design.catalog import phase as phase_spec
    from transformation.design.meta import RULE_MODULES

    out = []
    template = phase_spec(phase_id).template
    if template:
        out.append(f"templates/{template}")
    module_file = Path(RULE_MODULES[phase_id].__file__).resolve()
    out.append(str(module_file.relative_to(REPO)))
    return out


def declared(phase_id: str) -> list[dict]:
    """A phase's rule set as the plain data a workflow seals.

    Both locators are emitted when a rule declares a register. `section_title` alone unbinds a
    derived rule from the register it was derived for, and `register` alone loses the fallback P0
    depends on — the failure mode is a rule that resolves to nothing and passes silently.
    """
    from transformation.design.meta import RULE_MODULES

    out = []
    for rule in RULE_MODULES[phase_id].rule_set():
        entry: dict = {"id": rule.id, "check": rule.check}
        if rule.register:
            entry["register"] = rule.register
        if rule.section_title and rule.section_title != rule.register:
            entry["section_title"] = rule.section_title
        if rule.params:
            entry["params"] = rule.params
        if rule.intent:
            entry["intent"] = rule.intent
        out.append(entry)
    return out


def render(rules: list[dict]) -> str:
    """The rule set as it appears inside the workflow's `Machine` block.

    Dumped with aliases left on: several phases repeat one large `known_registers` list across
    dozens of rules, and expanding it every time would bury the declaration in its own boilerplate.
    """
    body = yaml.dump(rules, sort_keys=False, width=100, allow_unicode=True, default_flow_style=False)
    pad = " " * RULE_SET_INDENT
    return "".join(f"{pad}{line}\n" if line.strip() else "\n" for line in body.splitlines())


def splice(text: str, rendered: str) -> str:
    """Replace the `rule_set:` block in a workflow artifact, leaving everything else untouched.

    The block runs from its key to the next line indented shallower than the key — the node's
    `next:` routing. Rewriting the whole YAML document instead would reformat hand-written
    structure and strip the comments that explain it.
    """
    lines = text.splitlines(keepends=True)
    key = " " * RULE_SET_INDENT + "rule_set:"
    starts = [i for i, line in enumerate(lines) if line.rstrip("\n") == key]
    if len(starts) != 1:
        raise SystemExit(f"expected exactly one {key!r} line, found {len(starts)}")
    start = starts[0]

    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].lstrip()
        if not stripped:
            continue
        if len(lines[i]) - len(stripped) < RULE_SET_INDENT:
            end = i
            break

    return "".join(lines[:start + 1]) + rendered + "".join(lines[end:])


def provenance(phase_id: str) -> str:
    """What the artifact says about how it was reached.

    Prose, deliberately: the compiler reads the `## Machine` block and nothing else, so this states
    the fact to the person who opens the file and to the review that would otherwise have to take
    the generator's word for it. It is emitted rather than typed for the same reason the rule set
    is — a hand-written provenance is a third copy, and the one nobody regenerates.
    """
    listed = "\n".join(f"  - `{path}`" for path in sources(phase_id))
    return (
        f"{PROVENANCE_HEADING}\n"
        "\n"
        "This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and\n"
        "the copy is never corrected directly: where this artifact and its generator disagree, this\n"
        "artifact is stale, and an edit here lasts until whoever next runs the emission.\n"
        "\n"
        f"- **Generator:** `{GENERATOR}`\n"
        "- **Generator sources** — one generator together, never separately:\n"
        f"{listed}\n"
        "\n"
        "To change what this phase judges, amend a source and invoke the generator.\n"
        "`tc phase emit --check` refuses a build in which the two disagree.\n"
        "\n"
        "---\n"
        "\n"
    )


def splice_provenance(text: str, block: str) -> str:
    """Place the provenance section, replacing any the artifact already carries.

    Replacing rather than appending is what keeps this idempotent — an emission that added a second
    section every run would produce exactly the two-statements-of-one-truth this section exists to
    refuse.
    """
    lines = text.splitlines(keepends=True)
    heads = [i for i, line in enumerate(lines) if line.rstrip("\n") == PROVENANCE_HEADING]

    if heads:
        start = heads[0]
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        return "".join(lines[:start]) + block + "".join(lines[end:])

    anchors = [i for i, line in enumerate(lines) if line.rstrip("\n") == PROVENANCE_ANCHOR]
    if not anchors:
        raise SystemExit(f"expected {PROVENANCE_ANCHOR!r} to place the provenance section before")
    at = anchors[0]
    return "".join(lines[:at]) + block + "".join(lines[at:])


def emit_contract(check_only: bool = False) -> Emission:
    """Bring the judging contract's `observed` map into agreement with what the phases declare.

    The map is generated for the same reason the rule sets are: it is a copy of a declaration that
    lives elsewhere, and the two drifted the moment anyone added an observation. Generated, adding
    one to a phase is enough — and an observation no step produces is a build failure rather than a
    rule that silently sees nothing.
    """
    path = REPO / JUDGE_CONTRACT
    current = path.read_text(encoding="utf-8")
    stepped = splice_observing_steps(current)
    updated = splice_observed(stepped, render_observed(stepped))
    drifted = updated != current
    if drifted and not check_only:
        path.write_text(updated, encoding="utf-8")
    return Emission(phase="cc", filename=pathlib.Path(JUDGE_CONTRACT).name,
                    rules=len(observations()), drifted=drifted)


def emit(check_only: bool = False) -> list[Emission]:
    """Bring every phase workflow into agreement with what its phase declares.

    Under `check_only` nothing is written and the drift is reported instead, which is what a build
    gate needs: the question "does the composition already agree with its generator" has to be
    answerable without changing the answer.
    """
    out: list[Emission] = []
    for phase_id, filename in SEALED_IN.items():
        path = WORKFLOWS / filename
        rules = declared(phase_id)
        current = path.read_text(encoding="utf-8")
        updated = splice_provenance(splice(current, render(rules)), provenance(phase_id))
        drifted = updated != current
        if drifted and not check_only:
            path.write_text(updated, encoding="utf-8")
        out.append(Emission(phase=phase_id, filename=filename, rules=len(rules), drifted=drifted))
    out.append(emit_contract(check_only))
    return out


def emit_rule_sets() -> list[Emission]:
    """The generator, as a design names it and as construction invokes it."""
    return emit(check_only=False)


def check() -> list[Emission]:
    """Every workflow that does not agree with its generator. Empty is the only passing answer."""
    return [e for e in emit(check_only=True) if e.drifted]
