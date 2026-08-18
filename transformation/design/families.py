"""The artifact families, declared once.

A family — `WF`, `CC`, `TI` — is named in seven places: two template vocabularies, three regular
expressions across the phase rule sets, and three tables in the renderer. Each was a hand-kept copy
of the same truth, and they had already drifted: the P5 template admitted no `VOCAB` where P7's did,
and neither binding pattern admitted the transport families at all, so a design could not name a
boundary contract even though the composition carries thirty-six of them.

So the list lives here and everything else derives from it. Adding a family is one entry.

**Citable is not authorable.** A binding may name `CS_...` — every capability contract does — but no
change request authors a capability side effect: it is neutral substrate, and a business domain that
wrote one would be adding to the platform under its own namespace. The distinction is declared
rather than implied, because the two sets differ by exactly that one family and a reader guessing
from a single list would guess wrong.

**Renderable is narrower still.** A family is renderable when construction has a builder for it. A
family declared here and unbuilt is reported by `render.unrenderable` and measured as undetermined,
which is what makes the gap visible instead of silent.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Family:
    """One artifact family: what it compiles to, what governs it, and where it is written."""

    code: str
    artifact_kind: str
    constitution: str
    directory: str
    # Whether a change request may author one. False for the neutral substrate a domain binds but
    # never writes.
    authorable: bool = True


FAMILIES: tuple[Family, ...] = (
    Family("AC", "ACTOR", "fb.governance::CONSTITUTION_GOVERNANCE_V0", "actors"),
    Family("IN", "INTENT", "fb.intent::CONSTITUTION_INTENT_V0", "intents"),
    Family("WF", "WORKFLOW", "fb.workflow::CONSTITUTION_WORKFLOW_V0", "workflows"),
    Family("CC", "CAPABILITY_CONTRACT",
           "fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0", "capability_contracts"),
    Family("CT", "CAPABILITY_TRANSFORM",
           "fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0",
           "capability_transforms"),
    Family("CS", "CAPABILITY_SIDE_EFFECT",
           "fb.capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0",
           "capability_side_effects", authorable=False),
    Family("RB", "RUNTIME_BINDING",
           "fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0", "runtime_bindings"),
    Family("EV", "EVENT", "fb.event::CONSTITUTION_EVENT_V0", "events"),
    Family("VOCAB", "VOCABULARY", "fb.vocabulary::CONSTITUTION_VOCABULARY_V0", "vocabulary"),
    Family("STRUCTURE", "STRUCTURE", "fb.structure::CONSTITUTION_STRUCTURE_V0", "layers"),
    Family("TI", "TRANSPORT_INGRESS",
           "fb.transport::CONSTITUTION_TRANSPORT_INGRESS_V0", "transport"),
    Family("TE", "TRANSPORT_EGRESS",
           "fb.transport::CONSTITUTION_TRANSPORT_EGRESS_V0", "transport/egress"),
)

BY_CODE: dict[str, Family] = {family.code: family for family in FAMILIES}

# Longest first, so `STRUCTURE` is matched before nothing and `TI` never shadows a longer code.
CITABLE: tuple[str, ...] = tuple(sorted(BY_CODE, key=len, reverse=True))
AUTHORABLE: tuple[str, ...] = tuple(
    sorted((f.code for f in FAMILIES if f.authorable), key=len, reverse=True)
)


def alternation(codes: tuple[str, ...]) -> str:
    """The regex alternation for a set of families, longest-first so no code shadows a longer one."""
    return "|".join(codes)


def binding_fqdn_pattern() -> str:
    """A fully-qualified identity a binding may name. Every citable family, substrate included."""
    return r"^[a-z][a-z0-9_.]*::(?:" + alternation(CITABLE) + r")_[A-Z0-9_]+_V\d+$"


def artifact_token_pattern() -> str:
    """A bare artifact code anywhere in prose — what a business-language cell must not contain."""
    return r"\b(?:" + alternation(CITABLE) + r")_[A-Z0-9_]+_V\d+\b"


def authorable_fqdn_pattern() -> str:
    """An identity a design may amend: one whose family the renderer can build.

    A design amends an artifact by re-rendering it whole, so it may only amend what it could have
    authored. A constitution, an invariant and a schema have no family here and no builder there —
    the governance surface is authored by a person under a governed dossier, and the pipeline's
    authority over it ends at P6. Citing one is untouched; scheduling one to be rewritten from
    registers that never held its content is what this refuses.
    """
    return r"^[a-z][a-z0-9_.]*::(?:" + alternation(AUTHORABLE) + r")_[A-Z0-9_]+_V\d+$"
