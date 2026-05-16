import anthropic
import json
from datetime import datetime

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a financial document analyst assistant. Your role is to help users understand financial documents, reports, earnings calls, and market data.

When analyzing documents you will:
1. Provide a concise executive summary
2. Extract key financial metrics and figures
3. Identify risks and opportunities
4. Answer specific questions about the document clearly and accurately
5. Always cite specific sections or data points from the document when making claims

Respond in clear, professional language suitable for a financial services context."""

def analyze_document(document_text: str, query: str = None) -> dict:
    """Analyze a financial document and optionally answer a specific query."""
    
    if query:
        user_message = f"""Please analyze the following financial document and specifically answer this question: {query}

Document:
{document_text}"""
    else:
        user_message = f"""Please provide a comprehensive analysis of the following financial document, including:
- Executive summary
- Key financial metrics
- Notable risks and opportunities
- Key takeaways

Document:
{document_text}"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}]
    )
    
    return {
        "analysis": response.content[0].text,
        "tokens_used": response.usage.input_tokens + response.usage.output_tokens,
        "timestamp": datetime.now().isoformat()
    }

def chat_with_document(document_text: str) -> None:
    """Interactive chat session about a financial document."""
    print("\n" + "="*60)
    print("FINANCIAL DOCUMENT ANALYZER")
    print("Powered by Claude AI")
    print("="*60)
    print("\nDocument loaded. Running initial analysis...\n")
    
    # Initial analysis
    result = analyze_document(document_text)
    print("INITIAL ANALYSIS:")
    print("-"*40)
    print(result["analysis"])
    print(f"\n[Tokens used: {result['tokens_used']}]")
    
    # Conversation history for multi-turn chat
    conversation_history = [
        {
            "role": "user",
            "content": f"Here is the financial document I want to discuss:\n\n{document_text}"
        },
        {
            "role": "assistant", 
            "content": result["analysis"]
        }
    ]
    
    print("\n" + "="*60)
    print("You can now ask specific questions about the document.")
    print("Type 'quit' to exit.")
    print("="*60)
    
    while True:
        user_input = input("\nYour question: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nSession ended. Thank you for using the Financial Document Analyzer.")
            break
            
        if not user_input:
            continue
        
        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Get response maintaining conversation context
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=conversation_history
        )
        
        assistant_response = response.content[0].text
        
        # Add assistant response to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_response
        })
        
        print("\nANALYSIS:")
        print("-"*40)
        print(assistant_response)
        print(f"\n[Tokens used: {response.usage.input_tokens + response.usage.output_tokens}]")

# Sample financial document for demonstration
SAMPLE_DOCUMENT = """
ACME CORPORATION - Q4 2024 EARNINGS REPORT

Financial Highlights:
- Total Revenue: $4.2B (up 12% YoY)
- Net Income: $890M (up 8% YoY)  
- Earnings Per Share (EPS): $3.42 (beat analyst estimate of $3.15)
- Operating Margin: 21.2% (vs 20.1% prior year)
- Free Cash Flow: $1.1B

Segment Performance:
- Technology Solutions: $2.1B revenue (+18% YoY) — strongest growth driver
- Financial Services: $1.4B revenue (+7% YoY) — steady growth
- Consumer Products: $700M revenue (-2% YoY) — headwinds from inflation

Balance Sheet:
- Cash and equivalents: $3.2B
- Total debt: $5.8B
- Debt-to-equity ratio: 1.4x (up from 1.2x prior year)

Guidance for Q1 2025:
- Revenue: $4.0B - $4.3B
- EPS: $3.20 - $3.40

Key Risks:
- Rising interest rates increasing debt service costs
- Supply chain disruptions in Consumer Products segment
- Increased competition in Technology Solutions market
- FX headwinds expected to impact international revenue by ~3%

Management Commentary:
CEO Jane Smith: "Our strong Q4 results reflect the resilience of our diversified business model. 
While we face macroeconomic headwinds, our Technology Solutions segment continues to outperform, 
and we remain confident in our ability to deliver sustainable long-term value for shareholders."
"""

if __name__ == "__main__":
    print("Loading sample Q4 earnings report...")
    chat_with_document(SAMPLE_DOCUMENT)
