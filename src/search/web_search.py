from typing import List, Dict, Any
from serpapi import GoogleSearch
from ..config import Config

class WebSearch:
    def __init__(self, config: Config):
        self.config = config
    
    async def search(self, query: str) -> List[Dict[str, Any]]:
        """Perform web search using SerpAPI"""
        search = GoogleSearch({
            "q": query,
            "api_key": self.config.serpapi_key
        })
        return search.get_dict().get("organic_results", [])