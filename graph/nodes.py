from langchain_google_genai import ChatGoogleGenerativeAI
from state import State

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def chatbot(state: State):
    msg = llm.invoke(state["messages"])
    return {"messages": [msg]}

def test_edge(state: State):
    return {"summary": "hello"}

def test_edge2(state: State):
    print(state)
    return {"summary": "hello2"}