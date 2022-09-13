import yfinance as yf
import pandas as pd

file = open("Tickers", "r")
tkrs = file.read().splitlines()

for ticker in tkrs:
    details = yf.Ticker(ticker)
    print(details.info)