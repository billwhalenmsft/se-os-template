"""Run the customer-free outcome-framing agent from the command line."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agents import AgentRequest, OutcomeFramerAgent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", help="Synthetic or authorized request to frame")
    parser.add_argument("--owner", default="Demo Operator", help="Local experiment owner")
    args = parser.parse_args()

    result = OutcomeFramerAgent().run(
        AgentRequest(text=args.request, context={"owner": args.owner})
    )
    print(json.dumps({"agent": result.agent, **result.output}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
