# Business Problem Statement — the phase pipeline

The platform governs how business capability enters a composition: every artifact is declared,
compiled, sealed, and inspectable. One thing escapes that discipline — the pipeline that decides
which changes are admissible in the first place. Its rules live in a build tool rather than in the
composition, so the platform cannot answer "what governs a change request?" from its own contents.

We require the change pipeline to be governed the same way everything else is. Each phase of the
pipeline should be a declared capability of the platform: what it consumes, what it produces, which
rules decide admissibility, and who is accountable at each gate.

The first phase to establish is the seed phase. It takes a business problem statement written by a
person and produces a conformant seed — the same content, reorganized into fixed registers that
later phases read. A seed is either admissible or it is not; there is no partial pass. The phase
must decide that by applying a declared rule set, and must report every rule it failed rather than
stopping at the first.

The rules that decide admissibility are governance, not implementation detail. They must be
readable from the composition, versioned like any other declared behavior, and changeable only
through the same governed change process. A mechanism that merely knows how to perform a check is
implementation and may live in code; what is being checked, and why it matters, may not.

The seed phase must also record accountability. A person is the author of record for a seed, and a
person confirms at the gate that the seed says what they meant. Today that is convention. It should
be a declared property of the pipeline.

The phase reorganizes; it never decides. It may not add business content the problem statement does
not contain, resolve an open question by guessing, assign any design, or promote something believed
about the existing system into something asserted as fact. Those distinctions are what later phases
depend on, and collapsing them is the failure this phase exists to prevent.

This change establishes the seed phase and its rule set only. The remaining phases, the workers that
might draft a seed, and any reachability beyond a local command line are intentionally excluded, and
are expected to arrive through later governed change requests rather than being designed in now.

## Clarifications answered by the business author

The following business questions were put to the business author and answered by them. They were not
assumed by the design process.

- **In what form is the rule set carried as declared data?** Sealed inside the phase's own compiled
  artifact, alongside the workflow that applies it. The business wants one thing to version, one
  thing to inspect and one thing to review: a rule set held apart from the phase it governs is a
  second thing that can be changed without the phase changing, which is the drift the requirement
  that rules be readable from the composition exists to stop. The copy is generated from the
  declaration, never typed, and the two are compared on every run.
- **Does the phase receive the seed as text, or as a location it must read?** As text. The whole
  document travels with the request. A verdict must be reproducible from what was judged, and a
  phase handed a location judges whatever that location holds at the moment it looks — which is not
  the same document twice, and makes a recorded verdict evidence of nothing.

