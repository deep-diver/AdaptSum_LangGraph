from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver

from graph import compile_graph

def stream_graph_updates(graph: StateGraph, user_input: str, config: dict):
    messages = [{"role": "user", "content": user_input}]
    
    for event in graph.stream({"messages": messages}, config):
        for value in event.values():
            print(value)
            # if "summary" in value and len(value["summary"]) > 0:
            #     # print(value["summary"])
            #     print("Summary:\n", value["summary"][0])
            # elif "scores" in value:
            #     print("Scores:\n", value["scores"])
            # print("Assistant:", value["messages"][-1].content)

def main():
    memory = MemorySaver()
    graph = compile_graph(memory)
    config = {"configurable": {"thread_id": "1"}}
    
    while True:
        try:
            user_input = input("User: ")
            while not user_input.strip():
                user_input = input("User: ")
                
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(graph, user_input, config)
        except Exception as e:
            break

if __name__ == "__main__":
    main()