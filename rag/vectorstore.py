from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.embeddings import get_embeddings

def get_retriever():
    loader = TextLoader("data/knowledge.txt")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings()
    )

    return vectorstore.as_retriever()