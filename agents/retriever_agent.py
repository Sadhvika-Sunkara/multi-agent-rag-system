import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# Load API key from .env file
load_dotenv()

def build_knowledge_base(text_file_path):
    """
    Load a text file, split into chunks,
    convert to embeddings, store in FAISS
    """
    print(f"📚 Loading document: {text_file_path}")
    
    # Step 1: Read the text file
    with open(text_file_path, 'r') as f:
        text = f.read()
    
    # Wrap in Document object
    documents = [Document(page_content=text)]
    print(f"✅ Loaded document successfully")
    
    # Step 2: Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)
    print(f"✅ Split into {len(chunks)} chunks")
    
    # Step 3: Convert to embeddings + store in FAISS
    print("🔄 Creating embeddings... (this calls OpenAI API)")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    # Step 4: Save to disk
    vectorstore.save_local("data/faiss_index")
    print("✅ Knowledge base built and saved!")
    
    return vectorstore

def retrieve_relevant_chunks(question, k=3):
    """
    Search the knowledge base for 
    the most relevant chunks
    """
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(
        "data/faiss_index", 
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    docs = vectorstore.similarity_search(question, k=k)
    print(f"🔍 Found {len(docs)} relevant chunks")
    return docs

if __name__ == "__main__":
    # Build knowledge base from our sample data
    print("=== Building Knowledge Base ===")
    build_knowledge_base("data/company_knowledge.txt")
    
    print("\n=== Testing Retrieval ===")
    docs = retrieve_relevant_chunks(
        "What is the company revenue?")
    
    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}:")
        print(doc.page_content)