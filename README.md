# SmartAgent

A powerful multi-LLM agent system that integrates various AI capabilities through LangChain, ROG functions, MCP, web search, and n8n automation.

## Features

- 🤖 Multiple LLM Integration (GPT-4, Claude, etc.)
- 🔗 LangChain for complex reasoning chains
- 🌐 Web search capabilities
- 🔄 ROG (Retrieval-Oriented Generation) functions
- 🔌 MCP (Multi-Channel Platform) integration
- 🔧 n8n workflow automation
- 📚 Knowledge base management
- 🎯 Task routing and orchestration

## Architecture

```
smartagent/
├── agents/          # Different agent implementations
├── chains/          # LangChain chains
├── integrations/    # External integrations (n8n, MCP)
├── knowledge/       # Knowledge base management
├── rog/             # ROG function implementations
├── search/          # Web search capabilities
└── utils/           # Utility functions
```

## Prerequisites

- Python 3.9+
- n8n instance
- MCP setup
- API keys for various LLMs

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parsahpmx/samrtagent.git
   cd samrtagent
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configurations
   ```

## Configuration

Configure the following in your `.env` file:

```env
# LLM API Keys
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# MCP Configuration
MCP_API_KEY=your_mcp_key
MCP_BASE_URL=your_mcp_url

# n8n Configuration
N8N_URL=your_n8n_url
N8N_API_KEY=your_n8n_key

# Search Configuration
SERPAPI_KEY=your_serpapi_key
```

## Usage

1. Start the agent system:
   ```bash
   python main.py
   ```

2. Access the API:
   ```bash
   curl http://localhost:8000/agent/query -d '{"query": "your question here"}'
   ```

## Development

### Adding New Agents

1. Create new agent in `agents/` directory
2. Implement required interfaces
3. Register in agent registry

### Adding New Chains

1. Create new chain in `chains/` directory
2. Configure chain components
3. Register in chain registry

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Create pull request

## License

MIT License - see LICENSE file