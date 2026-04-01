from sklearn.ensemble import IsolationForest
import numpy as np

# 1. Feature Engineering: Model needs numbers, not text
# Let's say we have: [failed_logins, bytes_sent, unique_files_accessed]
data = np.array([
    [1, 100, 5],   # Normal
    [0, 150, 2],   # Normal
    [2, 120, 8],   # Normal
    [50, 9000, 400] # HUGE ANOMALY (High failures, high data, high files)
])

# 2. Initialize the Model
# 'contamination' is your guess of what % of the logs are malicious (e.g., 1%)
model = IsolationForest(contamination=0.1, random_state=42)

# 3. Fit and Predict
# 1 = Normal, -1 = Anomaly
predictions = model.fit_predict(data)

for i, pred in enumerate(predictions):
    if pred == -1:
        status = "ANOMALY"
    else:
        status = "Normal"
    print(f"Log Entry {i}: {status}")