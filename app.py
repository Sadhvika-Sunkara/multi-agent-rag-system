import streamlit as st
import os
from dotenv import load_dotenv
from agents.retriever_agent import (build_knowledge_base,
                                    retrieve_relevant_chunks)
from agents.reasoner_agent import reasoner_agent
from agents.synthesizer_agent import synthesizer_agent

load_dotenv()

# Page config
st.set_page_config(
    page_title="Multi-Agent RAG System",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 Multi-Agent RAG System")
st.caption("Enterprise Knowledge Q&A powered by 3 AI agents")

# Sidebar
with st.sidebar:
    st.header("📚 Knowledge Base")
    st.success("✅ Company knowledge base loaded")
    st.markdown("---")
    st.markdown("### How it works")
    st.markdown("**Agent 1 — Retriever** 🔍")
    st.markdown("Searches documents for relevant information")
    st.markdown("**Agent 2 — Reasoner** 🧠")
    st.markdown("Analyses and extracts key facts")
    st.markdown("**Agent 3 — Synthesizer** ✍️")
    st.markdown("Writes clear business recommendations")
    st.markdown("---")
    st.markdown("### Sample questions")
    st.markdown("- What is the company revenue?")
    st.markdown("- What are the HR policies?")
    st.markdown("- What is the product roadmap?")
    st.markdown("- What cloud infrastructure do we use?")

# Main area
st.markdown("### Ask a question about your company documents")

question = st.text_input(
    "Your question:",
    placeholder="e.g. What is the company revenue in Q1 2026?"
)

if st.button("🚀 Ask the AI Agents", type="primary"):
    if question:
        # Show agent progress
        with st.status("Running 3 AI agents...", expanded=True) as status:
            
            # Agent 1
            st.write("🔍 Agent 1 (Retriever): Searching knowledge base...")
            docs = retrieve_relevant_chunks(question)
            st.write(f"✅ Found {len(docs)} relevant chunks")
            
            # Agent 2
            st.write("🧠 Agent 2 (Reasoner): Analysing information...")
            reasoning = reasoner_agent(question, docs)
            st.write("✅ Analysis complete")
            
            # Agent 3
            st.write("✍️ Agent 3 (Synthesizer): Writing answer...")
            final_answer = synthesizer_agent(question, reasoning)
            st.write("✅ Answer ready")
            
            status.update(label="✅ All agents complete!", 
                         state="complete")
        
        # Show results
        st.markdown("---")
        
        # Final answer
        st.markdown("### 💡 Answer")
        st.info(final_answer)
        
        # Show reasoning in expander
        with st.expander("🧠 See Agent 2 reasoning"):
            st.markdown(reasoning)
            
        # Show retrieved chunks
        with st.expander("📄 See retrieved document chunks"):
            for i, doc in enumerate(docs):
                st.markdown(f"**Chunk {i+1}:**")
                st.text(doc.page_content[:300])
    else:
        st.warning("Please enter a question first!")

# Footer
st.markdown("---")
st.caption("Built with LangChain · OpenAI · FAISS · Streamlit")