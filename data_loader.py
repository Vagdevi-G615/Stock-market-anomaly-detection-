import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker="AAPL", start="2023-01-01", end="2024-01-01", save_csv=True):
    """
    Fetch stock data from Yahoo Finance.
    
    Parameters:
    - ticker (str): Stock symbol (e.g., "AAPL")
    - start (str): Start date in YYYY-MM-DD format
    - end (str): End date in YYYY-MM-DD format
    - save_csv (bool): Whether to save the data as CSV

    Returns:
    - pd.DataFrame: Stock data
    """

    print(f"📈 Fetching data for {ticker} from {start} to {end}...")
    
    # Fetch stock data
    stock = yf.download(ticker, start=start, end=end)

    if stock.empty:
        print(f"⚠️ No data found for {ticker}. Check the stock symbol or date range.")
        return None

    # Reset index and rename columns for consistency
    stock.reset_index(inplace=True)
    stock.rename(columns={"Adj Close": "Close"}, inplace=True)

    # Save to CSV
    if save_csv:
        filename = f"{ticker}_stock_data.csv"
        stock.to_csv(filename, index=False)
        print(f"✅ Data saved as {filename}")

    return stock

# Example usage
if __name__ == "__main__":
    df = fetch_stock_data("AAPL", "2023-01-01", "2024-01-01")
    print(df.head())