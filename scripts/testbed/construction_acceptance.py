"""Construction acceptance — render a domain's artifacts from its dossiers and compare with what was built.

A domain's registry is what its change requests have made it, in order, so acceptance renders the
**sequence** and not one change of it. Each dossier's design is rendered in turn and a later one
overrides an earlier for any artifact it touches, exactly as promotion did on disk. The comparison
then asks the only question worth asking: **does the accumulated design determine the registry?**

Rendering a single dossier was right while one change request owned the domain and wrong the moment a
second amended eight of its artifacts — the earlier design still renders them as they were, so
acceptance reported twenty-six differences that were history rather than defects. Evolution is never
greenfield here; the acceptance corpus is a sequence for the same reason validation is.

Every difference is one of exactly two things, and the difference itself says which:

    a generator bug          the design states the fact and the renderer got it wrong
    a design insufficiency   the design does not state the fact at all

The second is the more valuable finding. Construction Completeness measures whether the facts the
probe *knows to ask about* are determined; this measures whether the artifact can actually be
rebuilt, which is the question the probe's fact list can only approximate.

Comparison is semantic and scoped to the Machine block. An artifact's prose is human narrative that
no register determines, and comparing text would report a hundred differences about paragraphs
nobody claims are generated.

Run:  python scripts/testbed/construction_acceptance.py [dossier ...] [--registry <path>]
Exit: 0 when every artifact matches, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

# `MACHINE_BLOCK` is one spelling of where a machine block ends, owned by the module
# that renders them — there were three spellings and two of them disagreed.
from transformation.build.render import MACHINE_BLOCK as MACHINE
from transformation.build.render import render_all, bare
from transformation.design.read import read_seed

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
# In order. A dossier appended here is a change that came after the ones above it, and the ordering
# is the whole of what makes the composite meaningful.
# The fixture dossiers, not the approved ones. A closed change request is evidence and is never
# amended to satisfy a rule written after it was gated; a fixture is maintained against the
# current rule set on purpose. See `fixture_dossiers/README.md`.
CR_DOSSIERS = REPO / "scripts/testbed/fixture_dossiers"
REGISTRY = WORKSPACE / "business_domains/book_library_mgmt/registry"

# Every domain whose registry a dossier sequence determines, as (dossier root, registry).
#
# The two are read from different places and the asymmetry is deliberate. **The catalog is read from
# maintained fixtures** because its own harnesses judge those documents and a delivered dossier goes
# inadmissible as the design language grows. **blockchain is read from its delivered dossiers**,
# which is possible because rendering reads registers and never judges admissibility — a dossier that
# would be refused at P7 today still determines exactly the artifacts it determined when it was
# gated. Nothing had ever compared those 40 artifacts against their designs.
# The base-code roots below are read from their delivered dossiers for the same reason blockchain is:
# rendering reads registers and never judges admissibility. They carry no numbering, so they carry no
# order — see `sequence`.
# `(dossier root, registry, whole)`. `whole` is whether the dossiers account for the registry
# entirely — true where a domain was built by change requests from its first artifact, false where
# the registry predates the lifecycle and most of it is determined by no design.
DOMAINS = (
    (CR_DOSSIERS, REGISTRY, True),
    (WORKSPACE / "business_domains/blockchain/cr_dossiers",
     WORKSPACE / "business_domains/blockchain/registry", True),
    (WORKSPACE / "software_governance/dossiers",
     WORKSPACE / "software_governance/registry", False),
    (WORKSPACE / "transformation/dossiers",
     WORKSPACE / "transformation/registry", False),
)

# The catalog's entry above overrides what discovery would find, and only that one: its dossiers are
# read from maintained fixtures rather than from the domain's own delivered ones. Named here so the
# coverage check below can tell a deliberate substitution from an omission.
SUBSTITUTED = {WORKSPACE / "business_domains/book_library_mgmt/cr_dossiers"}

# The sequence used to be a literal list, and a delivered dossier that re-rendered an artifact an
# earlier one rendered had to be appended by hand. Miss the step and the harness compares a built
# artifact against a design that is no longer its design of record, then reports the difference as
# a field difference — which reads like a construction defect rather than a stale corpus. cr_03
# cost 12 such differences before anyone thought to look at the list.
#
# A business-domain dossier is numbered, and the number *is* the sequence: `cr_NN_<subject>` is the
# form, declared in `transformation/CLAUDE.md`. So the ordering is read from the name rather than
# restated beside it. A directory that is not numbered that way is not part of a sequence and is
# not silently swept in.
SEQUENCED = re.compile(r"^cr_(\d+)_")


def sequence(root: Path) -> list[Path]:
    """The delivered dossiers of one domain, in the order they were delivered.

    A business domain numbers its dossiers and the number *is* the order. A base-code domain does
    not — `transformation/CLAUDE.md` rules that `cr_NN_` "says nothing true about it and reads as a
    sequence that does not exist", because git manages the change. So an unnumbered root has a set
    and no order, and this returns it sorted by name for a stable report rather than a meaningful one.

    That is safe exactly while no two of its dossiers determine the same artifact, which `acceptance`
    checks rather than assumes. Where two do, an order is needed, none is declared, and the harness
    refuses instead of picking one.
    """
    numbered = [(int(m.group(1)), p) for p in root.iterdir()
                if p.is_dir() and (m := SEQUENCED.match(p.name))]
    if numbered:
        return [p for _, p in sorted(numbered)]
    return sorted(p for p in root.iterdir() if p.is_dir() and determines_artifacts(p))


DOSSIERS = sequence(CR_DOSSIERS)

def registers(path: Path) -> dict[str, list[dict]]:
    doc = read_seed(path)
    out: dict[str, list[dict]] = {}
    for entry in doc.registers:
        block = doc.register(entry["id"])
        if block and block.table:
            out[entry["id"]] = block.table.rows
    return out


def built(registry: Path) -> dict[str, dict]:
    out = {}
    for path in sorted(registry.rglob("*.md")):
        found = MACHINE.search(path.read_text(encoding="utf-8"))
        if not found:
            continue
        machine = yaml.safe_load(found.group(1))
        if isinstance(machine, dict) and "fqdn" in machine:
            out[bare(machine["fqdn"])] = machine
    return out


# Keys that are documentation even inside the Machine block. Two tests decide membership, and both
# are empirical rather than aesthetic:
#
#   nothing consumes it   `isolation`, `resolution`, `storage_roots` and `extensions` appear in no
#                         compiler, assembler or runtime read path. `isolation.rules` restates in
#                         prose what `entity_stores` already says structurally.
#   it varies by author   the built corpus carries a field `description` on some fields and not
#                         others; a governed fact is present or absent by rule.
#
# A key that something reads is governed however prose-like it looks — `parameters` on a runtime
# binding is a list of names an assertion checks, so it stays in.
DOCUMENTATION = {"description", "isolation", "resolution", "storage_roots", "extensions"}

# `superseded_by` is written when an artifact is **stood down**, which is a separate act from
# rendering it: a replaced artifact has no design left to render from, so construction marks the
# header and leaves the rest alone. Comparing it here would report every superseded artifact as a
# construction defect, when what it records is that the artifact was correctly retired. The rest of
# the machine block is still compared, so a superseded artifact whose *content* drifted is caught.
STOOD_DOWN = {"superseded_by"}


def diff(expected, actual, path: str = "") -> list[str]:
    """Every leaf where two Machine blocks disagree, addressed by dotted path."""
    if isinstance(expected, dict) and isinstance(actual, dict):
        out = []
        for key in sorted(set(expected) | set(actual)):
            if key in DOCUMENTATION or key in STOOD_DOWN:
                continue
            here = f"{path}.{key}" if path else key
            if key not in actual:
                out.append(f"{here}: not rendered")
            elif key not in expected:
                out.append(f"{here}: rendered but not built")
            else:
                out += diff(expected[key], actual[key], here)
        return out
    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            return [f"{path}: {len(actual)} rendered, {len(expected)} built"]
        out = []
        for i, (e, a) in enumerate(zip(expected, actual)):
            out += diff(e, a, f"{path}[{i}]")
        return out
    if expected != actual:
        return [f"{path}: rendered {actual!r}, built {expected!r}"]
    return []


def acceptance(dossier_root: Path, registry: Path, dossiers: list[Path] | None = None,
               whole: bool = True) -> tuple[int, int, int]:
    """Render one domain's dossier sequence and compare it with what was built.

    `whole` says whether the dossiers account for the registry entirely. A business domain built by
    change requests from the first artifact onward is whole, and a built artifact no dossier
    determines is a real gap. A base-code domain is not: its registry was authored before the
    lifecycle reached it, and most of it is determined by no design at all. Reporting those as gaps
    would bury the two that matter under two hundred that do not.

    What is compared is the same either way — every artifact a dossier determines. What changes is
    whether the remainder is a finding.

    Returns (compared, failures, field differences).
    """
    dossiers = dossiers or sequence(dossier_root)
    if not dossiers:
        return 0, 0, 0

    # Later changes override earlier ones, artifact by artifact — the same thing promotion did.
    rendered: dict[str, dict] = {}
    determined_by: dict[str, str] = {}
    ordered = bool(SEQUENCED.match(dossiers[0].name))
    for dossier in dossiers:
        p7 = registers(next(dossier.glob("p7_*.md")))
        p8 = registers(next(dossier.glob("p8_*.md")))
        for artifact in render_all(p7, p8):
            code = bare(artifact["machine"]["fqdn"])
            # Overriding is what promotion did, and it is only meaningful where the dossiers are
            # ordered. An unnumbered root carries no order, so two of its dossiers determining one
            # artifact is two designs of record and nothing says which is later. That is the hazard
            # `transformation/CLAUDE.md` names and nothing enforces — enforced here, for the roots
            # where it can be.
            if not ordered and code in rendered:
                print(f"  REFUSED  {code} is determined by both {determined_by[code]} and "
                      f"{dossier.name}, which carry no order between them")
                return 0, 1, 0
            rendered[code] = artifact
            determined_by[code] = dossier.name

        # The domain build manifest is no longer compared, because construction no longer produces
        # one. It was generated rather than rendered, and its domain was read from the namespace of
        # the first scheduled artifact — the same word as the domain for a business domain, and not
        # for anything else. Comparing a producer that has been withdrawn reported three differences
        # against a manifest nobody now claims to derive.

    reference = built(registry)
    print(f"construction acceptance — {' -> '.join(d.name for d in dossiers)}")
    print(f"{len(rendered)} rendered against {len(reference)} built\n")

    failures, total_diffs = 0, 0
    undetermined = 0
    for code in sorted(reference):
        # A build manifest is determined by no design, in any domain. Every field of it is
        # configuration the compiler discovers a domain by, and no register of any phase states one.
        # Construction used to generate it and no longer does; comparing it here would report a gap
        # against an artifact nothing claims to determine. Whether it should have a producer at all
        # is an open ruling, and until it has one this is not a construction defect.
        if code.startswith("STRUCTURE_BUILD_") and code.endswith("_CONFIG_V0"):
            undetermined += 1
            continue
        if code not in rendered:
            if not whole:
                undetermined += 1
                continue
            print(f"  MISS  {code:<44} rendered nothing")
            failures += 1
            continue
        differences = diff(reference[code], rendered[code]["machine"])
        total_diffs += len(differences)
        if not differences:
            print(f"  OK    {code:<44} {determined_by[code]}")
            continue
        failures += 1
        print(f"  DIFF  {code:<44} {len(differences)} field(s)   {determined_by[code]}")
        for line in differences[:6]:
            print(f"          {line}")
        if len(differences) > 6:
            print(f"          … {len(differences) - 6} more")

    for code in sorted(set(rendered) - set(reference)):
        print(f"  EXTRA {code:<44} rendered, never built")
        failures += 1

    # Compared is what a dossier determines, not what the registry holds. For a whole domain those
    # are the same number; for a partial one the difference is the tail the lifecycle has not reached,
    # reported so it stays visible rather than counted as reproduced.
    compared = len(reference) - undetermined
    print(f"\n  {compared - failures}/{compared} artifacts reproduced"
          f"   ({total_diffs} field difference(s))"
          + (f"   [{undetermined} built artifact(s) determined by no dossier]" if undetermined else "")
          + "\n")
    return compared, failures, total_diffs


def determines_artifacts(dossier: Path) -> bool:
    """True when a dossier's design schedules an artifact for construction to render.

    A dossier that only amends existing artifacts renders nothing, so acceptance has nothing to
    compare and its absence from the corpus is not a gap.
    """
    for p7 in dossier.glob("p7_*.md"):
        rows = registers(p7).get("new_artifacts") or []
        if any(_cell_of(row, "Code") for row in rows):
            return True
    return False


def _cell_of(row: dict, prefix: str) -> str:
    for key, value in row.items():
        if key.startswith(prefix):
            return str(value).strip()
    return ""


def uncovered() -> list[Path]:
    """Dossier roots holding a design that determines artifacts and that DOMAINS does not read.

    `DOMAINS` is a hand-kept pair, which is the shape `SEQUENCED` was introduced to remove one level
    down: the *sequence* used to be a literal list and a missed entry cost twelve differences read as
    construction defects. The *domain* list is still literal, and a third domain whose dossiers
    determine artifacts would be reproduced by nothing and reported by nothing.

    So rather than derive the list — the fixture substitution above is deliberate and derivation
    would undo it — this asks the question the list can go stale on, and asks it of the workspace
    rather than of a second list.
    """
    covered = {root.resolve() for root, _, _ in DOMAINS} | {p.resolve() for p in SUBSTITUTED}
    out = []
    for repo in sorted(WORKSPACE.iterdir()):
        if not repo.is_dir() or repo.name.startswith("."):
            continue
        for root in sorted(repo.glob("**/cr_dossiers")) + sorted(repo.glob("*/dossiers")) \
                + sorted(repo.glob("dossiers")):
            if root.resolve() in covered or not root.is_dir():
                continue
            if any(determines_artifacts(d) for d in root.iterdir() if d.is_dir()):
                out.append(root)
    return out


def main() -> int:
    args = sys.argv[1:]
    if "--registry" in args:
        i = args.index("--registry")
        if i + 1 >= len(args):
            print("--registry needs a path")
            return 1
        registry = Path(args[i + 1])
        del args[i:i + 2]
        compared, failures, _ = acceptance(CR_DOSSIERS, registry, [Path(a) for a in args] or None)
        return 1 if failures else 0

    compared = failures = diffs = 0
    for dossier_root, registry, whole in DOMAINS:
        c, f, d = acceptance(dossier_root, registry, whole=whole)
        compared += c; failures += f; diffs += d

    print(f"  {compared - failures}/{compared} artifacts reproduced across {len(DOMAINS)} domain(s)"
          f"   ({diffs} field difference(s))")

    missing = uncovered()
    for root in missing:
        print(f"  UNCOVERED  {root.relative_to(WORKSPACE)} determines artifacts and is compared "
              f"against nothing")
    if missing:
        print(f"\n  {len(missing)} dossier root(s) outside DOMAINS — add them, or say why not")
    return 1 if failures or missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
