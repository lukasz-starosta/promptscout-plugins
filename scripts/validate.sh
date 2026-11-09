#!/usr/bin/env bash
# Validate the PromptScout Claude plugin and the marketplace, then run the static checks.
# Usage (from anywhere): ./scripts/validate.sh
# Needs Claude Code 2.1.281 or later (`claude` on PATH) and Python 3.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== claude plugin validate --strict ./claude/promptscout"
claude plugin validate --strict ./claude/promptscout

echo "== claude plugin validate --strict . (marketplace)"
claude plugin validate --strict .

echo "== python3 -m unittest discover -s tests -v"
python3 -m unittest discover -s tests -v
