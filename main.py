import os

from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver

from graph import compile_graph

def stream_graph_updates(graph: StateGraph, user_input: str, config: dict):
    messages = [{"role": "user", "content": user_input}]
    
    for event in graph.stream(
        {"messages": messages},
        config
    ):
        for value in event.values():
            if "summary" in value:
                # print(value["summary"])
                print("Summary:\n", value["summary"][0])
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
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)
            stream_graph_updates(graph, user_input, "", config)
            break

if __name__ == "__main__":
    main()