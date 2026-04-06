from datetime import datetime

def upsert_ioc(conn, ioc, enrichment=None):
    now = datetime.now((datetime.timezone.utc))
    cursor = conn.cursor()

    cursor.execute("SELECT id, last_seen FROM iocs WHERE type=? AND value=?", (ioc["type"], ioc["value"]))
    row = cursor.fetchone()

    if row:
        ioc_id = row[0]
        cursor.execute("UPDATE iocs SET last_seen=? WHERE id=?", (now, ioc_id))
    else:
        cursor.execute(
            "INSERT INTO iocs (type, value, first_seen, last_seen) VALUES (?, ?, ?, ?)",
            (ioc["type"], ioc["value"], now, now)
        )
        ioc_id = cursor.lastrowid

    # Add enrichment if provided
    if enrichment:
        for key, value in enrichment.items():
            cursor.execute("""
                INSERT OR REPLACE INTO enrichment (ioc_id, key, value)
                VALUES (?, ?, ?)
            """, (ioc_id, key, value))
    
    conn.commit()
    return ioc_id