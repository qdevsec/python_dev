from collections import Counter

def plurality(findall):
    """
    calculate the item (eg, ip, hash, etc) that show up most often
    assign a score 
    """
    scores = {}
    counter = Counter()

    # print(findall)

    for i in findall:
        counter[i] += 1

    
    # print(f"{counter}")
    
    max_count = max(counter.values())

    for item, count in counter.items():
        scores[item] = count / max_count


    for i in scores:
        print(f"{i}: {scores[i]}")

def unique(data):
    unique_iocs = list(set(data.values()))
    print(unique_iocs)


