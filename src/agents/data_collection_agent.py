import yfinance as yf
import pandas as pd

class DataCollectionAgent:
    """
    Agent responsible for collecting historical stock data.
    """
    def fetch_data(self, ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetches historical stock data for a given ticker.

        Args:
            ticker (str): The stock ticker symbol (e.g., 'AAPL').
            start_date (str): The start date for the data in 'YYYY-MM-DD' format.
            end_date (str): The end date for the data in 'YYYY-MM-DD' format.

        Returns:
            pd.DataFrame: A pandas DataFrame with the historical stock data.
        """
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        if data.empty:
            raise ValueError(f"No data found for ticker {ticker} from {start_date} to {end_date}")
        return data
