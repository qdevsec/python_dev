import pandas as pd
import requests

######## Free threat intel feeds
# 1. AlienVault OTX (Open Threat Exchange)
#   - API + STIX / TAXII support
#   - General threat hunting
#   - API-friendly ingestion
#
# 2. Abuse.ch (ThreatFox, Feodo Tracker, SSLBL)
#   - High quality malware & botnet intelligence
#   - Examples:
#       - ThreatFox -> malware IOCs
#       - Feodo Tracker -> botnet C2 servers
#   - Frequently updated
#
# 3. Spamhaus
#   - Tracks:
#       - Spam sources
#       - botnets
#       - malicious IP ranges
#   - Good for Network filtering / blocklists
# 
# 4. OpenPhish
#   - Real-time phishing URLs
#   - Simple TXT feed
#   - Best for: Phishing detection systems
# 
# 5. Emerging Threats (ET Open)
#   - Maintained by Proofpoint
#   - Categorized malicious IPs / domains with confidence scores
#   - Best for: IDS / IPS (Suricata / Snort rules)
# 
# 6. Shadowserver Foundation
#   - Nonprofit collecting:
#       - malware
#       - botnet activity
#       - vulnerable services
#   - Best for: Infrastructure-level intelligence
# 
# 7. CIRCL / MISP OSINT feeds
#   - Structured feeds for MISP platform 
#   - Includes multiple aggregated source
#   - Best for: Structured CTI pipelines
#
# 8. FireHOL IP lists
#   - Aggregated blocklists from multiple sources
#   - Best for: Quick enrichment / blocking
#
# 9. GreyNoise (community / free tier)
#   - Focuses on "internet noise" vs real threats
#   - Best for: reducing false positives
#
# 10. Aggregators (huge value)
#   - ThreatFeeds.io -> directory of feeds
#   - OpenCTI -> integrates many feeds
#   - MISP -> ingest + share feeds
#   - Best for: Real-world pipelines (not just raw feeds)

# free urls
# https://www.spamhaus.org/drop/drop.txt <-- 
# https://rules.emergingthreats.net/blockrules/compromised-ips.txt <-- 
# https://urlhaus.abuse.ch/downloads/text/ 

def dual_feodo_ophish():
    feeds = {
        "feodo": "https://feodotracker.abuse.ch/downloads/ipblocklist.csv",
        "openphish": "https://openphish.com/feed.txt",
    }

    data = {}

    for name, url in feeds.items():
        data[name] = fetch_feed(name, url)
    
    # preview
    for source, lines in data.items():
        print(f"\n--- {source} ---")
        print(f"number: {len(lines)}")
        print(lines[:15])

def fetch_feed(name, url):
    try:
        res = requests.get(url, timeout=10)
        return res.text.splitlines()
    except Exception as e:
        print(f"Error fetching {name}: {e}")
        return []
    

def get_ips_blocked(choice):
    url1 = "https://feodotracker.abuse.ch/downloads/ipblocklist.csv"
    url2 = "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset"

    print(f"user's choice: {choice}")

    print("...now requesting ip blocked lists...")

    lines = []
    ips = []

    if choice == "foed":
        response = requests.get(url1)
        print(f"status code: {response.status_code}")
        lines = response.text.splitlines()
    elif choice == "firehol":
        response = requests.get(url2)
        print(f"status code: {response.status_code}")
        lines = response.text.splitlines()        

    

    # create a dataframe
    df = pd.DataFrame(lines)
    df.to_csv('feed_info_blocked_ips.csv', index=False)

    # print(f"choice {choice}: {lines}")
    
    # parse lines
    for line in lines:
        if line.startswith('#') or not line:
            continue
        
        parts = line.split(",")
        print({choice})


        if choice == "foed":
            print(f"line 98 {choice}")
            print(parts[1])
            ip = parts[1]  # depends on format
            ips.append(ip)
        elif choice == "firehol":
            print(parts)
            ip = parts
            ips.append(ip)

        # print(f"choice: {choice} parts: {parts}")

    # # get the first 10 (0:10), exclusive stop so 0 - 9
    print(ips[:10])
    print(f"how many ips? {len(ips)}")

    # create a dataframe 
    df = pd.DataFrame(ips)
    # df.to_json('blocked_list.json') <-- save to json
    # save it to a csv
    df.to_csv('blocked_list.csv', na_rep='N/A') 

    # with open("blocked_list.csv", 'w') as file:
        # pass        


def open_Phish():
    url = "https://openphish.com/feed.txt"

    urls = requests.get(url).text.splitlines()
    print(f"status code: {requests.get(url).status_code}")
    # print(f"text: {requests.get(url).text}")
    print(f"number of urls: {len(urls)}")

    print(f"the 1st 10: {urls[:10]}")

    # create a dataframe 
    df = pd.DataFrame(urls)
    # write to csv
    df.to_csv('phish_urls.csv')    


# select function based on user input
def selection(ans):
    print("...now starting selection...")
    if ans == "blocked_ips":
        get_ips_blocked(choice=input("foed or firehol: "))
    if ans == "open_phish":
        open_Phish()
    if ans == "dual_f_op":
        dual_feodo_ophish()
    

def start():
    ans = input("📰 What kind of intel? 🗞️: \n" \
                "Choose one of the following \n"
                "blocked_ips open_phish dual_f_op: ")
    
    selection(ans)

# Begin program
start()