#!/usr/bin/python3
"""Log parsing and metrics computation."""
import sys


total_size = 0
status_counts = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            size = int(parts[-1])
            code = parts[-2]

            total_size += size
            if code in status_counts:
                status_counts[code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_counts):
                    if status_counts[code] > 0:
                        print(f"{code}: {status_counts[code]}")

        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")
    sys.exit(0)
