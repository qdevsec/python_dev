import json

def export_to_json(conn, filename="iocs.json"):
    cursor = conn.cursor()
    cursor.execute("SELECT type, value, first_seen, confidence FROM iocs")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "type": row[0],
            "value": row[1],
            "first_seen": row[2],
            "last_seen": row[3],
            "confidence": row[4]
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=2, default=str)

def to_siem_event(ioc):
    return {
        "@timestamp": ioc["last_seen"],
        "threat.indicator.type": ioc["type"],
        "threat.indicator.value": ioc["value"],
        "threat.indicator.confidence": ioc["confidence"],
        "threat.feed.name": ioc.get("source", "unkown")
    }
