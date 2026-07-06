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
CUSTOMER RETENTION RISK REPORT
WARNING: Kwame: Usage dropped by 80% in the last month; he downgraded his plan, and he has not responded to two check-in emails.
WARNING: Ngozi complained twice about slow customer support response times, is considering switching to a competitor, and her last login was 10 days ago.
WARNING: Amara: Stopped logging in for two weeks, reported an unresolved app-crashing bug, and has not received a support reply for five days.

## Why This Matters

In my previous roles, I saw support teams react *after* customers left. This agent flips that — it gives teams *predictive* warnings so they can act first. With memory, patterns that were invisible before (like "this customer complained twice in a month") become signals the AI can connect and reason about.

## What I Learned

- **Memory is everything in AI.** A generic LLM sees isolated facts. With Cognee's graph memory, the same LLM can reason across time and relationships.
- **Beginners can build AI agents.** I started not knowing Python well, but AI-assisted development (using Claude) let me focus on the problem, not syntax.
- **Context is the hardest part.** The real work wasn't the code — it was figuring out what signals matter for churn risk. That domain knowledge (from Quidax) was invaluable.

## Next Steps

- [ ] Expand to real customer data
- [ ] Add automatic alerting (Slack, email)
- [ ] Build a web UI for non-technical support teams
