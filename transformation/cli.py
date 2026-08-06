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

from transformation.baseline import Baseline, BaselineMismatch, observe, verify
from transformation.design.checks import kinds as check_kinds
from inspector import api as inspector_api

from transformation.build.completeness import measure, narrowing
from transformation.build.render import render_all
from transformation.design.merit import PolicyUnavailable, load_policy, rate as rate_merit
from transformation.design.oracle import evaluate
from transformation.design.project import PROJECTIONS
from transformation.design.read import read_seed
from transformation.design.p0_change_seed import rules as p0_rules
from transformation.design.p1_change_request import rules as p1_rules
from transformation.design.p2_domain_model import rules as p2_rules
from transformation.design.p3_analysis_loop import rules as p3_rules
from transformation.design.p4_business_model import rules as p4_rules
from transformation.design.p5_business_intent import rules as p5_rules
from transformation.design.p6_governance_intent import rules as p6_rules
from transformation.design.p7_design_intent import rules as p7_rules
from transformation.design.p8_authoring_mandate import rules as p8_rules
from transformation.design import catalog
from transformation.design.template_reader import load as load_template

# Rule sets still declared per phase; purpose, question, key rule and purity rung come from the
# catalogue, which mirrors field manual §4.1 and §4.2.
RULE_SETS = {
    "p0": p0_rules,
    "p1": p1_rules,
    "p2": p2_rules,
    "p3": p3_rules,
    "p4": p4_rules,
    "p5": p5_rules,
    "p6": p6_rules,
    "p7": p7_rules,
    "p8": p8_rules,
}


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
                        "register": r.section_title,
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
        register = rule.section_title or "(document)"
        click.echo(f"  {rule.id:<38} {rule.check:<24} {register}")
        if rule.intent:
            click.echo(f"  {'':<38} └─ {rule.intent}")
    click.echo(f"\n  {len(declared)} rules over {len(check_kinds())} check kinds")


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
    actual = observe(snapshot_root)
    click.echo(
        json.dumps(
            {
                "snapshot_id": actual.snapshot_id,
                "artifact_count": actual.artifact_count,
                "domains": list(actual.domains),
            },
            indent=2,
        )
    )
