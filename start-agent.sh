#!/bin/bash
# Launcher script for Contract Review Agent

cd "$(dirname "$0")"

echo "=================================="
echo "Contract Review Agent"
echo "=================================="
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run: python3 -m venv .venv && source .venv/bin/activate && pip install -r contract_review_agent/requirements.txt"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Check if .env exists
if [ ! -f "contract_review_agent/.env" ]; then
    echo "❌ No .env file found!"
    echo "Please create contract_review_agent/.env with your GOOGLE_API_KEY"
    exit 1
fi

# Check if contracts are indexed
if [ ! -d "contract_review_agent/data/chroma_db" ]; then
    echo "📚 Indexing contracts for the first time..."
    cd contract_review_agent
    python index_contracts.py
    cd ..
    echo ""
fi

echo "🚀 Starting Contract Review Agent..."
echo ""
echo "Web interface will be available at: http://localhost:8000"
echo "Select 'contract_review_agent' from the dropdown"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Run adk web from parent directory
adk web
