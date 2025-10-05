"""
Contract search tool using ChromaDB and sentence transformers for semantic search.
"""
import os
from typing import List, Dict
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


class ContractSearchEngine:
    """Semantic search engine for legal contracts."""

    def __init__(self, persist_directory: str = os.path.expanduser("~/contract_review_data/chroma_db")):
        """Initialize the search engine with ChromaDB."""
        self.persist_directory = persist_directory
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(path=persist_directory)

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name="contracts",
            metadata={"description": "Legal contract clauses and sections"}
        )

    def index_contract(self, contract_path: str, contract_name: str = None):
        """
        Index a contract file into the search engine.

        Args:
            contract_path: Path to the contract file
            contract_name: Optional name for the contract (defaults to filename)
        """
        if contract_name is None:
            contract_name = os.path.basename(contract_path)

        with open(contract_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split contract into chunks (paragraphs or sections)
        chunks = self._split_into_chunks(content)

        # Prepare data for ChromaDB
        documents = []
        metadatas = []
        ids = []

        for i, chunk in enumerate(chunks):
            if chunk.strip():  # Skip empty chunks
                documents.append(chunk)
                metadatas.append({
                    "contract_name": contract_name,
                    "chunk_id": i,
                    "source": contract_path
                })
                ids.append(f"{contract_name}_{i}")

        if documents:
            # Add to collection (ChromaDB automatically handles embeddings)
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            return len(documents)
        return 0

    def _split_into_chunks(self, text: str, chunk_size: int = 500) -> List[str]:
        """
        Split text into semantic chunks.

        Args:
            text: The contract text
            chunk_size: Approximate size of each chunk in characters

        Returns:
            List of text chunks
        """
        # Split by double newlines (paragraphs) first
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = ""

        for para in paragraphs:
            if len(current_chunk) + len(para) < chunk_size:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Search for relevant contract clauses.

        Args:
            query: Search query or question
            top_k: Number of results to return

        Returns:
            List of matching contract sections with metadata
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        # Format results
        matches = []
        if results['documents'] and results['documents'][0]:
            for i, doc in enumerate(results['documents'][0]):
                match = {
                    "text": doc,
                    "contract_name": results['metadatas'][0][i]['contract_name'],
                    "source": results['metadatas'][0][i]['source'],
                    "distance": results['distances'][0][i] if 'distances' in results else None
                }
                matches.append(match)

        return matches

    def get_stats(self) -> Dict:
        """Get statistics about indexed contracts."""
        count = self.collection.count()
        return {
            "total_chunks": count,
            "collection_name": self.collection.name
        }


# Tool functions for ADK agent
def search_contracts(query: str, top_k: int = 5) -> dict:
    """
    Search through indexed legal contracts for relevant clauses.

    Use this tool when the user asks to find specific clauses, terms, or provisions
    in contracts. For example: "Find non-compete clauses" or "Show confidentiality terms".

    Args:
        query: The search query describing what to find in the contracts
        top_k: Number of most relevant results to return (default: 5)

    Returns:
        A dictionary containing search results with contract excerpts and metadata
    """
    try:
        search_engine = ContractSearchEngine()
        results = search_engine.search(query, top_k=top_k)

        if not results:
            return {
                "status": "success",
                "message": "No matching clauses found",
                "results": []
            }

        return {
            "status": "success",
            "query": query,
            "results": results,
            "count": len(results)
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Search failed: {str(e)}"
        }


def analyze_clause(clause_text: str, analysis_type: str = "general") -> dict:
    """
    Analyze a specific contract clause for legal implications.

    Use this tool when the user wants deeper analysis of a particular clause
    or contract provision. Analysis types: 'general', 'risk', 'compliance'.

    Args:
        clause_text: The text of the clause to analyze
        analysis_type: Type of analysis ('general', 'risk', or 'compliance')

    Returns:
        A dictionary with analysis results and recommendations
    """
    # This is a simplified analysis - in production you'd use LLM for deeper analysis
    analysis = {
        "status": "success",
        "clause_text": clause_text[:200] + "..." if len(clause_text) > 200 else clause_text,
        "analysis_type": analysis_type
    }

    # Basic keyword-based insights
    keywords = {
        "liability": ["liability", "indemnify", "indemnification", "damages"],
        "termination": ["terminate", "termination", "cancel", "cancellation"],
        "confidentiality": ["confidential", "proprietary", "trade secret"],
        "non_compete": ["non-compete", "non compete", "competitive", "competition"],
        "ip_rights": ["intellectual property", "copyright", "trademark", "patent"]
    }

    found_topics = []
    for topic, terms in keywords.items():
        if any(term.lower() in clause_text.lower() for term in terms):
            found_topics.append(topic)

    analysis["topics_identified"] = found_topics if found_topics else ["general_contract_terms"]
    analysis["recommendation"] = "Review this clause with legal counsel for specific implications."

    return analysis
