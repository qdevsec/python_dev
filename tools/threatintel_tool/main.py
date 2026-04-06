"""
Threat Intelligence Pipeline Orchestrator

Pipeline steps:
1. Fetch feeds
2. Validate IOCs
3. Enrich (GeoIP, ASN, reputation)
4. Upsert into DB with timestamps
5. Calculate confidence based on sources
6. Export to JSON / SIEM-friendly format
"""

import sqlite3
from datetime import datetime
from db.schema import init_db
from db.operations import upsert_ioc
from validation.validators import validate_ioc
from enrichment.geoip import enrich_ip
from utils.export import export_to_json
from utils.patterns import IOC_PATTERNS 

# Feed modules (you need to implement fetch_and_parse in each)
from feeds import abusech, openphish, spamhaus


def calculate_confidence(num_sources, last_seen):
    """Simple confidence scoring based on number of sources and recency."""
    score = 0
    # Source weight
    score += min(num_sources * 20, 60)
    # Recency boost
    age_hours = (datetime.now((datetime.timezone.utc)) - last_seen).total_seconds() / 3600
    if age_hours < 24:
        score += 30
    elif age_hours < 72:
        score += 20
    else:
        score += 10
    return min(score, 100)

def main():
    # Connect to DB
    conn = sqlite3.connect("threatintel.db")
    init_db(conn)

    # List of feed modules
    feeds = [abusech, openphish, spamhaus]

    print("[INFO] Starting Threat Intel Pipeline...")

    total_iocs = 0

    for feed in feeds:
        print(f"[INFO] Fetching feed: {feed.__name__}")
        try:
            iocs = feed.fetch_and_parse() # Each feed should return list of dicts: {"type", "value", "source"}
        except Exception as e:
            print(f"[ERROR] Failed to fetch {feed.__name__}: {e}")
            continue

        for ioc in iocs:
            if not validate_ioc(ioc["type"], ioc["value"]):
                continue  # Skip invalid IOCs

            # Enrich if IP
            enrichment = {}
            if ioc["type"] == "ip":
                enrichment = enrich_ip(ioc["value"])

            # Upsert IOC into DB
            ioc_id = upsert_ioc(conn, ioc, enrichment)

            # Optional: confidence scoring (simple example: number of sources = 1 for now)
            last_seen = datetime.now((datetime.timezone.utc))
            confidence = calculate_confidence(num_sources=1, last_seen=last_seen)

            # Update confidence in DB
            cursor = conn.cursor()
            cursor.execute("UPDATE iocs SET confidence=? WHERE id=?", (confidence, ioc_id))
            conn.commit()

            total_iocs += 1
    
    print(f"[INFO] Total IOCs processed: {total_iocs}")

    # Export to JSON
    export_to_json(conn, "iocs.json")
    print("[INFO] Exported IOCs to iocs.json")

    conn.close()
    print("[INFO] Pipeline completed successfully.")

if __name__ == "__main__":
    main()