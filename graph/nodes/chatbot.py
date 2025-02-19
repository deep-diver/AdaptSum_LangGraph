from state import State
from .utils import llm

def chatbot(state: State):
    msg = llm.invoke(state["messages"])
    return {"messages": [msg]}