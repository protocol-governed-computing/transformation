"""The phase catalogue — what each phase is for, and what it may say.

A filename says which phase; it does not say what the phase is *for*. Authoring a dossier means
holding in mind, per phase, the question being answered and the vocabulary admitted — and the
commonest authoring failure is answering the next phase's question early, which the purity ladder
exists to prevent.

Purpose, question and key rule are taken from field manual §4.1; the purity rung from §4.2. They
live here rather than in prose so that `tc phase list` can state them at the moment of authoring,
and so a rule set can key on the rung rather than restating it.

**The purity ladder** (§4.2) — each phase admits exactly one more vocabulary class:

    p1–p4    business language only — nothing new gets a code
    p5       + provisional capability names (IN/WF/CC vocabulary, unbound)
    p6       + placement (WHERE) — still no new codes
    p6b      + binding FQDNs, topology, schemas, stores
    p7       + build order

With one exception at every rung: **an artifact already in the baseline may be cited by exact FQDN
as evidence — citing the baseline is observation, not design.** That exception is why a grounding
register legitimately names artifacts a business register may not, and it is checked by resolving
the identity against the baseline rather than by which column it sits in.
"""

from __future__ import annotations

from dataclasses import dataclass

# Vocabulary classes a phase may introduce, in ladder order. A phase admits its own rung and every
# rung below it.
RUNGS = ("business_language", "provisional_codes", "placement", "binding_fqdns", "build_order")


@dataclass(frozen=True)
class Phase:
    """One phase of the dossier pipeline."""

    id: str
    purpose: str
    question: str
    key_rule: str
    rung: str
    template: str | None = None
    gate: str | None = None

    @property
    def admits(self) -> tuple[str, ...]:
        """Every vocabulary class this phase may use — its rung and all below it."""
        return RUNGS[: RUNGS.index(self.rung) + 1]

    @property
    def may_declare_new_codes(self) -> bool:
        """Whether this phase may introduce an artifact identity that does not yet exist."""
        return self.rung in ("binding_fqdns", "build_order")


PHASES: tuple[Phase, ...] = (
    Phase(
        id="p0",
        purpose="seed",
        question="What does the business want, stated in its own words?",
        key_rule="Faithful rewrite only — no content added, no clarification resolved, no design assigned",
        rung="business_language",
        template=None,  # new in this rehost; no RI-0 original to salvage
        gate="Gate 0 — the human confirms the seed says what they meant",
    ),
    Phase(
        id="p1",
        purpose="change request",
        question="Classification · Problem · Outcome · Known Facts · Deferrals",
        key_rule="Business language only; baseline claims verified against the snapshot, never memory",
        rung="business_language",
        template="p1_change_request_template_v0.md",
    ),
    Phase(
        id="p2",
        purpose="domain model",
        question="Entities · Processes · Baseline fit · Gaps",
        key_rule="Record what was searched, not only what was found",
        rung="business_language",
        template="p2_domain_model_template_v0.md",
    ),
    Phase(
        id="p3",
        purpose="analysis loop",
        question="How is each gap resolved, iterated to Discovery Saturation?",
        key_rule="Every answer carries evidence; overturned answers are marked, never erased",
        rung="business_language",
        template="p3_analysis_loop_template_v0.md",
    ),
    Phase(
        id="p4",
        purpose="business model",
        question="What is the canonical consolidation every later phase projects from?",
        key_rule="Consolidation, not re-litigation",
        rung="business_language",
        template="p4_business_model_template_v0.md",
    ),
    Phase(
        id="p5",
        purpose="business intent",
        question="WHAT — behaviour, objects, identity, invariants, actions",
        key_rule="Provisional capability names are admissible; no bindings, no paths",
        rung="provisional_codes",
        template="p5_business_intent_template_v0.md",
    ),
    Phase(
        id="p6",
        purpose="governance intent",
        question="WHERE — domain and subdomain, ownership, dependencies",
        key_rule="No new artifact codes; cross-subdomain writes forbidden",
        rung="placement",
        template="p6_governance_intent_template_v0.md",
    ),
    Phase(
        id="p6b",
        purpose="design intent",
        question="HOW — FQDNs, topology, schemas, stores, module paths, runtime bindings",
        key_rule="The full dossier is reviewed as a body",
        rung="binding_fqdns",
        template="p6b_design_intent_template_v0.md",
        gate="Gate 1 — Design Approval",
    ),
    Phase(
        id="p7",
        purpose="authoring mandate",
        question="IN WHAT ORDER — topologically sorted build waves",
        key_rule="Mechanical derivation; must reconcile with p6b exactly",
        rung="build_order",
        template="p7_authoring_mandate_template_v0.md",
        gate="Gate 2 — Mandate Approval; the dossier is locked",
    ),
)

PHASES_BY_ID: dict[str, Phase] = {p.id: p for p in PHASES}


def phase(phase_id: str) -> Phase:
    """Look up a declared phase, or fail hard. There is no default."""
    if phase_id not in PHASES_BY_ID:
        raise KeyError(f"no such phase: {phase_id!r}; declared phases are {sorted(PHASES_BY_ID)}")
    return PHASES_BY_ID[phase_id]
