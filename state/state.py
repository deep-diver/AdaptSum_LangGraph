from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages
from graph.types import GradeSummary

class State(TypedDict):
    messages: Annotated[list, add_messages]
    summary: str
    new_summary: str
    scores: GradeSummary
