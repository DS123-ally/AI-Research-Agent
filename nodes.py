import os
from dotenv import load_dotenv

# Load .env from the current script's directory FIRST
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'), override=True)

from ddgs import results
from langchain_core.messages import HumanMessage
from tools import search_tool
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# 1. Generate search queries
def generate_queries(state):
    topic = state["topic"]

    prompt = f"""
    Generate 3 smart search queries for researching this topic:
    {topic}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    queries = [
    q.replace("-", "").replace("1.", "").replace("2.", "").replace("3.", "").strip()
    for q in response.content.split("\n")
    if q.strip()
]

    return {"queries": queries}


# 2. Search node
def search_node(state):
    queries = state["queries"]

    all_results = []

    for q in queries:
        if not q.strip():
            continue

        results = search_tool(q)
        all_results.extend(results)

    # LIMIT RESULTS
    return {"results": all_results[:5]}


# 3. Summarize node
def summarize_node(state):
    topic = state["topic"]
    results = state["results"]

    MAX_CHARS = 4000  # safe limit

    content = ""
    for r in results:
        if len(content) < MAX_CHARS:
            content += r["content"][:500] + "\n\n"

    prompt = f"""
    Summarize the following research for: {topic}

    Give:
    - 5 key insights
    - 3 important facts
    - short conclusion

    Content:
    {content}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"final_report": response.content}