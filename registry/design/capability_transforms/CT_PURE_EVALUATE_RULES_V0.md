# CT_PURE_EVALUATE_RULES_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_EVALUATE_RULES_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Apply a declared rule set to parsed registers and report every rule that failed.

**This transform is phase-neutral by design.** Every phase of the pipeline does the same thing to a
different document with a different rule set: parse registers, evaluate declared rules, reach a
verdict. Naming this `..._SEED_RULES_` would have forced each later phase to author its own copy of
the same mechanism — the exact duplication the analysis loop exists to prevent. P1 through P7 reuse
this transform and supply their own rule sets.

It is a **mechanism, not a policy**. It knows how to perform a kind of check — is this cell's value
in a vocabulary, is this column absent, does this token appear anywhere — and nothing about which
register should be checked or why that matters. Reading it tells you how a check runs; it cannot
tell you what is governed. That is declared in the rule set the calling workflow supplies.

`rule_set` is therefore a **declared input**, not embedded content. The rules travel in the calling
workflow's artifact, where they are compiled, sealed, versioned and readable from the composition —
a rule table buried in this transform would be less inspectable than the code it replaced.

Every rule is applied to every document. There is no short-circuit on first failure: an author needs
the whole finding set, and a rule that stops running is a rule that cannot be trusted. An unknown
check kind is a hard failure, never a skipped rule — silently skipping a rule reports green over an
unevaluated subject.

---

## Machine

```yaml
fqdn: transformation::CT_PURE_EVALUATE_RULES_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
core:
  summary: Evaluate a declared rule set against parsed registers
  refusal: returns
  description: |
    Iterates the declared rule set, dispatching each rule to its check kind and collecting findings.
    Raises CTExecutionError on an unknown check kind; the runtime maps any CT exception to
    VIOLATION. A verdict of INADMISSIBLE is a normal return value, not an exception — an
    inadmissible document is a governed outcome, not an execution failure.
  inputs:
    header:
      type: object
      required: true
      description: Header fields as parsed from the document
    sections:
      type: array
      required: true
      description: Parsed document sections
    registers:
      type: array
      required: true
      description: Parsed registers, addressed by marker id — how a rule locates what it governs
    document_text:
      type: string
      required: true
      description: The original document text, for whole-document rules
    rule_set:
      type: array
      required: true
      description: The declared rules deciding admissibility — supplied by the calling workflow
    observed:
      type: object
      required: true
      description: |
        Facts gathered about the composition, keyed by the inspection operation that produced each.
        Empty for a phase that judges a document alone; a phase that grounds claims fills it from a
        governed inspection capability. A rule needing an observation that is absent reports that
        it could not be checked rather than passing silently.
    priors:
      type: object
      required: true
      description: |
        The upstream phase documents this one is judged against, parsed, keyed by phase id. Empty
        for a phase judged on its own document; a phase that preserves an upstream commitment fills
        it from the priors the caller handed over. A cross-phase rule whose prior is absent reports
        that the handoff is unchecked rather than passing silently — an unchecked handoff and a
        preserved one are otherwise indistinguishable.
  outputs:
    verdict:
      type: string
      required: true
      description: ADMISSIBLE when no rule failed, INADMISSIBLE otherwise
    findings:
      type: array
      required: true
      description: One entry per failed rule, naming the rule, where it failed, and why it matters
    rules_evaluated:
      type: integer
      required: true
      description: How many rules were applied — every rule in the set, always
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_EVALUATE_RULES
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_evaluate_rules_v0
    callable: execute
```
