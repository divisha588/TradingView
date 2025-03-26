import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_last_available_price(ticker_symbol, reference_date):
    """
    Fetch the last available closing price for the given ticker before the reference date.
    """
    try:
        # Download historical data
        data = yf.download(ticker_symbol, start=reference_date - timedelta(days=10), end=reference_date)

        # Debugging: Print the retrieved table properly formatted
        if data is None or data.empty:
            print(f"❌ No data found for {ticker_symbol} before {reference_date}")
            return None, None

        # Print formatted table
        print("\n📊 Downloaded Data:\n")
        print(data[['Open', 'High', 'Low', 'Close', 'Volume']].tail().to_string())

        # Get the last available closing price
        last_date = data.index[-1].date()
        last_price = data['Close'].iloc[-1]

        if pd.isna(last_price).any():
            print(f"❌ No valid closing price found for {ticker_symbol} on {last_date}")
            return None, None

        print(f"\n✅ Using last available price on {last_date}: {last_price:.2f}")
        return last_price, last_date

    except Exception as e:
        print(f"❌ Error fetching data for {ticker_symbol}: {e}")
        return None, None

# Example usage
ticker_symbol = "AAPL"  # Change this to your desired stock ticker
reference_date = datetime.today().date()

last_price, last_date = get_last_available_price(ticker_symbol, reference_date)

if last_price is not None:
    print(f"\n🎯 Final Result: {ticker_symbol} last price on {last_date}: {last_price:.2f}")
else:
    print(f"\n⚠️ Could not retrieve a valid price for {ticker_symbol}.")












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
