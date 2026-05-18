# 📊 Financial Document Analyzer
### Ask questions about financial documents in plain English — get instant AI-powered answers.

---

## 🤔 What Is This?

Have you ever looked at a company's financial report and felt completely lost?

These documents are usually dozens of pages long, packed with numbers and confusing language. Most people don't have the time or background to read them.

**Financial Document Analyzer solves that.**

You paste in any financial document, and instead of reading the whole thing yourself, you just **ask questions in plain English** — like texting a smart friend who already read it for you.

> **Example:**
> You: *"Is this company doing well?"*
> AI: *"Yes — revenue grew 12% and they beat profit expectations. However, their debt is rising, which is worth watching."*

That's it. No finance degree needed.

---

## ✨ Features

- 🤖 **AI-Powered Analysis** — Uses Claude AI (by Anthropic) to read and understand financial documents for you
- 💬 **Conversational Q&A** — Ask as many follow-up questions as you want, just like a real conversation
- 🧠 **Remembers Context** — It remembers what you already asked, so you don't have to repeat yourself
- 📋 **Auto Summary** — Automatically gives you a structured breakdown the moment you load a document
- 🔒 **Completely Private** — Your document never leaves your computer or gets searched on the internet
- ⚡ **Fast** — Get answers in seconds instead of spending hours reading

---

## 🛠️ Tech Stack

| Layer | What It Is | Plain English Explanation |
|---|---|---|
| **Python** | Programming language | The language the app is written in |
| **Anthropic Claude API** | AI engine | The brain that reads and understands the documents |
| **`anthropic` library** | Python package | The tool that connects Python to the Claude AI |

---

## ✅ Prerequisites

Before you can run this app, you need three things:

1. **Python 3.8 or higher** — the programming language this runs on
   - Check if you have it: open your terminal and type `python --version`
   - Download it at [python.org](https://python.org) if needed

2. **An Anthropic API Key** — this is what lets the app talk to Claude AI
   - Sign up at [console.anthropic.com](https://console.anthropic.com)
   - Go to **API Keys** → click **Create Key**
   - Add a small amount of credit ($5 is plenty for hundreds of uses)
   - Copy your key — it looks like: `sk-ant-api03-xxxxxxxxxx`

3. **A terminal / command prompt** — where you type commands to run the app
   - Windows: search "Command Prompt" in the Start menu
   - Mac: search "Terminal" in Spotlight

---

## 🚀 Getting Started

### Step 1 — Download the project

Click the green **Code** button on this page → **Download ZIP** → unzip it on your computer.

Or if you have Git installed:
```bash
git clone https://github.com/mohc60/financial-document-analyzer.git
cd financial-document-analyzer
```

### Step 2 — Install the required library

Open your terminal, navigate to the project folder, and run:
```bash
pip install anthropic
```

This installs the tool that lets Python talk to Claude AI.

### Step 3 — Add your API key

In your terminal, paste this — replacing the x's with your actual key:

**Windows:**
```bash
set ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxx
```

**Mac / Linux:**
```bash
export ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxx
```

> ⚠️ **Never share your API key with anyone or upload it to GitHub.** Treat it like a password.

### Step 4 — Run the app

```bash
python analyzer.py
```

That's it! The app will start, load a sample financial report, and you can begin asking questions.

---

## 🔑 Environment Variables

| Variable | What It Is | How To Get It |
|---|---|---|
| `ANTHROPIC_API_KEY` | Your personal key to access Claude AI | [console.anthropic.com](https://console.anthropic.com) → API Keys |

---

## 💬 How To Use It

Once the app is running, you'll see an automatic analysis of the document. Then a prompt appears:

```
Your question:
```

Just type any question and press **Enter**. Here are some examples to try:

```
What are the biggest risks for this company?
```
```
How much money did they make?
```
```
Would you recommend this company to an investor?
```
```
Which part of the business is growing the fastest?
```
```
Summarize this in 3 sentences.
```
```
Should I be worried about their debt?
```

To exit the app, type:
```
quit
```

---

## 📁 Project Structure

```
financial-document-analyzer/
│
├── analyzer.py       # Main application file — run this to start the app
└── README.md         # You're reading this!
```

---

## 💡 Example Session

```
============================================================
FINANCIAL DOCUMENT ANALYZER
Powered by Claude AI
============================================================

Document loaded. Running initial analysis...

INITIAL ANALYSIS:
Revenue grew 12% to $4.2B. The technology segment is the
biggest driver of growth at +18%. Debt levels are rising
and worth monitoring...

============================================================
You can now ask specific questions about the document.
Type 'quit' to exit.
============================================================

Your question: Is this company profitable?

ANSWER:
Yes — the company made $890 million in profit this quarter,
which is 8% more than the same time last year. Their profit
margin also improved, meaning they're getting better at
turning revenue into actual profit.

[Tokens used: 312]

Your question:
```

---

## 👨‍💻 About the Developer

**Mohammad Chaudhry**
BS Computer Science & Software Engineering — University of Washington (December 2024)

Built as a portfolio project demonstrating real-world application of large language model APIs, prompt engineering, and conversational AI design.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
