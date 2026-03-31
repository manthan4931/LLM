from langchain_groq import ChatGroq
import os


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("api_key")
)

def write_answer(query, context,memory):
    
    
    prompt = f"""
You are an smart ai assistant. Use the conversation history and context to answer the question.

Conversation History:
{memory}

Context:
{context}

Question:
{query}

Give a helpful and conceptual answer
"""
    response = llm.invoke(prompt)
    return response.content

def write_answer_strict(query, context,memory):
    prompt = f"""
Conversation History:
{memory}

Context:
{context}

Question:
{query}

You are a document-based AI assistant.

Answer ONLY using the provided document context.

Rules:
- Do NOT use outside knowledge
- If answer is not in document → say "Not found in document"

Context:
{context}

Question:
{query}
"""
    response = llm.invoke(prompt)
    return response.content