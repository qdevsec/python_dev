import re
import json
import base64
import datetime
from collections import defaultdict

"""
from apt campaign logs ~85k events

detect base64 encoded commands

lsass activity

beaconing activity

"""

pattern = r'powershell.exe'
file_path = "test/apt_campaign_logs.jsonl"
output_file = "alerts.jsonl"

### the helper functions
def try_base64_decode(s):
    # adding try except to handle potential errors
    try:
        decoded = base64.b64decode(s).decode("utf-8", errors="ignore")

        if any(c.isalpha() for c in decoded):
            return decoded
    except Exception:
        pass
    return None

def parse_timestamp(ts):
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except Exception:
        return None


# --- Detection State

beacon_tracker = defaultdict(list) # host -> list of timestamps

# 1 . detecting base64 events, decoding it
def detect_base64_command(event):
    cmd = event.get("command", "") or event.get("cmdline", "")
    
    # powershell =  event.get("powershell.exe", "")
    
    decoded = try_base64_decode(cmd)

    if decoded:
        return {
            "type": "base64_obfuscation",
            "decoded_command": decoded
        }
    
    return None

# 2 . detect lsass activity
def detect_lsass_access(event):
    text = json.dumps(event).lower()

    indicators = [
        "lsass",
        "sekurlsa",
        "mimikatz",
        "procdump",
        "comsvcs.dll"
    ]

    if any(ind in text for ind in indicators):
        return {
            "type": "credential_dumping_lsass",
            "matched_indicators": [i for i in indicators if i in text]
        }
    
    return None

# 3. Beaconing detection activity
def detect_beaconing(event):
    host = event.get("host", "unknown")
    ts_raw = event.get("timestamp")

    ts = parse_timestamp(ts_raw)
    if not ts:
        return None
    
    timestamps = beacon_tracker[host]
    timestamps.append(ts)

    if len(timestamps) < 4:
        return None

    # compute intervals (seconds)
    intervals = [
        (timestamps[i] - timestamps[i - 1]).total_seconds() for i in range(1, len(timestamps))
    ]

    # check last few intervals for ~180 +- 30 seconds
    recent = intervals[-5:]

    matches = [150 <= i <= 210 for i in recent]

    if len(recent) >= 3 and sum(matches) >= 3:
        return {
            "type": "c2_beaconing",
            "intervals": recent
        }
    
    return None

# main pipeline

def process_file():
    alerts = []

    # clean line if no line continue
    with open(file_path) as file:
        # print(file)
        for line in file:
            # print(line)
            line = line.strip()
            if not line:
                continue

            # may throw error, wrapping in try except
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            detections = []

            # the detections to run
            b64_hit = detect_base64_command(event)
            if b64_hit:
                detections.append(b64_hit)

            lsass_hit = detect_lsass_access(event)
            if lsass_hit:
                detections.append(lsass_hit)

            beacon_hit = detect_beaconing(event)
            if beacon_hit:
                detections.append(beacon_hit)

            # generate alert in any detection
            if detections:
                alert = {
                    "timestamp": event.get("timestamp"),
                    "host": event.get("host"),
                    "detections": detections,
                    "raw_event": event
                }
                alerts.append(alert)

    # will write out alerts to output file
    with open(output_file, 'a') as file:
        for alert in alerts:
            file.write(json.dumps(alert) + "\n")
        
# start
process_file()


        