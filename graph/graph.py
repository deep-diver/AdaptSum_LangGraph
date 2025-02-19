from langgraph.graph import StateGraph

from state import State
from graph.nodes import chatbot, test_edge, test_edge2

def compile_graph():
    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("test_edge", test_edge)
    graph_builder.add_node("test_edge2", test_edge2)
    graph_builder.add_edge("chatbot", "test_edge")
    graph_builder.add_edge("test_edge", "test_edge2")
    graph_builder.set_entry_point("chatbot")
    graph_builder.set_finish_point("test_edge2")

    return graph_builder.compile()