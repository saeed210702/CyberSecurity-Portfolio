# Linux Log Analyser

**Status:** Starter script included  
**Focus:** Python, log parsing, basic detection logic, and testing.

## Objective
Parse a synthetic authentication log and summarise failed logins by source IP. This is a learning exercise, not a production detection tool.

## Run locally
From this directory:

```bash
python3 src/analyse_auth_logs.py ../soc-incident-investigation/sample-logs/auth.log
```

If your folder layout differs, pass the correct path to `auth.log`.

## What it currently does
- Counts matching failed-password events by source IP.
- Prints source IPs with three or more failures.
- Reports the total number of matching failed events.

## Improvements to implement
- Add unit tests.
- Parse timestamps and group events into time windows.
- Add configurable thresholds.
- Output JSON or CSV.
- Handle malformed lines and document parsing limitations.
- Add a test report with expected and actual results.

## Limitations
The script uses simple text matching and is intended for the provided synthetic log format. It may miss other log formats and should not be used as a sole basis for incident decisions.
