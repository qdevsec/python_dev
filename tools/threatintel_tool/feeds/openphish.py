import requests

"""
OpenPhish feed module
Fetches the feed and normalizes IOCs (URLs)

Features:

1. Normalized - IOC return these exact fields

{
    "type": "ip" | "url" | "domain",
    "value": "<IOC value>",
    "source": "<feed name>"
}

2. Error handling with request exception

3. CSV parsing, using csv.DictReader to handle csv fees

4. Can test feed directly with python feeds/openphish.py

"""

FEED_URL = "https://openphish.com/feed.txt"
SOURCE_NAME = "OpenPhish"

def fetch_and_parse():
    """
    Fetch the OpenPhish feed (TXT, one URL per line)
    Returns: List[dict]: Each dict has keys: "type", "value", "source" 
    """
    iocs = []

    try:
        response = requests.get(FEED_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch OpenPhish feed: {e}")
        return iocs
    
    lines = response.text.splitlines()

    for line in lines:
        url = line.strip()
        if url and not url.startswith("#"):
            iocs.append({
                "type": "url",
                "value": url,
                "source": SOURCE_NAME
            })
    
    return iocs

if __name__ == "__main__":
    for ioc in fetch_and_parse():
        print(ioc)