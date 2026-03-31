from rag.vectorstore import get_retriever
from agents.planner import plan_task
from agents.researcher import research_task
from agents.writer import write_answer
from dotenv import load_dotenv
import os 
from memory.chat_memory import *
from agents.tool_agents import *
load_dotenv()

print("DEBUG KEY:", os.getenv("api_key"))

retriever = get_retriever()

while True:
    query = input("\nAsk: ")

    if query.lower() in ["exit", "quit"]:
        break
    tool_result= use_tool(query)

    if tool_result and "No Result" not in tool_result:
        print("\n Tool Used:",tool_result)
        add_to_memory(query,tool_result)
        continue

    print("\n🧭 Planning...")
    plan = plan_task(query)
    print(plan)

    print("\n🔎 Researching...")
    context = research_task(query, retriever)

    print("\n✍️ Writing answer...")
    answer = write_answer(query, context)

    print("\n🤖 Final Answer:\n", answer)

    add_to_memory(query,answer)
