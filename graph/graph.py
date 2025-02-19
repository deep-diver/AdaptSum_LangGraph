from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from state import State
from graph.nodes import chatbot, summarizer # test_edge, test_edge2

def compile_graph(memory: MemorySaver):
    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("summarizer", summarizer)
    graph_builder.add_edge("chatbot", "summarizer")
    graph_builder.set_entry_point("chatbot")
    graph_builder.set_finish_point("summarizer")

    return graph_builder.compile(checkpointer=memory)