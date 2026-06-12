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

def top(data, n):
    """
    takes dict {line #: ioc_value} and n (int): # of top values to return 
    returns the n most common IOC value

    prints list[tuple]: [(ioc, count), ...]
    """
    counts = Counter(data.values())

    most_common = counts.most_common(n)
    
    for i in most_common:
        print(i)

def get_frequencies(data):
    
    iocs = Counter(data.values())
    ans = input("Would you like results printed vertically or wrapped? [vert, wrap]: ")
    
    if ans == 'vert':
    
        for i in iocs:
            print(f"{i}: {iocs[i]}")

    if ans == 'wrap':
        print(iocs)