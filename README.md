# AI-Powered Financial Document Analyzer

A Python application that leverages the Claude AI API (Anthropic) to analyze financial documents, extract key insights, and enable interactive Q&A sessions about financial data.

## Features

- **Automated Document Analysis** — Generates executive summaries, extracts key financial metrics, and identifies risks and opportunities
- **Multi-turn Conversational Q&A** — Ask specific questions about any financial document in a natural conversation
- **Context-Aware Responses** — Maintains conversation history for coherent, contextual follow-up answers
- **Finance-Focused System Prompt** — Engineered for accuracy and relevance in financial services contexts

## Tech Stack

- Python 3.x
- Anthropic Claude API (`claude-sonnet-4-20250514`)
- Prompt Engineering — custom system prompt optimized for financial document analysis
- Multi-turn conversation management

## How It Works

1. Load a financial document (earnings report, 10-K, market analysis, etc.)
2. Claude generates an initial comprehensive analysis automatically
3. Ask follow-up questions in natural language
4. Conversation history is maintained for contextual, accurate responses

## Example Use Cases

- Analyzing quarterly earnings reports
- Summarizing 10-K/10-Q filings
- Extracting key metrics from investor presentations
- Comparing financial performance across periods

## Setup

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
python analyzer.py
```

## Sample Output

Given a Q4 earnings report, the analyzer automatically extracts:
- Revenue growth trends and segment performance
- EPS vs analyst estimates
- Balance sheet health indicators
- Forward guidance and key risks
- Management sentiment analysis
