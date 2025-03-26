import yfinance as yf
import pandas as pd
from tabulate import tabulate

def get_last_available_price(ticker, reference_date):
    """
    Get the last available closing price before or on the given reference date.
    """
    data = yf.download(ticker, end=reference_date, progress=False)

    if data.empty:
        print(f"❌ No data found for {ticker} up to {reference_date}.")
        return None

    last_price = data['Close'].iloc[-1]
    last_date = data.index[-1].date()
    print(f"✅ Using last available price on {last_date}: {last_price:.2f}")
    return float(last_price)  # Ensure it's a float

def compare_prices_and_display_table(ticker, reference_price, threshold=0.05):
    """
    Compare daily stock prices with the reference price and display results in a table.
    """
    data = yf.download(ticker, period="1mo", progress=False)  # Fetch last month’s data
    if data.empty:
        print(f"❌ No recent data found for {ticker}.")
        return

    data = data[['Close']].copy()
    data['Lower Bound'] = reference_price * (1 - threshold)
    data['Upper Bound'] = reference_price * (1 + threshold)
    data['Within ±5%?'] = data['Close'].between(data['Lower Bound'], data['Upper Bound'])
    
    # Convert to ✅/❌ symbols
    data['Within ±5%?'] = data['Within ±5%?'].map({True: "✅ Yes", False: "❌ No"})

    # Print reference price and bounds
    print(f"\n📌 Reference Price (2019 or closest available): {reference_price:.2f}")
    print(f"📉 Lower Bound: {data['Lower Bound'].iloc[0]:.2f}, 📈 Upper Bound: {data['Upper Bound'].iloc[0]:.2f}")

    # Format table output
    table = tabulate(data[['Close', 'Within ±5%?']], headers=["Date", "Closing Price", "Within ±5%?"], tablefmt="fancy_grid")
    print("\n📊 Daily Stock Price Comparison:\n")
    print(table)

# 🎯 Define stock ticker and reference date
ticker_symbol = "RELIANCE.NS"
reference_date = "2019-12-31"

# 🔄 Get last available stock price before reference date
reference_price = get_last_available_price(ticker_symbol, reference_date)

# 🔍 Compare with recent prices if reference price was found
if reference_price is not None:
    compare_prices_and_display_table(ticker_symbol, reference_price)









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
