# Business Problem Statement — the transformation pipeline

The platform governs how business capability enters a composition: every artifact is declared,
compiled, sealed and inspectable. The pipeline that decides whether a change to a composition may
proceed, and that turns an approved design into the artifacts it describes, must be governed the same
way. Its rules must be readable from the composition, so the platform can answer "what governs a
change?" from its own contents and an independent implementation needs no code to read them.

A change is carried in nine phases, from a problem statement a person writes to a mandate that
schedules the artifacts to build. Each phase takes one document, judges it against the rules declared
for that phase, and returns a verdict: admissible or inadmissible. A verdict reports every rule the
document failed, never only the first, and says for each where it failed and why the rule exists. The
same document judged by the same rules always gets the same verdict.

The first phase reorganizes a person's problem statement into a seed and never decides anything. It
adds no business content, resolves no open question by guessing, assigns no design, and never treats
a belief about the existing system as a fact. Later phases verify beliefs against the composition the
change is designed against, consolidate the business model, state what the change does, place it, and
design it. The last phase orders the build.

The rules that decide admissibility are governance, not implementation. Each is declared once,
versioned, and changed only through a governed change. A mechanism that knows how to perform a kind
of check may live in code; what is checked, and why it matters, may not.

Construction turns an approved mandate into the artifacts it schedules. It writes only what the
design states or what a governing artifact fixes, and reports how much of each artifact the design
determined. A value construction would have to invent is a defect in the design, never a value to
supply.

People are accountable at the gates. The person who writes a problem statement is its author of
record. A person confirms the seed says what they meant, approves the design, and approves the
mandate. Nothing is built that a person did not approve, and nothing a person approved is changed
without a new approval.

The pipeline is a build-time tool. It runs before a composition exists, its readers are the people
driving a change, and it is not reachable from outside. It reads the composition only through the
platform's inspection capability.

This change describes the pipeline as it stands: the nine phases and their rules, construction, and
the people who author and approve. Workers that draft documents, any reachability beyond a local
command line, and a governed step that generates documents are excluded, and are expected to arrive
through later governed changes.
