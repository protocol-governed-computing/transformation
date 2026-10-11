"""Construction identity (REBUILD_CHARTER §5, item 4): the rebuild renders what the oracle renders.

1. Each side renders every domain's dossier sequence, exactly as its `construction_acceptance`
   does: later dossiers override earlier ones, and re-points move references.
   - The oracle reads the fixture dossiers in its own worktree, and the delivered dossiers where
     they were delivered, in the form they were approved in.
   - The rebuild reads its converted fixtures and its test copies of the delivered dossiers.
2. For each domain, both must render the same artifacts with identical Machine blocks.

    python scripts/rebuild/construction.py

Exit 0 when every rendered artifact agrees, 1 otherwise.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

REBUILD = Path(__file__).resolve().parents[2]
WORKSPACE = REBUILD.parent
ORACLE = Path.home() / "pgc-oracle" / "transformation"



def dump(side: Path) -> dict:
    """Every artifact the side's construction renders, by registry and code."""
    sys.path.insert(0, str(side / "scripts" / "testbed"))
    import construction_acceptance as ca
    from transformation.build import sameness
    from transformation.build.render import bare, cell, render_all, rows, supersessions

    out: dict[str, dict] = {}
    for root, registry, _ in ca.DOMAINS:
        # The oracle names its delivered roots under its own parent, which holds no domains.
        if not root.exists() and root.is_relative_to(ca.WORKSPACE):
            root = WORKSPACE / root.relative_to(ca.WORKSPACE)
        rendered: dict[str, dict] = {}
        for dossier in ca.sequence(root):
            p7 = ca.registers(next(dossier.glob("p7_*.md")))
            p8 = ca.registers(next(dossier.glob("p8_*.md")))
            for artifact in render_all(p7, p8):
                rendered[bare(artifact["machine"]["fqdn"])] = artifact["machine"]
            successor = sameness.successors(supersessions(p7))
            for row in rows(p7, "existing_inventory"):
                code = bare(cell(row, "FQDN"))
                if cell(row, "Action").upper() == "REPOINT" and code in rendered:
                    rendered[code] = ca.repointed({"machine": rendered[code]}, successor)["machine"]
        out[str(Path(registry).relative_to(ca.WORKSPACE))] = rendered
    return out


def _side(cwd: Path, pythonpath: str | None) -> dict:
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    if pythonpath:
        env["PYTHONPATH"] = pythonpath
    done = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--dump", str(cwd)], cwd=cwd,
                          env=env, capture_output=True, text=True)
    if done.returncode:
        raise SystemExit(f"{cwd} failed:\n{done.stderr[-3000:]}")
    return json.loads(done.stdout)


def _differences(a, b, path: str = "") -> list[str]:
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b), key=str):
            if k not in a or k not in b:
                out.append(f"{path}.{k}: {'only rebuild' if k not in a else 'only oracle'}")
            else:
                out += _differences(a[k], b[k], f"{path}.{k}")
        return out
    if a != b:
        return [f"{path}: oracle {json.dumps(a, default=str)[:120]} / rebuild {json.dumps(b, default=str)[:120]}"]
    return []


def main(argv: list[str]) -> int:
    if "--dump" in argv:
        json.dump(dump(Path(argv[argv.index("--dump") + 1])), sys.stdout, default=str)
        return 0
    was, now = _side(ORACLE, str(ORACLE)), _side(REBUILD, None)
    differ, total = 0, 0
    for registry in sorted(set(was) | set(now)):
        a, b = was.get(registry, {}), now.get(registry, {})
        for code in sorted(set(a) | set(b)):
            total += 1
            if code not in a or code not in b:
                differ += 1
                print(f"  {'ONLY REBUILD' if code not in a else 'ONLY ORACLE '}  {registry}  {code}")
                continue
            diffs = _differences(a[code], b[code])
            if diffs:
                differ += 1
                print(f"  DIFF  {registry}  {code}")
                for line in diffs[:6]:
                    print(f"          {line}")
    if differ:
        print(f"\nCONSTRUCTION DIFFERS — {differ} of {total} artifact(s)")
        return 1
    print(f"CONSTRUCTION IDENTICAL — {total} artifacts over {len(was)} domains, rendered alike")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
