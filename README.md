# 🧠 Deep Agent – Research Intelligence System

Deep Agent is an AI-powered research intelligence system that automates the complete research process using multiple specialized agents and AI chains.

It searches the web for relevant information, extracts detailed content from selected sources, generates a structured research report, and then critically evaluates the generated report.

## 🚀 Live Demo

🌐 **[Try Deep Agent – Research Intelligence System](https://deep-agent-research.streamlit.app/)**

---

## ✨ Features

- 🔎 Real-time web research using Tavily
- 🤖 AI-powered Search Agent
- 📖 AI-powered Reader Agent
- 🌐 Web content extraction using BeautifulSoup
- 🧠 Google Gemini for reasoning and generation
- ✍️ Automated research report generation
- 🧐 AI-powered research criticism and evaluation
- 📊 End-to-end research pipeline
- 🖥️ Interactive Streamlit interface
- 🔐 Secure API key management

---

## 🧠 How It Works

Deep Agent follows a multi-stage research workflow instead of generating an answer directly from a single LLM call.

```text
User Research Topic
        │
        ▼
┌─────────────────────┐
│    Search Agent     │
│      Gemini         │
│      Tavily         │
└──────────┬──────────┘
           │
           ▼
     Search Results
           │
           ▼
┌─────────────────────┐
│    Reader Agent     │
│      Gemini         │
│   BeautifulSoup     │
└──────────┬──────────┘
           │
           ▼
    Scraped Content
           │
           ▼
┌─────────────────────┐
│    Writer Chain     │
│                     │
│ Prompt → Gemini     │
│ → Output Parser     │
└──────────┬──────────┘
           │
           ▼
    Research Report
           │
           ▼
┌─────────────────────┐
│    Critic Chain     │
│                     │
│ Prompt → Gemini     │
│ → Output Parser     │
└──────────┬──────────┘
           │
           ▼
    Critic Feedback
