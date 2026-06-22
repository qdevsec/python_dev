import math
from collections import Counter
# deprecated, used in line 152 when IOCs were presented in  
# table = [(i,k) for i, k in enumerate(sorted(IOC_PATTERNS.keys()), 1)]

# Generic feature extraction for multi-ioc records
def multi_extract_features(results):
    """
    turns results into a normalized feature for ML

    returns: feature dictionary
    """

    features = {
        "total_ioc_types": 0,
        "total_hits": 0,
        "total_unique_matches": 0,
        "total_lines_flagged": 0,
    }

    flagged_lines = set()
    unique_matches = set()

    ioc_stats = {}

    for ioc_type, entries in results.items():

        hit_count = len(entries)
        
        unique_for_type = set()

        for entry in entries:

            flagged_lines.add(entry["line"])

            for match in entry["matches"]:
                unique_matches.add(str(match))
                unique_for_type.add(str(match))

        ioc_stats[ioc_type] = {
            "hits": hit_count,
            "unique": len(unique_for_type)
        }

        features[f"{ioc_type}_hits"] = hit_count
        features[f"{ioc_type}_unique"] = len(unique_for_type)

        if hit_count > 0:
            features["total_ioc_types"] += 1

        features["total_hits"] += hit_count

    features["total_unique_matches"] = len(unique_matches)
    features["total_lines_flagged"] = len(flagged_lines)

    return {"features": features, "ioc_stats": ioc_stats}

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
