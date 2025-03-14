# Stock-market-anomaly-detection
Stock market anomaly detection with Machine Learning

Anomalies in stock prices may signal significant market events, fraud, or opportunities.
The project employs several anomaly detection algorithms to discover malicious stock price movements.

### Project Features
✅ Retrieves real-time stock market data via Yahoo Finance API.

✅ Applies four anomaly detection methods (Z-Score, IQR, LOF, Isolation Forest).

✅ Offers interactive graphs with Plotly.

✅ Classifies mild & severe anomalies for improved insights.

### To Install Dependencies

pip install -r requirements.txt

### Run This Project Using the Below Command Line

python stock_anomaly_detection.py

### How It Works

*Data Collection*

- Fetches stock data from Yahoo Finance API.
  
Example: Fetching AAPL stock price from 2023-2024.


*Data Preprocessing*

- Handles missing values.

- Computes SMA (Simple Moving Average) and EMA (Exponential Moving Average).

- Normalizes price movements.
  
  
*Machine Learning Anomaly Detection*
  
- Z-Score Method – Detects outliers statistically.
  
- IQR Method – Detects anomalies using quartiles.
  
- LOF Method – Finds rare patterns in stock trends.
  
- Isolation Forest – Detects unusual stock price movements.
  
  
*Interactive Visualization with Plotly*
  
- Mild anomalies → 🟠 Orange
  
- Extreme anomalies → 🔴 Red
  
### Understanding the Output Data in Hover Details

- Close – The stock’s closing price for the given date.
  
- SMA (Simple Moving Average) – The average stock price over a selected period.
  
- EMA (Exponential Moving Average) – A weighted moving average giving more importance to recent prices.
  
- ACD (Moving Average Convergence Divergence) – A momentum indicator showing trend strength.
  
- ATR (Average True Range) – A volatility measure showing how much the price moves on average.
  
- Std Dev (Standard Deviation) – Measures price fluctuation intensity.
  
-  Anomaly Type – Indicates whether an anomaly is mild (orange) or extreme (red).
   
- Upper Threshold – The upper bound above which prices are considered extreme.
  
- Lower Threshold – The lower bound below which prices are considered extreme.

### Lower Graph in the Output

Provides a focused view of anomalies detected over time.

✅ Zoomed-in trend of stock prices with anomalies.

✅ Clearer view of volatility and price deviations.

✅ Helps detect clusters of anomalies (if multiple unusual movements occur in a short period).

This lower graph helps in understanding:

- Frequent anomalies in a specific period → Could indicate market instability.
  
- Extreme anomalies appearing before major price shifts → May signal market reversals.
  
- Helps traders react quickly to market changes.
  
- With this dual visualization, investors can analyze both long-term trends and short-term market fluctuations!

### 📢 Contributing

🔹 Feel free to fork the repo, submit pull requests, or suggest improvements!

### Output

![Screenshot 2025-03-14 225309](https://github.com/user-attachments/assets/40aa45b1-d074-41d7-9755-a5a24ede9283)

![Screenshot 2025-03-14 225321](https://github.com/user-attachments/assets/d1149c64-3004-4cfd-ace4-35bbe57e41a7)
