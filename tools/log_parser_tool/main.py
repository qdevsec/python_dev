import re
from utils.re_patterns import IOC_PATTERNS
from utils.ml_util import *

data = []

def parser(ans, path):
    log_line = "User downloaded malware.exe and connected to 192.168.1.100 at 2023-04-05T12:34:56Z"

    # Extract IPs
    # data = re.findall(IOC_PATTERNS[ans], log_line)

    with open(path, "r") as file:
        for line in file:
            match = re.search(IOC_PATTERNS[ans], line)

    # Extract suspicious files
    # files = [m[0] for m in re.findall(IOC_PATTERNS["suspicious_file"], log_line)]

    # Extract timestamps
    # timestamps = re.findall(IOC_PATTERNS["iso8601"], log_line)

    for i in data:
        print(f"{i}")

def start():
    ans = input(f"What pattern do you want to search for: {IOC_PATTERNS.keys()}: ")
    path = input("Point me to the file: ")
    parser(ans, path)

##
start()