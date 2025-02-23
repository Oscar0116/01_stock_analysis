import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf

# Download Tesla stock data
tesla = yf.Ticker("TSLA")
tesla_stock_data = tesla.history(period="max")
print(tesla_stock_data.head())
