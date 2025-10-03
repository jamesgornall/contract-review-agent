# How to Run the Contract Review Agent

## Quick Start

### 1. Activate Virtual Environment & Navigate to Project
```bash
cd /Users/jamesgornall/agent-testing
source .venv/bin/activate
```

### 2. Index Contracts (First Time Only)
```bash
cd contract_review_agent
python index_contracts.py
cd ..
```

### 3. Launch Web Interface
```bash
# Make sure you're in /Users/jamesgornall/agent-testing (the PARENT directory)
adk web
```

### 4. Open Browser
- Go to: **http://localhost:8000**
- Select **"contract_review_agent"** from the dropdown menu
- Start chatting!

## Alternative: CLI Interface

If you prefer command-line interaction:

```bash
cd /Users/jamesgornall/agent-testing
source .venv/bin/activate
adk run contract_review_agent.agent.contract_agent
```

## Common Issues

**"Agent not found in dropdown"**
- Make sure you run `adk web` from `/Users/jamesgornall/agent-testing` (NOT from inside `contract_review_agent/`)

**"Module not found" errors**
- Activate virtual environment: `source .venv/bin/activate`
- Check you're in the right directory

**"No matching clauses found"**
- Index contracts first: `cd contract_review_agent && python index_contracts.py`

## Example Queries to Try

- "Find all non-compete clauses"
- "Show me confidentiality provisions"
- "What does the contract say about intellectual property?"
- "Find termination clauses"
- "Show me liability limitations"
