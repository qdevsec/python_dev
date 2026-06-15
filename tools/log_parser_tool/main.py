import re
import math
from collections import Counter
from pathlib import Path
from tabulate import tabulate
from utils.re_patterns import IOC_PATTERNS
from utils.ml_util import *
from utils.reg_util import *
from InquirerPy import inquirer

data = {}
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
def extract_features(line, compiled_patterns):
    features = {}
    length = max(len(line), 1)


    # IOC patterns
    for name, pattern in compiled_patterns.items():
        count = sum(1 for _ in pattern.finditer(line))

        features[f"{name}_count"] = count
        features[f"{name}_density"] = count / length

    # stats
    features["line_length"] = length
    # lightweight statistical signal about the structure and content of the log line
    features["digit_ratio"] = sum(c.isdigit() for c in line) / length
    features["uppercase_ratio"] = sum(c.isupper() for c in line) / length
    features["specialchar_ratio"] = sum(not c.isalnum() for c in line) / length

    # tokens
    tokens = line.split()
    features["token_count"] = len(tokens)
    features["avg_token_length"] = sum(len(t) for t in tokens) / max(len(tokens), 1)

    # entropy
    ent = shannon_entropy(line)
    features["entropy"] = ent
    features["high_entropy_flag"] = int(ent > 4.5)

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
            print("....analyzing file")
            print("\n")

            # matches = re.findall(IOC_PATTERNS[ans], file)
            
            # iterates directly over the file object (lazy loading)
            for line_number, line in enumerate(file, 1):
                
                find = ''

                match = log_pattern.search(line)

                if match:
                    if ans == "port":
                        a = match.group(0)
                        find = a.strip(":")  
                    else:
                        find = match.group(0)

                # extend instead of append because extend() unpacks the list (findall() produces a list) and appends value
                findall_results.append(find)

                # create data structure with the line number and specific ioc
                # data.append(f"Line {line_number}: {findall}")
                data[line_number] = find

                # data.append(f"Line {line_number}: {line}")
                lines.append(line)

                items_all.append(find)
                
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

    compiled_patterns = {
        name: re.compile(pattern)
        for name, pattern in IOC_PATTERNS.items()
    }

    records = [
        extract_features(line, compiled_patterns)
        for line in lines
    ]

    X, scaler, feature_names = prepare_feature_matrix(records)

    category = input("Would category of functions would you like to use [normal, machine-learning]: ").lower()

    if category == 'machine-learning':

        # prompt user about ML capability
        ml_use = input(f"What ml utilities would you like to use? [anomaly, predict, vectorize]: ").lower()
            # Use ML
        if ml_use == "anomaly":
            # print(lines)
            # print(f"all items: \n{items_all}\n")

            anomaly(lines)
        if ml_use == "predict":
            # print(f"all items: \n{items_all}\n")

            # print(records)
            # df_lines = pd.DataFrame(records)
            # print(df_lines.head())
            # print(df_lines.describe())
            
            # passing in from prepare_feature_matrix() from ml_util tooling  
            predict_plot(lines, X)
        
        if ml_use == "vectorize":
            # print(f"all items: \n{items_all}\n")
            tfid_vectorizer(lines)

        
        

    if category == 'normal':
        # prompt user about normal function 
        norm_use = input(f"What normal utilities would you like to use? [plurality, unique, top, frequency]: ").lower()

        if norm_use == "plurality":
            # print(f"main: {findall_results}")
            plurality(findall_results)

        if norm_use == "unique":
            unique(data)

        if norm_use == "top":
            n = int(input("number of top values to return: "))
            top(data, n)

        if norm_use == "frequency":
            get_frequencies(data)

def start():
    
    ans = ""

    print("👋 Hi, this tools lets you perform analysis on log files, here are the tool features: \n"
          "  - allows you to provide path to log file \n" 
          "  - allows you to search for IOCs (eg ipv4, md5, etc) or be presented the total list of IOCs \n"  
          "  - presents ml functions and other functions to get analysis on the log files \n ")

    # enable user to filter if they dont know the ioc exactly, or present neat table of iocs
    choice = input("Do you prefer to provide an ioc (partial or whole) or to be present with a table? [provide, present]: ").lower()

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
            message="here are the IOCs, use the up or down arrow keys to peruse through the IOC options. Can also start typing out a word for filtering:",
            choices=list(IOC_PATTERNS.keys()),
        ).execute()
        print(f"[{b}]")

        ans = b

    # ans = input(f"What pattern do you want to search for: \n {tabulate(table, headers=["#", "IOC"])} \n: ")   
    
    path = input("Point me to the file: ").strip()
    parser(ans, path)

##
start()