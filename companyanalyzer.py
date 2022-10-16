from multiprocessing import current_process
import string
import yfinance as yf # Used for financial data
import pandas as pd # Used to store data in a dataframe
from datetime import date


def earning_per_share_calculator(price_to_earnings, current_price):
    return current_price / price_to_earnings

def growth_rate_calculator(history_price, current_price):
    return ((history_price + current_price) / history_price)

# This function is used to calculate the intrinsic value of a company
def intrinsic_value_calculator(price_to_earnings, current_price, ten_years_price):
    # V = [ EPS * (8.5 + 2 * g) * 4.4 ] / Y , where:
    # EPS = earnings_per_share
    # g = growth_rate
    # Y = bond_yield
    Y = 5.21
    earnings_per_share = earning_per_share_calculator(price_to_earnings, current_price)
    growth_rate = growth_rate_calculator(ten_years_price, current_price)
    return int((earnings_per_share * (8.5 + (2 * growth_rate)) * 4.4) / Y)

# This function is used to calculate the margin of safety of a company
def margin_of_safety(intrinsic_value, current_market_price):
    # MS = ( V - CMP ) / V , where:
    # V = intrinsic_value
    # CMP = current_market_price
    return "{:.2f}".format(float(intrinsic_value - current_market_price) / intrinsic_value * 100)

# This function is used to read the list of tickers
def read_tickers(filename):
    file = open(filename, "r")
    tkrs = file.read().splitlines()
    return tkrs

# This function creates the dataframe structure that will store the data
def create_df():
    df = pd.DataFrame(columns=['Name', 'Sector', 'Industry', 'MarketCap',
                        'P/E', 'Current Price', 'Intrinsic Value', 'Margin of Safety',
                        'Return on Equity', 'Return on Assets', 'Current Ratio',
                        'Debt to Equity', 'Profit Margins', 'Gross Margins', 
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
        worth = calculate_worth(details.info['totalCash'],
                details.info['totalAssets'], details.info['totalDebt'])
        ten_years_price = details.history(period='10y')
        current_price = details.history(period='1d')
        intrinsic_value = intrinsic_value_calculator(details.info['trailingPE'],
                          current_price['Close'][0], ten_years_price['Close'][0])
        safety_margin = margin_of_safety(intrinsic_value, current_price['Close'][0])
        safety_margin = str(safety_margin) + '%'
        # Creates a new row for the dataframe
        new_row = {'Name':ticker, 'Sector':details.info['sector'], 'Industry':
        details.info['industry'], 'MarketCap':details.info['marketCap'],
        'P/E':details.info['trailingPE'], 'Current Price':
        details.info['currentPrice'], 'Intrinsic Value':intrinsic_value,
        'Margin of Safety':safety_margin,'Debt to Equity':details.info['debtToEquity'],
        'Profit Margins':details.info['profitMargins'], 'Gross Margins':
        details.info['grossMargins'], 'Five Years Average Dividend Yeald':
        details.info['fiveYearAvgDividendYield'], 'Last Dividend Value':
        details.info['lastDividendValue'], 'Three Year Average Return':
        details.info['threeYearAverageReturn'], 'Five Year Average Return':
        details.info['fiveYearAverageReturn'], 'Worth':worth ,
        'Total Cash':details.info['totalCash'],'Total Assets':
        details.info['totalAssets'], 'Total Debt':details.info['totalDebt'],
        'Forward P/E':details.info['forwardPE']}
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