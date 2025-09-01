import pandas as pd
import pandas_ta as ta
from crewai.tools import tool

@tool("Technical Analyzer")
def analyze_technical_data(data_json: str) -> str:
    """
    Performs technical analysis on stock data and returns the data with indicators.
    The input is a JSON string of a pandas DataFrame.
    The output is a JSON string of the analyzed pandas DataFrame.
    """
    try:
        data = pd.read_json(data_json, orient='split')
    except Exception as e:
        return f"Error loading data from JSON: {e}"

    if data.empty:
        return "Input data is empty."

    # Calculate RSI
    data.ta.rsi(append=True)

    # Calculate MACD
    data.ta.macd(append=True)

    # Calculate Simple Moving Averages (SMA)
    data.ta.sma(length=20, append=True)
    data.ta.sma(length=50, append=True)

    # Remove rows with NaN values
    data.dropna(inplace=True)

    return data.to_json(orient='split')
