# Stock-market-anomaly-detection
Stock market anomaly detection with Machine Learning

Anomalies in stock prices may signal significant market events, fraud, or opportunities.
The project employs several anomaly detection algorithms to discover malicious stock price movements.

### Project Features

✅ Retrieves real-time stock market data via Yahoo Finance API.

✅ Applies four anomaly detection methods(Z-Score, IQR, LOF, Isolation Forest).

✅ Offers interactive graphs with Plotly.

✅ Classifies mild & severe anomalies for improved insights.

### To install dependencies

pip install -r requirements.txt

### Run this project using the below command line

python stock_anomaly_detection.py

### How it works 

 *Data Collection*

- Fetches stock data from Yahoo Finance API

- Example: Fetching AAPL stock price from 2023-2024

*Data Preprocessing*

- Handles missing values

- Computes SMA, EMA

- Normalizes price movements

*Machine Learning Anomaly Detection*

- Z-Score Method – Detects outliers statistically

- IQR Method – Detects anomalies using quartiles

- LOF Method – Finds rare patterns in stock trends

- Isolation Forest – Detects unusual stock price movements

*Interactive Visualization with Plotly*

- Mild anomalies → Orange

- Extreme anomalies → Red

### 📢  Contributing

🔹 Feel free to fork the repo, submit pull requests, or suggest improvements!

