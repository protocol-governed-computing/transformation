"""Judge a list of documents through `tc phase check`, in one process, and print the verdicts.

Version-agnostic: it drives the CLI and nothing else, so the same script judges with the oracle
(`PYTHONPATH=~/pgc-oracle/transformation`) and with the rebuild. Every document is judged by the
working tree's declared rules against one frozen composition.

    judge.py SNAPSHOT ROOT < cases.json > verdicts.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from click.testing import CliRunner

from transformation.cli import main as tc


def main(argv: list[str]) -> int:
    snapshot, root = Path(argv[0]), Path(argv[1])
    runner = CliRunner()
    out = []
    for case in json.load(sys.stdin):
        args = ["phase", "check", str(root / case["doc"]), "--phase", case["phase"],
                "--snapshot", str(snapshot), "--rules", "declared", "--json"]
        for phase, path in case["priors"].items():
            args += ["--prior", f"{phase}={root / path}"]
        result = runner.invoke(tc, args)
        try:
            verdict = json.loads(result.output)
        except json.JSONDecodeError:
            verdict = {"error": (result.output or repr(result.exception))[-2000:]}
        out.append({"doc": case["doc"], "result": verdict})
    json.dump(out, sys.stdout, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
