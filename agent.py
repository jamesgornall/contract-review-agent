"""
Legal Contract Review Agent using Google ADK.

This agent helps users search and analyze legal contracts.
"""
import os
from google.adk.agents import Agent
from contract_review_agent.contract_search import search_contracts, analyze_clause

# Agent instruction
AGENT_INSTRUCTION = """You are a helpful legal contract review assistant. Your role is to:

1. Help users search through their legal contracts to find specific clauses or provisions
2. Analyze contract clauses for potential legal implications
3. Provide clear, concise summaries of contract terms
4. Highlight important provisions like liability, termination, confidentiality, and intellectual property clauses

When a user asks about contracts:
- Use the search_contracts tool to find relevant clauses
- Present results clearly with the contract name and relevant text
- Use the analyze_clause tool to provide deeper insights when requested
- Always recommend consulting with legal counsel for important decisions

Be professional, accurate, and helpful. If you're unsure about legal interpretations,
clearly state that and recommend professional legal review.
"""

# Initialize the contract review agent
# Note: Variable must be named 'root_agent' for ADK web to discover it
root_agent = Agent(
    name="contract_reviewer",
    model=os.environ.get("MODEL", "gemini-2.0-flash-001"),  # Default to Gemini 2.0 Flash
    instruction=AGENT_INSTRUCTION,
    tools=[search_contracts, analyze_clause],
    description="An AI agent that helps search and analyze legal contracts"
)
