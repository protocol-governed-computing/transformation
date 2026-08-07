"""`tc` — the transformation compiler CLI.

The only interface this tool has. It is build-time: no transport surface, no Operation Identity.
"""

from __future__ import annotations

import json
import re
import sys

import yaml
from pathlib import Path

import click

from transformation.baseline import (
    Baseline,
    BaselineMismatch,
    grounded_registers,
    observe,
    pending,
    verify,
)
from transformation.design.checks import kinds as check_kinds
from inspector import api as inspector_api

from transformation.build.completeness import measure, narrowing
from transformation.build.render import bare, build_manifest, render_all, render_document, render_documents
from transformation.design.merit import PolicyUnavailable, load_policy, rate as rate_merit
from transformation.design.meta import RULE_MODULES, verify as meta_verify
from transformation.design.oracle import evaluate
from transformation.design.project import PROJECTIONS
from transformation.design.read import read_seed
from transformation.design import catalog
from transformation.design.template_reader import load as load_template

# Rule sets are declared per phase and mapped once, in `design.meta` — the module that has to
# verify the mapping is complete. Purpose, question, key rule and purity rung come from the
# catalogue, which mirrors field manual §4.1 and §4.2.
RULE_SETS = RULE_MODULES


def _parse_prior(argument: str) -> tuple[str, Path]:
    """Split a `--prior p1=<path>` argument, or fail hard.

    The phase is named rather than inferred from the filename. A dossier's filenames are a
    convention, and inferring a phase from one would let a misnamed file be judged as the wrong
    upstream document while reporting a confident verdict.
    """
    phase_id, separator, raw_path = argument.partition("=")
    if not separator or not phase_id or not raw_path:
        raise click.BadParameter(f"expected PHASE=PATH, got {argument!r}", param_hint="--prior")
    if phase_id not in RULE_SETS:
        raise click.BadParameter(
            f"unknown phase {phase_id!r}; declared phases are {sorted(RULE_SETS)}",
            param_hint="--prior",
        )
    path = Path(raw_path)
    if not path.is_file():
        raise click.BadParameter(f"{raw_path} is not a file", param_hint="--prior")
    return phase_id, path


def _read_prior(path: Path) -> dict:
    """An upstream phase document as the plain data a cross-phase check reads."""
    prior = read_seed(path)
    return {"header": prior.header, "sections": prior.sections, "registers": prior.registers}


@click.group()
@click.version_option(package_name="transformation")
def main() -> None:
    """PGC transformation compiler — governed change request to authoring mandate."""


@main.group()
def phase() -> None:
    """The dossier phases — judge a document against a phase's declared rule set."""


_PHASE_OPTION = click.option(
    "--phase",
    "phase_key",
    type=click.Choice(sorted(RULE_SETS)),
    required=True,
    help="Which phase's template and rule set to apply.",
)


@phase.command("check")
@click.argument("doc_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@_PHASE_OPTION
@click.option(
    "--snapshot",
    "snapshot_root",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    help="Composition to ground against. Required by phases that verify claims about the system.",
)
@click.option(
    "--prior",
    "prior_args",
    multiple=True,
    metavar="PHASE=PATH",
    help="An upstream phase document this one is judged against, e.g. --prior p1=<path>.",
)
@click.option("--json", "as_json", is_flag=True, help="Emit the verdict as JSON.")
def phase_check(
    doc_path: Path,
    phase_key: str,
    snapshot_root: Path | None,
    prior_args: tuple[str, ...],
    as_json: bool,
) -> None:
    """Judge a phase document against that phase's structural oracle.

    A phase that grounds claims needs a composition to ground against, and a phase that preserves
    an upstream commitment needs the document carrying it. Without `--snapshot` or `--prior` those
    rules report that they could not be checked — they do not quietly pass, because a silent pass
    would look identical to a verified one.

    Exit 0 if ADMISSIBLE, 1 if INADMISSIBLE.
    """
    rules_mod = RULE_SETS[phase_key]
    # operation → the key its result carries the rows under. A phase may ground against more than
    # one observation: P3 resolves identities against the artifact list and bounds its reuse search
    # by what each domain declares, and those are different questions asked of different surfaces.
    observes = getattr(rules_mod, "OBSERVATIONS", {})

    doc = read_seed(doc_path)
    if observes and snapshot_root:
        gathered = {}
        for operation, result_key in observes.items():
            status, result = inspector_api.query(operation, {}, str(snapshot_root))
            if status != "SUCCESS":
                raise click.ClickException(
                    f"{operation} failed against {snapshot_root}: {status}"
                )
            gathered[operation] = result.get(result_key, result)
        doc.observed = gathered
    elif observes:
        click.echo(
            f"  note: {phase_key} grounds claims through {', '.join(observes)}; "
            f"pass --snapshot to check them",
            err=True,
        )

    # Reading a prior is the driver's job, exactly as reading the document is. A check that opened
    # a file would make its verdict depend on a filesystem the compiled transform cannot reach, and
    # the genesis oracle and the composition would stop judging the same thing.
    declared_priors = getattr(rules_mod, "PRIORS", ())
    supplied = dict(_parse_prior(arg) for arg in prior_args)
    for unexpected in sorted(set(supplied) - set(declared_priors)):
        raise click.ClickException(
            f"{phase_key} declares no prior {unexpected!r}; it reads {list(declared_priors)}"
        )
    doc.priors = {
        phase_id: _read_prior(supplied[phase_id])
        for phase_id in declared_priors
        if phase_id in supplied
    }
    missing = [p for p in declared_priors if p not in supplied]
    if missing:
        click.echo(
            f"  note: {phase_key} preserves commitments from {', '.join(missing)}; "
            f"pass --prior {missing[0]}=<path> to check them",
            err=True,
        )

    verdict = evaluate(doc, rules_mod.rule_set())
    # Admissibility and quality are separate axes: the rule set decides the verdict, the figure of
    # merit says how good the document is. A document may be admissible and imperfect, or
    # inadmissible over one misspelling while otherwise strong.
    # The policy is declared in the composition, so a rating needs one to read. Without a snapshot
    # there is no policy and therefore no rating — reported as not computed, never defaulted.
    merit = None
    if snapshot_root:
        merit = rate_merit(verdict, doc, load_policy(str(snapshot_root)))

    if as_json:
        payload = verdict.as_dict()
        payload["merit"] = None if merit is None else {
            "rating": merit.rating,
            "maximum": merit.maximum,
            "deductions": [
                {"id": d.id, "label": d.label, "weight": d.weight, "count": d.count}
                for d in merit.deductions
            ],
        }
        click.echo(json.dumps(payload, indent=2))
    else:
        click.echo(f"{verdict.verdict}  [{phase_key}]  {doc_path}")
        for finding in verdict.findings:
            click.echo(f"  {finding}")
        click.echo(
            f"  {len(verdict.findings)} finding(s) over {verdict.rules_evaluated} declared rules"
        )
        click.echo()
        click.echo(f"  Status            {verdict.verdict}")
        if merit is None:
            click.echo("  Figure of Merit   not computed — pass --snapshot to read the policy")
        else:
            click.echo(f"  Figure of Merit   {merit.stars} {merit.rating}/{merit.maximum}")
            if merit.deductions:
                click.echo("  Deductions")
                for deduction in merit.deductions:
                    click.echo(f"      {deduction}")
            else:
                click.echo("  Deductions        none")
        nxt = catalog.next_phase(phase_key)
        if nxt:
            click.echo(f"  Ready for {nxt.upper():<7} {'YES' if verdict.admissible else 'NO'}")

    sys.exit(0 if verdict.admissible else 1)


@phase.command("project")
@click.argument("prior_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@_PHASE_OPTION
@click.option(
    "--out",
    "out_path",
    type=click.Path(dir_okay=False, path_type=Path),
    required=True,
    help="Where to write the projected document.",
)
@click.option(
    "--force",
    is_flag=True,
    help="Overwrite an existing document. Without it, an existing file is left alone.",
)
def phase_project(prior_path: Path, phase_key: str, out_path: Path, force: bool) -> None:
    """Project a phase document from the prior that uniquely determines it.

    Only phases that decide nothing can be projected. P1 is one: with blocking clarifications
    inadmissible at P0, a change request is the seed's registers plus the citation naming where each
    row was said, and there is no authoring choice left to make. A phase absent from the projection
    table is one a human still decides.

    The prior is judged before it is projected. Projecting an inadmissible seed would launder its
    open questions into a document that reads as settled — and a citation is only evidence if the
    thing it cites was admitted.

    Exit 0 if the document was written, 1 if the prior was refused.
    """
    if phase_key not in PROJECTIONS:
        raise click.ClickException(
            f"{phase_key} is not projected — it is authored. "
            f"Projected phases are {sorted(PROJECTIONS)}"
        )
    prior_phase, projection = PROJECTIONS[phase_key]

    prior = read_seed(prior_path)
    verdict = evaluate(prior, RULE_SETS[prior_phase].rule_set())
    if not verdict.admissible:
        click.echo(f"{verdict.verdict}  [{prior_phase}]  {prior_path}")
        for finding in verdict.findings:
            click.echo(f"  {finding}")
        click.echo(
            f"\n  {len(verdict.findings)} finding(s) over {verdict.rules_evaluated} declared rules"
        )
        click.echo(f"  {phase_key.upper()} not projected — resolve the prior first")
        sys.exit(1)

    if out_path.exists() and not force:
        raise click.ClickException(f"{out_path} exists; pass --force to overwrite it")

    out_path.write_text(projection(prior), encoding="utf-8")
    click.echo(f"  projected {phase_key} from {prior_phase}  ->  {out_path}")
    click.echo(f"  {prior_phase} ADMISSIBLE over {verdict.rules_evaluated} declared rules")


@phase.command("rules")
@_PHASE_OPTION
@click.option("--json", "as_json", is_flag=True, help="Emit the rule set as JSON.")
def phase_rules(phase_key: str, as_json: bool) -> None:
    """Print a phase's declared admissibility rule set.

    The rules are data, not code: this is the whole of what governs that phase's document.
    """
    declared = RULE_SETS[phase_key].rule_set()

    if as_json:
        click.echo(
            json.dumps(
                [
                    {
                        "id": r.id,
                        "check": r.check,
                        "register": r.register or r.section_title,
                        "params": r.params,
                        "intent": r.intent,
                    }
                    for r in declared
                ],
                indent=2,
            )
        )
        return

    for rule in declared:
        register = rule.register or rule.section_title or "(document)"
        click.echo(f"  {rule.id:<38} {rule.check:<24} {register}")
        if rule.intent:
            click.echo(f"  {'':<38} └─ {rule.intent}")
    click.echo(f"\n  {len(declared)} rules over {len(check_kinds())} check kinds")


@phase.command("meta")
@click.option("--json", "as_json", is_flag=True, help="Emit the findings as JSON.")
def phase_meta(as_json: bool) -> None:
    """Verify the rule sets themselves — declaration/enforcement parity, before any document.

    Meta-governance: this judges no dossier. It asserts that every declared rule can actually run
    and that every implemented mechanism is actually declared. If that correspondence is broken, a
    verdict over a document is meaningless — a rule that cannot run reports green over a subject it
    never evaluated.
    """
    findings = meta_verify(RULE_SETS)

    if as_json:
        click.echo(
            json.dumps(
                {
                    "verdict": "CONSISTENT" if not findings else "INCONSISTENT",
                    "phases": sorted(RULE_SETS),
                    "rules_examined": sum(len(m.rule_set()) for m in RULE_SETS.values()),
                    "check_kinds": len(check_kinds()),
                    "findings": [
                        {"code": f.code, "where": f.where, "detail": f.detail} for f in findings
                    ],
                },
                indent=2,
            )
        )
        sys.exit(1 if findings else 0)

    examined = sum(len(m.rule_set()) for m in RULE_SETS.values())
    if not findings:
        click.echo(
            f"  CONSISTENT — {examined} rules across {len(RULE_SETS)} phases resolve against "
            f"{len(check_kinds())} check kinds"
        )
        return

    for finding in findings:
        click.echo(f"  [{finding.code}] {finding.where}")
        click.echo(f"      {finding.detail}")
    click.echo(
        f"\n  INCONSISTENT — {len(findings)} finding(s) over {examined} declared rules"
    )
    sys.exit(1)


@phase.command("template")
@_PHASE_OPTION
def phase_template(phase_key: str) -> None:
    """Print a phase's required section structure."""
    spec = catalog.phase(phase_key)
    click.echo(f"{phase_key} — {spec.purpose}\n  {spec.question}\n  admits: {spec.rung}\n")

    for reg in load_template(phase_key).registers:
        cols = f"table[{', '.join(reg.columns)}]" if reg.columns else "no table"
        click.echo(f"  §{reg.section_number or '-':<3} {reg.id:<24} {cols}{'  (may be empty)' if reg.optional else ''}")
        for column, values in reg.vocabularies.items():
            click.echo(f"       {column}: {', '.join(values)}")


@phase.command("list")
def phase_list() -> None:
    """Print the pipeline: what each phase is for, and what vocabulary it admits.

    A phase name says which step; it does not say what the step is for. The commonest authoring
    failure is answering the next phase's question early, so the question and the purity rung are
    stated alongside the name.
    """
    for spec in catalog.PHASES:
        built = "built" if spec.id in RULE_SETS else "   — "
        rules = len(RULE_SETS[spec.id].rule_set()) if spec.id in RULE_SETS else 0
        click.echo(f"  {spec.id:<4} {spec.purpose:<20} [{built}] {rules or '':>4} rules   admits: {spec.rung}")
        click.echo(f"       {spec.question}")
        click.echo(f"       rule: {spec.key_rule}")
        if spec.gate:
            click.echo(f"       {spec.gate}")
        click.echo()


def _narrowed(p7: dict, p8: dict, snapshot_root: Path | None,
              dossier: Path = Path(".")) -> dict | None:
    """Facts each amended artifact would lose, or None when there is nothing to compare against.

    An EXTEND is rendered whole and replaces its predecessor, so the design must state the artifact
    whole. Reading what the composition already holds is the only way to know that it did.
    """
    if snapshot_root is None:
        return None

    # An amendment is only meaningfully compared with the composition the change was designed
    # against. Handed the live snapshot after the change was promoted, this compares the design with
    # its own output and reports the change's additions as losses whenever they are revised. The
    # dossier names the composition it was validated against, so say so rather than let a reader
    # take the wrong reading for a defect.
    pin = dossier / "baseline.json"
    if pin.is_file():
        declared = json.loads(pin.read_text()).get("snapshot_id", "")
        status, summary = inspector_api.query("si.snapshot.summary", {}, str(snapshot_root))
        observed = summary.get("snapshot_id", "") if status == "SUCCESS" else ""
        if declared and observed and declared != observed:
            click.echo(
                f"  note: {snapshot_root} is not this change's baseline "
                f"({observed[:12]}… vs {declared[:12]}…) — an amendment compared against a "
                f"composition that already holds this change reads its own additions as losses",
                err=True)

    existing = {}
    for entry in p7.get("existing_inventory", []):
        action = next((v for k, v in entry.items() if k.startswith("Action")), "")
        fqdn = next((v for k, v in entry.items() if k.startswith("FQDN")), "").strip()
        if action.strip().upper() == "EXTEND" and fqdn:
            status, result = inspector_api.query(
                "si.artifact.show", {"artifact": fqdn}, str(snapshot_root))
            if status != "SUCCESS":
                continue
            # The machine block, read out of the canonical artifact the composition holds. It is the
            # same shape construction renders, which is what makes the two comparable at all.
            block = re.search(r"```yaml\n(.*?)```",
                              (result.get("canonical") or {}).get("content", ""), re.S)
            if block:
                existing[fqdn.split("::")[-1]] = yaml.safe_load(block.group(1)) or {}
    return narrowing(render_all(p7, p8), existing)


@main.group()
def construction() -> None:
    """The Construction lifecycle — is a design ready to build from?"""


@construction.command("check")
@click.argument("dossier", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("--require", "threshold", type=float, default=100.0, show_default=True,
              help="Minimum Construction Completeness; below it the design is refused.")
@click.option("--json", "as_json", is_flag=True, help="Emit the measurement as JSON.")
@click.option("--snapshot", "snapshot_root",
              type=click.Path(exists=True, file_okay=False, path_type=Path),
              help="Composition to compare amendments against, so none narrows what it replaces.")
def construction_check(dossier: Path, threshold: float, as_json: bool,
                       snapshot_root: Path | None = None) -> None:
    """Measure whether a design uniquely determines the artifacts it specifies.

    `tc phase check` admits a document against a rule set; this admits a *design* to construction.
    A fact the design does not state is a fact the generator would have to invent, and a generator
    that invents design is a second, ungoverned design authority — so the default threshold is 100
    and anything less is a refusal.

    Exit 0 if the threshold is met, 1 otherwise.
    """
    p7 = _dossier_registers(dossier, "p7")
    p8 = _dossier_registers(dossier, "p8")
    result = measure(p7, p8)

    if as_json:
        click.echo(json.dumps({
            "completeness": round(result.percentage, 2),
            "determined": result.determined,
            "required": result.total,
            "undetermined": dict(result.undetermined),
        }, indent=2))
    else:
        click.echo(f"{dossier.name} — {len(result.by_artifact)} artifact(s), "
                   f"{result.total} required fact(s)\n")
        for code, facts in sorted(result.by_artifact.items()):
            missing = [path for path, ok in facts if not ok]
            mark = "OK  " if not missing else "GAP "
            click.echo(f"  {mark} {code:<44} {len(facts) - len(missing)}/{len(facts)}"
                       + (f"   {', '.join(missing[:3])}" if missing else ""))
        click.echo(f"\n  Construction Completeness  {result.percentage:.1f}%"
                   f"   ({result.determined}/{result.total} determined)")

        lost = _narrowed(p7, p8, snapshot_root, dossier)
        if lost is None:
            click.echo("  note: pass --snapshot to check that no amendment narrows what it replaces",
                       err=True)
        elif lost:
            click.echo("\n  AMENDMENT NARROWS — these facts exist now and the design does not state them:")
            for code, facts in sorted(lost.items()):
                click.echo(f"      {code:<44} {len(facts)} fact(s) lost")
                for fact in facts[:4]:
                    click.echo(f"          {fact}")
                if len(facts) > 4:
                    click.echo(f"          ... and {len(facts) - 4} more")
            sys.exit(1)
        for name, n in result.undetermined.most_common():
            click.echo(f"    {n:>3}  {name}")

    sys.exit(0 if result.meets(threshold) else 1)


def _dossier_registers(dossier: Path, phase_key: str) -> dict:
    """A dossier phase document's registers, as the plain rows construction reads."""
    matches = sorted(dossier.glob(f"{phase_key}_*.md"))
    if not matches:
        raise click.ClickException(f"{dossier} carries no {phase_key} document")
    doc = read_seed(matches[0])
    out: dict[str, list[dict]] = {}
    for entry in doc.registers:
        block = doc.register(entry["id"])
        if block and block.table:
            out[entry["id"]] = block.table.rows
    return out



@construction.command("emit")
@click.argument("dossier", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("--root", "domain_root", required=True,
              type=click.Path(exists=True, file_okay=False, path_type=Path),
              help="The domain repository the artifacts belong to.")
@click.option("--force", is_flag=True, help="Overwrite artifacts that already exist.")
@click.option("--require", "threshold", type=float, default=100.0, show_default=True,
              help="Minimum Construction Completeness; below it nothing is written.")
def construction_emit(dossier: Path, domain_root: Path, force: bool, threshold: float) -> None:
    """Write the artifacts a mandate schedules into the domain that owns them.

    Construction has always been able to render; nothing put the result on disk, so the only thing
    that ever consumed a render was the acceptance harness comparing it against artifacts written
    by hand. This is the other half.

    **Measured before anything is written.** A design below the threshold does not determine its
    artifacts, and emitting one would put the generator's guesses into a registry where they read
    as authored. Nothing is written unless everything can be.

    The domain's build manifest is written too when the domain has none. It is not an artifact any
    phase designs — every field of it is compiler configuration — but a domain the compiler cannot
    discover is a domain that does not build, and hand-copying it between domains has drifted.

    Exit 0 if everything was written, 1 if the design was refused or a path already exists.
    """
    p7 = _dossier_registers(dossier, "p7")
    p8 = _dossier_registers(dossier, "p8")

    result = measure(p7, p8)
    if not result.meets(threshold):
        click.echo(f"REFUSED — Construction Completeness {result.percentage:.1f}% is below "
                   f"{threshold:.0f}%; nothing written.", err=True)
        for path, count in result.undetermined.most_common(8):
            click.echo(f"    {count:>3}  {path}", err=True)
        sys.exit(1)

    documents = render_documents(p7, p8)
    manifest = build_manifest(p7, p8)
    planned: list[tuple[Path, str]] = [(domain_root / d["path"], d["text"]) for d in documents]
    if manifest is not None:
        target = domain_root / "registry" / "structures" / f"{bare(manifest['fqdn'])}.md"
        if not target.exists():
            planned.append((target, render_document({"machine": manifest})))

    clashes = [path for path, _ in planned if path.exists()]
    if clashes and not force:
        click.echo(f"REFUSED — {len(clashes)} artifact(s) already exist; pass --force to "
                   f"overwrite. Nothing written.", err=True)
        for path in clashes[:8]:
            click.echo(f"    {path}", err=True)
        sys.exit(1)

    for path, text in planned:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    click.echo(f"  emitted {len(planned)} file(s) under {domain_root}")
    for path, _ in planned:
        click.echo(f"    {path.relative_to(domain_root)}")
    click.echo(f"\n  Construction Completeness {result.percentage:.1f}% "
               f"({result.determined}/{result.total} determined)")



@main.group()
def baseline() -> None:
    """The pinned validation baseline."""


@baseline.command("verify")
@click.argument("pin_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "--snapshot",
    "snapshot_root",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    required=True,
    help="Snapshot root to check against the pin.",
)
def baseline_verify(pin_path: Path, snapshot_root: Path) -> None:
    """Assert the snapshot on disk is the pinned baseline."""
    pin = Baseline.load(pin_path)
    try:
        actual = verify(pin, snapshot_root)
    except BaselineMismatch as exc:
        click.echo(str(exc), err=True)
        sys.exit(1)
    click.echo(f"BASELINE OK  {actual.snapshot_id}")
    click.echo(f"  artifacts {actual.artifact_count}  domains {', '.join(actual.domains)}")

    # The id proves the composition is the one named. It proves nothing about whether anyone
    # re-read the registers that assert facts about it, which is the half a re-pin silently drops.
    outstanding = {phase: pending(pin, phase) for phase in sorted(RULE_MODULES)}
    outstanding = {phase: regs for phase, regs in outstanding.items() if regs}
    approved = sum(len(r) for r in pin.approved_registers.values())
    if approved:
        for phase, registers in sorted(pin.approved_registers.items()):
            for register, who in sorted(registers.items()):
                click.echo(f"  approved  {phase}/{register:<28} {who}")
    if outstanding:
        # Phrased as owed rather than neglected: a phase this CR has not reached yet trivially
        # carries no approval, and calling that a defect would cry wolf on every early dossier.
        click.echo("\n  NOT YET APPROVED against this pin — each rests on a snapshot fact:")
        for phase, registers in outstanding.items():
            for register in registers:
                click.echo(f"    {phase}/{register}")
        click.echo("    run: tc baseline approve --phase <p> --by <name> " + str(pin_path))


@baseline.command("approve")
@click.argument("pin_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--phase", "phase_key", type=click.Choice(sorted(RULE_MODULES)), required=True,
              help="Which phase's grounded registers were re-read.")
@click.option("--by", "approver", required=True, help="Who re-grounded them.")
@click.option("--register", "registers", multiple=True,
              help="A single register; repeatable. Omit to approve every grounded register of the phase.")
def baseline_approve(pin_path: Path, phase_key: str, approver: str, registers: tuple[str, ...]) -> None:
    """Record that a phase's snapshot-grounded registers were re-read against this pin.

    The second half of rebaselining. Verifying the id proves the composition is the one named; this
    records that someone re-read the registers asserting facts about it. The approval lives in the
    pin, so re-pinning drops it — an approval is against one composition and survives no other.

    Which registers a phase owes is derived from its rule set: a register rests on a snapshot fact
    exactly when a rule governing it consults an observation.
    """
    pin = Baseline.load(pin_path)
    owed = grounded_registers(phase_key)
    if not owed:
        raise click.ClickException(
            f"{phase_key} has no register resting on a snapshot fact — nothing to approve"
        )
    chosen = registers or owed
    unknown = [r for r in chosen if r not in owed]
    if unknown:
        raise click.ClickException(
            f"{phase_key} grounds no register named {', '.join(unknown)}; it grounds {', '.join(owed)}"
        )
    updated = pin.approve(phase_key, chosen, approver)
    pin_path.write_text(json.dumps(updated.as_dict(), indent=2) + "\n", encoding="utf-8")
    for register in chosen:
        click.echo(f"  approved  {phase_key}/{register}  by {approver}")
    still = pending(updated, phase_key)
    click.echo(f"  {phase_key}: {len(owed) - len(still)}/{len(owed)} grounded register(s) approved "
               f"against {updated.snapshot_id[:16]}")


@baseline.command("show")
@click.option(
    "--snapshot",
    "snapshot_root",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    required=True,
    help="Snapshot root to read.",
)
def baseline_show(snapshot_root: Path) -> None:
    """Print the composition present at a snapshot root, as a pin."""
    # Deliberately carries no approvals: observing a composition approves nothing about it, and a
    # re-pin that inherited them would assert a review that never happened.
    actual = observe(snapshot_root)
    click.echo(
        json.dumps(
            actual.as_dict(),
            indent=2,
        )
    )
