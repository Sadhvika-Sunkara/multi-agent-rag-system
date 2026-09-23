# 🤖 Multi-Agent RAG System

> Enterprise Knowledge Q&A powered by 3 specialised AI agents

## 🎯 What it does
Ask any business question in plain English and get an AI-powered answer with business recommendations — sourced directly from your company documents.

## 🏗️ Architecture# multi-agent-rag-system


## 🛠️ Tech stack
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=flat)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-blue?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

## 📁 Project structure


## 🚀 How to run
```bash
# Clone the repo
git clone https://github.com/Sadhvika-Sunkara/multi-agent-rag-system.git
cd multi-agent-rag-system

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
echo "OPENAI_API_KEY=your-key-here" > .env

# Build knowledge base
python agents/retriever_agent.py

# Run the web app
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