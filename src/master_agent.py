from agents.data_collection_agent import DataCollectionAgent
from agents.technical_analysis_agent import TechnicalAnalysisAgent
from agents.decision_agent import DecisionAgent

class MasterAgent:
    """
    The master agent that orchestrates the other agents to perform stock analysis.
    """
    def __init__(self):
        self.data_collection_agent = DataCollectionAgent()
        self.technical_analysis_agent = TechnicalAnalysisAgent()
        self.decision_agent = DecisionAgent()

    def run_analysis(self, ticker: str, start_date: str, end_date: str) -> str:
        """
        Runs the full analysis pipeline for a given stock.

        Args:
            ticker (str): The stock ticker symbol.
            start_date (str): The start date for the analysis.
            end_date (str): The end date for the analysis.

        Returns:
            str: The final decision ('BUY', 'SELL', or 'HOLD').
        """
        try:
            # 1. Collect data
            stock_data = self.data_collection_agent.fetch_data(ticker, start_date, end_date)

            # 2. Analyze data
            analyzed_data = self.technical_analysis_agent.analyze(stock_data)

            # 3. Make a decision
            decision = self.decision_agent.decide(analyzed_data)

            return decision
        except Exception as e:
            return f"An error occurred: {e}"
