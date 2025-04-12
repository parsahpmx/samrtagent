from abc import ABC, abstractmethod
from typing import Any, Dict
from ..config import Config

class BaseAgent(ABC):
    def __init__(self, config: Config):
        self.config = config
    
    @abstractmethod
    async def process_query(self, query: str) -> Dict[str, Any]:
        """Process a query and return response"""
        pass
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize agent components"""
        pass