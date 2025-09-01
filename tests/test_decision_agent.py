import sys
import os
import pandas as pd
import pytest

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agents.decision_agent import DecisionAgent

@pytest.fixture
def decision_agent():
    """Pytest fixture to create a DecisionAgent instance."""
    return DecisionAgent()

def test_decide_buy(decision_agent):
    """Test the BUY decision logic."""
    data = {
        'SMA_20': [110],
        'SMA_50': [100],
        'RSI_14': [60],
        'MACD_12_26_9': [5],
        'MACDs_12_26_9': [4]
    }
    df = pd.DataFrame(data)
    assert decision_agent.decide(df) == 'BUY'

def test_decide_sell(decision_agent):
    """Test the SELL decision logic."""
    data = {
        'SMA_20': [90],
        'SMA_50': [100],
        'RSI_14': [40],
        'MACD_12_26_9': [4],
        'MACDs_12_26_9': [5]
    }
    df = pd.DataFrame(data)
    assert decision_agent.decide(df) == 'SELL'

def test_decide_hold_sma_cross_miss(decision_agent):
    """Test the HOLD decision when SMA cross is not met for buy."""
    data = {
        'SMA_20': [90],
        'SMA_50': [100],
        'RSI_14': [60],
        'MACD_12_26_9': [5],
        'MACDs_12_26_9': [4]
    }
    df = pd.DataFrame(data)
    assert decision_agent.decide(df) == 'HOLD'

def test_decide_hold_rsi_miss(decision_agent):
    """Test the HOLD decision when RSI condition is not met for buy."""
    data = {
        'SMA_20': [110],
        'SMA_50': [100],
        'RSI_14': [80],
        'MACD_12_26_9': [5],
        'MACDs_12_26_9': [4]
    }
    df = pd.DataFrame(data)
    assert decision_agent.decide(df) == 'HOLD'

def test_decide_hold_macd_miss(decision_agent):
    """Test the HOLD decision when MACD condition is not met for buy."""
    data = {
        'SMA_20': [110],
        'SMA_50': [100],
        'RSI_14': [60],
        'MACD_12_26_9': [4],
        'MACDs_12_26_9': [5]
    }
    df = pd.DataFrame(data)
    assert decision_agent.decide(df) == 'HOLD'

def test_decide_empty_data(decision_agent):
    """Test the decision for empty data."""
    df = pd.DataFrame()
    assert decision_agent.decide(df) == 'HOLD'
