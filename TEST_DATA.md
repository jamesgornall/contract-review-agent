# Test Data - Contract Review Agent

## Overview
This document describes the test contract data available for the Contract Review Agent.

## Data Location
All contract files are stored in: `~/contract_review_data/contracts/`

This location is outside the git repository to keep demo data separate from the codebase.

## Test Contracts Summary

### Total Contracts: 33
- **30 Qodea Professional Services Contracts** (QODEA_001 to QODEA_030)
- **3 Original Sample Contracts** (Employment, NDA, Service Agreement)

### Vector Database
- **Total chunks indexed**: 374
- **Database location**: `~/contract_review_data/chroma_db/`

## Qodea Contract Distribution

### By Contract Type
- **Fixed Resource**: 10 contracts
  - Dedicated team members/FTEs allocated for defined period
  - Examples: QODEA_001, QODEA_004, QODEA_007, etc.

- **Fixed Deliverable**: 10 contracts
  - Agreed scope with defined outcomes and acceptance criteria
  - Examples: QODEA_002, QODEA_006, QODEA_009, etc.

- **Time & Materials**: 10 contracts
  - Hourly/daily rates with estimated hours
  - Examples: QODEA_003, QODEA_005, QODEA_008, etc.

### By Working Location
- **UK Only**: 10 contracts (all work from UK offices/sites)
- **Remote Only**: 10 contracts (fully distributed)
- **Hybrid**: 10 contracts (mix of on-site and remote)

### By Industry Sector
- **Retail**: 10 contracts
  - Includes PCI-DSS compliance, e-commerce, high availability
  - Examples: Albion Retail, Elite Fashion, Value Supermarkets, etc.

- **Finance**: 10 contracts
  - Includes FCA regulations, data residency, SOC 2 compliance
  - Examples: Sterling Bank, Premier Asset Management, Capital Insurance, etc.

- **Public Sector**: 10 contracts
  - Includes G-Cloud, GDS standards, accessibility (WCAG)
  - Examples: Westminster Council, NHS Trusts, Department for Education, etc.

### Contract Values
- **Range**: £66,000 to £498,000
- **Total aggregate value**: ~£8.2 million
- **Average**: ~£273,000 per contract

### Duration Range
- **Shortest**: 3 months
- **Longest**: 12 months
- **Average**: 7-8 months

## Google Cloud Services Referenced

Contracts include various Google Cloud Platform services:
- Google Kubernetes Engine (GKE)
- BigQuery & BigQuery ML
- Cloud Run
- Vertex AI (Vision, Recommendations, Predictions)
- Cloud Storage & CDN
- Cloud Spanner
- Cloud Functions
- Dataflow & Pub/Sub
- Cloud IoT Core
- Document AI
- Looker
- Cloud Composer (Airflow)
- Firebase
- Cloud Healthcare API
- Apigee
- Anthos

## Compliance & Regulations

### Retail Sector
- PCI-DSS (Levels 1 & 2)
- GDPR
- Food Safety Authority (FSA) standards
- High availability SLAs (99.95% - 99.99%)

### Finance Sector
- FCA (Financial Conduct Authority) regulations
- PRA (Prudential Regulation Authority) standards
- MiFID II, Basel III, Solvency II
- SOC 2 Type II, ISO 27001
- PSD2, AML/CTF compliance
- Open Banking standards

### Public Sector
- G-Cloud 13 framework
- GDS (Government Digital Service) standards
- WCAG 2.1 AA accessibility
- Government Security Classifications (OFFICIAL to SECRET)
- NHS Data Security & Protection Toolkit (DSPT)
- Clinical Safety (DCB0129/0160)
- Freedom of Information Act
- IR35 compliance

## Example Queries to Test

### By Contract Type
- "Find all Fixed Resource contracts"
- "Show me Time & Materials agreements"
- "Which contracts are Fixed Deliverable?"

### By Industry
- "Find all retail sector contracts"
- "Show me finance contracts with FCA compliance"
- "Which public sector contracts mention NHS?"

### By Compliance
- "Find contracts with PCI-DSS requirements"
- "Show me contracts requiring SOC 2 compliance"
- "Which contracts mention GDPR?"

### By Technology
- "Find contracts using BigQuery"
- "Show me contracts with Vertex AI"
- "Which contracts use GKE?"

### By Value/Duration
- "Find contracts over £300,000"
- "Show me contracts longer than 9 months"
- "Which contracts are for 6 months or less?"

### By Working Model
- "Find all UK Only contracts"
- "Show me remote-only agreements"
- "Which contracts are hybrid working?"

## Regenerating Test Data

To recreate the test contracts:

1. **Clear existing data** (optional):
   ```bash
   rm -rf ~/contract_review_data/contracts/QODEA_*
   rm -rf ~/contract_review_data/chroma_db/*
   ```

2. **Generate new contracts**: Use the contract generation agent to create 30 diverse contracts

3. **Reindex**:
   ```bash
   cd contract_review_agent
   python index_contracts.py
   ```

## Notes
- All contracts are realistic but fictional - generated for testing purposes only
- Contract data is gitignored and stored locally
- Each contract includes comprehensive legal terms and industry-specific requirements
- Vector database is regenerated when contracts are reindexed
