import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.title("Apple Stock Prices")

# Define the ticker symbol for Apple
ticker_symbol = 'AAPL'

# Get the data of the stock
apple_stock = yf.Ticker(ticker_symbol)

# Define default date range (past year)
end_date = datetime.today().date()
start_date = end_date - timedelta(days=365)

# Create date input widgets
st.sidebar.header("Select Date Range")
start_date = st.sidebar.date_input("From", start_date)
end_date = st.sidebar.date_input("To", end_date)

# Get the historical prices for Apple stock based on the selected date range
historical_prices = apple_stock.history(start=start_date, end=end_date)

# Create a matplotlib figure
fig, ax = plt.subplots()

# Plot the historical data
ax.plot(historical_prices.index, historical_prices['Close'], label='Stock Value')
ax.set_xlabel('Date')
ax.set_ylabel('Stock Value')
ax.set_title('Apple Stock Value')
ax.legend(loc='upper left')
ax.tick_params(axis='x', rotation=45)

# Use st.pyplot to display the plot
st.pyplot(fig)

# Show the latest stock value in the app
if not historical_prices.empty:
    latest_price = historical_prices['Close'].iloc[-1]
    latest_time = historical_prices.index[-1].strftime('%Y-%m-%d')
    st.write(f"Latest Price ({latest_time}): {latest_price}")
else:
    st.write("No data available for the selected date range.")
