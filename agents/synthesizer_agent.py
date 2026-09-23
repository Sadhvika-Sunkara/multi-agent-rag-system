import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def synthesizer_agent(question, reasoning):
    """
    Takes the reasoner's analysis and writes
    a clear business recommendation
    """
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)
    
    prompt = f"""You are a clear business communicator 
writing for a non-technical executive.

Analysis provided:
{reasoning}

Original question: {question}

Write a response that:
1. Answers the question directly in 1-2 sentences
2. Gives one specific business recommendation
3. Flags any uncertainty honestly

Keep it concise and actionable."""

    print("✍️ Synthesizer Agent writing response...")
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    # Test the full pipeline
    from retriever_agent import retrieve_relevant_chunks
    from reasoner_agent import reasoner_agent
    
    question = "What is the company revenue and what should we focus on?"
    
    print("=== FULL 3-AGENT PIPELINE TEST ===\n")
    
    print("Step 1: Retrieving relevant information...")
    docs = retrieve_relevant_chunks(question)
    
    print("\nStep 2: Reasoning about the information...")
    reasoning = reasoner_agent(question, docs)
    
    print("\nStep 3: Synthesizing final answer...")
    final_answer = synthesizer_agent(question, reasoning)
    
    print("\n" + "="*50)
    print("FINAL ANSWER:")
    print("="*50)
    print(final_answer)