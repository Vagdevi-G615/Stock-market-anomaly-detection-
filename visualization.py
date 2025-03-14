import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_anomalies(stock_file="processed_stock_data.csv", anomaly_file="anomaly_results.csv", window=10):
    print(f"📊 Loading stock data from {stock_file}...")
    print(f"🔍 Loading anomaly data from {anomaly_file}...")

    # Load datasets
    stock_data = pd.read_csv(stock_file)
    anomaly_data = pd.read_csv(anomaly_file)

    # Ensure correct date format (DD-MM-YYYY)
    stock_data["Date"] = pd.to_datetime(stock_data["Date"], format="%d-%m-%Y", dayfirst=True)
    anomaly_data["Date"] = pd.to_datetime(anomaly_data["Date"], format="%d-%m-%Y", dayfirst=True)

    # Sort data by Date and remove duplicates
    stock_data = stock_data.sort_values("Date").drop_duplicates(subset=["Date"])
    anomaly_data = anomaly_data.sort_values("Date").drop_duplicates(subset=["Date"])

    # Merge datasets
    merged_df = stock_data.merge(anomaly_data[["Date", "Final_Anomaly"]], on="Date", how="left")
    merged_df["Final_Anomaly"].fillna(0, inplace=True)

    # Apply Rolling Window for Smoothing
    merged_df["Smoothed_Close"] = merged_df["Close"].rolling(window=window, min_periods=1).mean()

    # Create figure
    plt.figure(figsize=(14, 6))
    
    # Plot Smoothed Stock Prices
    plt.plot(merged_df["Date"], merged_df["Smoothed_Close"], label="Smoothed Stock Price", color="blue", linewidth=2, alpha=0.8)

    # Highlight anomalies
    anomalies = merged_df[merged_df["Final_Anomaly"] == 1]
    plt.scatter(anomalies["Date"], anomalies["Close"], color="red", label="Anomalies", marker="o", s=60)

    # Format date labels properly
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Show every 3rd month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    # Titles and labels
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Stock Price", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid()
    plt.title("Stock Price with Anomalies", fontsize=14)

    # Save & show
    plt.savefig("anomaly_plot.png", dpi=300, bbox_inches="tight")
    print("✅ Anomaly plot saved as 'anomaly_plot.png'")
    plt.show()

# Run visualization
if __name__ == "__main__":
    plot_anomalies()
