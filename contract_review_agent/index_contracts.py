"""
Utility script to index contract files into the search engine.

Usage:
    python index_contracts.py
    python index_contracts.py path/to/contract.txt
"""
import sys
import os
from pathlib import Path
from contract_search import ContractSearchEngine


def index_all_contracts(contracts_dir: str = os.path.expanduser("~/contract_review_data/contracts")):
    """Index all contract files in the specified directory."""
    search_engine = ContractSearchEngine()
    contracts_path = Path(contracts_dir)

    if not contracts_path.exists():
        print(f"Error: Directory '{contracts_dir}' does not exist")
        return

    # Find all text files
    contract_files = list(contracts_path.glob("*.txt"))

    if not contract_files:
        print(f"No .txt files found in {contracts_dir}")
        return

    print(f"Found {len(contract_files)} contract files")

    total_chunks = 0
    for contract_file in contract_files:
        print(f"\nIndexing: {contract_file.name}")
        chunks = search_engine.index_contract(str(contract_file))
        total_chunks += chunks
        print(f"  ✓ Indexed {chunks} chunks")

    stats = search_engine.get_stats()
    print(f"\n{'='*50}")
    print(f"Indexing complete!")
    print(f"Total chunks indexed: {stats['total_chunks']}")
    print(f"{'='*50}")


def index_single_contract(contract_path: str):
    """Index a single contract file."""
    if not os.path.exists(contract_path):
        print(f"Error: File '{contract_path}' does not exist")
        return

    search_engine = ContractSearchEngine()
    print(f"Indexing: {contract_path}")
    chunks = search_engine.index_contract(contract_path)
    print(f"✓ Indexed {chunks} chunks")

    stats = search_engine.get_stats()
    print(f"\nTotal chunks in database: {stats['total_chunks']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Index specific file
        index_single_contract(sys.argv[1])
    else:
        # Index all contracts in default directory
        index_all_contracts()
