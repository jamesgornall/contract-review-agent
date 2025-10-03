#!/bin/bash
# Quick start script for Contract Review Agent

set -e

echo "=================================="
echo "Contract Review Agent Quick Start"
echo "=================================="
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found!"
    echo "Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "📝 Please edit .env and add your GOOGLE_API_KEY"
    echo "   Get your API key from: https://makersuite.google.com/app/apikey"
    echo ""
    echo "After adding your API key, run this script again."
    exit 1
fi

# Check if API key is set
if grep -q "your_google_api_key_here" .env; then
    echo "⚠️  Please set your GOOGLE_API_KEY in the .env file"
    echo "   Edit .env and replace 'your_google_api_key_here' with your actual API key"
    echo "   Get your API key from: https://makersuite.google.com/app/apikey"
    exit 1
fi

echo "✓ Environment configured"
echo ""

# Check if contracts are indexed
if [ ! -d "data/chroma_db" ]; then
    echo "📚 Indexing sample contracts..."
    python index_contracts.py
    echo ""
else
    echo "✓ Contracts already indexed"
    echo ""
fi

echo "=================================="
echo "🚀 Starting ADK Web Interface..."
echo "=================================="
echo ""
echo "The web interface will open at: http://localhost:8000"
echo ""
echo "Try these example queries:"
echo "  • 'Find all non-compete clauses'"
echo "  • 'Show me confidentiality provisions'"
echo "  • 'What does the contract say about IP rights?'"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start ADK web interface
adk web
