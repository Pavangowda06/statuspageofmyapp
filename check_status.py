import urllib.request
import urllib.error
import json
from datetime import datetime, timezone

services = [
    {"name": "Azure Web App", "url": "https://your-web-app.azurewebsites.net"},
    {"name": "Azure Function", "url": "https://your-function.azurewebsites.net/api/health"},
]

results = []
for s in services:
    try:
        start = datetime.now()
        resp = urllib.request.urlopen(s["url"], timeout=5)
        delta = (datetime.now() - start).total_seconds() * 1000  # in ms
        status = "up" if resp.getcode() == 200 else "down"
    except urllib.error.URLError:
        status = "down"
        delta = None
    except Exception:
        status = "down"
        delta = None

    results.append({
        "name": s["name"],
        "status": status,
        "response_time_ms": round(delta, 2) if delta else None,
        "checked_at": datetime.now(timezone.utc).isoformat()
    })

with open("status.json", "w") as f:
    json.dump(results, f, indent=2)
