import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Load dataset
df = pd.read_csv('anomaly_results.csv', parse_dates=['Date'])

# Ensure 'Final_Anomaly' column exists
if 'Final_Anomaly' not in df.columns:
    raise ValueError("The 'Final_Anomaly' column is missing in the dataset.")

# Calculate MACD for trend analysis
short_window = 12
long_window = 26
signal_window = 9
df['EMA_12'] = df['Close'].ewm(span=short_window, adjust=False).mean()
df['EMA_26'] = df['Close'].ewm(span=long_window, adjust=False).mean()
df['MACD'] = df['EMA_12'] - df['EMA_26']
df['Signal_Line'] = df['MACD'].ewm(span=signal_window, adjust=False).mean()

# Calculate ATR for volatility analysis
atr_window = 14
high_low = df['High'] - df['Low']
high_close = abs(df['High'] - df['Close'].shift())
low_close = abs(df['Low'] - df['Close'].shift())
tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
df['ATR'] = tr.rolling(window=atr_window).mean()

# Calculate Standard Deviation for volatility
df['Std_Dev'] = df['Close'].rolling(window=20).std()

# Filter anomalies
anomalies = df[df['Final_Anomaly'] == 1]

# Define anomaly thresholds (adjust as needed)
upper_threshold = df['Close'].mean() + 2 * df['Close'].std()
lower_threshold = df['Close'].mean() - 2 * df['Close'].std()

# Categorize anomalies
mild_anomalies = anomalies[(anomalies['Close'] > lower_threshold) & (anomalies['Close'] < upper_threshold)]
extreme_anomalies = anomalies[(anomalies['Close'] <= lower_threshold) | (anomalies['Close'] >= upper_threshold)]

# Create figure
fig = go.Figure()

# Add stock price line with hover tooltip
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['Close'], 
    mode='lines', 
    name='Stock Price', 
    line=dict(color='blue'),
    hoverinfo="text",
    text=[f"Close: {c}<br>SMA: {sma}<br>EMA: {ema}<br>MACD: {macd}<br>ATR: {atr}<br>Std Dev: {std_dev}" 
          for c, sma, ema, macd, atr, std_dev in zip(df['Close'], df['SMA_20'], df['EMA_20'], df['MACD'], df['ATR'], df['Std_Dev'])]
))

# Add mild anomalies (Orange markers for better visibility)
fig.add_trace(go.Scatter(
    x=mild_anomalies['Date'], y=mild_anomalies['Close'], 
    mode='markers', 
    name='Mild Anomalies', 
    marker=dict(color='orange', size=9, symbol='circle'),
    text=[f"Close: {c}<br>Anomaly Type: Mild" for c in mild_anomalies['Close']],
    hoverinfo="text"
))

# Add extreme anomalies (Solid Red markers)
fig.add_trace(go.Scatter(
    x=extreme_anomalies['Date'], y=extreme_anomalies['Close'], 
    mode='markers', 
    name='Extreme Anomalies', 
    marker=dict(color='red', size=12, symbol='circle'),
    text=[f"Close: {c}<br>Anomaly Type: Extreme" for c in extreme_anomalies['Close']],
    hoverinfo="text"
))

# Add threshold lines (dotted for better contrast)
fig.add_trace(go.Scatter(
    x=df['Date'], y=[upper_threshold] * len(df),
    mode='lines', name='Upper Threshold',
    line=dict(color='green', dash='dot')
))

fig.add_trace(go.Scatter(
    x=df['Date'], y=[lower_threshold] * len(df),
    mode='lines', name='Lower Threshold',
    line=dict(color='purple', dash='dot')
))

# Improve layout
fig.update_layout(
    title='Stock Price with Enhanced Anomaly Detection',
    xaxis_title='Date',
    yaxis_title='Stock Price',
    template='plotly_white',
    xaxis=dict(
        showgrid=True, 
        tickangle=-45, 
        tickmode='auto', 
        nticks=15,
        rangeslider=dict(visible=True)  # Add range slider for zooming
    ),
    yaxis=dict(showgrid=True),
    hovermode='x unified',
    showlegend=True
)

# Ensure plot works in VS Code
pio.renderers.default = 'browser'

fig.show()
