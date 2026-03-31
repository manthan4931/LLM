from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.embeddings import get_embeddings

def create_retriever(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings()
    )

    return vectorstore.as_retriever(search_kwargs={"k": 3})