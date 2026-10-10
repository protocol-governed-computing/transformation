# Transformation Rebuild — Charter

This charter replaces the delivery plan of `TRANSFORMATION_UNRAVEL.md` §10. The analysis in that
document stands, and becomes the specification of the rebuild.

---

## 1. Why a rebuild

The unravel was planned as five changes, each a dossier judged by the transformation lifecycle.
That plan oscillates instead of progressing.

- **The tool judges its own redesign.** Each defect in the tool blocks the dossier that would fix
  it. The fix must run first as a dossier of its own, and it can hit the next defect.
- **The chain only grew.** Five dossiers were opened. Two were delivered as fixes
  (`binding_literals`, `quoted_literals`). `register_format` is parked behind `version_retirement`,
  and that is blocked by a platform invariant. None of the five reached the target.
- **Succession costs most during development.** Every replacement carried its predecessor, and the
  carried versions then blocked the next change. Development has no consumer of the live tree to
  protect.

The target has not changed: rules visible without reading code, one design language, no
force-fitted concepts.

## 2. The decision

Freeze the current transformation module. It becomes the **oracle**. Rebuild the module on a branch,
designed once from everything the unravel learned. Replace the old module whole when the rebuild
meets the oracle.

This is a rebuild against a fixed oracle, not greenfield. Evolution is never greenfield. The frozen
module and the composition it produced are the baseline the rebuild is measured against.

## 3. The oracle

- The transformation repository, at the checkpoint commit on `dev/18`, tagged `oracle/transformation`.
- The working composition built from that commit, with its regression at 71/71.
- From the tag until the swap, `dev/18` takes no change to transformation except one that the rest
  of the workspace needs to stay green. Each such change is applied on the branch as well.

## 4. Scope

**In scope.** The five changes of the unravel, designed as one:

1. **Format.** Registers carried as a structured block apart from the prose (§9.9). One form, with
   no reading of tables.
2. **Structure.** Values inside cells given structure: routing, bindings, literals and generated
   values (§9.9, and the obligations in §9).
3. **Design unravel.** Rules declared as artifacts, not code (§3, §6):
   - transformation invariants under a transformation constitution;
   - a register schema per phase;
   - each expanded rule identified by schema `$id` and JSON Pointer (§9.2);
   - findings with structured locators (§4.6);
   - `rules.py` reduced to a loader, `checks.py` kept as the interpreter.
4. **Rule effectivity.** A document, a verdict and an approval name the rule set that judged them
   (§9.6, `dossiers/rule_effectivity/p0_business_problem_statement.md`).
5. **Construction.** Governed and specified on its own, against the same declarations (§9.7).

**Out of scope:**
- re-expressing tier-B kinds (§9.3);
- an independent evaluator (§8.5);
- the protocol track (§9.4);
- any feature not named above.

A need found during the rebuild that is not in this list goes on the list below, not into the build.

**Unchanged.** The doctrine in `transformation/CLAUDE.md`:
- phases P0–P8 and their gates;
- two compilers;
- snapshot facts only through `inspector.api.query`;
- the pinned baseline;
- CLI only, with no boundary contract;
- a deterministic oracle with assistive drafting.

## 5. Acceptance

The rebuild replaces the old module only when every item below holds. A deliberate divergence is
entered in §8 before the build is written, never after it is seen.

1. **The corpus.** Every test document and every delivered dossier, converted mechanically by the
   oracle's reader into the new form. A delivered dossier's original is never edited. The tests read
   its converted copy.
2. **Declaration identity.** The rebuild's expanded rule set equals the oracle's, rule for rule,
   apart from the divergences in §8.
3. **Behavioural identity.** The rebuild gives every corpus document the oracle's verdict and
   findings: the rule, register, row and detail. The oracle runs live beside the rebuild. Its
   output is not replayed from a record.
4. **Construction identity.** From the converted corpus, construction reproduces every artifact the
   oracle reproduces.
5. **Closure.** Every rule cites an invariant that resolves. Every invariant is realised or declared
   not enforced. Every check kind is used (§3).
6. **The workspace.** `regression.sh --all` passes. The rebuild updates `expectations.yaml` only
   for counts that it explains in §8.

## 6. Identity at the swap

Development is open. `.github/process/retention.yaml` declares that nothing is retained for its own
sake.

- An oracle artifact the rebuild does not keep is deleted, and recorded in
  `.github/process/retired_identities.yaml`.
- A deleted name is never reused. A rebuilt artifact takes a new identity whenever its meaning
  changes.
- A deletion leaves the successor's `supersedes` pointing at an absent identity. The platform's
  surface closure refuses that today. The fix is decided (option B): `supersedes` records history,
  is exempt from surface closure, and is checked against the ledger by `supersession_agreement`.
  It is a `software_governance` change. The frozen oracle judges it, so the oracle is not judging
  its own redesign. It lands before the swap.

## 7. Governance exception

The rebuild is not judged by its own lifecycle. It produces no dossier of its own P0–P8, because
the tool that would judge it is the tool being replaced.

- This is an exception, made openly, and it is the reason for this charter. The generated-artifacts
  exception was declared the last one. This charter re-opens that ruling, so the exception is
  recorded in `.github/process/rulings.md` before the branch opens.
- **What stands in for the lifecycle.** The oracle in §5 decides whether the rebuild is admissible.
  A human approves this charter and the design before any code. A human approves the swap.
- After the swap, every change to transformation goes through the lifecycle again, judged by the
  rebuilt module.

## 8. Divergences and additions

The deliberate differences from the oracle, each with its reason, entered before it is built. The
rebuild starts with these:

| Item | Divergence | Reason |
|---|---|---|
| Form of a phase document | Structured block, not tables | Format, in scope (§4.1). |
| Retained phase workflows and contracts | Deleted, with a ledger entry | Development retains nothing for its own sake (§6). |

## 9. The in-flight dossiers

- `binding_literals` and `quoted_literals` stay as delivered. They are part of the oracle.
- `register_format` (P0–P7) and `version_retirement` (P0–P6) are parked and never delivered. They
  are kept as evidence. Their findings are inputs to the design: the readers' shape, the test copies,
  deletion by record, and node keys as places.
- `rule_effectivity` keeps its P0, as the statement of change 4 of the scope.

## 10. Sequence

1. **Checkpoint.** Commit the workspace as it stands, tag the oracle, and record the exception.
2. **Design.** One design document for the whole scope. A human gates it, and it fills §8.
3. **The platform fix.** `supersedes` exempt from surface closure (§6), through the lifecycle,
   judged by the oracle.
4. **Build.** On the branch `rebuild/transformation`, cut from the tag.
5. **Acceptance.** §5, item by item.
6. **Swap.** Squash the branch into `dev/18` as one commit. The oracle's dead artifacts are deleted
   and recorded in the same change. The human runs every git command.

## 11. Open decisions

- **Branch and tag names.** Proposed: `rebuild/transformation` and `oracle/transformation`.
- **Where the design lives.** Proposed: `transformation/doc/REBUILD_DESIGN.md`, on the branch.
- **Converted corpus location.** Proposed: beside the catalog's existing fixtures, as `register_format`
  found (§9.10 R3).
