#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

# Run the pytest tests with JSON report output
pytest /tests/test_outputs.py -v --tb=short --json-report --json-report-file=/logs/verifier/ctrf.json

if [ $? -eq 0 ]; then
  echo "1" > /logs/verifier/reward.txt
else
  echo "0" > /logs/verifier/reward.txt
fi
