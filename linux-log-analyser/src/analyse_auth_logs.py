#!/usr/bin/env python3
"""Summarise failed SSH password attempts in a synthetic authentication log."""

from collections import Counter
from pathlib import Path
import re
import sys

FAILED_PASSWORD = re.compile(r"Failed password for .* from (?P<ip>\S+) port \d+")


def analyse_log(path: Path, threshold: int = 3) -> tuple[int, Counter]:
    """Return total matched failures and counts by source IP."""
    failures_by_ip = Counter()
    total_failures = 0

    with path.open("r", encoding="utf-8", errors="replace") as log_file:
        for line in log_file:
            match = FAILED_PASSWORD.search(line)
            if match:
                total_failures += 1
                failures_by_ip[match.group("ip")] += 1

    return total_failures, Counter(
        {ip: count for ip, count in failures_by_ip.items() if count >= threshold}
    )


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} <path-to-auth.log>", file=sys.stderr)
        return 2

    log_path = Path(sys.argv[1])
    if not log_path.is_file():
        print(f"Error: file not found: {log_path}", file=sys.stderr)
        return 2

    total, flagged = analyse_log(log_path)
    print(f"Matched failed-password events: {total}")
    print("Sources with 3 or more failures:")
    if not flagged:
        print("  None")
    else:
        for ip, count in flagged.most_common():
            print(f"  {ip}: {count} failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
