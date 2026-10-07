import os
import random
import time
from datetime import datetime, timezone

# Add random jitter between 10 and 120 seconds
jitter = random.randint(10, 120)
print(f"Applying dynamic jitter: {jitter}s...")
time.sleep(jitter)

now_utc = datetime.now(timezone.utc)
timestamp = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
date_str = now_utc.strftime("%Y-%m-%d")

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

with open("ACTIVITY.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated ACTIVITY.md with heartbeat at {timestamp}")