from tavily import TavilyClient
import os
from dotenv import load_dotenv

# Load .env from the current script's directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_tool(query:str):
    response= tavily.search(query=query, max_results=5)
    results =[]

    for r in response["results"]:
        results.append({
            "title": r["title"],
            "content": r["content"],
            "url":r["url"]
        }) 
    return results