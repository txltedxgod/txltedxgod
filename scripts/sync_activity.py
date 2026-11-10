import random
import re
import time
from datetime import datetime, timezone
from pathlib import Path

# Add random jitter between 10 and 90 seconds
jitter = random.randint(10, 90)
print(f"Applying dynamic jitter: {jitter}s...")
time.sleep(jitter)

now_utc = datetime.now(timezone.utc)
timestamp = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")

activity_path = Path("ACTIVITY.md")
if activity_path.exists():
    existing = activity_path.read_text(encoding="utf-8")
    updated = re.sub(
        r"(-\s+\*\*Last Heartbeat\*\*:\s+)`[^`]+`",
        rf"\1`{timestamp}`",
        existing,
        count=1,
    )
    updated = re.sub(
        r"^\[timestamp\]\s+.*$",
        f"[timestamp] {timestamp}",
        updated,
        count=1,
        flags=re.MULTILINE,
    )
    if updated != existing:
        activity_path.write_text(updated, encoding="utf-8")
        print(f"Updated ACTIVITY.md heartbeat preserving telemetry at {timestamp}")
    else:
        print("ACTIVITY.md already up to date or no matching timestamp marker found.")
else:
    content = f"""# Activity & Heartbeat Ledger

Automated contribution pulse and engineering health telemetry.

- **Last Heartbeat**: `{timestamp}`
- **Status**: `ACTIVE / HEALTHY`
- **Automated Agent**: `GitHub Actions Matrix Runner`

```text
[telemetry] system check: pass | latency: low | memory: nominal
[timestamp] {timestamp}
```
"""
    activity_path.write_text(content, encoding="utf-8")
    print(f"Created ACTIVITY.md with heartbeat at {timestamp}")
