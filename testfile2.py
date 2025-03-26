import yfinance as yf
import pandas as pd
from tabulate import tabulate  # For pretty table formatting

def get_last_available_price(ticker, reference_date):
    """
    Fetch historical stock data and return the last available closing price before or on reference_date.
    """
    data = yf.download(ticker, start="2019-12-01", end=reference_date)

    if data.empty:
        print(f"❌ No data found for {ticker} in December 2019.")
        return None

    last_price = data['Close'].dropna().iloc[-1]  # Get last valid closing price
    last_date = data.index[-1].date()
    print(f"✅ Using last available price on {last_date}: {float(last_price):.2f}")
    return float(last_price)  # Convert to float

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data for a specific date range.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    
    if data.empty:
        print(f"❌ No stock data found for {ticker} in {start_date} - {end_date}.")
        return None
    
    return data[['Close']]  # Only keep closing prices

def compare_prices_and_display_table(ticker, data, reference_price, threshold=0.05):
    """
    Compare stock prices with the reference price and display results in a table.
    """
    if data is None or reference_price is None:
        print("⚠️ No valid data to compare.")
        return

    lower_bound = reference_price * (1 - threshold)
    upper_bound = reference_price * (1 + threshold)

    # Prepare data for table
    table_data = []
    for date, row in data.iterrows():
        price = row['Close'].item()  # ✅ Convert to float correctly
        within_range = "✅ Yes" if lower_bound <= price <= upper_bound else "❌ No"
        table_data.append([date.date(), round(price, 2), within_range])

    # Print table
    print("\n📊 Daily Stock Price Comparison:")
    print(tabulate(table_data, headers=["Date", "Closing Price", f"Within ±{threshold*100}%?"], tablefmt="fancy_grid"))

# 🎯 Define stock ticker and date range
ticker_symbol = "RELIANCE.NS"
reference_date = "2019-12-31"
comparison_start = "2024-02-01"
comparison_end = "2024-02-28"

# 🔄 Get reference price
reference_price = get_last_available_price(ticker_symbol, reference_date)

# 📉 Fetch current stock prices for the given date range
stock_data = fetch_stock_data(ticker_symbol, comparison_start, comparison_end)

# 🔍 Compare and display results
compare_prices_and_display_table(ticker_symbol, stock_data, reference_price)








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
