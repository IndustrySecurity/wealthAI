import yfinance as yf
import pandas as pd
from crewai.tools import tool

@tool("Stock Data Fetcher")
def fetch_stock_data(ticker: str, start_date: str, end_date: str) -> str:
    """
    Fetches historical stock data for a given ticker and returns it as a JSON string.
    The ticker, start_date, and end_date are required arguments.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    if data.empty:
        return "No data found."
    return data.to_json(orient='split')
