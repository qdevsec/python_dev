import re
import pandas as pd

log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\[(?P<time>.*?) \+0000\].*?\" (?P<status>\d+)'
log_pattern2 = r'401'
pattern = r''


def parse_and_detect(logfile, threshold=10):
    # This Regex matches: IP, Timestamp, and Status Code
    # Example: 10.0.0.99 - - [23/Mar/2026:20:50:45 +0000] "POST /login..." 401

    
    data = []
    
    with open(logfile, "r") as f:
        for line in f:
            match = re.search(log_pattern2, line)
            if match:
                # entry = match.groupdict()
                entry = line
                #debug
                print(f"Parsed Entry: {entry}")
                # Only keep failed logins (HTTP 401 Unauthorized)
                # if entry['status'] == '401':
                #     entry['time'] = pd.to_datetime(entry['time'], format='%d/%b/%Y:%H:%M:%S')
                #     print(f"here is the line: {entry['ip']} at {entry['time']}")
                #     data.append(entry)
                data.append(entry)

    df = pd.DataFrame(data)
    if df.empty:
        return "No failed logins found."

    # Identify Brute Force: Count failures per IP in 1-minute buckets
    # df.set_index('time', inplace=True)
    # results = df.groupby('ip').resample('1min').size().reset_index(name='failure_count')
    
    # Flag IPs that exceed the threshold
    # alerts = results[results['failure_count'] >= threshold]

    print(df)
    return df
    # return alerts

# Execute
alerts = parse_and_detect("access.log")
if isinstance(alerts, pd.DataFrame) and not alerts.empty:
    print(f"🚨 BRUTE FORCE ALERT DETECTED and here are the lines 🚨: {len(alerts)},")
    print("Details: Please investigate the following IP addresses for potential brute force attacks and determine if false postive")
    print(alerts)
else:
    print("Log analysis complete. No threats found.")