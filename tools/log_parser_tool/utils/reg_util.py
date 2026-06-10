from collections import Counter

def plurality(findall):
    """
    calculate the item (eg, ip, hash, etc) that show up most often
    assign a score 
    """
    scores = {}
    counter = Counter()

    for i in findall:
        counter[i] += 1
    
    total = sum(counter.values())

    # print(findall)

    # print(f"{counter}")
    
    # max_count = max(counter.values())

    # for item, count in counter.items():
    #     scores[item] = count / max_count

    scores = {
        item: count / total
        for item, count in counter.items()
    }

    ans = input("Would you like to output be [file, console, both]: ")

    if ans == "file":

        with open("log_parser_output.csv", "w") as f:

            for i in scores:
                f.write(f"{i}: {scores[i]}\n")

    elif ans == "console":
        for i in scores:
            print(f"{i}: {scores[i]}")
    
    elif ans == "both":

        with open("log_parser_output.csv", "w") as f:

            for i in scores:
                f.write(f"{i}: {scores[i]}\n")

        for i in scores:
            print(f"{i}: {scores[i]}")

def unique(data):
    unique_iocs = list(set(data.values()))
    print(unique_iocs)


