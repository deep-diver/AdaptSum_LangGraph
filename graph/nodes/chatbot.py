from state import State
from .llms import llm

def chatbot(state: State):
    msg = llm.invoke(state["messages"])
    if "new_summary" in state:
        print("---chatbot(NEW SUMMARY FOUND)---")
        return {"messages": [msg], "summary": [state["new_summary"]]}
    else:
        print("---chatbot(NO NEW SUMMARY FOUND)---")
        return {"messages": [msg]}
