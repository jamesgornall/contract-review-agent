# Changes Summary - Contract Review Agent

## Overview
Reorganized project structure to work properly with Google ADK web interface by moving demo contract data outside the project directory.

## Key Changes

### 1. **Data Storage Location**
- **Old**: `contract_review_agent/data/contracts/` (inside project)
- **New**: `~/contract_review_data/contracts/` (outside project, in home directory)
- **Reason**: ADK was scanning subdirectories and treating the data folder as an agent, causing conflicts

### 2. **File Path Updates**
- **contract_search.py**: Updated ChromaDB path to use `~/contract_review_data/chroma_db`
- **index_contracts.py**: Updated contracts path to use `~/contract_review_data/contracts`
- Both now use `os.path.expanduser()` for cross-platform home directory resolution

### 3. **Root Agent File**
- **Added**: `agent.py` at project root
- **Purpose**: Provides a clean entry point for ADK to discover the agent
- Imports from `contract_review_agent` module and exposes `root_agent`

### 4. **Module Initialization**
- **Updated**: `contract_review_agent/__init__.py`
- Now properly exports `root_agent` for module-level access
- Includes `__all__` declaration for clean API

### 5. **Git Ignore Updates**
- Removed references to `contract_review_agent/data/chroma_db/`
- Added note that contract data is stored in `~/contract_review_data/`
- Simplified to just ignore `**/chroma_db/` anywhere

### 6. **Sample Contracts**
- Removed from git tracking (now in `~/contract_review_data/contracts/`)
- Three demo contracts available:
  - sample_employment_contract.txt
  - sample_nda.txt
  - sample_service_agreement.txt

## How to Use

### Initial Setup
```bash
# Index the contracts (creates vector database)
cd contract_review_agent
python index_contracts.py
```

### Launch the Agent
```bash
# From project root
adk web .
```

Then open http://localhost:8000 and select "contract_review_agent" from the dropdown.

## Benefits of New Structure
1. ✅ **ADK Compatibility**: No more data folder conflicts
2. ✅ **Clean Separation**: Code in git, data in home directory
3. ✅ **Portable**: Works across different machines
4. ✅ **Maintainable**: Clear separation of concerns
5. ✅ **Flexible**: Easy to add new contracts without touching code

## Data Location
- **Contracts**: `~/contract_review_data/contracts/`
- **Vector DB**: `~/contract_review_data/chroma_db/`

Both are gitignored and managed separately from the codebase.
