import sys
import os
import pandas as pd
import pytest

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agents.technical_analysis_agent import TechnicalAnalysisAgent

@pytest.fixture
def technical_analysis_agent():
    """Pytest fixture to create a TechnicalAnalysisAgent instance."""
    return TechnicalAnalysisAgent()

@pytest.fixture
def sample_stock_data():
    """Pytest fixture to create sample stock data."""
    # Create enough data to avoid NaNs after indicator calculation
    data = {
        'Open': [i for i in range(100, 200)],
        'High': [i * 1.05 for i in range(100, 200)],
        'Low': [i * 0.95 for i in range(100, 200)],
        'Close': [i for i in range(100, 200)],
        'Volume': [1000 for _ in range(100, 200)]
    }
    return pd.DataFrame(data)

def test_analyze_adds_indicators(technical_analysis_agent, sample_stock_data):
    """Test that the analyze method adds the correct indicator columns."""
    # Act
    analyzed_data = technical_analysis_agent.analyze(sample_stock_data)

    # Assert
    assert 'RSI_14' in analyzed_data.columns
    assert 'MACD_12_26_9' in analyzed_data.columns
    assert 'MACDs_12_26_9' in analyzed_data.columns
    assert 'MACDh_12_26_9' in analyzed_data.columns
    assert 'SMA_20' in analyzed_data.columns
    assert 'SMA_50' in analyzed_data.columns
    assert not analyzed_data.isnull().values.any()
