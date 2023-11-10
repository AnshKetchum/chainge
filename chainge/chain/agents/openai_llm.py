import chainge 

#We'll use OpenAI as the standard, but our primary goal is to make chainge focused towards with more open source LLMs
from langchain.llms import OpenAI
from chainge.chain.tools.utils import StockLookupTool
from chainge.chain.tools.fundamentals import StockFundamentalsTool, StockFundamentalsProbeTool
from chainge.chain.tools.utils import AlternativesLookupTool
from chainge.chain.tools.fundamentals import StockFinancialReportsTool
from langchain.agents import initialize_agent, AgentType
from chainge.config import OPENAI_API_KEY


def load_agent():
    llm = OpenAI(temperature = 0, openai_api_key= OPENAI_API_KEY)

    tools = [
        StockFundamentalsProbeTool(),
        StockFundamentalsTool(),
        StockLookupTool(),
        AlternativesLookupTool(),
        StockFinancialReportsTool(),
    ]

    agent_executor = initialize_agent(
        tools,
        llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
