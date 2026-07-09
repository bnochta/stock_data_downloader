import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plot


def download_data(ticker: str, start: str, end: str):
    """Downloads raw stock market data from yahoo finance"""
    raw_data = yf.download(ticker, start, end)
    return raw_data

def clean_data(data: pd.DataFrame, ticker: str):
    """Basic data cleaning steps, inserts ticker as column."""
    data.columns = raw_data.columns.get_level_values(0)
    clean_data = raw_data.dropna()
    clean_data.index = pd.to_datetime(data.index)
    clean_data = clean_data.reset_index()
    clean_data.insert(0,"Ticker", ticker)
    return clean_data

def save_data(data: pd.DataFrame, ticker: str, start: str, end: str):
    """Saves the data into the project subfolder"""
    path = f"../data/{ticker}_{start}_-_{end}.csv"
    data.to_csv(path)
    print(f"{ticker} data saved.")


ticker = input("Ticker:")
start = input("Start date (YYYY-MM-DD):")
end = input("End date (YYYY-MM-DD):")

raw_data = download_data(ticker, start, end)
clean_data = clean_data(raw_data, ticker)
save_data(clean_data, ticker, start, end)

from visualizer import plot_close_price
plot_close_price(clean_data, ticker)