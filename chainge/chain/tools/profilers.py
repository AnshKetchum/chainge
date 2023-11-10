from langchain.tools import BaseTool, StructuredTool, Tool, tool
from pydantic import BaseModel, Field
from typing import Optional, Type

#Import our Company adapter
from chainge.api.api import company_api
from typing import Union, Tuple, Dict

class CompanyEntitySearchInput(BaseModel):
    company_name: str = Field()

class CompanyEntitySearchTool(BaseTool):
    name = "company_entity_search_tool"

    description = """Use this tool BEFORE the company lookup tool to figure out the corresponding entity names for a particular company. Pick the best 
    entity name after receiving the output that makes sense, given the context

    The entity name of a company is just the company name - i.e, apple, google facebook, etc.
    """

    args_schema: Type[BaseModel] = CompanyEntityLookupInput

    def _run(
        self, company_name: str, run_manager = None
    ) -> str:
        """Use the tool."""
        return company_api.search(company_name) 

    async def _arun(
        self, stock_ticker_name: str, run_manager = None
    ) -> str:
        """Use the tool asynchronously."""
        return company_api.search(company_name) 

class CompanyEntityLookupTool(BaseModel):
    entity_name: str = Field()


class CompanyEntityLookupTool(BaseTool):
    name = "company_entity_lookup"

    description = """Use this tool AFTER selecting a company entity using the company_entity_search_tool. You can use this tool to grab some
    basic information on a company, including a short description and some reference links.  
    """
    args_schema: Type[BaseModel] = CompanyEntityLookupTool

    def _run(
        self, stock_ticker_name: str, run_manager = None
    ) -> str:
        """Use the tool."""
        return company_api.lookup(company_name) 

    async def _arun(
        self, stock_ticker_name: str, run_manager = None
    ) -> str:
        """Use the tool asynchronously."""
        return company_api.lookup(company_name) 
