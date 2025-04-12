import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.config import Config
from src.agents import AgentRegistry
from src.utils.logging import setup_logging

app = FastAPI(title="SmartAgent")
config = Config()
setup_logging(config)

class Query(BaseModel):
    query: str
    agent_type: str = "default"

@app.post("/agent/query")
async def query_agent(query: Query):
    try:
        agent = AgentRegistry.get_agent(query.agent_type)
        response = await agent.process_query(query.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=config.debug_mode)