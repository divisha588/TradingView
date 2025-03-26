import yfinance as yf
import pandas as pd

def get_stock_prices(ticker, start_date, end_date):
    """
    Fetch historical stock data for the given date range.
    Returns a DataFrame with Open, High, Low, and Close prices.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        print(f"❌ No data found for {ticker} in {start_date} - {end_date}.")
        return None
    return data[['Open', 'High', 'Low', 'Close']]

def compare_stock_prices(ticker, historical_data, reference_price, threshold=0.05):
    """
    Compare daily closing prices with a reference price.
    """
    lower_bound = reference_price * (1 - threshold)
    upper_bound = reference_price * (1 + threshold)

    # Create a new column to check if price is within range
    historical_data['Within ±5%?'] = historical_data['Close'].apply(
        lambda price: "✅ Yes" if lower_bound <= price <= upper_bound else "❌ No"
    )

    # Format the table
    print("\n📊 Daily Stock Price Comparison:\n")
    print(historical_data[['Close', 'Within ±5%?']].to_markdown())

# 🎯 Define stock ticker and date range
ticker_symbol = "RELIANCE.NS"

# 🔄 Get 2019's last price automatically
price_2019_data = get_stock_prices(ticker_symbol, "2019-12-31", "2019-12-31")
if price_2019_data is not None:
    reference_price = price_2019_data['Close'].iloc[0]
    print(f"\n🎯 Reference Price (2019 Last Close): {reference_price:.2f}")

    # 🔄 Get latest stock prices for comparison
    latest_data = get_stock_prices(ticker_symbol, "2024-02-01", "2024-02-29")

    if latest_data is not None:
        compare_stock_prices(ticker_symbol, latest_data, reference_price)





# import yfinance as yf
# import pandas as pd
# from tabulate import tabulate  # For displaying table output

# def get_stock_price(ticker, start_date, end_date):
#     """
#     Fetch historical stock data and return the last closing price in the given date range.
#     """
#     data = yf.download(ticker, start=start_date, end=end_date)

#     if data.empty:
#         print(f"❌ No data found for {ticker} in {start_date} - {end_date}.")
#         return None, None

#     last_price = float(data['Close'].iloc[-1])  # Convert to float for safe formatting
#     last_date = data.index[-1].date()
#     print(f"✅ {ticker} price on {last_date} was {last_price:.2f}")
#     return last_price, last_date

# def get_latest_stock_price(ticker):
#     """
#     Fetch the latest available stock price.
#     """
#     data = yf.download(ticker, period="1d")

#     if data.empty:
#         print(f"❌ No recent data available for {ticker}.")
#         return None, None

#     latest_price = float(data['Close'].iloc[-1])  # Convert to float
#     latest_date = data.index[-1].date()
#     print(f"✅ Current {ticker} price on {latest_date} is {latest_price:.2f}")
#     return latest_price, latest_date

# def compare_stock_prices(ticker, reference_price, reference_date, threshold=0.05):
#     """
#     Compare the latest price with the reference price within a given threshold and display results in a table.
#     """
#     latest_price, latest_date = get_latest_stock_price(ticker)
#     if latest_price is None or reference_price is None:
#         return

#     lower_bound = reference_price * (1 - threshold)
#     upper_bound = reference_price * (1 + threshold)

#     is_within_threshold = "✅ Yes" if lower_bound <= latest_price <= upper_bound else "❌ No"

#     # Create table data
#     table_data = [
#         ["Stock", "Reference Date", "Reference Price", "Latest Date", "Latest Price", "Within ±5%?"],
#         [ticker, reference_date, f"{reference_price:.2f}", latest_date, f"{latest_price:.2f}", is_within_threshold]
#     ]

#     print("\n📊 Stock Price Comparison:\n")
#     print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

# # 🎯 Define stock ticker and date range
# ticker_symbol = "RELIANCE.NS"
# start_2019 = "2019-01-01"
# end_2019 = "2019-12-31"

# # 🔄 Get stock prices
# price_2019, date_2019 = get_stock_price(ticker_symbol, start_2019, end_2019)

# # 🔍 Compare with current price if 2019 price was found
# if price_2019 is not None:
#     compare_stock_prices(ticker_symbol, price_2019, date_2019)
