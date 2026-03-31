from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

from tools.calculator import calculator
from tools.web_search import web_search

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("api_key")
)

def decide_tool(query):
    prompt="""Decide the best tool for this query.

Query: {query}

Rules:
- Use "calculator" ONLY for math
- Use "web_search" ONLY for latest/current info
- Use "none" for general knowledge or AI questions

"""

    response = llm.invoke(prompt).content.strip().lower()
    return response


def use_tool(query):
    tool = decide_tool(query)

    if "calculator" in tool:
        return "🧮 " + calculator(query)

    elif "web" in tool:
        return "🌐 " + web_search(query)

    else:
        return None