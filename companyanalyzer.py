import yfinance as yf # Used for financial data
import pandas as pd # Used to store data in a dataframe
from datetime import date

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
                        'Worth', 'Total Cash', 'Total Assets', 'Total Debt', 
                        'Forward P/E'])
    return df

def calculate_worth(cash, assets, debt):
    if cash is None:
        cash = 0
    if assets is None:
        assets = 0
    if debt is None:
        debt = 0 
    worth = cash + assets - debt
    return worth

# This function gets the details of the companies and stores them in a dataframe
def get_details(tkrs):
    df = create_df()
    # Parses the whole list of tickers
    for ticker in tkrs:
        # Requests the company details
        details = yf.Ticker(ticker)
        try:
            details.info['totalCash'] = int(details.info['totalCash'])
        except TypeError:
            details.info['totalCash'] = 0
        try:
            details.info['totalAssets'] = int(details.info['totalAssets'])
        except TypeError:
            details.info['totalAssets'] = 0
        try:
            details.info['totalDebt'] = int(details.info['totalDebt'])
        except TypeError:
            details.info['totalDebt'] = 0
        worth = calculate_worth(details.info['totalCash'], details.info['totalAssets'], details.info['totalDebt'])
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
        details.info['fiveYearAverageReturn'], 'Worth':worth ,'Total Cash':details.info['totalCash'],
        'Total Assets':details.info['totalAssets'], 'Total Debt':
        details.info['totalDebt'], 'Forward P/E':details.info['forwardPE']}
        # Appends the new row to the dataframe
        df = df.append(new_row, ignore_index=True)
    # Sorts the companies by MarketCap
    df.sort_values(by=['MarketCap'], inplace=True)
    # Resets the index
    df = df.reset_index()
    # Drop the index column
    df.drop('index', axis=1, inplace=True)
    return df
    
# This functions saves the dataframe to an excel
def save_dataframe_to_excell(df):
    today = date.today()
    df.to_excel('companies.xlsx', sheet_name=today.strftime("%d.%m.%Y"))

# This functions saves the dataframe to a csv
def save_dataframe_to_csv(df):
    df.to_csv('companies.csv')

# Reading the tickers
tickers = read_tickers("Tickers")
# Getting companies details
companydf = get_details(tickers)
# Starting the index count from 1
companydf.index += 1
# Saving the details to an Excell file
save_dataframe_to_excell(companydf)
save_dataframe_to_csv(companydf)