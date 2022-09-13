import yfinance as yf
import pandas as pd

file = open("Tickers", "r")
tkrs = file.read().splitlines()
companydf = pd.DataFrame(columns=['Name', 'Sector', 'Industry', 'MarketCap',
                        'P/E', 'Current Price', 'Return on Equity', 
                        'Return on Assets', 'Current Ratio', 'Debt to Equity',
                        'Profit Margins', 'Gross Margins', 
                        'Five Years Average Dividend Yeald', 'Last Dividend Value',
                        'Three Year Average Return', 'Five Year Average Return', 
                        'Total Cash', 'Total Assets', 'Total Debt', 'Forward P/E',
                        'Morning Star Risk Rating', 'Morning Star Overall Rating'])

for ticker in tkrs:
    details = yf.Ticker(ticker)
    new_row = {'Name':ticker, 'Sector':details.info['sector'], 'Industry':
    details.info['industry'], 'MarketCap':details.info['marketCap'],
    'P/E':details.info['trailingPE'], 'Current Price':
    details.info['currentPrice'], 'Debt to Equity':details.info['debtToEquity'],
    'Profit Margins':details.info['profitMargins'], 'Gross Margins':
    details.info['grossMargins'], 'Five Years Average Dividend Yeald':
    details.info['fiveYearAvgDividendYield'], 'Last Dividend Value':
    details.info['lastDividendValue'], 'Three Year Average Return':
    details.info['threeYearAverageReturn'], 'Five Year Average Return':
    details.info['fiveYearAverageReturn'], 'Total Cash':details.info['totalCash'],
    'Total Assets':details.info['totalAssets'], 'Total Debt':
    details.info['totalDebt'], 'Forward P/E':details.info['forwardPE'],
    'Morning Star Risk Rating':details.info['morningStarRiskRating'],
    'Morning Star Overall Rating':details.info['morningStarOverallRating']}
    # #append row to the dataframe
    companydf = companydf.append(new_row, ignore_index=True)
    
companydf.to_excel('companyes.xlsx')