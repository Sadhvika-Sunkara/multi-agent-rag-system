# 🤖 Multi-Agent RAG System

> Enterprise Knowledge Q&A powered by 3 specialised AI agents

## 🎯 What it does
Ask any business question in plain English and get an AI-powered answer with business recommendations — sourced directly from your company documents.

## 🏗️ Architecture

User Question
↓
Agent 1 — Retriever 🔍
Searches FAISS vector database for relevant chunks
↓
Agent 2 — Reasoner 🧠
Analyses chunks, extracts key facts, rates confidence
↓
Agent 3 — Synthesizer ✍️
Writes clear business recommendation
↓
Final Answer 💡


## 🛠️ Tech stack
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=flat)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-blue?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

## 📁 Project structure

    multi-agent-rag-system/
    ├── agents/
    │   ├── retriever_agent.py    ← Agent 1: searches vector DB
    │   ├── reasoner_agent.py     ← Agent 2: analyses facts
    │   └── synthesizer_agent.py  ← Agent 3: writes recommendations
    ├── data/
    │   ├── company_knowledge.txt ← knowledge base document
    │   └── faiss_index/          ← vector database
    ├── app.py                    ← Streamlit web interface
    ├── main.py                   ← CLI pipeline runner
    └── requirements.txt

## 🚀 How to run

```bash
git clone https://github.com/Sadhvika-Sunkara/multi-agent-rag-system.git
cd multi-agent-rag-system
pip install -r requirements.txt
echo "OPENAI_API_KEY=your-key-here" > .env
python agents/retriever_agent.py
streamlit run app.py
```

## 💡 Sample questions
- "What is the company revenue?"
- "What are the HR policies?"
- "What is the product roadmap for 2026?"

## 📊 Results
- 3 specialised agents working in pipeline
- Sub-5 second response time
- Transparent reasoning with confidence scoring
- Honest uncertainty flagging