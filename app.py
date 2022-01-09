import os
import streamlit as st
import requests
import simplejson as json
import pandas as pd
import csv

# Get Alpha Vantage API key
key = os.environ.get('KEY')

# Get list of active stocks
stocks_url = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={}'.format(key)
stocks = pd.read_csv(stocks_url)
# st.dataframe(stocks)

# Choose stock ticker
# ticker = st.selectbox('Choose stock ticker:', ('AAPL', 'GOOG'))
ticker = st.selectbox('Choose a stock ticker:', stocks['symbol'])

# Make API request
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)

# Extract data
data = response.json()
df=pd.DataFrame.from_dict(data['Time Series (Daily)'], orient="index")

# Display resulting pandas data frame
# st.dataframe(df)

# Plot closing values
st.line_chart(df['4. close'][0:30])