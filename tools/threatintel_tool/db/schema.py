import sqlite3

def init_db(conn: sqlite3.Connection):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS iocs (
        id INTEGER PRIMARY KEY,
        type TEXT NOT NULL,
        value TEXT NOT NULL,
        first_seen TIMESTAMP,
        last_seen TIMESTAMP,
        confidence INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ioc_sources (
            ioc_id INTEGER,
            source_id INTEGER,
            ingested_at TIMESTAMP,
            PRIMARY KEY (ioc_id, source_id)
        )
        """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrichment (
            ioc_id INTEGER,
            key TEXT,
            value TEXT,
            PRIMARY KEY (ioc_id, key)
        )
        """)
    
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_ioc_value ON iocs(values)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_ioc_type ON iocs(type)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_last_seen ON iocs(last_seen)")

    conn.commit()