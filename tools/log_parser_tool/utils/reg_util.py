from collections import Counter
from pprint import pprint

####################
# Helper functions #
####################
def _severity(score):

    if score >= 80:
        return "critical"
    
    if score >= 60:
        return "high"
    
    if score >= 30:
        return "medium"
    
    return "low"


########################
# single ioc functions #
########################
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


##########################
# multiple ioc functions #
##########################
def summarize_results_norm(data):
    """
    summarize IOC extraction results
    """
    summary = {
        "total_ioc_types": len(data),
        "total_hits": 0,
        "total_unique_matches": 0,
        "total_lines_flagged": 0,
        "ioc_stats": {}
    }

    flagged_lines = set()
    unique_matches = set()

    for ioc_type, entries in data.items():

        hits = 0
        unique = set()
        lines = set()

        for entry in entries:

            matches = entry.get("matches", [])
            line = entry.get("line")

            hits += len(matches)

            unique.update(matches)

            if line is not None:
                lines.add(line)
                flagged_lines.add(line)

        summary["ioc_stats"][ioc_type] = {
            "hits": hits,
            "unique": len(unique),
            "lines": len(lines)
        }

        summary["total_hits"] += hits
        unique_matches.update(unique)

    summary["total_unique_matches"] = len(unique_matches)
    summary["total_lines_flagged"] = len(flagged_lines)

    pprint(summary)


def summarize_results(data):
    """
    can be used with results or results_prepped
    """

    print("....Generating summary....\n")
    summary = {
        "ioc_types": {},
        "totals": {
            "hits": 0,
            "unique": 0,
            "lines_flagged": 0,
            "ioc_types": 0
        }
    }

    if "features" in data and "ioc_stats" in data:

        for ioc, stats in data["ioc_stats"].items():
            summary["ioc_types"][ioc] = {
                "hits": stats["hits"],
                "unique": stats["unique"]
            }

        summary["totals"]["hits"] = data["features"]["total_hits"]
        summary["totals"]["unique"] = data["features"]["total_unique_matches"]
        summary["totals"]["lines_flagged"] = data["features"]["total_lines_flagged"]
        summary["totals"]["ioc_types"] = data["features"]["total_ioc_types"]

        # return summary      

    pprint(summary)


def calculate_ioc_percentages(results_prepped):
    total_hits = results_prepped["features"].get("total_hits", 0)

    percentages = {}

    if total_hits == 0:
        return percentages
    
    for ioc_type, stats in results_prepped["ioc_stats"].items():
        hits = stats.get("hits", 0)

        percentages[ioc_type] = {
            "hits": hits,
            "unique": stats.get("unique", 0),
            "percent_of_hits": f'{round((hits / total_hits) * 100, 2)}%'
        }

    print("\n")
    print("#########################")

    for key, value in percentages.items():
        print(f"{key}: {value}")
        
    print("######################### \n")   

def analyze_features(results):
    
    findings = []
    score = 0

    features = results["features"]

    total_hits = features["total_hits"]
    total_unique = features["total_unique_matches"]
    total_lines = features["total_lines_flagged"]

    diversity = (
        total_unique / total_hits
        if total_hits
        else 0
    )

    density = (
        total_hits / total_lines
        if total_lines
        else 0
    )

    if total_hits > 500:
        findings.append(
            f"High IOC volume detected ({total_hits:,} matches)"
        )
        score += 30

    if diversity > 0.4:
        findings.append(
            f"High IOC variety ({diversity:,} unique)"
        )
        score += 20
        
    if density > 1.25:
        findings.append(
            f"High IOC variety ({density:.2f} matches per flagged line)"
        )
        score += 30
        
    for key, value in results.items():
        if key.endswith("_hits") and not key.startswith("total"):
            ratio = value / total_hits

            if ratio > 0.75:
                findings.append(
                    f"{key.replace('_hits','')} indicators dominate "
                    f"({ratio:.1%} of detections)"
                )

    score += min(results["features"]["total_ioc_types"] * 5, 20)

    ans = {
        "severity": _severity(score),
        "score": score,
        "findings": findings,
        "metrics": {
            "variety": round(diversity, 3),
            "density": round(density, 3)
        }

    }
    print("\n")
    print("#########################")

    for key, value in ans.items():
        print(f"{key}: {value}")
        
    print("######################### \n")