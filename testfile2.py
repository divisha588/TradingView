import yfinance as yf
import pandas as pd

def get_stock_price(ticker, start_date, end_date):
    """
    Fetch historical stock data and return the last closing price in the given date range.
    """
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        print(f"❌ No data found for {ticker} in {start_date} - {end_date}.")
        return None

    last_price = float(data['Close'].iloc[-1])  # Convert to float for safe formatting
    last_date = data.index[-1].date()
    print(f"✅ {ticker} price on {last_date} was {last_price:.2f}")
    return last_price

def get_latest_stock_price(ticker):
    """
    Fetch the latest available stock price.
    """
    data = yf.download(ticker, period="1d")

    if data.empty:
        print(f"❌ No recent data available for {ticker}.")
        return None

    latest_price = float(data['Close'].iloc[-1])  # Convert to float
    print(f"✅ Current {ticker} price is {latest_price:.2f}")
    return latest_price

def compare_stock_prices(ticker, reference_price, threshold=0.05):
    """
    Compare the latest price with the reference price within a given threshold.
    """
    latest_price = get_latest_stock_price(ticker)
    if latest_price is None or reference_price is None:
        return

    lower_bound = reference_price * (1 - threshold)
    upper_bound = reference_price * (1 + threshold)

    if lower_bound <= latest_price <= upper_bound:
        print(f"✅ {ticker} is trading within ±{threshold*100}% of its 2019 level.")
    else:
        print(f"❌ {ticker} is NOT trading within ±{threshold*100}% of its 2019 level.")

# 🎯 Define stock ticker and date range
ticker_symbol = "RELIANCE.NS"
start_2019 = "2019-01-01"
end_2019 = "2019-12-31"

# 🔄 Get stock prices
price_2019 = get_stock_price(ticker_symbol, start_2019, end_2019)

# 🔍 Compare with current price if 2019 price was found
if price_2019 is not None:
    compare_stock_prices(ticker_symbol, price_2019)
