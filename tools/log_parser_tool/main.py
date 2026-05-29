import re
import math
from collections import Counter
from pathlib import Path
from tabulate import tabulate
from utils.re_patterns import IOC_PATTERNS
from utils.ml_util import *
from InquirerPy import inquirer

data = []
lines = []

# deprecated, used in line 152 when IOCs were presented in  
# table = [(i,k) for i, k in enumerate(sorted(IOC_PATTERNS.keys()), 1)]

# detect randomness
def shannon_entropy(data):
    if not data:
        return 0
    
    counts = Counter(data)
    probs = [v / len(data) for v in counts.values()]

    return - sum(p * math.log2(p) for p in probs)

# extract features also known as the ioc names
#  
def extract_features(line, patterns):
    features = {}

    for name, pattern in patterns.items():
        matches = re.findall(pattern, line)

        features[f"{name}_count"] = len(matches)

    features["line_length"] = len(line)
    # lightweight statistical signal about the structure and content of the log line
    features["digit_ratio"] = (
        sum(c.isdigit() for c in line) / max(len(line), 1)
    )

    features["entropy"] = shannon_entropy(line)

    # print(f"\n features:\n {features} \n")

    return features

def parser(ans, path):


    # may have multiple occurrences
    items_all = []

    findall_results = []

    print("#------------ Starting -----------------\n")
    # Extract IPs

    log_pattern = re.compile(IOC_PATTERNS[ans])

    # format path
    f_path = Path(path).expanduser().resolve()
    
    # debug: path to file
    # print(f"{f_path}")

    try:
        with open(f_path, "r") as file:
            print("\n\n")
            print("....analyzing file")
            print("\n\n")

            # matches = re.findall(IOC_PATTERNS[ans], file)
            
            # iterates directly over the file object (lazy loading)
            for line_number, line in enumerate(file, 1):
                findall = log_pattern.findall(line)

                # extend instead of append because extend() unpacks the list (findall() produces a list) and appends value
                findall_results.extend(findall)

                if log_pattern.search(line):
                    data.append(f"Line {line_number}: {line}")
                    lines.append(line)

                    for i in findall:
                        items_all.append(i)
                
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


    # for i in data:
    #     print(f"{i}")

    records = [
        extract_features(line, IOC_PATTERNS)
        for line in lines
    ]

    # prompt user about ML capability
    ml_use = input(f"Would you like to use ml utilities? [anomaly, predict, vectorize, plurality]: ").lower()
        # Use ML
    if ml_use == "anomaly":
        # print(lines)
        # print(f"all items: \n{items_all}\n")

        anomaly(lines)
    if ml_use == "predict":
        # print(f"all items: \n{items_all}\n")

        # print(records)
        df_lines = pd.DataFrame(records)
        # print(df_lines.head())
        # print(df_lines.describe())
        predict_plot(lines, df_lines)
    if ml_use == "vectorize":
        # print(f"all items: \n{items_all}\n")

        tfid_vectorizer(lines)
    if ml_use == "plurality":
        # print(f"main: {findall_results}")
        plurality(findall_results)


def start():
    
    ans = ""

    # enable user to filter if they dont know the ioc exactly, or present neat table of iocs
    choice = input("\n\nDo you prefer to provide an ioc (partial or whole) or to be present with a table? [provide, present]: ").lower()

    if choice == 'provide':
        search = input("Filter IOC types (blank for all) or pow | Pow  for [powershell_encoded, powershell_download] : ").lower()

        filtered = [
            i for i in IOC_PATTERNS.keys()
            if search in i.lower()
        ]

        if not filtered:
            print("No matches found, try again ")
            a = input("Do you want to try again? ").lower()
            if a == 'yes':
                start()
            else:
                print("Okay bye.")
                exit()
        
        print("\nResults: ")
        for i, item in enumerate(filtered, 1):
            print(f"{i}. {item}")

        num = input("\nSelect IOC (type the number): ")
        ans = filtered[int(num) - 1]
    
    if choice == 'present':
        b = inquirer.fuzzy(
            message="here are the IOCs, use the up or down arrow keys to peruse through the IOC options:",
            choices=list(IOC_PATTERNS.keys()),
        ).execute()
        print(f"[{b}]")

        ans = b

    # ans = input(f"What pattern do you want to search for: \n {tabulate(table, headers=["#", "IOC"])} \n: ")   
    
    path = input("Point me to the file: ").strip()
    parser(ans, path)

##
start()