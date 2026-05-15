from langgraph.graph import StateGraph
from typing import TypedDict,List,Dict
from nodes import generate_queries,search_node,summarize_node

## Define State
class AgentState(TypedDict):
    topic: str
    queries: List[str]
    results: List[str]
    final_report: str

##Create Graph

builder=StateGraph(AgentState)

builder.add_node("generate_queries",generate_queries)
builder.add_node("search",search_node)
builder.add_node("summarize",summarize_node)

#Flow
builder.set_entry_point("generate_queries")

builder.add_edge("generate_queries","search")
builder.add_edge("search","summarize")

builder.set_finish_point("summarize")

graph=builder.compile()