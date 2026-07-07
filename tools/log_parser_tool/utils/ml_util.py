# find keyword importance, highlight most meaningful words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from pyod.models.iforest import IForest
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from pprint import pprint
import seaborn as sns
import pandas as pd
import mplcursors
import numpy as np



##########################
# multiple ioc functions #
##########################
def multiple_score_results(results_prepped):
    f = results_prepped["features"]

    score = min(
        int(
            f["total_hits"] * 0.05 +
            f["total_ioc_types"] * 10 +
            f["total_unique_matches"] * 0.1

        ),
        100
    )
    # print(round(score, 2))

    severity = (
        "Critical" if score >= 80 else
        "High" if score >= 60 else
        "Moderate" if score >= 40 else
        "Low" if score >= 20 else
        "Minimal"
    )

    ans = {
        "score": score,
        "severity": severity,
        "summary": f"{severity} IOC activity.",
        "reasons": [
            f'{f["total_hits"]} IOC matches',
            f'{f["total_unique_matches"]} unique indicators',
            f'{f["total_ioc_types"]} IOC types'
        ]
    }

    print("\n")
    print("#########################")
    pprint(ans)


def multi_ioc_features(results_prepped):
    """
    get generated ml features from:

        features["total_ioc_types"],
        features["total_hits"],
        features["total_unique_matches"],
        features["total_lines_flagged"],
        features["mean_hits_per_type"],
        features["max_hits_per_type"],
        features["std_hits_per_type"],
        features["mean_unique_per_type"],
        features["max_unique_per_type"],
        features["std_unique_per_type"],
        features["density"],
        features["uniqueness_ratio"]
    """
    features = results_prepped.get("features", {})
    ioc_stats = results_prepped.get("ioc_stats", {})

    total_hits = features.get("total_hits", 0)
    total_unique = features.get("total_unique_matches", 0)
    total_lines = features.get("total_lines_flagged", 0)

    hits_by_type = []
    unique_by_type = []

    for ioc_type, stats in ioc_stats.items():
        hits_by_type.append(stats.get("hits", 0))
        unique_by_type.append(stats.get("unique", 0))

    ml_features = {

        # Base counts
        "total_ioc_types": len(ioc_stats),
        "total_hits": total_hits,
        "total_unique_matches": total_unique,
        "total_lines_flagged": total_lines,

        # IOC distribution
        "mean_hits_per_type": np.mean(hits_by_type) if hits_by_type else 0,
        "max_hits_per_type": max(hits_by_type) if hits_by_type else 0,
        "std_hits_per_type": np.std(hits_by_type) if hits_by_type else 0,

        "mean_unique_per_type": np.mean(unique_by_type) if unique_by_type else 0,
        "max_unique_per_type": max(unique_by_type) if unique_by_type else 0,
        "std_unique_per_type": np.std(unique_by_type) if unique_by_type else 0,

        # Derived features
        "density": (
            total_hits / total_lines
            if total_lines > 0
            else 0
        ),

        "uniqueness_ratio": (
            total_unique / total_hits
            if total_hits > 0
            else 0
        )
    }

    print("\n")
    print("#########################")

    for key, value in ml_features.items():
        print(f"{key}: {value}")
        
    print("######################### \n")

def visualize_ioc_distribution(results):
    counts = {
        ioc_type: sum(
            len(entry.get("matches", []))
            for entry in entries
        )
        for ioc_type, entries in results.items()
    }

    plt.figure(figsize=(8,6))

    sns.barplot(
        x=list(counts.keys()),
        y=list(counts.values()),
        palette="mako"
    )

    plt.title("IOC Type Distribution")
    plt.xlabel("IOC Type")
    plt.ylabel("Hits")

    plt.tight_layout()
    plt.show()


########################
# single ioc functions #
########################
# takes features dictionaries (records) and return clean matrix
def prepare_feature_matrix(records, scalar=None, fit=True):
    df = pd.DataFrame(records).fillna(0)
    numeric_df = df.select_dtypes(include=["number"])

    if scalar is None:
        scaler = StandardScaler()

    if fit:
        X = scaler.fit_transform(numeric_df)
    else:
        X = scaler.transform(numeric_df)

    return X, scaler, numeric_df.columns


def calculate_risk_score(prepped_data):
    """
    improve insights from this function
    """

    # debug
    # print(f"prepped: \n {prepped_data}")

    f = prepped_data["features"]

    score = 0

    score += f["total_hits"] * 2
    score += f["total_unique_matches"] * 3
    score += f["total_ioc_types"] * 5

    # debug
    print(f"prepped: \n {score}")

    print(min(score, 100))

def predict_plot(logs):
    # preprocess and vectorize
    # collect collection of unformatted logs document to tf-idf features
    vectorize = TfidfVectorizer()

    if logs != "":

        print(logs)

        X = vectorize.fit_transform(logs)
    else:
        raise ValueError("Need log data, the select IOC was not found in logs")

    # train Isolation forest object
    # contamination: estimated % of anomalies in log data
    model = IsolationForest(contamination=0.1, n_estimators=200, random_state=42)
    model.fit(X)

    scores = model.decision_function(X)  # how weird each log line is (lower = more suspicious)
    # labels = model.predict
    # visualize
    # perplexity - the effective number of nearest neighbors t-SNE uses
    # low perplexity - each point cares about only a few neighbors
    # high perplexity - each point cares about many neighbors
    X_2d = TSNE(n_components=2, perplexity=1).fit_transform(X)

    sns.set_theme(style="darkgrid")

    plt.figure(figsize=(12, 6))


    # num_cols = df_lines.select_dtypes(include="number").columns.tolist()
    
    # # debug
    # # print(f"df_lines: {df_lines}")
    # # print(f"Num cols: {num_cols}")

    # x_col = ''
    # y_col = ''

    # if len(num_cols) >= 2:
    #     x_col = num_cols[0]
    #     y_col = num_cols[1]
    # else:
    #     raise ValueError("need at least 2 numeric field to create x y plot")

    # sns.scatterplot(
    #     data=df_lines,
    #     x=x_col,
    #     y=y_col
    # )

    # plt.xlabel("Bytes In")
    # plt.ylabel("Bytes Out")



    scatter = plt.scatter(X_2d[:,0], X_2d[:,1], c=scores, cmap='coolwarm')
    plt.colorbar(label="Anomaly Score")
    
    # # add mpl so you can hover over points and see more info
    cursor = mplcursors.cursor(scatter, hover=True)

    @cursor.connect("add")
    def on_add(sel):
        x, y = sel.target
        i = sel.index
        sel.annotation.set_text(
            f"Point: {i}\n"
            f"Value: ({x}, {y})\n"
            f"Score: {scores[i]}"
        )

    plt.title(f"Flow Prediction Analysis")    
    plt.tight_layout()
    plt.show()


def anomaly(logs):
    # preprocess and vectorize
    # collect collection of unformatted logs document to tf-idf features
    vectorize = TfidfVectorizer()
    X = vectorize.fit_transform(logs)

    # train Isolation forest object
    # contamination: estimated % of anomalies in log data
    model = IsolationForest(contamination=0.1, n_estimators=200, random_state=42)
    model.fit(X)
    # seem to only find the rare value
    # make prediction, -1 is an anomaly, 1 is normal
    predictions = model.predict(X)

    scores = model.decision_function(X)  # how weird each log line is (lower = more suspicious)
    # labels = model.predict
    # visualize
    # perplexity - the effective number of nearest neighbors t-SNE uses
    # low perplexity - each point cares about only a few neighbors
    # high perplexity - each point cares about many neighbors
    X_2d = TSNE(n_components=2, perplexity=1).fit_transform(X)

    # rank the most suspicious log lines
    anomaly_indices = np.argsort(scores)[:20]  # top 20 weirdest logs

    for idx in anomaly_indices:
        print(scores[idx], logs[idx])

    for log, prediction in zip(logs, predictions):
        if prediction == -1:
            print(f" Anomaly sighting: {log}")

def tfid_vectorizer(lines):
    """
    TfidVectorizer converts text documents into matrix of TF-IDF features
    calculates token frequencies, computes inverse document frequency (IDF) to weight
    important terms and returns sparse matrix, widely used for text classification 

    Features:
    - Numerical transformation - converts text into numbers (w decimals) to indicate feature importance
    - Term Importance Weighting - it boosts rare unique terms and lowers the weight of common less relevant terms
    - Built in Normalization - applies L2 normalization to output rows so their sum of squares is 1
    - All-in-one process - directly computes both word counts (TF- term frequency) and inverse document frequency (IDF) 
    in one step
    """
    print("Vectorizing....TfidVectorizer from the sklearn library turns text docs to matrix of TF-IDF features..\n\n")

    # print(f"log lines:\n {lines}\n\n")

    # create object, use fit
    vectorizer = TfidfVectorizer()

    # convert log lines into TF-IDF matrix
    tfid_matrix = vectorizer.fit_transform(lines)

    # output features
    print(f"Here are the features:\n {vectorizer.get_feature_names_out()}\n")

    # see matrix shape
    print(f"shape: {tfid_matrix.shape} \n")

    # converted text to numerical features, placed in array, 
    print(f"...converting to numerical features and storing in array \n {tfid_matrix.toarray()}")

    


# predict(logs, log_lines)