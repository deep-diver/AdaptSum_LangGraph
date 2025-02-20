from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from state import State
from graph.nodes import chatbot, summarizer, summary_grader # test_edge, test_edge2
from graph.edges import summary_grader_edge

def compile_graph(memory: MemorySaver):
    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("summarizer", summarizer)
    graph_builder.add_node("summary_grader", summary_grader)
    graph_builder.add_edge("chatbot", "summarizer")
    graph_builder.add_edge("summarizer", "summary_grader")
    graph_builder.add_conditional_edges(
        "summary_grader",
        summary_grader_edge,
        {
            "qualified": END,
            "unqualified": "summary_grader"
        }
    )
    graph_builder.set_entry_point("chatbot")
    return graph_builder.compile(checkpointer=memory)