import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
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

# Create an interactive plotly chart
fig = go.Figure()

# Add the close price line
fig.add_trace(go.Scatter(x=historical_prices.index, y=historical_prices['Close'], mode='lines', name='Close Price'))

# Add the volume bar
fig.add_trace(go.Bar(x=historical_prices.index, y=historical_prices['Volume'], name='Volume', yaxis='y2', opacity=0.4))

# Update layout for better visualization
fig.update_layout(
    title='Apple Stock Prices',
    xaxis_title='Date',
    yaxis_title='Stock Price (USD)',
    yaxis2=dict(title='Volume', overlaying='y', side='right'),
    xaxis=dict(rangeslider=dict(visible=True)),
    legend=dict(x=0, y=1.2, orientation='h')
)

# Display the plotly chart
st.plotly_chart(fig)

# Show the latest stock value in the app
if not historical_prices.empty:
    latest_price = historical_prices['Close'].iloc[-1]
    latest_time = historical_prices.index[-1].strftime('%Y-%m-%d')
    st.write(f"Latest Price ({latest_time}): ${latest_price:.2f}")
else:
    st.write("No data available for the selected date range.")

