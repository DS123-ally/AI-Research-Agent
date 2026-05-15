from graph import graph

def run_agent(topic):
    result = graph.invoke({"topic":topic})
    return result["final_report"]

if __name__ == "__main__":
    print("AI Research Agent")
    topic=input("Enter a research topic: ")
    report=run_agent(topic)
    
    print("\nFinal Report:\n")
    print(report)
