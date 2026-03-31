from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("api_key")
)

def plan_task(query):
    prompt=f"""Break the user query into three steps 
    Query:{query}

Steps:
1.
2.
3. 
"""
    response = llm.invoke(prompt)
    return response.content