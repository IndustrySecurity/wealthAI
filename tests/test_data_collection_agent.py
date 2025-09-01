import sys
import os
import pandas as pd
import pytest
from unittest.mock import patch, MagicMock

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agents.data_collection_agent import DataCollectionAgent

@pytest.fixture
def data_collection_agent():
    """Pytest fixture to create a DataCollectionAgent instance."""
    return DataCollectionAgent()

@patch('yfinance.Ticker')
def test_fetch_data_success(mock_ticker, data_collection_agent):
    """Test successful data fetching."""
    # Arrange
    mock_history = pd.DataFrame({'Close': [100, 101, 102]})
    mock_ticker.return_value.history.return_value = mock_history

    # Act
    data = data_collection_agent.fetch_data('TEST', '2023-01-01', '2023-01-03')

    # Assert
    assert not data.empty
    assert list(data.columns) == ['Close']
    assert len(data) == 3

@patch('yfinance.Ticker')
def test_fetch_data_no_data(mock_ticker, data_collection_agent):
    """Test the case where no data is returned."""
    # Arrange
    mock_ticker.return_value.history.return_value = pd.DataFrame()

    # Act & Assert
    with pytest.raises(ValueError, match="No data found for ticker TEST"):
        data_collection_agent.fetch_data('TEST', '2023-01-01', '2023-01-03')
