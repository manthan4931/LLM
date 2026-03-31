from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os
from rag.vectorstore import get_retriever

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_rag_chain():
    llm=ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv('api_key')
    )

    prompt = ChatPromptTemplate.from_template(
    """You are a smart AI assistant.

Answer ONLY using the provided context.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""
    )

    chain=(
        {
            "context":get_retriever() | format_docs,
            "question":RunnablePassthrough()
        }
        | prompt| llm
    )

    return chain 