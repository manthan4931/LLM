from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader



def load_document(file_path):

    text = ""

    # 📄 PDF
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        text = "\n".join([d.page_content for d in docs])

    # 📝 TXT (SAFE MANUAL READ)
    elif file_path.endswith(".txt"):
        with open(file_path, "rb") as f:
            raw = f.read()

        # decode safely
        text = raw.decode("utf-8", errors="ignore")

    else:
        raise ValueError("Unsupported file type")

    # 🧠 CLEAN TEXT
    text = text.strip()

    # 🚨 CRITICAL CHECK
    if not text:
        raise ValueError("File is empty or unreadable")

    return [Document(page_content=text)]