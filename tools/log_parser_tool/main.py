import re
from pathlib import Path
from utils.re_patterns import IOC_PATTERNS
from utils.ml_util import *

data = []

def parser(ans, path):
    log_line = "User downloaded malware.exe and connected to 192.168.1.100 at 2023-04-05T12:34:56Z"
    print("#------------ Starting -----------------")
    # Extract IPs

    log_pattern = re.compile(IOC_PATTERNS[ans])

    # format path
    f_path = Path(path).expanduser().resolve()
    print(f"{f_path}")

    try:
        with open(f_path, "r") as file:
            print("....analyzing file")

            # matches = re.findall(IOC_PATTERNS[ans], file)
            
            # iterates directly over the file object (lazy loading)
            for line_number, line in enumerate(file, 1):
                if log_pattern.search(line):
                    data.append(f"Line {line_number}: {line}")
                
        # Extract suspicious files
        # files = [m[0] for m in re.findall(IOC_PATTERNS["suspicious_file"], log_line)]

        # Extract timestamps
        # timestamps = re.findall(IOC_PATTERNS["iso8601"], log_line)
    except FileNotFoundError:
        print("Error: The file does not exist")
    except PermissionError:
        print("Error: You do not have permission to access this file")
    except OSError as e:
        print(f"Error: A system error occurred: {e}")


    for i in data:
        print(f"{i}")

def start():
    ans = input(f"What pattern do you want to search for: {IOC_PATTERNS.keys()}: ")
    path = input("Point me to the file: ").strip()
    parser(ans, path)

##
start()