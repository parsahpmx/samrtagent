from typing import Any, Dict
import aiohttp
from ..config import Config

class MCPClient:
    def __init__(self, config: Config):
        self.config = config
        self.base_url = config.mcp_base_url
        self.api_key = config.mcp_api_key
    
    async def send_response(self, response: Dict[str, Any]):
        """Send response through MCP"""
        async with aiohttp.ClientSession() as session:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            async with session.post(
                f"{self.base_url}/api/response",
                json=response,
                headers=headers
            ) as resp:
                return await resp.json()