import yfinance as yf # Used for financial data
import pandas as pd # Used to store data in a dataframe

# This function is used to read the list of tickers
def read_tickers(filename):
    file = open(filename, "r")
    tkrs = file.read().splitlines()
    return tkrs

# This function creates the dataframe structure that will store the data
def create_df():
    df = pd.DataFrame(columns=['Name', 'Sector', 'Industry', 'MarketCap',
                        'P/E', 'Current Price', 'Return on Equity', 
                        'Return on Assets', 'Current Ratio', 'Debt to Equity',
                        'Profit Margins', 'Gross Margins', 
                        'Five Years Average Dividend Yeald', 'Last Dividend Value',
                        'Three Year Average Return', 'Five Year Average Return', 
                        'Total Cash', 'Total Assets', 'Total Debt', 'Forward P/E',
                        'Morning Star Risk Rating', 'Morning Star Overall Rating'])
    return df

# This function gets the details of the companies and stores them in a dataframe
def get_details(tkrs):
    df = create_df()
    # Parses the whole list of tickers
    for ticker in tkrs:
        # Requests the company details
        details = yf.Ticker(ticker)
        # Creates a new row for the dataframe
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
        # Appends the new row to the dataframe
        df = df.append(new_row, ignore_index=True)
    return df
    
# This functions saves the dataframe to an excell
def save_dataframe_to_excell(df):
    df.to_excel('companies.xlsx')
# This functions saves the dataframe to a csv
def save_dataframe_to_csv(df):
    df.to_csv('companies.csv')

# Reading the tickers
tickers = read_tickers("Tickers")
# Getting companies details
companydf = get_details(tickers)
# Saving the details to an Excell file
save_dataframe_to_excell(companydf)