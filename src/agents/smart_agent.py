from typing import Any, Dict
from .base import BaseAgent
from ..chains import ChainRegistry
from ..rog import ROGFunctions
from ..search import WebSearch
from ..integrations.mcp import MCPClient
from ..integrations.n8n import N8NClient

class SmartAgent(BaseAgent):
    async def initialize(self):
        self.chain_registry = ChainRegistry(self.config)
        self.rog_functions = ROGFunctions(self.config)
        self.web_search = WebSearch(self.config)
        self.mcp_client = MCPClient(self.config)
        self.n8n_client = N8NClient(self.config)
    
    async def process_query(self, query: str) -> Dict[str, Any]:
        # 1. Analyze query intent
        intent = await self.chain_registry.get_chain("intent").run(query)
        
        # 2. Search relevant information
        search_results = await self.web_search.search(query)
        
        # 3. Apply ROG functions
        rog_results = await self.rog_functions.process(query, search_results)
        
        # 4. Generate response using appropriate chain
        response = await self.chain_registry.get_chain(intent).run({
            "query": query,
            "search_results": search_results,
            "rog_results": rog_results
        })
        
        # 5. Trigger relevant n8n workflows
        await self.n8n_client.trigger_workflow(intent, response)
        
        # 6. Send response through MCP
        await self.mcp_client.send_response(response)
        
        return response