import pandas as pd
from crewai.tools import tool

@tool("Trading Decision Maker")
def make_trading_decision(analyzed_data_json: str) -> str:
    """
    Makes a buy, sell, or hold decision based on analyzed stock data.
    The input is a JSON string of a pandas DataFrame with technical indicators.
    """
    try:
        data = pd.read_json(analyzed_data_json, orient='split')
    except Exception as e:
        return f"Error loading data from JSON: {e}"

    if data.empty:
        return 'HOLD'

    latest_data = data.iloc[-1]

    is_buy_signal = (
        latest_data['SMA_20'] > latest_data['SMA_50'] and
        latest_data['RSI_14'] < 70 and
        latest_data['MACD_12_26_9'] > latest_data['MACDs_12_26_9']
    )

    is_sell_signal = (
        latest_data['SMA_20'] < latest_data['SMA_50'] and
        latest_data['RSI_14'] > 30 and
        latest_data['MACD_12_26_9'] < latest_data['MACDs_12_26_9']
    )

    if is_buy_signal:
        return 'BUY'
    elif is_sell_signal:
        return 'SELL'
    else:
        return 'HOLD'
