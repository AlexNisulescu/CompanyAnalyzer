import yfinance as yf
import pandas as pd

tsla = yf.Ticker("TSLA")
print(tsla.info['sector'])
print(tsla.info['industry'])
print(tsla.info['marketCap'])
print(tsla.info['currentPrice'])
print(tsla.info['freeCashflow'])
print(tsla.info['currentRatio'])
print(tsla.info['returnOnAssets'])
print(tsla.info['returnOnEquity'])
print(tsla.info['debtToEquity'])
print(tsla.info['totalCash'])
print(tsla.info['totalDebt'])
print(tsla.info['totalAssets'])
print(tsla.info['lastDividendValue'])
print(tsla.info['fiveYearAvgDividendYield'])
print(tsla.info['threeYearAverageReturn'])
print(tsla.info['fiveYearAverageReturn'])
print(tsla.info['totalAssets'])
print(tsla.info['trailingPE'])
print(tsla.info['forwardPE'])
print(tsla.info['profitMargins'])
print(tsla.info['grossMargins'])
print(tsla.info['morningStarRiskRating'])
print(tsla.info['morningStarOverallRating'])

companydf = pd.DataFrame(columns=['Name', 'Sector', 'Industry', 'MarketCap',
                        'P/E', 'Current Price', 'Return on Equity', 
                        'Return on Assets', 'Current Ratio', 'Debt to Equity',
                        'Profit Margins', 'Gross Margins', 
                        'Five Years Average Dividend Yeald', 'Last Dividend Value',
                        'Three Year Average Return', 'Five Year Average Return', 
                        'Total Cash', 'Total Assets', 'Total Debt', 'Forward P/E',
                        'morning Star Risk Rating', 'Morning Star Overall Rating'])


# new_row = {'name':'Geo', 'physics':87, 'chemistry':92, 'algebra':97}
# #append row to the dataframe
# df_marks = df_marks.append(new_row, ignore_index=True)



# df = pd.read_excel("Tickers.xlsx", sheet_name="Tickers")

# for ticker in df['Ticker']:
#     # print(ticker)
#     details = yf.Ticker(ticker)
#     details.info
