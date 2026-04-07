# find keyword importance, highlight most meaningful words

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

logs = ["INFO: User login", "INFO: User login", "ERROR: Disk full", "ERROR: Disk full", "ERROR: Disk full", "INFO: User login", "INFO: login from different location"]
lines = ["The quick brown fox","The agile cat", "The lazy dog", "The fox and the cat", "The dog and the fox"]
log_lines = [
    "Failed password for invalid user root from 10.0.0.5",
    "GET /index.html 200",
    "Accepted password for admin from 192.168.1.10",
]

def predict(logs, log_lines):
    # preprocess and vectorize
    # collect collection of unformatted logs document to tf-idf features
    vectorize = TfidfVectorizer()
    X = vectorize.fit_transform(log_lines)

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

    plt.scatter(X_2d[:,0], X_2d[:,1], c=scores, cmap='coolwarm')
    plt.colorbar(label="Anomaly Score")
    plt.show()



    # seem to only find the rare value
    # make prediction, -1 is an anomaly, 1 is normal
    predictions = model.predict(X)

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

    # create object, use fit
    vectorizer = TfidfVectorizer()
    tfid_matrix = vectorizer.fit_transform(lines)

    # output features
    print(vectorizer.get_feature_names_out())

    # converted text to numerical features, placed in array, 
    print(tfid_matrix.toarray())


predict(logs, log_lines)