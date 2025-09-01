import sys
import os
from datetime import datetime, timedelta

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from master_agent import MasterAgent

def main():
    """
    Main function to run the stock analysis.
    """
    # Configuration
    ticker = 'AAPL'
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

    print(f"Running analysis for {ticker} from {start_date} to {end_date}...")

    # Initialize and run the master agent
    master = MasterAgent()
    decision = master.run_analysis(ticker, start_date, end_date)

    print(f"Ticker: {ticker}")
    print(f"Decision: {decision}")

if __name__ == "__main__":
    main()
