# Operationalizing Detection Logic

## What was automated
SQL-based detection logic for repeated failed logons

## Operational assumptions
- This report is generated once a day.
- Thresholds (failures count) require tuning.

## Future improvements
- Add time-window logic (e.g., failures within 5 minutes)
- Add context