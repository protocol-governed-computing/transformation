# Seed Template V0

The required shape of `0_seed_business_problem_statement.md` — the output of P0 and the only input
P1 accepts.

---

## What a seed is

A seed is the human's business problem statement, faithfully reorganized into governed registers.
P0 reorganizes; it does not decide. Specifically it must **not**:

- add business content the problem statement does not contain
- invent design — no artifact identifiers, no FQDNs, no capability names
- resolve a Clarification by guessing
- promote a System Belief to a Known Fact

Everything the seed asserts must be traceable to a sentence in the problem statement. Everything the
problem statement leaves unsaid becomes a §14 Clarification Request. **Gate 0** is a human
confirming the seed says what they meant.

## The three-way split

The register structure exists to keep three different kinds of statement apart, because the
downstream phases treat them completely differently:

| Register | Nature | Who is authoritative | What P2 does with it |
|---|---|---|---|
| §4 Known Facts | **Business truths** | the human | takes as given |
| §5 System Beliefs | **suspicions about what exists** | nobody yet | verifies against the snapshot |
| §14 Clarifications | **open questions** | unanswered | must ask, never guess |

Collapsing these is the failure P0 exists to prevent. A belief recorded as a fact is never
verified; a question recorded as a fact is answered by invention.

## Header

Four fields, before the first section:

```markdown
- **Domain:** book_library_mgmt
- **Primary subdomain:** catalog — NEW
- **Secondary subdomain:** none
- **CR version:** V0
```

`Domain` and `Primary subdomain` must be lowercase identifiers.

## Sections

| | Section | Shape |
|---|---|---|
| — | Subdomain Purpose | prose |
| 1 | CR Type | prose — exactly one of `NEW_SUBDOMAIN`, `EXTEND_SUBDOMAIN`, `MODIFY`, `DEPRECATE` |
| 2 | Business Vocabulary | table — Term, Definition |
| 3 | Requested Outcomes | prose |
| 4 | Known Facts — Business Truths | table — #, Fact, Certainty |
| 5 | Existing-System Beliefs | table — #, Belief, Why it matters, Verification Goal |
| 6 | Assumptions | table — Assumption, Basis *(may be empty)* |
| 7 | Constraints | table — Constraint, Source *(may be empty)* |
| 8 | Business Invariants | table — #, Invariant |
| 9 | Lifecycle States | table — Object, State, Meaning |
| 10 | Business Events | table — Event, When It Occurs, Significance |
| 11 | Authority Boundaries | table — Business Object, Authoritative Owner |
| 12 | Out of Scope | table — Item, Reason |
| 13 | Governance Scope | table — Scope Item, Relationship |
| 14 | Clarification Requests | prose *(may be `(none)`)* |
| 15 | Acceptance Criteria | prose |

Section titles may carry a trailing annotation (`## 4. Known Facts — Business Truths
(human-authoritative)`); the oracle matches on the prefix.

### Notes on the load-bearing sections

**Subdomain Purpose** is the one irreducible business narrative no compiled artifact can derive:
what this subdomain governs and why it exists. Stated once, at the source, and consumed downstream
rather than rediscovered.

**§5 Existing-System Beliefs** must carry no Certainty column. A certainty rating is what makes a
statement a fact; beliefs carry a *Verification Goal* instead, stating what P2 has to establish.
Every row needs both `Why it matters` (scoping the belief to this CR) and `Verification Goal`.

**§12 Out of Scope** is what makes later CRs governed evolution rather than retrofitted scope. The
business author declaring a deferral here is what lets a later P2 verification distinguish "not yet
built" from "was never intended."

**§13 Governance Scope** relationships: `CREATED`, `EXTENDED`, `MODIFIED`, `DEPRECATED`,
`ADJACENT`.

## The oracle

```bash
tc seed check path/to/0_seed_business_problem_statement.md
tc seed check path/to/seed.md --json
tc seed template
```

Verdict is `ADMISSIBLE` or `INADMISSIBLE` — there is no warning tier. A seed a human must think
about before P1 consumes it is not admissible. Exit 0 admissible, 1 inadmissible.

The oracle is deterministic and reads no snapshot. It judges shape and discipline, never business
correctness: it cannot know whether a Business Truth is true, only whether the seed keeps truths,
beliefs and questions in their proper registers and invents no design.

### Rules

| Rule | Catches |
|---|---|
| `HEADER_FIELD_MISSING` / `HEADER_MALFORMED` | missing or non-identifier header fields |
| `SECTION_MISSING` / `SECTION_MISNUMBERED` / `SECTION_OUT_OF_ORDER` | structural drift from the template |
| `TABLE_MISSING` / `TABLE_COLUMN_MISSING` / `TABLE_EMPTY` | a register that cannot be read as rows |
| `CR_TYPE_NOT_IN_VOCABULARY` / `CR_TYPE_AMBIGUOUS` | no CR type, or more than one |
| `CERTAINTY_NOT_IN_VOCABULARY` | a Known Fact rated outside HIGH/MEDIUM/LOW |
| `BELIEF_CARRIES_CERTAINTY` | §5 given a Certainty column — that would make beliefs facts |
| `BELIEF_WITHOUT_VERIFICATION_GOAL` / `BELIEF_WITHOUT_RATIONALE` | a belief P2 cannot act on |
| `BELIEF_STATED_AS_FACT` | a belief written with the grammar of an assertion |
| `SCOPE_RELATIONSHIP_NOT_IN_VOCABULARY` | an invented governance relationship |
| `DESIGN_LEAKED_INTO_SEED` | a compiled artifact identifier — P0 assigning design |
| `CLARIFICATIONS_UNSTATED` | §14 left blank rather than answered or `(none)` |

## Extending the template

The template is data, in `transformation/seed/template.py`. Adding a section or a controlled
vocabulary term is an edit to that file and nowhere else — including future CR types
(`MERGE_SUBDOMAIN`, `SPLIT_SUBDOMAIN`), which must remain a vocabulary extension rather than a
redesign.
