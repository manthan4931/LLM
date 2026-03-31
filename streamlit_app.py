import streamlit as st
from rag.dynamic_vectorstore import create_retriever
from agents.planner import plan_task
from agents.researcher import research_task
from agents.writer import write_answer , write_answer_strict
from agents.tool_agents import use_tool
from memory.chat_memory import add_to_memory, chat_history
from dotenv import load_dotenv
import tempfile
from rag.document_loader import load_document


load_dotenv()

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("🤖 Multi-Agent AI Assistant")


if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def build_memory():
    history=""
    for chat in st.session_state.chat_history[-5:]:  # last 5 messages
        history += f"User: {chat['user']}\nBot: {chat['bot']}\n"
    return history



uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])

if uploaded_file:
    # 🔥 Reset pointer BEFORE reading
    uploaded_file.seek(0)

    file_bytes = uploaded_file.read()
     # debug

    # preserve correct extension
    file_extension = uploaded_file.name.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}", mode="wb") as tmp_file:
        tmp_file.write(file_bytes)
        file_path = tmp_file.name

    # 🔍 Debug raw file
    

    # 🧠 Load document
    docs = load_document(file_path)

    

    # 🚀 Create retriever
    st.session_state.retriever = create_retriever(docs)

    st.success("Document processed!")
    st.session_state.chat_history = []
else:
    st.session_state.retriever=None
if st.session_state.retriever:
    st.success("Document Mode: Answers only from uploaded file")
else:
    st.info("Normal Mode: Using tools + general knowledge")
memory=build_memory()

query = st.chat_input("Ask something...")

if query:
    doc_mode = st.session_state.retriever is not None

    


    if not doc_mode:
        tool_result = use_tool(query)

        if tool_result:
            response = tool_result
        else:
            context = "No specific document"
            response = write_answer(query, context,memory)

  
    else:
        retriever = st.session_state.retriever
        context = research_task(query, retriever)

        response = write_answer_strict(query, context,memory)

    st.session_state.chat_history.append({
        "user": query,
        "bot": response
    })

# Display chat
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["bot"])

if st.button("Clear Chat"):
    st.session_state.chat_history = []  
