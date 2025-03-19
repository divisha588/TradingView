import yfinance as yf
import pandas as pd

# Define your ticker and date range for 2019
ticker = "RELIANCE.NS"  # Replace with any NSE ticker
start_date = "2019-01-01"
end_date = "2019-12-31"

# Download historical data for 2019
data_2019 = yf.download(ticker, start=start_date, end=end_date)

# Get the closing price on the last trading day in 2019
price_2019 = data_2019['Close'].iloc[-1]
print(f"{ticker} price on {data_2019.index[-1].date()} was {price_2019:.2f}")

# Fetch the current price (here assuming the latest available closing price)
current_data = yf.download(ticker, period="1d")
current_price = current_data['Close'].iloc[-1]
print(f"Current {ticker} price is {current_price:.2f}")

# Define a threshold, for example 5%.
threshold = 0.05  # 5%

# Check if current price is within the threshold of the 2019 price
lower_bound = price_2019 * (1 - threshold)
upper_bound = price_2019 * (1 + threshold)

if lower_bound <= current_price <= upper_bound:
    print(f"{ticker} is trading within 5% of its 2019 level.")
else:
    print(f"{ticker} is not trading within 5% of its 2019 level.")
