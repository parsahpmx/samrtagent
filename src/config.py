from pydantic import BaseSettings
from dotenv import load_dotenv
import os

class Config(BaseSettings):
    # Load environment variables
    load_dotenv()
    
    # LLM API Keys
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    
    # MCP Configuration
    mcp_api_key: str = os.getenv("MCP_API_KEY", "")
    mcp_base_url: str = os.getenv("MCP_BASE_URL", "http://localhost:3000")
    
    # n8n Configuration
    n8n_url: str = os.getenv("N8N_URL", "http://localhost:5678")
    n8n_api_key: str = os.getenv("N8N_API_KEY", "")
    
    # Search Configuration
    serpapi_key: str = os.getenv("SERPAPI_KEY", "")
    
    # Agent Configuration
    default_llm: str = os.getenv("DEFAULT_LLM", "gpt-4")
    debug_mode: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Database Configuration
    vectorstore_path: str = os.getenv("VECTORSTORE_PATH", "./data/vectorstore")
    knowledge_base_path: str = os.getenv("KNOWLEDGE_BASE_PATH", "./data/knowledge")
    
    class Config:
        env_file = ".env"
        case_sensitive = True