import os
from datetime import datetime, timedelta

from crewai import Agent, Task, Crew, Process

# Set a dummy API key to avoid errors.
# The user should replace this with their actual key.
os.environ["OPENAI_API_KEY"] = "DUMMY_KEY"
os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1"


# Add src to path to be able to import tools
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from tools.data_collection_tool import fetch_stock_data
from tools.technical_analysis_tool import analyze_technical_data
from tools.decision_tool import make_trading_decision

# Define the Agents
data_collector = Agent(
    role='Stock Data Collector',
    goal='Fetch historical stock data for a given ticker.',
    backstory='An expert at retrieving financial data from the web.',
    verbose=True,
    allow_delegation=False,
    tools=[fetch_stock_data]
)

technical_analyst = Agent(
    role='Technical Analyst',
    goal='Analyze the provided stock data and add key technical indicators.',
    backstory='A seasoned analyst with a deep understanding of technical analysis.',
    verbose=True,
    allow_delegation=False,
    tools=[analyze_technical_data]
)

trading_advisor = Agent(
    role='Trading Advisor',
    goal='Provide a final recommendation (BUY, SELL, or HOLD) based on the technical analysis.',
    backstory='An experienced trading advisor who makes decisions based on data.',
    verbose=True,
    allow_delegation=False,
    tools=[make_trading_decision]
)

# Define the Tasks
collect_data_task = Task(
    description='Fetch historical stock data for {ticker} from {start_date} to {end_date}.',
    agent=data_collector,
    expected_output='A JSON string representing the stock data.'
)

analyze_data_task = Task(
    description='Analyze the stock data from the previous step to identify trends.',
    agent=technical_analyst,
    expected_output='A JSON string of the data with technical indicators added.'
)

advise_trade_task = Task(
    description='Use the analyzed stock data to make a final trading recommendation.',
    agent=trading_advisor,
    expected_output='A final recommendation string: "BUY", "SELL", or "HOLD".'
)


# Create the Crew
stock_analysis_crew = Crew(
    agents=[data_collector, technical_analyst, trading_advisor],
    tasks=[collect_data_task, analyze_data_task, advise_trade_task],
    process=Process.sequential,
    verbose=True
)

def main():
    """
    Main function to run the CrewAI stock analysis.
    """
    ticker = 'AAPL'
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')

    print(f"Running CrewAI analysis for {ticker} from {start_date} to {end_date}...")

    inputs = {
        'ticker': ticker,
        'start_date': start_date,
        'end_date': end_date
    }

    result = stock_analysis_crew.kickoff(inputs=inputs)

    print("\n\n########################")
    print("## Crew Analysis Result:")
    print("########################")
    print(result)

if __name__ == "__main__":
    main()
