# Legal Contract Review Agent

An AI-powered contract review agent built with Google Agent Development Kit (ADK) that helps you search and analyze legal contracts using semantic search.

## Features

- **Semantic Search**: Find relevant contract clauses using natural language queries
- **Contract Analysis**: Analyze specific clauses for legal implications
- **Local Embeddings**: Uses ChromaDB and sentence-transformers for privacy-focused local search
- **Multiple Contract Support**: Index and search across multiple contracts simultaneously
- **Web Interface**: Interactive chat interface via ADK's web UI

## Project Structure

```
contract_review_agent/
├── __init__.py              # Package initialization
├── agent.py                 # Main ADK agent definition
├── contract_search.py       # Search engine with ChromaDB
├── index_contracts.py       # Utility to index contract files
├── data/
│   ├── contracts/          # Place your contract files here (.txt)
│   └── chroma_db/          # ChromaDB vector database (auto-generated)
├── .env.example            # Environment variable template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Prerequisites

- Python 3.10 or higher
- Google AI API key (free from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Virtual environment (recommended)

## Setup Instructions

### 1. Install Dependencies

The virtual environment and packages are already set up in the parent directory. Activate it:

```bash
cd /Users/jamesgornall/agent-testing
source .venv/bin/activate
```

If you need to install packages manually:

```bash
pip install google-adk sentence-transformers chromadb
```

### 2. Configure Environment Variables

Create a `.env` file in the `contract_review_agent` directory:

```bash
cd contract_review_agent
cp .env.example .env
```

Edit `.env` and add your Google AI API key:

```
GOOGLE_API_KEY=your_actual_api_key_here
MODEL=gemini-2.0-flash-001
```

**Get your API key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) to create a free API key.

### 3. Index Sample Contracts

Three sample contracts are included in `data/contracts/`:
- `sample_employment_contract.txt` - Employment agreement with various clauses
- `sample_nda.txt` - Non-disclosure agreement
- `sample_service_agreement.txt` - Professional services contract

Index them into the search engine:

```bash
cd contract_review_agent
python index_contracts.py
```

You should see output like:
```
Found 3 contract files

Indexing: sample_employment_contract.txt
  ✓ Indexed 12 chunks

Indexing: sample_nda.txt
  ✓ Indexed 15 chunks

Indexing: sample_service_agreement.txt
  ✓ Indexed 18 chunks

==================================================
Indexing complete!
Total chunks indexed: 45
==================================================
```

### 4. Add Your Own Contracts

To index your own contracts:

1. Save your contracts as `.txt` files in `data/contracts/`
2. Run the indexer again: `python index_contracts.py`

Or index a single contract:
```bash
python index_contracts.py path/to/your/contract.txt
```

## Running the Agent

### Option 1: Web Interface (Recommended)

Launch the ADK web interface:

```bash
cd /Users/jamesgornall/agent-testing
source .venv/bin/activate
cd contract_review_agent
adk web
```

Then open your browser to [http://localhost:8000](http://localhost:8000)

### Option 2: CLI Interface

Use the ADK CLI:

```bash
adk run contract_review_agent.agent.contract_agent
```

## Example Queries

Try these queries with your agent:

**Finding Specific Clauses:**
- "Find all non-compete clauses"
- "Show me confidentiality provisions"
- "What does the contract say about intellectual property?"
- "Find termination clauses"
- "Show liability limitations"

**Analysis Requests:**
- "Analyze the non-compete clause in the employment contract"
- "What are the risks in the indemnification provisions?"
- "Explain the confidentiality requirements"
- "Summarize the payment terms"

**General Questions:**
- "Which contracts mention intellectual property rights?"
- "What are the notice requirements across all contracts?"
- "Find clauses about data protection"

## How It Works

### Architecture

1. **Contract Indexing**: Contracts are split into semantic chunks and embedded using the `all-MiniLM-L6-v2` model
2. **Vector Storage**: ChromaDB stores embeddings locally for fast semantic search
3. **ADK Agent**: Gemini 2.0 Flash model orchestrates search and analysis using custom tools
4. **Search Tools**:
   - `search_contracts`: Performs semantic search across indexed contracts
   - `analyze_clause`: Provides basic analysis of contract clauses

### Custom Tools

The agent has access to two main tools:

**search_contracts(query, top_k)**
- Searches indexed contracts using semantic similarity
- Returns relevant contract sections with metadata
- Highlights which contract each result comes from

**analyze_clause(clause_text, analysis_type)**
- Analyzes specific contract clauses
- Identifies key topics (liability, IP, confidentiality, etc.)
- Provides basic risk assessment

## Advanced Usage

### Customizing the Search

Edit `contract_search.py` to customize:
- Chunk size (default: 500 characters)
- Embedding model (default: `all-MiniLM-L6-v2`)
- Search parameters (top_k, distance threshold)

### Customizing the Agent

Edit `agent.py` to customize:
- Agent instructions and behavior
- Model selection (Gemini 2.0 Flash, Gemini Pro, etc.)
- Tool configurations

### Using Different Models

You can use different Gemini models by setting the `MODEL` environment variable:

```bash
# In your .env file
MODEL=gemini-1.5-pro-002        # More capable, slower
MODEL=gemini-2.0-flash-001      # Fast, efficient (default)
```

## Limitations

- **Legal Disclaimer**: This is an AI tool for assistance only. Always consult qualified legal counsel for important contract decisions.
- **Analysis Depth**: Basic clause analysis is keyword-based. For deeper analysis, the agent relies on the LLM's reasoning.
- **Contract Format**: Currently supports plain text files. PDFs would need conversion to text first.
- **Privacy**: All processing happens locally except LLM calls to Google AI.

## Troubleshooting

**"No module named 'google.adk'"**
- Make sure you've activated the virtual environment: `source .venv/bin/activate`
- Reinstall: `pip install google-adk`

**"API key not found"**
- Check that `.env` file exists in `contract_review_agent/` directory
- Verify `GOOGLE_API_KEY` is set correctly
- Make sure you're running from the correct directory

**"No matching clauses found"**
- Verify contracts are indexed: `python index_contracts.py`
- Check that contract files are in `data/contracts/`
- Try broader search queries

**ChromaDB errors**
- Delete `data/chroma_db/` directory and re-index contracts
- Make sure you have write permissions in the project directory

## Future Enhancements

Potential improvements:
- PDF contract support
- Clause comparison across contracts
- Risk scoring algorithms
- Contract template generation
- Multi-language support
- Integration with document management systems
- Export search results to structured formats

## License

This is a sample project for demonstration purposes.

## Support

For Google ADK documentation: [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)
