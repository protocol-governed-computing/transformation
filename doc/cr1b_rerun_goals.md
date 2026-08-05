The first CR-1 answered **\"Can we invent a language that is expressive enough?\"** The rerun should answer a different question:

**\"Can an engineer who knows the business, but not the implementation details, naturally drive the language to a complete design?\"**

Those are very different validations.

I would actually elevate this into a first-class design principle for the Design Compiler.

**The inversion**

The first CR-1 naturally worked like this:

Human

↓

AI inferred

↓

Pipeline accepted

The rerun should deliberately invert it:

Human provides business knowledge

↓

AI asks for missing business knowledge

↓

AI derives everything that is mechanically derivable

↓

Pipeline judges

Notice the subtle change.

The AI is no longer primarily a producer.

It becomes a **knowledge elicitor**.

That is a much more valuable role.

**The two information classes**

I think you\'ve identified exactly the right distinction.

**Type A --- Derivable facts**

These should never be asked of the human.

Examples

- existing artifact identities

- namespaces

- existing workflows

- existing actors

- baseline graph

- reusable capabilities

- existing stores

- vocabulary already present

- dependency graph

- snapshot metadata

- compiler version

- graph hashes

- existing contracts

These are observations.

The AI should obtain them from the baseline snapshot.

The human should never have to remember them.

**Type B --- Human knowledge**

Only the business owner can answer these.

Examples

Why?

When?

Priority?

Business intent?

Success criteria?

Tradeoffs?

Policies?

Expected behavior?

Business terminology?

Domain language?

Acceptance criteria?

Future direction?

Non-functional priorities?

Out-of-scope decisions?

Those are not derivable.

Those are exactly where the human adds value.

I would actually formalize this.

Information Source

OBSERVED

snapshot

DERIVED

compiler

PROVIDED

human

GENERATED

deterministic projection

That is a clean ontology.

**AI should become a Socratic interviewer**

Instead of this

Human:

Need a catalog.

AI:

I\'ll assume\...

I\'ll infer\...

I\'ll create\...

It should become

Human:

Need a catalog.

AI:

I already know:

✓ existing domains

✓ baseline

✓ reusable capabilities

What I do NOT know:

1\.

Who may register books?

2\.

Can books be edited?

3\.

Can books be deleted?

4\.

What uniquely identifies a book?

5\.

What should happen if duplicate?

6\.

What is considered success?

Notice something.

Those are all value questions.

Not implementation questions.

**This changes the Figure of Merit**

Today the star system measures document quality.

I think it should also measure **knowledge provenance.**

For example

Knowledge Provenance

Observed

65%

Human supplied

28%

Compiler derived

7%

AI inferred

0%

That last number is interesting.

Your goal should almost be

AI inferred

0%

Not because AI is weak.

Because inference is risk.

If AI had to invent something\...

\...the dossier wasn\'t complete.

**New merit dimension**

Today

★★★★★

identity

coverage

holes

handoff

I would add

Inference debt

or

Assumption debt

Every time AI must invent something

−1

or

AI_INFERENCE_REQUIRED

That becomes a measurable quality.

Eventually

★★★★★

0 inferred facts

becomes an achievement.

**Pipeline improvement**

The rerun shouldn\'t only produce documents.

It should improve the compiler.

For every clarification question asked, ask:

\"Why did the AI have to ask this?\"

Possible answers:

**Missing template field**

Template defect

**Missing rule**

Compiler defect

**Missing register**

Language defect

**Human simply forgot**

Authoring defect

Only the last one is not a platform issue.

Everything else should feed back into the language.

That is exactly how CR-1 evolved.

**Human contribution should taper**

I like your observation.

The expected curve should look like this:

P0

██████████████████ Human

P1

███████████████

P2

██████████

P3

██████

P4

████

P5

███

P6

██

P7

█

P8

almost none

Construction

none

The farther down the pipeline, the less new human information should be entering.

By P7 the design should simply be becoming increasingly determined.

By Construction there should be zero human contribution.

**I would add one more explicit objective**

I think the rerun should have four goals, not three.

1.  Validate that a human can successfully drive the pipeline from scratch.

2.  Maximize human contribution where only humans can add value, while minimizing AI inference.

3.  Every clarification question should either:

    - improve the language,

    - improve a template,

    - improve a rule,

    - or expose a true business ambiguity.

4.  Measure the pipeline itself.

After the rerun you should be able to produce something like:

  ---------------------------------------------
  **Metric**                       **Value**
  -------------------------------- ------------
  Human clarifications requested   41

  Snapshot-derived facts           126

  AI assumptions                   2

  New template fields discovered   5

  New rules added                  8

  Figure-of-Merit improvement      +0.6 stars
  ---------------------------------------------

That becomes evidence that the **Design Compiler language is converging**. Eventually, successive reruns should require fewer clarification questions and fewer language changes while maintaining zero AI assumptions. That is a much stronger measure of maturity than simply reproducing CR-1.
