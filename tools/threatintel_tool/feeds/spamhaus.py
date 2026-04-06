"""
Spamhaus DROP list module
Fetches the feed and normalizes IOCs (IP ranges)
"""

import requests

FEED_URL = "https://www.spamhaus.org/drop/drop.txt"
SOURCE_NAME = "Spamhaus DROP"

def fetch_and_parse():
    """
    Fetch the Spamhaus DROP feed (TXT, one IP/CIDR per line)
    Returns: List[dict]: Each dict has keys: "type", "value", "source"
    """

    iocs = []

    try:
        response = requests.get(FEED_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch Spamhaus feed: {e}")
        return iocs
    
    lines = response.text.splitlines()

    for line in lines:
        line = line.strip()
        if line and not line.startswith(";"): # 
            # Split line to extract IP/CIDR before comment
            ip_cidr = line.split(";")[0].strip()
            if ip_cidr:
                iocs.append({
                    "type": "ip",
                    "value": ip_cidr,
                    "source": SOURCE_NAME
                })

    return iocs

if __name__ == "__main__":
    for ioc in fetch_and_parse():
        print(ioc)