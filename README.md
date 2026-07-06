# Retention Risk Agent

A Cognee-powered AI agent that analyzes customer behavior patterns and identifies at-risk accounts before they churn.

## Problem

Customer support teams at fintech companies spend hours manually reviewing customer data to identify who might leave. By then, it's often too late. Traditional systems see each customer interaction in isolation; they forget context.

**This agent remembers.** It ingests customer support tickets, usage patterns, and payment history, builds a knowledge graph of relationships between these signals, and flags accounts showing churn risk with reasoning.

## How It Works

1. **Ingest** — Feed customer records into Cognee
2. **Remember** — Cognee builds a graph connecting patterns (e.g., "failed payment" → "support ticket" → "account downgrade")
3. **Analyze** — Ask the agent, "Which customers are at risk?" 
4. **Output** — Get a prioritized list with reasons (e.g., "Kwame: usage dropped 80%, ignoring check-in emails")

## Tech Stack

- **Cognee** — Graph + vector memory layer
- **Google Gemini API** — LLM for reasoning
- **Python** — Core logic
- **SQLite** — Local persistence

## Installation

```bash
pip install cognee
cp .env.example .env
# Add your Gemini API key to .env
python retention_agent.py
```

## Example Output
