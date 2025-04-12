from typing import Any, Dict
import aiohttp
from ..config import Config

class N8NClient:
    def __init__(self, config: Config):
        self.config = config
        self.base_url = config.n8n_url
        self.api_key = config.n8n_api_key
    
    async def trigger_workflow(self, workflow_id: str, data: Dict[str, Any]):
        """Trigger n8n workflow"""
        async with aiohttp.ClientSession() as session:
            headers = {"X-N8N-API-KEY": self.api_key}
            async with session.post(
                f"{self.base_url}/webhook/{workflow_id}",
                json=data,
                headers=headers
            ) as resp:
                return await resp.json()