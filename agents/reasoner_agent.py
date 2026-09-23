import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def reasoner_agent(question, retrieved_docs):
    """
    Takes retrieved chunks and analyses them
    to identify key facts and confidence level
    """
    # Combine all retrieved chunks into context
    context = "\n\n".join([doc.page_content 
                           for doc in retrieved_docs])
    
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    prompt = f"""You are a careful analyst. 
    
Retrieved information:
{context}

Question: {question}

Analyse the retrieved information and provide:
1. KEY FACTS: List the most relevant facts
2. CONFIDENCE: Rate your confidence (High/Medium/Low)
3. GAPS: What information is missing?

Be analytical and precise."""

    print("🧠 Reasoner Agent analysing...")
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    # Test the reasoner
    from retriever_agent import retrieve_relevant_chunks
    
    question = "What is the company revenue and top region?"
    docs = retrieve_relevant_chunks(question)
    
    analysis = reasoner_agent(question, docs)
    print("\n=== REASONER OUTPUT ===")
    print(analysis)