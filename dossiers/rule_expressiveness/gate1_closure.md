# Gate 1 Closure — rule_expressiveness

**CR:** rule_expressiveness · transformation / design
**Phases completed:** P0 – P6, every one admissible
**Baseline:** `f171afc5277a57958bf498c621fcf02563d5d21e98cbc7e40316d384b4b5248c`

---

## Why this dossier closes at Gate 1

The design is complete and approved. It does not proceed to P7 and P8, and the reason is a property
of the artifacts this change touches rather than of the design.

**P7 requires that an amended artifact be redeclared whole.** Construction renders the amended
artifact from the design alone, and the result replaces its predecessor — so a design stating only
what it adds renders an artifact with everything else deleted, while reporting complete.

**The artifacts this change touches are not authored.** Each phase's rule set is emitted, not typed:
a phase declares its registers in a template and its remaining rules in code, and the workflow
artifact carries a generated copy so the rules can be sealed, versioned and inspected. The largest
of them is 1,707 lines carrying 189 generated rules. Redeclaring one whole in a design register is
not possible — no register has a shape that carries a nested rule set — and an artifact rendered
from such a design would be overwritten by the next emission in any case.

So the delivery path for this change is the one the artifacts already have: amend the declaration,
re-emit, recompile, reassemble. The design that governs it was judged through six phases and is
recorded here.

## What this closure does not concede

The lifecycle governs authored artifacts and has no account of generated ones. That is a gap in the
lifecycle, not a property of this change, and it is opened as its own dossier — `generated_artifacts`
— rather than absorbed here. A change that cannot state how it reaches an artifact is a change whose
delivery is ungoverned, and this one records that plainly rather than passing construction on a
design that could not be built from.

## The approved design, as it will be delivered

| # | Correction | Where it is declared |
|---|---|---|
| 1 | A classification names the subdomain it applies to | The register's column, in the seed and change-request templates |
| 2 | The span of a change is derived from its classifications | Read from those rows; declared nowhere |
| 3 | Every subdomain a change touches has its purpose stated | A rule of the business-intent phase |
| 4 | Every subdomain a change touches has its owner declared | A rule of the governance-intent phase |
| 5 | A dependency may be recorded as existing and altered | The disposition vocabulary of the analysis phase |
| 6 | A rule may constrain how many rows a register has | A way of judging, added and applied to nothing |

## What must hold when it is delivered

Every dossier already judged is re-judged. A verdict that moves for any reason other than these six
corrections is a regression. Five dossiers stand against these phases:

| Dossier | Expectation |
|---|---|
| `blockchain/cr_01_identity` | unchanged |
| `blockchain/cr_02_identity` | unchanged |
| `blockchain/cr_03_identity` | unchanged |
| `blockchain/cr_04_wallet` | **P5 and P6 become inadmissible** — it modifies a subdomain whose purpose is unstated and whose owner is undeclared. This is the acceptance test, not a regression. |
| `transformation/new_subdomain` | unchanged |

The row-count constraint is applied to no register, so no verdict may move because of correction 6.
