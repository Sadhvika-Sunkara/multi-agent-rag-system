import os
from dotenv import load_dotenv
from agents.retriever_agent import (build_knowledge_base, 
                                    retrieve_relevant_chunks)
from agents.reasoner_agent import reasoner_agent
from agents.synthesizer_agent import synthesizer_agent

load_dotenv()

def run_multi_agent_pipeline(question):
    """
    Orchestrates all 3 agents to answer
    a business question
    """
    print(f"\n{'='*60}")
    print(f"QUESTION: {question}")
    print(f"{'='*60}")
    
    # Agent 1: Retrieve
    print("\n🔍 Agent 1 (Retriever): Searching knowledge base...")
    docs = retrieve_relevant_chunks(question)
    
    # Agent 2: Reason
    print("\n🧠 Agent 2 (Reasoner): Analysing information...")
    reasoning = reasoner_agent(question, docs)
    
    # Agent 3: Synthesize
    print("\n✍️  Agent 3 (Synthesizer): Writing answer...")
    final_answer = synthesizer_agent(question, reasoning)
    
    print(f"\n{'='*60}")
    print("💡 FINAL ANSWER:")
    print(f"{'='*60}")
    print(final_answer)
    
    return {
        'question': question,
        'retrieved_docs': len(docs),
        'reasoning': reasoning,
        'answer': final_answer
    }

if __name__ == "__main__":
    # Test with multiple questions
    questions = [
        "What is the company revenue?",
        "What are the HR policies?",
        "What is the product roadmap for 2026?"
    ]
    
    for question in questions:
        run_multi_agent_pipeline(question)
        print("\n")