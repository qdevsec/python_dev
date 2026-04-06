import re
from utils.re_patterns import IOC_PATTERNS


def parser(ans):
    log_line = "User downloaded malware.exe and connected to 192.168.1.100 at 2023-04-05T12:34:56Z"

    # Extract IPs
    ips = re.findall(IOC_PATTERNS["ipv4"], log_line)

    # Extract suspicious files
    files = [m[0] for m in re.findall(IOC_PATTERNS["suspicious_file"], log_line)]

    # Extract timestamps
    timestamps = re.findall(IOC_PATTERNS["iso8601"], log_line)

    print("IPs:", ips)
    print("Files:", files)
    print("Timestamps:", timestamps)

def start():
    ans = input(f"What pattern do you want to search for: {IOC_PATTERNS.keys()}: ")
    parser(ans)

##
start()