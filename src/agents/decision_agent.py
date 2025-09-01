import pandas as pd

class DecisionAgent:
    """
    Agent responsible for making buy/sell/hold decisions based on technical indicators.
    """
    def decide(self, data: pd.DataFrame) -> str:
        """
        Makes a decision for the latest data point.

        Args:
            data (pd.DataFrame): The stock data with technical indicators.

        Returns:
            str: The decision ('BUY', 'SELL', or 'HOLD').
        """
        if data.empty:
            return 'HOLD'

        latest_data = data.iloc[-1]

        # A simple strategy
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
