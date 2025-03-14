import pandas as pd
import ta

def preprocess_data(file_name="AAPL_stock_data.csv", save_csv=True):
    print(f"📊 Loading data from {file_name}...")

    # Load stock data
    df = pd.read_csv(file_name, parse_dates=["Date"])

    # Convert 'Close' column to numeric
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    # Handle missing values before indicators
    df.fillna(method="ffill", inplace=True)
    df.fillna(method="bfill", inplace=True)

    # Ensure chronological order
    df.sort_values(by="Date", inplace=True)

    # Add technical indicators
    df["SMA_20"] = ta.trend.sma_indicator(df["Close"], window=20)
    df["EMA_20"] = ta.trend.ema_indicator(df["Close"], window=20)
    df["ATR"] = ta.volatility.average_true_range(df["High"], df["Low"], df["Close"], window=14)
    df["BB_Upper"], df["BB_Middle"], df["BB_Lower"] = (
        ta.volatility.bollinger_hband(df["Close"], window=20),
        ta.volatility.bollinger_mavg(df["Close"], window=20),
        ta.volatility.bollinger_lband(df["Close"], window=20)
    )

    # **Drop initial rows where indicators are NaN**
    df.dropna(inplace=True)

    print("✅ Technical indicators added!")

    # Save processed data
    if save_csv:
        processed_file = "processed_stock_data.csv"
        df.to_csv(processed_file, index=False)
        print(f"✅ Processed data saved as {processed_file}")

    return df

# Example usage
if __name__ == "__main__":
    df = preprocess_data()
    print(df.head())
