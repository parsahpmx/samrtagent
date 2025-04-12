from typing import Dict
from langchain import Chain
from ..config import Config

class ChainRegistry:
    def __init__(self, config: Config):
        self.config = config
        self.chains: Dict[str, Chain] = {}
    
    def register_chain(self, name: str, chain: Chain):
        self.chains[name] = chain
    
    def get_chain(self, name: str) -> Chain:
        return self.chains.get(name)
    
    def list_chains(self) -> list[str]:
        return list(self.chains.keys())