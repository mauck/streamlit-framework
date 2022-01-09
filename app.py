# Sample Python Integration Code for Alpha Vantage
# From:
# https://medium.com/@patrick.collins_58673/stock-api-landscape-5c6e054ee631

import requests
import json

key = 'XXX'
ticker = 'AAPL'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)

response = requests.get(url)
print(response.json())