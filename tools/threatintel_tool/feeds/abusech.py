"""
Abuse.ch Feodo Tracker feed module
Fetches the CSV feed and normalizes IOCs

Features:

1. Normalized - IOC return these exact fields

{
    "type": "ip" | "url" | "domain",
    "value": "<IOC value>",
    "source": "<feed name>"
}

2. Error handling with request exception

3. CSV parsing, using csv.DictReader to handle csv fees

4. Can test feed directly with python feeds/abusech.py

"""

import requests
import csv
from io import StringIO
import pandas as pd

FEED_URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.csv"
SOURCE_NAME = "Abuse.ch Feodo Tracker"


def fetch_and_parse():
    """
    get from Abuse.ch csv feed and return a list of IOCs
    Returns: List[dict]: Each dict has keys: "type", "value", "source"
    """
    
    iocs = []

    try:
        print("starting....")
        response = requests.get(FEED_URL, timeout=10)
        response.raise_for_status()
        print(f"{response.status_code}")
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch Abuse.ch feed: {e}")
        return iocs
    
    content = response.text.splitlines()
    # print(f"{content}")
    # csv_reader = csv.DictReader(StringIO(content))
    # df = pd.DataFrame(content)
    # print(df)

    # pandas implementation
    # for value in df['dest_ip']:
    #     print("pandas way")
    #     print(value)

    for row in content:
        # Skip comment lines
        # print(f"{row}")
        if row.startswith('#') or not row: # if first part is true of row is empty
            print("skipping iteration...")
            continue

        sections = row.split(",")

        # print(f"ip: {sections[1]}")
        ip = sections[1]
        if ip:
            iocs.append({
                "type": "ip",
                "value": ip,
                "source": SOURCE_NAME
            })

    # Debug    
    # print(f"{iocs}")
    return iocs

fetch_and_parse()

if __name__ == "__main__":
    # Test run
    for ioc in fetch_and_parse():
        print("test run...")
        print(ioc)