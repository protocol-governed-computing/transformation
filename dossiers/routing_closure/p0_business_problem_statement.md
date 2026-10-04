# Business Problem Statement

**Project Name:** transformation — design

## 1. Context

A phase judges a change document. Six of the nine phases first ask the composition questions about
itself: which artifacts it holds, which stores it declares, what each act composes. Each question goes
to one governed capability, and the phase judges the document against the answers.

That capability can answer in four ways. It can answer, refuse a malformed question, fail to reach the
composition, or report that what was asked about does not exist.

---

## 2. Problem Statement

**A phase that asks the composition a question does not say what happens when the answer is that
the thing does not exist.**

The steps that ask were written answering three of the four ways the capability can answer. The
fourth, that nothing was found, has no answer. The phase workflows were written the same way: they
route a judgement, a refusal and a failed observation, and not the fourth.

This is the gap the design language exists to refuse in the changes it judges. A change whose act
leaves an outcome unanswered is refused at P7. The pipeline that does the refusing has the same gap
in itself.

**And the gap can reopen.** The steps and the routing were each written by hand beside a generator
that already writes the rest of the same artifacts. The next way of answering the capability gains
would again be answered nowhere, until somebody noticed.

This change shall:

- end a phase's judgement as rejected when an observation reports that nothing was found;
- make every way an observation can answer one the phase answers, now and when another is added;
- leave every judgement on an observation that succeeds unchanged.

### What the business already decided

These are settled and are not reopened by this change:

- **A phase either judges a document or rejects it.** There is no third ending.
- **A phase that cannot observe what it judges against does not judge.** It rejects.

---

## 3. Clarifications answered by the business author

- **Should "nothing found" end as rejected, or let the phase judge without the observation?** As
  rejected. A rule judging against an observation that did not arrive would report nothing, and
  nothing is indistinguishable from a pass.
