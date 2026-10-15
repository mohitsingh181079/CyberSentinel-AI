import pandas as pd
from sklearn.ensemble import IsolationForest

def train_model(df):
    # Select features for anomaly detection
    X = df[['login_attempts', 'data_mb']]
    # Isolation Forest model
    model = IsolationForest(contamination=0.3, random_state=42)
    model.fit(X)
    return model