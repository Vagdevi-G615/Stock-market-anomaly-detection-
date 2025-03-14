import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

def detect_anomalies(file_name="processed_stock_data.csv", save_csv=True):
    print(f"🔍 Loading processed data from {file_name}...")

    # Load processed stock data
    df = pd.read_csv(file_name, parse_dates=["Date"])

    # Ensure 'Close' is numeric
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    # **Method 1: Z-Score Method**
    df["Z_Score"] = (df["Close"] - df["Close"].mean()) / df["Close"].std()
    df["Z_Anomaly"] = np.where(np.abs(df["Z_Score"]) > 3, 1, 0)

    # **Method 2: Interquartile Range (IQR)**
    Q1 = df["Close"].quantile(0.25)
    Q3 = df["Close"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df["IQR_Anomaly"] = np.where((df["Close"] < lower_bound) | (df["Close"] > upper_bound), 1, 0)

    # **Method 3: Local Outlier Factor (LOF)**
    lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
    df["LOF_Anomaly"] = lof.fit_predict(df[["Close"]])
    df["LOF_Anomaly"] = df["LOF_Anomaly"].apply(lambda x: 1 if x == -1 else 0)

    # **Method 4: Isolation Forest**
    iso_forest = IsolationForest(contamination=0.05, random_state=42)
    df["Iso_Anomaly"] = iso_forest.fit_predict(df[["Close"]])
    df["Iso_Anomaly"] = df["Iso_Anomaly"].apply(lambda x: 1 if x == -1 else 0)

    # Count total anomalies detected
    total_anomalies = df[["Z_Anomaly", "IQR_Anomaly", "LOF_Anomaly", "Iso_Anomaly"]].sum(axis=1)
    df["Final_Anomaly"] = np.where(total_anomalies >= 2, 1, 0)  # Anomaly if flagged by 2+ methods

    print("✅ Anomaly detection completed!")

    # Save anomaly results
    if save_csv:
        df.to_csv("anomaly_results.csv", index=False)
        print("✅ Anomaly results saved as 'anomaly_results.csv'")

    return df

# Example usage
if __name__ == "__main__":
    df = detect_anomalies()
    print(df[df["Final_Anomaly"] == 1])  # Display detected anomalies
